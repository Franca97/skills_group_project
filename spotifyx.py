import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from the terminal:
username = sys.argv[1]

# User ID:  franca.b?si=iWuK25DNQyWlTM8OAquqaA

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
print(print(json.dumps(VARIABLE, sort_keys=TRUE, ident=4)))

#print(json.dumps(VARIABLE, sort_keys=TRUE, ident=4))



