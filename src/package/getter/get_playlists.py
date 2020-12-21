import json

def get_playlists():
    """Retourne les playlists dans settings.json"""
    with open('settings.json') as f:
        data = json.load(f)
    return data['playlists']
