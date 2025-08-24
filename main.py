import os, requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

BASE = "https://api.spotify.com/v1"

def get_token():
    """
    Make a request to Spotify API and returns the access token
    """
    r = requests.post(
        "https://accounts.spotify.com/api/token",
        data={"grant_type": "client_credentials"},
        auth=(CLIENT_ID, CLIENT_SECRET),
        timeout=10
    )
    r.raise_for_status()
    return r.json()["access_token"]

def get_api(path, token, params=None):
    """
    Make a request to Spotify API and returns the API response
    """
    path = path if path.startswith("/") else f"/{path}"
    url = f"{BASE}{path}"
    headers = {"Authorization": f"Bearer {token}"}

    while True:
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(resp.status_code)
            return None
