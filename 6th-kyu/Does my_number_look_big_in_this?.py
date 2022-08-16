def narcissistic(value):
    answer = 0
    for i in str(value):
        answer+=((int(i))**len(str(value)))
    return value == answer
