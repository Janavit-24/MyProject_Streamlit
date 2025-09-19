import streamlit as st

# Title
st.title("User Registration Form")

# Initialize session state
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Page 1: Registration Form
if not st.session_state.submitted:
    with st.form("registration_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        age = st.number_input("Age", min_value=1, step=1)
        gender = st.radio("Gender", ("Male", "Female", "Other"))
        password = st.text_input("Password", type="password")
        
        # Submit button
        submitted = st.form_submit_button("Submit")

    if submitted:
        if name and email and password:
            st.session_state.submitted = True
            st.session_state.name = name  # save for next page
        else:
            st.error("⚠️ Please fill in all required fields.")

# Page 2: After Submit
else:
    st.success("✅ Successfully Submitted!")
    st.write(f"Welcome, **{st.session_state.name}**! 🎉")
    st.write("This is the next page after submission.")
    
    # Option to go back
    if st.button("Go Back"):
        st.session_state.submitted = False
