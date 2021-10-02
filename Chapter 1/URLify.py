def URLify(s, n):
    output = ""
    for i in range(n):
        if (s[i] == " "):
            output += "%20"
        else:
            output += s[i]
    print(output)

def main():
    URLify("Mr John Smith      ", 13)

main()

