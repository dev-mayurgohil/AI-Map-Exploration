import streamlit as st

def main():
    st.set_page_config(page_title="Bhugol Khoj ", page_icon=":earth_americas:")

    st.title("Bhugol Khoj")
    st.markdown("""
        <div style="display: flex; align-items: center;">
            <div>
                Your tool for exploring textual landscapes and uncovering hidden geographical insights!
            </div>
            <div style="margin-left: auto;">
                <img src="https://c.tenor.com/nCaqDCZtDPYAAAAd/tenor.gif"alt="Animated Globe" width="300" height="200">
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.write(
        """
        Bhugol Khoj  is a user-friendly web application designed to analyze text input and extract contextual locations. 
        By leveraging advanced natural language processing (NLP) techniques, Bhugol Khoj  identifies locations mentioned 
        within the text and plots them on an interactive map, providing users with a visual representation of the geographical 
        context embedded in their textual data.
        """
    )

    if st.button("Explore Bhugol Khoj "):
        st.page_link("pages/Analysis.py", label="Get Started")


if __name__ == "__main__":
    main()
