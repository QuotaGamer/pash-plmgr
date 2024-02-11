import os
from colorama import Fore as f
aliases=["pacman", "apt", "plmgr", "pmgr"]
data="./plugins/plmgr"
ver:float=1.1
print(f"{f.YELLOW}[WARN] plmgr is NOT currently functional!{f.RESET}")

def main(args):
    if not os.path.exists(data):
        os.mkdir(data)
        print("Plugin folder was not found; creating...")
        return 0
    args = args.split(" ", 2)
    download(args)

def download(arg):
    pass
def update(arg):
    pass
def upgrade(arg):
    pass
def search(arg):
    pass