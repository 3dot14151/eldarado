# -*- coding: utf-8 -*-
name_bot= "Телеграмм Викторина"
avtor   = "{Автор:'Купинов Вадим',tel:'+79033671563',Skype:'Izofen74'}"
version = "Version 1.1"
##print (name_bot)
##print (avtor)
##print (version)

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



def print_message (textmes):
    tokenH   = '475495426:AAFoJogOHi5LcOXNiUeQ2VwSZ9LS8TpdR8U' ### БОТ ИНФОРМАТОР
    botH = telebot.TeleBot(tokenH) 
    print ('[!]',textmes)
    chat_id = '399838806'  ### ЛИЧНОЕ СООБЩЕНИЕ
    botH.send_message(chat_id,'<b>Eldarado: </b>'+textmes+'',parse_mode='HTML')


#--------------------------------------------------------------------------------------------------
if 1==1:
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
    ###disable_web_page_preview
    ###disable_notification
#--------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    ### ВСТАВЛЯЕМ ИМЯ БОТА ###  
    token = '501597719:AAGAj46xpfelWVUEimmYUeWLhTXhyBwTTB8'
    token = '567327243:AAGn1Iz27ltBmEClBq8vKMPnT1qyidgu5XA'
    bot    = telebot.TeleBot(token)
    parser=optparse.OptionParser(version=version, description='Some test program to show chect of Python')
    parser.add_option('-f','--file', type='string', dest='file', help='Input DB SQL file for additional data')
    parser.add_option('-s','--save', type='string', dest='save', help='save data')
    parser.add_option('-l','--load', type='string', dest='load', help='load data')
    options,arguments=parser.parse_args()
    print_message ('Запуск программы: '+str(name_bot))
    print ('[!] Автор:'+c23+avtor+c00)
    print ('[!] Версия:'+c23+version+c00)


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

if options.load == 'win':
    print_message ('Разыскиваем победителей')
    koll = 0
    conn = sqlite3.connect("win.sqlite") 
    cursor = conn.cursor()
    connID = sqlite3.connect("win.sqlite") 
    cursorID = conn.cursor()
    sql = "select DISTINCT user_id from site where 1=1 "
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print ('[+] Список пользователей: ',row[0])
        sql = "select user_id,team from site where user_id = '"+str(row[0])+"' "
        cursor.execute(sql)
        dataV = cursor.fetchall()
        kamm   = ''
        sumkam = 0
        for rowV in dataV:
             print ('[+] Лента побед: ',rowV[0],rowV[1])
             ##if rowV[1] == kamm:  
             sumkam = sumkam + 1
             ##else:
                 ##kamm = rowV[1]
                 ##sumkam = 1 
        print ('[+]',row[0],' побед подряд',sumkam)
        if sumkam > 4:
            textmes = str(row[0])
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            keyboard.add(types.InlineKeyboardButton(text=textmes, callback_data='win_'+str(row[0]))) 
            chat_id = '42857380'  ### ЛИЧНОЕ СООБЩЕНИЕ
            bot.send_message(chat_id,'Победители:',reply_markup=keyboard)  
        koll = koll +1  




    print ('[+] Всего в базе найдено пользователей:',koll)
    exit (0)



    ##############################################################          ВЫСЫЛАЕМ НОВЫЕ СЛОВА          ##################################################################
