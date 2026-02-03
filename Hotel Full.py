import streamlit as st
import time

# 1. የታሪክ ማስቀመጫ ፈንክሽን
def save_to_history(name, phone, amount):
    current_time = time.asctime()
    with open("hotel_history.txt", "a", encoding="utf-8") as file:
        file.write(f"{'-'*40}\nDate: {current_time}\nCustomer: {name}\nPhone: {phone}\nTotal: {amount} Birr\n{'-'*40}\n\n")

# የዌብሳይቱ ርዕስ
st.set_page_config(page_title="Ethio Hotel", page_icon="🏨")
st.title("🍎🍉 🇪🇹 WELCOME TO ETHIO HOTEL 🇪🇹 🥂")
st.write(f"አሁን ያለው ሰዓት: {time.asctime()}")

# --- የደንበኛ መረጃ ---
st.sidebar.header("የደንበኛ መረጃ")
first_name = st.sidebar.text_input("First Name", key="fname")
last_name = st.sidebar.text_input("Second Name", key="lname")
phone = st.sidebar.text_input("Phone number (10 digits)", key="u_phone")

# የሂሳብ መያዣ (Session State) - በStreamlit ውስጥ ሂሳብ እንዳይጠፋ የግድ ያስፈልጋል
if 'total_bill' not in st.session_state:
    st.session_state.total_bill = 0

# --- አገልግሎቶች ---
st.header("✅ THE SERVICE WE PROVIDE")
menu = st.selectbox("የአገልግሎት አይነት ይምረጡ", 
                    ["ይምረጡ", "ETHIOPIAN FOOD", "CHINESE FOOD", "AMERICAN FOOD", "ROOM RENT"], key="main_menu")

# 1. ETHIOPIAN FOOD
if menu == "ETHIOPIAN FOOD":
    category = st.selectbox("ምድብ ይምረጡ", 
                            ["Vegetable (30)", "Meat Foods (150)", "Traditional (40)", "Drinks (30)"], key="eth_cat")
    price = int(category.split('(')[1].split(')')[0])
    qty = st.number_input("ብዛት", min_value=1, value=1, key="eth_qty")
    if st.button("ወደ ሂሳብ ጨምር", key="btn1"):
        st.session_state.total_bill += (price * qty)
        st.success(f"ታዟል! ለጊዜው ጠቅላላ ሂሳብ: {st.session_state.total_bill} Birr")

# 2. CHINESE FOOD
elif menu == "CHINESE FOOD":
    category = st.selectbox("ምድብ ይምረጡ", 
                            ["Lamian (80)", "Pasta (65)", "Rice (70)", "Drinks (20)"], key="chi_cat")
    price = int(category.split('(')[1].split(')')[0])
    qty = st.number_input("ብዛት", min_value=1, value=1, key="chi_qty")
    if st.button("ወደ ሂሳብ ጨምር", key="btn2"):
        st.session_state.total_bill += (price * qty)
        st.success(f"ታዟል! ለጊዜው ጠቅላላ ሂሳብ: {st.session_state.total_bill} Birr")

# 3. AMERICAN FOOD
elif menu == "AMERICAN FOOD":
    category = st.selectbox("ምድብ ይምረጡ", 
                            ["Cheeseburger (350)", "Salad (80)", "Drinks (25)"], key="us_cat")
    price = int(category.split('(')[1].split(')')[0])
    qty = st.number_input("ብዛት", min_value=1, value=1, key="us_qty")
    if st.button("ወደ ሂሳብ ጨምር", key="btn3"):
        st.session_state.total_bill += (price * qty)
        st.success(f"ታዟል! ለጊዜው ጠቅላላ ሂሳብ: {st.session_state.total_bill} Birr")

