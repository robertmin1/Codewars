def square_digits(num):
    answer = ""
    for i in str(num):
        answer+="{}".format(int(i)**2)
    return int(answer)
        
