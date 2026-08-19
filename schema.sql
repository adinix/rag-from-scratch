CREATE TABLE documents(
    id SERIAL PRIMARY KEY,     
    title TEXT, 
    source TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE chunks(
    id SERIAL PRIMARY KEY,
    content TEXT,
    chunk_index INTEGER,
    page_number INTEGER,
    embedding VECTOR(1536),
    document_id INTEGER REFERENCES documents(id) ON DELETE CASCADE
);
