# chess-capture-map
Fetches games for any user on Lichess.org
Writes to a single PGN file. (this could potentially be huge)
Searches all games in the PGN to find the coordinates of each capture. 
Uses Plotly.Express Heatmap to graph all the captures. 

![](https://github.com/tomasquinones/chess-capture-map/blob/c88828af154432d2056005f6792487e2d56e5929/sample_capture_heatmap.png)

Notes:
This was a personal learning project that helped me learn and practice some programming concepts:
1. Fetching data over the internet using an API.
2. Searching a large blob of text using Regex.
3. Refactoring my code into functions in a separate function file.
4. Writing unit tests using the Unittest module.
5. Fair amount of list/dict manipulation and iteration.
