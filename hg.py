import telebot
import os
import random

# 🔹 ضع توكن البوت هنا
TOKEN = "6942172617:AAHaR4e0QAv8VaOYKlGeqUoEA3--6PMVsdg"

bot = telebot.TeleBot(TOKEN)

# 🔹 مجلد لحفظ الملفات
OUTPUT_FOLDER = "offsets"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# 🔹 قالب إيقاف الأوفست
OFFSET_TEMPLATE = """PATCH_LIB("libUE4.so", "0x{offset:X}", "00 00 00 00");"""

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 أهلاً بك! اضغط /generate لإنشاء تجاوز لليب UE4.")

@bot.message_handler(commands=['generate'])
def generate_offsets(message):
    num_offsets = 25  # عدد الأوفستات العشوائية
    offsets = {}

    for _ in range(num_offsets):
        offset = random.randint(0x1000000, 0xFFFFFFF)  # توليد أوفست عشوائي
        offsets[offset] = OFFSET_TEMPLATE.format(offset=offset)

    # 🔹 حفظ الأوفستات في ملف
    file_path = os.path.join(OUTPUT_FOLDER, "offsets.cpp")
    with open(file_path, "w") as f:
        for entry in offsets.values():
            f.write(entry + "\n")

    # 🔹 إرسال الملف للمستخدم
    with open(file_path, "rb") as f:
        bot.send_document(message.chat.id, f)

    bot.send_message(message.chat.id, "✅ تم إنشاء الحماية!")

# 🔹 تشغيل البوت
bot.polling()