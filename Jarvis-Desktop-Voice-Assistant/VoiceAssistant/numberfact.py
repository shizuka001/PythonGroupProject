import requests

def numfacts(number):

    url = "https://numbersapi.p.rapidapi.com/"+number+"/math"

    querystring = {"fragment":"true","json":"true"}

    headers = {
        "X-RapidAPI-Key": "85002f489dmshace7493952edcd4p17598ajsn90c8e819583e",
        "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return(response.json()['text'])