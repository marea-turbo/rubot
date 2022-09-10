import telebot

# Chave do bot criada no BotFather -Alterar depois para a principal
API_KEY = "5475254576:AAHixEJiFnDmHPgg5L4jaGn7gcpl3pU6bw8"
bot = telebot.TeleBot(API_KEY)

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

# Envia o help para todas as mensagens NAO comandos
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
    """

    info = """
    Bot criado por:
    Anthon @FanDeMorbius
    e 
    Nicolas @Mipsquadriciclo

    Inspirado no @quibebot
    """

    bot.send_message(message.chat.id, info)
    bot.reply_to(message, options)

#Recebe as mensagens
bot.polling()