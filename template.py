ver:float=1.0 #Version.
def main(args):
    if args == None: print("Hello, world! I have not yet been interacted with using words.")
    else: print(f"Hello, world! I've been told {args}.")
aliases:list=["world", "hello-world"] #First index should be the main command, everything past that is aliases.