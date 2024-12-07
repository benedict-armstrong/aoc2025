directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]

message = "XMAS"
mentions = 0
lines_out = []

with open("input.txt") as f:
    lines = f.readlines()
    for y, line in enumerate(lines):
        lines_out.append([])
        for x, char in enumerate(line.strip()):
            local = 0
            for d, dir in enumerate(directions):
                try:
                    coord = x, y
                    for i in range(len(message)):
                        if coord[0] < 0 or coord[1] < 0:
                            raise IndexError
                        if lines[coord[1]][coord[0]] != message[i]:
                            raise ValueError
                        coord = coord[0] + dir[0], coord[1] + dir[1]
                    else:
                        # found word
                        local += 1
                        mentions += 1
                except IndexError:
                    continue
                except ValueError:
                    continue
            if local > 0:
                lines_out[y].append(d)
            else:
                lines_out[y].append(0)


# with open("out.txt", "w") as f:
#     for line in lines_out:
#         line = map(str, line)
#         f.write("".join(line))
#         f.write("\n")


print(mentions)
