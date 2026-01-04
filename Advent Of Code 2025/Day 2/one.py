def sum_invalid_ids(raw_input_line):
    ranges = []
    for part in raw_input_line.strip().split(","):
        if not part:
            continue
        lo, hi = part.split("-")
        ranges.append((int(lo), int(hi)))
    
    max_val = max(r[1] for r in ranges)
    invalids = []

    max_len = len(str(max_val))

    for length in range(2, max_len + 1):
        if length % 2 != 0:
            continue  
        half = length // 2

        start = 10 ** (half - 1)
        end   = 10 ** half

        for base in range(start, end):
            repeated = int(str(base) * 2)
            if repeated > max_val:
                break
            invalids.append(repeated)

    total = 0
    for val in invalids:
        for lo, hi in ranges:
            if lo <= val <= hi:
                total += val
                break

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        line = f.read()
    print(sum_invalid_ids(line))