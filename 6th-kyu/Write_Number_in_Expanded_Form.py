def expanded_form(num):
    answer = []
    pow = 10
    n = 0
    s = ""
    while num!=0:
        if n == 0:
            answer.append(num%10)
            num = num//10
            n+=1
        else:
            answer.append(num%10 * pow**n)
            n+=1
            num = num//10
    answer.reverse()
    for i in answer:
        if i == 0:
            continue
        else:
            s = s+str(i)+" + "

    return (s[:-3])
