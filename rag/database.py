import psycopg2
from pgvector.psycopg2 import register_vector
import numpy as np
from abc import ABC, abstractmethod

class Store(ABC):
    
    @abstractmethod
    def add_doc(self, title, source):
        pass
    
    @abstractmethod
    def add_chunks(self, document_id, texts, embeddings):
        pass
    
    @abstractmethod
    def searching(self, embed_ques, limit):
        pass
    
    
class PgVector(Store):
    def __init__(self, host, port, dbname, user, password):
        self.conn = psycopg2.connect(
            host = host,
            port = port,
            dbname = dbname,
            user = user,
            password = password 
        )
        register_vector(self.conn)
        
    def add_doc(self, title, source):
            with self.conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO documents (title, source) VALUES (%s, %s) RETURNING id",(title, source),
                )
                document_id = cur.fetchone()[0]
            self.conn.commit()
            return document_id
    
    def add_chunks(self, document_id, texts, embeddings):
        with self.conn.cursor() as cur:
            for i in range(len(embeddings)):
                cur.execute(
                    "INSERT INTO chunks (content, embedding, chunk_index, document_id) VALUES (%s, %s, %s, %s)", (texts[i], np.array(embeddings[i]), i, document_id),
                )
        self.conn.commit()
            
    def searching(self, embed_ques, limit):
        with self.conn.cursor() as cur:
            cur.execute(
                "SELECT content, chunk_index, document_id, embedding <=> %s AS distance "
                "FROM chunks "
                "ORDER BY embedding <=> %s "
                "LIMIT %s", 
                (np.array(embed_ques),np.array(embed_ques), limit)
            )
            return cur.fetchall()
