class InvalidAgeException(Exception):
    "Age is less than 18"
    pass


try:
    num=int(input("Enter a number:"))
    if(num<18):
        raise InvalidAgeException
    else:
        print("Eligible to vote")
except ValueError as err:
    print(err)

except InvalidAgeException as err:
    print("Invalid age")

