import telebot
CHAVE_API = '*******************************'
bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=['sobremim'])
def sobremim(mensagem):
    chat_id = mensagem.chat.id
    bot.send_message(chat_id, 'xxx')




def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, '''Olá seja bem vindo ao Guia LIRA - Esse CHATBOT além de ser uma ferramenta de estudo para trabalhar com o Telegram é também um Guia de aprendizado para aprender programação\n
Destancando links de projetos pessoais meus, recomendações de sites para aprender , desafios e cursos sobre programação \n
Todo o ChatBOT está sendo feito em Python por - Raphael Lira''')
    chat_id = mensagem.chat.id

    # Envie uma mensagem de resposta
    bot.send_message(chat_id, 'Aqui está a listinha das opções que você tem')
    bot.send_message(chat_id, '''/sobremim - Nessa função eu falo sobre mim e coloco meus''')


bot.polling()