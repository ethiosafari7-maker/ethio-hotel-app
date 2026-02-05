import streamlit as st
import requests

# --- የቴሌግራም ቦት ቅንብር (አሁን በሰጠኸኝ መረጃ ተስተካክሏል) ---
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
st.set_page_config(page_title="Ethio Hotel", page_icon="🏨", layout="centered")
st.markdown("<h1 style='text-align: center; color: #2E7D32;'>🏨 WELCOME TO ETHIO HOTEL 🇪🇹</h1>", unsafe_allow_html=True)

# 2. የሂሳብ እና የትዕዛዝ ዝርዝር መያዣ (Session State)
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'total_bill' not in st.session_state:
    st.session_state.total_bill = 0

# --- የደንበኛ መረጃ (Sidebar) ---
st.sidebar.header("👤 የደንበኛ መረጃ")
first_name = st.sidebar.text_input("First Name (ስም)", key="fname")
phone = st.sidebar.text_input("Phone Number (ስልክ)", key="u_phone")

# --- አገልግሎቶች ---
st.header("🍴 ምግብና አገልግሎቶችን ይምረጡ")
menu_option = st.selectbox("የአገልግሎት አይነት", 
                    ["ይምረጡ", "ETHIOPIAN FOOD", "CHINESE FOOD", "AMERICAN FOOD", "ROOM RENT"], key="main_menu")

items_dict = {
    "ETHIOPIAN FOOD": {"Vegetable": 30, "Meat Foods": 150, "Traditional": 40, "Drinks": 30},
    "CHINESE FOOD": {"Lamian": 80, "Pasta": 65, "Rice": 70, "Drinks": 20},
    "AMERICAN FOOD": {"Cheeseburger": 350, "Salad": 80, "Drinks": 25},
    "ROOM RENT": {"1st Floor": 230, "2nd Floor": 280, "3rd Floor": 200, "4th Floor": 380}
}

if menu_option in items_dict:
    options = list(items_dict[menu_option].keys())
    selected_item = st.selectbox(f"{menu_option} ይምረጡ", options)
    price = items_dict[menu_option][selected_item]
    qty = st.number_input("ብዛት", min_value=1, value=1, step=1)
    
    if st.button("🛒 ወደ ዝርዝር ጨምር"):
        item_total = price * qty
        st.session_state.cart.append({"item": selected_item, "qty": qty, "price": price, "subtotal": item_total})
        st.session_state.total_bill += item_total
        st.success(f"✅ {selected_item} ተጨምሯል!")

# --- የትዕዛዝ ዝርዝር (Cart) ---
if st.session_state.cart:
    st.subheader("📝 የእርስዎ ትዕዛዞች")
    for i, entry in enumerate(st.session_state.cart):
        st.write(f"{i+1}. {entry['item']} - {entry['qty']} x {entry['price']} = **{entry['subtotal']} Birr**")
    
    st.markdown(f"### 💰 ጠቅላላ ሂሳብ: `{st.session_state.total_bill}` Birr")
    
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
            # መልዕክቱን ማዘጋጀት
            order_details = ""
            for item in st.session_state.cart:
                order_details += f"• {item['item']} ({item['qty']} x {item['price']})\n"
            
            full_msg = (f"🔔 *አዲስ ትዕዛዝ ደርሷል!*\n\n"
                        f"👤 *ስም:* {first_name}\n"
                        f"📞 *ስልክ:* {phone}\n"
                        f"💳 *ክፍያ:* {pay_method}\n\n"
                        f"🍴 *ዝርዝር:*\n{order_details}\n"
                        f"💰 *ጠቅላላ ሂሳብ:* {st.session_state.total_bill} Birr")
            
            # ቦቱ መልዕክቱን በራሱ ለአንተ ይልካል
            if send_to_telegram(full_msg):
                st.balloons()
                st.success("✅ ትዕዛዝዎ በተሳካ ሁኔታ ተልኳል! በቅርቡ እንደውላለን።")
                # ከላከ በኋላ ዝርዝሩን ያጸዳል
                st.session_state.cart = []
                st.session_state.total_bill = 0
            else:
                st.error("❌ መልዕክቱ አልተላከም። ቦትዎ ላይ '/start' ማለታቸውን ያረጋግጡ።")
        else:
            st.error("እባክዎ መጀመሪያ ስም እና ትክክለኛ ስልክ ቁጥር ያስገቡ!")
