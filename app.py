# Streamlit App: Hotel Intel Bot
# Input: Hotel Name + URL | Output: Profile Info + Mews Pitch

import streamlit as st
import requests
from bs4 import BeautifulSoup
import openai
import os

# --- Configuration ---
openai.api_key = st.secrets["OPENAI_API_KEY"]  # Set in Streamlit secrets

# --- Functions ---
def get_profile_info(hotel_name, url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        rating = soup.select_one('div.b5cd09854e.d10a6220b4')
        rating = rating.text.strip() if rating else 'N/A'

        highlights = soup.select('div.b978843432')
        highlight_texts = [item.text.strip() for item in highlights[:5]]

        profile = {
            'name': hotel_name,
            'url': url,
            'rating': rating,
            'highlights': highlight_texts or ['Wellness', 'Mountain view', 'Family-friendly']
        }
        return profile
    except Exception as e:
        return {'error': f"Error fetching hotel data: {e}"}


def generate_pitch(profile):
    prompt = f"""
    Hotel Profile:
    Name: {profile.get('name')}
    URL: {profile.get('url')}
    Rating: {profile.get('rating')}
    Highlights: {', '.join(profile.get('highlights', []))}

    Based on this information, answer the following:
    1. What type of guest likely stays here?
    2. What are the property's key selling points?
    3. How should Mews pitch their property management system to this hotel?
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"OpenAI error: {e}"


# --- Streamlit UI ---
st.set_page_config(page_title="Hotel Intel Bot", layout="centered")
st.title("🏨 Hotel Intel Bot")
st.markdown("Enter a hotel name and its website or Booking.com URL to get sales insights.")

hotel_name = st.text_input("Hotel Name")
hotel_url = st.text_input("Hotel URL (Booking.com or official site)")

if st.button("Generate Insight") and hotel_name and hotel_url:
    with st.spinner("Fetching and analyzing hotel data..."):
        profile = get_profile_info(hotel_name, hotel_url)

        if 'error' in profile:
            st.error(profile['error'])
        else:
            st.subheader("🔎 Hotel Profile")
            st.write(f"**Name:** {profile['name']}")
            st.write(f"**Rating:** {profile['rating']}")
            st.write(f"**Highlights:** {', '.join(profile['highlights'])}")

            st.subheader("💡 Mews Sales Insight")
            pitch = generate_pitch(profile)
            st.write(pitch)
else:
    st.info("Please enter both hotel name and URL to get started.")
