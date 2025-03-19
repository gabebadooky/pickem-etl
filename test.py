import requests

data = requests.get('https://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/311').json()

print(hasattr(data['team'], 'alternateColor'))