def proprietatea1():
    n = int(input("Dati nr. de elemente din lista:"))
    lst = []
    for i in range(0, n):
        x = int(input(f"Dati elementul {i}: "))
        lst.append(x)
    print(f"Cea mai lunga secventa care are toate elementele nr. pare este: {get_longest_all_even(lst)}")

def proprietatea2():
    n = int(input("Dati nr. de elemente din lista:"))
    lst = []
    for i in range(0, n):
        x = int(input(f"Dati elementul {i}: "))
        lst.append(x)
    print(f"Cea mai lunga secventa care are acelasi nr de biti de 1: {get_longest_same_bit_counts(lst)}")

def proprietatea3():
    n = int(input("Dati nr. de elemente din lista:"))
    lst = []
    for i in range(0, n):
        x = int(input(f"Dati elementul {i}: "))
        lst.append(x)
    print(f"Cea mai lunga secventa in care nr au acelasi nr de divizori: {get_longest_same_div_count(lst)}")

def get_longest_all_even(lst: list[int]):
    """
    Returneaza subsecventa maxima cu proprietatea ca toate numerele consecutive sunt pare
    :param lst: lista de nr intregi
    :return: subsecventa maxima
    """
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

def test_get_longest_all_even():
    assert get_longest_all_even([10, 9, 8, 2, 6, 14, 11]) == [8, 2, 6, 14]


def bit_1_counter_in_base_2(x: int) -> int:
    '''
    Returneaza numarul de cate ori apare 1 in scrierea binara
    :param x: numar intreg
    :return: counter: numar intreg
    '''
    counter = 0
    while x:
        counter = counter + x % 2
        x = x//2
    return counter


def get_longest_same_bit_counts(lst: list[int]) -> list[int]:
    '''
    Returneaza subsecventa maxima cu proprietea ca toate elementele sa aiba acelasi numar de cifra 1 in scrierea binara
    Functia afla subsecventa maxima prin verificarea continua a doi termeni consecutivi
    :param lst: lista de numere intregi
    :return: subsecventa_maxima: lista de numere intregi
    '''
    i = 1
    pozitia_initiala = 0
    pozitia_finala = 0
    subsecventa_maxima = [lst[0]]
    while i < len(lst):
        if bit_1_counter_in_base_2(lst[i-1]) == bit_1_counter_in_base_2(lst[i]):
            pozitia_finala = i
        else:
            pozitia_initiala = i
        if len(lst[pozitia_initiala:pozitia_finala+1]) > len(subsecventa_maxima):
            subsecventa_maxima = lst[pozitia_initiala:pozitia_finala+1]
        i=i+1
    return subsecventa_maxima


def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([16, 454, 7, 6, 10, 7, 10, 6, 5, 16, 454]) == [10,6,5]
    assert get_longest_same_bit_counts([10, 454, 6]) == [10]

def nrDivizori(a: int):
    '''
    Determina numarul divizorilor
    :param a: int
    :return: numar divizori
    '''
    x=1
    s=0
    while x<=a:
        if a % x == 0:
            s+=1
        x+=1
    return s

def get_longest_same_div_count(lst: list[int]):
    """
    Determina subsecventa maxima in care nr au acelasi nr de divizori
    :param lst: lista
    :return: subsecventa maxima
    """
    i=0
    nr=len(lst)-1
    st=0
    dr=0
    while i < nr:
        count=1
        if nrDivizori(lst[i]) == nrDivizori(lst[i+1]):
            while i < nr and nrDivizori(lst[i]) == nrDivizori(lst[i+1]) :
                i+=1
                count+=1
            if dr-st+1 < count :
                st=i-count+1
                dr=i
        else:
            i+=1
    return lst[st:dr+1]


def test_get_longest_same_div_count():
    assert get_longest_same_div_count([1,2,3,4,5]) ==[2,3]
    assert get_longest_same_div_count([2,4,6,8,10]) ==[6,8,10]
    assert get_longest_same_div_count([3,5,7]) ==[3,5,7]
    assert get_longest_same_div_count([1]) ==[1]


def menu():
    test_get_longest_same_div_count()
    test_get_longest_same_bit_counts()
    should_run = True
    while should_run:
        optiune = input("Alegeti problema pe care vreti sa o rezolvati:")
        if optiune == "1":
            print("Problema 1: Cea mai lunga secventa care are toate elem. nr. pare:")
            proprietatea1()
        elif optiune == "2":
            print("Problema 2: Cea mai lunga secventa care are acelasi nr de biti de 1")
            proprietatea2()
        elif optiune == "3":
            print("Problema 3: Cea mai lunga secventa in care nr au acelasi nr de divizori:")
            proprietatea3()
        elif optiune == "x":
            should_run = False
        else:
            print("Ati ales o optiune gresita!")


menu()