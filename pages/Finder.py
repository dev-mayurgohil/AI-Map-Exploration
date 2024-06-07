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