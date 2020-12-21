def check_args(args):
    """Retourne False si une option n'est pas presente"""
    if args.url == False:
        return False
    if args.cmp == False:
        return False
    if args.dest == False:
        return False
    return True
