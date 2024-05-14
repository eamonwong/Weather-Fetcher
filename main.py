import tkinter as tk
import requests

API_KEY = "047313308e4ff618959465753ef430ac"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = round(data["main"]["temp"] - 273.15, 2)
        weather_label.config(text="Weather: " + weather)
        temp_label.config(text="Temperature: " + str(temperature) + " Celsius")
    else:
        weather_label.config(text="An error occurred.")

# Create main window
root = tk.Tk()
root.title("Weather App")

# Create widgets
city_label = tk.Label(root, text="Enter a city name:")
city_entry = tk.Entry(root)
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
weather_label = tk.Label(root, text="")
temp_label = tk.Label(root, text="")

# Arrange widgets using grid layout
city_label.grid(row=0, column=0)
city_entry.grid(row=0, column=1)
get_weather_button.grid(row=1, columnspan=2)
weather_label.grid(row=2, columnspan=2)
temp_label.grid(row=3, columnspan=2)

# Start the main event loop
root.mainloop()
