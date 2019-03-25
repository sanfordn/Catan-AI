import random

def think():
    if command == "setup":
        return random.randint(0,53)
    if command == "build":
        return "-b"
    elif command == "end":
        return "-e"
