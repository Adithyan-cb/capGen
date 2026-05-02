import os
import requests
from typing import List, Dict, Optional
from dotenv import load_dotenv

load_dotenv()

DEEZER_API_KEY = os.getenv("DEEZER_API_KEY")
RAPIDAPI_HOST = "deezerdevs-deezer.p.rapidapi.com"
DEEZER_BASE_URL = "https://deezerdevs-deezer.p.rapidapi.com"


class DeezerTrack:
    def __init__(self, track_data: Dict):
        self.id = track_data.get("id")
        self.title = track_data.get("title")
        self.artist_name = track_data.get("artist", {}).get("name", "Unknown Artist")
        self.album_title = track_data.get("album", {}).get("title", "")
        self.album_cover = track_data.get("album", {}).get("cover_medium", track_data.get("album", {}).get("cover", ""))
        self.preview = track_data.get("preview")
        self.duration = track_data.get("duration", 0)
        self.link = track_data.get("link")

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "title": self.title,
            "artist_name": self.artist_name,
            "album_title": self.album_title,
            "album_cover": self.album_cover,
            "preview": self.preview,
            "duration": self.duration,
            "link": self.link,
        }


def search_songs(artist_name: str, song_name: str) -> Optional[Dict]:
    """
    Searches for a song on Deezer API based on artist and song name.
    Returns track data with preview URL or None if not found.
    """
    if not DEEZER_API_KEY:
        print("Deezer API key not configured")
        return None

    query = f'"{song_name}" {artist_name}'
    
    headers = {
        "X-RapidAPI-Key": DEEZER_API_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    
    params = {
        "q": query,
        "limit": 1
    }
    
    try:
        response = requests.get(f"{DEEZER_BASE_URL}/search", headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        tracks = data.get("data", [])
        if tracks:
            return DeezerTrack(tracks[0]).to_dict()
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching song from Deezer: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error in search_songs: {e}")
        return None


def get_song_details(track_id: int) -> Optional[Dict]:
    """
    Gets detailed track info by ID from Deezer API.
    """
    if not DEEZER_API_KEY:
        print("Deezer API key not configured")
        return None

    headers = {
        "X-RapidAPI-Key": DEEZER_API_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    
    try:
        response = requests.get(f"{DEEZER_BASE_URL}/track/{track_id}", headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return DeezerTrack(data).to_dict()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching track details from Deezer: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error in get_song_details: {e}")
        return None