def check_args(args):
    if args.url == False:
        return False
    if args.cmp == False:
        return False
    if args.dest == False:
        return False
    return True
