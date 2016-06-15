
artist_answer = input("Search for an artist")
import requests
response = requests.get('https://api.spotify.com/v1/search?q='+artist_answer+'&type=artist&market=US&limit=50')
#https://api.spotify.com/v1/search?type=artist
artist = response.json()
#print(artist.keys())
#print(artist['artists'].keys())
#print(type(artist['artists']['items']))
artist_count = 0
for artist in artist['artists']['items']:
    artist_name = artist['name']
    artist_id= artist['id']
    artist_count = artist_count + 1
    #artist_dictionary[artist_count]= artist_name
    artist_dictionary = {}
    artist_dictionary['number'] = artist_count
    artist_dictionary['name'] = artist['name']
    artist_dictionary['id'] = artist['id']

    print(artist_dictionary['name'],artist_dictionary['number'] )

selection= input("Get more info about one of this artists by inputing its number")
if selection
for artist in artist_dictionary['number']:
    print(artist_dictionary['name'])

#for item in artist_dictionary[number]
#if number == artist_dictionary['number']:
    #for item in number:
        #print(item)
        #selected_number = artist_dictionary['id']
        #print(selected_number)

import requests
response = requests.get('https://api.spotify.com/v1/artists/'+selected_number+'/top-tracks?country=US')
artist_toptracks= response.json()
top_tracks = artist_toptracks['tracks']
for tracks in top_tracks:
    print("These are", artist_dictionary['name'],"top tracks:", tracks['name'])
