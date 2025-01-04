import telebot
from telebot import types
import config
from questreader import qreader
from bossreader import breader
from database import addUserId
from sender import sendAllPhoto, sendAll
from loger import writeLog

from questreader import news

bot = telebot.TeleBot(config.token)



def newsteller(message):
    if message.text == '74382122932':
        writeLog("Запущенна рассылка с " + str(message.chat.id))
        sendAll(bot,news())
    elif message.text == '74382122932b':
         writeLog("Запущенна фото-рассылка с " + str(message.chat.id))
         sendAllPhoto(bot,news())



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton("Карты и выходы")
    btn2 = types.KeyboardButton("Квесты")
    btn3 = types.KeyboardButton("Боссы")
    btn4 = types.KeyboardButton("Информация")

    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, 'Добро пожаловать в интерактивного бота с картами, ключами, выходами для игры Escape From Tarkov \nЧтобы начать вводить новый запрос по поиску квеста нужно перезайти в меню', reply_markup = markup, parse_mode="Markdown")
    print(message.chat.id)
    writeLog("Новый пользователь добавлен в базу данных. ID:" + str(message.chat.id))
    addUserId(message)

def prapor_quest(message):
    if 'проба' and 'пера' in message.text.lower():
            temp = qreader('prapor','proba_pera')
            bot.send_message(message.chat.id, temp)

    elif 'проверка' and 'вшивость' in message.text.lower():
         temp = qreader('prapor','proverka_na_vshivost')
         bot.send_message(message.chat.id, temp)

    elif 'пикник' and 'стрельбой' in message.text.lower():
         temp = qreader('prapor','piknik_so_strelboy')
         bot.send_message(message.chat.id, temp)

    elif 'посылка' and 'прошлого' in message.text.lower():
         temp = qreader('prapor','posylka_iz_proshlogo')
         bot.send_message(message.chat.id, temp)

    elif 'компромат' in message.text.lower():
         temp = qreader('prapor','Kompromat')
         bot.send_message(message.chat.id, temp)

    elif 'рожки' and 'мороженного' in message.text.lower():
         temp = qreader('prapor','rojki_dlya_morojennogo')
         bot.send_message(message.chat.id, temp)

    elif 'почтальон' and 'печкин' and 'часть 1' in message.text.lower():
         temp = qreader('prapor','pochtalyon_pechkin1')
         bot.send_message(message.chat.id, temp)

    elif 'тряхнуть' and 'кассира' in message.text.lower():
         temp = qreader('prapor','tryahnut_kassira')
         bot.send_message(message.chat.id, temp)
    
    elif 'бомж' and 'полихима' in message.text.lower():
         temp = qreader('prapor','bomj_s_polihima')
         bot.send_message(message.chat.id, temp)
    
    elif 'большой' and 'заказчик' in message.text.lower():
         temp = qreader('prapor','bolshoy_zakazchik')
         bot.send_message(message.chat.id, temp)

    elif 'поисковая' and 'миссия' in message.text.lower():
         temp = qreader('prapor','poiskovaya_missiya')
         bot.send_message(message.chat.id, temp)

    elif 'нефтянка' in message.text.lower():
         temp = qreader('prapor','neftyanka')
         bot.send_message(message.chat.id, temp)

    elif 'бункер' and 'часть 1' in message.text.lower():
         temp = qreader('prapor','bunker1')
         bot.send_message(message.chat.id, temp)

    elif 'бункер' and 'часть 2' in message.text.lower():
         temp = qreader('prapor','bunker2')
         bot.send_message(message.chat.id, temp)

    elif 'ренегатам' and 'место' in message.text.lower():
         temp = qreader('prapor','renegatam_tut_ne_mesto')
         bot.send_message(message.chat.id, temp)

    elif 'Документы' in message.text.lower():
         temp = qreader('prapor','dokumenty')
         bot.send_message(message.chat.id, temp)

    elif 'идеальный' and 'переговорщик' in message.text.lower():
         temp = qreader('prapor','idealniy_peregovorshik')
         bot.send_message(message.chat.id, temp)

    elif 'гренадер' in message.text.lower():
         temp = qreader('prapor','grenader')
         bot.send_message(message.chat.id, temp)

    elif 'каратель' and 'часть 1' in message.text.lower():
         temp = qreader('prapor','karatel1')
         bot.send_message(message.chat.id, temp)

    elif 'анестезия' in message.text.lower():
         temp = qreader('prapor','anestezia')
         bot.send_message(message.chat.id, temp)

    elif 'тест' and 'драйв' and 'часть 1' in message.text.lower():
         temp = qreader('prapor','test_drive1')
         bot.send_message(message.chat.id, temp)

    elif 'поставщик' in message.text.lower():
         temp = qreader('prapor','postavshik')
         bot.send_message(message.chat.id, temp)

    elif 'каратель' and 'часть 2' in message.text.lower():
         temp = qreader('prapor','karatel2')
         bot.send_message(message.chat.id, temp)

    elif 'каратель' and 'часть 3' in message.text.lower():
         temp = qreader('prapor','karatel3')
         bot.send_message(message.chat.id, temp)

    elif 'каратель' and 'часть 4' in message.text.lower():
         temp = qreader('prapor','karatel4')
         bot.send_message(message.chat.id, temp)

    elif 'каратель' and 'часть 5' in message.text.lower():
         temp = qreader('prapor','karatel5')
         bot.send_message(message.chat.id, temp)

    elif 'каратель' and 'часть 6' in message.text.lower():
         temp = qreader('prapor','karatel6')
         bot.send_message(message.chat.id, temp)

    elif 'устрашитель' in message.text.lower():
         temp = qreader('prapor','ustrashitel')
         bot.send_message(message.chat.id, temp)

    elif 'захват' and 'аванпоста' in message.text.lower():
         temp = qreader('prapor','zahvat_avanposta')
         bot.send_message(message.chat.id, temp)

    elif 'конвоир' in message.text.lower():
         temp = qreader('prapor','konvoir')
         bot.send_message(message.chat.id, temp)
    
    elif 'без' and 'обид' in message.text.lower():
         temp = qreader('prapor','bez_obid')
         bot.send_message(message.chat.id, temp)

    elif 'простая' and 'задача' and 'часть 1' in message.text.lower():
         temp = qreader('prapor','Prostaya_zadacha1')
         bot.send_message(message.chat.id, temp)

    elif 'простая' and 'задача' and 'часть 2' in message.text.lower():
         temp = qreader('prapor','Prostaya_zadacha2')
         bot.send_message(message.chat.id, temp)

    elif 'своя' and 'земля' in message.text.lower():
         temp = qreader('prapor','svoya_zemlya')
         bot.send_message(message.chat.id, temp)
         
    elif 'разведка' in message.text.lower():
         temp = qreader('prapor','razvedka')
         bot.send_message(message.chat.id, temp)

    elif 'вам' and 'посылка' in message.text.lower():
         temp = qreader('prapor','vam_posylka')
         bot.send_message(message.chat.id, temp)
         pocht = open('maps/pochta.jpg', 'rb')
         bot.send_photo(message.chat.id, pocht)

    elif 'зеленый' and 'коридор' in message.text.lower():
         temp = qreader('prapor','zeleny_koridor')
         bot.send_message(message.chat.id, temp)\
         
    elif 'короли' and 'высоток' in message.text.lower():
         temp = qreader('prapor','koroli_vysotok')
         bot.send_message(message.chat.id, temp)

    elif 'слава' and 'кпсс' and 'часть 1' in message.text.lower():
         temp = qreader('prapor','slava_kpss1')
         bot.send_message(message.chat.id, temp)

    elif 'тест' and 'драйв' and 'часть 2' in message.text.lower():
         temp = qreader('prapor','test_drive2')
         bot.send_message(message.chat.id, temp)

    elif 'лучшая' and 'работа' and 'свете' in message.text.lower():
         temp = qreader('prapor','luchshaya_rabota_na_svete')
         bot.send_message(message.chat.id, temp)
    
    elif 'слава' and 'кпсс' and 'часть 2' in message.text.lower():
         temp = qreader('prapor','slava_kpss2')
         bot.send_message(message.chat.id, temp)

    elif 'городской' and 'жандарм' and 'охранник' and 'супермаркета' in message.text.lower():
         temp = qreader('prapor','gorodskoy_jandarm_ohrannik_supermaketa')
         bot.send_message(message.chat.id, temp)

    elif 'городской' and 'жандарм' and 'прерванный' and 'сеанс' in message.text.lower():
         temp = qreader('prapor','gorodskoy_jandarm_prervanny_seans')
         bot.send_message(message.chat.id, temp)

    elif 'городской' and 'жандарм' and 'новый' and 'участковый' in message.text.lower():
         temp = qreader('prapor','gorodskoy_jandarm_novy_uchastkovy')
         bot.send_message(message.chat.id, temp)

    elif 'тест' and 'драйв' and 'часть 3' in message.text.lower():
         temp = qreader('prapor','test_drive3')
         bot.send_message(message.chat.id, temp)

    elif 'стрельба' and 'баночкам' in message.text.lower():
         temp = qreader('prapor','strelba_po_banochkam')
         bot.send_message(message.chat.id, temp)

    elif 'роскошная' and 'жизнь' in message.text.lower():
         temp = qreader('prapor','roskoshnaya_jizn')
         bot.send_message(message.chat.id, temp)

    elif 'земельный' and 'вопрос' in message.text.lower():
         temp = qreader('prapor','zemelny_vopros')
         bot.send_message(message.chat.id, temp)

    elif 'тест' and 'драйв' and 'часть 4' in message.text.lower():
         temp = qreader('prapor','test_drive4')
         bot.send_message(message.chat.id, temp)

    elif 'как' and 'старые' and 'добрые' and 'часть 1' in message.text.lower():
         temp = qreader('prapor','kak_v_stary_dobrie1')
         bot.send_message(message.chat.id, temp)

    elif 'ад' and 'земле' and 'часть 1' in message.text.lower():
         temp = qreader('prapor','ad_na_zemle1')
         bot.send_message(message.chat.id, temp)
    
    elif 'ад' and 'земле' and 'часть 2' in message.text.lower():
         temp = qreader('prapor','ad_na_zemle2')
         bot.send_message(message.chat.id, temp)

    elif 'как' and 'старые' and 'добрые' and 'часть 2' in message.text.lower():
         temp = qreader('prapor','kak_v_stary_dobrie2')
         bot.send_message(message.chat.id, temp)

    elif 'наблюдатель' in message.text.lower():
         temp = qreader('prapor','nabludatel')
         bot.send_message(message.chat.id, temp)

    elif 'чужой' and 'шкуре' in message.text.lower():
         temp = qreader('prapor','v_chujoy_shkure')
         bot.send_message(message.chat.id, temp)

    elif 'как' and 'старые' and 'добрые' and 'часть 1' in message.text.lower():
         temp = qreader('prapor','kak_v_stary_dobrie1')
         bot.send_message(message.chat.id, temp)

    elif 'тест' and 'драйв' and 'часть 5' in message.text.lower():
         temp = qreader('prapor','test_drive5')
         bot.send_message(message.chat.id, temp)

    elif 'спецсвязь' in message.text.lower():
         temp = qreader('prapor','spec_svyaz')
         bot.send_message(message.chat.id, temp)

    elif 'белка' and 'стрелка' in message.text.lower():
         temp = qreader('prapor','belka_i_strelka')
         bot.send_message(message.chat.id, temp)
    
    elif 'новогодний' and 'стол' in message.text.lower():
         temp = qreader('prapor','novogodny_stol')
         bot.send_message(message.chat.id, temp)

    elif 'horovod'in message.text.lower():
         temp = qreader('prapor','horovod')
         bot.send_message(message.chat.id, temp)

    elif 'это' and 'моя' and 'вечеринка' in message.text.lower():
         temp = qreader('prapor','eto_moya_vecherinka')
         bot.send_message(message.chat.id, temp)



        

    

    

    else:
         bot.send_message(message.chat.id,'Квест не найден')
     
