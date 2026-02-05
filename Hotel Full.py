import streamlit as st
import requests

# --- የቴሌግራም ቦት ቅንብር ---
BOT_TOKEN = "8477843612:AAFQxTf8e5XuVTVOvWPUK9AlMY2KsqwBiDc"
MY_CHAT_ID = "1312047180"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": MY_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        response = requests.post(url, data=data)
        return response.ok
    except:
        return False

# 1. የቋንቋ ምርጫ
lang = st.sidebar.selectbox("🌍 Select Language / ቋንቋ ይምረጡ / Afaan Filadhu", ["አማርኛ", "English", "Afaan Oromoo"])

txt = {
    "አማርኛ": {
        "title": "MULE TECH",
        "sidebar_header": "👤 የደንበኛ መረጃ",
        "name_label": "የሰውየው ሙሉ ስም",
        "phone_label": "የስልክ ቁጥር",
        "main_header": "🛠 የምንሰጣቸው አገልግሎቶች",
        "select_main": "ዋና አገልግሎት ይምረጡ",
        "select_sub": "ዝርዝሮችን ይምረጡ",
        "package_price": "ጥቅል ዋጋ",
        "add_to_cart": "🛒 ወደ ዝርዝር ጨምር",
        "cart_header": "📝 የመረጧቸው አገልግሎቶች ማጠቃለያ",
        "total": "ጠቅላላ ድምር ሂሳብ",
        "clear": "🗑 ዝርዝሩን አጥፋ",
        "pay_header": "💳 ክፍያ እና ማጠናቀቂያ",
        "pay_method": "የክፍያ ዘዴ",
        "cash": "በጥሬ ገንዘብ",
        "bank": "በባንክ / ቴሌብር",
        "order_btn": "🚀 ትዕዛዙን አሁን ላክ (Complete Order)",
        "success": "✅ ትዕዛዝዎ በተሳካ ሁኔታ ተልኳል!",
        "error_msg": "እባክዎ መረጃዎን በትክክል ያስገቡ!",
        "social_header": "📱 ማህበራዊ ሚዲያዎቻችን",
        "choose": "ይምረጡ"
    },
    "English": {
        "title": "MULE TECH",
        "sidebar_header": "👤 Customer Information",
        "name_label": "Full Name",
        "phone_label": "Phone Number",
        "main_header": "🛠 Our Services",
        "select_main": "Select Main Service",
        "select_sub": "Select Details",
        "package_price": "Package Price",
        "add_to_cart": "🛒 Add to Cart",
        "cart_header": "📝 Selected Services Summary",
        "total": "Total Bill",
        "clear": "🗑 Clear List",
        "pay_header": "💳 Payment and Completion",
        "pay_method": "Payment Method",
        "cash": "Cash",
        "bank": "Bank / Telebirr",
        "order_btn": "🚀 Complete Order Now",
        "success": "✅ Order sent successfully!",
        "error_msg": "Please enter your information correctly!",
        "social_header": "📱 Our Social Media",
        "choose": "Choose"
    },
    "Afaan Oromoo": {
        "title": "MULE TECH",
        "sidebar_header": "👤 Odeeffannoo Maamilaa",
        "name_label": "Maqaa Guutuu",
        "phone_label": "Lakk. Bilbilaa",
        "main_header": "🛠 Tajaajiloota Keenya",
        "select_main": "Tajaajila Guddaa Filadhu",
        "select_sub": "Bal'inaan Filadhu",
        "package_price": "Gatii Waligalaa",
        "add_to_cart": "🛒 Gara Kaartitti Dabali",
        "cart_header": "📝 Cuunfaa Tajaajiloota Filataman",
        "total": "Ida'ama Waligalaa",
        "clear": "🗑 Haqi",
        "pay_header": "💳 Kafaltii fi Xumura",
        "pay_method": "Mala Kafaltii",
        "cash": "Kashidhaan",
        "bank": "Baankiidhaan / Telebirr",
        "order_btn": "🚀 Amma Ergi (Order)",
        "success": "✅ Ergaan keessan milkaayinaan ddarbeera!",
        "error_msg": "Maaloo odeeffannoo keessan sirriitti guutaa!",
        "social_header": "📱 Miidiyaalee Hawaasaa Keenya",
        "choose": "Filadhu"
    }
}

t = txt[lang]

# 2. የገጽታ ቅንብር
st.set_page_config(page_title="MULE TECH", page_icon="💻", layout="centered")

# --- ፕሮፋይል ምስል ---
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("https://r.jina.ai/i/6c21e6be959f400780211832049e776a", width=150)

