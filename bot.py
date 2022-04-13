# -*- coding: utf-8 -*-
import serial
import time
from telegram.ext import (Updater, CommandHandler)

def start(update, context):
    ''' START '''
    # Enviar un mensaje a un ID determinado.
    context.bot.send_message(update.message.chat_id, "Bienvenido")

def passwd(update, context):
    try:
        passwd = int(context.args[0])
        if passwd == "1234":
            update.message.reply_text('Contraseña correcta, apagando alarma')
            arduino.write(b'3')
    except (IndexError, ValueError):
        update.message.reply_text('Introduzca un parámetro de contraseña válido')

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def cero():
    alarma = 1
    #virtual.write(b'3')
    print("cero")
 
def uno():
    alarma = 0
    print("uno")
 
def dos():
    alarma = 0
    print("dos")

def tres():
    alarma = 0
    print("tres")
 
def switch(argument):
    print(argument)
    
    switcher = {
        b'0': cero,
        b'1': uno,
        b'2': dos,
        b'3': tres,
    }
    
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid month")
    # Execute the function
    func()

def main():
    arduino = serial.Serial('/dev/pts/1', 9600)
    virtual = serial.Serial('/dev/pts/2', 9600)

    alarma = 0

    TOKEN="5231442515:AAGAdYf_kHlcm07JRwXp98uKiUdCE0_k51M"
    updater=Updater(TOKEN, use_context=True)
    dp=updater.dispatcher

    # Eventos que activarán nuestro bot.
    dp.add_handler(CommandHandler('start',  start))
    dp.add_handler(CommandHandler('passwd',  passwd))
    
    # Comienza el bot
    updater.start_polling()
    # Lo deja a la escucha. Evita que se detenga.
    #updater.idle()

    while True:
            time.sleep(0.1)
            rawString = arduino.read()
            switch(rawString)
            #if rawString==b'0':
                #alarma = true
                #print(rawString)
                #virtual.write(b'3')

if __name__ == '__main__':
    main()

