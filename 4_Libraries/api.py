#Section 4 Notes Segment 8

import requests


def main():
    #best pracice to put GET requests in a try statement, in case of bad connection
    try:
        print("Search the Art Institute of Chicago!")
        artist = input("Artist: ")

        #GET request = requests.get()
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            #can specfiy, look at api documentation
            {"q": artist}
        )
        response.raise_for_status()
    except requests.HTTPError: 
        print("Couldn't complete request!")
        return
    #.json turns the request into a json file
    content = response.json()
    #specific to documentation of specfic api
    for artwork in content["data"]:
        print(f"* {artwork['title']}")

#make sure to look at documentation

main()