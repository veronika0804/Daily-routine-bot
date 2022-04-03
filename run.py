import telebot
import dialog

# BEFORE RUNNING!
# CREATE FILE 'bot_token'
# and fill it as a token, given by BotFather
#(read.me for getting more information)

# Getting token from file
token_file = open('bot_token')
token_string = token_file.readline().strip()
token_file.close()

# Bot init
bot = telebot.TeleBot(token_string)
dialog.handlerization(bot)

def main():
    # Reaction start        
    bot.infinity_polling()

if __name__ == '__main__':
    main()
