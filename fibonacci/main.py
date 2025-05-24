with open('fibonacci/input.txt', 'r') as f:
    input = f.read()

lines = input.splitlines()

for line in lines:
    test_case = line.strip()
    if not test_case:
        continue

    try:
        n = int(test_case)
    except ValueError:
        print("N/A")
        continue

    if n < 0:
        print("N/A")
        continue

    a, b = 0, 1
    fib_div3 = []
    while a <= n:
        if a % 3 == 0:
            fib_div3.append(a)
        a, b = b, a + b

    # Ha csak a 0 van benne, az nem számít megoldásnak
    if len(fib_div3) <= 1:
        print("N/A")
    else:
        print(", ".join(map(str, fib_div3)))
