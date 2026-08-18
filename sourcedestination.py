import os
import urllib.parse

print("===== GOOGLE MAPS ROUTE =====")

source = input("Enter source: ")
destination = input("Enter destination: ")

# Create Google Maps URL
source = urllib.parse.quote(source)
destination = urllib.parse.quote(destination)

url = f"https://www.google.com/maps/dir/?api=1&origin={source}&destination={destination}"

print("\nOpening Google Maps...")

# Open Google Maps in the default browser
os.system(f'start "" "{url}"')