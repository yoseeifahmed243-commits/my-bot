import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import sqlite3
import time
import random

# ========== البيانات المهمة ==========
TOKEN = "8788796273:AAFu2ZFBtG8zcv4DlcqBJ0OeZU0pbCXj3BU"  # استبدل بتوكن البوت من BotFather

# حط معرف المدير (جيبه من @userinfobot)
ADMIN_IDS = [8767607098]  # تم التحديث

# يوزر الدعم
SUPPORT_USERNAME = "SULTANPRO223"
SUPPORT_LINK = f"https://t.me/{SUPPORT_USERNAME}"

# ========== إعدادات البوت ==========
bot = telebot.TeleBot(TOKEN)

# ========== قنوات الاشتراك الإجباري ==========
REQUIRED_CHANNELS = [
    {
        'username': 'shrhsultanpro',
        'link': 'https://t.me/shrhsultanpro',
        'name': '📚 قناة شروحات السلطان'
    },
    {
        'username': 'sultanpro00',
        'link': 'https://t.me/sultanpro00',
        'name': '📢 القناة الأساسية'
    },
    {
        'username': 'sultanbro223',
        'link': 'https://t.me/sultanbro223',
        'name': '🔑 قناة التفعيلات'
    }
]

# ========== أسعار شحن الرصيد بالنجوم ==========
STARS_DEPOSITS = {
    '15': {'stars': 15, 'amount': 5},
    '30': {'stars': 30, 'amount': 10},
    '75': {'stars': 75, 'amount': 25},
    '150': {'stars': 150, 'amount': 50},
    '300': {'stars': 300, 'amount': 100},
    '750': {'stars': 750, 'amount': 250},
    '1500': {'stars': 1500, 'amount': 500},
    '3000': {'stars': 3000, 'amount': 1000},
}

# ========== أسعار الهدايا ==========
GIFTS = {
    'star': {'name': '⭐ نجمة', 'price': 0.015, 'emoji': '⭐'},
    'bear': {'name': '🧸 دب', 'price': 0.22, 'emoji': '🧸'},
    'rose': {'name': '🌹 وردة', 'price': 0.3, 'emoji': '🌹'},
    'cake': {'name': '🎂 كيكة', 'price': 0.7, 'emoji': '🎂'},
    'ring': {'name': '💍 خاتم', 'price': 1.1, 'emoji': '💍'},
}

# ========== قائمة الدول (الأسعار +5 روبل) ==========
COUNTRIES = {
    'uzbekistan': {'name': '🇺🇿 Uzbekistan', 'price': 30.5},
    'bangladesh': {'name': '🇧🇩 Bangladesh', 'price': 17},
    'saudi': {'name': '🇸🇦 Saudi Arabia', 'price': 48.5},
    'russia': {'name': '🇷🇺 Russia', 'price': 56},
    'italy': {'name': '🇮🇹 Italy', 'price': 41.5},
    'mexico': {'name': '🇲🇽 Mexico', 'price': 27},
    'yemen': {'name': '🇾🇪 Yemen', 'price': 25},
    'latvia': {'name': '🇱🇻 Latvia', 'price': 56},
    'portugal': {'name': '🇵🇹 Portugal', 'price': 70.5},
    'kyrgyzstan': {'name': '🇰🇬 Kyrgyzstan', 'price': 48.5},
    'tajikistan': {'name': '🇹🇯 Tajikistan', 'price': 30.5},
    'usa': {'name': '🇺🇸 United States', 'price': 18},
    'egypt': {'name': '🇪🇬 Egypt', 'price': 21.5},
    'iraq': {'name': '🇮🇶 Iraq', 'price': 70.5},
    'turkey': {'name': '🇹🇷 Turkey', 'price': 41.5},
    'venezuela': {'name': '🇻🇪 Venezuela', 'price': 41.5},
    'colombia': {'name': '🇨🇴 Colombia', 'price': 17},
    'zimbabwe': {'name': '🇿🇼 Zimbabwe', 'price': 18},
    'france': {'name': '🇫🇷 France', 'price': 52.5},
    'argentina': {'name': '🇦🇷 Argentina', 'price': 32.5},
    'netherlands': {'name': '🇳🇱 Netherlands', 'price': 48.5},
    'uk': {'name': '🇬🇧 United Kingdom', 'price': 27},
    'hongkong': {'name': '🇭🇰 Hong Kong', 'price': 48.5},
    'thailand': {'name': '🇹🇭 Thailand', 'price': 29},
    'spain': {'name': '🇪🇸 Spain', 'price': 52.5},
    'tunisia': {'name': '🇹🇳 Tunisia', 'price': 34.5},
    'morocco': {'name': '🇲🇦 Morocco', 'price': 23.5},
    'india': {'name': '🇮🇳 India', 'price': 18},
    'lebanon': {'name': '🇱🇧 Lebanon', 'price': 56},
    'uae': {'name': '🇦🇪 UAE', 'price': 70.5},
    'germany': {'name': '🇩🇪 Germany', 'price': 56},
    'brazil': {'name': '🇧🇷 Brazil', 'price': 32.5},
    'japan': {'name': '🇯🇵 Japan', 'price': 52.5},
}

