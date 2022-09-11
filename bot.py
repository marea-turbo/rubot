import telebot
from auto_message import AutoMessage
from datetime import datetime
from pytz import timezone

# Chave do bot criada no BotFather -Alterar depois para a principal
API_KEY = "5475254576:AAHixEJiFnDmHPgg5L4jaGn7gcpl3pU6bw8"
bot = telebot.TeleBot(API_KEY)
auto_message = AutoMessage()

# Alterar menssages depois que decidirmos o nome do bot
@bot.message_handler(commands=["rubot"])
def rubot(message):
    bot.send_message(message.chat.id, "cardapio de HOJE colocar string que vem do EXTRATOR")

@bot.message_handler(commands=["rubot_amanha"])
def rubot_amanha(message):
    bot.send_message(message.chat.id, "cardapio de AMANHA colocar string que vem do EXTRATOR")

@bot.message_handler(commands=["rubot_semana"])
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

@bot.message_handler(commands=["teste"])
def rubot_today(message):
    targets = auto_message.user_ids()
    for id in targets:
        bot.send_message(id, "testando")

# Envia o help para todas as mensagens NAO comandos so funfa no pv
def verify(message):
    return True

@bot.message_handler(func=verify)
def help(message):
    options = """
    Escolha uma opção para continuar (Selecione um item):
    /help Para opções
    /rubot Para cardapio de hoje
    /rubot_amanha Para cardapio de amanhã
    /rubot_semana Para cardapio da semana

    Vc pode dar um /subscribe para receber o cardapio de hoje todos os dias pela manhã.
    """

    info = """
    Bot criado por:
    Anthon @FanDeMorbius
    & 
    Nicolas @MipsQuadriciclo.

    Inspirado no @quibebot.
    """

    bot.send_message(message.chat.id, info)
    bot.reply_to(message, options)


#now = datetime.now(timezone('America/Sao_Paulo'))

#Recebe as mensagens
bot.polling()