a, b = map(int, input().split())
c = int(input())


def conjuction(x, y):
    return x & y


def disjunction(x, y):
    return x | y


def implication(x, y):
    return ((not x) | y)


def equivalence(x, y):
    return int(x == y)


def xor(x, y):
    return a ^ b


def nor(x, y):
    return int(not (x | y))


def nand(x, y):
    return int(not (x & y))


match c:
    case 1:
        print(conjuction(a, b))
    case 2:
        print(disjunction(a, b))
    case 3:
        print(implication(a, b))
    case 4:
        print(equivalence(a, b))
    case 5:
        print(xor(a, b))
    case 6:
        print(nor(a, b))
    case 7:
        print(nand(a, b))
