from os import system as cmd1
from subprocess import run as cmd2

aliases=["sh", "bash", "ash", "cmd", "term", "bat", "run", "command", "powershell"]
ver:float=1.2
def main(args):
    if args.startswith("help"):
        if args == "help":
            print("sh (command)//(shell type [can be 1 or 2])")
            print("Run 'help types' to find out more about shell types.")
            return 0
        if args == "help types":
            print("Shell type 1: os.system()")
            print("Shell type 2: subprocess.run(shell=True)")
            return 0
    args=args.split("//", 1)
    args[1] = int(args[1])
    if len(args) == 2:
        if args[1] == 1:
            cmd1(args[0])
        if args[1] == 2:
            cmd2(args[0], shell=True)
    else:
        print("You must provide a shell type.")
        return 0