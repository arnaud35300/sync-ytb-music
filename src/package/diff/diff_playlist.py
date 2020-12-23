import numpy as np

def diff_playlist(filename, new: iter):
    """ 
    Fonction qui compare le fichier filename avec le tableau new:
    Elle permet de connaître les nouvelles musiques de la playlist et les musiques à supprimer.
    Elle return : un tableau Add contenant les musiques à ajouter à la playlist.
                : un tableau Delete contenant les musiques à supprimer de la playlist.
    """
    # convert file
    tabDelete = []
    tabAdd = []
    f =  open(filename, "r")
    last = f.read().splitlines()
    f.close()
    #Tab Delete
    for i in range(len(last)):
        if last[i] not in new:
            tabDelete.append(last[i]) 
    #Tab Add
    for i in range(len(new)):
        if new[i] not in last:
            tabAdd.append(new[i]) 
    return [tabAdd, tabDelete]
