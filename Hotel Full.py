import streamlit as st
import requests
import re

# --- የቴሌግራም ቦት ቅንብር ---
BOT_TOKEN = "8477843612:AAFQxTf8e5XuVTVOvWPUK9AlMY2KsqwBiDc"
MY_CHAT_ID = "1312047180"

def send_to_admin(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": MY_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        response = requests.post(url, data=data)
        return response.ok
    except: return False

# --- የገጽታ ቅንብር ---
st.set_page_config(page_title="MULE TECH | Official", page_icon="💻", layout="centered")

# Custom CSS ለውበት እና ለሁኔታዎች ማሳያ
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; font-weight: bold; height: 3em; }
    .success-text { color: #28a745; font-size: 0.9em; font-weight: bold; }
    .error-text { color: #dc3545; font-size: 0.9em; font-weight: bold; }
    div[data-testid="stExpander"] { border: 1px solid #1E88E5; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Session State መቆጣጠሪያ
if 'page' not in st.session_state: st.session_state.page = "personal_info"
if 'user_data' not in st.session_state: st.session_state.user_data = {}

# 1. የቋንቋ ምርጫ (Bilingual Support)
lang = st.sidebar.selectbox("🌍 ቋንቋ ይምረጡ / Select Language / Afaan Filadhu", ["አማርኛ", "English", "Afaan Oromoo"])

texts = {
    "አማርኛ": {"next": "ቀጥል", "back": "ተመለስ", "complete": "ትዕዛዙን አጠናቅቅ", "order_id": "የትዕዛዝ መለያ", "valid_email": "ትክክለኛ ኢሜይል", "invalid_email": "እባክዎን ትክክለኛ ኢሜይል ያስገቡ (@gmail.com)"},
    "English": {"next": "Next", "back": "Back", "complete": "Complete Order", "order_id": "Order ID", "valid_email": "Valid Email", "invalid_email": "Please enter a valid email (@gmail.com)"},
    "Afaan Oromoo": {"next": "Itti fufi", "back": "Gara duubaa", "complete": "Xumuri", "order_id": "Eenyummaa Ajajaa", "valid_email": "Email Sirrii", "invalid_email": "Maaloo Email sirrii galchaa (@gmail.com)"}
}
t = texts[lang]

# --- ርዕስ ---
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>💻 MULE TECH 🇪🇹</h1>", unsafe_allow_html=True)

# --- ገፅ 1: የግል መረጃ (Personal Information) ---
if st.session_state.page == "personal_info":
    st.subheader("👤 Personal Information")
    
    # Validation Logic
    col1, col2, col3 = st.columns(3)
    with col1:
        f_name = st.text_input("First Name")
        if len(f_name) >= 3: st.markdown("<span class='success-text'>✅</span>", unsafe_allow_html=True)
    with col2:
        m_name = st.text_input("Middle Name")
        if len(m_name) >= 3: st.markdown("<span class='success-text'>✅</span>", unsafe_allow_html=True)
    with col3:
        l_name = st.text_input("Last Name")
        if len(l_name) >= 3: st.markdown("<span class='success-text'>✅</span>", unsafe_allow_html=True)

    email = st.text_input("Email Address")
    is_email_valid = email.lower().endswith("@gmail.com")
    if email:
        if is_email_valid: st.markdown(f"<span class='success-text'>✅ {t['valid_email']}</span>", unsafe_allow_html=True)
        else: st.markdown(f"<span class='error-text'>❌ {t['invalid_email']}</span>", unsafe_allow_html=True)

    phone = st.text_input("Phone Number", placeholder="09/07********", max_chars=10)
    is_phone_valid = len(phone) == 10 and (phone.startswith("09") or phone.startswith("07"))
    if phone:
        if is_phone_valid: st.markdown("<span class='success-text'>✅ Phone Valid</span>", unsafe_allow_html=True)
        else: st.markdown("<span class='error-text'>❌ Phone must be 10 digits (09/07)</span>", unsafe_allow_html=True)

    alt_phone = st.text_input("Additional Phone (Optional)", placeholder="Optional")
    
    c_age, c_gen = st.columns(2)
    with c_age: age = st.number_input("Age", 12, 100)
    with c_gen: gender = st.selectbox("Gender", ["Male", "Female"])
    
    address = st.text_area("Residential Address")
    st.markdown("---")
    e_name = st.text_input("Emergency Contact Name")
    e_phone = st.text_input("Emergency Contact Phone", max_chars=10)

    if st.button(t['next']):
        if len(f_name) >= 3 and len(m_name) >= 3 and len(l_name) >= 3 and is_email_valid and is_phone_valid and address and e_name:
            st.session_state.user_data = {
                "full_name": f"{f_name} {m_name} {l_name}", "email": email, "phone": phone,
                "alt_phone": alt_phone, "address": address, "age": age, "gender": gender,
                "e_name": e_name, "e_phone": e_phone
            }
            st.session_state.page = "services"
            st.rerun()
        else:
            st.error("Please ensure all fields are correct and names are > 3 letters.")

# --- ገፅ 2: አገልግሎት እና ክፍያ ---
elif st.session_state.page == "services":
    # --- Portfolio Section ---
    st.info("📂 **MULE TECH Portfolio**\n\n* **Telegram:** 1200+ Clients use free internet.\n* **YouTube:** 340+ Clients learning Video editing, Free Internet, and Graphics Design.")
    
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        st.link_button("🔥 YouTube Channel", "https://youtube.com/@muletechreact", type="primary")
    with p_col2:
        st.link_button("📢 Telegram Channel", "https://t.me/muletechreact", type="primary")

    st.divider()
    
    # የአገልግሎት ምርጫ
    st.subheader("🛠 Select Services")
    service_list = ["Video Editing", "Graphics Design", "Free Internet Files", "Social Media Management"]
    selected = st.multiselect("Choose Services", service_list)
    
    if selected:
        st.write(f"### Total: {len(selected) * 400} ETB")
        
        st.subheader("💳 Payment Methods (No Cash/In-person)")
        pay_col1, pay_col2, pay_col3 = st.columns(3)
        
        with pay_col1:
            if st.button("Telebirr"): st.session_state.bank = "Telebirr: 0927275152 | MULUYE ARGO TADESSE"
        with pay_col2:
            if st.button("CBE"): st.session_state.bank = "CBE: 1000745084773 | MULUYE ARGO TADESSE"
        with pay_col3:
            if st.button("Abyssinia"): st.session_state.bank = "Abyssinia: 231006718 | MULUYE ARGO TADESSE"
            
        if 'bank' in st.session_state:
            st.success(st.session_state.bank)

        if st.button(t['complete']):
            u = st.session_state.user_data
            report = f"🔔 *NEW ORDER*\n👤 Name: {u['full_name']}\n📧 Email: {u['email']}\n📞 Phone: {u['phone']}\n📍 Address: {u['address']}\n🛠 Services: {', '.join(selected)}"
            if send_to_admin(report):
                st.balloons()
                st.success("Order Sent Successfully!")

    # Support Buttons
    st.divider()
    sup_col1, sup_col2 = st.columns(2)
    with sup_col1:
        st.link_button("📧 Support Email", "mailto:Mulereact6@gmail.com")
    with sup_col2:
        st.link_button("✈️ Support Telegram", "https://t.me/MuleTechSupport")
    
    if st.button(t['back']):
        st.session_state.page = "personal_info"
        st.rerun()
