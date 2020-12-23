import json
from pathlib import Path
def get_playlists():
    """Retourne les playlists dans settings.json"""
    with open(Path(__file__).absolute().parent / '../../settings.json') as f:
        data = json.load(f)
    return data['playlists']

