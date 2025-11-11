n = int(input())
if n > 3999 or n <= 0:
    print("NoProceed")
else: 
    symbolic_numbers = [
        (1000, "M"),
        (900, "ZM"),
        (500, "D"),
        (400, "ZD"),
        (100, "Z"),
        (90, "XZ"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "AX"),
        (5, "V"),
        (4, "AV"),
        (1, "A")
    ]
    result = ""
    for value, symbol in symbolic_numbers:
        while n >= value:
            result += symbol
            n -= value
    print(result)