#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length_args = len(sys.argv)

    if length_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = ('+', '-', '*', '/')
    args = sys.argv
    operator = args[2]

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div

    a, b = int(args[1]), int(args[3])

    if operator == operators[0]:
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == operators[1]:
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif operaror == operators[2]:
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

    sys.exit(0)
