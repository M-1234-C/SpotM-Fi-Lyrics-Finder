# SpotM-Fi-Lyrics-Finder
A external app for SpotM-Fi that lets you find the lyrics for the song you want with time stamps 

# But what actually is it ?
Its a lightweight, command-line Python utility that searches for song lyrics, extracts their timing data, reformats the timestamps into a clean `[minute:second]` format, and exports them directly to text files. This runs i a clean loop so you can get all you lyrics in one go and just add them into SpotM-fi

## Features

* **Smart Formatting:** Converts standard precision LRC timestamps (e.g., `[03:45.12]`) into a highly readable, simplified format (`[3:45]`).
* **Metadata Stripping:** Automatically cleans up internal database tags (like `[ar:Artist]` or `[ti:Title]`) to give you *only* the verses.
* **Timestamp Fallback:** If lyrics are found but lack timing data, the script detects it and asks if you still want to view and save the plain text version. (you have to add ther time stamps in)
* **Text Export:** Saves your formatted lyrics directly into a cleanly named `.txt` file.
* **Continuous Loop:** Stays open and ready for your next search until you explicitly type `exit`.

## Prerequisites

This project requires **Python 3.6+** and the `syncedlyrics` library, which scrapes multiple open lyrics databases behind the scenes.
