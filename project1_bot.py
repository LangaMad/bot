
from h11 import Data

from cgitb import text
from email import message
from tkinter import Button

from numpy import number
from ShopSQL.man_clothSQL import Men_clothSQL
from ShopSQL.women_clothSQL import Women_clothSQL
from ShopSQL.shoesSQL import ShoesSQL
from ShopSQL.women_shoesSQL import Women_shoesSQL
from ShopSQL.Feedback import Feedback
from ShopSQL.adress_cash import Adress_cash
from ShopSQL.adress_cashless import Adress_cashless



from configbot1 import TOKEN 
import telebot
from telebot import types
from telebot import TeleBot

import mysql.connector
bot = telebot.TeleBot(token=TOKEN)
from telegram_bot_pagination import InlineKeyboardPaginator





db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="271711hasan",
    db="telegrambot_1",
    autocommit = True
)

cursor = db.cursor()

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup 



@bot.message_handler(commands=["start"])
def send_welcome_message(message):
    text = """
    Здравствуйте , вас приветсвует магазин одежды "Nike",
Чем могу помочь?
    """
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    category = types.InlineKeyboardButton("Выбрать категорю одежды", callback_data="category")
    # brand = types.InlineKeyboardButton("Выбрать бренд", callback_data="brand")
    feedback_button = types.InlineKeyboardButton("Написать отзыв", callback_data="feedback")
    contacts = types.InlineKeyboardButton("Наши контакы", callback_data="contacts")
    # paginations = types.InlineKeyboardButton("Страницы", callback_data="paginations")
    markup.add(category, feedback_button,contacts)
    bot.send_message(message.chat.id, text, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == "feedback")
def answer_feedback_callback(call):
    message=call.message
    bot.edit_message_text(chat_id=message.chat.id, 
                        text="Напишите пожалуйста ваш отзыв", 
                        message_id=message.id, 
                        reply_markup=None
                        )
    bot.register_next_step_handler(message=message, callback=get_feedback)

def get_feedback(message):
    from datetime import datetime
    add_feed = Feedback(cursor)
    text = message.text
    user = message.from_user.username
    message_time = message.date
    message_time=datetime.fromtimestamp(message_time).strftime("%d-%m-%Y %H:%M:%S")
    add_feed.add_feedback(create_time=message_time,user=user,text=text)
    feed_id = add_feed.get_id()

    
            
    bot.send_message(chat_id=message.chat.id, text=f"ID вашего отзыва {feed_id} ,Спасибо за ваш отзыв!")


@bot.callback_query_handler(func= lambda call: call.data=='category')
def sand_all_category(call):
    message = call.message
    
    
    
    markup = types.InlineKeyboardMarkup()
    mens_cloth = types.InlineKeyboardButton("Мужская Одежда", callback_data="man_cloth")
    men_kross = types.InlineKeyboardButton("Мужские Кроссовки", callback_data="men_shoes")
    womens_cloth = types.InlineKeyboardButton("Женская Одежда", callback_data="women_cloth")
    women_kross = types.InlineKeyboardButton("Женские Кроссовки", callback_data="women_shoes")
    go_back = types.InlineKeyboardButton ("Назад", callback_data="back1")

    markup.row_width = 1
    markup.add(men_kross,women_kross,mens_cloth,womens_cloth,go_back)
    bot.edit_message_text(chat_id=call.message.chat.id, text="Категории",
    message_id=call.message.message_id, reply_markup=markup)
    
@bot.callback_query_handler(func= lambda call: call.data=='man_cloth')
def sand_all_men_cloth(call):
    message = call.message

    men_cloth_maneger = Men_clothSQL(cursor)
    men_cloth = men_cloth_maneger.get_men_cloth()
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    for (id,name,price) in men_cloth:
        button = types.InlineKeyboardButton(name, callback_data=f"man_cloth_{id}")
        button2 = types.InlineKeyboardButton(price, callback_data=f"man_cloth_{id}a")

        markup.add(button,button2)
    bot.edit_message_text(
    chat_id=message.chat.id, 
    text="Выберите одежду",
    message_id=message.id,
    reply_markup=markup)



