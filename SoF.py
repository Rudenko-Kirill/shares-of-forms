import matplotlib.pyplot as plt
import numpy as np


ph_start = 0
ph_end = 14



def get_sh(m):  # m - pH
    A = 0
    shares = []
    for i in range(n + 1):  # Считает знаменатель для формулы долей форм
        A += 10 ** (-(i * m)) * const[len(const) - 1 - i]
    for j in range(n + 1):  # Считает долю (share) для каждой формы кислоты при данном pH и заносит в один список shares
        share = 10 ** (-(j * m)) * const[len(const) - 1 - j] / A
        shares.append(share)
    return shares


def get_max_point():
    print('Отрезок значений pH: от 0 до 14')
    for i in range(n + 1):
        print('Для формы', i + 1, 'максимальное значение доли', maximum_s[i], 'при pH', maximum_pH[i])


def get_ph_of_forms():
    pH = float(input('Введите pH: '))
    print('Доли форм при данном pH (от депротонированной к протонированной) :', get_sh(pH))


n = int(input('Введите основность: '))  # Основность кислоты
const = [1]
for i in range(n):
    a = float(input('Введите pKa: '))
    const.append(10 ** (-a) * const[i])
maximum_s = []
maximum_pH = []
for j in range(n + 1):
    x = []
    y = []
    for i in np.arange(ph_start, ph_end, 0.01):
        y.append(get_sh(i)[j])  # Доли форм
        x.append(i)  # pH
    plt.plot(x, y)
    maximum_s.append(max(y))
    maximum_pH.append(x[y.index(max(y))])
    y.clear()
get_max_point()
get_ph_of_forms()
plt.show()
