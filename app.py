import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(page_title="AI Grocery Planning Agent", layout="wide")

# Background styling
page_bg = """
<style>
[data-testid="stAppViewContainer"]{
background-image: linear-gradient(120deg,#a8edea,#fed6e3);
background-size: cover;
}

h1{
color:#2c3e50;
text-align:center;
}

.stButton>button{
background-color:#2ecc71;
color:white;
font-size:18px;
border-radius:10px;
padding:10px 20px;
}

.stTextInput>div>div>input{
border-radius:10px;
}

.stNumberInput>div>div>input{
border-radius:10px;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.title("🛒 Smart Grocery Planning AI Agent")

st.write("Plan groceries, find nearby stores, and compare online shopping options.")

st.divider()

# User inputs
col1, col2, col3 = st.columns(3)

with col1:
    family = st.number_input("Family Size", 1, 10, 3)

with col2:
    budget = st.number_input("Budget ₹", 100, 10000, 2000)

with col3:
    diet = st.selectbox("Diet Preference", ["Vegetarian","Non-Vegetarian"])

location = st.text_input("Enter your city or area")

st.divider()

# Grocery generator
if st.button("Generate Grocery List"):

    if diet == "Vegetarian":
        items = [
        "Rice","Dal","Tomatoes","Onions","Potatoes",
        "Spinach","Milk","Curd","Bananas","Cooking Oil"
        ]
    else:
        items = [
        "Rice","Chicken","Eggs","Milk","Tomatoes",
        "Onions","Potatoes","Bananas","Cooking Oil"
        ]

    df = pd.DataFrame(items, columns=["Grocery Items"])

    st.subheader("Generated Grocery List")
    st.table(df)

    st.success("Grocery plan created successfully!")

st.divider()

# Nearby stores
st.subheader("📍 Find Nearby Grocery Stores")

if st.button("Locate Stores"):

    if location:
        maps_link = f"https://www.google.com/maps/search/grocery+stores+near+{location}"
        st.markdown(f"### 👉 [Open Nearby Stores in Google Maps]({maps_link})")
    else:
        st.warning("Please enter your location")

st.divider()

# Online shopping
st.subheader("🛍️ Buy Groceries Online")

item_search = st.text_input("Search item to buy online")

if st.button("Search Online Stores"):

    if item_search:

        st.markdown(
        f"🛒 [Search on Amazon](https://www.amazon.in/s?k={item_search}+grocery)"
        )

        st.markdown(
        f"🛒 [Search on Flipkart](https://www.flipkart.com/search?q={item_search})"
        )

        st.markdown(
        f"🛒 [Search on BigBasket](https://www.bigbasket.com/ps/?q={item_search})"
        )

        st.markdown(
        f"🛒 [Search on Blinkit](https://blinkit.com/s/?q={item_search})"
        )

st.divider()

# Price comparison demo
st.subheader("💰 Smart Price Comparison")

data = {
"Item":["Rice","Milk","Tomatoes"],
"Amazon":[220,60,40],
"BigBasket":[210,58,35],
"Blinkit":[230,65,45]
}

df = pd.DataFrame(data)

st.table(df)

totals = {
"Amazon":sum(df["Amazon"]),
"BigBasket":sum(df["BigBasket"]),
"Blinkit":sum(df["Blinkit"])
}

best_store = min(totals, key=totals.get)

st.success(f"Recommended Store: {best_store}")