@bot.callback_query_handler(func= lambda call: call.data=='men_shoes')
def sand_all_shoes(call):
    message = call.message

    men_cloth_maneger = ShoesSQL(cursor)
    men_cloth = men_cloth_maneger.get_shoes()
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    for (id,name,price) in men_cloth:
        button = types.InlineKeyboardButton(name, callback_data=f"man_shoes_{id}")
        button2 = types.InlineKeyboardButton(price, callback_data=f"man_shoes_{id}a")
        markup.add(button,button2)

        

    bot.edit_message_text(
    chat_id=message.chat.id, 
    text="Выберите обувь",
    message_id=message.id,
    reply_markup=markup)

@bot.callback_query_handler(func= lambda call: call.data == f"man_shoes_1")
def call_buy(call):
    message = call.message
    
    
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    button = types.InlineKeyboardButton('Купить', callback_data=f"buy")
    booking = types.InlineKeyboardButton("Бронировать", callback_data="book")
    markup.add(button,booking)



    bot.edit_message_text(
    chat_id=message.chat.id,
    text="Выберите способ полчения товара",
    message_id=message.id,
    reply_markup=markup)


@bot.callback_query_handler(func= lambda call: call.data == f"man_cloth_1")
def call_buy(call):
    message = call.message
    
    
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    button = types.InlineKeyboardButton('Купить', callback_data=f"buy")
    booking = types.InlineKeyboardButton("Бронировать", callback_data="book")
    markup.add(button,booking)



    bot.edit_message_text(
    chat_id=message.chat.id,
    text="Выберите способ полчения товара",
    message_id=message.id,
    reply_markup=markup)


@bot.callback_query_handler(func= lambda call: call.data == f"man_cloth_2")
def call_buy(call):
    message = call.message
    
    
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    button = types.InlineKeyboardButton('Купить', callback_data=f"buy")
    booking = types.InlineKeyboardButton("Бронировать", callback_data="book")
    markup.add(button,booking)



    bot.edit_message_text(
    chat_id=message.chat.id,
    text="Выберите способ полчения товара",
    message_id=message.id,
    reply_markup=markup)


@bot.callback_query_handler(func= lambda call: call.data == f"man_cloth_3")
def call_buy(call):
    message = call.message
    
    
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    button = types.InlineKeyboardButton('Купить', callback_data=f"buy")
    booking = types.InlineKeyboardButton("Бронировать", callback_data="book")
    markup.add(button,booking)



    bot.edit_message_text(
    chat_id=message.chat.id,
    text="Выберите способ полчения товара",
    message_id=message.id,
    reply_markup=markup)



@bot.callback_query_handler(func= lambda call: call.data == f"man_shoes_2")
def call_buy(call):
    message = call.message
    
    
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    button = types.InlineKeyboardButton('Купить', callback_data=f"buy")
    booking = types.InlineKeyboardButton("Бронировать", callback_data="book")
    markup.add(button,booking)



    bot.edit_message_text(
    chat_id=message.chat.id,
    text="Выберите способ полчения товара",
    message_id=message.id,
    reply_markup=markup)

@bot.callback_query_handler(func= lambda call: call.data == f"man_shoes_3")
def call_buy(call):
    message = call.message
    
    
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    button = types.InlineKeyboardButton('Купить', callback_data=f"buy")
    booking = types.InlineKeyboardButton("Бронировать", callback_data="book")
    markup.add(button,booking)



    bot.edit_message_text(
    chat_id=message.chat.id,
    text="Выберите способ полчения товара",
    message_id=message.id,
    reply_markup=markup)

@bot.callback_query_handler(func= lambda call: call.data == f"man_shoes_4")
def call_buy(call):
    message = call.message
    
    
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    button = types.InlineKeyboardButton('Купить', callback_data=f"buy")
    booking = types.InlineKeyboardButton("Бронировать", callback_data="book")
    markup.add(button,booking)



    bot.edit_message_text(
    chat_id=message.chat.id,
    text="Выберите способ полчения товара",
    message_id=message.id,
    reply_markup=markup)

@bot.callback_query_handler(func= lambda call: call.data == f"man_shoes_5")
def call_buy(call):
    message = call.message
    
    
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    button = types.InlineKeyboardButton('Купить', callback_data=f"buy")
    booking = types.InlineKeyboardButton("Бронировать", callback_data="book")
    markup.add(button,booking)



    bot.edit_message_text(
    chat_id=message.chat.id,
    text="Выберите способ полчения товара",
    message_id=message.id,
    reply_markup=markup)