# ========== أرقام واتساب (WhatsApp Numbers) ==========
WHATSAPP_NUMBERS = {
    'random': {'name': '🎲 عشوائي', 'price': 14.0},
    'philippines': {'name': '🇵🇭 الفلبين', 'price': 14.0},
    'vietnam': {'name': '🇻🇳 فيتنام', 'price': 14.0},
    'indonesia': {'name': '🇮🇩 إندونيسيا', 'price': 14.0},
    'thailand': {'name': '🇹🇭 تايلاند', 'price': 14.0},
    'canada': {'name': '🇨🇦 كندا', 'price': 14.0},
    'egypt': {'name': '🇪🇬 مصر', 'price': 14.0},
    'south_africa': {'name': '🇿🇦 جنوب أفريقيا', 'price': 14.0},
    'morocco': {'name': '🇲🇦 المغرب', 'price': 17.0},
    'puerto_rico': {'name': '🇵🇷 بورتوريكو', 'price': 14.0},
    'libya': {'name': '🇱🇾 ليبيا', 'price': 14.0},
    'france': {'name': '🇫🇷 فرنسا', 'price': 14.0},
    'yemen': {'name': '🇾🇪 اليمن', 'price': 17.0},
    'syria': {'name': '🇸🇾 سوريا', 'price': 14.0},
    'algeria': {'name': '🇩🇿 الجزائر', 'price': 14.0},
    'angola': {'name': '🇦🇴 أنغولا', 'price': 14.0},
    'brazil': {'name': '🇧🇷 البرازيل', 'price': 12.0},
    'mexico': {'name': '🇲🇽 المكسيك', 'price': 14.0},
    'australia': {'name': '🇦🇺 استراليا', 'price': 14.0},
    'saudi': {'name': '🇸🇦 السعودية', 'price': 22.0},
    'uk': {'name': '🇬🇧 بريطانيا', 'price': 14.0},
    'turkey': {'name': '🇹🇷 تركيا', 'price': 14.0},
    'bangladesh': {'name': '🇧🇩 بنغلاديش', 'price': 14.0},
    'iraq': {'name': '🇮🇶 العراق', 'price': 14.0},
}

# ========== خدمات رشق تليجرام ==========
TELEGRAM_SPAM = {
    'reactions_blue': {'name': '🔵 تفاعلات تليجرام (أزرق)', 'price': 0.0025, 'type': 'تفاعلات'},
    'reactions_random': {'name': '🎲 تفاعلات تليجرام (عشوائي)', 'price': 0.0044, 'type': 'تفاعلات'},
    'reactions_gold': {'name': '⭐ تفاعلات تليجرام (ذهبي)', 'price': 0.0050, 'type': 'تفاعلات'},
    'members_channel': {'name': '📢 أعضاء قنوات خاصة', 'price': 0.05, 'type': 'أعضاء'},
    'members_group': {'name': '👥 أعضاء جروبات خاصة', 'price': 0.05, 'type': 'أعضاء'},
    'activation_code': {'name': '🔑 تفعيل تليجرام (رمز)', 'price': 0.0025, 'type': 'تفعيلات'},
}

