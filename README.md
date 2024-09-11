# Spotify Playlist Analysis

This project analyses my Spotify playlist using Python for data processing and Tableau for visualisation.\
With over 500 songs in my playlist, many were frequently skipped.\
Although I was hesitant to remove them, fearing I might want to listen to them in the future,\
I decided to reorganise my playlist by identifying frequently played songs and those that haven't been listend to recently.\
This allows me to streamline the playlist for better listening experience without constantly skipping tracks.


## Project Structure

### 1. Data Collection
I requested my Spotify streaming history via my personal account, and the data was provided as a JSON file.\
The JSON file contains detailed listening history, including music and podcast data.

### 2. Data Cleaning & Preprocessing
To prepare the data for analysis, I used the following steps using python pandas
- Correcting Data: Fixed any mislabeling in 'ArtistName' and 'TrackName' within the dataset
- Combining Data: Merged streaming history from three JSON files containing both music and podcast data
- Handling Duplicates: Grouped songs by the same 'trackName' and 'artistName' and summed the playtime(msPlayed)
- Filter and Sort: Sorted playtime(msPlayed) in descending order, and filtered based on the specific playlist that I aimed to analyse
- Remove Missing Data: Verified that there were no missing data in 'trackName' and 'artistName'


### 3. Feature Selection
For the analysis, the following features were considered
- msPlayed: total playtime in milliseconds
- endTime: Last played date

The Criteria for selecting songs to remove were as follows
- Songs with below-average playtime(msPlayed)
- Songs not played in the past three months
- Songs that were played fewer than five times

### 4. Visualisation
The analysis is visualised using Tableau
- [My Playlist Dashboard](https://public.tableau.com/app/profile/jihye.bae7934/viz/PlaylistDashboardforMyPlaylist/PlaylistAnalysis#1)
- [KR Playlist Dashboard](https://public.tableau.com/app/profile/jihye.bae7934/viz/PlaylistDashboard_17235772954290/1)


## Results
- KR Playlist: Reduced from 428 songs to 245 songs
- My Playlist: Reduced from 136 songs to 93 songs


## Installations and Setup
- Instructions on how to clone the repository and install dependencies
```
git clone https://github.com/jihyebaee/Spotify_Playlist_Analysis.git
cd Spotify_Playlist_Analysis
pip install pandas
``` 
