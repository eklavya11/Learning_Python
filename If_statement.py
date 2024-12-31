is_male = True
is_tall = True

if is_male and not(is_tall):
    print("You are a male or tall or both")
elif is_male and is_tall:
    print("You are a tall male")
else:
    print("You are neither tall or  male")