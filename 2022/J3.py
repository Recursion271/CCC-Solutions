s = input("Tuning instructons: ")
r = ""

for i in range(len(s)):
   
    if i > 0 and s[i].isalpha() and s[i-1].isnumeric():
        print(r.replace("+"," tighten ").replace("-"," loosen "))
        r = s[i]
    else:
        r = r + s[i]
print(r.replace("+"," tighten ").replace("-"," loosen "))



