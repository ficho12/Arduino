# -*- coding: utf-8 -*-
import serial
import time
from telegram.ext import (Updater, CommandHandler)

def start(update, context):
    ''' START '''
    # Enviar un mensaje a un ID determinado.
    global chat_id
    chat_id = update.message.chat_id
    context.bot.send_message(update.message.chat_id, "Bienvenido")

def passwd(update, context):
    if alarma==1:
        try:
            passwd = context.args[0]
            if passwd == "1234":
                update.message.reply_text('Contraseña correcta, apagando alarma')
                arduino.write(b'2')
            else:
                update.message.reply_text('Contraseña incorrecta.')
        except (IndexError, ValueError):
            update.message.reply_text('Introduzca un parámetro de contraseña válido')
    else:
        update.message.reply_text('La alarma no está activa')


def cero(dp):
    global alarma
    alarma = 1
    dp.bot.sendMessage(chat_id=chat_id, text='¡Alarma activa! Por favor escriba la contraseña con el comando /passwd contraseña')
    print("cero")
 
def uno(dp):
    global alarma
    alarma = 0
    dp.bot.sendMessage(chat_id=chat_id, text='Alarma desactivada mediante keypad')
    print("uno")

def retorno(dp):
    print('Retorno de carro')
 
def error(dp):
    print('Entrada serial no programada')

#Hacer comprobación de inicializacion del bot
 
def switch(argument,dp):
    print(argument)
    
    switcher = {
        b'0': cero,
        b'1': uno,
        b'\n': retorno
    }
    
    # Elegir la funcion del diccionario switcher
    func = switcher.get(argument, error)
    # Ejecutar la funcion
    func(dp)

def main():
    global arduino, virtual, alarma
    arduino = serial.Serial('/dev/pts/1', 9600)
    virtual = serial.Serial('/dev/pts/2', 9600)
    alarma = 0

    TOKEN="5231442515:AAGAdYf_kHlcm07JRwXp98uKiUdCE0_k51M"  #Token de nuestro bot
    updater=Updater(TOKEN, use_context=True)
    dp=updater.dispatcher

    # Eventos que activarán nuestro bot.
    dp.add_handler(CommandHandler('start',  start))
    dp.add_handler(CommandHandler('passwd',  passwd))
    
    # Comienza el bot
    updater.start_polling()

    while True:
            time.sleep(0.1)
            rawString = arduino.read()
            switch(rawString,dp)

if __name__ == '__main__':
    main()

