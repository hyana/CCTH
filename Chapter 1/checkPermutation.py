def checkPermutation(s, t):
    if len(s) != len(t):
        return False
    s1 = sorted(s)
    s2 = sorted(t)
    for c1, c2 in zip(s1, s2) :
        if c1 != c2:
            return False
    return True        

def main():
    checkPermutation("asdf","fdsa")

main()
