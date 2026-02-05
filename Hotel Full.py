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

# --- ፕሮፋይል ምስል በራስጌ ላይ (Header Profile Image) ---
# ምስሉ ክብ እንዲሆን በ CSS ስታይል ተደርጓል
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.markdown(
        """
        <style>
        .profile-img {
            border-radius: 50%;
            width: 150px;
            height: 150px;
            object-fit: cover;
            display: block;
            margin-left: auto;
            margin-right: auto;
            border: 3px solid #1E88E5;
        }
        </style>
        """, unsafe_allow_html=True
    )
    # ያንተን የፕሮፋይል ፎቶ ሊንክ እዚህ ጋር ተጠቅሜያለሁ
    st.image("https://r.jina.ai/i/6c21e6be959f400780211832049e776a", width=150)

# MULE TECH በትልቅ ሳይዝ
st.markdown("<h1 style='text-align: center; color: #1E88E5; font-size: 60px; margin-top: -20px;'>💻 MULE TECH 🇪🇹</h1>", unsafe_allow_html=True)

# 2. የሂሳብ እና የትዕዛዝ ዝርዝር መያዣ (Session State)
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'total_bill' not in st.session_state:
    st.session_state.total_bill = 0

# --- የደንበኛ መረጃ (Sidebar) ---
st.sidebar.header("👤 የደንበኛ መረጃ")
first_name = st.sidebar.text_input("First Name (ስም)", key="fname")
phone = st.sidebar.text_input("Phone Number (ስልክ)", key="u_phone")

# --- የምንሰጣቸው አገልግሎቶች ---
st.header("🛠 የምንሰጣቸው አገልግሎቶች")
menu_option = st.selectbox("አገልግሎት ይምረጡ", 
                    ["ይምረጡ", "Video Editing", "Graphics Design", "HTTP/Free Internet File Making", "Social Media Management"], key="main_menu")

# የአገልግሎት ዝርዝር እና ዋጋ (ሁሉም 400 ብር)
services_dict = {
    "Video Editing": ["YouTube video Editing", "TikTok Video Editing", "Facebook Reel Video Editing", "YouTube Short Video Editing"],
    "Graphics Design": ["Thumbnail design", "Photo Design"],
    "HTTP/Free Internet File Making": ["SSH File making", "Xray File Making", "Http File Making", "Slow DNS File Making"],
    "Social Media Management": ["YouTube", "TikTok", "Telegram", "Facebook"]
}

if menu_option in services_dict:
    st.subheader(f"የ {menu_option} ዝርዝሮች")
    sub_service = st.selectbox("የአገልግሎት አይነት ይምረጡ", services_dict[menu_option])
    price = 400 
    
    st.write(f"የአገልግሎቱ ዋጋ: **{price} Birr**")
    
    if st.button("🛒 ወደ ዝርዝር ጨምር"):
        st.session_state.cart.append({"item": f"{menu_option} ({sub_service})", "price": price})
        st.session_state.total_bill += price
        st.success(f"✅ {sub_service} በዝርዝሩ ውስጥ ተጨምሯል!")

# --- የትዕዛዝ ዝርዝር (Cart) ---
if st.session_state.cart:
    st.divider()
    st.subheader("📝 የመረጧቸው አገልግሎቶች")
    for i, entry in enumerate(st.session_state.cart):
        st.write(f"{i+1}. {entry['item']} = **{entry['price']} Birr**")
    
    st.markdown(f"### 💰 ጠቅላላ ድምር ሂሳብ: `{st.session_state.total_bill}` Birr")
    
    if st.button("🗑 ዝርዝሩን አጥፋ"):
        st.session_state.cart = []
        st.session_state.total_bill = 0
        st.rerun()

st.divider()

# --- ክፍያ እና ትዕዛዙን መላኪያ ---
if st.session_state.cart:
    st.subheader("💳 ክፍያ እና ማጠናቀቂያ")
    pay_method = st.radio("የክፍያ ዘዴ", ["በጥሬ ገንዘብ", "በባንክ / ቴሌብር"])
    
    if pay_method == "በባንክ / ቴሌብር":
        st.info("🙏 እባክዎ ክፍያውን በዚህ የቴሌብር ቁጥር ይፈጽሙ፦")
        st.code("0927275152")
        st.write("ስም፦ **MULUYE ARGO TADESSE**")
    
    if st.button("🚀 ትዕዛዙን አሁን ላክ (Complete Order)"):
        if first_name and len(phone) >= 10:
            order_details = ""
            for item in st.session_state.cart:
                order_details += f"• {item['item']} - {item['price']} Birr\n"
            
            full_msg = (f"🔔 *አዲስ የ MULE TECH ትዕዛዝ!*\n\n"
                        f"👤 *ደንበኛ:* {first_name}\n"
                        f"📞 *ስልክ:* {phone}\n"
                        f"💳 *ክፍያ:* {pay_method}\n\n"
                        f"🛠 *የታዘዙ አገልግሎቶች:* \n{order_details}\n"
                        f"💰 *ጠቅላላ ድምር:* {st.session_state.total_bill} Birr")
            
            if send_to_telegram(full_msg):
                st.balloons()
                st.success("✅ ትዕዛዝዎ በተሳካ ሁኔታ ለ MULE TECH ተልኳል! በቅርቡ እናነጋግርዎታለን።")
                st.session_state.cart = [] 
                st.session_state.total_bill = 0
            else:
                st.error("❌ መልዕክቱ አልተላከም። እባክዎ በድጋሚ ይሞክሩ።")
        else:
            st.error("እባክዎ መጀመሪያ ስም እና ትክክለኛ ስልክ ቁጥር ያስገቡ!")
