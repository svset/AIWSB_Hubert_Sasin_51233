a = 25

if a % 2 == 0:
    print(a, "jest parzysta")

else:
    print(a, "nie jest parzysta")
    if a % 3 == 0:
        print(a, "nie jest parzysta, ale jest podzielna przez 3")
    else:
        print(a, "nie jest parzysta i nie dzieli się przez 3")