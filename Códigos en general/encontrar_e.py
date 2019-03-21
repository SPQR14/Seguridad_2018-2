def main():
    fi = (7 - 1)*(13 - 1)
    print(buscar_e(fi))

def buscar_e(fi):
    for i in range(15, 73):
        if mcd(i, fi) == 1:
            break
    return i

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

main()