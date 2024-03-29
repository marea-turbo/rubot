import src.ru as ru
import telebot
import os


API_KEY = os.environ.get("TOKEN")
if API_KEY is None:
    raise RuntimeError("token not found or missing")

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

    Repositório: https://github.com/marea-turbo/rubot
    """
    bot.send_message(message.chat.id, info)


@bot.message_handler(commands=["start", "help"])
def help(message):
    options = """
    Eu sou o BOT que te mostra o cardapio do RU!!

    Escolha uma opção para continuar (Selecione um item):
    /help Para opções
    /ruh Para cardapio de hoje
    /amanha Para cardapio de amanhã
    /semana Para cardapio da semana
    /about Para saber sobre o bot
    """
    bot.send_message(message.chat.id, options)


if __name__ == "__main__":
    bot.polling()
