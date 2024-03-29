#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]

        if op == "+":
            result = calc.add(a, b)
        elif op == "-":
            result = calc.sub(a, b)
        elif op == "*":
            result = calc.mul(a, b)
        elif op == "/":
            result = calc.div(a, b)
        else:
            result = None
        if result is None:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            print("{} {} {} = {}".format(a, op, b, result))
