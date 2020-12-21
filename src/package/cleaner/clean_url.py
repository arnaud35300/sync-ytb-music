import re

def clean_url(url):
    """Fonctions qui extrait l'id de la playlist a partir d'une URL"""
    m =  re.search('list=(.*?)$', url)
    if m is not None:
        return m.group(1)
    return False
