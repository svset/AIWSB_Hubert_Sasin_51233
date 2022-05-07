def obcinaj(s):
    print(s[1:4])
obcinaj("nauka")

def max_sum(a, b, c):
    print(max(a, b, c))
max_sum(3, 8, -4)

def wybierz_parzyste(x):
    for i in x:
        if i % 2 == 0:
            print(i)
wybierz_parzyste([1, 2, 3, 4, 5, 6, 7])

def pole_trapezu(a, b, h):
    print((a+b)*h)
pole_trapezu(7, 9 ,3)
