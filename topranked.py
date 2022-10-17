import requests

def get_session(api_key):
  session = requests.Session()
  # add the riot games api token to the sessions request headers:
  session.headers.update({"X-Riot-Token": api_key})
  return session

def make_api_request(session, endpoint, parameter):
  region = "na1"
  base_url = "api.riotgames.com"
  # construct an api request URL, make the GET request, and return the JSON response
  api_response = session.get(f"https://{region}.{base_url}/{endpoint}/{parameter}")
  return api_response.json()

session = get_session("RGAPI-3a22ebe5-32f7-454f-8c4b-3675c25872fa")

response = make_api_request(session, "lol/league/v4/challengerleagues/by-queue", "RANKED_SOLO_5x5")

# parse the json response
for player in response['entries']:
  name = str(player['summonerName'].encode("utf-8"))
  # utf 8 encoding is needed because python's print() cant handle emojis or symbols in usernames
  print(name.strip("b'"))