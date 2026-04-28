#Ask for the password
password = input("Enter password: ")
is_upcase = False
is_lwcase = False
is_special = False
is_digit = False

##Now, Check for the strength of the password
#break down each character of the password and evaluate
for char in password:
    if char.isupper():
        is_upcase = True
    elif char.islower():
        is_lwcase = True
    elif char.isdigit():
        is_digit = True
    elif char in "!@#$%^&*()_+-=?/.,<>?":
        is_special = True
if is_upcase and is_lwcase and is_special and is_digit:
    print("Strong password")
