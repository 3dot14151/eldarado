# -*- coding: utf-8 -*-
name_bot= "Телеграмм Викторина"
avtor   = "{Автор:'Купинов Вадим',tel:'+79033671563',Skype:'Izofen74'}"
version = "Version 2.1"

## Начинаем 16 Января 2017 г.
## Доработка 31 Января 2017г.

import telebot      # telegram bot
from telebot import types
import optparse     # import optparse module
import time       
import sqlite3
import random
import subprocess
import shlex


##print (ord('<'))
##print (ord('>'))

##print (chr(60))
##print (chr(62))


def print_message (textmes):
    c00 = "\033[0;0m"   ## Off
    c10 = "\033[0;30m"  ## Darkblack
    c11 = "\033[0;31m"  ## Darkred
    c11 = "\033[0;31m"  ## Красный
    c12 = "\033[0;32m"  ## Зеленый
    c13 = "\033[0;33m"  ## Darkyellow
    c14 = "\033[0;34m"  ## Darkblue
    c15 = "\033[0;35m"  ## Darkmagenta
    c16 = "\033[0;36m"  ## Darkcyan
    c17 = "\033[0;37m"  ## Белый
    c20 = "\033[1;30m"  ## Черный
    c21 = "\033[1;31m"  ## Red
    c23 = "\033[1;33m"  ## Желтый'
    c24 = "\033[1;34m"  ## Синий
    c25 = "\033[1;35m"  ## Magenta
    c26 = "\033[1;36m"  ## Cyan
    P01 = '😊'
    #from grab import Grab
    #g  = Grab()
    #try:
        #chat_id = '399838806'  ### ЛИЧНОЕ СООБЩЕНИЕ
        #message = '<b>Eldarado: </b>'+str(textmes)
        #tokenH   = '475495426:AAFoJogOHi5LcOXNiUeQ2VwSZ9LS8TpdR8U' ### БОТ ИНФОРМАТОР
        #g.go('https://api.telegram.org/bot475495426:AAFoJogOHi5LcOXNiUeQ2VwSZ9LS8TpdR8U/sendMessage?text='+message+'&chat_id='+str(chat_id)+'&parse_mode=HTML')
    #except:
        #pass

if __name__ == "__main__":
#--------------------------------------------------------------------------------------------------
    c00 = "\033[0;0m"   ## Off
    c10 = "\033[0;30m"  ## Darkblack
    c11 = "\033[0;31m"  ## Darkred
    c11 = "\033[0;31m"  ## Красный
    c12 = "\033[0;32m"  ## Зеленый
    c13 = "\033[0;33m"  ## Darkyellow
    c14 = "\033[0;34m"  ## Darkblue
    c15 = "\033[0;35m"  ## Darkmagenta
    c16 = "\033[0;36m"  ## Darkcyan
    c17 = "\033[0;37m"  ## Белый
    c20 = "\033[1;30m"  ## Черный
    c21 = "\033[1;31m"  ## Red
    c23 = "\033[1;33m"  ## Желтый'
    c24 = "\033[1;34m"  ## Синий
    c25 = "\033[1;35m"  ## Magenta
    c26 = "\033[1;36m"  ## Cyan
    P01 = '😊'
#--------------------------------------------------------------------------------------------------
    ### ВСТАВЛЯЕМ ИМЯ БОТА ###  
    token = '501597719:AAGAj46xpfelWVUEimmYUeWLhTXhyBwTTB8'
    token = '494728117:AAFRNF8niiydFt1j8njpMol2_hCNvkHjgCo'
    bot    = telebot.TeleBot(token)
    parser=optparse.OptionParser(version=version, description='Some test program to show chect of Python')
    parser.add_option('-f','--file', type='string', dest='file', help='Input DB SQL file for additional data')
    parser.add_option('-s','--save', type='string', dest='save', help='save data')
    parser.add_option('-l','--load', type='string', dest='load', help='load data')
    options,arguments=parser.parse_args()
    print_message ('Запуск программы: @TreasureHuntersBot  @Game_knb_bot')
    print ('[!] Автор:'+c23+avtor+c00)
    print ('[!] Версия:'+c23+version+c00)

