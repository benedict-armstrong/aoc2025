message = "MAS"
mentions = 0
lines_out = []

with open("input.txt") as f:
    lines = f.readlines()
    for y in range(1, len(lines) - 1):
        lines_out.append([])
        for x in range(1, len(lines[y].strip())):
            if lines[y][x] == "A" and (
                (
                    (lines[y - 1][x - 1] == "M" and lines[y + 1][x + 1] == "S")
                    or (lines[y - 1][x - 1] == "S" and lines[y + 1][x + 1] == "M")
                )
                and (
                    (lines[y + 1][x - 1] == "M" and lines[y - 1][x + 1] == "S")
                    or (lines[y + 1][x - 1] == "S" and lines[y - 1][x + 1] == "M")
                )
            ):
                mentions += 1


print(mentions)
