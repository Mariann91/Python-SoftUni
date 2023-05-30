string = input().split(", ")

if string[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    string.reverse()
    wolf_index = string.index("wolf")
    print(f"Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!")