def save_status (username,first_name,last_name,user_id,date,status,znachen):
    import sqlite3
    connP = sqlite3.connect("eldarado.sqlite") 
    cursorP = connP.cursor()
    if username == None: username = ''
    if first_name == None: first_name = ''
    if last_name  == None: last_name  = ''
    a = [username,first_name,last_name,user_id,date,status,znachen]    
    cursorP.execute("INSERT INTO user (username,first_name,last_name,user_id,date,status,znachen)VALUES (?,?,?,?,?,?,?);",a)    
    connP.commit()

def get_status (from_id):
    import sqlite3
    connP = sqlite3.connect("eldarado.sqlite") 
    cursorP = connP.cursor()
    sql = "SELECT id,status,znachen FROM user WHERE user_id = "+str(from_id)+" ORDER BY id  "
    status  = 'no'
    znachen = 'no'
    cursorP.execute(sql)
    dataP = cursorP.fetchall() 
    for row in dataP:        
        id_m,status,znachen = row
    return status,znachen

def main_menu ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('🤔 Загадки')
    markup.row('🔎 Добыть $','💵 Печать $','🏦 Вложить $')
    markup.row('😈 Украсть $','👮 Защитить $','💰 Клад')
    markup.row('💡Поддержка')
    return markup 


def skazka_menu ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('🔴 Клондайк','🔵Эльдорадо')
    markup.row('📘 Правила','📋 Меню')
    return markup 




## ЗАПУСК ПРИ НАЧАЛЕ ВОПРОСА
if options.load == 'start':
    print_message ('Отправка сообщений пользователям')
    user_id = '399838806'
    markup = main_menu ()
    conn = sqlite3.connect("skazka.sqlite") 
    cursor = conn.cursor()
    sql = "UPDATE skazka SET label = 'old' WHERE label = 'test' "
    cursor.execute(sql)
    conn.commit()
    sql = "select id,name,answer01,answer02,answer03,label from skazka where label = 'new' limit 1"  ### ПОЛУЧИТЬ НОВУЮ ЗАГАДКУ ИЗ БАЗЫ ДАННЫХ
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id_sk,name_sk,answer01_sk,answer02_sk,answer03_sk,label_sk = row
        print ('[+] Новая загадка: ',name_sk)
        sql = "UPDATE skazka SET label = 'test' WHERE id = '"+str(id_sk)+"'"                        ### ОТМЕЧАЕМ СКАЗКУ КАК В РАБОТЕ
        cursor.execute(sql)
        conn.commit()
    conn = sqlite3.connect("eldarado.sqlite") 
    cursor = conn.cursor()
    conn.commit()
    try:
        sql = "select DISTINCT user_id from user where 1=1 "                                        ### РАССЫЛАЕМ ВСЕ ВОПРОС
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            id_user_u = row[0]
            print ('[u]',id_user_u,name_sk)
            user_id =  id_user_u
            try:
                bot.send_message(user_id,name_sk,reply_markup=markup) 
                time.sleep(1) 
            except:
                pass
            sql = "UPDATE user SET team = '' WHERE user_id = '"+str(user_id)+"'"     
            cursor.execute(sql)
            conn.commit()
    except:
        bot.send_message(user_id,'На данный момент новых загадок нет')
    exit (0)


