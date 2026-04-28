import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Movie Recommender", layout="centered")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Dark Universe Background with overlay */
.stApp {
    background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.95)),
    url("https://images.unsplash.com/photo-1462331940025-496dfbfc7564");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Title */
.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #ff1a1a;
    text-shadow: 0 0 20px red;
}

/* Input box */
.stTextInput > div > div > input {
    background-color: rgba(0,0,0,0.8);
    color: white;
    border: 2px solid red;
}

/* Button */
div.stButton > button {
    background-color: rgba(0,0,0,0.9);
    color: red;
    border: 2px solid red;
    padding: 10px;
    border-radius: 10px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: red;
    color: black;
}

/* Text */
.result {
    color: #ffffff;
    font-size: 18px;
    padding: 6px;
}

/* Subheader */
h3 {
    color: #ff4d4d;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="title">🎬 HORROR MOVIE RECOMMENDER 👻</div>', unsafe_allow_html=True)

st.write("")

# ---------------- INPUT ----------------
movie_name = st.text_input("Enter movie name")

# ---------------- BUTTON ----------------
if st.button("🔮 Recommend Movies"):
    
    if movie_name:
        try:
            response = requests.get(
                "http://127.0.0.1:8000/recommend",
                params={"movie": movie_name}
            )

            data = response.json()

            if "error" in data:
                st.error(data["error"])
            else:
                st.subheader("👻 Recommended Movies:")
                for movie in data["recommendations"]:
                    st.markdown(f'<div class="result">🩸 {movie}</div>', unsafe_allow_html=True)

        except:
            st.error("⚠️ API not running. Start FastAPI first!")

    else:
        st.warning("⚠️ Please enter a movie name")