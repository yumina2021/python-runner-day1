import streamlit as st
import sys
import io
import contextlib

st.set_page_config(page_title="My First Python Runner")

st.title("My First Python Runner")

default_code = "print('Hello, Antigravity!')"
code_input = st.text_area("Python Code", value=default_code, height=200)

if st.button("実行"):
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()
    
    try:
        with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
            exec(code_input, globals())
        
        output = stdout_capture.getvalue() + stderr_capture.getvalue()
        st.code(output)
        
    except Exception as e:
        st.error(f"エラー: {e}")
