import streamlit as st
import pandas as pd
from datetime import datetime

# Session storage
if "my_books" not in st.session_state:
    st.session_state.my_books = []

# Sidebar Navigation
st.sidebar.title("📚 BookTok Navigation")
section = st.sidebar.radio(
    "Go to section:",
    [
        "Rate a Book",
        "Book Tracker",
        "My Book Table"
    ]
)

# ---------- SECTION: Rate a Book ----------
if section == "Rate a Book":
    st.title("🌟 Rate a Book")

    with st.form("rate_form"):
        book_title = st.text_input("Book Title")
        start_date = st.date_input("📅 Start Date")
        end_date = datetime.now().date()
        st.markdown(f"📅 **End Date (Today):** {end_date}")

        uploaded_cover = st.file_uploader("📕 Upload Book Cover", type=["jpg", "png", "jpeg"])
        if uploaded_cover:
            st.image(uploaded_cover, width=150, caption="Book Cover")

        rating = st.slider("Overall Rating", 0.0, 5.0, step=0.5)
        spicy_rating = st.slider("🌶 Spicy Level", 0.0, 5.0, step=0.5)
        fluff_rating = st.slider("☁️ Fluff Level", 0.0, 5.0, step=0.5)
        comedy_rating = st.slider("😂 Comedy Level", 0.0, 5.0, step=0.5)
        format_read = st.radio("📖 Format", ["E-book", "Physical Book", "Audiobook"])

        fav_chapters = st.text_input("Favorite Chapters (e.g., Chapter 5, Chapter 12)")
        fav_quotes = st.text_area("Favorite Quotes (add memorable lines)")
        review = st.text_area("Short Review")

        visibility = st.radio("Visibility", ["Public", "Private"])
        submit_rating = st.form_submit_button("Submit")

        if submit_rating and book_title.strip():
            new_rating = {
                "title": book_title,
                "start_date": start_date,
                "end_date": end_date,
                "rating": rating,
                "spicy": spicy_rating,
                "fluff": fluff_rating,
                "comedy": comedy_rating,
                "format": format_read,
                "review": review,
                "fav_chapters": fav_chapters,
                "fav_quotes": fav_quotes,
                "visibility": visibility,
                "cover_image": uploaded_cover.name if uploaded_cover else None,
                "timestamp": datetime.now()
            }

            st.session_state.my_books.append(new_rating)
            st.success(f"✅ Your rating and notes for **{book_title}** have been saved!")

# ---------- SECTION: Book Tracker ----------
elif section == "Book Tracker":
    st.title("📖 Book Tracker")
    with st.form("track_form"):
        book = st.text_input("Book Title")
        status = st.selectbox("Status", ["Want to Read", "Reading", "Finished"])
        track_submit = st.form_submit_button("Add to Tracker")
        st.subheader("Select a Genre")
        genres = ["Rom-Com", "Fantasy", "Dark Romance", "Contemporary", "Historical"]
        selected_genre = st.selectbox("Choose a genre", genres)
        st.success(f"📚 You selected the genre: {selected_genre}")

        st.markdown("---")

        st.subheader("✨ Choose Your Favorite Micro-Tropes")
        micro_tropes = [
            "Grumpy x Sunshine", "Fake Dating", "Enemies to Lovers", "Friends to Lovers",
            "Second Chance", "Only One Bed", "Slow Burn", "Forced Proximity",
            "Secret Royal", "Found Family", "Marriage of Convenience"
        ]
        selected_tropes = st.multiselect("Pick micro-tropes that appeal to you", micro_tropes)

        if selected_tropes:
            st.success("💘 You vibe with: " + ", ".join(selected_tropes))

        if track_submit and book.strip():
            st.session_state.my_books.append({
                "title": book,
                "status": status,
                "visibility": "Private",
                "timestamp": datetime.now()
            })
    st.success(f"Added: {book}")

# ---------- SECTION: My Book Table ----------
elif section == "My Book Table":
    st.title("📋 Your Book Table")
    if st.session_state.my_books:
        df = pd.DataFrame(st.session_state.my_books).fillna("-")
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No entries yet.")
