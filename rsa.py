#!/usr/bin/python3

def check_prime(number):
    if number == 2:
        return True
    for num in range(2, number // 2):
        if number % num == 0:
            return False
    return True
        

def print_factors(number):
    for num in range(2, number):
        if (number % num == 0):
            if (check_prime(num)):
                fct = number // num
                if (check_prime(fct)):
                    print("{:d}={:d}*{:d}".format(number, fct, num))
                    break


def main():
    from sys import argv, exit, stderr

    if len(argv) != 2:
        stderr.write("Usage: ./factors <file>\n")
        exit()

    try:
        f = open(argv[1], "r")
    except FileNotFoundError:
        stderr.write("Could not find file {}, not exist\n".format(argv[1]))
    else:
        while (True):
            line = f.readline()
            if (not line):
                break
            line = int(line)
            print_factors(line)


main()
