import pandas as pd
import json

# Read json file
df1 = pd.read_json('StreamingHistory_music_0.json')
df2 = pd.read_json('StreamingHistory_music_1.json')
df3 = pd.read_json('StreamingHistory_podcast_0.json')

# Change column name for podcast
# podcastName -> artistName, episodeName -> trackName
rename_podcast = df3.rename(columns={'podcastName':'artistName', 'episodeName':'trackName'})

# Change values for podcast
# artistName: Bubble gum -NEWJEANS -> NewJeans, Loreansbob -> NewJeans
# trackName: NewJeans (뉴진스) 'Bubble Gum -> Bubble Gum
rename_podcast.loc[rename_podcast['artistName'] == "Bubble gum -NEWJEANS", 'artistName'] = "NewJeans"
rename_podcast.loc[rename_podcast['artistName'] == "Loreansbob", 'artistName'] = "NewJeans"
rename_podcast.loc[rename_podcast['trackName'] == "NewJeans (뉴진스) 'Bubble Gum", 'trackName'] = "Bubble Gum"
# print(rename_podcast)

# Concatenate 3 datarame
all_history = pd.concat([df1, df2, rename_podcast])
# print(all_history)

# Drop column 'endTime'
# drop_endTime = all_history.drop('endTime', axis=1)

# Sum msPlayed if artistName and trackName are same
sum_msPlayed = all_history.groupby(['trackName', 'artistName'], as_index=False)['msPlayed'].sum()
# print(sum_msPlayed)

# Get the latest endTime for trackName and artistName
endTime = all_history.groupby(['trackName', 'artistName'], as_index=False)['endTime'].max()

# Add 'endTime' column in 'sum_msPlayed'
sum_msPlayed_with_endTime = pd.merge(sum_msPlayed, endTime, on=['trackName', 'artistName'], how='left')

# print(sum_msPlayed_with_endTime)


# Test with trackName 'Flower' if sum_msPlayed is working
# sum_example = df1.loc[df1['trackName'] == "FLOWER"]
# print(sum_example)

# is_flower = sum_msPlayed.index.get_level_values('trackName') == "FLOWER"
# flower_tracks = sum_msPlayed[is_flower]
# print(flower_tracks)


# Sort sum_msPlayed by descending order
sort_desc = sum_msPlayed_with_endTime.sort_values(by='msPlayed', ascending=False, ignore_index=True)
# print(sort_desc)

# Check if there is any empty values in 'trackName' and 'artistName'
check_empty = sort_desc[['trackName', 'artistName']].isnull().sum()
# print(check_empty)

# Because Json file is nested
with open('Playlist1.json',encoding='UTF-8') as json_file:
    data = json.load(json_file)

# Flatten the JSON
df_flattened = pd.json_normalize(data['playlists'], record_path='items', meta=['name'], errors='ignore')

# Filter specific playlists
filtered_playlists = df_flattened[df_flattened['name'].isin(["My playlist", "🇰🇷"])]
# print(filtered_playlists)

# Return only trackName and artistName
item_names = filtered_playlists[['track.trackName', 'track.artistName', 'name']]
item_names = item_names.sort_values(by='track.trackName', ignore_index=True)
item_names = item_names.rename(columns={"track.trackName":"trackName", "track.artistName":"artistName", "name":"playlistName"})
item_names = item_names.dropna(how='any', inplace=False)
# print(item_names)

# Get the songs that are in both streaming history and the playlists
duplicated_playlist = pd.merge(sort_desc, item_names, how='right', on=['trackName', 'artistName'])
duplicated_playlist = duplicated_playlist.sort_values(by='msPlayed', ascending=False, ignore_index=True)
print(duplicated_playlist)

# Change to excel file
file_name = 'Playlist_organised.xlsx'
duplicated_playlist.to_excel(file_name, index=False)