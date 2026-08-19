# Computer Troubleshooting Guide

A practical reference for common desktop and laptop problems.

## The machine will not turn on

If nothing happens at all when you press the power button — no lights, no fan noise, no sound — the machine is not receiving power. Check the wall socket with a different device first, then check the power cable at both ends. On a laptop, remove the battery if it is removable and try running on mains power alone.

A charger that has failed will often look completely normal. If the charging light does not come on when you plug it in, borrow a known-good charger of the same wattage before assuming the machine is dead.

## The machine powers on but the screen stays black

Listen for the fan. If the fan spins and lights come on but nothing appears on screen, the computer is running and the problem is the display path rather than the machine itself. Shine a torch at the screen at an angle — if you can faintly see the desktop, the backlight has failed rather than the panel.

On a desktop, check that the monitor cable is seated at both ends and that the monitor is set to the correct input. A monitor left on the wrong input source shows exactly the same black screen as a broken graphics card.

## Forcing a shutdown

Hold the power button down for ten seconds. The machine will cut power regardless of what the operating system is doing. This is safe to do when the computer is frozen, but any unsaved work is lost, so use it only when nothing else responds.

After a forced shutdown, wait about thirty seconds before pressing power again. Some laptops need that time to fully discharge before they will start.

## The fan is very loud

A loud fan means the machine is trying to cool itself. The most common cause is dust blocking the vents. Compressed air, used in short bursts with the machine switched off, clears most of it. Do not spin the fan blades with the air jet — hold them still with a cocktail stick while you spray.

The second most common cause is a single process using all of the processor. Open the task manager and sort by CPU usage. A browser tab playing video in the background is a frequent culprit.

If the fan is loud and the case is hot to the touch even at idle, the thermal paste between the processor and its heatsink may have dried out. Replacing it is straightforward on a desktop and awkward on a laptop.

## The computer is slow

Slowness has three usual causes: a full disk, insufficient memory, or a failing drive. Check free disk space first — a drive with less than ten percent free will slow down noticeably, because the operating system has no room to work.

If disk space is fine, open the task manager and look at memory usage. A machine that is constantly at ninety percent memory is swapping to disk, which is many times slower than RAM.

A drive that is physically failing produces a distinctive pattern: the machine freezes for several seconds at a time, then recovers. Check the drive health with the manufacturer's diagnostic tool before replacing anything else.

## Wi-Fi will not connect

Restart the router before touching the computer. Unplug it, wait thirty seconds, plug it back in and give it two minutes to come back up. This resolves a surprising proportion of connection problems.

If other devices connect fine and only one machine cannot, the problem is on that machine. Forget the network in the Wi-Fi settings and reconnect from scratch, entering the password again. A saved network with a stale password fails silently.

Check whether the machine connects when standing next to the router. If it does, the problem is range or interference rather than configuration. Microwave ovens and cordless phones both interfere with the 2.4 GHz band.

## The keyboard is not responding

On a laptop, try an external USB keyboard. If that works, the internal keyboard or its ribbon cable has failed. If neither keyboard works, the machine has frozen even though the screen may still look normal.

Liquid damage often shows up as a few keys failing rather than the whole keyboard. Anything spilled should be dealt with immediately: power off, unplug, turn the machine upside down, and leave it to dry for at least forty-eight hours before trying again.

## Resetting a forgotten password

You cannot recover a Windows or macOS password, only reset it. On Windows, a Microsoft account password is reset through the account recovery page on another device. A local account requires the installation media and a recovery command prompt.

On macOS, restart holding Command and R to enter recovery mode, then use the password reset utility. You will need the Apple ID associated with the machine.

Resetting a password does not give access to files encrypted with that password. BitLocker and FileVault both require the recovery key, which is stored in your Microsoft or Apple account if you set it up through the normal process.

## Cleaning a mechanical keyboard

Unplug the keyboard first. Turn it upside down and shake out the loose debris, then use compressed air between the keys. This is enough for routine cleaning.

For a deeper clean, remove the keycaps with a keycap puller — pulling them off with fingers or a screwdriver risks breaking the switch stems. The caps can be washed in warm soapy water and left to dry completely. Never put the keyboard body in water.

## Backing up before any repair

Any repair carries some risk of data loss, so copy anything irreplaceable to an external drive or cloud storage before starting. This applies especially to drive diagnostics, which can push an already failing drive over the edge.

A backup that has never been tested is not a backup. Open a few files from the copy and confirm they actually work before you rely on it.