@bot.message_handler(commands=['newsteller'])
def newsteller2(message):
    bot.send_message(message.chat.id, "Введите пароль")
    writeLog("Пользователь " + str(message.chat.id) + "вызвал запрос рассылки")
    bot.register_next_step_handler(message, newsteller)
    
                



@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == "Информация":
            bot.send_message(message.chat.id, "Бот был создан в любительских целях, вся информация бралась с таких сайтов как https://tarkov.dev/ и https://tarkov.help/ru ")
        elif message.text == "Карты и выходы":
              markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
              Street = types.KeyboardButton('Улицы таркова')
              epi = types.KeyboardButton('Эпицентр')
              Bereg = types.KeyboardButton('Берег')
              zavod = types.KeyboardButton('Завод')
              labs = types.KeyboardButton('Лабаратория')
              woods = types.KeyboardButton('Лес')
              razvyaz = types.KeyboardButton('Развязка')
              rezerv = types.KeyboardButton('Резерв')
              tamog = types.KeyboardButton('Таможня')
              mayak = types.KeyboardButton('Маяк')
              back = types.KeyboardButton("Назад")

              markup.add(Street, epi, Bereg, zavod, labs, woods, razvyaz, rezerv, tamog, mayak, back)
              bot.send_message(message.chat.id, "Вы в меню карты и выходы", reply_markup = markup)



        elif message.text == "Таможня":
             tamog = open('maps/Tamoga.png', 'rb')
             bot.send_photo(message.chat.id, tamog)
             bot.send_message(message.chat.id, 'Контейнеры: \n11x Выдвижной ящик \n5x Гранатный ящик \n37x Деревянный ящик \n57x Закопанная бочка \n6x Кассовый аппарат \n54x Куртка \n5x Медсумка СМУ06 \n 8x Медукладка \n10x Мертвый дикий \n25x Малый оружейный ящик \n7x Патронный ящик \n7x Сейф, \n12x Системный блок, \n51x Спортивная сумка \n9x Схрон в земле \n2x Ящик медицины \n11x Ящик с инструментами \n1x Ящик продовольствия \n7x Ящик технического снабжения \n10x Большой черный оружейный ящик \n3x Большой зеленый оружейный ящик \n16x Плоский оружейный ящик')
             bot.send_message(message.chat.id, 'Лут: \n17x Ценности \n29x Электроника \n7x Элементы питания \n7x Раздведанные \n117x Провизия \n52x Медикаменты и Медматериалы \n 14x Стройматериалы \n15x Хозтовары \n6x Флешка \n10x Горюче-Смазочные \n21x Топливо \n17x Инструменты \n16x Оружие \n28x Модификации \n28x Ключи \n2x Броня Модуль-3М \n38x Коробка с патронами \n2x Патроны \n1x M4A1 \n23x Фото и переход \n6x Фильтры \n13x Ремкомплекты для брони и оружия \n4x Меченая комната - удачный спавн \n1x Старая заправка - удачный спавн \n2x За старой заправкой - удачный спавн \n5x Предметы для бартера - удачный спавн')
        
        elif message.text == "Берег":
             berega = open('maps/bereg.jpg', 'rb')
             bot.send_photo(message.chat.id, berega)

        elif message.text == "Лес":
             lesa = open('maps/les.jpg', 'rb')
             bot.send_photo(message.chat.id, lesa)

        elif message.text == "Завод":
             zadoda = open('maps/zavod.jpg', 'rb')
             bot.send_photo(message.chat.id, zadoda)

        elif message.text == "Лабаратория":
             laba = open('maps/lab.png', 'rb')
             bot.send_photo(message.chat.id, laba)

        elif message.text == "Маяк":
             mayaka = open('maps/mayak.png', 'rb')
             bot.send_photo(message.chat.id, mayaka)

        elif message.text == "Развязка":
             razvyaza = open('maps/razvyaz.png', 'rb')
             bot.send_photo(message.chat.id, razvyaza)

        elif message.text == "Улицы таркова":
             streetsa = open('maps/streets.png', 'rb')
             bot.send_photo(message.chat.id, streetsa)

        elif message.text == "Эпицентр":
             epi = open('maps/streets.png', 'rb')
             bot.send_photo(message.chat.id, epi)

        elif message.text == "Резерв":
             rez = open('maps/rezerv.png', 'rb')
             bot.send_photo(message.chat.id, rez)

        elif message.text == "Квесты":
              markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
              Prapor = types.KeyboardButton('Квесты Прапора')
              Terap = types.KeyboardButton('Квесты Терапевта')
              Skup = types.KeyboardButton('Квесты Скупщика')
              lyj = types.KeyboardButton('Квесты Лыжника')
              mir = types.KeyboardButton('Квесты миратворца')
              mech = types.KeyboardButton('Квесты механика')
              barah = types.KeyboardButton('Квесты Барахольщика')
              eger = types.KeyboardButton('Квесты Егеря')
              tamog = types.KeyboardButton('Таможня')
              smotr = types.KeyboardButton('Квесты Смотрителя')
              back = types.KeyboardButton("Назад")

              markup.add(Prapor, Terap, Skup, lyj, mir, mech, barah, eger, smotr, back)
              bot.send_message(message.chat.id, "Вы в меню квестов", reply_markup = markup)
        elif message.text == "Квесты Прапора":
             bot.send_message(message.chat.id, 'Введите название квеста')
             bot.register_next_step_handler(message, prapor_quest)

        elif message.text == "Квесты Барахольщика":
             bot.send_message(message.chat.id, 'Введите название квеста')
             bot.register_next_step_handler(message, baraholshik_quest)

        elif message.text == "Квесты Терапевта":
             bot.send_message(message.chat.id, 'Введите название квеста')
             bot.register_next_step_handler(message, terapevt_quest)

        elif message.text == "Квесты Скупщика":
             bot.send_message(message.chat.id, 'Введите название квеста')
             bot.register_next_step_handler(message, skupshik_quest)

        elif message.text == "Квесты Смотрителя":
             bot.send_message(message.chat.id, 'Введите название квеста')
             bot.register_next_step_handler(message, smotritel_quest)

        elif message.text == "Квесты Миратворца":
             bot.send_message(message.chat.id, 'Введите название квеста')
             bot.register_next_step_handler(message, miratvorec_quest)

        elif message.text == "Квесты Механика":
             bot.send_message(message.chat.id, 'Введите название квеста')
             bot.register_next_step_handler(message, mechanik_quest)


            
        elif message.text == 'Назад':
             markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
             btn1 = types.KeyboardButton("Карты и выходы")
             btn2 = types.KeyboardButton("Квесты")
             btn3 = types.KeyboardButton("Информация")
             btn4 = types.KeyboardButton("Боссы")

             markup.add(btn1, btn2, btn3, btn4)

             bot.send_message(message.chat.id, 'Добро пожаловать в интерактивного бота с картами, ключами, выходами для игры Escape From Tarkov', reply_markup = markup)
        elif message.text == 'Боссы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            boss1 = types.KeyboardButton('Глухарь')
            boss2 = types.KeyboardButton('Дед мороз')
            boss3 = types.KeyboardButton('Зрячий')
            boss4 = types.KeyboardButton('Кабан')
            boss5 = types.KeyboardButton('Килла')
            boss6 = types.KeyboardButton('Колонтай')
            boss7 = types.KeyboardButton('Отступник')
            boss8 = types.KeyboardButton('Партизан')
            boss9 = types.KeyboardButton('Рейдер')
            boss10 = types.KeyboardButton('Решала')
            boss11 = types.KeyboardButton('Санитар')
            boss12 = types.KeyboardButton('Сектант Жрец')
            boss13 = types.KeyboardButton('Тагилла')
            boss14 = types.KeyboardButton('Штурман')
            boss15 = types.KeyboardButton('Knight')
            back = types.KeyboardButton("Назад")
            markup.add(boss1, boss2, boss3, boss4, boss5, boss6, boss7, boss8, boss9, boss10, boss11, boss12, boss13, boss14, boss15, back)
            bot.send_message(message.chat.id, "Вы в меню боссы", reply_markup = markup)
        
        elif message.text == 'Глухарь':
            temp2 = breader('glukhar')
            bot.send_message(message.chat.id, temp2)
            gluh = open('bossphto/glukh.jpg', 'rb')
            bot.send_photo(message.chat.id, gluh)

        elif message.text == "Дед мороз":
            temp2 = breader('moroz')
            bot.send_message(message.chat.id, temp2)
            moroz2 = open('bossphto/moroz.jpg', 'rb')
            bot.send_photo(message.chat.id, moroz2)

        elif message.text == "Зрячий":
            temp2 = breader('moroz')
            bot.send_message(message.chat.id, temp2)
            zryachiy2 = open('bossphto/zryachiy.jpg', 'rb')
            bot.send_photo(message.chat.id, zryachiy2)

        elif message.text == "Кабан":
            temp2 = breader('kaban')
            bot.send_message(message.chat.id, temp2)
            kaban1 = open('bossphto/kaban.jpg', 'rb')
            bot.send_photo(message.chat.id, kaban1)

        elif message.text == "Килла":
            temp2 = breader('killa')
            bot.send_message(message.chat.id, temp2)
            killa1 = open('bossphto/killa.jpg', 'rb')
            bot.send_photo(message.chat.id, killa1)

        elif message.text == "Колонтай":
            temp2 = breader('colontay')
            bot.send_message(message.chat.id, temp2)
            colontay1 = open('bossphto/colontay.jpg', 'rb')
            bot.send_photo(message.chat.id, colontay1, parse_mode="Markdown")

        elif message.text == "Отступник":
            temp2 = breader('otstupnik')
            bot.send_message(message.chat.id, temp2)
            otstupnik1 = open('bossphto/otstupnik.jpg', 'rb')
            bot.send_photo(message.chat.id, otstupnik1)

        elif message.text == "Партизан":
            temp2 = breader('partizan')
            bot.send_message(message.chat.id, temp2)
            partizan1 = open('bossphto/partizan.jpg', 'rb')
            bot.send_photo(message.chat.id, partizan1)

        elif message.text == "Рейдер":
            temp2 = breader('raider')
            bot.send_message(message.chat.id, temp2)
            raider1 = open('bossphto/raider.jpg', 'rb')
            bot.send_photo(message.chat.id, raider1)

        elif message.text == "Решала":
            temp2 = breader('reshala')
            bot.send_message(message.chat.id, temp2)
            reshala1 = open('bossphto/otstupnik.jpg', 'rb')
            bot.send_photo(message.chat.id, reshala1)

        elif message.text == "Санитар":
            temp2 = breader('sanitar')
            bot.send_message(message.chat.id, temp2)
            sanitar1 = open('bossphto/sanitar.jpg', 'rb')
            bot.send_photo(message.chat.id, sanitar1)

        elif message.text == "Сектант Жрец":
            temp2 = breader('sectant')
            bot.send_message(message.chat.id, temp2)
            sectant1 = open('bossphto/sectant.jpg', 'rb')
            bot.send_photo(message.chat.id, sectant1)

        elif message.text == "Тагилла":
            temp2 = breader('tagila')
            bot.send_message(message.chat.id, temp2)
            tagila1 = open('bossphto/tagila.jpg', 'rb')
            bot.send_photo(message.chat.id, tagila1)

        elif message.text == "Штурман":
            temp2 = breader('shturman')
            bot.send_message(message.chat.id, temp2)
            shturman1 = open('bossphto/shturman.jpg', 'rb')
            bot.send_photo(message.chat.id, shturman1)

        elif message.text == "Knight":
            temp2 = breader('Knight')
            bot.send_message(message.chat.id, temp2)
            Knight1 = open('bossphto/knight.jpg', 'rb')
            bot.send_photo(message.chat.id, Knight1)

     

