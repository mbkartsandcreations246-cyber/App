import streamlit as st

# --- Seed requirement (kg per acre) ---
seed_rate = {
    "rice": 30,
    "wheat": 40,
    "maize": 20,
    "millet": 10
}

# --- Soil advice ---
soil_advice = {
    "clay": {"en": "Clay soil holds water well, good for Rice.", "ta": "களிமண் மண் தண்ணீரை நன்றாக பிடிக்கும், அரிசிக்கு ஏற்றது."},
    "sandy": {"en": "Sandy soil drains quickly, good for groundnut & millet.", "ta": "மணல் மண் விரைவாக வடிகிறது, நிலக்கடலை மற்றும் கேழ்வரகு வளர்க்க ஏற்றது."},
    "loamy": {"en": "Loamy soil is rich and suitable for most crops.", "ta": "களிமண் கலந்த மண்வகை பல பயிர்களுக்கு ஏற்றது."},
    "red": {"en": "Red soil is good for cotton, pulses, and groundnut.", "ta": "சிவப்பு மண் பருத்தி, பருப்பு மற்றும் நிலக்கடலைக்கு நல்லது."},
    "black": {"en": "Black soil retains moisture, best for cotton & wheat.", "ta": "கருப்பு மண் ஈரத்தை தக்க வைக்கும், பருத்தி மற்றும் கோதுமைக்கு ஏற்றது."}
}

# --- UI ---
st.set_page_config(page_title="🌾 Smart Crop Advisory", layout="centered")

st.title("🌾 Smart Crop Advisory")

# Language selection
lang = st.selectbox("Select Language / மொழியைத் தேர்ந்தெடுக்கவும்:", ["English", "தமிழ்"])

# Inputs
ph = st.number_input("Soil pH/மண்ணின் அமிலத்தன்மை:", step=0.1)
rain = st.number_input("Rainfall/மழைப்பொழிவு (mm):", step=1)
crop = st.selectbox("Crop/பயிர்:", ["Rice/அரிசி", "Wheat/கோதுமை", "Maize/சோளம்", "Millet/தினை"])
soil = st.selectbox("Soil Type/மண் வகை", ["Clay/களிமண்", "Sandy/மணல்", "Loamy/களிமண் கலந்த", "Red/செம்மண்", "Black/கரிசல் மண் "])
land = st.number_input("Land Size/நில அளவு(in acres/ஏக்கர்):", step=1)

if st.button("Get Advice/அறிவுரை பெற"):
    crop_key = crop.lower()
    tips = []

    # pH advice
    if ph < 6:
        tips.append({"en": "⚠️ Soil is acidic → Apply lime.", "ta": "⚠️ மண் அமிலமாக உள்ளது → சுண்ணாம்பு சேர்க்கவும்."})
    elif ph > 7.5:
        tips.append({"en": "⚠️ Soil is alkaline → Add gypsum or compost.", "ta": "⚠️ மண் காரமாக உள்ளது → ஜிப்சம் அல்லது உரமிடவும்."})
    else:
        tips.append({"en": "✅ Soil pH is suitable.", "ta": "✅ மண்ணின் pH ஏற்றதாக உள்ளது."})

    # Rainfall advice
    if rain < 300:
        tips.append({"en": "⚠️ Low rainfall → Irrigation required.", "ta": "⚠️ குறைந்த மழை → பாசனம் தேவை."})
    elif rain > 1200:
        tips.append({"en": "⚠️ Excess rainfall → Ensure drainage.", "ta": "⚠️ அதிக மழை → வடிகால் வசதி செய்யவும்."})
    else:
        tips.append({"en": "✅ Rainfall is sufficient.", "ta": "✅ மழை போதுமானதாக உள்ளது."})

    # Soil advice
    tips.append(soil_advice[soil.lower()])

    # Seed requirement
    if crop_key in seed_rate:
        required_seed = seed_rate[crop_key] * land
        tips.append({
            "en": f"For {land} acres, you need approx {required_seed} kg of {crop}.",
            "ta": f"{land} ஏக்கருக்கு, சுமார் {required_seed} கிலோ {crop} விதைகள் தேவை."
        })

    # Display result
    st.subheader(f"🌱 Advisory for {crop}")
    for tip in tips:
        if lang == "English":
            st.write("- " + tip["en"])
        else:
            st.write("- " + tip["ta"])

