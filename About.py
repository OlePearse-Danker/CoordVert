import streamlit as st

st.title("About")

"""
#### What does this website do?
"""

st.markdown('''
This Website prompts the user to enter coordinates in decimal degrees format (DD) through a command-line interface. 
It then cleans up the input string by removing commas and specific degree symbols.
After that, the input string is split into latitude and longitude values. 
These values are converted to a desired format for use with Google Maps. The latitude is divided by 100,000 
and the longitude is divided by 100,000.
Finally, the script formats the latitude and longitude into a string suitable for Google Maps. 

''')