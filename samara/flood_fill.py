visited = set()
def paint(picture, x, y, old_char, new_char):

    if x < 0 or x >= len(picture) or y < 0 or y >= len(picture[0]):
        return
    if picture[x][y] != old_char:
        return

    picture[x][y] = new_char

    paint(picture, x+1, y, old_char, new_char)
    paint(picture, x-1, y, old_char, new_char)
    paint(picture, x, y+1, old_char, new_char)
    paint(picture, x, y-1, old_char, new_char)


picture = [
    "bbba",
    "abba",
    "acaa",
    "aaac"
]

picture = [list(row) for row in picture]

num_operations = 0
visited = set()

for i in range(len(picture)):
    for j in range(len(picture[0])):
        # If the character hasn't been seen yet (i.e., hasn't been converted to '*')
        if picture[i][j] != '*':
            old_char = picture[i][j]
            paint(picture, i, j, old_char, '*')
            num_operations += 1

print(f"Number of operations needed: {num_operations}")
