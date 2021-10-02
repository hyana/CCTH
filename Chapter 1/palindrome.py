def palindrome(input):
    hash = {}
    count = 0
    for c in input.lower():
        if c == " ":
            continue
        if c not in hash:
            hash[c] = 1
        else:
            hash[c] += 1
    for key, value in hash.items():
        if (value % 2 == 1):
            count += 1
        if (count >= 2): 
            print(False)
            return
    print(True)

def main():
    palindrome("Tact CooaAa")
main()