def baraholshik_quest(message):
    if 'только' and 'бизнес' in message.text.lower():
            temp = qreader('baraholshik','tolko_biznes')
            bot.send_message(message.chat.id, temp)

    elif 'распродажа' in message.text.lower():
               temp = qreader('baraholshik','rasprodaja')
               bot.send_message(message.chat.id, temp)

    elif 'вернем' and 'ультре' and 'былое' and 'величие' in message.text.lower():
               temp = qreader('baraholshik','ultra')
               bot.send_message(message.chat.id, temp)

    elif 'топливный' and 'вопрос' in message.text.lower():
               temp = qreader('baraholshik','toplivo')
               bot.send_message(message.chat.id, temp)

    elif 'кровь' and 'войны' in message.text.lower():
               temp = qreader('baraholshik','krov')
               bot.send_message(message.chat.id, temp)

    elif 'картотека' and 'часть 1' in message.text.lower():
               temp = qreader('baraholshik','kartoteka1')
               bot.send_message(message.chat.id, temp)

    elif 'знаток' and 'резерва' in message.text.lower():
               temp = qreader('baraholshik','znatok')
               bot.send_message(message.chat.id, temp)

    elif 'модный' and 'приговор' in message.text.lower():
               temp = qreader('baraholshik','prigovor')
               bot.send_message(message.chat.id, temp)

    elif 'картотека' and 'часть 2' in message.text.lower():
               temp = qreader('baraholshik','kartoteka2')
               bot.send_message(message.chat.id, temp)

    elif 'благодарность' in message.text.lower():
               temp = qreader('baraholshik','blagodarnost')
               bot.send_message(message.chat.id, temp)

    elif 'ночь' and 'распродаж' in message.text.lower():
               temp = qreader('baraholshik','noch')
               bot.send_message(message.chat.id, temp)

    elif 'шить' and 'тужить' and 'часть 1' in message.text.lower():
               temp = qreader('baraholshik','tujit1')
               bot.send_message(message.chat.id, temp)

    elif 'маршрутка' in message.text.lower():
               temp = qreader('baraholshik','marshrutka')
               bot.send_message(message.chat.id, temp)

    elif 'шить' and 'тужить' and 'часть 2' in message.text.lower():
               temp = qreader('baraholshik','tujit2')
               bot.send_message(message.chat.id, temp)

    elif 'кровь' and 'войны' and 'часть 2' in message.text.lower():
               temp = qreader('baraholshik','krov2')
               bot.send_message(message.chat.id, temp)

    elif 'Скавенжер' in message.text.lower():
               temp = qreader('baraholshik','skavenger')
               bot.send_message(message.chat.id, temp)

    elif 'супервайзер' in message.text.lower():
               temp = qreader('baraholshik','supervizer')
               bot.send_message(message.chat.id, temp)

    elif 'секрет' and 'успеха' in message.text.lower():
               temp = qreader('baraholshik','secret_uspeha')
               bot.send_message(message.chat.id, temp)


    elif 'шить' and 'тужить' and 'часть 3' in message.text.lower():
               temp = qreader('baraholshik','tujit3')
               bot.send_message(message.chat.id, temp)


    elif 'кровь' and 'войны' and 'часть 3' in message.text.lower():
               temp = qreader('baraholshik','krov3')
               bot.send_message(message.chat.id, temp)

    elif 'длинная' and 'очередь' in message.text.lower():
               temp = qreader('baraholshik','ochered')
               bot.send_message(message.chat.id, temp)

    elif 'выпивка' in message.text.lower():
               temp = qreader('baraholshik','vipivka')
               bot.send_message(message.chat.id, temp)

    elif 'борода' and 'нужна' in message.text.lower():
               temp = qreader('baraholshik','boroda')
               bot.send_message(message.chat.id, temp)

    elif 'шить' and 'тужить' and 'часть 4' in message.text.lower():
               temp = qreader('baraholshik','tujit4')
               bot.send_message(message.chat.id, temp)

    elif 'красиво' and 'жить' and "запретишь" and 'часть 1' in message.text.lower():
               temp = qreader('baraholshik','krasivo1')
               bot.send_message(message.chat.id, temp)

    elif 'красиво' and 'жить' and "запретишь" and 'часть 2' in message.text.lower():
               temp = qreader('baraholshik','krasivo2')
               bot.send_message(message.chat.id, temp)

    elif 'текстиль' and 'часть 1' in message.text.lower():
               temp = qreader('baraholshik','tekstil1')
               bot.send_message(message.chat.id, temp)

    elif 'текстиль' and 'часть 2' in message.text.lower():
               temp = qreader('baraholshik','tekstil2')
               bot.send_message(message.chat.id, temp)

    elif 'аудит' in message.text.lower():
               temp = qreader('baraholshik','audit')
               bot.send_message(message.chat.id, temp)

    elif 'любитель' and 'балета' in message.text.lower():
               temp = qreader('baraholshik','balet')
               bot.send_message(message.chat.id, temp)

    elif 'меломан' in message.text.lower():
               temp = qreader('baraholshik','meloman')
               bot.send_message(message.chat.id, temp)

    elif 'выгодная' and 'сделка' in message.text.lower():
               temp = qreader('baraholshik','sdelka')
               bot.send_message(message.chat.id, temp)

    elif 'стиляги' in message.text.lower():
               temp = qreader('baraholshik','stilyagi')
               bot.send_message(message.chat.id, temp)

    elif 'обновка' and 'часть 1' in message.text.lower():
               temp = qreader('baraholshik','obnovka1')
               bot.send_message(message.chat.id, temp)


    elif 'обновка' and 'часть 2' in message.text.lower():
               temp = qreader('baraholshik','obnovka2')
               bot.send_message(message.chat.id, temp)

    elif 'невидимая' and 'рука' and 'рынка' in message.text.lower():
               temp = qreader('baraholshik','ruka')
               bot.send_message(message.chat.id, temp)

    elif 'ключ' and 'города' in message.text.lower():
               temp = qreader('baraholshik','key')
               bot.send_message(message.chat.id, temp)

    elif 'пустить' and 'оборот' in message.text.lower():
               temp = qreader('baraholshik','oborot')
               bot.send_message(message.chat.id, temp)

    elif 'специальное' and 'предложение' in message.text.lower():
               temp = qreader('baraholshik','spec')
               bot.send_message(message.chat.id, temp)

    elif 'проверенный' and 'товар' in message.text.lower():
               temp = qreader('baraholshik','tovar')
               bot.send_message(message.chat.id, temp)

    elif 'знай' and 'свое' and 'место' in message.text.lower():
               temp = qreader('baraholshik','mesto')
               bot.send_message(message.chat.id, temp)

    elif 'спрятать' and 'видном' and 'месте' in message.text.lower():
               temp = qreader('baraholshik','spryatat')
               bot.send_message(message.chat.id, temp)

    elif 'сорвать' and 'сделку' in message.text.lower():
               temp = qreader('baraholshik','sorvat')
               bot.send_message(message.chat.id, temp)

    elif 'этому' and 'больше' and 'наливать' in message.text.lower():
               temp = qreader('baraholshik','spryatat')
               bot.send_message(message.chat.id, temp)

    else:
         bot.send_message(message.chat.id,'Квест не найден')



