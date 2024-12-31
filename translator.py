#translate vowels to g

x = input("enter a word or text:")

y=""
for i in x:
    if i.lower() in ["a","e","i","o","u"]:
        if i.isupper():
            y=y+"G"
        else:
            y=y+"g"
    else:
        y=y+i

print(y)


#multi line comments below - use mainly

'''
hello eklavya jdjjs
'''
