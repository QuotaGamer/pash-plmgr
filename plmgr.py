import os
from colorama import Fore as f
aliases=["pacman", "apt", "plmgr", "pmgr"]
data="./plugins/plmgr"
ver:float=1.1
print(f"{f.YELLOW}[WARN] plmgr is NOT currently functional!{f.RESET}")

def main(args):
    if args == None:
        print("i want argument, give me argument.")
        return 0
    if not os.path.exists(data):
        os.mkdir(data)
        print("Conf folder was not found, created.")
        return 0
    args=args.split(" ", 2)
    if len(args) == 1:
        if not args[0] in ["update", "upgrade"]:
            if args[0] in ["download", "search"]:
                print("This requires another argument.")
                return 0
            else:
                print("Invalid.")
                return 0
    elif len(args) == 2:
        if args[0] == "download":
            download(args)
        elif args[0] == "search":
            search(args)
    else:
        print("What the fuck.")
        return 0

def download(arg):
    pass
def update(arg):
    pass
def upgrade(arg):
    pass
def search(arg):
    pass