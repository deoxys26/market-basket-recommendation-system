import streamlit as st
import requests

# Title
st.title("Retail Recommendation System")

# Description
st.write(
    "Get product recommendations using "
    "Apriori Association Rule Mining"
)

# Input box
product = st.text_input(
    "Enter Product Name"
)

# Button
if st.button("Recommend"):

    # Empty input check
    if product.strip() == "":
        st.warning("Please enter a product name")

    else:

        try:

            # Send request safely
            response = requests.get(
                "http://127.0.0.1:8000/recommend",
                params={"product": product}
            )

            # Convert response to JSON
            data = response.json()

            st.subheader("Recommended Products")

            recommendations = data["recommendations"]

            # Show recommendations
            if recommendations:

                for item in recommendations:
                    st.write("•", item)

            else:
                st.write("No recommendations found")

        except Exception as e:

            st.error(
                f"Error connecting to backend: {e}"
            )