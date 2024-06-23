import telebot
from telebot import types

# Ganti 'YOUR_TOKEN' dengan token bot Anda yang sebenarnya
TOKEN = '7486932063:AAF943JUL7WjXLvNB--YtILH5rieY3s3_DA'
bot = telebot.TeleBot(TOKEN)

# Menentukan handler perintah
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Selamat datang di Bot Sate Taichan Borneo! 🍢\n\n"
        "Kami senang Anda di sini! Silakan gunakan /perintah untuk melihat apa saja yang bisa Anda lakukan. "
        "Jika Anda butuh bantuan lebih lanjut, jangan ragu untuk menghubungi kami."
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['perintah'])
def send_help(message):
    help_text = (
        "Berikut adalah perintah yang tersedia:\n"
        "/start - Mulai bot\n"
        "/perintah - Tampilkan pesan bantuan ini\n"
        "/info - Informasi tentang bisnis kami\n"
        "/menu - Tampilkan menu\n"
        "/instagram - Dapatkan tautan ke akun Instagram kami\n"
        "/location - Temukan lokasi kami\n"
        "/hours - Dapatkan jam kerja kami\n"
        "/contact  - Hubungi kami\n"
        "/FAQ - Pertanyaan yang Sering Diajukan"
    )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['info'])
def send_info(message):
    info_text = (
        "Sate Taichan & Pisang Gapit Borneo adalah UMKM yang terletak di Jl. Semanggi Timur kav. 10. No. 20, Kota Malang."
        "Sejak tahun 2021, kami hadir dengan menu utama kami, sate taichan dan pisang gapit."
        "Kami tersedia di beberapa platform (Shopeefood dan Grabfood). Anda juga bisa pesan melalui WhatsApp kami, dan tinggal ambil pesanannya ke lokasi kami. Tunggu apa lagi? yuk, segera pesan untuk amankan sate taichanmu! 🤤😊"
    )
    bot.reply_to(message, info_text)

@bot.message_handler(commands=['menu'])
def send_menu(message):
    menu_text = "Berikut adalah menu kami. Harga di bawah adalah harga untuk pembelian secara online, ya. Tentunya, akan berbeda jika pesan melalui WhatsApp atau datang langsung.😊"
    bot.reply_to(message, menu_text)

    # Mengirim gambar menu
    with open('menu.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['instagram'])
def send_instagram(message):
    instagram_text = (
        "Halo, Kak. Ketuk tautan ini untuk bisa berkunjung ke akun Instagram kami, ya.😉"
    "(https://www.instagram.com/satetaichanborneo/?hl=en)"
    )
    bot.reply_to(message, instagram_text, parse_mode='Markdown')

@bot.message_handler(commands=['location'])
def send_location(message):
    location_text = (
        "Lokasi Kami:\nJalan Semanggi Timur Kav 10 No 20, Malang 65141\n\n"
        "Halo! Ketuk tautan berikut ini, dan dapatkan informasi lokasi kami!"
    )
    bot.reply_to(message, location_text)

    # Mengirim lokasi Google Maps
    google_maps_url = "https://maps.app.goo.gl/XDrw8BrwcEiNNFY26"
    bot.send_message(message.chat.id, google_maps_url)

@bot.message_handler(commands=['hours'])
def send_hours(message):
    hours_text = (
        "Kami buka jam 10.00 hingga 22.00, ya ^^ yuk, segera pesan sebelum kehabisan 🤤"
    )
    bot.reply_to(message, hours_text)

@bot.message_handler(commands=['contact'])
def send_contact(message):
    contact_text = (
        "Hubungi Kami:\n"
        "Whatsapp: wa.me/62881026780972\n"
        "Instagram: https://www.instagram.com/satetaichanborneo/?hl=en"
    )
    bot.reply_to(message, contact_text)

@bot.message_handler(commands=['FAQ'])
def send_faq(message):
    faq_text = (
        "Pertanyaan yang Sering Diajukan:\n"
        "Q: Apa itu Sate Taichan?\n"
        "A: Sate Taichan adalah jenis sate ayam yang dipanggang dan disajikan dengan saus cabai pedas.\n\n"
        "Q: Apa itu Pisang Gapit Borneo?\n"
        "A: Pisang Gapit Borneo adalah hidangan penutup tradisional yang terbuat dari pisang panggang yang disajikan dengan saus manis.\n\n"
        "Q: Apakah Anda menawarkan layanan pengiriman?\n"
        "A: Ya, kami menawarkan layanan pengiriman melalui berbagai aplikasi pengiriman makanan.\n\n"
        "Q: Apa metode pembayaran yang Anda terima?\n"
        "A: Kami menerima pembayaran tunai, kartu kredit/debit, dan pembayaran melalui ponsel.\n\n"
        "Q: Bagaimana saya bisa menghubungi Anda?\n"
        "A: Anda dapat menghubungi kami melalui telepon di wa.me/62881026780972."
    )
    bot.reply_to(message, faq_text)

@bot.message_handler(func=lambda message: message.text.lower() == 'halo')
def send_hello(message):
    bot.reply_to(message, "Hi, selamat datang di bot Sate Taichan & Borneo")

# Handler untuk menangani perintah atau pesan yang tidak dikenal
@bot.message_handler(func=lambda message: True)
def handle_unknown_command(message):
    bot.reply_to(message, "Maaf, saya tidak mengerti perintah tersebut. Silakan gunakan /perintah untuk melihat daftar perintah yang tersedia.")

print ("bot is running...")
# Mulai polling
bot.polling()
