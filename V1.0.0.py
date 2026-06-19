import syncedlyrics
import re

def get_synced_lyrics():
    # The main loop keeps the program restarting until you close it
    while True:
        print("\n🎵 Synced Lyrics Finder 🎵")
        
        # Get the song name and artist from the user
        song_name = input("Enter the song name (or type 'exit' to quit): ").strip()
        if song_name.lower() == 'exit':
            print("Goodbye! 👋")
            break
            
        artist_name = input("Enter the artist name (optional): ").strip()
        
        search_query = f"{song_name} {artist_name}".strip()
        print(f"\nSearching for lyrics for: '{search_query}'...")
        
        try:
            # Fetch the lyrics
            lrc_lyrics = syncedlyrics.search(search_query)
            
            if lrc_lyrics:
                formatted_lines = []
                has_timestamps = False
                
                for line in lrc_lyrics.split('\n'):
                    # Check if the line has a timestamp
                    if re.search(r"\[\d{1,2}:\d{2}\.\d+\]", line):
                        has_timestamps = True
                        # Reformat to [M:SS]
                        clean_line = re.sub(r"\[0?(\d+):(\d{2})\.\d+\]", r"[\1:\2]", line)
                        formatted_lines.append(clean_line)
                    else:
                        # Keep plain text lines in case they want it without timestamps
                        # Filters out metadata tags like [ar: Artist]
                        if not re.search(r"\[[a-zA-Z]+:.*\]", line) and line.strip():
                            formatted_lines.append(line)
                
                # If timestamps were found, we only kept the timestamped lines
                if has_timestamps:
                    # Re-filter to make sure we only have the timestamped ones
                    final_lyrics = "\n".join([line for line in formatted_lines if line.startswith("[")])
                else:
                    # If no timestamps were found in the file at all, ask the user
                    print("\n⚠️ Lyrics were found, but they do NOT have timestamps.")
                    choice = input("Would you still like to see and save the plain lyrics? (y/n): ").lower()
                    if choice != 'y':
                        print("\nRestarting...")
                        continue
                    final_lyrics = "\n".join(formatted_lines)

                print("\n--- Lyrics Found! ---\n")
                print(final_lyrics)
                print("\n---------------------\n")
                
                # Save to a .txt file
                save = input("Do you want to save these lyrics to a text file? (y/n): ").lower()
                if save == 'y':
                    safe_name = song_name.replace(' ', '_').replace('/', '_')
                    filename = f"{safe_name}_lyrics.txt"
                    
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(final_lyrics)
                    print(f"✅ Lyrics successfully saved to {filename}")
            else:
                print("\n❌ Sorry, lyrics couldn't be found for this track.")
                
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            
        print("\n--- Restarting Search ---")

if __name__ == "__main__":
    get_synced_lyrics()
