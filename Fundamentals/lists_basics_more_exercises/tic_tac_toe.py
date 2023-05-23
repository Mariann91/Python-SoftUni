row1, row2, row3 = input().split(), input().split(), input().split()

col1 = [row1[0], row2[0], row3[0]]
col2 = [row1[1], row2[1], row3[1]]
col3 = [row1[2], row2[2], row3[2]]

diagonal1 = [row1[0], row2[1], row3[2]]
diagonal2 = [row1[2], row2[1], row3[0]]
diagonal3 = [0, 0, 0]

rows = [row1, row2, row3]
cols = [col1, col2, col3]
diagonals = [diagonal1, diagonal2, diagonal3]

for i in range(3):
    if rows[i].count("1") == 3 or cols[i].count("1") == 3 or diagonals[i].count("1") == 3:
        print("First player won")
        break
    elif rows[i].count("2") == 3 or cols[i].count("2") == 3 or diagonals[i].count("2") == 3:
        print("Second player won")
        break
else:
    print("Draw!")
