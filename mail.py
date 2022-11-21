email = input("what's your email")
while len(email) > 25 or not ("A" <= email[0].upper() <= "Z") or email.find("@") == -1:
    email = input("what's your email")
passw = (
    email[0]
    + str(len(email[0 : email.find("@")]))
    + email[email.find("@") + 1]
    + str(ord(email[len(email) - 1]))
)
print(f"generated password is {passw}")