# 4. ROOM RENT
elif menu == "ROOM RENT":
    floor = st.selectbox("ፎቅ ይምረጡ", 
                         ["1st Floor (230)", "2nd Floor (280)", "3rd Floor (200)", "4th Floor (380)"], key="room_cat")
    price = int(floor.split('(')[1].split(')')[0])
    qty = st.number_input("የቀናት ብዛት", min_value=1, value=1, key="room_qty")
    if st.button("ክፍል ያዝ", key="btn4"):
        st.session_state.total_bill += (price * qty)
        st.success("ክፍል ተይዟል!")

# --- ደረሰኝ ማውጫ ---
st.divider()
st.subheader(f"ጠቅላላ ሂሳብ: {st.session_state.total_bill} Birr")

if st.button("ጨርሻለሁ (Final Receipt)", key="finish"):
    if first_name and len(phone) == 10 and phone.isdigit():
        st.balloons()
        st.markdown(f"""
        ### 🧾 RECEIPT - ETHIO HOTEL
        **Customer:** {first_name} {last_name}  
        **Phone:** {phone}  
        **Total Amount:** {st.session_state.total_bill} Birr  
        *Thank you for visiting us!*
        """)
        # ታሪክ ውስጥ ያስቀምጣል
        save_to_history(first_name, phone, st.session_state.total_bill)
    else:
        st.error("እባክዎ ስም እና ትክክለኛ 10 አሃዝ ስልክ ቁጥር ያስገቡ!")

if st.button("አዲስ ትዕዛዝ (Reset)", key="reset"):
    st.session_state.total_bill = 0
    st.rerun()

    # --- 2. CHINESE FOOD ---
    elif menu == '2':
        print("\n   1. Lamian (80 Birr)\n   2. Pasta (65 Birr)\n   3. Rice (70 Birr)\n   4. Drinks (20 Birr)")
        category = st.text_input("   Choose category: ")
        price = 0
        if category == '1': price = 80
        elif category == '2': price = 65
        elif category == '3': price = 70
        elif category == '4': price = 20
        
        if price > 0:
            qty = st.number_input("   Enter quantity: ")
            total_bill += (price * qty)
            print(f"   Added! Subtotal: {price * qty} Birr")

    # --- 3. AMERICAN FOOD ---
    elif menu == '3':
        print("\n   1. Cheeseburger (350 Birr)\n   2. Salad (80 Birr)\n   3. Drinks (25 Birr)")
        category = st.text_input("   Choose category: ")
        price = 0
        if category == '1': price = 350
        elif category == '2': price = 80
        elif category == '3': price = 25
        
        if price > 0:
            qty = st.number_input("   Enter quantity: ")
            total_bill += (price * qty)
            print(f"   Added! Subtotal: {price * qty} Birr")

    # --- 4. ROOM RENT ---
    elif menu == '4':
        print("\n   1. First Floor (230 Birr)\n   2. Second Floor (280 Birr)\n   3. Third Floor (200 Birr)\n   4. Fourth Floor (380 Birr)")
        floor = st.text_input("   Choose Floor: ")
        price = 0
        if floor == '1': price = 230
        elif floor == '2': price = 280
        elif floor == '3': price = 200
        elif floor == '4': price = 380
        if price > 0:
            qty = st.number_input("   Enter Number of Days: ")
            total_bill += (price * qty)
            print(f"   Room booked! Subtotal: {price * qty} Birr")

    # --- 5. FINISH --- 
    elif menu == '5':
        break  # ሉፑን ያቆመዋል

    else:
        print("   Wrong selection! Please try again.")

# --- የመጨረሻ ደረሰኝ (Final Receipt) ---
print(f"{BG_BLUE}{B_YELLOW}")
print("\n" + "*"*45)
print(f"        RECEIPT - ETHIO HOTEL")
print("*"*45)
print(f"   Customer: {first_name} {last_name}")
print(f"   Phone: {phone}")
print(f"   Date: {current_time}")
print("-" * 45)
print(f"   TOTAL AMOUNT TO PAY: {total_bill} Birr")
print("-" * 45)
print("     Thank you for visiting us!")
print("*"*45)
