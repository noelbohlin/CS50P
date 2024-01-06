# från uppgiften response validation från cs50

import validators

if validators.email(input("What's your email address? ")) == True:
    print("Valid")
else:
    print("Invalid")
