def proprietatea1():
    n = int(input("Dati nr. de elemente din lista:"))
    lst = []
    for i in range(0, n):
        x = int(input(f"Dati elementul {i}: "))
        lst.append(x)
    print(f"Cea mai lunga secventa care are toate elementele nr. pare este: {get_longest_all_even(lst)}")


def get_longest_all_even(lst: list[int]):
    lg = len(lst)
    secvmax, start, end = 0, 0, 0

    for i in range(0, lg):
        if lst[i] % 2 == 0:
            st = i
            dr = 0
            for j in range(i, lg):
                if lst[j] % 2 == 0:
                    dr = j
                    if dr - st + 1 > secvmax:
                        secvmax = dr - st + 1
                        start = st
                        end = dr
                else:
                    break
    listnrpare = lst[start: end + 1]
    return listnrpare


def menu():
    should_run = True
    while should_run:
        optiune = input("Alegeti problema pe care vreti sa o rezolvati:")
        if optiune == "1":
            print("Problema 1: Cea mai lunga secventa care are toate elem. nr. pare:")
            proprietatea1()
        elif optiune == "2":
            print("Problema 2:")
        elif optiune == "x":
            should_run = False
        else:
            print("Ati ales o optiune gresita!")


menu()
