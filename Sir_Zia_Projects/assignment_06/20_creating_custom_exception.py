

class InvalidAgeError(Exception): pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18+")
    print("Access granted")

try:
    check_age(16)
except InvalidAgeError as e:
    print(e)