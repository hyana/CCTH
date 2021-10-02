def oneAway(s1, s2):
    hash = {}
    count = 0
    for c1 in s1:
        if c1 not in hash:
            hash[c1] = 1
        else:
            hash[c1] += 1
    for c2 in s2:
        if c2 not in hash:
            hash[c2] = 1
        else:
            hash[c2] += 1
    for key, value in hash.items():
        if (value == 1):
            count += 1
        if (count > 2): 
            return False
    return True

def main():
    oneAway("pale", "ple")
    oneAway("bakes", "bkes")
main()