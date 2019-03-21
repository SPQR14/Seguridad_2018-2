def main():
    print("Algoritmo de Extendido de Euclides")
    a = int(input("El valor de a: "))
    b = int(input("El valor de b: "))
    print(euclides_extendido(a, b))


def euclides_extendido(a, b):
    a_aux = a
    b_aux = b
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
    while b != 0:
        q = a // b
        r = a - (b * q)
        x = x0 - (x1 * q)
        y = y0 - (y1 * q)
        print(r, q, x, y)
        a = b
        b = r
        x0 = x1
        x1 = x
        y0 = y1
        y1 = y
        if comprobacion(a_aux, b_aux, r, x, y):
            print("no se satisface la condición")
            break

    if y0 < 0:
        y0 = y0 + a_aux

    return a, x0, y0


def comprobacion(a, b, r, x ,y):
    flag = True
    if r == (a * x) + (b * y):
        flag = False
    return flag

main()
