#!/usr/bin/env python3

import sys
import operator
import argparse

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def eval_tokens(a_str, op, b_str):
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        raise ValueError("Invalid numeric input.")
    if op not in OPERATIONS:
        raise ValueError(f"Unsupported operator: {op}")
    if op == '/' and b == 0:
        raise ZeroDivisionError("Division by zero.")
    return OPERATIONS[op](a, b)

def interactive_loop():
    print("Simple calculator. Enter expressions like: 2 + 3  (type 'quit' to exit)")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            return
        if not line:
            continue
        if line.lower() in ('quit', 'exit'):
            print("Goodbye.")
            return
        parts = line.split()
        if len(parts) != 3:
            print("Please enter expressions as: <number> <op> <number> (e.g. 4 * 5)")
            continue
        a_str, op, b_str = parts
        try:
            result = eval_tokens(a_str, op, b_str)
        except Exception as e:
            print("Error:", e)
        else:
            print("=", result)

def main():
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument('a', nargs='?', help='left operand')
    parser.add_argument('op', nargs='?', help='operator (+ - * /)')
    parser.add_argument('b', nargs='?', help='right operand')
    args = parser.parse_args()

    if args.a is None:
        interactive_loop()
        return

    try:
        result = eval_tokens(args.a, args.op, args.b)
    except Exception as e:
        print("Error:", e)
        sys.exit(2)
    else:
        print(result)

if __name__ == "__main__":
    main()
