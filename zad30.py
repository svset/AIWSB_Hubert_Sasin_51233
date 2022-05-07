def liczba_pierwsza(x):
    for i in range(2, x):
        if x % i == 0:
            return 0
        return 1

    liczba = int(input("Podaj liczbę: "))

    if liczba_pierwsza(liczba) == 1:
        print("Jest to liczba pierwsza")
    else:
        print("Nie jest to liczba pierwsza")
