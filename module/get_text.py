import streamlit as st


def input_text() -> str:
    """
    text widget
    Returns:
        str
    """
    input_text = st.text_input(label="You: ", value="", key="input")
    return input_text
