import telebot

CHAVE_API = '5945993384:AAHkGz9G0GrIk9BoHBK3UUay56UjrfYrwqA'
bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=['sobremim'])
def sobremim(mensagem):
    chat_id = mensagem.chat.id
    bot.send_message(chat_id, '''Me chamo Raphael Lira tenho 19 anos e trabalho com programação a 1.5 anos 

Minha principal linguagem é Python com foco para RPA e Dados, todo esse projeto está disponivel no meu GitHub.

Linkedin - https://www.linkedin.com/in/raphaellira/
Numero - 71 9 96457785 para trabalhos 
Discord - Zharboy#6228
GitHub -  https://github.com/Raphael-Lira''')


@bot.message_handler(commands=['area'])
def sobremim(mensagem):
    chat_id = mensagem.chat.id
    bot.send_message(chat_id, '''Se você selecionou essa opção você está provavelmente com duvida em qual ramo seguir e nessa abinha irei explicar tudo para você !

Existem diversas áreas de programação, mas podemos destacar 3 principais:

Desenvolvimento web: Nessa área, as linguagens mais utilizadas são o HTML, CSS, PHP, JavaScript, e suas frameworks, como React, Angular, VueJS e Django.

Desenvolvimento mobile: Para o desenvolvimento de aplicativos móveis, destacam-se as linguagens Java para Android, Swift para iOS e Kotlin, que pode ser utilizada para ambas as plataformas.

Data Science: Nessa área, Python é a linguagem mais utilizada para análise de dados, junto com suas bibliotecas, como Numpy, Pandas e Scikit-learn. Além disso, também são utilizadas linguagens como R e SQL ''')


@bot.message_handler(commands=['cursos'])
def cursos(mensagem):
    chat_id = mensagem.chat.id
    bot.send_message(chat_id, '''Ao escolher um curso de programação, pode ser difícil decidir qual é o melhor, dada a ampla gama de opções disponíveis. Há cursos gratuitos e pagos, mas encontrar os melhores requer pesquisa. Aqui, vou compartilhar a minha experiência com alguns cursos que considero de qualidade.

Em primeiro lugar, recomendo os cursos da Hashtag Treinamentos. Esta plataforma oferece uma ampla variedade de cursos, incluindo dois que se destacam na área de programação: Python Impressionador e SQL Impressionador. Ambos os cursos são extremamente completos, com uma ótima didática, sistema de suporte para dúvidas e uma plataforma super intuitiva.

Em segundo lugar, sugiro o curso da Dev Media, que tem um excelente conteúdo, plataforma bem estruturada e material didático vasto, focado especialmente em desenvolvimento web.

Em terceiro lugar, temos o curso da Danki Code, uma plataforma de programação com milhares de cursos na área, guias, suporte para dúvidas e vasto conteúdo sobre desenvolvimento web.

Ao considerar essas opções, lembre-se de que a escolha do curso certo depende de suas metas e objetivos de aprendizado específicos. Então, avalie suas necessidades e escolha o curso que melhor se adapte a elas.''')


@bot.message_handler(commands=['ferramentas'])
def ferramentas(mensagem):
    chat_id = mensagem.chat.id
    bot.send_message(chat_id, '''CHAT GPT:
O Chat GPT é uma ferramenta de bate-papo baseada em inteligência artificial, que utiliza a tecnologia de processamento de linguagem natural para gerar respostas para as perguntas dos usuários. Essa ferramenta pode ser usada para auxiliar na programação, permitindo que desenvolvedores obtenham sugestões, ideias e até mesmo linhas de código a partir do modelo treinado do GPT.

GITHUB:
O GitHub é uma plataforma de hospedagem de código-fonte e colaboração, que permite que desenvolvedores compartilhem, colaborem e controlem o código-fonte de seus projetos. Além disso, ele oferece recursos como controle de versão, gerenciamento de problemas e solicitações de pull, além de integração com outras ferramentas de desenvolvimento.

STACK OVERFLOW:
O Stack Overflow é uma plataforma de perguntas e respostas voltada para desenvolvedores, que permite que os usuários postem perguntas e obtenham respostas de outros desenvolvedores. A plataforma possui uma grande comunidade ativa e é conhecida por ter respostas de alta qualidade e confiáveis para uma ampla variedade de tópicos de programação.

FIGMA:
O Figma é uma ferramenta de design colaborativo baseada na nuvem, que permite que equipes de design criem, compartilhem e iterem designs em tempo real. Com o Figma, é possível criar protótipos de alta fidelidade, apresentações interativas e até mesmo códigos ''')


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
    bot.send_message(chat_id, '''/sobremim - Irei falar sobre mim e colocar meus projetos e perfis\n
/area - Se você está em duvida em qual área seguir  clique aqui para entender mais\n
/cursos - Cursos que eu recomendo baseado na minha experiencia de seguimento\n
/ferramentas - Todas as ferramentas que você precisa conhecer para melhorar sua performance''')


bot.polling()