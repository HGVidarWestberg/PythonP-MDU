import subprocess; subprocess.run('cls', shell=True)

continue hoppar tillbaka till loopens början (startar inte om, utan startar bara nästa iteration)

range(stop) start blir 0 och step blir 1
range(start,stop) step blir 1
range(start,stop,step)
step kan vara negativ

while condition:
    pass
    if condition:
        break
else:
    körs om while loopen inte blivit bruten


syntaxfel = SyntaxError
körfel = Exceptions
logikfel = inget error 


try/except används för att fånga fel
except ValueError fångar upp bara om det är ett ValueError (funkar inte med syntaxfel)

escape character är \
representerar tecken som inte går
print(" \" ") ger "
print(" \\ ") ger \
\n gör ny rad
\t tabbar

'''...
....
...'''  (''' definierar en sträng över flera rader)

strängar sparas som listor med karaktärer med index "i" i sträng[i]

.upper()      uppercase
.lower()      lowercase
.strip(a)     tar bort a i början och slutet
len(sträng)   längd på strängen
.replace(a,b) byter ut a mot b
.center()

for c in string:
    print(c)

if "sträng1" in "sträng2": (kollar om sträng 1 finns i sträng 2)

x[start:stop:steg]

sträng = "sträng"
sträng[1,4,2] = tä
sträng[-1] = g
[-1] går bakifrån

letter = input("")
match letter:
    case "a":
        print("du valde a")
    case "_": 
        print("hittade inte tecken")