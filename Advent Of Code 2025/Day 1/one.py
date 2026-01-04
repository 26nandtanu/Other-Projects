def count_zeros_from_file(path):
    pos = 50          # starting position
    zeros = 0

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            dist = int(line[1:])

            if direction == "L":
                pos = (pos - dist) % 100
            else:  # direction == "R"
                pos = (pos + dist) % 100

            if pos == 0:
                zeros += 1

    return zeros


if __name__ == "__main__":
    print(count_zeros_from_file("input.txt"))