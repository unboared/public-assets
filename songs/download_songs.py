import json
import os
 
# Opening JSON file
f = open('../../songs.json')
 
# returns JSON object as
# a dictionary
songs = json.load(f)
 
# Iterating through the json
# list
for song in songs:
    print("# Downloading {} de {}".format(song['title'], song['artist']))
    os.system("youtube-dl -x --audio-format mp3 -o '{}.(ext)s' --postprocessor-args '-ss 00:00:00 -to 00:00:30' {}".format(song['id'],song['trackLink']))
 
# Closing file
f.close()