import streamlit as st
import pickle

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title("Substance Abuse Risk Detection System")

st.header("Enter your details below:")

# Basic Inputs
age = st.number_input("Age", 15, 60)
stress = st.slider("Stress Level (1=Low, 3=High)", 1, 3)
sleep = st.slider("Sleep Hours", 3, 10)

alcohol = st.selectbox("Do you consume alcohol?", ["No", "Yes"])
smoking = st.selectbox("Do you smoke?", ["No", "Yes"])

# Convert to numeric
alcohol_val = 1 if alcohol == "Yes" else 0
smoking_val = 1 if smoking == "Yes" else 0

# Additional Inputs
st.subheader("Health & Lifestyle Information")

prescription = st.text_area("Prescription (if any)")
medical_history = st.text_area("Medical History")
mental_health = st.selectbox("Mental Health Status", ["Good", "Average", "Poor"])
lifestyle = st.selectbox("Lifestyle Habits", ["Healthy", "Moderate", "Unhealthy"])
routine = st.selectbox("Daily Routine", ["Regular", "Irregular"])

# Predict Button
if st.button("Predict Risk"):

    # ML Prediction
    result = model.predict([[age, stress, sleep, alcohol_val, smoking_val]])

    # Show Risk Result
    if result[0] == 0:
        st.success("Low Risk ✅")
    elif result[0] == 1:
        st.warning("Medium Risk ⚠️")
    else:
        st.error("High Risk 🚨")

    # Show Detailed Report
    st.subheader("Health Report")

    st.write("💊 Prescription:", prescription if prescription else "None")
    st.write("🏥 Medical History:", medical_history if medical_history else "None")
    st.write("🧠 Mental Health:", mental_health)
    st.write("🏃 Lifestyle Habits:", lifestyle)
    st.write("⏰ Daily Routine:", routine)

    # Precautions & Suggestions
    st.subheader("Precautions & Recommendations")

    if result[0] == 2:  # High Risk
        st.error("⚠️ High Risk - Immediate Action Needed")

        st.write("### 🚫 Precautions:")
        st.write("- Avoid alcohol and smoking completely")
        st.write("- Stay away from negative peer influence")
        st.write("- Maintain a structured daily routine")
        st.write("- Stay connected with family and friends")

        st.write("### 💡 How to Get Rid of It:")
        st.write("- Seek professional counseling")
        st.write("- Practice meditation and yoga")
        st.write("- Engage in physical activities")
        st.write("- Join support or awareness programs")

    elif result[0] == 1:  # Medium Risk
        st.warning("⚠️ Medium Risk - Be Careful")

        st.write("### 🚫 Precautions:")
        st.write("- Limit alcohol consumption")
        st.write("- Avoid unhealthy habits")
        st.write("- Improve sleep schedule")

        st.write("### 💡 How to Reduce Risk:")
        st.write("- Follow healthy lifestyle")
        st.write("- Exercise regularly")
        st.write("- Manage stress effectively")

    else:  # Low Risk
        st.success("✅ Low Risk - You are Safe")

        st.write("### 👍 Maintain This Lifestyle:")
        st.write("- Continue healthy habits")
        st.write("- Keep regular sleep routine")
        st.write("- Stay active and positive")