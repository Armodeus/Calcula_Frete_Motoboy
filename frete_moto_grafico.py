from tkinter import *


def calctarifa():
    tarifa = 0.00167
    dist1 = ed1.get()
    dist = float(dist1)
    metros = dist * 1000
    taxa = metros * tarifa

    if dist < 3:
        lb = Label(text='O valor da corrida é de R$ 5.00 ')  # texto direto na janela.
        lb.place(x=30, y=130)  # (POSIÇÃO DO TEXTO) (x) se refere a horizontal, (y) se refere a vertical.

    else:
        lb = Label(text='O valor da corrida é de: R$ {:.2f}'.format(taxa))  # texto direto na janela.
        lb.place(x=30, y=130)  # (POSIÇÃO DO TEXTO) (x) se refere a horizontal, (y) se refere a vertical.


janela = Tk()
janela.title('Cálculo Tele Entrega')

botao1 = Button(text='CALCULAR', command=calctarifa)
botao1.place(x=125, y=180)

lb = Label(text='FRETE MOTOBOY')  # texto direto na janela.
lb.place(x=110, y=10)  # (POSIÇÃO DO TEXTO) (x) se refere a horizontal, (y) se refere a vertical.

lb = Label(text='Utilize PONTO (.)')  # texto direto na janela.
lb.place(x=30, y=50)  # (POSIÇÃO DO TEXTO) (x) se refere a horizontal, (y) se refere a vertical.

lb = Label(text='DISTÂNCIA em KM:')  # texto direto na janela.
lb.place(x=30, y=80)  # (POSIÇÃO DO TEXTO) (x) se refere a horizontal, (y) se refere a vertical.
ed1 = Entry(janela)  # Modo de coleta atribuído a variável ed1 no elemento janela.
ed1.place(x=138, y=80)  # Posicionando o modo de entrada na janela

lb = Label(text='Valor de referência a cada 100 metros R$ 0.00167')  # texto direto na janela.
lb.place(x=10, y=260)  # (POSIÇÃO DO TEXTO) (x) se refere a horizontal, (y) se refere a vertical.

lb = Label(text='Desenvolvido por Márcio Diitter.')  # texto direto na janela.
lb.place(x=10, y=280)  # (POSIÇÃO DO TEXTO) (x) se refere a horizontal, (y) se refere a vertical.

janela.geometry('300x300')
janela.mainloop()
