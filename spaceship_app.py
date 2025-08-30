import streamlit as st

def spaceship_order_app():
    st.title("🛸 Welcome to Walsal201 Spaceship")

    # User name input
    name = st.text_input("What is your name?")

    # Fleet menu
    fleet_list = ["iron", "cobalt", "manganese", "molybdenum", "nickel", "aluminium", "titanium"]

    if name:
        st.write(f"{name}, nice to meet you in my spaceship!")
        order = st.selectbox("Choose a resource to bring back to Earth:", fleet_list)
        quantity = st.number_input("How many units do you want to order?", min_value=1, step=1)

        price = 10000
        total = price * quantity

        if st.button("Submit Order"):
            st.success(f"Thank you very much, {name}! Your resource order cost is: ${total:,} for {order}. Enjoy your mission!")

# Run the app
spaceship_order_app()
