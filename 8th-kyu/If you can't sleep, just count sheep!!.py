def count_sheep(n):
    i = 1 
    s = []
    while i < n+1:
        d = "{} sheep...".format(i)
        i+=1
        s.append("{}".format(d))
    d = ""
    for i in s:
        d+=i
    return(d)  