def terapevt_quest(message):
     if 'дефицит' in message.text.lower():
            temp = qreader('terapevt','deficit')
            bot.send_message(message.chat.id, temp)

     elif 'cанэпиднадзор' and 'часть 1' in message.text.lower():
            temp = qreader('terapevt','epidnadzor1')
            bot.send_message(message.chat.id, temp)

     elif 'операция' and 'водолей' in message.text.lower():
            temp = qreader('terapevt','vodoley1')
            bot.send_message(message.chat.id, temp)

     elif 'почтальон' and 'печкин' and 'часть 2' in message.text.lower():
            temp = qreader('terapevt','pechkin2')
            bot.send_message(message.chat.id, temp)

     elif 'санэпиднадзор' and 'часть 2' in message.text.lower():
            temp = qreader('terapevt','epidnadzor2')
            bot.send_message(message.chat.id, temp)

     elif 'операция' and 'водолей' and 'часть 2' in message.text.lower():
            temp = qreader('terapevt','vodoley2')
            bot.send_message(message.chat.id, temp)

     elif 'пейнкиллер' in message.text.lower():
            temp = qreader('terapevt','pain')
            bot.send_message(message.chat.id, temp)

     elif 'провизор' in message.text.lower():
            temp = qreader('terapevt','provizor')
            bot.send_message(message.chat.id, temp)

     elif 'медецинский' and 'журнал' in message.text.lower():
            temp = qreader('terapevt','jurnal')
            bot.send_message(message.chat.id, temp)

     elif 'планы' and 'снабжения' in message.text.lower():
            temp = qreader('terapevt','plan')
            bot.send_message(message.chat.id, temp)

     elif 'врачебная' and 'тайна' and 'часть 1' in message.text.lower():
            temp = qreader('terapevt','tayna1')
            bot.send_message(message.chat.id, temp)

     elif 'авторем' in message.text.lower():
            temp = qreader('terapevt','autorem')
            bot.send_message(message.chat.id, temp)

     elif 'сельпо' in message.text.lower():
            temp = qreader('terapevt','selpo')
            bot.send_message(message.chat.id, temp)

     elif 'врачебная' and 'тайна' and 'часть 2' in message.text.lower():
            temp = qreader('terapevt','tayna2')
            bot.send_message(message.chat.id, temp)

     elif 'врачебная' and 'тайна' and 'часть 3' in message.text.lower():
            temp = qreader('terapevt','tayna3')
            bot.send_message(message.chat.id, temp)

     elif 'коллеги' and 'часть 2' in message.text.lower():
            temp = qreader('terapevt','kollegi2')
            bot.send_message(message.chat.id, temp)

     elif 'врачебная' and 'тайна' and 'часть 4' in message.text.lower():
            temp = qreader('terapevt','tayna4')
            bot.send_message(message.chat.id, temp)

     elif 'здоровом' and 'теле' and 'здоровый' and 'дух' in message.text.lower():
            temp = qreader('terapevt','dux')
            bot.send_message(message.chat.id, temp)

     elif 'физкультурник' in message.text.lower():
            temp = qreader('terapevt','fizcult')
            bot.send_message(message.chat.id, temp)

     elif 'врачебная' and 'тайна' and 'часть 5' in message.text.lower():
            temp = qreader('terapevt','tayna5')
            bot.send_message(message.chat.id, temp)

     elif 'частная' and 'клиника' in message.text.lower():
            temp = qreader('terapevt','clinika')
            bot.send_message(message.chat.id, temp)

     elif 'служба' and 'дезинфекции' in message.text.lower():
            temp = qreader('terapevt','slujba')
            bot.send_message(message.chat.id, temp)

     elif 'коллеги' and 'часть 3' in message.text.lower():
            temp = qreader('terapevt','kollegi3')
            bot.send_message(message.chat.id, temp)

     elif 'доктор' and 'айболит' in message.text.lower():
            temp = qreader('terapevt','doc')
            bot.send_message(message.chat.id, temp)

     elif 'простое' and 'любопытство' in message.text.lower():
            temp = qreader('terapevt','prosto')
            bot.send_message(message.chat.id, temp)

     elif 'забудем' and 'старые' and 'обиды' in message.text.lower():
            temp = qreader('terapevt','zabudem')
            bot.send_message(message.chat.id, temp)

     elif 'потерянный' and 'контакт' in message.text.lower():
            temp = qreader('terapevt','lost')
            bot.send_message(message.chat.id, temp)

     elif 'отдых' and 'моря' in message.text.lower():
            temp = qreader('terapevt','chill')
            bot.send_message(message.chat.id, temp)

     elif 'наркотрафик' in message.text.lower():
            temp = qreader('terapevt','narko')
            bot.send_message(message.chat.id, temp)

     elif 'перепись' and 'населения' in message.text.lower():
            temp = qreader('terapevt','perepis')
            bot.send_message(message.chat.id, temp)

     elif 'опасная' and 'дорога' in message.text.lower():
            temp = qreader('terapevt','danger')
            bot.send_message(message.chat.id, temp)

     elif 'городская' and 'медицина' in message.text.lower():
            temp = qreader('terapevt','med')
            bot.send_message(message.chat.id, temp)

     elif 'инвентаризация' and 'часть 1' in message.text.lower():
            temp = qreader('terapevt','invent1')
            bot.send_message(message.chat.id, temp)

     elif 'фельдшер' in message.text.lower():
            temp = qreader('terapevt','feldsher')
            bot.send_message(message.chat.id, temp)

     elif 'первый' and 'очереди' in message.text.lower():
            temp = qreader('terapevt','ochered')
            bot.send_message(message.chat.id, temp)

     elif 'инвентаризация' and 'часть 2' in message.text.lower():
            temp = qreader('terapevt','invent2')
            bot.send_message(message.chat.id, temp)

     elif 'стандарт' and 'качаства' in message.text.lower():
            temp = qreader('terapevt','standart')
            bot.send_message(message.chat.id, temp)

     elif 'водохлеб' and 'эхо' in message.text.lower():
            temp = qreader('terapevt','eho')
            bot.send_message(message.chat.id, temp)

     elif 'водохлеб' and 'секреты' in message.text.lower():
            temp = qreader('terapevt','secrety')
            bot.send_message(message.chat.id, temp)

     elif 'врачебная' and 'тайна' and 'часть 6' in message.text.lower():
            temp = qreader('terapevt','tayna6')
            bot.send_message(message.chat.id, temp)

     elif 'здоровая' and 'альтернатива' in message.text.lower():
            temp = qreader('terapevt','secrety')
            bot.send_message(message.chat.id, temp)

     elif 'все' and 'тайное' and 'становится' and 'явным' in message.text.lower():
            temp = qreader('terapevt','yavnoye')
            bot.send_message(message.chat.id, temp)

     elif 'непарадный' and 'тарков' in message.text.lower():
            temp = qreader('terapevt','tarkov')
            bot.send_message(message.chat.id, temp)

     elif 'брошенный' and 'груз' in message.text.lower():
            temp = qreader('terapevt','gruz')
            bot.send_message(message.chat.id, temp)

     elif 'отследить' and 'направление' in message.text.lower():
            temp = qreader('terapevt','naprav')
            bot.send_message(message.chat.id, temp)

     elif 'ближе' and 'народу' in message.text.lower():
            temp = qreader('terapevt','narod')
            bot.send_message(message.chat.id, temp)
     
     else:
         bot.send_message(message.chat.id,'Квест не найден')

