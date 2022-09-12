from email import message
import telebot
from src.auto_message import AutoMessage
from datetime import datetime, timedelta, timezone


# Chave do bot criada no BotFather -Alterar depois para a principal
API_KEY = "5475254576:AAHixEJiFnDmHPgg5L4jaGn7gcpl3pU6bw8"
bot = telebot.TeleBot(API_KEY)
auto_message = AutoMessage()

hour_to_message = datetime.time(8, 0, 0)

@bot.message_handler(commands=["rubot"])
def rubot(message):
    bot.send_message(message.chat.id, "cardapio de HOJE colocar string que vem do EXTRATOR")

@bot.message_handler(commands=["amanha"])
def rubot_amanha(message):
    bot.send_message(message.chat.id, "cardapio de AMANHA colocar string que vem do EXTRATOR")

@bot.message_handler(commands=["semana"])
def rubot_semana(message):
    bot.send_message(message.chat.id, "cardapio da SEMANA colocar string que vem do EXTRATOR")

@bot.message_handler(commands=["subscribe"])
def rubot_subscribe(message):
    auto_message.save_user(message.from_user)
    bot.send_message(message.from_user.id, "Todos os dias pela manhã vc receberá o cardapio do dia!")

@bot.message_handler(commands=["unsubscribe"])
def rubot_unsubscribe(message):
    auto_message.delete_user(message.from_user)
    bot.send_message(message.from_user.id, "Vc deixou de seguir, para receber todos os dias de /subscribe novamente")

#alterar isso pra uma rotina toda manhã enviar mensagem pra geral no json
# @bot.message_handler(func=send_on_day)
# def rubot_today(message):
#     targets = auto_message.user_ids()
#     for id in targets:
#         print(id)
#         bot.send_message(id, "testando")

# def send_on_day(message):
    
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

    Vc pode dar um /subscribe para receber o cardapio de hoje todos os dias pela manhã.
    """
    bot.send_message(message.chat.id, options)


#now = datetime.now(timezone('America/Sao_Paulo'))

#Recebe as mensagens
bot.polling()