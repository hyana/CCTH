def stringRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    posb = []
    for i in range(len(s1)):
        posb.append(s1[i:] + s1[:i])
    if s2 in posb:
        return True
    else:
        return False

def main():
    stringRotation("waterb ottle", "ewaterb ottl")

main()