### ПРИ КОНЕЦ ВИКТОРИНЕ ###
if options.load == 'end':
    print_message ('Запуск программы: '+str("Конец викторины"))
    conn = sqlite3.connect("skazka.sqlite") 
    cursor = conn.cursor()
    sql = "select id,name,answer01,answer02,answer03,label,koment from skazka where label = 'test' limit 1"
    cursor.execute(sql)
    data = cursor.fetchall()
    answer01_en = ''
    koment_en = ''
    name_en     = '' 
    for row in data:
        id_en,name_en,answer01_en,answer02_en,answer03_en,label_en,koment_en = row
    print ('[+] Ответ на вопрос: ',answer01_en,koment_en)
    if name_en == '': ## Вопросы кончились
        print ('[!] Вопросов нет')
        conn = sqlite3.connect("eldarado.sqlite") # Отправляем всем сообщение
        cursor = conn.cursor()
        conn.commit()
        sql = "select DISTINCT user_id from user where 1=1 "
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            id_user_u = row[0]
            print ('[u]',id_user_u)
            user_id =  id_user_u
            try:
                pass
            except:
                pass  
    else: ## Найден вопрос
        conn = sqlite3.connect("answer.sqlite") 
        cursor = conn.cursor()    
        sql = "select DISTINCT answer from skazka where nomerskazky = '"+str(name_en)+"' "
        cursor.execute(sql)
        data = cursor.fetchall()
        answerall = '' # Собираем ответы
        for row in data:
            if row[0] != 'xxx':
                answerall = answerall +', '+ row[0]

        answerall = answerall[1:]
        print ('[+] Ответы на вопрос:',answerall)    
        conn = sqlite3.connect("eldarado.sqlite") 
        cursor = conn.cursor()
        conn.commit()
        summ01 = 0
        summ02 = 0 
        connAn   = sqlite3.connect("answer.sqlite") 
        cursorAn = connAn.cursor()    
        win01 = []
        sql = "select DISTINCT user_id from user where team  = '01' "
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            user_id_ans = row[0]
            sql = "select id,answer,user_id from skazka where nomerskazky = '"+str(name_en)+"' "
            cursorAn.execute(sql)
            dataAn = cursorAn.fetchall()
            for rowAn in dataAn:
                id_ot,answer_ot,user_id_ot = rowAn
                if (answer_ot.lower() == answer01_en.lower()) and (user_id_ans == user_id_ot):
                    summ01 = summ01 +1
                    win01.append(str(user_id_ot)) 
        print ('[+] Правильных ответов у (1) КЛОНДАЙК команды',summ01)
        win02 = []
        sql = "select DISTINCT user_id from user where team  = '02' "
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            user_id_ans = row[0]
            sql = "select id,answer,user_id from skazka where nomerskazky = '"+str(name_en)+"' "   #koment
            cursorAn.execute(sql)
            dataAn = cursorAn.fetchall()
            for rowAn in dataAn:
                id_ot,answer_ot,user_id_ot = rowAn  ###,koment_en
                ###print ('[111]',answer_ot)
                ###print (user_id_ans,answer01_en)
                if (answer_ot.lower() == answer01_en.lower()) and (user_id_ans == user_id_ot):
                    summ02 = summ02 +1
                    win02.append(str(user_id_ot)) 
                    print ('Совпадение')
        print ('[+]Правильных ответов у (2) Эльдорадо команды',summ02)


        if summ01 >= summ02:
            viktory = 'Победила команда: <b>Эльдорадо</b>.'
            print ('[+] '+viktory+' Список победителей '+str(win02))
            conn_win = sqlite3.connect("win.sqlite") 
            cursor_win = conn_win.cursor()
            for win_user_id in win02:
                a = [win_user_id,'Эльдорадо']    
                cursor_win.execute("INSERT INTO site (user_id,team)VALUES (?,?);",a)    
                conn_win.commit()    


        if summ01 <= summ02:
            viktory = 'Победила команда: <b>Клондайк</b>.'
            conn_win = sqlite3.connect("win.sqlite") 
            cursor_win = conn_win.cursor()
            print (viktory+' Список победителей '+str(win01))
            for win_user_id in win01:
                a = [win_user_id,'Клондайк']    
                cursor_win.execute("INSERT INTO site (user_id,team)VALUES (?,?);",a)    
                conn_win.commit()

        if summ01 == summ02:
            viktory = 'В этот раз победили обе команды (ничья).'


        print ('[+]',viktory)
        sql = "select DISTINCT user_id from user where 1=1 "
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            id_user_u = row[0]
            print ('[u]',id_user_u)
            user_id =  id_user_u
            try:
                ###if 1==1: 
                ansallkom = answer01_en
                if answer01_en != '':
                    bot.send_message(user_id,viktory+'\nПравильный ответ на загадку: <b>'+ansallkom+'</b>.\n'+koment_en,parse_mode='HTML') 
                    time.sleep(1)     
                    bot.send_message(user_id,'Ответы, которые давали игроки: '+answerall+' 😊') 
                    time.sleep(1)  
                    ###print ('----------------',koment_en)                         
            except:
                pass
        conn = sqlite3.connect("skazka.sqlite") 
        cursor = conn.cursor()
        sql = "UPDATE skazka SET label = 'old' WHERE label = 'test' "
        cursor.execute(sql)
        conn.commit()
    exit (0)



    ### Ищем статус сотрудника ###
