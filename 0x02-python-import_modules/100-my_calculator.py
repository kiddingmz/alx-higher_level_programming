#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv)

    if num_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a, b = int(sys.argv[1]), int(sys.argv[3])

    if op == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif op == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
