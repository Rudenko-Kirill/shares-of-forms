import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np


def enter_pKa():
    def new_win():
        for j in range(z):
            a = float(en["var" + str(j)].get())
            const.append(10 ** (-a) * const[j])

        def sh(m):  # m - pH
            A = 0
            N1 = z
            N2 = z
            shares = []
            while N1 >= 0:  # Считает знаменатель для формулы долей форм
                A += 10 ** (-(N1 * m)) * const[len(const) - 1 - N1]
                N1 -= 1
            while N2 >= 0:  # Считает долю (share) для каждой формы кислоты при данном pH и заносит в один список shares
                share = 10 ** (-(N2 * m)) * const[len(const) - 1 - N2] / A
                shares.append(share)
                N2 -= 1
            return shares

        def gpH():
            pH = float(get_pH.get())
            for i in range(z + 1):
                ttk.Label(win2, text='При данном pH, для формы ' f'{i + 1}' ' доля равна ' f'{sh(pH)[i]}',
                          font=("Calibri", 11)).grid(row=z + 5 + i, column=0, stick='w')

        win1.destroy()
        win2 = tk.Tk()  # Создание второго окна
        win2.title('Доли форм')
        win2.geometry('700x500')
        maximum_s = []
        maximum_pH = []
        for j in range(z + 1):
            x = []
            y = []
            for i in np.arange(0, 14, 0.01):
                y.append(sh(i)[j])  # Доли форм
                x.append(i)  # pH
            plt.plot(x, y)
            maximum_s.append(max(y))
            maximum_pH.append(x[y.index(max(y))])
            y.clear()
        ttk.Label(win2, text='Отрезок значений pH: от 0 до 14', font=("Calibri", 12)).grid(row=0, column=0, stick='w')
        for i in range(z + 1):
            ttk.Label(win2,
                      text='Для формы ' f'{i + 1}' ' максимальная доля ' f'{maximum_s[i]}' ' при pH ' f'{maximum_pH[i]}',
                      font=("Calibri", 11)).grid(row=i + 1, column=0, stick='w')
        ttk.Label(win2, text='Введите значение pH:', font=("Calibri", 12)).grid(row=z + 2, column=0, sticky='w')
        get_pH = ttk.Entry(win2)
        get_pH.grid(row=z + 3, column=0, stick='w')
        ttk.Button(win2, text='Далее', command=gpH).grid(row=z + 4, column=0, stick='w')
        plt.show()

    btn1.state(['disabled'])
    z = int(ent1.get())  # Основность кислоты
    const = [1]  # Список с произведениями константы для A
    en = {}
    ttk.Label(win1, text='Введите pKa:').pack()
    for i in range(z):  # Создание полей для ввода pKa
        en["var" + str(i)] = ttk.Entry(win1)
        en["var" + str(i)].pack()
    btn2 = ttk.Button(win1, text='Сохранить', command=new_win)  # Кнопка для сохранения значений pKa
    btn2.pack()


win1 = tk.Tk()  # Создание и настройки первого окна
win1.title('Доли форм')
win1.geometry('400x300+580+240')
win1.minsize(200, 150)

lbl1 = ttk.Label(win1, text='Введите основность:')  # Заголовок
lbl1.pack()

ent1 = ttk.Entry(win1)  # Поле для воода основности кислоты
ent1.pack()

btn1 = ttk.Button(win1, text='Далее', command=enter_pKa)  # Кнопка для сохранения основности кислоты
btn1.pack()

win1.mainloop()
