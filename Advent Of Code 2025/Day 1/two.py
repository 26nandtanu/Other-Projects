def count_all_zero_hits(path):
    pos = 50          # starting position
    zeros = 1 if pos == 0 else 0  # count if starting is 0 (it's not, but keep logic clean)

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            dist = int(line[1:])

            step = -1 if direction == "L" else 1

            # simulate each click
            for _ in range(dist):
                pos = (pos + step) % 100
                if pos == 0:
                    zeros += 1

    return zeros


if __name__ == "__main__":
    print(count_all_zero_hits("input.txt"))