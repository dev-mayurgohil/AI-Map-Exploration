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
