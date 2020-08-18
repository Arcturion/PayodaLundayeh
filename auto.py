import telepot
import time
import urllib3

from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

bot = telepot.Bot('1355362257:AAElq_EJOygVq4TlGC6d5pHVrhob768G4Ds')

radar = '/root/data/sepuluh/current/citra_radar.png'

call_data = {
  "WRF Rain 6": "/root/data/harian/wrf/6.png",
  "WRF Rain 12": "/root/data/harian/wrf/12.png",
  "WRF Rain 18": "/root/data/harian/wrf/18.png",
  "WRF Rain 24": "/root/data/harian/wrf/24.png",
  "WRF Rain 30": "/root/data/harian/wrf/30.png",
  "WRF Rain 36": "/root/data/harian/wrf/36.png",
  "WRF Rain 42": "/root/data/harian/wrf/42.png",
  "WRF Rain 48": "/root/data/harian/wrf/48.png",
  "WRF Rain 54": "/root/data/harian/wrf/54.png",
  "WRF Rain 60": "/root/data/harian/wrf/60.png",
  "WRF Rain 66": "/root/data/harian/wrf/66.png",
  "WRF Rain 72": "/root/data/harian/wrf/72.png",
  "WRF Rain 78": "/root/data/harian/wrf/72.png",
  "WRF Rain 84": "/root/data/harian/wrf/72.png",
  "WRF Rain 90": "/root/data/harian/wrf/72.png",
  "WRF Rain 96": "/root/data/harian/wrf/72.png",
  "WRF Rain 102": "/root/data/harian/wrf/72.png",
  "WRF Rain 108": "/root/data/harian/wrf/72.png",
  "WRF Rain 114": "/root/data/harian/wrf/72.png",
  "WRF Rain 120": "/root/data/harian/wrf/72.png",
  "IFS RAIN 6": "/root/data/harian/ifs/6.png",
  "IFS RAIN 12": "/root/data/harian/ifs/12.png",
  "IFS RAIN 18": "/root/data/harian/ifs/18.png",
  "IFS RAIN 24": "/root/data/harian/ifs/24.png",
  "IFS RAIN 30": "/root/data/harian/ifs/30.png",
  "IFS RAIN 36": "/root/data/harian/ifs/36.png",
  "IFS RAIN 42": "/root/data/harian/ifs/42.png",
  "IFS RAIN 48": "/root/data/harian/ifs/48.png",
  "IFS RAIN 54": "/root/data/harian/ifs/54.png",
  "KMA Rain 6": "/root/data/harian/kma/6.png",
  "KMA Rain 12": "/root/data/harian/kma/12.png",
  "KMA Rain 18": "/root/data/harian/kma/18.png",
  "KMA Rain 24": "/root/data/harian/kma/24.png",
  "KMA Rain 30": "/root/data/harian/kma/30.png",
  "KMA Rain 36": "/root/data/harian/kma/36.png",
  "KMA Rain 42": "/root/data/harian/kma/42.png",
  "KMA Rain 48": "/root/data/harian/kma/48.png",
  "KMA Rain 54": "/root/data/harian/kma/54.png",
  "Satelit EH": "/root/data/sepuluh/current/sat_EH.png",
  "Satelit RP": "/root/data/sepuluh/current/sat_RP.png",
  "Radar": "/root/data/sepuluh/current/citra_radar.png",
}

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if msg["text"] == "Menu Utama":
            markup = ReplyKeyboardMarkup(keyboard=[
                     ['Satelit'],
                     ['Radar'],
                     ['Model'],
                 ])
            bot.sendMessage(chat_id, 'Misi kaakk!! mau cari apa kak ??', reply_markup=markup)

        elif msg["text"] == "Satelit":
            markup = ReplyKeyboardMarkup(keyboard=[
                     ['Satelit EH'],
                     ['Satelit RP'],
                     ['Menu Utama'],
                 ])
            bot.sendMessage(chat_id, 'Misi kaakk!! mau data satelit apa kak ??', reply_markup=markup)

        elif msg["text"] == "Model":
            markup = ReplyKeyboardMarkup(keyboard=[
                     ['WRF'],
                     ['IFS'],
                     ['KMA'],
                     ['Menu Utama'],
                 ])
            bot.sendMessage(chat_id, 'Misi kaakk!! mau output model apa kak ??', reply_markup=markup)

        elif msg["text"] == "KMA":
            markup = ReplyKeyboardMarkup(keyboard=[
                     ['KMA Rain 6', 'KMA Rain 12', 'KMA Rain 18'],
                     ['KMA Rain 24', 'KMA Rain 30', 'KMA Rain 36'],
                     ['KMA Rain 42', 'KMA Rain 48', 'KMA Rain 54'],
                     ['Menu Utama'],
                 ])
            bot.sendMessage(chat_id, 'MMisi kaakk!! mau output jam berapa ??', reply_markup=markup)

        elif msg["text"] == "WRF":
            markup = ReplyKeyboardMarkup(keyboard=[
                     ['WRF Rain 6', 'WRF Rain 12', 'WRF Rain 18'],
                     ['WRF Rain 24', 'WRF Rain 30', 'WRF Rain 36'],
                     ['WRF Rain 42', 'WRF Rain 48', 'WRF Rain 54'],
                     ['WRF Rain 60', 'WRF Rain 66', 'WRF Rain 72'],
                     ['WRF Rain 78', 'WRF Rain 84', 'WRF Rain 90'],
                     ['WRF Rain 96', 'WRF Rain 102', 'WRF Rain 108'],
                     ['WRF Rain 114', 'WRF Rain 120'],
                     ['Menu Utama'],
                 ])
            bot.sendMessage(chat_id, 'Misi kaakk!! mau output jam berapa ??', reply_markup=markup)

        elif msg["text"] == "IFS":
            markup = ReplyKeyboardMarkup(keyboard=[
                     ['IFS RAIN 6', 'IFS RAIN 12', 'IFS RAIN 18'],
                     ['IFS RAIN 24', 'IFS RAIN 30', 'IFS RAIN 36'],
                     ['IFS RAIN 42', 'IFS RAIN 48', 'IFS RAIN 54'],
                     ['IFS RAIN 60', 'IFS RAIN 66', 'IFS RAIN 72'],
                     ['IFS RAIN 78', 'IFS RAIN 84', 'IFS RAIN 90'],
                     ['IFS RAIN 96', 'IFS RAIN 102', 'IFS RAIN 108'],
                     ['IFS RAIN 114', 'IFS RAIN 120'],
                     ['Menu Utama'],
                 ])
            bot.sendMessage(chat_id, 'Misi kaakk!! mau output jam berapa ??', reply_markup=markup)

        elif msg["text"] in call_data:
            greetings = bot.sendMessage(chat_id, "Data {} Masih di Upload Bosss, tunggu yak".format(msg["text"]))
            msg_idf = telepot.message_identifier(greetings)
            bot.sendDocument(chat_id, open(call_data[msg['text']], 'rb'))
            bot.deleteMessage(msg_idf)


bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)