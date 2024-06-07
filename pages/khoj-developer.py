# developers.py

import streamlit as st

def show():
    st.title("Meet the Developer")
    
    # Developer 1
    st.write(
        f"""
        <div style="margin-bottom: 40px;">
            <img src="https://avatars.githubusercontent.com/u/60852091?v=4" alt="Mayur Gohil" style="width: 100px; height: 100px; border-radius: 50%;">
            <div style="display: inline-block; vertical-align: middle;">
                <h3>Mayur Gohil</h3>
                <p><strong>   Transforming World usign AI</strong></p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    show()
