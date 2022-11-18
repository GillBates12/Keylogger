import json
import pandas as pd
from pprint import pprint
from typing import Dict, List

accumulated_song_data = []


def read_json_file(filepath: str) -> List[Dict]:
    with open(filepath) as f:
        data = json.load(f)
    return data


def process_list_of_songs(data: List):
    for entry in data:  # Each entry is a Dict
        new_song_entry = {
            "album": entry['master_metadata_album_album_name'],
            "artist": entry['master_metadata_album_artist_name'],
            "song": entry['master_metadata_track_name'],
            "timestamp": entry['ts'],
            "time_played": entry["ms_played"]
        }
        accumulated_song_data.append(new_song_entry)


test_data1 = read_json_file("/Users/pablorizo/Downloads/endsong_0.json")
test_data2 = read_json_file("/Users/pablorizo/Downloads/endsong_1.json")
test_data3 = read_json_file("/Users/pablorizo/Downloads/endsong_2.json")
test_data4 = read_json_file("/Users/pablorizo/Downloads/endsong_3.json")
test_data5 = read_json_file("/Users/pablorizo/Downloads/endvideo.json")
process_list_of_songs(test_data1)
process_list_of_songs(test_data2)
process_list_of_songs(test_data3)
process_list_of_songs(test_data4)
process_list_of_songs(test_data5)

#pprint(accumulated_song_data)

df = pd.DataFrame(accumulated_song_data)
#df.to_csv('SpotifyData.csv', index=False)
print(df)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
