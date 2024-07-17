---
title: code-Explanation
---
# Introduction

This document will walk you through the implementation of the Bhugol Khoj feature. Bhugol Khoj is a <SwmToken path="/pages/About.py" pos="12:9:11" line-data="            Bhugol Khoj is a user-friendly web application designed to analyze text input and extract contextual locations. ">`user-friendly`</SwmToken> web application designed to analyze text input and extract contextual locations. By leveraging advanced natural language processing (NLP) techniques, Bhugol Khoj identifies locations mentioned within the text and plots them on an interactive map, providing users with a visual representation of the geographical context embedded in their textual data.

We will cover:

1. The design and purpose of the About page.


2. The implementation of the Finder feature.


3. The introduction of the developer's page.


4. The creation of the Home page.

# About page

<SwmSnippet path="/pages/About.py" line="1">

---

The About page serves as an introduction to the Bhugol Khoj application. It explains what Bhugol Khoj is, how it works, why users should use it, and how to get started. It also includes a flowchart to visually represent the process of using Bhugol Khoj.

```python
import streamlit as st
from graphviz import Digraph

st.title("About Bhugol Khoj")
st.markdown(
   "Welcome to Bhugol Khoj (Geography Hunt) – your tool for exploring textual landscapes and uncovering hidden geographical insights!"
)

st.header("What is Bhugol Khoj?")
st.markdown(
   """
            Bhugol Khoj is a user-friendly web application designed to analyze text input and extract contextual locations. 
            By leveraging advanced natural language processing (NLP) techniques, Bhugol Khoj identifies locations mentioned 
            within the text and plots them on an interactive map, providing users with a visual representation of the geographical 
            context embedded in their textual data.
            """
)

st.header("How does it work?")
st.markdown(
   """
            1. **Input Text**: Users can input text directly into the application or upload a text file. This text could be 
               anything from articles, essays, or even social media posts.
            2. **Text Analysis**: Bhugol Khoj employs state-of-the-art NLP algorithms to analyze the input text. It detects 
               mentions of geographical locations, such as cities, countries, or landmarks.
            3. **Location Extraction**: The application extracts the most relevant contextual location from the input text. 
               This could be a city, country, or specific landmark mentioned within the text.
            4. **Geographical Visualization**: Bhugol Khoj then plots the extracted location on an interactive map, allowing 
               users to explore the geographical context of the text visually.
            5. **Additional Insights**: Users can also view additional insights, such as the origin country of the text (if 
               different from the contextual location) and the translated text (if the original text is not in English).
            """
)

st.header("Why use Bhugol Khoj?")
st.markdown(
   """
            - **Discover Hidden Geographical Insights**: Uncover geographical contexts embedded within textual data.
            - **Visualize Textual Landscapes**: Transform text into interactive maps for a richer understanding of location references.
            - **Explore Global Connections**: Gain a deeper understanding of the global context within your text.
            - **Streamlined User Experience**: Enjoy a user-friendly interface for seamless text analysis and visualization.
            """
)

st.header("Get Started with Bhugol Khoj")
st.markdown(
   """
            Ready to explore the world through text? Simply input your text or upload a text file, 
            and let Bhugol Khoj unveil the geographical insights within!
            """
)
st.header("Bhugol Khoj Flow")
dot = Digraph('flowchart', node_attr={'shape': 'plaintext'})
dot.edge_attr.update(arrowhead='vee', arrowsize='1.5')
dot.attr(rankdir='LR')
dot.attr(ranksep='0')
# Add nodes to the flowchart
dot.node('A', 'Input Text')
dot.node('B', 'Language Identification')
dot.node('C', 'Text Analysis')
dot.node('D', 'Location Extraction')
dot.node('E', 'Geographical Visualization')
dot.node('F', 'Additional Insights')

# Add edges between nodes
dot.edges(['AB', 'BC', 'CD', 'DE', 'EF'])

# Render the flowchart
st.graphviz_chart(dot)

```

---

</SwmSnippet>

# Finder feature

<SwmSnippet path="/pages/Finder.py" line="1">

---

The Finder feature is the core of the Bhugol Khoj application. It allows users to input text directly into the application or upload a text file. The application then uses NLP algorithms to analyze the input text, detect mentions of geographical locations, and extract the most relevant contextual location. This location is then plotted on an interactive map. The Finder feature also provides additional insights, such as the origin country of the text (if different from the contextual location) and the translated text (if the original text is not in English).

