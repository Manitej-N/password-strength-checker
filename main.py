#Ask for the password
password = input("Enter password: ")
is_upcase = False
is_lwcase = False
is_special = False
is_digit = False
score = 0

##Now, Check for the strength of the password
#break down each character of the password and evaluate
for char in password:
    if char.isupper():
        is_upcase = True
        score += 1
    elif char.islower():
        is_lwcase = True
        score += 1
    elif char.isdigit():
        is_digit = True
        score += 1
    elif char in "!@#$%^&*()_+-=?/.,<>?":
        is_special = True
        score += 1
#Cases for password strength
if is_upcase and is_lwcase and is_special and is_digit:
    print("Strong password", score)
if is_upcase and is_lwcase and is_special==False and is_digit==False:
    print("Try a better password", score)
if is_upcase==False and is_special==False:
    print("Weak password", score)

