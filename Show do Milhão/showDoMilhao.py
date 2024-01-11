import time
import flet as ft

controle = [0]
#Função para criar a tela inicial
def inicial(page):
    page.clean()
    page.bgcolor = "#9b87bc"   
    
    #Adicionando e tratando a imagem da Rommanel
    imagem = ft.Image(src="rommanel.png", width=600, height=200)
    row_img = ft.Row(controls=[imagem], alignment="center")
    
    #Adicionando texto   
    t = ft.Text(value="SHOW DO MILÃO", color="white",size=60,font_family="arial")
    row_t = ft.Row(controls=[t], alignment="center")
    
    btn1 = criar_botao(texto="Iniciar Jogo 1")
    btn2 = criar_botao(texto="Iniciar Jogo 2")

    btn1.on_click = lambda event: acao2(btn1,page)
    btn2.on_click = lambda event: acao2(btn2,page)

    btn_line_1 = ft.Row(controls=[btn1],alignment=ft.MainAxisAlignment.CENTER)
    btn_line_2 = ft.Row(controls=[btn2],alignment=ft.MainAxisAlignment.CENTER)
    
    coluna1 = ft.Column(controls=[row_img, row_t], spacing=50)
    coluna2 = ft.Column(controls=[btn_line_1,btn_line_2], spacing=70)
    coluna = ft.Column(controls=[coluna1,coluna2], spacing=60)
    page.add(coluna)

#Função para mudar da tela inicial à tela de perguntas
def acao2(button, page):
    global lista_principal
    if button.text == "Iniciar Jogo 1":
        controle[0] = 1
        trataArq(1)
        criaPagina(page)
    elif button.text == "Iniciar Jogo 2":
        controle[0] = 2
        trataArq(2)
        criaPagina(page)

lista_principal = []
lista_ganhos = []
lista_partes = []
ganhos = []

def trataArq(controle):    
    if controle == 1:
        with open("perguntas.txt", "r",encoding="utf-8") as arquivo: #abrindo o caminho base passado pelo usuário e convertendo para lista
            lista_principal = arquivo.readlines()
    if controle == 2:
        with open("perguntas2.txt", "r",encoding="utf-8") as arquivo: #abrindo o caminho base passado pelo usuário e convertendo para lista
            lista_principal = arquivo.readlines()

    with open("valores.txt", "r",encoding="utf-8") as arquivo: #abrindo o caminho base passado pelo usuário e convertendo para lista
        lista_ganhos = arquivo.readlines()

    lista_limpa_ganhos = []
    lista_limpa = []
    linhas = 0

    for linha in lista_principal: #removendo o \n ao final de cada linha
        lista_limpa.append(linha.strip("\n"))
        linhas+=1
        
    for linha in lista_ganhos: #removendo o \n ao final de cada linha
        lista_limpa_ganhos.append(linha.strip("\n"))

    lista_parte = []
    
    i=0
    for linha in lista_limpa:
        if i==6:
            lista_parte.append(linha)
            lista_partes.append(lista_parte)
            lista_parte = []
            i=-1
        else:
            lista_parte.append(linha)
        i+=1

    for linha in lista_limpa_ganhos:
        ganhos.append(linha)
        
guia_perguntas = [0]
guia_valores= [0]
        

def criaPagina(page):
    page.clean()
    
    page.bgcolor = "#9b87bc"   
    
    #Adicionando e tratando a imagem da Rommanel
    imagem = ft.Image(src="rommanel.png", width=600, height=200)
    row_img = ft.Row(controls=[imagem], alignment="center")
    
    #Adicionando e tratando o texto da pergunta    
    t = ft.Text(value=lista_partes[guia_perguntas[0]][0], color="white",size=40,font_family="arial")
    row_t = ft.Row(controls=[t], alignment="center")
    
    btnA = criar_botao(texto=lista_partes[guia_perguntas[0]][1])
    btnB = criar_botao(texto=lista_partes[guia_perguntas[0]][2])
    btnC = criar_botao(texto=lista_partes[guia_perguntas[0]][3])
    btnD = criar_botao(texto=lista_partes[guia_perguntas[0]][4])

    btnA.on_click = lambda event: acao(btnA,page)
    btnB.on_click = lambda event: acao(btnB,page)
    btnC.on_click = lambda event: acao(btnC,page)
    btnD.on_click = lambda event: acao(btnD,page)


    btn_line_1 = ft.Row(controls=[btnA,btnB],alignment=ft.MainAxisAlignment.CENTER)
    btn_line_2 = ft.Row(controls=[btnC,btnD],alignment=ft.MainAxisAlignment.CENTER)
    
    coluna1 = ft.Column(controls=[row_img, row_t], spacing=50)
    coluna2 = ft.Column(controls=[btn_line_1,btn_line_2], spacing=70)
    coluna = ft.Column(controls=[coluna1,coluna2], spacing=60)
    page.add(coluna)     
    
