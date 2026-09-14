LarNum = 0

while True:
    Num = input("nummer: ")
    try:
        Num = int(Num)
    except ValueError:
        print("inte ett nummer")
        continue
    if Num == 0:
        print(f"största numret är {LarNum}")
        break
    if Num > LarNum:
        LarNum = Num