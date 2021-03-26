from tkinter import *
from math import log10
background_color = '#95d5b2'

#Interface
janela = Tk()
janela.title('pH of a Buffer')
janela['bg'] = background_color

global kab1
#defs
def resultado():
    global kab1
    if rb1.get() == 1 and rb2.get() == 1 or rb1.get() == 2 and rb2.get == 2:
        kab1 = float(kab.get())
    else:
        kab1 = (10**-14)/float(kab.get())
    c_sal = float(csal.get())
    c_a = float(ca.get())
    a = 1
    b = (c_sal + kab1)
    c = float(((c_a))*(kab1)*(-1))
    dlt = (float(((b)**2) - (4*a*c)))
    dlt_sqrt = float(dlt**(1/2))
    delta_resultado['text'] = round(dlt,4) , 'e', round(dlt_sqrt,4)
    x1 = float((-b - dlt_sqrt) / (2))
    x2 = float((-b + dlt_sqrt) / (2))
    if x1 < 0:
        x = x2
    else:
        x = x1
    x_resultado['text'] = round(x,8) ,'mol/L'
    pH = (-log10(x))
    pOH = (14 - pH)
    if rb1.get() == 1:
        ph_resultado['text'] = round(pH,4)
    else:
        ph_resultado['text'] = round(pOH,4)

#RadioButtons
rb1 = IntVar()
rb2 = IntVar()
Radiobutton(text='Acid', bg=background_color, variable = rb1, value = 1).place(x=205,y=0)
Radiobutton(text='Base', bg=background_color, variable = rb1, value = 2).place(x=260,y=0)
Radiobutton(text='Ka', bg=background_color, variable = rb2, value = 1).place(x=205,y=20)
Radiobutton(text='Kb', bg=background_color, variable = rb2, value = 2).place(x=260,y=20)

#Buttons
button = Button(janela, text ='Calculate', command = resultado)
button.place(x=170, y=200)

#Texts
lab = Label(janela, text = 'Is your solution basic or acidic?', bg=background_color)
lab.place(x=0,y=0)
lkab = Label(janela, text = 'Do you have the value of Ka or Kb?', bg=background_color)
lkab.place(x=0,y=20)
lv_kab = Label(janela, text='Indicate its value: ', bg=background_color)
lv_kab.place(x=0,y=40)
lca = Label(janela, text = 'Concentration of the acid/base :', bg=background_color)
lca.place(x=0,y=60)
lsal = Label(janela, text = 'Concentration of the salt :', bg=background_color)
lsal.place(x=0,y=80)

#Data input
kab = Entry(janela, bg=background_color)
kab.place(x=210,y=40)
ca = Entry(janela, bg=background_color)
ca.place(x=210,y=60)
csal = Entry(janela, bg=background_color)
csal.place(x=210,y=80)

#Results
delta = Label(janela, text = 'Value of Delta and its square root: ', bg=background_color)
delta.place(x=0,y=120)
delta_resultado = Label(janela, text = '', bg=background_color)
delta_resultado.place(x=205,y=120)
x = Label(janela, text = 'Value of x: ', bg=background_color)
x.place(x=0,y=140)
x_resultado = Label(janela, text = '', bg=background_color)
x_resultado.place(x=205,y=140)
ph = Label(janela,text = 'pH: ', bg =background_color)
ph.place(x=0,y=160)
ph_resultado = Label(janela,text = '', bg =background_color)
ph_resultado.place(x=205,y=160)

#Screen size and mainloop
janela.geometry('400x230+500+250')
janela.mainloop()