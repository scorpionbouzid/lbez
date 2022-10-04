def saise():
    ch1 = input('donner ch1')
    while not verif(ch1):
        ch1 = input('donner ch1')
    return ch1
def verif(ch1):
    if ch1[len(ch1)-1]==".":
        ch1 = ch1[:len(ch1)-1]
        i = 0
        l = True
        while not (i == len(ch1) or l == False):
            l = "A" <= ch1[i] <= "Z" or ch1[i] == " "
            i+=1
        return l
    else :
        return False
def crypt(ch1):
    cryptedstrin = ""
    # input of p et q 
    p,q = int(input("donner p")),int(input("donner q"))
    while not (1<p<11 and 1<q<11):
        p,q = int(input("give p between 2 and 10")),int(input("give q between 2 and 10"))
    # ctyptage
    for i in range(len(ch1)):
        if ch1[i] in [' ', '.']:
            cryptedstrin += ch1[i]
        else : 
            alph_i = ord(ch1[i])-64
            j = ( p * alph_i + q ) % 26 + 1
            cryptedstrin += chr(j+64)
    return cryptedstrin
ch = saise()
print(f"uncrypted string = {ch}")
ch3 = crypt(ch)
print(f" crypted string = {ch3}")