@bot.callback_query_handler(func= lambda call: call.data == f"women_cloth_1")
def call_buy(call):
    message = call.message
    
    
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    button = types.InlineKeyboardButton('Купить', callback_data=f"buy")
    booking = types.InlineKeyboardButton("Бронировать", callback_data="book")
    markup.add(button,booking)



    bot.edit_message_text(
    chat_id=message.chat.id,
    text="Выберите способ полчения товара",
    message_id=message.id,
    reply_markup=markup)

@bot.callback_query_handler(func= lambda call: call.data == f"women_cloth_2")
def call_buy(call):
    message = call.message
    
    
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    button = types.InlineKeyboardButton('Купить', callback_data=f"buy")
    booking = types.InlineKeyboardButton("Бронировать", callback_data="book")
    markup.add(button,booking)



    bot.edit_message_text(
    chat_id=message.chat.id,
    text="Выберите способ полчения товара",
    message_id=message.id,
    reply_markup=markup)



@bot.callback_query_handler(func= lambda call: call.data == f"women_cloth_3")
def call_buy(call):
    message = call.message
    
    
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    button = types.InlineKeyboardButton('Купить', callback_data=f"buy")
    booking = types.InlineKeyboardButton("Бронировать", callback_data="book")
    markup.add(button,booking)



    bot.edit_message_text(
    chat_id=message.chat.id,
    text="Выберите способ полчения товара",
    message_id=message.id,
    reply_markup=markup)

@bot.callback_query_handler(func= lambda call: call.data=='buy')
def get_buy(call):
    message = call.message
    markup = types.InlineKeyboardMarkup()
    markup.row_width =2

    button = types.InlineKeyboardButton('Доставка(наличная)',callback_data=f"cash")
    button2 = types.InlineKeyboardButton("Доставка(безналичная)", callback_data=f"cashless")
    button3 = types.InlineKeyboardButton("Назад",callback_data="back_buy")
    markup.add(button,button2,button3)

    bot.edit_message_text(
    chat_id=message.chat.id,
    text="Выберите способ оплаты",
    message_id=message.id,
    reply_markup=markup)


@bot.callback_query_handler(func= lambda call: call.data=='cash')
def get_cash_buy(call):
    message = call.message
    markup = types.InlineKeyboardMarkup()
    markup.row_width =2

    button3 = types.InlineKeyboardButton("Назад",callback_data="back_cash")
    markup.add(button3)
    bot.edit_message_text(
    chat_id=message.chat.id,
    text="Напишите свой адресс , после свой номер(все поля обязаельны), курьер приедет в течении 2 часов , оплата на руки курьеру, доставка по городу от 150 сом.",
    message_id=message.id,
    reply_markup=markup)
    bot.register_next_step_handler(message=message, callback=get_cash)

def get_cash(message):
    from datetime import datetime
    add_feed = Adress_cash(cursor)
    text = message.text
    number = message.text
    message_time = message.date
    message_time=datetime.fromtimestamp(message_time).strftime("%d-%m-%Y %H:%M:%S")
    add_feed.add_cash(create_time=message_time,text=text,number=number)
    feed_id = add_feed.get_id()


            
    bot.send_message(chat_id=message.chat.id, text=f"ID вашего заказ {feed_id} ,Спасибо за ваш заказа!")


@bot.callback_query_handler(func= lambda call: call.data=='cashless')
def get_cash_buy(call):
    message = call.message
    markup = types.InlineKeyboardMarkup()
    markup.row_width =2

    button3 = types.InlineKeyboardButton("Назад",callback_data="back_cash")
    markup.add(button3)
    bot.edit_message_text(
    chat_id=message.chat.id,
    text="""Наши реквизиты:
    Optina: 12345678987754,
    Elsom: +996553674743,
    PayPal: 3822952023,
    Отправьте чек с подтверждением оплыты
    Напишите свой адресс , после свой номер(все поля обязаельны), курьер приедет в течении 2 часов, доставка по городу от 150 сом.""",
    message_id=message.id,
    reply_markup=markup)
    bot.register_next_step_handler(message=message, callback=get_cash)

def get_cash(message):
    from datetime import datetime
    add_feed = Adress_cashless(cursor)
    text = message.text
    number = message.text
    message_time = message.date
    message_time=datetime.fromtimestamp(message_time).strftime("%d-%m-%Y %H:%M:%S")
    add_feed.add_cash(create_time=message_time,text=text,number=number)
    feed_id = add_feed.get_id()


            
    bot.send_message(chat_id=message.chat.id, text=f"ID вашего заказа {feed_id} ,Спасибо за ваш заказ!")