st.markdown(f"<h1 style='text-align: center; color: #1E88E5; font-size: 55px; margin-top: -20px;'>💻 {t['title']} 🇪🇹</h1>", unsafe_allow_html=True)

# 3. የማህበራዊ ሚዲያ ክፍሎች
st.divider()
st.subheader(t['social_header'])
s_col1, s_col2 = st.columns(2)
with s_col1:
    st.markdown(f"[![YouTube](https://img.shields.io/badge/YouTube-@muletechreact-red?style=for-the-badge&logo=youtube)](https://youtube.com/@muletechreact)")
with s_col2:
    st.markdown(f"[![Telegram](https://img.shields.io/badge/Telegram-@muletechreact-blue?style=for-the-badge&logo=telegram)](https://t.me/muletechreact)")

st.divider()

# Session State
if 'cart' not in st.session_state: st.session_state.cart = []
if 'total_bill' not in st.session_state: st.session_state.total_bill = 0

# Sidebar
st.sidebar.header(t['sidebar_header'])
full_name = st.sidebar.text_input(t['name_label'])
phone = st.sidebar.text_input(t['phone_label'])

# Services Data
services_data = {
    "Video Editing": ["YouTube video Editing", "TikTok Video Editing", "Facebook Reel Video Editing", "YouTube Short Video Editing"],
    "Graphics Design": ["Thumbnail design", "Photo Design"],
    "HTTP/Free Internet File Making": ["SSH File making", "Xray File Making", "Http File Making", "Slow DNS File Making"],
    "Social Media Management": ["YouTube", "TikTok", "Telegram", "Facebook"]
}

# 4. የአገልግሎት ምርጫ (Main Selection)
st.header(t['main_header'])
main_service = st.selectbox(t['select_main'], [t['choose']] + list(services_data.keys()))

if main_service != t['choose']:
    st.subheader(f"{t['select_sub']} ({main_service})")
    selected_subs = []
    for sub in services_data[main_service]:
        if st.checkbox(sub, key=f"{main_service}_{sub}"):
            selected_subs.append(sub)
    
    price = 400 
    st.info(f"{t['package_price']}: **{price} Birr**")
    
    if st.button(t['add_to_cart']):
        if selected_subs:
            details = ", ".join(selected_subs)
            # ዝርዝሩን ወደ ካርት መያዣው መክተት
            st.session_state.cart.append({"main": main_service, "details": details, "price": price})
            st.session_state.total_bill += price
            st.rerun()
        else:
            st.warning("Please select at least one detail!")

# --- 5. የመረጧቸው አገልግሎቶች ማጠቃለያ (Summary) ---
if st.session_state.cart:
    st.divider()
    st.subheader(t['cart_header'])
    
    # ሰንጠረዥ ወይም ዝርዝር መልክ ማሳያ
    for i, entry in enumerate(st.session_state.cart):
        with st.expander(f"📍 {entry['main']} - {entry['price']} Birr"):
            st.write(f"**ዝርዝር (Details):** {entry['details']}")
    
    st.markdown(f"### 💰 {t['total']}: `{st.session_state.total_bill}` Birr")
    
    if st.button(t['clear']):
        st.session_state.cart = []; st.session_state.total_bill = 0
        st.rerun()

    st.divider()

    # 6. ክፍያና ትዕዛዝ መላኪያ
    st.subheader(t['pay_header'])
    pay_method = st.radio(t['pay_method'], [t['cash'], t['bank']])
    if pay_method in [t['bank'], "Baankiidhaan / Telebirr", "በባንክ / ቴሌብር"]:
        st.warning("Telebirr: 0927275152 | Name: MULUYE ARGO TADESSE")
    
    if st.button(t['order_btn']):
        if full_name and len(phone) >= 10:
            order_summary = ""
            for item in st.session_state.cart:
                order_summary += f"• *{item['main']}*\n  ({item['details']})\n"
            
            full_msg = (f"🔔 *New Order!*\n👤 Name: {full_name}\n📞 Phone: {phone}\n💳 Pay: {pay_method}\n🛠 Services:\n{order_summary}\n💰 Total: {st.session_state.total_bill} Birr")
            
            if send_to_telegram(full_msg):
                st.balloons(); st.success(t['success'])
                st.session_state.cart = []; st.session_state.total_bill = 0
                # ከአጭር ጊዜ በኋላ ገጹን ለማደስ
                # st.rerun()
            else:
                st.error("Telegram error!")
        else:
            st.error(t['error_msg'])
