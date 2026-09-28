list_a = [4, 1, 9, 4, 7, 9, 3, 8, 5, 8]
list_b = [4, 1, 1, 4, 7, 9, 6, 8, 5, 8]

for i in range(len(list_a)):
    if list_a[i] == list_b[i]: 
        print(list_a[i], ":", list_b[i])
    else:
        print(list_a[i], ":", list_b[i], "<- DIFF!")