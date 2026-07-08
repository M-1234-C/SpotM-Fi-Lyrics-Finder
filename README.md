# SpotM-Fi-Lyrics-Finder
A external app for SpotM-Fi that lets you find the lyrics for the song you want with time stamps 

# But what actually is it ?
Its a lightweight, command-line Python utility that searches for song lyrics, extracts their timing data, reformats the timestamps into a clean `[minute:second:millisecond]` format, and exports them directly to text files or dedicated lrc files. This runs a clean loop so you can get all you lyrics in one go and just add them into SpotM-fi

## Features

​**Precision Timestamps**: Retains standard millisecond precision (e.g., [03:45.12]) to ensure perfect synchronization when loading the files into modern media players.

​**Metadata Stripping**: Automatically cleans up internal database tags (like [ar:Artist], [ti:Title], or contributor credits) to give you only the verses.

​**Timestamp Fallback**: If synced lyrics aren't available, the script automatically detects this and asks if you'd still like to view and save the plain, untimed text version instead.

​**Flexible Export**: Saves your formatted lyrics directly into a cleanly named file, letting you choose on the fly whether you want a standard .txt document or a dedicated .lrc track.

​**Continuous Loop**: Stays open and ready for your next search without needing to restart the app, running until you explicitly type exit.

## Prerequisites

This project requires **Python 3.6+** and the `syncedlyrics` library, which scrapes multiple open lyrics databases behind the scenes.
