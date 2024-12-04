class Command:
    def __init__(self, seq: str, num_args: int = 0) -> None:
        self.seq = seq
        self.num_args = num_args
        self.reset()

    def add(self, char: str):
        if self.accept_args:
            if char == ")":
                if len(self.args) != self.num_args:
                    self.reset()
                else:
                    self.valid = True
                    self.accept_args = False
            elif self.num_args and len(self.args) <= self.num_args:
                # read args
                if not self.args:
                    self.args.append("")
                if char == ",":
                    self.args.append("")
                    return
                self.args[-1] += char
            else:
                self.reset(char)

        else:
            if self.i == len(self.seq):
                if char == "(":
                    self.accept_args = True
                else:
                    self.reset(char)

            elif self.seq[self.i] != char:
                self.reset()
            else:
                self.i += 1

    def reset(self, add=None):
        self.i = 0
        self.accept_args = False
        self.valid = False
        self.args = []
        if add:
            self.add(add)

    def __bool__(self):
        return self.valid

    def get_args(self):
        args = self.args
        self.reset()
        return args


mul = Command("mul", args=2)
do = Command("do")
dont = Command("don't")

commands = [mul, do, dont]
read_on = True
sum = 0

with open("input.txt") as f:
    for line in f:
        for i, c in enumerate(line):
            for b in commands:
                b.add(c)

            if do:
                read_on = True

            if not read_on:
                continue

            if dont:
                read_on = False
                continue

            if mul:
                args = mul.get_args()

                if len(args) != 2:
                    continue

                try:
                    n1 = int(args[0])
                    n2 = int(args[1])
                    if not (0 <= n1 < 1000) or not (0 <= n2 < 1000):
                        continue
                    sum += n1 * n2
                except ValueError:
                    continue

print(sum)
