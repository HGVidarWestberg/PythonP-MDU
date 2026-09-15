consonants = "qwrtpsdfghjklzxcvbnm"
txt = input("text: ")
output = ""

for t in txt:
    if t in consonants:
        output += t+"o"+t
    else:
        output += t
print(output)