# -*- coding: utf-8 -*-
import serial
import time
from telegram.ext import (Updater, CommandHandler)
import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update, context):
    ''' START '''
    # Enviar un mensaje a un ID determinado.
    global chat_id
    chat_id = update.message.chat_id
    context.bot.send_message(update.message.chat_id, "Bienvenido")

#No detecta bien la contraseña

def passwd(update, context):
    try:
        passwd = context.args[0]
        if passwd == "1234":
            update.message.reply_text('Contraseña correcta, apagando alarma')
            arduino.write(b'3')
        else:
            update.message.reply_text('Contraseña incorrecta.')
    except (IndexError, ValueError):
        update.message.reply_text('Introduzca un parámetro de contraseña válido')

def cero(dp):
    global alarma
    alarma = 1
    dp.bot.sendMessage(chat_id=chat_id, text='¡Alarma activa! Por favor escriba la contraseña con el comando /passwd contraseña')
    print("cero")
 
def uno(dp):
    global alarma
    alarma = 0
    print("uno")
 
def dos(dp):
    global alarma
    alarma = 0
    print("dos")

def tres(dp):
    global alarma
    alarma = 0
    print("tres")

def error(dp):
    print('error en diccionario')

#Hacer comprobación de inicializacion del bot
 
def switch(argument,dp):
    print(argument)
    
    switcher = {
        b'0': cero,
        b'1': uno,
        b'2': dos,
        b'3': tres
    }
    
    # Get the function from switcher dictionary
    func = switcher.get(argument, error)
    # Execute the function
    func(dp)

def main():
    global arduino, virtual, alarma
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
            switch(rawString,dp)
            #if rawString==b'0':
                #alarma = true
                #print(rawString)
                #virtual.write(b'3')

if __name__ == '__main__':
    main()

