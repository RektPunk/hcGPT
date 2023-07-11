from typing import List
import streamlit as st


def initialize_state() -> None:
    """
    Initialize params
    """
    if "generated" not in st.session_state:
        st.session_state["generated"]: List[str] = []

    if "past" not in st.session_state:
        st.session_state["past"]: List[str] = []
