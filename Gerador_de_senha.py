import random
import string
import PySimpleGUI as sg


#caracteres = string.ascii_letters #retorna todas as letras maisculas e minusculas
#caracteres = string.punctuation #retorna caracteres especiais
#caracteres = string.digits #retorna os numeros decimais de 0 a 9

#caracteres = string.ascii_letters + string.punctuation + string.digits


#senha = " ".join(random.choices(caracteres, k=1600))
#print(f"essa é sua senha {senha}")


#layout

layout =[
    
    [sg.Text(" Gerador de Senha", font=("Arial black", 20, ))],

    [sg.Button("Gerar uma Senha Segura")],
    [sg.Input(key='senha')],

]    

# ===== JANELA =====
janela = sg.Window("EduLogic System", layout)



# ===== LOOP =====
while True:
    evento, valores = janela.read()

    if evento == sg.WINDOW_CLOSED:
        break

    if evento == "Gerar uma Senha Segura":
        caracteres = string.ascii_letters + string.punctuation + string.digits
        senha = "".join(random.choices(caracteres, k=16))
        janela["senha"].update(senha)


janela.close()
