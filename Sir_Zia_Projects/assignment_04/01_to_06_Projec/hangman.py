import streamlit as st, random

word = random.choice(["cat", "dog", "bat"])
display = ["_"] * len(word)
attempts = 6

st.title("Hangman")
st.write(" ".join(display) + f" | Attempts left: {attempts}")
guess = st.text_input("Guess a letter: ").lower()

if guess:
    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                display[index] = guess
        st.write("✅ Correct!")
    else:
        attempts -= 1
        st.write("❌ Wrong!")

    st.write(" ".join(display) + f" | Attempts left: {attempts}")

    if "_" not in display:
        st.success(" You Win!")
    elif attempts == 0:
        st.error(f"❌ You Lose! Word: {word}")