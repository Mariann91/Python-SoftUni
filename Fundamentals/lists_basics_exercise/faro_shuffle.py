items = input().split()
shaffle_count = int(input())

start = [items[0]]
end = [items[-1]]
items.pop(0)
items.pop(-1)

for _ in range(shaffle_count):
    shuffled_deck = []
    for (a, b) in zip(items[:len(items) // 2], items[len(items) // 2:]):
        shuffled_deck.append(b)
        shuffled_deck.append(a)

    items = shuffled_deck

final_list = start + items + end
print(final_list)