def skupshik_quest(message):
     if 'Выбор' in message.text.lower():
            temp = qreader('skupshik','vybor')
            bot.send_message(message.chat.id, temp)

     elif 'сделка' and 'совестью' and 'часть 1' in message.text.lower():
            temp = qreader('skupshik','sdelka1')
            bot.send_message(message.chat.id, temp)

     elif 'между' and 'двух' and 'огней' in message.text.lower():
            temp = qreader('skupshik','fire')
            bot.send_message(message.chat.id, temp)

     elif 'наладить' and 'контакт' in message.text.lower():
            temp = qreader('skupshik','contact')
            bot.send_message(message.chat.id, temp)

     elif 'свой' and 'среди' and 'чужих' in message.text.lower():
            temp = qreader('skupshik','svoy')
            bot.send_message(message.chat.id, temp)

     elif 'резистентность' in message.text.lower():
            temp = qreader('skupshik','rezist')
            bot.send_message(message.chat.id, temp)

     elif 'малое' and 'предпринимательство' and 'часть 1' in message.text.lower():
            temp = qreader('skupshik','predpren1')
            bot.send_message(message.chat.id, temp)

     elif 'малое' and 'предпринимательство' and 'часть 2' in message.text.lower():
            temp = qreader('skupshik','predpren2')
            bot.send_message(message.chat.id, temp)

     elif 'малое' and 'предпринимательство' and 'часть 3' in message.text.lower():
            temp = qreader('skupshik','predpren3')
            bot.send_message(message.chat.id, temp)

     elif 'марафон' and 'конца' and 'конец' in message.text.lower():
            temp = qreader('skupshik','maraphon')
            bot.send_message(message.chat.id, temp)

     elif 'что то' and 'мне' and 'напоминает' in message.text.lower():
            temp = qreader('skupshik','napom')
            bot.send_message(message.chat.id, temp)

     else:
            bot.send_message(message.chat.id,'Квест не найден')


def eger_quest(message):
     if 'мутное' and 'дело' in message.text.lower():
            temp = qreader('eger','delo')
            bot.send_message(message.chat.id, temp)

     elif 'Знакомство' in message.text.lower():
            temp = qreader('eger','znak')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'выживальщика' and 'беззащитен' and 'опасен' in message.text.lower():
            temp = qreader('eger','put')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'выживальщика' and 'запасливый' in message.text.lower():
            temp = qreader('eger','zapas')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'выживальщика' and 'живчик' in message.text.lower():
            temp = qreader('eger','jivchik')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'выживальщика' and 'раненый' and 'зверь' in message.text.lower():
            temp = qreader('eger','zver')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'выживальщика' and 'хладнокровный' in message.text.lower():
            temp = qreader('eger','hladkrov')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'выживальщика' and 'охранка' in message.text.lower():
            temp = qreader('eger','ohrana')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'выживальщика' and 'крепыш' in message.text.lower():
            temp = qreader('eger','krepysh')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'выживальщика' and 'филин' in message.text.lower():
            temp = qreader('eger','krepysh')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'выживальщика' and 'боевой' and 'медик' in message.text.lower():
            temp = qreader('eger','med')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'выживальщика' and 'торчок' in message.text.lower():
            temp = qreader('eger','torchok')
            bot.send_message(message.chat.id, temp)

     elif 'скорая' and 'помощь' in message.text.lower():
            temp = qreader('eger','help')
            bot.send_message(message.chat.id, temp)

     elif 'резерв' in message.text.lower():
            temp = qreader('eger','rezerv')
            bot.send_message(message.chat.id, temp)

     elif 'визит' and 'вежливости' in message.text.lower():
            temp = qreader('eger','vizit')
            bot.send_message(message.chat.id, temp)

     elif 'ностальгия' in message.text.lower():
            temp = qreader('eger','nostalgy')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'трофей' in message.text.lower():
            temp = qreader('eger','trofey')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'очистка' and 'леса' in message.text.lower():
            temp = qreader('eger','clear')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'справедливость' in message.text.lower():
            temp = qreader('eger','sprav')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'переучет' in message.text.lower():
            temp = qreader('eger','pereuchet')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'контроллер' in message.text.lower():
            temp = qreader('eger','control')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'злой' and 'выхтер' in message.text.lower():
            temp = qreader('eger','zloy')
            bot.send_message(message.chat.id, temp)

     elif 'рыбное' and 'место' in message.text.lower():
            temp = qreader('eger','fish')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'санитар' and 'леса' in message.text.lower():
            temp = qreader('eger','sanitar')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'начальник' and 'завода' in message.text.lower():
            temp = qreader('eger','zavod')
            bot.send_message(message.chat.id, temp)

     elif 'охоту' in message.text.lower():
            temp = qreader('eger','hunt')
            bot.send_message(message.chat.id, temp)

     elif 'борьба' and 'вредителями' in message.text.lower():
            temp = qreader('eger','vred')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'стиратель' in message.text.lower():
            temp = qreader('eger','stirat')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'стиратель 2' in message.text.lower():
            temp = qreader('eger','stir2')
            bot.send_message(message.chat.id, temp)

     elif 'охотник' in message.text.lower():
            temp = qreader('eger','stir2')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'непреклонный' in message.text.lower():
            temp = qreader('eger','nepreklon')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'садист' in message.text.lower():
            temp = qreader('eger','sadist')
            bot.send_message(message.chat.id, temp)

     elif 'ловкач' in message.text.lower():
            temp = qreader('eger','lovkach')
            bot.send_message(message.chat.id, temp)

     elif 'тарковский' and 'стрелок' and 'часть 1' in message.text.lower():
            temp = qreader('eger','tar1')
            bot.send_message(message.chat.id, temp)

     elif 'тарковский' and 'стрелок' and 'часть 2' in message.text.lower():
            temp = qreader('eger','tar2')
            bot.send_message(message.chat.id, temp)

     elif 'тарковский' and 'стрелок' and 'часть 3' in message.text.lower():
            temp = qreader('eger','tar3')
            bot.send_message(message.chat.id, temp)

     elif 'тарковский' and 'стрелок' and 'часть 4' in message.text.lower():
            temp = qreader('eger','tar4')
            bot.send_message(message.chat.id, temp)

     elif 'тарковский' and 'стрелок' and 'часть 5' in message.text.lower():
            temp = qreader('eger','tar5')
            bot.send_message(message.chat.id, temp)

     elif 'тарковский' and 'стрелок' and 'часть 6' in message.text.lower():
            temp = qreader('eger','tar6')
            bot.send_message(message.chat.id, temp)

     elif 'тарковский' and 'стрелок' and 'часть 7' in message.text.lower():
            temp = qreader('eger','tar7')
            bot.send_message(message.chat.id, temp)

     elif 'тарковский' and 'стрелок' and 'часть 8' in message.text.lower():
            temp = qreader('eger','tar8')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'отступники' in message.text.lower():
            temp = qreader('eger','otstup')
            bot.send_message(message.chat.id, temp)

     elif 'отшельник' in message.text.lower():
            temp = qreader('eger','otshelnik')
            bot.send_message(message.chat.id, temp)

     elif 'залетные' in message.text.lower():
            temp = qreader('eger','zalet')
            bot.send_message(message.chat.id, temp)

     elif 'продразведка' in message.text.lower():
            temp = qreader('eger','prodrazved')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'администратор' in message.text.lower():
            temp = qreader('eger','admin')
            bot.send_message(message.chat.id, temp)

     elif 'прекратить' and 'огонь' in message.text.lower():
            temp = qreader('eger','stop')
            bot.send_message(message.chat.id, temp)

     elif 'стрим' and 'часть 3' in message.text.lower():
            temp = qreader('eger','strim3')
            bot.send_message(message.chat.id, temp)

     elif 'стрим' and 'часть 4' in message.text.lower():
            temp = qreader('eger','strim4')
            bot.send_message(message.chat.id, temp)

     elif 'стрим' and 'часть 5' in message.text.lower():
            temp = qreader('eger','strim5')
            bot.send_message(message.chat.id, temp)

     elif 'потрошитель' in message.text.lower():
            temp = qreader('eger','potroshitel')
            bot.send_message(message.chat.id, temp)

     elif 'путь' and 'охотника' and 'крупная' and 'дичь' in message.text.lower():
            temp = qreader('eger','dich')
            bot.send_message(message.chat.id, temp)
     
     elif 'путь' and 'охотника' and 'оборотень' and 'погонах' in message.text.lower():
            temp = qreader('eger','dich')
            bot.send_message(message.chat.id, temp)

     elif 'водохлеб' and 'ищейки' in message.text.lower():
            temp = qreader('eger','isheiki')
            bot.send_message(message.chat.id, temp)

     elif 'клаустрофобия' in message.text.lower():
            temp = qreader('eger','phobia')
            bot.send_message(message.chat.id, temp)

     elif 'тарков' and 'прощает' and 'ошибок' in message.text.lower():
            temp = qreader('eger','fail')
            bot.send_message(message.chat.id, temp)

     elif 'план' and 'перехват' in message.text.lower():
            temp = qreader('eger','plan')
            bot.send_message(message.chat.id, temp)

     elif 'каждый' and 'охотник' and 'знает' and 'где' and 'сидит' and 'фазан' in message.text.lower():
            temp = qreader('eger','fazan')
            bot.send_message(message.chat.id, temp)

     elif 'долг' and 'лесника' in message.text.lower():
            temp = qreader('eger','lesnik')
            bot.send_message(message.chat.id, temp)

     elif 'умный' and 'гору' and 'пойдет' in message.text.lower():
            temp = qreader('eger','gora')
            bot.send_message(message.chat.id, temp)

     elif 'инициация' in message.text.lower():
            temp = qreader('eger','iniciaciya')
            bot.send_message(message.chat.id, temp)

     elif 'закалка' in message.text.lower():
            temp = qreader('eger','zakalka')
            bot.send_message(message.chat.id, temp)

     elif 'незаконная' and 'рубка' in message.text.lower():
            temp = qreader('eger','rubka')
            bot.send_message(message.chat.id, temp)

     else:
            bot.send_message(message.chat.id,'Квест не найден')

