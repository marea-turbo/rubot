import src.ru as ru
import telebot

API_KEY = config("TOKEN")
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["ruh"])
def ruh(message):
    bot.send_message(message.chat.id, ru.get_today(), parse_mode='Markdown')

@bot.message_handler(commands=["amanha"])
def ruhbot_amanha(message):
    bot.send_message(message.chat.id, ru.get_tomorrow(), parse_mode='Markdown')

@bot.message_handler(commands=["semana"])
def ruhbot_semana(message):
    bot.send_message(message.chat.id, ru.get_week(), parse_mode='Markdown')

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
    /ruhbot Para cardapio de hoje
    /amanha Para cardapio de amanhã
    /semana Para cardapio da semana
    /about Para saber sobre o bot
    """
    bot.send_message(message.chat.id, options)

bot.polling()
