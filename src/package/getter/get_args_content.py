from package.cleaner.clean_url import clean_url

def get_args_content(args):
    """Assigne les valeurs des options passes en parametres dans la propriete playlist de Data"""
    return {'1' : {'name' : clean_url(args.url), 'folder': args.dest, 'compression': args.cmp}}
