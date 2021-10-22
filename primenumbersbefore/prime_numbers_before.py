#!/usr/bin/env python3

from canonicalrepresentation.canrepr import can_repr

def prime_nums_before(x: int) -> list:
    '''Take a positive integer and return all prime numbers not greater than that in ascending order.'''
    if x <= 0:
        try:
            print('\n\t' + 'Enter a positive integer!' + '\n')
            a = int(input('\t\t> '))
            return prime_nums_before(a)
        except:
            print('\n\t' + 'Enter a positive integer!' + '\n')
            a = int(input('\t\t> '))
            return prime_nums_before(a)
    result = []
    for i in range(2, x + 1):
        if [i] == can_repr(i):
            result.append(i)
    return result

def main():
    try:
        a = int(input('\t\t> '))
    except:
        print('\n\t' + 'Enter a positive integer!' + '\n')
        return main()
    print('\n\t' + 'RESULT: ', prime_nums_before(a), '\n')

def start():
    print('\n\t' + 'Enter a positive integer to find all prime numbers not greater than that:' + '\n')
    main()

if __name__ == '__main__':
    start()