def get_team (user_id):
    conn = sqlite3.connect("eldarado.sqlite") 
    cursor = conn.cursor()    
    sql = "select user_id,team from user where user_id = '"+str(user_id)+"' "
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
         user_id_b,team_b = row            
         print ('------------',team_b)   
    return user_id_b,team_b


    ### СТАНДАРТНЫЙ БЛОК ДЛЯ ЗАГАДКИ ###
    ### Ищем название загадки ###
def get_task ():
    conn = sqlite3.connect("skazka.sqlite") 
    cursor = conn.cursor()
    sql = "select id,name,answer01,answer02,answer03,label from skazka where label = 'test' limit 1"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id_sk,name_sk,answer01_sk,answer02_sk,answer03_sk,label_sk = row

    return id_sk,name_sk,answer01_sk,answer02_sk,answer03_sk,label_sk



@bot.message_handler(commands=['start', 'help'])  ### ПРИШЕЛ НОВЫЙ КЛИЕНТ
def send_welcome(message):
    first_name = ''
    last_name  = ''
    username   = ''
    username   = message.from_user.username
    first_name = message.from_user.first_name
    last_name  = message.from_user.last_name
    user_id    = message.from_user.id
    date       = message.date
    message_id = message.message_id
    save_status (username,first_name,last_name,user_id,date,'start','')
    status,znachen   = get_status (user_id)
    print ('[-1-]',status)    
    print_message ('Новый пользователь:'+str(user_id))
    markup = main_menu ()
    bot.send_message(user_id,'ДОЛЖЕН БЫТЬ ТЕКСТ',reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        user_id = call.message.chat.id
        if call.data.find ("kran") != -1:
            bot.edit_message_text(chat_id=user_id, message_id=call.message.message_id, text='Молодец! Ты добыл 1 🌕. Мы сообщим, когда подойдет следующая.')
        if call.data.find ("bonus") != -1:
            kollmonet = 0 
            kollmonet = random.randint(0, 10)
            bot.edit_message_text(chat_id=user_id, message_id=call.message.message_id, text='🎉  Ура! Ты откопал ('+str(kollmonet)+')  🌕. Завтра можно попробовать еще поискать.')







@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    user_id    = message.from_user.id 
    username   = message.from_user.username
    first_name = message.from_user.first_name
    last_name  = message.from_user.last_name
    date       = message.date
    name_sk    = ''
    message    = message.text.lower()
    print ('[+] Сообщение от пользователя: ',message)
    print_message ('Сообщение от:'+str(user_id)+'|'+message)
    if username == None: username = ''
    status,znachen   = get_status (user_id)
    ### ----------------------------------------- ###
    bot.send_message(user_id,'Статус - '+status)
    labelmess = 'no'  ## Метка что выводиться команда
    id_sk,name_sk,answer01_sk,answer02_sk,answer03_sk,label_sk = get_task ()
    print ('[Текущая загадка на данный момент:]',name_sk) 

    user_id_b,team_b = get_team (user_id)
    print ('[+] Команда игрока ',user_id,team_b)



    if status == 'win10':
        bot.send_message(user_id,' Ставка принята. Розыгрыш происходит каждый раз, когда набирается 100 ставок, следи за результатом на нашем канале @t_hunters .') 
        save_status (username,first_name,last_name,user_id,date,'','')
        labelmess = 'yes'

    if status == 'win13':
        bot.send_message(user_id,' Ставка принята. Следи за результатом на нашем канале @t_hunters .') 
        save_status (username,first_name,last_name,user_id,date,'','')
        labelmess = 'yes'


    if status == 'help':
        bot.send_message(user_id,' Спасибо, мы обязательно свяжемся с тобой.') 
        save_status (username,first_name,last_name,user_id,date,'','')
        labelmess = 'yes'


    ### БЛОК ДЛЯ САМОЙ ИГРЫ ###

    if message == '🔴 клондайк':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('📘 Правила','📋 Меню')
        ##markup.row('📋 Меню')
        bot.send_message(user_id,'Ждем от Вас ответ (у Вас 24 часа и всего 3 попытки)',reply_markup=markup) 
        conn = sqlite3.connect("eldarado.sqlite") 
        cursor = conn.cursor()
        sql = "UPDATE user SET team = '01' WHERE user_id = '"+str(user_id)+"'"
        cursor.execute(sql)
        conn.commit()
        labelmess = 'yes'

    if message == '🔵эльдорадо':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('📘 Правила','📋 Меню')
        ##markup.row('📋 Меню')
        bot.send_message(user_id,'Ждем от Вас ответ (у Вас 24 часа и всего 3 попытки)',reply_markup=markup) 
        conn = sqlite3.connect("eldarado.sqlite") 
        cursor = conn.cursor()
        sql = "UPDATE user SET team = '02' WHERE user_id = '"+str(user_id)+"'"
        cursor.execute(sql)
        conn.commit()
        labelmess = 'yes'

    if message == '📋 меню':        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('🤔 Загадки')
        markup.row('🔎 Добыть $','💵 Печать $','🏦 Вложить $')
        markup.row('😈 Украсть $','👮 Защитить $','💰 Клад')
        markup.row('💡Поддержка')
        bot.send_message(user_id,'Меню',reply_markup=markup)
        labelmess = 'yes'


    if message == 'назад':        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('🤔 Загадки')
        markup.row('🔎 Добыть $','💵 Печать $','🏦 Вложить $')
        markup.row('😈 Украсть $','👮 Защитить $','💰 Клад')
        markup.row('💡Поддержка')
        bot.send_message(user_id,'Меню',reply_markup=markup)
        labelmess = 'yes'


    if message == '⬆ назад':        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('🤔 Загадки')
        markup.row('🔎 Добыть $','💵 Печать $','🏦 Вложить $')
        markup.row('😈 Украсть $','👮 Защитить $','💰 Клад')
        markup.row('💡Поддержка')
        bot.send_message(user_id,'Меню',reply_markup=markup)
        labelmess = 'yes'


    if message == '🤔 загадки':        
        ### НОВАЯ ЗАГАДКА ДЛЯ ВИКТОРИНИ




        if 1==1:
            if 1==1:
                conn = sqlite3.connect("answer.sqlite") 
                cursor = conn.cursor()    
                sql = "select id,user_id,answer from skazka where user_id = '"+str(user_id)+"'and nomerskazky = '"+str(name_sk)+"' "
                cursor.execute(sql)
                data = cursor.fetchall()
                nomeranswer = 0  ### КОЛЛИЧЕСТВО ОТВЕТОВ
                labelrepit  = 'no'
                for row in data:
                    id_a,user_id_a,answer_a = row
                    nomeranswer = nomeranswer +1 
                    print ('[+] Ответы на загадку: ',user_id_a,answer_a)



        conn = sqlite3.connect("skazka.sqlite")     
        cursor = conn.cursor()
        sql = "select id,name,answer01,answer02,answer03,label,koment from skazka where label = 'test' limit 1"
        cursor.execute(sql)
        data = cursor.fetchall()
        answer01_en = ''
        name_en     = '' 
        for row in data:
            id_en,name_en,answer01_en,answer02_en,answer03_en,label_en,koment_en = row


        markup = skazka_menu ()


        if nomeranswer > 2:

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('📘 правила','📋 Меню')
            ###markup.row()
            ###bot.send_message(user_id,'Ждем от Вас ответ (у Вас 24 часа и всего 3 попытки)') 


            bot.send_message(user_id,'Играет загадка:'+name_en,reply_markup=markup) 



        else:
            bot.send_message(user_id,'Играет загадка:'+name_en,reply_markup=markup)
            print ('[+] Новая загадка для викторины:',)
        save_status (username,first_name,last_name,user_id,date,'mystery','')
        labelmess = 'yes'






    if message == '🔎 добыть $':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)        
        markup.row('🎊  Халява','🎲 Игры','👱 Друзья')
        markup.row('🔠 Задания','⌛ Конкурсы','📋 Меню')
        bot.send_message(user_id,'Добыть',reply_markup=markup)
        labelmess = 'yes'


    if message == '🎊  халява':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)        
        markup.row('💧  Кран','📦 Бонус','🔥Промокод')
        markup.row('⬆ Назад','📋 Меню')
        bot.send_message(user_id,'Халява',reply_markup=markup)
        labelmess = 'yes'


    if message == '💧  кран':
        message_out = 'Высоко в горах ⛰ кладоискатели нашли почти иссякший, но очень ценный источник 💧, из которого время от времени капают… золотые монеты.'
        print_message ('Ответ клиенту:'+str(user_id)+'|'+message_out)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton(text='Получить бесплатно 🌕', callback_data='kran')) 
        bot.send_message(user_id, text = message_out,parse_mode='HTML',reply_markup=keyboard)
        time.sleep(1)     
        labelmess = 'yes'


    if message == '📦 бонус':
        message_out = 'Весь день твой четвероногий друг 🐕 рыскал в поисках мест захоронений золотишка 💰 и, наконец, учуяв одно, привел тебя к нему.'
        print_message ('Ответ клиенту:'+str(user_id)+'|'+message_out)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton(text='Откопать монеты', callback_data='bonus')) 
        bot.send_message(user_id, text = message_out,parse_mode='HTML',reply_markup=keyboard)
        time.sleep(1)    
        labelmess = 'yes'
 

    if message == '🔥промокод':
        message_out = 'Каждый день по лесной дороге проезжает королевский экипаж, и по приказу Его щедрого Величества в каком-нибудь месте выкладывают мешочек с монетами для бедных крестьян. Не упусти момент и успей забрать (сделать в виде гиперссылки) эти 50 монет, а то их заберет кто-то другой!\nНикто не знает, когда проедет заветная карета, поэтому следи за сообщениями на нашем канале. @t_hunters'
        print_message ('Ответ клиенту:'+str(user_id)+'|'+message_out)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton(text='Откопать монеты', callback_data='zakaz')) 
        bot.send_message(user_id, text = message_out,parse_mode='HTML')
        time.sleep(1)     
        labelmess = 'yes'


    if message == '🎲 игры':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)        
        markup.row('Попади в 10-ку','Счастливое число 13')
        markup.row('⬆ Назад','📋 Меню')
        bot.send_message(user_id,'Игры',reply_markup=markup)
        labelmess = 'yes'


    if message == 'попади в 10-ку':
        message_out = 'Введи число от 1 до 10.\nЕсли ты угадаешь самое непопулярное среди игроков число, выиграешь целых 10 монет. Стоимость игры – 1 🌕.'
        print_message ('Ответ клиенту:'+str(user_id)+'|'+message_out)
        bot.send_message(user_id, text = message_out,parse_mode='HTML')
        save_status (username,first_name,last_name,user_id,date,'win10','')
        labelmess = 'yes'


    if message == 'счастливое число 13':
        message_out = 'Каждый час выпадает случайное число от 1 до 25. Выбери вариант, каким будет оно. Если угадаешь, выбрав <13 или >13, получишь вдвое больше, если же угадаешь, выбрав =13, получишь в 25 раз больше. Ставка – от 1 до 10 🌕.'
        print_message ('Ответ клиенту:'+str(user_id)+'|'+message_out)       
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)        
        markup.row('< 13','= 13','> 13')
        bot.send_message(user_id, text = message_out,reply_markup=markup)
        save_status (username,first_name,last_name,user_id,date,'win13','')
        labelmess = 'yes'


    if message == '👱 друзья':
        message_out = '«Один в поле не воин» - гласит старая поговорка кладоискателей. Среди твоих друзей обязательно найдутся любители приключений, готовые пуститься в поиски сокровищ, либо просто умные люди, которым бы понравилось отгадывать наши загадки.\nОтправь эту ссылку всем твоим друзьям и знакомым и получи за каждого по 10 🌕:\n(https://t.me/share/url?url=https%3A//t.me/TreasureHuntersBot?start='+str(user_id)+')\nЕе можно отправить в Telegram, WhatsApp, Viber, Instagram, по SMS или по E-mail.'
        print_message ('Ответ клиенту:'+str(user_id)+'|'+message_out)       
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)        
        markup.row('< 13','= 13','> 13')
        bot.send_message(user_id, text = message_out,parse_mode='HTML',reply_markup=markup)
        labelmess = 'yes'


    if message == '💵 печать $':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('🤔 Загадки')
        markup.row('🔎 Добыть $','💵 Печать $','🏦 Вложить $')
        markup.row('😈 Украсть $','👮 Защитить $','💰 Клад')
        markup.row('💡Поддержка')
        bot.send_message(user_id,'Печать',reply_markup=markup)
        labelmess = 'yes'


    if message == '🏦 вложить $':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('🤔 Загадки')
        markup.row('🔎 Добыть $','💵 Печать $','🏦 Вложить $')
        markup.row('😈 Украсть $','👮 Защитить $','💰 Клад')
        markup.row('💡Поддержка')
        bot.send_message(user_id,'Вложить',reply_markup=markup)
        labelmess = 'yes'


    if message == '😈 украсть $':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('🔖 Наводка','💣 Динамит','📋 Меню')
        bot.send_message(user_id,'Украсть',reply_markup=markup)
        labelmess = 'yes'


    if message == '👮 защитить $':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('🗄 Сейф','🔒Усиление','🛎 Сигнализация')
        markup.row('📋 Меню')
        bot.send_message(user_id,'Защитить',reply_markup=markup)
        labelmess = 'yes'


    if message == '💰 клад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('📜 Карта','🗝 Пароль','📋 Меню')
        bot.send_message(user_id,'Клад',reply_markup=markup)
        labelmess = 'yes'


    if message == '💡поддержка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('📊 Статистика','📖 Инструкция','🌟 Помощь')
        markup.row('🌟 Оценка','📋 Меню')
        bot.send_message(user_id,'Поддержка',reply_markup=markup)
        labelmess = 'yes'



    if message == '📊 статистика':
        bot.send_message(user_id,'🌕 – (число монет) монет\n👱 – (число друзей) друзей\n📊 – (рейтинг в игре, по числу монет) место в игре\n🗓 – (количество дней игры у игрока) дней в игре\n🗓 – (количество дней игры всего) дней идет игра\n🕵 – (обще число игроков) кладоискателей')
        labelmess = 'yes'



    if message == '📖 инструкция':
        bot.send_message(user_id,'Цель игры – накопить побольше монет, чтобы добыть карту клада с настоящими сокровищами!\nСпособов много:\n1. Отгадывай загадки, каждый раз\n2. Выигрывая вдвое больше.\n3. Получай халявные монеты.\n4. Играй в игры.\n5. Приглашай друзей.\n6. Побеждай в конкурсах.\n7. Выполняй задания.\n8. Вкладывай монеты в банк и получай проценты.\n9. Обкрадывай, наконец, других игроков!\n10. А еще ты можешь сам чеканить монеты с помощью чудо-майнера.\nИ не забывай о безопасности, ведь тебя тоже могут обокрасть.\nКогда у тебя накопится 1000 монет, ты можешь купить на черном рынке карту, а затем найти настоящие денежки! \nИ самое главное: курс нашей монеты будет расти вместе с числом игроков!\nУдачи тебе, отважный кладоискатель!\nP.S.')
        labelmess = 'yes'



    if message == '🌟 помощь':
        bot.send_message(user_id,'Введи ниже свой вопрос или предложение.')
        save_status (username,first_name,last_name,user_id,date,'help','')
        labelmess = 'yes'



    if message == '🌟 оценка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('⭐️','⭐️⭐️','⭐️⭐️⭐️')
        markup.row('⭐️⭐️⭐️⭐️⭐️','⬆ Назад')
        bot.send_message(user_id,'👍 Надеемся, тебе нравится наша игра. Пожалуйста, поддержи нас и помоги нам сделать ее популярнее!',reply_markup=markup)
        labelmess = 'yes'


    if message == '📘 правила':
        message_out = '<b>Правила игры</b>\n1. Каждый Пн, Ср и Пт в 8:00 (МСК) приходит новая загадка. Подсказки и варианты НЕ даются. Отгадка всегда в ед. числе, в одно слово; часто может иметь 2 и более смысла. Всегда обращай внимание на род (м, ж, ср) слова-отгадки; вообще каждая мелочь в загадке имеет значение.'
        print_message ('Ответ клиенту:'+str(user_id)+'|'+message_out)
        bot.send_message(user_id, text = message_out,parse_mode='HTML')
        time.sleep(1)     

        message_out = '2. Перед ответом игрок выбирает себе команду: Клондайк или Эльдорадо. Затем присылает ответ в русской транскрипции, без ошибок. Можно дать 1, 2 или 3 ответа, времени дается 24 часа. Каждый ответ стоит игроку 1 монету.'
        print_message ('Ответ клиенту:'+str(user_id)+'|'+message_out)
        bot.send_message(user_id, text = message_out,parse_mode='HTML')
        time.sleep(1)     

        message_out = '3. На следующий день приходит правильный ответ и информация о том, какая из двух команд в этот раз победила. Команда-победитель определяется по количеству угадавших. Побеждает меньшинство. Напр., угадали загадку 100 чел., из них 49 выбирало Клондайк, а 51 – Эльдорадо. Значит, победила команда Клондайк.'
        print_message ('Ответ клиенту:'+str(user_id)+'|'+message_out)
        bot.send_message(user_id, text = message_out,parse_mode='HTML')
        time.sleep(1)     


        message_out = '4. Все участники команды-победителя получают по 2 монеты и проходят дальше, а те, кто ответил правильно, но оказался в проигравшей команде, получают 1 монету и для них отсчет загадок начнется сначала, так же как и для всех, кто вообще не угадал загадку.'
        print_message ('Ответ клиенту:'+str(user_id)+'|'+message_out)
        bot.send_message(user_id, text = message_out,parse_mode='HTML')
        time.sleep(1)     

        message_out = '5. Каждый раз, когда игрок отгадал загадку, и при этом его команда победила, он получает вдвое больше монет, чем в предыдущий раз. После первой загадки – 2 монеты, после второй – 4, … после 10-й – 1024 и т.д.\nПравила могут меняться, поэтому советуем иногда заглядывать сюда.\nПри возникновении вопросов обращайся к администратору @gluxman.'
        print_message ('Ответ клиенту:'+str(user_id)+'|'+message_out)
        bot.send_message(user_id, text = message_out,parse_mode='HTML')
        labelmess = 'yes'



    if labelmess == 'no':
        if 1==1:
            if team_b == '' or team_b == None:
                markup = skazka_menu ()
                team_b = get_team (user_id)
                bot.send_message(user_id,'Сначала надо выбрать команду',reply_markup=markup)
            else: ### ПЕРЕБЕРАЕТ ОТВЕТЫ НА ЗАГАДКУ
               





                conn = sqlite3.connect("answer.sqlite") 
                cursor = conn.cursor()    
                sql = "select id,user_id,answer from skazka where user_id = '"+str(user_id)+"'and nomerskazky = '"+str(name_sk)+"' "
                cursor.execute(sql)
                data = cursor.fetchall()
                nomeranswer = 0  ### КОЛЛИЧЕСТВО ОТВЕТОВ
                labelrepit  = 'no'
                for row in data:
                    id_a,user_id_a,answer_a = row
                    nomeranswer = nomeranswer +1 
                    print ('[+] Ответы на загадку: ',user_id_a,answer_a)







                if nomeranswer == 0:
                    bot.send_message(user_id,'1-й ответ принят (у Вас в запасе еще 2 попытки).')
                    keyboard = types.InlineKeyboardMarkup()
                    url_button = types.InlineKeyboardButton(text="Отправить сообщение другу", url="https://t.me/share/url?url=https%3A//t.me/oren56_bot")
                    keyboard.add(url_button)
                    bot.send_message(user_id, "Вы можете позвать друзей в группу.\nЭто увеличит шансы добраться до клада.", reply_markup=keyboard)
                if nomeranswer == 1:
                    bot.send_message(user_id,'2-й ответ принят (у Вас в запасе еще 1 попытка).')
                if nomeranswer == 2:
                    bot.send_message(user_id,'3-й ответ принят (попыток больше не осталось). Правильный ответ узнаете по окончании отведенных 24 часов.')
                if nomeranswer > 2:
                    bot.send_message(user_id,'К сожалению, дальнейшие ответы не засчитываются. Дождитесь правильного ответа.') 



                   
                ### Записываем ответ в базе    
                conn = sqlite3.connect("answer.sqlite") 
                cursor = conn.cursor()                   
                message = message.lower()
                a = [user_id,message,name_sk]    
                cursor.execute("INSERT INTO skazka (user_id,answer,nomerskazky)VALUES (?,?,?);",a)    
                conn.commit()


bot.polling()







