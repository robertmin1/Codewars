def solution(s):
    str = []
    str = [s[i:i + 2] for i in range(0, len(s), 2)]
    for i in str:
        if len(i) != 2:
            str.append(i + "_")
            str.remove(i)
    print(str)
    return str
