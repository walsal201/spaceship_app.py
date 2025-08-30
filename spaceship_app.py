import streamlit as st

def spaceship_order_app():
    st.set_page_config(page_title="Walsal201 Spaceship", page_icon="🛸")
    st.title("🛸 Welcome to Walsal201 Spaceship")

    name = st.text_input("What is your name?")
    fleet_prices = {
        "iron": 10000,
        "cobalt": 12000,
        "manganese": 9500,
        "molybdenum": 15000,
        "nickel": 11000,
        "aluminium": 9000,
        "titanium": 18000
    }

    if name:
        st.markdown(f"""
        ### 👋 Greetings, {name}!
        Welcome aboard the **Walsal201 Spaceship**, your interstellar gateway to Earth's most valuable resources.

        Below you'll find a curated fleet menu of rare metals and minerals.  
        You can select **multiple items**, specify quantities, and place your order for delivery back to Earth.

        Let's get your mission started! 🌍🚀
        """)

        st.subheader("🧾 Resource Selection")
        order_summary = {}
        total_cost = 0

        with st.form("order_form"):
            for item, price in fleet_prices.items():
                qty = st.number_input(f"{item.capitalize()} (${price:,} per unit)", min_value=0, step=1, key=item)
                if qty > 0:
                    order_summary[item] = qty
                    total_cost += qty * price

            submitted = st.form_submit_button("Submit Order")

        if submitted:
            st.success(f"🛒 Thank you {name}! Here's your order summary:")
            for item, qty in order_summary.items():
                st.write(f"- {qty} units of {item} @ ${fleet_prices[item]:,} each")
            st.write(f"**💰 Total Cost:** ${total_cost:,}")
            st.balloons()

# Run the app
spaceship_order_app()