# ========== خدمات انستغرام ==========
INSTAGRAM_SERVICES = {
    'followers_diff': {'name': '👥 متابعين حسابات مختلفة', 'price': 0.025, 'category': 'متابعين'},
    'followers_fast': {'name': '⚡ متابعين سرعة عالية', 'price': 0.044, 'category': 'متابعين'},
    'followers_high': {'name': '⭐ متابعين جودة عالية', 'price': 0.05, 'category': 'متابعين'},
    'followers_cheap': {'name': '💰 متابعين الأرخص عالمياً', 'price': 0.016, 'category': 'متابعين'},
    'views_video': {'name': '📹 مشاهدات فيديوهات', 'price': 0.000125, 'category': 'مشاهدات'},
    'views_story': {'name': '📸 مشاهدات ستوري', 'price': 0.0044, 'category': 'مشاهدات'},
    'views_reels': {'name': '🎬 مشاهدات ريلز', 'price': 0.000125, 'category': 'مشاهدات'},
    'views_reels_high': {'name': '🎬 مشاهدات ريلز (جودة)', 'price': 0.00025, 'category': 'مشاهدات'},
    'likes_comments': {'name': '💬 لايكات على تعليقات', 'price': 0.041, 'category': 'لايكات'},
    'likes_cheap': {'name': '💰 لايكات رخيصة', 'price': 0.0075, 'category': 'لايكات'},
    'likes_cheapest': {'name': '🏆 الأرخص عالمياً', 'price': 0.0056, 'category': 'لايكات'},
    'likes_high': {'name': '⭐ جودة عالية', 'price': 0.00375, 'category': 'لايكات'},
    'likes_arab': {'name': '🇸🇦 حسابات عربية', 'price': 0.0475, 'category': 'لايكات'},
    'likes_photo': {'name': '🖼️ منشورات صور', 'price': 0.0044, 'category': 'لايكات'},
    'likes_fast': {'name': '⚡ رشق فوري', 'price': 0.00375, 'category': 'لايكات'},
    'likes_updated': {'name': '🔄 خدمة محدثة', 'price': 0.0025, 'category': 'لايكات'},
    'comments_post': {'name': '💬 تعليقات منشورات', 'price': 0.0875, 'category': 'تعليقات'},
}

# ========== خدمات فيس بوك ==========
FACEBOOK_SERVICES = {
    'followers_lifetime': {'name': '♾️ متابعين إعادة تعبئة مدى الحياة', 'price': 0.031, 'category': 'متابعين'},
    'followers_groups': {'name': '👥 أعضاء مجموعات فيسبوك', 'price': 0.0125, 'category': 'متابعين'},
    'followers_personal': {'name': '👤 متابعين حسابات شخصية', 'price': 0.019, 'category': 'متابعين'},
    'followers_pages': {'name': '📄 متابعين صفحات + حسابات', 'price': 0.025, 'category': 'متابعين'},
    'followers_cheap': {'name': '💰 متابعين الأرخص عالمياً', 'price': 0.0225, 'category': 'متابعين'},
    'followers_medium': {'name': '⚡ متابعين سرعة متوسطة', 'price': 0.0125, 'category': 'متابعين'},
    'views_reels_lifetime': {'name': '🎬 مشاهدات ريلز ضمان مدى الحياة', 'price': 0.00625, 'category': 'مشاهدات'},
    'views_reels': {'name': '🎬 مشاهدات ريلز فيسبوك', 'price': 0.005, 'category': 'مشاهدات'},
    'views_reels_clips': {'name': '🎬 مشاهدات مقاطع ريلز', 'price': 0.00375, 'category': 'مشاهدات'},
    'views_video_reels': {'name': '📹 مشاهدات فيديوهات + ريلز', 'price': 0.00375, 'category': 'مشاهدات'},
}

# ========== خدمات تيك توك ==========
TIKTOK_SERVICES = {
    'followers_medium': {'name': '👥 متابعين سرعة متوسطة', 'price': 0.156, 'category': 'متابعين'},
    'followers_updated': {'name': '🔄 متابعين محدثة', 'price': 0.125, 'category': 'متابعين'},
    'followers_cheap': {'name': '💰 متابعين الأرخص عالمياً', 'price': 0.05, 'category': 'متابعين'},
    'views_high': {'name': '⭐ مشاهدات جودة مرتفعة', 'price': 0.00375, 'category': 'مشاهدات'},
    'views_video': {'name': '📹 مشاهدات فيديوهات', 'price': 0.0025, 'category': 'مشاهدات'},
    'views_fast': {'name': '⚡ مشاهدات سريعة', 'price': 0.00125, 'category': 'مشاهدات'},
    'likes_slow': {'name': '🐢 لايكات رشق بطئ', 'price': 0.00875, 'category': 'لايكات'},
    'likes_medium': {'name': '⚡ لايكات رشق متوسط', 'price': 0.0075, 'category': 'لايكات'},
    'likes_new': {'name': '🆕 لايكات حديثة', 'price': 0.00375, 'category': 'لايكات'},
    'likes_fast': {'name': '🔥 لايكات سريعة', 'price': 0.005, 'category': 'لايكات'},
}

