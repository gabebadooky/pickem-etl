import requests
from open_cage_api_key import key

def extract_latitude(data: dict) -> str:
    return ''

def get_geocode(stadium: str, city: str, state=None) -> tuple:
    open_cage_geocode_endpoint = f'https://api.opencagedata.com/geocode/v1/json?key={key}'
    formatted_stadium = stadium.replace(' ', '+')
    formatted_city = city.replace(' ', '+')
    if all(state):
        formatted_state = state.replace(' ', '+')
        open_cage_geocode_endpoint = f'{open_cage_geocode_endpoint}&q={formatted_stadium}+{formatted_city}+{formatted_state}'
    else:
        open_cage_geocode_endpoint = f'{open_cage_geocode_endpoint}&q={formatted_stadium}+{formatted_city}'

    data = requests.get(open_cage_geocode_endpoint).json()

    latitude = data['results'][0]['geometry']['lat']
    longitude = data['results'][0]['geometry']['lng']

    return latitude, longitude