import time
def save_to_history(name, phone, amount):
    current_time = time.asctime()
    
    # 'history.txt' የሚባል ፋይል ይከፍታል (ከሌለ ይፈጥራል)
    # "a" (append) ማለት አዲስ መረጃ ከታች መጨመር ማለት ነው
    with open("hotel_history.txt", "a", encoding="utf-8") as file:
        file.write("-" * 40 + "\n")
        file.write(f"Date: {current_time}\n")
        file.write(f"Customer: {name}\n")
        file.write(f"Phone: {phone}\n")
        file.write(f"Total Paid: {amount} Birr\n")
        file.write("-" * 40 + "\n\n")
    
    print("\n✅ Order history has been saved to 'hotel_history.txt'")

# --- አጠቃቀም ---
# በኮድህ መጨረሻ ላይ እንዲህ ብለህ ጥራው፡
# save_to_history(first_name, phone, total_bill)

# የሰዓት አቆጣጠር
current_time = time.asctime(time.localtime(time.time()))
total_bill = 0
# Colors
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
RED = "\033[1;31m"
RESET = "\033[0m"
CYAN    = "\033[0;36m"
# --- የጽሁፍ ቀለሞች (Text Colors/Foreground) ---
BLACK   = "\033[0;30m"
BLUE    = "\033[0;34m"
PURPLE  = "\033[0;35m"
WHITE   = "\033[0;37m"

# --- ደማቅ የጽሁፍ ቀለሞች (Bold Text Colors) ---
B_RED    = "\033[1;31m"
B_GREEN  = "\033[1;32m"
B_YELLOW = "\033[1;33m"
B_BLUE   = "\033[1;34m"
B_CYAN   = "\033[1;36m"
B_WHITE  = "\033[1;37m"

# --- የጀርባ ቀለሞች (Background Colors) ---
BG_BLACK  = "\033[40m"
BG_RED    = "\033[41m"
BG_GREEN  = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE   = "\033[44m"
BG_PURPLE = "\033[45m"
BG_CYAN   = "\033[46m"
BG_WHITE  = "\033[47m"

# --- ልዩ ስታይሎች (Special Styles) ---
UNDERLINE = "\033[4m"
RESET     = "\033[0m" # ቀለሙን ወደ መደበኛው ለመመለስ የግድ አስፈላጊ ነው!
# Header
print(f"      {current_time}")
print(f"{GREEN}============================================================={RESET}")
print(f"       {BG_BLUE}{B_WHITE} 🍎🍉🍋🇪🇹WELCOME TO ETHIO HOTEL🥬☕️🥂🇪🇹{RESET}")
print(f"=============================================================={RED}{RESET}")
first_name = input("    Enter First Name: ")
last_name = input("    Enter Second Name: ")
# የስልክ ቁጥር ማረጋገጫ (Validation Loop)
while True:
    phone = input("    Enter Phone number (10 digits): ")
    
    # .isdigit() ቁጥር መሆኑን ያረጋግጣል፣ len() ደግሞ ርዝመቱን ያረጋግጣል
    if phone.isdigit() and len(phone) == 10:
        break  # ቁጥሩ ትክክል ከሆነ ከሉፑ ይወጣል
    else:
        print(f"       {RED}Error: እባክዎ በትክክል 10 አሃዝ ያለው ስልክ ቁጥር ብቻ ያስገቡ! \n    (ፊደል ወይም ምልክት አይፈቀድም){RESET}       ")

# ቁጥሩ ትክክል ከሆነ በኋላ ወደ ቀጣዩ ሜኑ ያልፋል...

# ፕሮግራሙ እንዲደጋገም Loop እንጠቀማለን
print(f"{GREEN}")
while True:
    print("   \n" + "="*40)
    print("      ✅✅✅THE SERVICE WE PROVIDE✅✅✅")
    print(f"{B_CYAN}")
    print("    1. ETHIOPIAN FOOD")
    print("    2. CHINESE FOOD")
    print("    3. AMERICAN FOOD")
    print("    4. ROOM RENT")
    print("    5. FINISH & SHOW TOTAL BILL")
    print("    ="*40)
    
    menu = input("    Please enter your choice (1-5): ")

    # --- 1. ETHIOPIAN FOOD ---
    if menu == '1':
        print("    \n   1. Vegetable (30 Birr)    \n   2. Meat Foods (150 Birr)\n   3. Traditional (40 Birr)\n   4. Drinks (30 Birr)")
        category = input("   Choose category: ")
        price = 0
        if category == '1': price = 30
        elif category == '2': price = 150
        elif category == '3': price = 40
        elif category == '4': price = 30
        
        if price > 0:
            qty = int(input("   Enter quantity: "))
            total_bill += (price * qty)
            print(f"   Added! Subtotal: {price * qty} Birr")

    # --- 2. CHINESE FOOD ---
    elif menu == '2':
        print("\n   1. Lamian (80 Birr)\n   2. Pasta (65 Birr)\n   3. Rice (70 Birr)\n   4. Drinks (20 Birr)")
        category = input("   Choose category: ")
        price = 0
        if category == '1': price = 80
        elif category == '2': price = 65
        elif category == '3': price = 70
        elif category == '4': price = 20
        
        if price > 0:
            qty = int(input("   Enter quantity: "))
            total_bill += (price * qty)
            print(f"   Added! Subtotal: {price * qty} Birr")

    # --- 3. AMERICAN FOOD ---
    elif menu == '3':
        print("\n   1. Cheeseburger (350 Birr)\n   2. Salad (80 Birr)\n   3. Drinks (25 Birr)")
        category = input("   Choose category: ")
        price = 0
        if category == '1': price = 350
        elif category == '2': price = 80
        elif category == '3': price = 25
        
        if price > 0:
            qty = int(input("   Enter quantity: "))
            total_bill += (price * qty)
            print(f"   Added! Subtotal: {price * qty} Birr")

    # --- 4. ROOM RENT ---
    elif menu == '4':
        print("\n   1. First Floor (230 Birr)\n   2. Second Floor (280 Birr)\n   3. Third Floor (200 Birr)\n   4. Fourth Floor (380 Birr)")
        floor = input("   Choose Floor: ")
        price = 0
        if floor == '1': price = 230
        elif floor == '2': price = 280
        elif floor == '3': price = 200
        elif floor == '4': price = 380
        if price > 0:
            qty = int(input("   Enter Number of Days: "))
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
