import os

# converts lines to strings
def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()

res = sum([((ord(a) - 65) + (ord(b) - 89)) % 3 + 1 + ((ord(b) - 89) + 1) * 3 for a,_,b in loadInput()])








