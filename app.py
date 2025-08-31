
import streamlit as st
import random

st.title("✊✋✌ Rock Paper Scissors Game")

choices = ["Rock", "Paper", "Scissors"]

# User choice
user_choice = st.radio("Choose your move:", choices)

# Play button
if st.button("Play"):
    computer_choice = random.choice(choices)
    st.write(f"Computer chose: **{computer_choice}**")

    if user_choice == computer_choice:
        st.success("It's a Tie!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.success("🎉 You Win!")
    else:
        st.error("😢 You Lose!")