def criar_botao(texto):
    if (guia_perguntas[0] == 7 and controle[0] ==2)  or (guia_perguntas[0] == 14 and controle[0] == 2):
        return ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value=texto, color="#9b87bc", size=28, width=700, height=55, text_align="center",font_family="arial"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=15,
                ),
            ),
            bgcolor="white",
            text=texto,
        )
    else:
        return ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value=texto, color="#9b87bc", size=40, width=700, height=55, text_align="center",font_family="arial"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=15,
                ),
            ),
            bgcolor="white",
            text=texto,
        )

    
def acao(button, page):
        #Tratando uma resposta errada
        if button.text != lista_partes[guia_perguntas[0]][5]:
            def final():
                global lista_principal
                global lista_ganhos
                global lista_partes
                global ganhos
                global guia_perguntas
                global guia_valores
                lista_principal = []
                lista_ganhos = []
                lista_partes = []
                ganhos = []
                guia_perguntas = [0]
                guia_valores= [0]
                inicial(page)
                
            page.bgcolor = "#c41010" 
            if guia_valores[0] == 0:
                txt_erro1 = ft.Text(value="ERRRRROUUU KKKKKKKKK, seu prêmio é: Nada", color="white",size=40,font_family="arial")
                row_txt_erro1 = ft.Row(controls=[txt_erro1], alignment="center")
            else:
                txt_erro1 = ft.Text(value="ERRRRROUUU KKKKKKKKK, seu prêmio é: " + ganhos[guia_valores[0]-1], color="white",size=40,font_family="arial")
                row_txt_erro1 = ft.Row(controls=[txt_erro1], alignment="center")
            
            
            txt_erro2 = ft.Text(value="Resposta correta: " + lista_partes[guia_perguntas[0]][5], color="white",size=40,font_family="arial")
            row_txt_erro2 = ft.Row(controls=[txt_erro2], alignment="center")
            
            btnErro = criar_botao(texto="Sair")
            btnErro.on_click = lambda event: final()
            row_btn_erro = ft.Row(controls=[btnErro], alignment="center")
            
            espaco_acima = ft.Text(value="", size=10)
            
            colunaErro = ft.Column(controls=[espaco_acima, row_txt_erro1, row_txt_erro2, row_btn_erro])
            
            page.add(colunaErro)
            
        #Tratando uma resposta correta
        elif button.text == lista_partes[guia_perguntas[0]][5]:
            def proximaPergunta():
                guia_perguntas[0]+=1
                guia_valores[0]+=1
                page.clean()
                criaPagina(page)
                
            def perguntaFinal():
                global lista_principal
                global lista_ganhos
                global lista_partes
                global ganhos
                global guia_perguntas
                global guia_valores
                lista_principal = []
                lista_ganhos = []
                lista_partes = []
                ganhos = []
                guia_perguntas = [0]
                guia_valores= [0]
                inicial(page)
                
            page.bgcolor = "#38d14f" 
            
            txt_ganhos = ft.Text(value="Você ganhou: " + ganhos[guia_valores[0]], color="white",size=40,font_family="arial")
            row_txt_ganhos = ft.Row(controls=[txt_ganhos], alignment="center")
               
            btnAcerto = criar_botao(texto="Continuar")
            if guia_perguntas[0] == 14:
                btnAcerto.on_click = lambda event: perguntaFinal()
            else:
                btnAcerto.on_click = lambda event: proximaPergunta()
            row_btn_acerto = ft.Row(controls=[btnAcerto], alignment="center")
            
            
            espaco_acima = ft.Text(value="", size=20)
            
            colunaAcerto = ft.Column(controls=[espaco_acima, row_txt_ganhos, row_btn_acerto])
            
            page.add(colunaAcerto)


def main(page: ft.Page):
    inicial(page)
      
ft.app(target=main)

