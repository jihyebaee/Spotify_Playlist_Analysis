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

# Drop column 'endTime'
# drop_endTime = all_history.drop('endTime', axis=1)

# Sum msPlayed if artistName and trackName are same
sum_msPlayed = all_history.groupby(['trackName', 'artistName'], as_index=False)['msPlayed'].sum()
# print(sum_msPlayed)


# Test with trackName 'Flower' if sum_msPlayed is working
# sum_example = df1.loc[df1['trackName'] == "FLOWER"]
# print(sum_example)

# is_flower = sum_msPlayed.index.get_level_values('trackName') == "FLOWER"
# flower_tracks = sum_msPlayed[is_flower]
# print(flower_tracks)


# Because Json file is nested
with open('Playlist1.json',encoding='UTF-8') as json_file:
    data = json.load(json_file)

# Flatten the JSON
df_flattened = pd.json_normalize(data['playlists'], record_path='items', meta=['name'], errors='ignore')

# Filter specific playlists
filtered_playlists = df_flattened[df_flattened['name'].isin(["My playlist", "🇰🇷"])]
print(filtered_playlists)

# Return only trackName and artistName
item_names = filtered_playlists[['track.trackName', 'track.artistName']]
print(item_names)
