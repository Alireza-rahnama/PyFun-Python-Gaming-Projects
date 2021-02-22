import sys

def hanoi(n, left):
    if n == 0:
        return " "
    move = str(n)
    move += "L" if left else "R"
    return hanoi(n-1, not(left)) + move + hanoi(n-1, not(left))

def main():
    n = int(sys.argv[1])
    print(hanoi(n, False))

main()
