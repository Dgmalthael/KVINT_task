# U.Deniz Geles Kvint task
import telebot
import keys
import responses as r
import random
print('Bot started...')

bot = telebot.TeleBot(keys.API_KEY)


# start command handler
@bot.message_handler(commands=['start'])
def greet(message):

    bot.reply_to(message, "Hello! Welcome to the Pizza Delivery bot")
    bot.send_message(message.chat.id, str(r.lump.state))


# help commend hendler
@bot.message_handler(commands=['help'])
def help(message):

    bot.reply_to(message, "Help is not available for now!")
    return


Selection = []


# changing the machine state
def message_handler(message):
    request = str(message.text.split()).lower()

    if r.size[0] in request or r.size[1] in request:  # size selection

        if r.size[0] in request and r.size[0] not in Selection:
            Selection.append('small')
            r.lump.pizza_size()
        if r.size[1] in request and r.size[1] not in Selection:
            Selection.append('large')
            r.lump.pizza_size()
        return True

    if r.payment[0] in request or r.payment[1] in request:  # payment selection

        if r.payment[0] in request and r.payment[0] not in Selection:
            Selection.append('cash')
            r.lump.payment_method()
        if r.payment[1] in request and r.payment[1] not in Selection:
            Selection.append('card')
            r.lump.payment_method()
        return True
    if r.y_n[0] in request or r.y_n[1] in request:  # confirmation

        if r.y_n[0] in request and r.y_n[0] not in Selection:
            Selection.append('yes')
            r.lump.thank()
            print("message chat ID: "+ str(message.chat.id) + "Payment Method:" + str(Selection[1]) + " payment")
        if r.y_n[1] in request and r.y_n[1] not in Selection:
            r.lump.turn_back()
            Selection.clear()
        return True
    else:
        bot.send_message(message.chat.id, random.choice(r.errror_messages))
        r.lump.turn_back()
        bot.send_message(message.chat.id, str(r.lump.state))
        return False


@bot.message_handler(func=message_handler)
def messenger(message):
    if r.lump.state != r.automatic_answers[2] and len(Selection) <= 1 or len(Selection) > 2:
        bot.send_message(message.chat.id, str(r.lump.state))
    if r.lump.state == r.automatic_answers[2] and len(Selection) == 2:
        # confirmation according to the selections
        answer = f'{str(r.lump.state)} {str(Selection[0])} pizza paid by {str(Selection[1])}'
        bot.send_message(message.chat.id, answer)
        print('hey')
    return


bot.polling()
