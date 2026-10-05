birds = {}
total = 0

while True:
    bird = input("bird: ").lower()
    if bird not in birds:
        birds[bird] = 0
    birds[bird] += 1
    total += 1
    print(f"({bird}), {birds[bird]} of {total}")