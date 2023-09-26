# Import necessary libraries
import streamlit as st

def determine_pizza(age, years_of_school, weight, height, continent, interests):
    """
    Determines the type of pizza based on user's quantitative and categorical details.
    """
    score = age + years_of_school + weight + height

    if continent == "Asia":
        score += 20
    elif continent == "Africa":
        score += 40
    elif continent == "North America":
        score += 60
    elif continent == "South America":
        score += 80
    elif continent == "Europe":
        score += 100
    elif continent == "Australia":
        score += 120
    elif continent == "Antarctica":
        score += 140

    if 'Adventure' in interests:
        score += 15
    if 'Music' in interests:
        score += 10
    if 'Reading' in interests:
        score += 5
    if 'Sports' in interests:
        score += 7
    if 'Art' in interests:
        score += 12

    if score < 200:
        return 'Margherita Pizza - A timeless classic!'
    elif score < 300:
        return 'Pepperoni Pizza - Spicy and full of character!'
    elif score < 400:
        return 'BBQ Chicken Pizza - A delightful mix of flavors!'
    else:
        return 'Veggie Pizza - Rich and diverse, like your experiences!'

# Streamlit App
st.title("What Kind of Pizza Are You?")

st.write("Discover which type of pizza resonates with your personality based on a mix of interests and personal details.")

age = st.slider("How old are you?", min_value=10, max_value=100, value=25, step=1)
years_of_school = st.slider("Years of school completed?", min_value=1, max_value=25, value=12, step=1)
weight = st.slider("Your weight (in kg)?", min_value=30, max_value=200, value=60, step=1)
height = st.slider("Your height (in cm)?", min_value=100, max_value=250, value=160, step=1)
continent = st.selectbox("Which continent are you from?", 
                         ["Asia", "Africa", "North America", "South America", "Europe", "Australia", "Antarctica"])

interests = st.multiselect('Select your interests', 
                           ['Adventure', 'Music', 'Reading', 'Sports', 'Art'], 
                           default=['Adventure'])

result = determine_pizza(age, years_of_school, weight, height, continent, interests)
st.subheader('You are:')
st.write(result)

st.write("Note: This is a fun app and results are just for entertainment purposes.")

if st.button("Retake"):
    st.experimental_rerun()

