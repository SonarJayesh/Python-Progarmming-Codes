#Write a program to create a custom exception class to validate age for voting eligibility (age >= 18).

class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter Your Age: "))
    if age < 18:
        raise InvalidAgeError
    else:
        print("Eligible for Voting ")

except InvalidAgeError:
    print("Not Eligible for Voting")    