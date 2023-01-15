import streamlit as st
import pyshorteners
import validators

st.write("""
<style>
footer, header {
    display: none !important;
}
.css-1offfwp img {
    position: fixed;
    bottom: 50px;
    left: calc(50% - 50px);
}
.css-1offfwp img {
    width: 100px;
}
</style>
""", unsafe_allow_html=True)

s = pyshorteners.Shortener()
long_url = st.text_input("Input link")

if long_url:
    if not validators.url(long_url):
        if not long_url.startswith("http"):
            long_url = "http://" + long_url
    short_url = s.tinyurl.short(long_url)
    st.success(f"Short link : {short_url}")

st.markdown("[![Foo](https://raw.githubusercontent.com/Damarcreative/Shortlink-Streamlit/main/gitlogo.png)](https://github.com/Damarcreative/Shortlink-Streamlit)")
