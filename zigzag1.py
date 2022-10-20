def zigzag(ch): 
    test = True
    i = 1
    if ch[0]>ch[1]:
        ch += "~"
        while test == True and  i <= len(ch)-1:
            test = ch[i] < ch[i+1] and ch[i] < ch[i-1]
            i += 2
    else :
        ch += "!"
        while test == True and  i <= len(ch)-1:
            test = ch[i] > ch[i+1] and ch[i] > ch[i-1]
            i+=2
    return test
