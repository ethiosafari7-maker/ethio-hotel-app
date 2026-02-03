import streamlit as st
import time

# 1. የታሪክ ማስቀመጫ ፈንክሽን
def save_to_history(name, phone, amount):
    current_time = time.ctime()
    try:
        with open("hotel_history.txt", "a", encoding="utf-8") as file:
            file.write(f"{'-'*40}\nDate: {current_time}\nCustomer: {name}\nPhone: {phone}\nTotal: {amount} Birr\n{'-'*40}\n\n")
    except:
        pass

# የዌብሳይቱ ገጽታ እና ርዕስ
st.set_page_config(page_title="Ethio Hotel", page_icon="🏨")
st.markdown("<h1 style='text-align: center; color: green;'>🏨 WELCOME TO ETHIO HOTEL 🇪🇹</h1>", unsafe_allow_html=True)
st.write(f"📅 **Date:** {time.ctime()}")

# የሂሳብ መያዣ (Session State) - ሂሳቡ እንዳይጠፋ
if 'total_bill' not in st.session_state:
    st.session_state.total_bill = 0

# --- የደንበኛ መረጃ (Sidebar) ---
st.sidebar.header("📋 የደንበኛ መረጃ")
first_name = st.sidebar.text_input("First Name", key="fname")
last_name = st.sidebar.text_input("Second Name", key="lname")
phone = st.sidebar.text_input("Phone number (10 digits)", key="u_phone")

# --- አገልግሎቶች ---
st.header("🍴 አገልግሎታችንን ይምረጡ")
menu = st.selectbox("የአገልግሎት አይነት", 
                    ["ይምረጡ", "1. ETHIOPIAN FOOD", "2. CHINESE FOOD", "3. AMERICAN FOOD", "4. ROOM RENT"], key="main_menu")

# --- 1. ETHIOPIAN FOOD ---
if menu == "1. ETHIOPIAN FOOD":
    category = st.selectbox("ምግብ ይምረጡ", 
                            ["Vegetable (30)", "Meat Foods (150)", "Traditional (40)", "Drinks (30)"], key="eth_cat")
    price = int(category.split('(')[1].split(')')[0])
    qty = st.number_input("ብዛት", min_value=1, value=1, step=1, key="eth_qty")
    if st.button("ወደ ሂሳብ ጨምር", key="btn1"):
        st.session_state.total_bill += (price * qty)
        st.success(f"ታዟል! ለጊዜው ጠቅላላ ሂሳብ: {st.session_state.total_bill} Birr")

# --- 2. CHINESE FOOD ---
elif menu == "2. CHINESE FOOD":
    category = st.selectbox("የቻይና ምግብ ይምረጡ", 
                            ["Lamian (80)", "Pasta (65)", "Rice (70)", "Drinks (20)"], key="chi_cat")
    price = int(category.split('(')[1].split(')')[0])
    qty = st.number_input("ብዛት", min_value=1, value=1, step=1, key="chi_qty")
    if st.button("ወደ ሂሳብ ጨምር", key="btn2"):
        st.session_state.total_bill += (price * qty)
        st.success(f"ታዟል! ለጊዜው ጠቅላላ ሂሳብ: {st.session_state.total_bill} Birr")

# --- 3. AMERICAN FOOD ---
elif menu == "3. AMERICAN FOOD":
    category = st.selectbox("የአሜሪካ ምግብ ይምረጡ", 
                            ["Cheeseburger (350)", "Salad (80)", "Drinks (25)"], key="us_cat")
    price = int(category.split('(')[1].split(')')[0])
    qty = st.number_input("ብዛት", min_value=1, value=1, step=1, key="us_qty")
    if st.button("ወደ ሂሳብ ጨምር", key="btn3"):
        st.session_state.total_bill += (price * qty)
        st.success(f"ታዟል! ለጊዜው ጠቅላላ ሂሳብ: {st.session_state.total_bill} Birr")

# --- 4. ROOM RENT ---
elif menu == "4. ROOM RENT":
    floor = st.selectbox("ፎቅ ይምረጡ", 
                         ["1st Floor (230)", "2nd Floor (280)", "3rd Floor (200)", "4th Floor (380)"], key="room_cat")
    price = int(floor.split('(')[1].split(')')[0])
    qty = st.number_input("የቀናት ብዛት", min_value=1, value=1, step=1

