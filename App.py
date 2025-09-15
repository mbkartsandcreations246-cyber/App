import streamlit as st

# Page setup
st.set_page_config(page_title="🌱 Smart Crop Advisory", page_icon="🌾", layout="centered")

st.title("🌾 Smart Crop Advisory")

# User inputs
ph = st.number_input("Enter Soil pH:", min_value=0.0, max_value=14.0, step=0.1)
rain = st.number_input("Enter Rainfall (mm):", min_value=0.0, step=1.0)
crop = st.selectbox("Select Crop:", ["Rice", "Wheat", "Maize", "Millet", "Other"])

if st.button("Get Advice ✅"):
    tips = []

    # Soil pH advice
    if ph < 6:
        tips.append("⚠️ Soil is acidic → Apply lime to balance pH.")
    elif ph > 7.5:
        tips.append("⚠️ Soil is alkaline → Add gypsum or compost.")
    else:
        tips.append("✅ Soil pH is suitable for most crops.")

    # Rainfall advice
    if rain < 300:
        tips.append("⚠️ Rainfall is low → Irrigation required.")
    elif rain > 1200:
        tips.append("⚠️ Excess rainfall → Ensure drainage system.")
    else:
        tips.append("✅ Rainfall is sufficient for farming.")

    # Crop-specific advice
    if crop == "Rice":
        tips.append("🌾 Rice: Needs standing water and clay soil.")
    elif crop == "Wheat":
        tips.append("🌿 Wheat: Prefers neutral soil and moderate irrigation.")
    elif crop == "Maize":
        tips.append("🌽 Maize: Requires nitrogen-rich soil, apply urea carefully.")
    elif crop == "Millet":
        tips.append("🌱 Millets: Grow well in dry, drought-prone areas.")
    else:
        tips.append("ℹ️ Consult local agri office for this crop.")

    # Display result
    st.subheader(f"Advisory for {crop}")
    for t in tips:
        st.write("- " + t)
