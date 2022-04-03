#import telebot
import answers
import random
from event import Event

# Events_list
# TEMPORARY!
events = [] 

# Hanging dialog function
# Навешивает обработчики на бота
def handlerization(bot):
    @bot.message_handler(commands=['start'])
    def send_hello(message):
        bot.send_message(message.chat.id, answers.hello_string)

    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.send_message(message.chat.id, answers.help_string)
    
    # Show_events-command
    @bot.message_handler(commands=['show_events'])
    def show_event(message):
        if not events: 
            bot.send_message(message.chat.id, answers.show_nothing)
        else:
            bot.send_message(message.chat.id, answers.show_events)
            result = '\n'.join(event.get_event_string() for event in events)
            bot.send_message(message.chat.id, result)
    
    @bot.message_handler(commands=['add_event'])
    def add_event(message):
        cur_chat_id = message.chat.id
        bot.send_message(message.chat.id, answers.insert_string)
        msg = bot.send_message(message.chat.id, answers.ask_event)
        bot.register_next_step_handler(msg, get_event_name_step)
    def get_event_name_step(message):
        events.append(Event(message.text))
        
        msg = bot.send_message(message.chat.id, answers.ask_time)
        bot.register_next_step_handler(msg, get_event_time_step)
    def get_event_time_step(message):
        sintax_check = events[-1].set_time(message.text)
        if not sintax_check:
            msg = bot.send_message(message.chat.id, answers.entered_time_error)
            bot.register_next_step_handler(msg, get_event_time_step)
        else:
            bot.send_message(message.chat.id, answers.event_added)
    
    @bot.message_handler(commands=['del_event'])
    def del_event(message):
        bot.send_message(message.chat.id, answers.del_string)
        msg = bot.send_message(message.chat.id, answers.ask_del_number)
        bot.register_next_step_handler(msg, get_del_number)
    def get_del_number(message):
        events.pop(int(message.text) - 1)
        bot.send_message(message.chat.id, answers.event_deleted)
        
