
import streamlit as st
from PIL import Image


# Centered title using HTML and Markdown
st.markdown("<h1 style='text-align: center;'>The Story Behind the Project</h1>", unsafe_allow_html=True)


# Set the title of the web app
#Picture
image = Image.open('/Users/jessicaseo/Documents/Projects/Forecasting Streetcar Delays/Streamlit/pages/profilepic.jpg')

#st.markdown("<h1 style='text-align: center; color: grey;'></h1>", unsafe_allow_html=True)


col1, col2, col3, col4 = st.columns(4)
with col2:

    st.image(image,width=400)

#Creator
st.write("\n")
st.write("Hey everyone! I'm Jessica Seo, and I'm delighted to welcome you to my dashboard. ")
st.write("This project was inspired by my personal curiosity as a resident of downtown Toronto." 
        " I often experienced the frustration of public transit delays, even while using transit apps. "
        " I preprocessed the dataset, analyzing the correlations between delays and features like time, streetcar route, and weather to find answers."
        " Join me in forecasting streetcar delays with a machine learning model I've created. "
        )

st.write("\n")

st.write("Feel free to explore my GitHub for a deeper understanding of the project and reach out on LinkedIn. "
        " Happy Communiting! ")

git_image_url = "https://github.githubassets.com/assets/GitHub-Logo-ee398b662d42.png"
git_link_url = "https://github.com/jessseo1246/Forecasting_TTC_Streetcar_Delays.git"

image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Logo.svg.original.svg"
link_url = "https://www.linkedin.com/in/jessseo1246/"

st.markdown(
    f"<div style='display: flex;'>"
    f"<div style='margin-right: 10px;'><a href='{git_link_url}' target='_blank'><img src='{git_image_url}' width='100'/></a></div>"
    f"<div style='margin-left: 10px;'><a href='{link_url}' target='_blank'><img src='{image_url}' width='100'/></a></div>"
    f"</div>",
    unsafe_allow_html=True
)
