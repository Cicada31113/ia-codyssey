def main():
    try:
        base = float(input("Enter number:"))
    except ValueError:
        print("Invalid number input.")
        return
    try:
        exponent = int(input("Enter exponent:"))
    except ValueError:
        print("Invalid exponet input.")
        return
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0: 
        result = 1 / result

    print("Result:",result)

if __name__ == "__main__":
    main()


