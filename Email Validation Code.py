"""
Check if the email entered is valid.
"""

def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."
    
    for words in string:
        if words not in valid:
            return True
    return False

def is_valid(email):
    if email.count("@") != 1:
        return False
   
    
    prefix, domain = email.split("@")
    if len(prefix) == 0:
        return False
        
    if email.count(".") != 1:
        return False
        
    domain_name, extension = domain.split(".")
    if len(domain_name) == 0:
        return False
    if len(extension) == 0:
        return False
        
    if has_invalid_characters(prefix):
        return False
    if has_invalid_characters(domain):
        return False
        
    return True
    
 
    

emails = [
    "test@example.com",
    "valid@gmail.com",
    "invalid@gmail",
    "invalid",
    "not an email",
    "invalid@email",
    "!@/",
    "test@@example.com",
    "test@.com",
    "test@site.",
    "@example.com",
    "an.example@test",
    "te#st@example.com",
    "test@exam!ple.com"
]




for email in emails:
    if is_valid(email):
        print(email + " is valid")
    else:
        print(email + " is invalid")