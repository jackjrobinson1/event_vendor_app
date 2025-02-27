import streamlit as st

def main():
    st.set_page_config(page_title="Event Vendor App", layout="centered")

    # Home Screen UI
    st.title("Find Vendors for Your Event")
    location = st.text_input("Enter your location or event area")

    # Categories
    st.subheader("Choose a category")
    categories = ["DJs", "MCs", "Venues", "Decorators", "Catering", "Kids Parties"]
    selected_category = st.radio("Categories", categories, horizontal=True)

    st.subheader(f"Top {selected_category} Near You")

    # Sample Vendor Listings
    vendors = [
        {"name": "DJ SoundWave", "rating": "⭐ 4.8", "contact": "📞 07812345678"},
        {"name": "MC Vibes", "rating": "⭐ 4.7", "contact": "📞 07456789123"},
        {"name": "Grand Banquet Hall", "rating": "⭐ 4.9", "contact": "📞 07333445566"}
    ]

    for vendor in vendors:
        with st.expander(f"{vendor['name']} {vendor['rating']}"):
            st.write("📍 Location: London, UK")
            st.write("📧 Email: contact@vendor.com")
            st.write(vendor["contact"])
            st.button(f"Add {vendor['name']} to Event Checklist", key=vendor['name'])

    # Event Checklist Section
    st.subheader("Your Event Checklist ✅")
    checklist_items = ["DJ Confirmed ✅", "Venue Pending ⏳"]
    for item in checklist_items:
        st.write("- " + item)

    st.button("Finalize Event Planning")

if __name__ == "__main__":
    main()
