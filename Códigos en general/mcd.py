def main():
    print("******Euclides*****")
    a = 986
    b = 14

    print("El máximo común dividor entre %1 y %i es %i", a, b, mcd(a, b))


def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


main()
