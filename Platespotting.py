numbers = "1234567890"
count = 0

while True:
    plate = input("Plate: ")
    if plate == "0":
        print("count:", count)
        break
    curr = ""
    for i in plate:
        if i in numbers:
            curr += i
    try:
        curr = int(curr)
    except:
        print("invalid plate")
        continue
    if curr == count+1:
        count += 1
        print(count)
    if count == 999:
        print("Finish!!!")
        break