# -*- coding: utf-8 -*-
import serial
import time
from telegram.ext import (Updater, CommandHandler)

def start(update, context):
    ''' START '''
    # Enviar un mensaje a un ID determinado.
    context.bot.send_message(update.message.chat_id, "Bienvenido")

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def main():
    TOKEN="5231442515:AAGAdYf_kHlcm07JRwXp98uKiUdCE0_k51M"
    updater=Updater(TOKEN, use_context=True)
    dp=updater.dispatcher

    # Eventos que activarán nuestro bot.
    dp.add_handler(CommandHandler('start',  start))

    # Comienza el bot
    updater.start_polling()
    # Lo deja a la escucha. Evita que se detenga.
    #updater.idle()

    while True:
            num = input("Enter a number: ")
            value = write_read(num)
            print(value)

if __name__ == '__main__':
    main()