def eger_quest(message):
     if 'снабженец' in message.text.lower():
            temp = qreader('Lyjnik','snab')
            bot.send_message(message.chat.id, temp)

     elif 'вымогатель' in message.text.lower():
            temp = qreader('Lyjnik','vymog')
            bot.send_message(message.chat.id, temp)

     elif 'движуха' in message.text.lower():
            temp = qreader('Lyjnik','dvij')
            bot.send_message(message.chat.id, temp)

     elif 'что' and 'на' and 'флешке' in message.text.lower():
            temp = qreader('Lyjnik','flash')
            bot.send_message(message.chat.id, temp)

     elif 'золотые' and 'понты' in message.text.lower():
            temp = qreader('Lyjnik','gold')
            bot.send_message(message.chat.id, temp)

     elif 'своего' and 'рода' and 'саботаж' in message.text.lower():
            temp = qreader('Lyjnik','sabotajh')
            bot.send_message(message.chat.id, temp)

     elif 'друг' and 'запада' and 'часть 1' in message.text.lower():
            temp = qreader('Lyjnik','zapad1')
            bot.send_message(message.chat.id, temp)

     elif 'друг' and 'запада' and 'часть 2' in message.text.lower():
            temp = qreader('Lyjnik','zapad2')
            bot.send_message(message.chat.id, temp)

     elif 'реагент' and 'часть 1' in message.text.lower():
            temp = qreader('Lyjnik','reagent1')
            bot.send_message(message.chat.id, temp)

     elif 'реагент' and 'часть 2' in message.text.lower():
            temp = qreader('Lyjnik','reagent2')
            bot.send_message(message.chat.id, temp)

     elif 'реагент' and 'часть 3' in message.text.lower():
            temp = qreader('Lyjnik','reagent3')
            bot.send_message(message.chat.id, temp)

     elif 'реагент' and 'часть 4' in message.text.lower():
            temp = qreader('Lyjnik','reagent4')
            bot.send_message(message.chat.id, temp)

     elif 'осведомлен' and 'значит' and 'вооружен' in message.text.lower():
            temp = qreader('Lyjnik','osved')
            bot.send_message(message.chat.id, temp)

     elif 'лендлиз' and 'часть 1' in message.text.lower():
            temp = qreader('Lyjnik','lendliz1')
            bot.send_message(message.chat.id, temp)

     elif 'прикормка' in message.text.lower():
            temp = qreader('Lyjnik','prikormka')
            bot.send_message(message.chat.id, temp)

     elif 'лендлиз' and 'часть 1' in message.text.lower():
            temp = qreader('Lyjnik','lendliz1')
            bot.send_message(message.chat.id, temp)

     elif 'игра' and 'верняк' in message.text.lower():
            temp = qreader('Lyjnik','vernyak')
            bot.send_message(message.chat.id, temp)

     elif 'витамины' and 'часть 1' in message.text.lower():
            temp = qreader('Lyjnik','vitaminy1')
            bot.send_message(message.chat.id, temp)

     elif 'витамины' and 'часть 2' in message.text.lower():
            temp = qreader('Lyjnik','vitaminy2')
            bot.send_message(message.chat.id, temp)

     elif 'безопасный' and 'коридор' in message.text.lower():
            temp = qreader('Lyjnik','koridor')
            bot.send_message(message.chat.id, temp)

     elif 'выкуп' and 'доверия' in message.text.lower():
            temp = qreader('Lyjnik','doverie')
            bot.send_message(message.chat.id, temp)

     elif 'деза' in message.text.lower():
            temp = qreader('Lyjnik','deza')
            bot.send_message(message.chat.id, temp)

     elif 'тихий' and 'калибр' in message.text.lower():
            temp = qreader('Lyjnik','tixiy')
            bot.send_message(message.chat.id, temp)

     elif 'кремень' in message.text.lower():
            temp = qreader('Lyjnik','kremen')
            bot.send_message(message.chat.id, temp)

     elif 'подстава' in message.text.lower():
            temp = qreader('Lyjnik','podstava')
            bot.send_message(message.chat.id, temp)

     elif 'ночная' and 'прогулка' in message.text.lower():
            temp = qreader('Lyjnik','noch')
            bot.send_message(message.chat.id, temp)

     elif 'долгая' and 'дорога' in message.text.lower():
            temp = qreader('Lyjnik','doroga')
            bot.send_message(message.chat.id, temp)

     elif 'пропавший' and 'груз' in message.text.lower():
            temp = qreader('Lyjnik','gruz')
            bot.send_message(message.chat.id, temp)

     elif 'совершенно' and 'секретно' in message.text.lower():
            temp = qreader('Lyjnik','secret')
            bot.send_message(message.chat.id, temp)

     elif 'должник' in message.text.lower():
            temp = qreader('Lyjnik','dolg')
            bot.send_message(message.chat.id, temp)

     elif 'домашний' and 'арест' and 'часть 1' in message.text.lower():
            temp = qreader('Lyjnik','arest1')
            bot.send_message(message.chat.id, temp)

     elif 'домашний' and 'арест' and 'часть 2' in message.text.lower():
            temp = qreader('Lyjnik','arest2')
            bot.send_message(message.chat.id, temp)

     elif 'секрет' and 'идеального' and 'вкуса' and 'часть 1' in message.text.lower():
            temp = qreader('Lyjnik','vkus1')
            bot.send_message(message.chat.id, temp)

     elif 'секрет' and 'идеального' and 'вкуса' and 'часть 2' in message.text.lower():
            temp = qreader('Lyjnik','vkus2')
            bot.send_message(message.chat.id, temp)

     elif 'коням' in message.text.lower():
            temp = qreader('Lyjnik','koni')
            bot.send_message(message.chat.id, temp)

     elif 'финансовая' and 'пирамида' in message.text.lower():
            temp = qreader('Lyjnik','piramida')
            bot.send_message(message.chat.id, temp)

     elif 'чужое' and 'добро' in message.text.lower():
            temp = qreader('Lyjnik','dobro')
            bot.send_message(message.chat.id, temp)
     else:
            bot.send_message(message.chat.id,'Квест не найден')

     

