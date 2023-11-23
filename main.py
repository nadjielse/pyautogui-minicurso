import pyautogui as bot
import time

"""
bot.PAUSE = 1

# print(bot.position()) # Mostra a posição do mouse

bot.moveTo(466, 1060, duration=0.5) # Move mouse para posição 466, 1060

bot.click() # Clica onde o mouse está

bot.hotkey("ctrl", "t") # Pressiona o atalho ctrl + t

bot.write("youtube.com") # Escreve youtube.com

bot.press("enter") # Pressiona a tecla enter

# print(bot.position()) # Mostra a posição do mouse
"""

bot.alert("Tarefa automatizada iniciada. Não mexa!")

# Ir para área de trabalho
bot.hotkey("win", "d")

# Mover mouse para o PyGestor
bot.moveTo(873, 542, duration=0.1)

# Clicar duplamente no PyGestor
bot.doubleClick()

# Espera 10 segundos para próximos comandos
time.sleep(10)

with open('produtos.txt', 'r') as arquivos:
    for linha in arquivos:
        codigo = linha.split(";")[0]
        produto = linha.split(";")[1]
        descricao = linha.split(";")[2]
        valor = linha.split(";")[3]
        quantidade = linha.split(";")[4]
        data = linha.split(";")[5]
        fabricante = linha.split(";")[6]
        unidade = linha.split(";")[7]

        # Mover mouse e clicar no campo código
        bot.moveTo(854, 421, duration=0.1)
        bot.click()
        bot.write(codigo)

        # Mover mouse e clicar no campo produto
        bot.moveTo(631, 420, duration=0.1)
        bot.click()
        bot.write(produto)

        # Mover mouse e clicar no campo descricao
        bot.moveTo(638, 502, duration=0.1)
        bot.click()
        bot.write(descricao)

        # Mover mouse e clicar no campo valor
        bot.moveTo(853, 481, duration=0.1)
        bot.click()
        bot.write(valor)

        # Mover mouse e clicar no campo quantidade
        bot.moveTo(850, 541, duration=0.1)
        bot.click()
        bot.write(quantidade)

        # Mover mouse e clicar no campo data
        bot.moveTo(1035, 420, duration=0.1)
        bot.click()
        bot.write(data)

        # Mover mouse e clicar no campo fabricante
        bot.moveTo(1049, 483, duration=0.1)
        bot.click()
        bot.write(fabricante)

        # Mover mouse e clicar no campo unidade
        bot.moveTo(1042, 539, duration=0.1)
        bot.click()
        bot.write(unidade)

        # Mover mouse e clicar no botão salvar
        bot.moveTo(1208, 486, duration=0.1)
        bot.click()

bot.alert("Tarefa automatizada finalizada. Pode mexer ;)")
