import streamlit as st
import pyperclip

st.set_page_config(
    page_title="Multipage App",
    page_icon=":tada:",
)

st.title("Coordinates Converter")
st.sidebar.success("Select a page above.")
# -------------CONVERTER -------------
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Enter coordinates in the format Decimal Degrees (DD) e.g 53,80262°N 10,95388°O", st.session_state["my_input"])
submit = st.button("Submit")

if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered:", my_input)

if my_input:
    # Clean up the input string
    my_input = my_input.replace(',', '')
    my_input = my_input.replace('°N', '')
    my_input = my_input.replace('°O', '')

    # Split the input string into latitude and longitude
    coordinates = my_input.split()
    if len(coordinates) == 2:
        latitude_dd, longitude_dd = map(float, coordinates)

        # Convert latitude and longitude to the desired format
        latitude_gmaps = latitude_dd / 100000
        longitude_gmaps = longitude_dd / 100000

        # Format coordinates for Google Maps
        coordinates_gmaps = f"{latitude_gmaps:.5f}, {longitude_gmaps:.5f}"

        # Output the formatted coordinates
        st.write('Coordinates for Google Maps:', f"<strong>{coordinates_gmaps}</strong>", unsafe_allow_html=True)

        # Add a "Copy to Clipboard" button
        def copy_to_clipboard(text):
            pyperclip.copy(text)
            st.success("Copied to clipboard!")


        # Create a button
        if st.button("Copy Coordinates"):
            copy_to_clipboard(coordinates_gmaps)
    else:
        st.write("Please enter the coordinates in the correct format e.g 53,80262°N 10,95388°O.")