def smotritel_quest(message):
     if 'открытие' and 'смотритель' and 'маяка' in message.text.lower():
            temp = qreader('smotritel','smotritel')
            bot.send_message(message.chat.id, temp)

     elif 'источник' and 'информации' in message.text.lower():
            temp = qreader('smotritel','info')
            bot.send_message(message.chat.id, temp)

     elif 'пропавший' and 'информатор' in message.text.lower():
            temp = qreader('smotritel','lost')
            bot.send_message(message.chat.id, temp)

     elif 'контр' and 'компромат' in message.text.lower():
            temp = qreader('smotritel','kompromat')
            bot.send_message(message.chat.id, temp)

     elif 'ответная' and 'услуга' in message.text.lower():
            temp = qreader('smotritel','usluga')
            bot.send_message(message.chat.id, temp)

     elif 'расплата' in message.text.lower():
            temp = qreader('smotritel','rasplata')
            bot.send_message(message.chat.id, temp)

     elif 'провокация' in message.text.lower():
            temp = qreader('smotritel','provokacia')
            bot.send_message(message.chat.id, temp)

     elif 'след' and 'хлебных' and 'крошек' in message.text.lower():
            temp = qreader('smotritel','sled')
            bot.send_message(message.chat.id, temp)

     elif 'наводчик' in message.text.lower():
            temp = qreader('smotritel','navod')
            bot.send_message(message.chat.id, temp)

     elif 'произвести' and 'впечатление' in message.text.lower():
            temp = qreader('smotritel','vpech')
            bot.send_message(message.chat.id, temp)

     elif 'городские' and 'разборки' in message.text.lower():
            temp = qreader('smotritel','razbor')
            bot.send_message(message.chat.id, temp)

     else:
            bot.send_message(message.chat.id,'Квест не найден')


def miratvorec_quest(message):
       if 'бессонница' in message.text.lower():
            temp = qreader('miratvorec','besson')
            bot.send_message(message.chat.id, temp)

       elif 'рыболовные' and 'снасти' in message.text.lower():
            temp = qreader('miratvorec','fish')
            bot.send_message(message.chat.id, temp)

       elif 'сафари' and 'тигра' in message.text.lower():
            temp = qreader('miratvorec','safari')
            bot.send_message(message.chat.id, temp)

       elif 'сафари' and 'тигра' in message.text.lower():
            temp = qreader('miratvorec','safari')
            bot.send_message(message.chat.id, temp)

       elif 'металлолом' in message.text.lower():
            temp = qreader('miratvorec','metall')
            bot.send_message(message.chat.id, temp)

       elif 'глаз' and 'орла' in message.text.lower():
            temp = qreader('miratvorec','glaz')
            bot.send_message(message.chat.id, temp)

       elif 'ревизия' and 'резерв' in message.text.lower():
            temp = qreader('miratvorec','rezerv')
            bot.send_message(message.chat.id, temp)

       elif 'гумманитарка' in message.text.lower():
            temp = qreader('miratvorec','gumm')
            bot.send_message(message.chat.id, temp)

       elif 'секретные' and 'разборки' in message.text.lower():
            temp = qreader('miratvorec','secret')
            bot.send_message(message.chat.id, temp)

       elif 'путевка' and 'санаторий' and 'часть 1' in message.text.lower():
            temp = qreader('miratvorec','sanatoriy1')
            bot.send_message(message.chat.id, temp)

       elif 'путевка' and 'санаторий' and 'часть 2' in message.text.lower():
            temp = qreader('miratvorec','sanatoriy2')
            bot.send_message(message.chat.id, temp)

       elif 'путевка' and 'санаторий' and 'часть 3' in message.text.lower():
            temp = qreader('miratvorec','sanatoriy3')
            bot.send_message(message.chat.id, temp)

       elif 'путевка' and 'санаторий' and 'часть 4' in message.text.lower():
            temp = qreader('miratvorec','sanatoriy4')
            bot.send_message(message.chat.id, temp)

       elif 'путевка' and 'санаторий' and 'часть 5' in message.text.lower():
            temp = qreader('miratvorec','sanatoriy5')
            bot.send_message(message.chat.id, temp)

       elif 'путевка' and 'санаторий' and 'часть 6' in message.text.lower():
            temp = qreader('miratvorec','sanatoriy6')
            bot.send_message(message.chat.id, temp)

       elif 'путевка' and 'санаторий' and 'часть 7' in message.text.lower():
            temp = qreader('miratvorec','sanatoriy7')
            bot.send_message(message.chat.id, temp)

       elif 'секта' and 'часть 1' in message.text.lower():
            temp = qreader('miratvorec','secta1')
            bot.send_message(message.chat.id, temp)

       elif 'секта' and 'часть 2' in message.text.lower():
            temp = qreader('miratvorec','secta2')
            bot.send_message(message.chat.id, temp)

       elif 'образцы' in message.text.lower():
            temp = qreader('miratvorec','obraz')
            bot.send_message(message.chat.id, temp)

       elif 'сотрудник' and 'terragroup' in message.text.lower():
            temp = qreader('miratvorec','sotr')
            bot.send_message(message.chat.id, temp)

       elif 'лендлиз' and 'часть 2' in message.text.lower():
            temp = qreader('miratvorec','lendliz2')
            bot.send_message(message.chat.id, temp)

       elif 'миратворческая' and 'миссия' in message.text.lower():
            temp = qreader('miratvorec','miratvor')
            bot.send_message(message.chat.id, temp)

       elif 'груз' and 'х' and 'часть 1' in message.text.lower():
            temp = qreader('miratvorec','gruz1')
            bot.send_message(message.chat.id, temp)

       elif 'груз' and 'х' and 'часть 2' in message.text.lower():
            temp = qreader('miratvorec','gruz2')
            bot.send_message(message.chat.id, temp)

       elif 'груз' and 'х' and 'часть 3' in message.text.lower():
            temp = qreader('miratvorec','gruz3')
            bot.send_message(message.chat.id, temp)

       elif 'груз' and 'х' and 'часть 4' in message.text.lower():
            temp = qreader('miratvorec','gruz4')
            bot.send_message(message.chat.id, temp)

       elif 'мокрое' and 'дело' and 'часть 1' in message.text.lower():
            temp = qreader('miratvorec','delo1')
            bot.send_message(message.chat.id, temp)

       elif 'мокрое' and 'дело' and 'часть 2' in message.text.lower():
            temp = qreader('miratvorec','delo2')
            bot.send_message(message.chat.id, temp)

       elif 'мокрое' and 'дело' and 'часть 3' in message.text.lower():
            temp = qreader('miratvorec','delo3')
            bot.send_message(message.chat.id, temp)

       elif 'мокрое' and 'дело' and 'часть 4' in message.text.lower():
            temp = qreader('miratvorec','delo4')
            bot.send_message(message.chat.id, temp)

       elif 'мокрое' and 'дело' and 'часть 5' in message.text.lower():
            temp = qreader('miratvorec','delo6')
            bot.send_message(message.chat.id, temp)

       elif 'мокрое' and 'дело' and 'часть 6' in message.text.lower():
            temp = qreader('miratvorec','delo6')
            bot.send_message(message.chat.id, temp)

       elif 'наставник' in message.text.lower():
            temp = qreader('miratvorec','nastav')
            bot.send_message(message.chat.id, temp)

       elif 'проводник' in message.text.lower():
            temp = qreader('miratvorec','provod')
            bot.send_message(message.chat.id, temp)

       elif 'чистильщик' in message.text.lower():
            temp = qreader('miratvorec','chist')
            bot.send_message(message.chat.id, temp)

       elif 'ревизия' and 'маяк' in message.text.lower():
            temp = qreader('miratvorec','mayak')
            bot.send_message(message.chat.id, temp)

       elif 'перенаселение' in message.text.lower():
            temp = qreader('miratvorec','perenasel')
            bot.send_message(message.chat.id, temp)

       elif 'трофеи' in message.text.lower():
            temp = qreader('miratvorec','trofei')
            bot.send_message(message.chat.id, temp)

       elif 'заказ' in message.text.lower():
            temp = qreader('miratvorec','zakaz')
            bot.send_message(message.chat.id, temp)
            
       elif 'противостояние' in message.text.lower():
            temp = qreader('miratvorec','protivostoyanie')
            bot.send_message(message.chat.id, temp)

       elif 'ревизия' and 'улицы' and 'таркова' in message.text.lower():
            temp = qreader('miratvorec','delo6')
            bot.send_message(message.chat.id, temp)

       elif 'техосмотр' in message.text.lower():
            temp = qreader('miratvorec','to')
            bot.send_message(message.chat.id, temp)

       elif 'худшая' and 'работа' and 'свете' in message.text.lower():
            temp = qreader('miratvorec','bad')
            bot.send_message(message.chat.id, temp)

       elif 'проезд' and 'закрыт' in message.text.lower():
            temp = qreader('miratvorec','close')
            bot.send_message(message.chat.id, temp)

       elif 'подчистить' and 'хвосты' in message.text.lower():
            temp = qreader('miratvorec','hvost')
            bot.send_message(message.chat.id, temp)

       elif 'новые' and 'маршруты' in message.text.lower():
            temp = qreader('miratvorec','new')
            bot.send_message(message.chat.id, temp)
       
       else:
            bot.send_message(message.chat.id,'Квест не найден')