# ========== خدمات كيك ==========
KICK_SERVICES = {
    'followers_month': {'name': '👥 متابعين ضمان شهر', 'price': 0.0875, 'category': 'متابعين'},
    'followers_year': {'name': '📅 متابعين ضمان سنة', 'price': 0.3125, 'category': 'متابعين'},
    'views_15min': {'name': '⏱️ مشاهدات بث 15 دقيقة', 'price': 0.0125, 'category': 'مشاهدات'},
    'views_30min': {'name': '⏱️ مشاهدات بث 30 دقيقة', 'price': 0.01625, 'category': 'مشاهدات'},
    'views_45min': {'name': '⏱️ مشاهدات بث 45 دقيقة', 'price': 0.0225, 'category': 'مشاهدات'},
    'views_60min': {'name': '⏱️ مشاهدات بث ساعة', 'price': 0.025, 'category': 'مشاهدات'},
    'views_90min': {'name': '⏱️ مشاهدات بث 90 دقيقة', 'price': 0.0375, 'category': 'مشاهدات'},
}

# ========== خدمات يوتيوب ==========
YOUTUBE_SERVICES = {
    'views_shorts': {'name': '📱 مشاهدات شورتس', 'price': 0.0375, 'category': 'مشاهدات'},
    'views_ads': {'name': '📺 مشاهدات إعلانات', 'price': 0.0625, 'category': 'مشاهدات'},
    'shares_twitter': {'name': '🐦 مشاركات تويتر', 'price': 0.025, 'category': 'مشاركات'},
    'shares_facebook': {'name': '📘 مشاركات فيسبوك', 'price': 0.025, 'category': 'مشاركات'},
    'shares_lifetime': {'name': '♾️ مشاركات ضمان مدى الحياة', 'price': 0.025, 'category': 'مشاركات'},
}

# ========== خدمات واتساب (رشق) ==========
WHATSAPP_SERVICES = {
    'members_arab': {'name': '🇸🇦 أعضاء قناة حسابات عربية', 'price': 0.125, 'category': 'أعضاء'},
    'members_month': {'name': '📅 أعضاء قناة ضمان شهر', 'price': 0.125, 'category': 'أعضاء'},
    'members_real': {'name': '👤 متابعين أعضاء حقيقيون', 'price': 0.1125, 'category': 'أعضاء'},
    'members_updated': {'name': '🔄 متابعين قناة خدمة محدثة', 'price': 0.081, 'category': 'أعضاء'},
    'reactions_blue': {'name': '🔵 تفاعلات مسابقات أزرق', 'price': 0.0375, 'category': 'تفاعلات'},
    'reactions_green': {'name': '🟢 تفاعلات مسابقات أخضر', 'price': 0.0375, 'category': 'تفاعلات'},
    'reactions_random_arab': {'name': '🎲 تفاعلات عشوائي عربي', 'price': 0.04, 'category': 'تفاعلات'},
    'reactions_random_mix': {'name': '🎲 تفاعلات عشوائي مختلف', 'price': 0.0475, 'category': 'تفاعلات'},
    'reactions_blue2': {'name': '🔵 تفاعلات مسابقات أزرق 2', 'price': 0.0475, 'category': 'تفاعلات'},
    'reactions_green2': {'name': '🟢 تفاعلات مسابقات أخضر 2', 'price': 0.041, 'category': 'تفاعلات'},
    'reactions_green3': {'name': '🟢 تفاعلات مسابقات أخضر 3', 'price': 0.044, 'category': 'تفاعلات'},
    'poll_1': {'name': '1️⃣ تصويت استطلاع الخيار 1', 'price': 0.1875, 'category': 'تصويتات'},
    'poll_2': {'name': '2️⃣ تصويت استطلاع الخيار 2', 'price': 0.1875, 'category': 'تصويتات'},
    'poll_3': {'name': '3️⃣ تصويت استطلاع الخيار 3', 'price': 0.1875, 'category': 'تصويتات'},
    'poll_4': {'name': '4️⃣ تصويت استطلاع الخيار 4', 'price': 0.1875, 'category': 'تصويتات'},
    'poll_random': {'name': '🎲 تصويت استطلاع عشوائي', 'price': 0.1875, 'category': 'تصويتات'},
}

