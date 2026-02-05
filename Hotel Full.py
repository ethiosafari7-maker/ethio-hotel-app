import streamlit as st
import requests
import random
import string
from datetime import datetime

# --- የቴሌግራም ቦት ቅንብር ---
BOT_TOKEN = "8477843612:AAFQxTf8e5XuVTVOvWPUK9AlMY2KsqwBiDc"
MY_CHAT_ID = "1312047180"

# Unique Order ID ማመንጫ
def generate_order_id():
    return 'MT-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def send_to_admin(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": MY_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        response = requests.post(url, data=data)
        return response.ok
    except: return False

# 1. የገጽታ ቅንብር (Custom CSS ለዲዛይን)
st.set_page_config(page_title="MULE TECH | Professional Tech Solutions", page_icon="💻", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #1E88E5; color: white; border: none; height: 3em; }
    .stButton>button:hover { background-color: #1565C0; border: none; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    h1 { color: #1E88E5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stExpander { border: 1px solid #1E88E5; border-radius: 10px; background-color: white; }
    </style>
    """, unsafe_allow_html=True)

# Live Chat Integration (Tawk.to)
st.markdown("""
    <script type="text/javascript">
    var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
    (function(){
    var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
    s1.async=True;
    s1.src='https://embed.tawk.to/YOUR_CHAT_ID_HERE/default';
    s1.charset='UTF-8';
    s1.setAttribute('crossorigin','*');
    s0.parentNode.insertBefore(s1,s0);
    })();
    </script>
    """, unsafe_allow_html=True)

# Session States
if 'page' not in st.session_state: st.session_state.page = "home"
if 'user_data' not in st.session_state: st.session_state.user_data = {}
if 'cart' not in st.session_state: st.session_state.cart = []

# --- Header Section ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://r.jina.ai/i/6c21e6be959f400780211832049e776a", width=180)
    st.markdown("<h1 style='text-align: center;'>MULE TECH SOLUTIONS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Your Reliable Partner in Digital Innovation</p>", unsafe_allow_html=True)

# --- Navigation Menu ---
menu = ["Home", "Services", "Portfolio", "Contact Us"]
choice = st.sidebar.radio("Navigation", menu)

# --- Home Page ---
if choice == "Home":
    st.session_state.page = "home"
    st.subheader("🚀 Welcome to the Future of Tech")
    
    # Portfolio Showcase
    st.markdown("### 🌟 Our Work Portfolio")
    p1, p2, p3 = st.columns(3)
    with p1: 
        st.image("https://via.placeholder.com/300x200?text=Video+Editing", caption="Professional Editing")
    with p2: 
        st.image("https://via.placeholder.com/300x200?text=Graphics+Design", caption="Creative Graphics")
    with p3: 
        st.image("https://via.placeholder.com/300x200?text=Network+Config", caption="Network Solutions")

    st.divider()
    
    # Registration Start
    st.subheader("👤 Client Registration")
    with st.form("professional_reg"):
        st.write("Please provide your formal details below:")
        f_name = st.text_input("Full Name *")
        f_email = st.text_input("Official Email Address *")
        f_phone = st.text_input("Primary Phone Number *")
        f_alt_phone = st.text_input("Alternative Phone (Optional)", placeholder="Optional")
        f_address = st.text_area("Residential/Business Address *")
        
        c1, c2 = st.columns(2)
        with c1: f_age = st.number_input("Age", 18, 90)
        with c2: f_gender = st.selectbox("Gender", ["Male", "Female"])
        
        st.write("---")
        st.write("👥 Emergency Contact (Closest Relative)")
        e_name = st.text_input("Relative Full Name *")
        e_phone = st.text_input("Relative Phone *")
        
        st.write("---")
        agree = st.checkbox("I agree to MULE TECH Terms of Service and Privacy Policy. *")
        
        if st.form_submit_button("Proceed to Services"):
            if f_name and f_email and f_phone and f_address and agree:
                st.session_state.user_data = {
                    "name": f_name, "email": f_email, "phone": f_phone,
                    "alt_phone": f_alt_phone, "address": f_address,
                    "age": f_age, "gender": f_gender, "e_name": e_name, "e_phone": e_phone
                }
                st.success("Information Saved. You can now select services from the Navigation menu!")
                st.session_state.page = "services"
            else:
                st.error("Please fill all required fields and agree to terms.")

# --- Services Page ---
elif choice == "Services":
    if not st.session_state.user_data:
        st.warning("⚠️ Please complete your registration on the Home page first.")
    else:
        st.header("🛠 Professional Service Selection")
        services = {
            "Video Editing": ["YouTube", "TikTok", "Facebook Reels", "Shorts"],
            "Graphics Design": ["Logo", "Thumbnail", "Poster", "Photo Retouch"],
            "Network Config": ["SSH", "Xray", "V2Ray", "SlowDNS"],
            "Social Management": ["YouTube Growth", "Telegram Admin", "FB Page Ads"]
        }
        
        selected_cat = st.selectbox("Select Service Category", list(services.keys()))
        selected_subs = st.multiselect(f"Select specific {selected_cat} services", services[selected_cat])
        
        if st.button("Add to Order"):
            if selected_subs:
                st.session_state.cart.append({"cat": selected_cat, "subs": ", ".join(selected_subs), "price": 400})
                st.toast("Service added to cart!")
            else:
                st.error("Select at least one sub-service.")

        if st.session_state.cart:
            st.divider()
            st.subheader("🛒 Your Order Summary")
            total = 0
            for item in st.session_state.cart:
                st.write(f"🔹 **{item['cat']}** ({item['subs']}) - {item['price']} ETB")
                total += item['price']
            
            st.markdown(f"### Total Amount: `{total} ETB`")
            
            pay_m = st.radio("Payment Method", ["Telebirr / Commercial Bank", "In-Person Cash"])
            if "Telebirr" in pay_m:
                st.info("Payment Details: 0927275152 (MULUYE ARGO)")
            
            if st.button("Finalize Order"):
                order_id = generate_order_id()
                u = st.session_state.user_data
                report = f"""
🔔 *NEW OFFICIAL ORDER: {order_id}*
👤 *Client:* {u['name']} ({u['gender']})
📧 *Email:* {u['email']}
📞 *Phone:* {u['phone']}
📍 *Address:* {u['address']}
👥 *Emergency:* {u['e_name']} ({u['e_phone']})

🛠 *Services:* {st.session_state.cart}
💰 *Total:* {total} ETB
💳 *Method:* {pay_m}
📅 *Date:* {datetime.now().strftime('%Y-%m-%d %H:%M')}
                """
                if send_to_admin(report):
                    st.balloons()
                    st.success(f"Order {order_id} submitted successfully! Check your email/Telegram for confirmation.")
                    st.session_state.cart = []

# --- Portfolio & Contact ---
elif choice == "Portfolio":
    st.header("📂 Previous Success Stories")
    st.write("MULE TECH has served over 500+ clients with 98% satisfaction.")
    # እዚህ ጋር ስራዎችህን በዝርዝር መደርደር ትችላለህ
    

elif choice == "Contact Us":
    st.header("📞 Contact Our Support Team")
    st.write("Telegram: @muletechreact")
    st.write("Phone: +251 927 275 152")
    st.write("Email: support@muletech.et")