@bot.callback_query_handler(func= lambda call: call.data=='book')
def get_book(call):
    message = call.message
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    button = types.InlineKeyboardButton("Назад", callback_data='back_buy')
    button2 = types.InlineKeyboardButton("Бронь(безналичная)", callback_data=f"book_cashless")
    markup.add(button2,button)

    bot.edit_message_text(
        chat_id=message.chat.id,
        text="Для того чтобы бронировать, нужно заплатить минимум 10% от стоимости товара, бронь будет действовать 2 недели после истечения срока сумма сгораетб товар уходит на прилавок. ",
        message_id=message.id,
        reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "back_buy")
def answer_category_callback(call):
    message = call.message
    if call.data == "back_book":
        call_buy(call)

@bot.callback_query_handler(func= lambda call: call.data=='book_cashless')
def get_book(call):
    message = call.message
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    button = types.InlineKeyboardButton("Назад", callback_data='back_buy')
    markup.add(button)
    
    bot.edit_message_text(
    chat_id=message.chat.id,
    text="""Наши реквизиты:
    Optina: 12345678987754,
    Elsom: +996553674743,
    PayPal: 3822952023,
    Отправьте чек с подтверждением оплыты
    Наш адресс: Слутана,Аскарa 43/2 , время работы с 10:00 до 21:00 без выходных.""",
    message_id=message.id,
    reply_markup=markup)


@bot.callback_query_handler(func= lambda call: call.data=='women_cloth')
def sand_all_women_cloth(call):
    message = call.message

    men_cloth_maneger = Women_clothSQL(cursor)
    men_cloth = men_cloth_maneger.get_women_cloth()
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    for (id,name,price ) in men_cloth:
        button = types.InlineKeyboardButton(name,callback_data=f"women_cloth_{id}")
        button2 = types.InlineKeyboardButton(price, callback_data=f"women_cloth_{id}a")

        
        markup.add(button,button2)
    
    bot.edit_message_text(
    chat_id=message.chat.id,
    text="Выберите одежду",
    message_id=message.id,
    reply_markup=markup)

@bot.callback_query_handler(func= lambda call: call.data=='women_shoes')
def sand_all_women_shoes(call):
    message = call.message

    men_cloth_maneger = Women_shoesSQL(cursor)
    men_cloth = men_cloth_maneger.get_women_shoes()
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    for (id,name,price) in men_cloth:
        button = types.InlineKeyboardButton(name, callback_data=f"women_shoes_{id}")
        button2 = types.InlineKeyboardButton(price, callback_data=f"women_shoes_{id}a")
        
        markup.add(button,button2)
    bot.edit_message_text(
    chat_id=message.chat.id, 
    text="Выберите обувь",
    message_id=message.id,
    reply_markup=markup)


# @bot.callback_query_handler(func= lambda call: call.data=='category')
# def sand_all_category(call):
#     message = call.message
    
    
#     genre_manger = CategorySQL(cursor)
#     category = genre_manger.get_all_category()
#     markup = types.InlineKeyboardMarkup()
#     go_back = InlineKeyboardButton ("Назад", callback_data="back1")
#     markup.row_width = 2 
#     for (id,name) in category:
#         button = types.InlineKeyboardButton(name, callback_data=f"category_{id}")
#         markup.add(button,go_back)
#     bot.edit_message_text(
#     chat_id=message.chat.id, 
#     text="Выберите категорию",
#     message_id=message.id,
#     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "back1")
def answer_category_callback(call):
    message = call.message
    if call.data == "back1":
        send_welcome_message(message)




@bot.callback_query_handler(func=lambda call: call.data == "contacts")
def answer_contacts_callback(call):
    message = call.message
    instagram = InlineKeyboardButton("Instagram", url="https://instagram.com/nike?utm_medium=copy_link" , callback_data="insta")
    number = InlineKeyboardButton("Number",  callback_data="number")
    facebook = InlineKeyboardButton ("Facebook", url="https://www.facebook.com/nike/", callback_data="fecebook")
    go_back = InlineKeyboardButton ("Назад", callback_data="back")
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(instagram,number, facebook, go_back)
    bot.edit_message_text(chat_id=call.message.chat.id, text="Наши контакты ",
    message_id=call.message.message_id, reply_markup=markup)

    
    
@bot.callback_query_handler(func=lambda call: call.data == "back")
def answer_conatcts_callback(call):
    message = call.message
    if call.data == "back":
        send_welcome_message(message)





bot.infinity_polling()

