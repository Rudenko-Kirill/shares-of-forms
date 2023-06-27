import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter.messagebox import showerror
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

win1_wl = '960x555'
win_title = 'Shares of forms'
const = [1]
en = {}
ph_start = 0
ph_end = 14


def get_basicity():
    if ent1.get() == '':
        showerror(title='Error', message='You must enter the value of the basicity')
    else:
        btn1.state(['disabled'])
        ent1.state(['disabled'])
        ttk.Label(win1, text='Enter pKa:', font=fontB).place(w=110, h=25, x=5, y=30)
        for i in range(int(ent1.get())):
            en["var" + str(i)] = ttk.Entry(win1)
            en["var" + str(i)].place(x=92 + 80 * i, y=30, h=25, w=75)
        btn2.place(x=92 + 80 * int(ent1.get()), y=30, h=25, w=75)


def get_pka():
    counter_of_errors = 0
    for j in range(int(ent1.get())):
        if en["var" + str(j)].get() == '':
            counter_of_errors += 1
    if counter_of_errors == 0:
        for i in range(int(ent1.get())):
            a = float(en["var" + str(i)].get())
            const.append(10 ** (-a) * const[i])
            en["var" + str(i)].state(['disabled'])
        fig = Figure(figsize=(6, 6),
                     dpi=100)
        plot1 = fig.add_subplot(111)
        btn2.state(['disabled'])
        maximum_s = []
        maximum_ph = []
        for J in range(int(ent1.get()) + 1):
            x = []
            y = []
            for i in np.arange(0, 14, 0.01):
                y.append(get_sh(i)[J])
                x.append(i)  # pH
            plot1.plot(x, y)
            maximum_s.append(max(y))
            maximum_ph.append(x[y.index(max(y))])
            y.clear()
        frame1 = ttk.Frame(borderwidth=1, relief='solid', height=30 * (int(ent1.get()) + 1), width=345, padding=2.5)
        ttk.Label(win1, text='pH from 0 to 14', font=fontB).place(x=5, y=65, height=25)
        for I in range(int(ent1.get()) + 1):
            ttk.Label(frame1,
                      text='For form ' f'{int(ent1.get()) - I + 1}' ' max share is ' f'{round(maximum_s[I], 5)}' ' when pH is ' f'{round(maximum_ph[I], 2)}',
                      font=fontS).place(x=0, y=30 * I, h=20, width=340)
        ttk.Label(win1, text='Enter pH:', font=fontB).place(x=5, y=100 + 30 * (int(ent1.get()) + 1), h=25)
        ent2.place(x=85, y=100 + 30 * (int(ent1.get()) + 1), h=25, w=75)
        ttk.Button(win1, text='Count', command=get_ph).place(x=165, y=100 + 30 * (int(ent1.get()) + 1), h=25)

        canvas = FigureCanvasTkAgg(fig,
                                   master=win1)
        canvas.get_tk_widget().place(y=65, x=355, height=485)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas,
                                       win1)
        toolbar.update()
        toolbar.place(x=355, y=65)
        frame1.place(x=5, y=95)
    else:
        showerror(title='Error', message='You must enter all pKa values')


def get_sh(m):
    A = 0
    shares = []
    for i in range(int(ent1.get()) + 1):
        A += 10 ** (-(i * m)) * const[len(const) - 1 - i]
    for j in range(int(ent1.get()) + 1):
        share = 10 ** (-(j * m)) * const[len(const) - 1 - j] / A
        shares.append(share)
    return shares


def get_ph():
    if ent2.get() == '':
        showerror(title='Error', message='You must enter the value of the pH')
    else:
        frame2 = ttk.Frame(borderwidth=1, relief='solid', height=30 * (int(ent1.get()) + 1), width=345, padding=2.5)
        ph = float(ent2.get())
        for i in range(int(ent1.get()) + 1):
            ttk.Label(frame2,
                      text='For form ' f'{int(ent1.get()) - i + 1}' ' share is ' f'{round(get_sh(ph)[i], 6)}',
                      font=fontS).place(x=0, y=30 * i, h=20, width=340)

        frame2.place(y=130 + 30 * (int(ent1.get()) + 1), x=5)


win1 = tk.Tk()
win1.title(win_title)
win1.geometry(win1_wl)
fontB = tkFont.Font(family='Segoe UI', size=12, underline=True)
fontS = tkFont.Font(family='Segoe UI', size=11)
ttk.Label(win1, text='Enter basicity:', font=fontB).place(w=110, h=25, x=5, y=0)
ent1 = ttk.Entry(win1)
ent1.place(x=120, y=0, h=25, w=75)
btn1 = ttk.Button(win1, text='Save', command=get_basicity)
btn1.place(x=200, y=0, h=25)
btn2 = ttk.Button(win1, text='Save', command=get_pka)
ent2 = ttk.Entry(win1)

win1.iconbitmap('Image.ico')
win1.mainloop()
