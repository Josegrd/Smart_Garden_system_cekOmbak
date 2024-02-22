from telegram.ext import Updater, CommandHandler
import RPi.GPIO as GPIO

# Konfigurasi pin GPIO
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Fungsi untuk menyalakan LED
def turn_on(update, context):
    GPIO.output(LED_PIN, GPIO.HIGH)
    update.message.reply_text('LED telah dinyalakan!')

# Fungsi untuk mematikan LED
def turn_off(update, context):
    GPIO.output(LED_PIN, GPIO.LOW)
    update.message.reply_text('LED telah dimatikan!')

def main():
    # Inisialisasi bot
    updater = Updater("TOKEN_BOT_ANDA", use_context=True)

    # Daftarkan handler untuk perintah /start dan /stop
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", turn_on))
    dispatcher.add_handler(CommandHandler("stop", turn_off))

    # Mulai bot
    updater.start_polling()

    # Jalankan bot hingga dihentikan
    updater.idle()

if __name__ == '__main__':
    main()
