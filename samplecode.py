import streamlit as st

# Title
st.title("User Registration Form")

# Create form
with st.form("registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=1, step=1)
    gender = st.radio("Gender", ("Male", "Female", "Other"))
    password = st.text_input("Password", type="password")
    
    # Submit button
    submitted = st.form_submit_button("Submit")

# Show success message
if submitted:
    if name and email and password:
        st.success("✅ Successfully Submitted!")
        st.write(f"Welcome, **{name}**! Your registration is complete.")
    else:
        st.error("⚠️ Please fill in all required fields.")
