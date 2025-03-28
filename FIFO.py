tab = [0, 0, 0, 0, 0]

def FIFO(t):
    licznik = 0
    while licznik < 10:
        znak = input('Input sign: ')
        swap_right = t[0]
        t[0] = znak
        for i in range(1, 5):
            swap_left = swap_right
            swap_right = t[i]
            t[i] = swap_left
        licznik += 1
        print(t)

FIFO(tab)

