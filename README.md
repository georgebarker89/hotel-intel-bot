# 🏨 Hotel Intel Bot

Hotel Intel Bot is a Streamlit app that helps sales teams research and prepare tailored sales pitches for hotels — powered by OpenAI. Just input the hotel name and its website or Booking.com URL, and the bot returns:

- Hotel profile summary (rating, highlights)
- Estimated guest demographics
- Key selling points
- A custom Mews PMS pitch for the property

---

## 🚀 Features

- 🌐 Scrapes public hotel data from Booking.com or hotel websites
- 🤖 Uses GPT-4 to analyze and generate smart sales recommendations
- ⚡️ Simple UI built with Streamlit for fast access and usability

---

## 🛠 How to Use (Locally or on Streamlit Cloud)

### Option 1: Use via [Streamlit Cloud](https://streamlit.io/cloud)

1. Fork or clone this repo
2. Push to your own GitHub account
3. Log into [Streamlit Cloud](https://streamlit.io/cloud) and create a new app
4. Set up your API key in **Secrets**:
   ```
   OPENAI_API_KEY = "your-openai-key-here"
   ```

### Option 2: Run Locally

```bash
# Clone repo
git clone https://github.com/yourusername/hotel-intel-bot.git
cd hotel-intel-bot

# Install dependencies
pip install -r requirements.txt

# Set OpenAI key (one-time setup)
export OPENAI_API_KEY="your-key-here"

# Run the app
streamlit run app.py
```

---

## 📄 Requirements

- Python 3.8+
- Streamlit
- OpenAI Python SDK
- BeautifulSoup4
- Requests

---

## ⚠️ Disclaimer

This app scrapes publicly available data and is intended for internal demo or educational use. Always check site terms before deploying commercially.

---

## 📬 Questions or Improvements?

Feel free to open an issue or contribute a pull request!
