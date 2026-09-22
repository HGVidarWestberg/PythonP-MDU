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

type(variabel) visar variabeltypen

del list[index] tar bort ett element i listan, funkar på fler datatyper
list.append(innehåll) lägger till något sist i listan
list.remove(innehåll) tar bort första elementen ur listan baserat på värdet (första innehåll)
list.pop(index) tar bort ett element och returnerar det
list.sort() sorterar i bokstavsordning (inte mellan int och str)
list.count(innehåll) räknar alla av innehåll i listan

när du deklarerar en varibel efter en annan pekar de på samma bit av minne => operationer sker på båda
var.copy() skapar en kopia som inte pekar på samma bit minne

item in list är ett bool-statement som kollar om itemen finns i list

f=open("filnamn", encoding = "utf-8") öppnar en fil från samma mapp som pythonfilen som utf8
t=f.read() ger en textsträng
f.close stänger filen, annars kan man få problem med datorn

f = open("filnamn", "w") byter ut filen mot en tom och öppnar den som redigerare
f.write("text")

with open("filnamn") as f: Stänger filen automatiskt när kodblocket slutar
    t = f.read()

i en .txt fil kan man bara skriva strängar, därför anväänder man json.dumps
import json
txt = json.dumps(list)

list = json.loads(txt) ger tillbaka listan från json-formatet
