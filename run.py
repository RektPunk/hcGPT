import streamlit as st
from datetime import datetime
from streamlit_chat import message

from module.state import initialize_state
from module.get_text import input_text
from module.util import random_hash
from module.get_response import query, summary_chats


st.header("hcgpt - demo")

initialize_state()

user_input = input_text()
if user_input:
    output = query(
        input_params={
            "inputs": {
                "past_user_inputs": st.session_state.past,
                "generated_responses": st.session_state.generated,
                "text": user_input,
            },
            "parameters": {"repetition_penalty": 1.33},
        }
    )
    st.session_state["past"].append(user_input)
    st.session_state["generated"].append(output)


if st.session_state["generated"] != []:
    for _past_text, _generated_text in zip(
        reversed(st.session_state["past"]), reversed(st.session_state["generated"])
    ):
        message(
            message=_past_text,
            is_user=True,
            key=random_hash(text=_past_text, time=str(datetime.now())),
        )
        message(
            message=_generated_text,
            key=random_hash(text=_generated_text, time=str(datetime.now())),
        )

if st.button(label="summarise"):
    st.text_area(label="", value=summary_chats())
