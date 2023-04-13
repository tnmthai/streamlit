import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.info(
    """
    - Web App URL: https://lincolnagritech.streamlit.app/
   
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Thai Tran: Thai.Tran@
    """
)

# Customize page title
st.title("Lincoln Agritech Geospatial Applications")

st.markdown(
    """
    An online interactive mapping tool to display basic vegetative metrics available over Canterbury.
    """
)

st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template) or [use it as a template](https://github.com/giswqs/streamlit-multipage-template/generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True, center=(-43.525650, 172.639847), zoom=6.25)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
