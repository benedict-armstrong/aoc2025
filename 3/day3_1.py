from queue import Queue

sum = 0


def parse_seq(queue):
    n1 = []
    n2 = []
    temp_s = []
    second = False
    debug = ""
    while not q.empty():
        c = q.get()
        debug += c
        if not "".join(temp_s).endswith("mul("):
            temp_s.append(c)
            continue
        else:
            if c.isdigit():
                if second:
                    n2.append(c)
                else:
                    n1.append(c)
                continue
            if c == "," and n1:
                second = ","
            else:
                break
    else:
        print(f"{debug=}: {n1=}, {n2=}")
        if not n1 or not n2:
            return 0

        try:
            return int("".join(n1)) * int("".join(n2))
        except Exception as e:
            print(e)
            return 0

    return 0


# input mul(000,000)
q = Queue(maxsize=11)

with open("input.txt") as f:
    for line in f:
        for c in line:
            if c == ")":
                # proccess items if possible
                # check if queue contains: "mul(000,000"
                sum += parse_seq(q)
            else:
                if q.full():
                    q.get(block=False)
                q.put(c, block=False)

print(sum)
