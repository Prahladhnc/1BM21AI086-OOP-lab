import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def check(email):
    if(re.fullmatch(regex, email)):
        print(email," is a Valid Email")
 
    else:
        print(email,"is an Invalid Email")
        
email1="https://www.google.com"
email2="india@gmail.com"
check(email1)
check(email2)
