#Arguments du programme syncytb.py
import argparse

def usage_msg():
    return '''syncytb.py 1.0
         [-u, --url, Pass youtube playlist url]
         [-c, --cmp, Pass compression extension]
    '''

def parse_args():
    parser = argparse.ArgumentParser(description='Liste des arguments pour la fonction parse_arg.', add_help=False, usage =usage_msg())

    parser.add_argument('-v', '--version', action='version',
                        version='syncytb.py 1.0', help="Affiche la derniere version du programme.")
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='Affiche les arguments et leurs rôles.')
    parser.add_argument('-u', '--url',
                        help='Indiquer l\'url d\'une playlist.', default=False)                        
    parser.add_argument('-c', '--cmp',
                        help='Indiquer le format de compression des fichiers audios. Ex: zip,tar,gz.', default=False, choices=['zip', 'tar', 'gz'])
    parser.add_argument('-d', '--dest',
                        help='Indiquer le dossier de sauvegarde des fichiers audios. Ex: C:/Documents/DossierMusiques', default=False)      
    return parser.parse_args()
