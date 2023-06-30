
import streamlit as st


def count_words_and_letters(text):
    """Counts the number of words and letters in a string."""
    words = text.split()
    letters = len(text)
    return words, letters


def main():
    """Main function."""
    st.header("Word Counter")
    text = st.text_input("Enter text here: ")
    words, letters = count_words_and_letters(text)
    st.write("Number of words:", len(words))
    st.write("Number of letters:", letters)


if __name__ == "__main__":
    main()

