def sum_invalid_ids_general(raw_input_line):
    ranges = []
    for part in raw_input_line.strip().split(","):
        if not part:
            continue
        lo, hi = part.split("-")
        ranges.append((int(lo), int(hi)))

    max_val = max(r[1] for r in ranges)

    invalids = []

    max_len = len(str(max_val))

    for base_len in range(1, max_len // 2 + 1):  
        start = 10**(base_len - 1) if base_len > 1 else 1
        end = 10**base_len
        for base in range(start, end):
            repeated_str = str(base)
            repeated_num = int(repeated_str * 2)  
            while repeated_num <= max_val:
                invalids.append(repeated_num)
                repeated_str += str(base)
                repeated_num = int(repeated_str)

    invalids = sorted(set(invalids))

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
    print(sum_invalid_ids_general(line))