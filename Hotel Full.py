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

# 1. የገጽታ ቅንብር
st.set_page_config(page_title="MULE TECH", page_icon="💻", layout="centered")

# --- ፕሮፋይል ምስል በራስጌ ላይ ---
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.markdown("<style>.profile-img {border-radius: 50%; border: 3px solid #1E88E5;}</style>", unsafe_allow_html=True)
    st.image("https://r.jina.ai/i/6c21e6be959f400780211832049e776a", width=150)

st.markdown("<h1 style='text-align: center; color: #1E88E5; font-size: 55px; margin-top: -20px;'>💻 MULE TECH 🇪🇹</h1>", unsafe_allow_html=True)

# 2. የትዕዛዝ መያዣ (Session State)
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'total_bill' not in st.session_state:
    st.session_state.total_bill = 0

# --- የደንበኛ መረጃ (Sidebar) ---
st.sidebar.header("👤 የደንበኛ መረጃ")
# እዚህ ጋር "የሰውየው ሙሉ ስም" ተብሎ ተቀይሯል
full_name = st.sidebar.text_input("የሰውየው ሙሉ ስም")
phone = st.sidebar.text_input("የስልክ ቁጥር")

# --- የምንሰጣቸው አገልግሎቶች ---
st.header("🛠 የምንሰጣቸው አገልግሎቶች")
main_service = st.selectbox("ዋና አገልግሎት ይምረጡ", 
                    ["ይምረጡ", "Video Editing", "Graphics Design", "HTTP/Free Internet File Making", "Social Media Management"])

# የአገልግሎት ዝርዝሮች
services_data = {
    "Video Editing": ["YouTube video Editing", "TikTok Video Editing", "Facebook Reel Video Editing", "YouTube Short Video Editing"],
    "Graphics Design": ["Thumbnail design", "Photo Design"],
    "HTTP/Free Internet File Making": ["SSH File making", "Xray File Making", "Http File Making", "Slow DNS File Making"],
    "Social Media Management": ["YouTube", "TikTok", "Telegram", "Facebook"]
}

if main_service != "ይምረጡ":
    st.subheader(f"የ {main_service} ዝርዝሮችን ይምረጡ")
    selected_subs = []
    
    # Checkbox በመጠቀም ዝርዝር አገልግሎቶችን መምረጥ
    for sub in services_data[main_service]:
        if st.checkbox(sub):
            selected_subs.append(sub)
    
    price = 400 
    st.info(f"የ {main_service} ጥቅል ዋጋ: **{price} Birr**")
    
    if st.button("🛒 ወደ ዝርዝር ጨምር"):
        if selected_subs:
            details = ", ".join(selected_subs)
            st.session_state.cart.append({"main": main_service, "details": details, "price": price})
            st.session_state.total_bill += price
            st.success(f"✅ {main_service} ታክሏል!")
        else:
            st.error("እባክዎ ቢያንስ አንድ ዝርዝር አገልግሎት ይምረጡ!")

# --- የትዕዛዝ ዝርዝር ማሳያ ---
if st.session_state.cart:
    st.divider()
    st.subheader("📝 የመረጧቸው አገልግሎቶች ዝርዝር")
    for i, entry in enumerate(st.session_state.cart):
        st.write(f"**{i+1}. {entry['main']}**")
        st.write(f"   _ዝርዝር፦ {entry['details']}_")
        st.write(f"   ዋጋ፦ **{entry['price']} Birr**")
    
    st.markdown(f"### 💰 ጠቅላላ ድምር ሂሳብ: `{st.session_state.total_bill}` Birr")
    
    if st.button("🗑 ዝርዝሩን አጥፋ"):
        st.session_state.cart = []
        st.session_state.total_bill = 0
        st.rerun()

st.divider()

# --- ክፍያ እና ትዕዛዝ ---
if st.session_state.cart:
    st.subheader("💳 ክፍያ እና ማጠናቀቂያ")
    pay_method = st.radio("የክፍያ ዘዴ", ["በጥሬ ገንዘብ", "በባንክ / ቴሌብር"])
    
    if pay_method == "በባንክ / ቴሌብር":
        st.warning("ቴሌብር: 0927275152 | ስም: MULUYE ARGO TADESSE")
    
    if st.button("🚀 ትዕዛዙን አሁን ላክ (Complete Order)"):
        if full_name and len(phone) >= 10:
            order_summary = ""
            for item in st.session_state.cart:
                order_summary += f"• *{item['main']}*\n  ({item['details']})\n"
            
            full_msg = (f"🔔 *አዲስ የ MULE TECH ትዕዛዝ!*\n\n"
                        f"👤 *ደንበኛ:* {full_name}\n"
                        f"📞 *ስልክ:* {phone}\n"
                        f"💳 *ክፍያ:* {pay_method}\n\n"
                        f"🛠 *አገልግሎቶች:* \n{order_summary}\n"
                        f"💰 *ጠቅላላ ድምር:* {st.session_state.total_bill} Birr")
            
            if send_to_telegram(full_msg):
                st.balloons()
                st.success("✅ ትዕዛዝዎ በተሳካ ሁኔታ ተልኳል!")
                st.session_state.cart = []
                st.session_state.total_bill = 0
            else:
                st.error("❌ መልዕክቱ አልተላከም።")
        else:
            st.error("እባክዎ የሰውየውን ሙሉ ስም እና ስልክ ያስገቡ!")
