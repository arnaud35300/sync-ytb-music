# Cahier des charges

## Presentation du projet

Le projet consiste en un utilitaire de commande permettant de synchroniser une playlist youtube en telechargeant ses musiques dans un format defini dans un dossier en local.

## MVP

### Gestion d'un fichier de configuration comportant les parametres de l'utilisateur tels que ses liens de playlist youtube, ses preferences de format et de compression, ainsi que le chemin vers son dossier de sauvegarde.

Template fichier `settings.json` :
```
{
    "lang": "fr",
    "playlists": {
        "1": {
            "name": "https...",
            "folder": "/folder",
            "compression": "zip"
        },
        "2": {
            "name": "https...",
            "folder": "/folder",
            "compression": "zip"
        }
    }
} 
}
```

### Gestion de commandes et d'options pour executer le programme.

Commande:
```
python3 syncytb.py [OPTION]...
```

Liste des options:

```
-h, --help      => Description du programme.
-u, --url       => Indiquer l'url d'une playlist.
-c, --cmp       => Indiquer le format de compression des fichiers audios. Ex: zip, tar, gz, etc..
```

### Mise en place de cron task.

### Mise à jour des données local grace à une synchronisation de la/les playlist(s)


