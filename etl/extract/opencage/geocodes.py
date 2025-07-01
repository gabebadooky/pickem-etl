import configparser, requests, time

def __read_opencage_api_key__() -> str:
    """Method to retrieve opencage key from config file"""
    config: configparser.ConfigParser = configparser.ConfigParser()
    config.read("config.ini")
    open_cage_api_key: str = config["opencage"]["api_key"]
    return open_cage_api_key


def __call_geocode_api__(stadium: str, city: str, state: str=None) -> dict:
    """Method to retrieve data from OpenCage forward geocode endpoint"""
    open_cage_geocode_endpoint: str = f"https://api.opencagedata.com/geocode/v1/json?key={__read_opencage_api_key__()}"
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
    data: dict = __call_geocode_api__(stadium, city, state)
    latitude: float
    longitude: float

    try:
        latitude = data["results"][0]["geometry"]["lat"]
        longitude = data["results"][0]["geometry"]["lng"]
    except:
        latitude = 0
        longitude= 0
    return latitude, longitude