aliases:list=["exit", "quit"]
ver:float=1.0
def main(args):
    if args == None: exit(0)
    else:
        try:
            int(args)
            exit(args)
        except Exception as e:
            print("Failed, invalid exit code, or something else happened.")
            print(e)