import requests, time
from credentials.open_cage_api_key import key


def call_geocode_api(stadium: str, city: str, state: str=None) -> dict:
    """Method to retrieve data from OpenCage forward geocode endpoint"""
    open_cage_geocode_endpoint: str = f"https://api.opencagedata.com/geocode/v1/json?key={key}"
    formatted_stadium: str = stadium.replace(" ", "+").replace("&", "")
    formatted_city: str = city.replace(" ", "+")
    data: dict

    if state is not None:
        formatted_state: str = state.replace(" ", "+")
        open_cage_geocode_endpoint: str = f"{open_cage_geocode_endpoint}&q={formatted_stadium}+{formatted_city}+{formatted_state}"
    else:
        open_cage_geocode_endpoint: str = f"{open_cage_geocode_endpoint}&q={formatted_stadium}+{formatted_city}"
    
    try:
        time.sleep(1)
        data = requests.get(open_cage_geocode_endpoint).json()
    except:
        data = { "results": [ { "geometry": { "lat": 0, "lng": 0 } } ] }
    return data


def get_lat_long_tuple(stadium: str, city: str, state=None) -> tuple:
    data: dict = call_geocode_api(stadium, city, state)
    latitude: float
    longitude: float

    try:
        latitude = data["results"][0]["geometry"]["lat"]
        longitude = data["results"][0]["geometry"]["lng"]
    except:
        latitude = 0
        longitude= 0
    return latitude, longitude