# ========== قاعدة البيانات ==========
def get_db():
    return sqlite3.connect('sms_bot.db')

def init_db():
    conn = get_db()
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (user_id INTEGER PRIMARY KEY, username TEXT, 
                  balance REAL DEFAULT 0, joined_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                  is_admin INTEGER DEFAULT 0)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS numbers
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  number TEXT UNIQUE, country TEXT, service TEXT,
                  price REAL, status TEXT DEFAULT 'available',
                  added_date DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS orders
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER, number_id INTEGER,
                  number TEXT, country TEXT, service TEXT, price REAL,
                  sms_code TEXT DEFAULT NULL,
                  purchase_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                  status TEXT DEFAULT 'pending',
                  delivered_by INTEGER DEFAULT NULL,
                  delivered_date DATETIME DEFAULT NULL,
                  FOREIGN KEY(user_id) REFERENCES users(user_id))''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER, amount REAL, type TEXT,
                  description TEXT DEFAULT '',
                  date DATETIME DEFAULT CURRENT_TIMESTAMP,
                  FOREIGN KEY(user_id) REFERENCES users(user_id))''')
    
    conn.commit()
    conn.close()

# ========== الأزرار الرئيسية ==========
def main_keyboard():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(
        KeyboardButton("📱 شراء أرقام تليجرام"),
        KeyboardButton("📱 أرقام واتساب")
    )
    markup.add(
        KeyboardButton("🔥 خدمات الرشق"),
        KeyboardButton("💰 رصيدي")
    )
    markup.add(
        KeyboardButton("📜 طلباتي"),
        KeyboardButton("🆘 الدعم")
    )
    markup.add(
        KeyboardButton("📢 القناة"),
        KeyboardButton("❓ مساعدة")
    )
    return markup

# ========== لوحة تحكم المدير ==========
def admin_keyboard():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(
        KeyboardButton("📊 الإحصائيات"),
        KeyboardButton("👥 المستخدمين")
    )
    markup.add(
        KeyboardButton("📋 الطلبات المعلقة"),
        KeyboardButton("📱 إدارة الأرقام")
    )
    markup.add(
        KeyboardButton("📢 إشعار عام"),
        KeyboardButton("➕ إضافة مدير")
    )
    markup.add(
        KeyboardButton("💳 طلبات الشحن"),
        KeyboardButton("📈 الأرباح")
    )
    markup.add(
        KeyboardButton("🔙 رجوع للقائمة الرئيسية")
    )
    return markup

# ========== التحقق من الاشتراك ==========
def check_subscription(user_id):
    for channel in REQUIRED_CHANNELS:
        try:
            status = bot.get_chat_member(f"@{channel['username']}", user_id)
            if status.status in ['left', 'kicked']:
                return False, channel
        except:
            return False, channel
    return True, None

def send_subscription_required(message):
    user_id = message.from_user.id if hasattr(message, 'from_user') else message.chat.id
    
    markup = InlineKeyboardMarkup(row_width=1)
    for channel in REQUIRED_CHANNELS:
        markup.add(InlineKeyboardButton(f"📢 {channel['name']}", url=channel['link']))
    markup.add(InlineKeyboardButton("✅ تم الاشتراك", callback_data="check_subscription"))
    
    bot.send_message(
        user_id,
        f"""
🔒 **اشتراك إجباري!**

📌 **يرجى الاشتراك في القنوات التالية لاستخدام البوت:**

1️⃣ 📚 قناة شروحات السلطان
2️⃣ 📢 القناة الأساسية
3️⃣ 🔑 قناة التفعيلات

⚠️ **تنبيه:** بعد الاشتراك في جميع القنوات اضغط على "✅ تم الاشتراك"
""",
        reply_markup=markup,
        parse_mode='Markdown'
    )

# ========== /start ==========
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username or "بدون اسم"
    
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()
    conn.close()
    
    is_subscribed, channel = check_subscription(user_id)
    
    if not is_subscribed:
        send_subscription_required(message)
        return
    
    if user_id in ADMIN_IDS:
        keyboard = admin_keyboard()
        welcome = f"👋 أهلاً بك المدير {username}! 🛡️"
    else:
        keyboard = main_keyboard()
        welcome = f"👋 أهلاً بك {username}!"
    
    bot.send_message(
        user_id,
        welcome + "\n\n📱 اختر من الأزرار أدناه:",
        reply_markup=keyboard
    )

# ========== التحقق من الاشتراك بعد الضغط ==========
@bot.callback_query_handler(func=lambda call: call.data == "check_subscription")
def check_subscription_callback(call):
    user_id = call.from_user.id
    
    is_subscribed, channel = check_subscription(user_id)
    
    if is_subscribed:
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(
            user_id,
            "✅ **تم التحقق من الاشتراك!**\nأهلاً بك في البوت 🎉",
            reply_markup=main_keyboard(),
            parse_mode='Markdown'
        )
        bot.answer_callback_query(call.id, "✅ تم التحقق بنجاح!")
    else:
        markup = InlineKeyboardMarkup(row_width=1)
        for ch in REQUIRED_CHANNELS:
            markup.add(InlineKeyboardButton(f"📢 {ch['name']}", url=ch['link']))
        markup.add(InlineKeyboardButton("✅ تم الاشتراك", callback_data="check_subscription"))
        
        bot.edit_message_text(
            f"""
❌ **لم تشترك في جميع القنوات!**

📌 **يرجى الاشتراك في القناة المتبقية:**
🔹 {channel['name']}
🔗 {channel['link']}

⚠️ **بعد الاشتراك اضغط على "✅ تم الاشتراك"**
""",
            chat_id=user_id,
            message_id=call.message.message_id,
            reply_markup=markup,
            parse_mode='Markdown'
        )
        bot.answer_callback_query(call.id, "❌ اشترك في القناة أولاً")

# ========== عرض أرقام تليجرام ==========
@bot.message_handler(func=lambda msg: msg.text == "📱 شراء أرقام تليجرام")
def show_countries(message):
    user_id = message.from_user.id
    page = 1
    
    markup = InlineKeyboardMarkup(row_width=2)
    items_per_page = 10
    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    
    countries_list = list(COUNTRIES.items())[start_idx:end_idx]
    
    for key, value in countries_list:
        btn = InlineKeyboardButton(
            f"{value['name']} - {value['price']} ₽",
            callback_data=f"country_{key}"
        )
        markup.add(btn)
    
    nav_buttons = []
    for i in range(1, 9):
        text = f"[{i}]" if i == page else str(i)
        nav_buttons.append(InlineKeyboardButton(text, callback_data=f"page_{i}"))
    
    for i in range(0, len(nav_buttons), 4):
        markup.row(*nav_buttons[i:i+4])
    
    bot.send_message(
        user_id,
        f"""
📱 **اختر الدولة التي تريد شراء رقم منها**

📌 **الخدمة:** Telegram Activation
💰 **السيرفر:** (1)
📄 **الصفحة {page} من 8**
""",
        reply_markup=markup,
        parse_mode='Markdown'
    )

# ========== التنقل بين صفحات تليجرام ==========
@bot.callback_query_handler(func=lambda call: call.data.startswith('page_'))
def change_page(call):
    page = int(call.data.split('_')[1])
    user_id = call.from_user.id
    
    markup = InlineKeyboardMarkup(row_width=2)
    items_per_page = 10
    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    
    countries_list = list(COUNTRIES.items())[start_idx:end_idx]
    
    for key, value in countries_list:
        btn = InlineKeyboardButton(
            f"{value['name']} - {value['price']} ₽",
            callback_data=f"country_{key}"
        )
        markup.add(btn)
    
    nav_buttons = []
    for i in range(1, 9):
        text = f"[{i}]" if i == page else str(i)
        nav_buttons.append(InlineKeyboardButton(text, callback_data=f"page_{i}"))
    
    for i in range(0, len(nav_buttons), 4):
        markup.row(*nav_buttons[i:i+4])
    
    bot.edit_message_text(
        f"""
📱 **اختر الدولة التي تريد شراء رقم منها**

📌 **الخدمة:** Telegram Activation
💰 **السيرفر:** (1)
📄 **الصفحة {page} من 8**
""",
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=markup,
        parse_mode='Markdown'
    )
    bot.answer_callback_query(call.id)

# ========== اختيار دولة تليجرام ==========
@bot.callback_query_handler(func=lambda call: call.data.startswith('country_'))
def select_country(call):
    country_key = call.data.split('_')[1]
    user_id = call.from_user.id
    
    country_data = COUNTRIES.get(country_key)
    if not country_data:
        bot.answer_callback_query(call.id, "❌ الدولة غير موجودة")
        return
    
    country_name = country_data['name']
    price = country_data['price']
    
    markup = InlineKeyboardMarkup()
    confirm_btn = InlineKeyboardButton(f"✅ شراء بـ {price} ₽", callback_data=f"buy_{country_key}_{price}")
    cancel_btn = InlineKeyboardButton("❌ إلغاء", callback_data="cancel_buy")
    markup.add(confirm_btn)
    markup.add(cancel_btn)
    
    bot.send_message(
        user_id,
        f"""
📱 **شراء رقم من {country_name}**

📌 **الخدمة:** Telegram Activation
💰 **السعر:** {price} ₽
📌 **الحالة:** ✅ متاح

⚠️ **تنبيه:**
• سيتم خصم المبلغ من رصيدك
• الكود سيصلك خلال 5 دقائق
• في حال عدم وصول الكود سيتم الاسترداد

هل تريد تأكيد الشراء؟
""",
        reply_markup=markup,
        parse_mode='Markdown'
    )
    bot.answer_callback_query(call.id)

# ========== تأكيد شراء تليجرام ==========
@bot.callback_query_handler(func=lambda call: call.data.startswith('buy_') and not call.data.startswith('buy_wa_') and not call.data.startswith('buy_insta_') and not call.data.startswith('buy_fb_') and not call.data.startswith('buy_tt_') and not call.data.startswith('buy_kick_') and not call.data.startswith('buy_yt_') and not call.data.startswith('buy_spam_'))
def confirm_buy(call):
    user_id = call.from_user.id
    parts = call.data.split('_')
    country_key = parts[1]
    price = float(parts[2])
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute("SELECT balance FROM users WHERE user_id=?", (user_id,))
    result = c.fetchone()
    
    if not result:
        bot.send_message(user_id, "❌ يرجى استخدام /start أولاً")
        conn.close()
        return
    
    balance = result[0]
    
    if balance < price:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("💳 شحن الرصيد", callback_data="deposit"))
        
        bot.edit_message_text(
            f"""
❌ **رصيدك غير كافٍ!**

💰 رصيدك الحالي: {balance} ₽
💵 سعر الرقم: {price} ₽
🔻 العجز: {price - balance} ₽

📌 يرجى شحن رصيدك أولاً:
""",
            chat_id=user_id,
            message_id=call.message.message_id,
            reply_markup=markup,
            parse_mode='Markdown'
        )
        conn.close()
        return
    
    country_data = COUNTRIES.get(country_key)
    country_name = country_data['name']
    
    fake_number = f"+{random.randint(1000000000, 9999999999)}"
    
    c.execute("UPDATE users SET balance = balance - ? WHERE user_id=?", (price, user_id))
    c.execute("""
        INSERT INTO orders (user_id, number, country, service, price, status)
        VALUES (?, ?, ?, 'Telegram', ?, 'pending')
    """, (user_id, fake_number, country_name, price))
    
    order_id = c.lastrowid
    
    c.execute("""
        INSERT INTO transactions (user_id, amount, type)
        VALUES (?, ?, 'purchase')
    """, (user_id, -price))
    
    conn.commit()
    conn.close()
    
    bot.edit_message_text(
        f"""
✅ **تم شراء الرقم بنجاح!**

🆔 **رقم الطلب:** #{order_id}
📱 **الرقم:** `{fake_number}`
🏷️ **الدولة:** {country_name}
💰 **الس
