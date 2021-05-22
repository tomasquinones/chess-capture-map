# chess-capture-map
Fetches games for any user on Lichess.org
Writes to a single PGN file. (this could potentially be huge)
Searches all games in the PGN to find the coordinates of each capture. 
Displays a simple ascii map of all the capture counts. 

Notes:
This was a personal learning project that helped me learn and practice some programming concepts:
1. Fetching data over the internet using an API.
2. Searching a large blob of text using Regex.
3. Refactoring my code into functions in a separate function file.
4. Writing unit tests using the Unittest module.
