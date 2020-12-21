from package.validator.check_args import check_args
from package.getter.get_playlists import get_playlists
from package.getter.get_args_content import get_args_content

def init_data(args):
    """Initialise un objet Data qui contiendra les playlists"""
    class Data:
        def __init__(self, lang, playlists):
            self.lang = lang, 
            self.playlists = playlists

    if check_args(args) is False:
        data = Data('fr', get_playlists())
    else:
        data = Data('fr', get_args_content(args))
    return data
