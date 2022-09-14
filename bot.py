import telebot
import src.ru as ru
import src.wrappers.html as h
from pprint import pprint


API_KEY = "5475254576:AAHixEJiFnDmHPgg5L4jaGn7gcpl3pU6bw8"
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["rubot"])
def rubot(message):
    bot.send_message(message.chat.id, "HOJE")

@bot.message_handler(commands=["amanha"])
def rubot_amanha(message):
    bot.send_message(message.chat.id, "AMANHA")

@bot.message_handler(commands=["semana"])
def rubot_semana(message):
    bot.send_message(message.chat.id, "SEMANA")

@bot.message_handler(commands=["about"])
def info(message):
    info = """
    Bot criado por:
    Anthon @FanDeMorbius
    & 
    Nicolas @MipsQuadriciclo.

    Inspirado no @quibebot.

    Codigo: https://github.com/marea-turbo/rubot
    """
    bot.send_message(message.chat.id, info)


@bot.message_handler(commands=["start", "help"])
def help(message):
    options = """
    Eu sou o BOT que te mostra o cardapio do RU!!

    Escolha uma opção para continuar (Selecione um item):
    /help Para opções
    /rubot Para cardapio de hoje
    /amanha Para cardapio de amanhã
    /semana Para cardapio da semana
    /about Para saber sobre o bot
    """
    bot.send_message(message.chat.id, options)

bot.polling()
