def compression(s):
    count = 1
    compressed = ""
    for i in range(1,len(s)):
        if i == len(s)-1:
            compressed += s[i] + str(count)
        if s[i-1] == s[i]:
            count += 1
            continue
        else:
            compressed += s[i-1] + str(count)
            count = 1
    return compressed

def main():
    compression("aaacddsdfsdf")
main()