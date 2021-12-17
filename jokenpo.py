"""
DEV. PAULO CARDOSO
JOKENPÔ COM INTERFACE GRÁFICA
"""
"""
Bibliotecas usadas para aplicação
"""
from tkinter import *
from random import choice

player = ''

def jogo_inicial():
    """
    Atributos iniciais para aplicação
    """
    mao = ['pedra','papel','tesoura']
    pc = choice(mao)

    """
    Configurações iniciais do tkinter (titulo, dimensão, icone, etc)
    """
    global menu_inicial
    menu_inicial = Tk() #cria um model Tk()
    menu_inicial.title("JOKENPÔ") #atribui um titulo para aplicação
    menu_inicial.geometry("800x600+100+100") #largura x altura posX posY
    menu_inicial.resizable(False,False) #não é possivel redimensionar
    menu_inicial.iconbitmap("image/icon.ico") #alterar o icone da aplicação
    """
    Criando um titulo
    """
    Label(menu_inicial, text="JOKENPÔ", font=('Arial Black', 15)).pack(side=TOP, pady=10)
    """
    Tratando imagens para serem usadas nos botões citados abaixo
    """
    photoPapel = PhotoImage(file="image/papel.png")
    photoimagePapel = photoPapel.subsample(4,4)
    photoPedra = PhotoImage(file="image/pedra.png")
    photoimagePedra = photoPedra.subsample(4,4)
    photoTesoura = PhotoImage(file="image/tesoura.png")
    photoimageTesoura = photoTesoura.subsample(4,4)
    """
    Criando uma Frame paras os botões citados abaixo
    """
    bottomframe = Frame(menu_inicial)
    bottomframe.pack(side=TOP)
    Label(bottomframe, text="Escolhe uma mão: Pedra, Papel ou Tesoura?", font=('Arial', 12)).pack(side=TOP, pady=10)
    def teste(msg):
        global player
        player = msg
        bottomframe.destroy()
        menu_inicial.after(0, iniciar)
    """
    Criando um botão padrão apenas para teste
    """
    Button(bottomframe, text="Pedra", image=photoimagePedra, compound=TOP, cursor="hand2", command=lambda: teste('pedra')).pack(side=LEFT,padx=5)
    Button(bottomframe, text="Papel", image=photoimagePapel, compound=TOP, cursor="hand2", command=lambda: teste('papel')).pack(side=LEFT,padx=5)
    Button(bottomframe, text="Tesoura", image=photoimageTesoura, compound=TOP, cursor="hand2", command=lambda: teste('tesoura')).pack(side=LEFT,padx=5)
    """
    Criando uma Frame paras as labels abaixo
    """
    labelframe = Frame(menu_inicial)
    labelframe.pack(side=TOP)
    """
    Criando um Label para exibir abaixo dos botões
    """
    def iniciar():
        Label(labelframe, text="JO", font=('Arial Black', 30)).pack(side=LEFT, pady=20)
        menu_inicial.after(1000, carregando)

    def carregando():
        Label(labelframe, text="KEN", font=('Arial Black', 30)).pack(side=LEFT, pady=20)
        menu_inicial.after(1000, concluido)

    def concluido():
        Label(labelframe, text="PÔ", font=('Arial Black', 30)).pack(side=LEFT, pady=20)
        menu_inicial.after(5, mostrarResultado)
    """
    Criando algumas frames para mostrar as informaçõs, o resultado e a opcção de reiniciar
    """
    infoframe = Frame(menu_inicial)
    infoframe.pack(side=TOP)

    btinfoframe = Frame(menu_inicial)
    btinfoframe.pack(side=TOP)

    resulframe = Frame(menu_inicial)
    resulframe.pack(side=TOP)

    opframe = Frame(menu_inicial)
    opframe.pack(side=TOP)


    def mostrarResultado():
        Label(infoframe, text="Você escolheu", font=('Arial', 12)).pack(side=LEFT, pady=2, padx=20)
        Label(infoframe, text="PC escolheu", font=('Arial', 12)).pack(side=LEFT, pady=2, padx=20)
        mostrarPlayer()
        mostrarPc()
        if player == pc:
            Label(resulframe, text="Jogo empatado! Jogue novamente!", font=('Arial Black', 15)).pack(side=LEFT, pady=10)
        elif (player == 'pedra' and pc == 'tesoura') or (player == 'papel' and pc == 'pedra') or (player == 'tesoura' and pc == 'papel'):
            Label(resulframe, text="Parabêns! Você venceu!", font=('Arial Black', 15)).pack(side=LEFT, pady=10)
        elif (pc == 'pedra' and player == 'tesoura') or (pc == 'papel' and player == 'pedra') or (pc == 'tesoura' and player == 'papel'):
            Label(resulframe, text="Que Pena! O PC venceu!", font=('Arial Black', 15)).pack(side=LEFT, pady=10)
        else:
            print('Escolha invalida! Por favor, tente novamente!')

        Button(opframe, text="Reiniciar", cursor="hand2", font=('Arial Black', 12), command=lambda: reiniciar()).pack(side=LEFT,pady=20, padx=5)

    def mostrarPc():
        if(pc == 'pedra'):
            return Button(btinfoframe, text="Pedra", image=photoimagePedra, compound=TOP).pack(side=LEFT, padx=5)
        elif(pc == 'papel'):
            return Button(btinfoframe, text="Papel", image=photoimagePapel, compound=TOP).pack(side=LEFT, padx=5)
        else:
            return Button(btinfoframe, text="Tesoura", image=photoimageTesoura, compound=TOP).pack(side=LEFT, padx=5)

    def mostrarPlayer():
        if (player == 'pedra'):
            return Button(btinfoframe, text="Pedra", image=photoimagePedra, compound=TOP).pack(side=LEFT, padx=5)
        elif (player == 'papel'):
            return Button(btinfoframe, text="Papel", image=photoimagePapel, compound=TOP).pack(side=LEFT, padx=5)
        else:
            return Button(btinfoframe, text="Tesoura", image=photoimageTesoura, compound=TOP).pack(side=LEFT, padx=5)

    menu_inicial.mainloop() #exibi o model Tk() criado com as configurações especificadas

if __name__ == "__main__":
    def reiniciar():
        menu_inicial.destroy()
        global player
        player = ''
        jogo_inicial()

    jogo_inicial()