def mechanik_quest(message):
       if 'кабинет' and 'химии' in message.text.lower():
            temp = qreader('mechanik','ximiya')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 1' in message.text.lower():
            temp = qreader('mechanik','gun1')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 2' in message.text.lower():
            temp = qreader('mechanik','gun2')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 3' in message.text.lower():
            temp = qreader('mechanik','gun3')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 4' in message.text.lower():
            temp = qreader('mechanik','gun4')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 5' in message.text.lower():
            temp = qreader('mechanik','gun5')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 6' in message.text.lower():
            temp = qreader('mechanik','gun6')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 7' in message.text.lower():
            temp = qreader('mechanik','gun7')
            bot.send_message(message.chat.id, temp)
            
       elif 'оружейник' and 'часть 8' in message.text.lower():
            temp = qreader('mechanik','gun8')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 9' in message.text.lower():
            temp = qreader('mechanik','gun9')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 10' in message.text.lower():
            temp = qreader('mechanik','gun10')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 12' in message.text.lower():
            temp = qreader('mechanik','gun12')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 13' in message.text.lower():
            temp = qreader('mechanik','gun13')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 14' in message.text.lower():
            temp = qreader('mechanik','gun14')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 15' in message.text.lower():
            temp = qreader('mechanik','gun15')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 16' in message.text.lower():
            temp = qreader('mechanik','gun16')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 17' in message.text.lower():
            temp = qreader('mechanik','gun17')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 18' in message.text.lower():
            temp = qreader('mechanik','gun18')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 19' in message.text.lower():
            temp = qreader('mechanik','gun19')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 20' in message.text.lower():
            temp = qreader('mechanik','gun20')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 21' in message.text.lower():
            temp = qreader('mechanik','gun21')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 22' in message.text.lower():
            temp = qreader('mechanik','gun22')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 23' in message.text.lower():
            temp = qreader('mechanik','gun23')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 24' in message.text.lower():
            temp = qreader('mechanik','gun24')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'часть 25' in message.text.lower():
            temp = qreader('mechanik','gun25')
            bot.send_message(message.chat.id, temp)

       elif 'поручение' in message.text.lower():
            temp = qreader('mechanik','poruch')
            bot.send_message(message.chat.id, temp)

       elif 'садоводство' and 'часть 1' in message.text.lower():
            temp = qreader('mechanik','sad1')
            bot.send_message(message.chat.id, temp)

       elif 'садоводство' and 'часть 2' in message.text.lower():
            temp = qreader('mechanik','sad2')
            bot.send_message(message.chat.id, temp)
       
       elif 'садоводство' and 'часть 3' in message.text.lower():
            temp = qreader('mechanik','sad3')
            bot.send_message(message.chat.id, temp)

       elif 'садоводство' and 'часть 4' in message.text.lower():
            temp = qreader('mechanik','sad4')
            bot.send_message(message.chat.id, temp)
       
       elif 'сигнал' and 'часть 1' in message.text.lower():
            temp = qreader('mechanik','signal1')
            bot.send_message(message.chat.id, temp)

       elif 'сигнал' and 'часть 2' in message.text.lower():
            temp = qreader('mechanik','signal2')
            bot.send_message(message.chat.id, temp)

       elif 'сигнал' and 'часть 3' in message.text.lower():
            temp = qreader('mechanik','signal3')
            bot.send_message(message.chat.id, temp)

       elif 'сигнал' and 'часть 4' in message.text.lower():
            temp = qreader('mechanik','signal4')
            bot.send_message(message.chat.id, temp)

       elif 'свой' and 'человек' in message.text.lower():
            temp = qreader('mechanik','svoy')
            bot.send_message(message.chat.id, temp)

       elif 'стрелок' and 'бога' in message.text.lower():
            temp = qreader('mechanik','strelok')
            bot.send_message(message.chat.id, temp)

       elif 'скаут' in message.text.lower():
            temp = qreader('mechanik','sout')
            bot.send_message(message.chat.id, temp)
       
       elif 'военный' and 'хабар' in message.text.lower():
            temp = qreader('mechanik','habar')
            bot.send_message(message.chat.id, temp)

       elif 'черный' and 'выход' in message.text.lower():
            temp = qreader('mechanik','exit')
            bot.send_message(message.chat.id, temp)

       elif 'удобрения' in message.text.lower():
            temp = qreader('mechanik','udobreniya')
            bot.send_message(message.chat.id, temp)

       elif 'импорт' in message.text.lower():
            temp = qreader('mechanik','import')
            bot.send_message(message.chat.id, temp)

       elif 'пристрелка' in message.text.lower():
            temp = qreader('mechanik','pristrelka')
            bot.send_message(message.chat.id, temp)

       elif 'курьер' in message.text.lower():
            temp = qreader('mechanik','kura')
            bot.send_message(message.chat.id, temp)

       elif 'снайпер' and 'психопат' in message.text.lower():
            temp = qreader('mechanik','sniper')
            bot.send_message(message.chat.id, temp)

       elif 'тайны' and 'корпоратов' in message.text.lower():
            temp = qreader('mechanik','tainy')
            bot.send_message(message.chat.id, temp)

       elif 'энергетический' and 'кризис' in message.text.lower():
            temp = qreader('mechanik','krizis')
            bot.send_message(message.chat.id, temp)

       elif 'вредная' and 'привычка' in message.text.lower():
            temp = qreader('mechanik','vred')
            bot.send_message(message.chat.id, temp)

       elif 'стрим' and 'часть 1' in message.text.lower():
            temp = qreader('mechanik','strim1')
            bot.send_message(message.chat.id, temp)

       elif 'стрим' and 'часть 2' in message.text.lower():
            temp = qreader('mechanik','strim2')
            bot.send_message(message.chat.id, temp)

       elif 'наблюдение' in message.text.lower():
            temp = qreader('mechanik','nablud')
            bot.send_message(message.chat.id, temp)

       elif 'слежка' in message.text.lower():
            temp = qreader('mechanik','slejka')
            bot.send_message(message.chat.id, temp)

       elif 'сетевой' and 'провайдер' and 'часть 1' in message.text.lower():
            temp = qreader('mechanik','web1')
            bot.send_message(message.chat.id, temp)

       elif 'сетевой' and 'провайдер' and 'часть 2' in message.text.lower():
            temp = qreader('mechanik','web2')
            bot.send_message(message.chat.id, temp)

       elif 'проверка' and 'часть 1' in message.text.lower():
            temp = qreader('mechanik','proverka1')
            bot.send_message(message.chat.id, temp)

       elif 'проверка' and 'часть 2' in message.text.lower():
            temp = qreader('mechanik','proverka2')
            bot.send_message(message.chat.id, temp)

       elif 'проверка' and 'часть 3' in message.text.lower():
            temp = qreader('mechanik','proverka3')
            bot.send_message(message.chat.id, temp)

       elif 'ключ' and 'башни' in message.text.lower():
            temp = qreader('mechanik','key')
            bot.send_message(message.chat.id, temp)

       elif 'новое' and 'знакомство' in message.text.lower():
            temp = qreader('mechanik','znak')
            bot.send_message(message.chat.id, temp)

       elif 'дверь' in message.text.lower():
            temp = qreader('mechanik','door')
            bot.send_message(message.chat.id, temp)
            
       elif 'спасение' and 'крота' in message.text.lower():
            temp = qreader('mechanik','help')
            bot.send_message(message.chat.id, temp)
            
       elif 'устойчивый' and 'сигнал' in message.text.lower():
            temp = qreader('mechanik','ustoi')
            bot.send_message(message.chat.id, temp)

       elif 'секрет' and 'успеваемости' and 'часть 1' in message.text.lower():
            temp = qreader('mechanik','secret1')
            bot.send_message(message.chat.id, temp)

       elif 'секрет' and 'успеваемости' and 'часть 2' in message.text.lower():
            temp = qreader('mechanik','secret2')
            bot.send_message(message.chat.id, temp)

       elif 'авиапочта' in message.text.lower():
            temp = qreader('mechanik','pochta')
            bot.send_message(message.chat.id, temp)

       elif 'камера' and 'мотор' in message.text.lower():
            temp = qreader('mechanik','pochta')
            bot.send_message(message.chat.id, temp)

       elif 'черный' and 'лебедь' in message.text.lower():
            temp = qreader('mechanik','black')
            bot.send_message(message.chat.id, temp)

       elif 'секреты' and 'заводских' and 'стен' in message.text.lower():
            temp = qreader('mechanik','zavod')
            bot.send_message(message.chat.id, temp)

       elif 'конструктор' and 'любитель' in message.text.lower():
            temp = qreader('mechanik','proverka')
            bot.send_message(message.chat.id, temp)

       elif 'страсть' and 'эргономике' in message.text.lower():
            temp = qreader('mechanik','strast')
            bot.send_message(message.chat.id, temp)

       elif 'оружейник' and 'старой' and 'дружбы' in message.text.lower():
            temp = qreader('mechanik','oruj')
            bot.send_message(message.chat.id, temp)

       else:
            bot.send_message(message.chat.id,'Квест не найден')

       

       

       

     

     

     

     

     

     

     

     

     

     
     

            

     


    

    


    

    
    
            


             
             
             
            
             




     









    #  temp2 = qreader('bosses','glukhar')
    #  bot.send_message(message.chat.id, temp2)



            




bot.polling(none_stop=True)