```python
import streamlit as st
from langdetect import detect
from deep_translator import GoogleTranslator
import folium
from collections import Counter
import spacy
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim

# Function to detect language of text
def show():
    def detect_language(text):
        try:
            lang_code = detect(text)
            return lang_code
        except:
            return None

    # Function to get country name from language code
    def get_country_from_lang(lang_code):
        lang_country_map = {
            'hi': 'India',
            'es': 'Spain',          # Spanish
            'fr': 'France',         # French
            'de': 'Germany',        # German
            'it': 'Italy',          # Italian
            'ru': 'Russia',         # Russian
            'ja': 'Japan',          # Japanese
            'ko': 'South Korea',    # Korean
            'zh': 'China',          # Chinese
            'ur': 'Pakistan',       # Urdu
            'ar': 'Saudi Arabia',
            'dz' : 'Bhutan',
        }
        return lang_country_map.get(lang_code, 'Unknown')

    # Function to translate text and find relevant location
    def translate_and_map(input_text):
        detected_lang = detect_language(input_text)
        if detected_lang:
            if detected_lang!='en':
                translated_text = GoogleTranslator(source=detected_lang, target='en').translate(input_text)
            else:
                translated_text = input_text
            nlp = spacy.load("en_core_web_sm")
            doc = nlp(translated_text)
            locations = [ent.text for ent in doc.ents if ent.label_ == 'GPE']
            if locations:
                location_counts = Counter(locations)
                most_common_location = location_counts.most_common(1)[0][0]
                return most_common_location, get_country_from_lang(detected_lang), translated_text
        return None, None, None

    def get_coordinates(location):
        geolocator = Nominatim(user_agent="location_plotter")
        try:
            location_info = geolocator.geocode(location)
            if location_info:
                return location_info.latitude, location_info.longitude
        except Exception as e:
            print(f"Error getting coordinates for {location}: {e}")
        return None, None

    # Streamlit app title
    st.title("Bhugol Khoj")

    # Text input or file upload option
    option = st.sidebar.radio("Choose an option:", ("Enter Text", "Upload File"))

    if option == "Enter Text":
        input_text = st.text_area("Enter your text here:")
        if st.button("Process"):
            contextual_location, origin_country, translated_text = translate_and_map(input_text)
            if contextual_location:
                if origin_country != 'Unknown':
                    st.write("**Origin country location:**", origin_country)
                st.write("**Most relevant location:**", contextual_location)
                if origin_country!='Unknown' and translated_text:
                    st.write("**Translated text:**")
                    st.write(translated_text)
                m = folium.Map(location=[0, 0], zoom_start=2)
                folium.Marker(get_coordinates(contextual_location), popup=contextual_location, icon=folium.Icon(color='green')).add_to(m)
                if origin_country != 'Unknown':
                    folium.Marker(get_coordinates(origin_country), popup=origin_country).add_to(m)
                folium_static(m)

    elif option == "Upload File":
        uploaded_file = st.file_uploader("Upload a TXT file:")
        if uploaded_file is not None:
            file_contents = uploaded_file.getvalue().decode("utf-8")
            st.write("File content:")
            st.write(file_contents)
            if st.button("Process"):
                contextual_location, origin_country, translated_text = translate_and_map(file_contents)
                if contextual_location:
                    if origin_country != 'Unknown':
                        st.write("**Origin country location:**", origin_country)
                    st.write("**Most relevant location:**", contextual_location)
                    if origin_country!='Unknown' and translated_text:
                        st.write("**Translated text:**")
                        st.write(translated_text)
                    m = folium.Map(location=[0, 0], zoom_start=2)
                    folium.Marker(get_coordinates(contextual_location), popup=contextual_location, icon=folium.Icon(color='green')).add_to(m)
                    if origin_country != 'Unknown':
                        folium.Marker(get_coordinates(origin_country), popup=origin_country).add_to(m)
                    folium_static(m)

if __name__ == "__main__":
    show() 
```

---

</SwmSnippet>

# Developer's page

<SwmSnippet path="/pages/khoj-developer.py" line="1">

---

The Developer's page introduces the developer of the Bhugol Khoj application. It includes a photo and a brief description of the developer.

```python
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

```

---

</SwmSnippet>

# Home page

<SwmSnippet path="/Home.py" line="1">

---

The Home page is the first page users see when they visit the Bhugol Khoj application. It provides a brief overview of what Bhugol Khoj is and what it does. It also includes a button that users can click to start using Bhugol Khoj.

```python
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
        st.page_link("pages/Finder.py", label="Get Started")


if __name__ == "__main__":
    main()

```

---

</SwmSnippet>

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBQUktTWFwLUV4cGxvcmF0aW9uJTNBJTNBZGV2LW1heXVyZ29oaWw=" repo-name="AI-Map-Exploration"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