def sendnewword (message,user_id):
    if str(user_id) !=  '42857380':
        conn = sqlite3.connect("word.sqlite") 
        cursor = conn.cursor()
        sql = "select id,name from word where name = '"+str(message)+"' limit 1"
        cursor.execute(sql)
        data = cursor.fetchall()
        label_k = 'no'
        for row in data:
            id_k,name_k = row
            label_k = 'yes'
        if label_k == 'yes':
            ###print ('пропускаем слово есть') 
            pass
        else:
            chat_id = '488522300'  ### ЛИЧНОЕ СООБЩЕНИЕ
            chat_id = '42857380'
            bot.send_message(chat_id,'<b>Новое слово: </b>'+str(message)+'',parse_mode='HTML')
            a = [str(message),'robot']
            cursor.execute("INSERT INTO word (name,title) VALUES (?,?);",a)
            conn.commit()
            lid = cursor.lastrowid



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
    print_message ('Новый пользователь:'+str(user_id))
    mess = 'Ваши данные:'
    mess = mess + '\nusername:'+str(username)
    mess = mess + '\nfirst_name:'+str(first_name)
    mess = mess + '\nlast_name:'+str(last_name)
    mess = mess + '\nuser_id:'+str(user_id)
    bot.send_message(user_id,mess)
    conn = sqlite3.connect("skazka.sqlite") 
    cursor = conn.cursor()
    sql = "select id,name,answer01,answer02,answer03,label,koment from skazka where label = 'test' limit 1"
    cursor.execute(sql)
    data = cursor.fetchall()
    answer01_en = ''
    name_en     = '' 
    for row in data:
        id_en,name_en,answer01_en,answer02_en,answer03_en,label_en,koment_en = row
    print ('[+] Загадка:',name_en)
    if name_en == '':
        #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #markup.row('Правила')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('🤔 Загадки')
        markup.row('🔎 Добыть $','💵 Напечатать $','🏦 Преумножить $')
        markup.row('😈 Украсть $','👮 Защитить $','💰 Клад')
        markup.row('💡Поддержка')
        bot.send_message(user_id,'Очередная загадка будет в ближайшие Пн, Ср или Пт, в 8:00 (МСК). При возникновении вопросов читайте правила. До новых загадок!',reply_markup=markup)

        print ('-1-')        

    else:
        #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #markup.row('Клондайк','Эльдорадо')
        #markup.row('Правила')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('🤔 Загадки')
        markup.row('🔎 Добыть $','💵 Напечатать $','🏦 Преумножить $')
        markup.row('😈 Украсть $','👮 Защитить $','💰 Клад')
        markup.row('💡Поддержка')
        bot.send_message(user_id,name_en,reply_markup=markup)

        print ('-2-')        

    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        user_id = call.message.chat.id
        if call.data.find ("win_") != -1:
            codeglav = call.data.replace("win_","" )
            print ('ПОБЕДА '+codeglav)
            bot.edit_message_text(chat_id=user_id, message_id=call.message.message_id, text='Поздравления отправлены')
            ###chat_id = '399838806'  ### ЛИЧНОЕ СООБЩЕНИ
            bot.send_message(codeglav,'Вы победили !!!')
            conn = sqlite3.connect("win.sqlite") 
            cursor = conn.cursor()
            sql = "DELETE FROM site WHERE user_id = '"+str(codeglav)+"'"  ### УДАЛЯЕМ ЛИШНЕЕ
            cursor.execute(sql)
            conn.commit()


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    user_id    = message.from_user.id 
    message    = message.text.lower()
    print_message ('Сообщение от:'+str(user_id)+'|'+message)
    first_name = ''
    last_name  = ''
    username   = ''
    date       = ''
    name_sk    = ''

    ### Ищем название загадки ###
    conn = sqlite3.connect("skazka.sqlite") 
    cursor = conn.cursor()
    sql = "select id,name,answer01,answer02,answer03,label from skazka where label = 'test' limit 1"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id_sk,name_sk,answer01_sk,answer02_sk,answer03_sk,label_sk = row
        print ('[add]',name_sk) 


    labelmess  = 'no'
    labelnoyes = 'no'
    if message.lower().find ('send') != -1: 
        if str(user_id) == '42857380':
            labelnoyes = 'yes'
            codeglav = message.lower().replace("send","" )
            print ('[+] Отправляем всем сообщение:',codeglav)    
            conn = sqlite3.connect("eldarado.sqlite") 
            cursor = conn.cursor()
            conn.commit()
            try:
                sql = "select DISTINCT user_id from user where 1=1 "
                cursor.execute(sql)
                data = cursor.fetchall()
                for row in data:
                    id_user_u = row[0]
                    print ('[~]',id_user_u,name_sk)
                    ###user_id =  id_user_u
                    try:
                        ###user_id = '399838806'  ### ЛИЧНОЕ СООБЩЕНИЕ
                        if str(id_user_u) != '42857380':
                            bot.send_message(id_user_u,codeglav) 
                            time.sleep(1) 
                    except:
                        pass
            except:
                pass

   




    if  message.lower() == 'start' and str(user_id) == '42857380':
        labelnoyes = 'yes'
        cmd = 'python3 /home/izofen/Language/eldorado/eldarado.py -l skazka'
        args = shlex.split(cmd)
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = p.communicate()[0].decode()
        print (result)
        bot.send_message(user_id,'Команда выполнена')

    if  message.lower() == 'end' and str(user_id) == '42857380':
        labelnoyes = 'yes'
        cmd = 'python3 /home/izofen/Language/eldorado/eldarado.py -l end'
        args = shlex.split(cmd)
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = p.communicate()[0].decode()
        print (result)
        bot.send_message(user_id,'Команда выполнена')

    if  message.lower() == 'win' and str(user_id) == '42857380':
        labelnoyes = 'yes'
        cmd = 'python3 /home/izofen/Language/eldorado/eldarado.py -l win'
        args = shlex.split(cmd)
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = p.communicate()[0].decode()
        print (result)
        bot.send_message(user_id,'Команда выполнена')



    if message.lower().find ('add') != -1 and str(user_id) == '42857380':
        conn_wr = sqlite3.connect("nogood.sqlite") 
        cursor_wr = conn_wr.cursor()
        message = message.lower().replace('add', '')
        message = message.replace(' ', '')
        message = message.strip('')
        a = [message,'avtomat']
        cursor_wr.execute("INSERT INTO world (name,title) VALUES (?,?);",a)
        conn_wr.commit()
        lid = cursor_wr.lastrowid
        bot.send_message(user_id,'Добавил: '+message)

        conn_wr = sqlite3.connect("answer.sqlite") 
        cursor_wr = conn_wr.cursor()
        sql = "DELETE FROM skazka WHERE answer = '"+str(message)+"'"
        cursor_wr.execute(sql)
        conn_wr.commit()
        bot.send_message(user_id,'Очистил базу: '+message)
        labelnoyes = 'yes'


    if  message.lower().find ('dir') != -1 and str(user_id) == '42857380':
        allbad = ''
        conn_wr = sqlite3.connect("nogood.sqlite") 
        cursor_wr = conn_wr.cursor()
        sql = "SELECT id,name,title FROM world WHERE 1=1"
        data_wr = cursor_wr.execute(sql)
        for row_wr in data_wr:
            id_wr,name_wr,title_wr = row_wr
            allbad = allbad +','+name_wr
            ###print(allbad)
        bot.send_message(user_id,'Слова исключения '+allbad[1:])
        labelnoyes = 'yes'

    if  message.lower().find ('del') != -1  and str(user_id) == '42857380':
        conn_wr = sqlite3.connect("nogood.sqlite") 
        cursor_wr = conn_wr.cursor()
        message = message.lower().replace('del', '')
        message = message.replace(' ', '')
        message = message.strip('')
        sql = "DELETE FROM world WHERE name = '"+str(message)+"'"
        cursor_wr.execute(sql)
        conn_wr.commit()
        bot.send_message(user_id,'Удалил: '+message)
        labelnoyes = 'yes'

    if message == 'правила':
        mess = '<b>Правила игры</b>\n'
        mess = mess + '\n'+'1. Каждый Пн, Ср и Пт в 8:00 (МСК) приходит загадка.'
        mess = mess + '\n'+'2. Подсказки и варианты НЕ даются. Правильный ответ сразу НЕ сообщается.'
        mess = mess + '\n'+'3. Отгадка всегда в ед. числе, в 1 слово; часто может иметь 2 и более смысла.'
        mess = mess + '\n'+'4. Всегда обращайте внимание на род (м, ж, ср) слова-отгадки; вообще каждая мелочь в загадке имеет значение.'
        mess = mess + '\n'+'5. Перед ответом игрок выбирает себе команду: Клондайк или Эльдорадо.'
        mess = mess + '\n'+'6. Затем присылает ответ в русской транскрипции, без ошибок.'
        mess = mess + '\n'+'7. Можно дать 1, 2 или 3 ответа, времени дается 24 часа.'
        mess = mess + '\n'+'8. На следующий день приходит правильный ответ и информация о том, какая из двух команд в этот раз победила.'
        mess = mess + '\n'+'9. Команда-победитель определяется по количеству угадавших. Побеждает меньшинство. Напр., угадали загадку 100 чел., из них 49 выбирало Клондайк, а 51 – Эльдорадо. Значит, победила команда Клондайк.'
        mess = mess + '\n'+'10. Все участники команды-победителя проходят дальше и после пяти побед подряд оставшиеся в победителях получают денежный приз из призового фонда.'
        mess = mess + '\n'+'11. Все, кто оказался в проигравшей команде, также могут продолжить играть, просто отсчет для них начнется сначала. То же самое касается всех тех, кто вообще не угадал загадку.'
        mess = mess + '\n'+'12. Правила могут меняться, поэтому советуем иногда заглядывать сюда. При возникновении вопросов обращайтесь к администратору @gluxman.'
        conn = sqlite3.connect("eldarado.sqlite") 
        cursor = conn.cursor()    
        sql = "select user_id,team from user where user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            user_id_b,team_b = row
            print ('[+]',team_b)        
        if team_b == '':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Клондайк','Эльдорадо')
            markup.row('Правила')
        else: 
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Правила')
        mess = mess + '\n'+''
        bot.send_message(user_id,mess,reply_markup=markup,parse_mode='HTML') 
        time.sleep(1) 
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Отправить сообщение другу", url="https://t.me/share/url?url=https%3A//t.me/oren56_bot")
        keyboard.add(url_button)
        bot.send_message(user_id, "Вы можете позвать друзей в группу.\nЭто увеличит шансы добраться до клада.", reply_markup=keyboard)
        labelmess = 'yes'
    
    if message == 'клондайк':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Правила')
        bot.send_message(user_id,'Ждем от Вас ответ (у Вас 24 часа и всего 3 попытки)',reply_markup=markup) 
        conn = sqlite3.connect("eldarado.sqlite") 
        cursor = conn.cursor()
        sql = "UPDATE user SET team = '01' WHERE user_id = '"+str(user_id)+"'"
        cursor.execute(sql)
        conn.commit()
        labelmess = 'yes'

    if message == 'эльдорадо':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Правила')
        bot.send_message(user_id,'Ждем от Вас ответ (у Вас 24 часа и всего 3 попытки)',reply_markup=markup) 
        conn = sqlite3.connect("eldarado.sqlite") 
        cursor = conn.cursor()
        sql = "UPDATE user SET team = '02' WHERE user_id = '"+str(user_id)+"'"
        cursor.execute(sql)
        conn.commit()
        labelmess = 'yes'


    if labelmess == 'no' and labelnoyes == 'no':
        conn = sqlite3.connect("eldarado.sqlite") 
        cursor = conn.cursor()    
        sql = "select user_id,team from user where user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            user_id_b,team_b = row



        if team_b == '':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Клондайк','Эльдорадо')
            markup.row('Правила')
            bot.send_message(user_id,'Сначала надо выбрать команду',reply_markup=markup)
        else: 
            conn = sqlite3.connect("answer.sqlite") 
            cursor = conn.cursor()    
            sql = "select id,user_id,answer from skazka where user_id = '"+str(user_id)+"'and nomerskazky = '"+str(name_sk)+"' "
            cursor.execute(sql)
            data = cursor.fetchall()
            nomeranswer = 0
            labelrepit  = 'no'
            for row in data:
                id_a,user_id_a,answer_a = row
                nomeranswer = nomeranswer +1 
                print ('[*]',user_id_a,answer_a)
                if  message.lower() == answer_a.lower():
                    labelrepit  = 'yes'
            if name_sk == '':
                bot.send_message(user_id,'Очередная загадка будет в ближайшие Пн, Ср или Пт, в 8:00 (МСК). При возникновении вопросов читайте правила. До новых загадок!') ### Время закончино     
            else:
                

                #### ПРОВЕРКА НА повторные символы   
                ###if labelrepit  == 'yes': 
                if 1==2:  
                    pass
                    
                else:

                    #### ПРОВЕРКА НА корректные символы   
                    print ('Проверка на недопустимые символы:',message)
                    goodsim = 'йцукенгшщзхъфывапролджэячсмитьбюё'
                    lbgood = 'no'             
                    for nsim in message.lower():
                        goodsim.find (nsim)                    
                        if goodsim.find (nsim) != -1:
                           pass
                        else: 
                           lbgood = 'yes'
                        ###print ('[s] '+nsim+'|'+str(goodsim.find (nsim))+''+lbgood)                     

                    if nomeranswer > 2:
                        bot.send_message(user_id,'К сожалению, дальнейшие ответы не засчитываются. Дождитесь правильного ответа.')    
                    else:
                        if labelnoyes == 'no': ### КОМАНДЫ ВВОДА  yes это была команда         
                            if lbgood == 'yes':  ### На символы yes означает что символ есть 
                                print ('[+] Найден запрещенный символ')
                                bot.send_message(user_id,'Вводите, пожалуйста, только буквы (в кириллице, в одно слово, без пробелов и прочих знаков).') 
                            else:                        
                                if labelrepit  == 'yes':  ### ПОВТОРНЫЙ ВВОД
                                    bot.send_message(user_id,'Это слово уже вводили.')         
                                else:                                                 
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
                                    else:


                                        lbmat = 'no'  
                                        ### ПРОВЕРКА НА НЕЦЕНЗУРЩИНУ
                                        conn_wr = sqlite3.connect("nogood.sqlite") 
                                        cursor_wr = conn_wr.cursor()    
                                        sql = "select id,name,title from world where 1=1 "
                                        cursor_wr.execute(sql)
                                        data_wr = cursor_wr.fetchall()    
                                        for row_wr in data_wr:
                                            id_wr,name_wr,title_wr = row_wr
                                             
                                            if message.lower() == (name_wr.lower()): 
                                                lbmat = 'yes' 
                                                print (message.lower(),name_wr.lower())
                                                print ('Есть слово для замены') 

                                        if lbmat == 'no':
                                            pass
                                        else:
                                            message = 'XXX'    
                                            

                                        sendnewword (message,user_id) ### ОТПРАВЛЯЕМ НОВОЕ СЛОВО.

                                        ###print (message)

                                        conn = sqlite3.connect("answer.sqlite") 
                                        cursor = conn.cursor()                   
                                        message = message.lower()
                                        a = [user_id,message,name_sk]    
                                        cursor.execute("INSERT INTO skazka (user_id,answer,nomerskazky)VALUES (?,?,?);",a)    
                                        conn.commit()




bot.polling()
