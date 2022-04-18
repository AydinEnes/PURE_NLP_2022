from youtube_transcript_api import YouTubeTranscriptApi as yt


import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
import urllib
import simplejson

# extract playlist id from url
url = "https://www.youtube.com/playlist?list=PLbSqnUIy2z41tu7H6qxtYJq-WlUDI27UB"
query = parse_qs(urlparse(url).query, keep_blank_values=True)
playlist_id = query["list"][0]


youtube = googleapiclient.discovery.build(
    "youtube", "v3", developerKey="AIzaSyDBSzz965VcCCuC1MEDl2gbsr2lHOW3O14"
)

request = youtube.playlistItems().list(
    part="snippet", playlistId=playlist_id, maxResults=50
)
response = request.execute()

playlist_items = []
while request is not None:
    response = request.execute()
    playlist_items += response["items"]
    request = youtube.playlistItems().list_next(request, response)

videoURLS = [
    f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s'
    for t in playlist_items
]

with open(
    "/Users/tancetiner/Documents/GitHub/PURE_NLP_2022/files/model_input_texts/chem_texts/semih_balmuk_chem_organik.txt",
    "w",
) as f:
    for t in playlist_items:
        try:
            # json = simplejson.load(
            #     urllib.urlopen(
            #         f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s'
            #     )
            # )
            # title = json["entry"]["title"]["$t"]
            # f.write("{} - ".format(title))
            title = t["snippet"]["title"]
            f.write("{} - ".format(title))
            srt = yt.get_transcript(
                t["snippet"]["resourceId"]["videoId"], languages=["tr"]
            )
            for dic in srt:
                # print(dic["text"], end=" ")
                f.write(dic["text"] + " ")
            f.write("\n")
        except:
            pass
