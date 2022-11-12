# create a tkinter GUI application to know the 
# weather and temperature from a given latitude and longitude

from tkinter import *
import tkinter as tk

import json
import requests
from tkinter import messagebox


 
def GetWeather():
    url = "https://api.tomorrow.io/v4/timelines"
    querystring = {
    "location":txtLongitude.get()+", "+txtLatitude.get(),
    "fields":["temperature"],
    "units":"metric",
    "timesteps":"current",
    "apikey":"K4gXKOMBGeonxlkFdMJlUlC023gUU7n3"}
    response = requests.request("GET", url, params=querystring)
    myData = json.loads(response.text)
    temp=myData["data"]["timelines"][0]["intervals"][0]["values"]["temperature"]
    messagebox.showinfo("Weather App","Current temperature is "+str(temp) +" C")
 
root = tk.Tk()
root.title("Weather App")
Module = Label(root, text = "Weather App", font =("arial",17,"bold"))
Module.grid(row = 0, column = 0, columnspan = 2, padx = 5, sticky = W)
 
lblLatitude = Label(root, text = "Enter the Latitude")
lblLatitude.grid(row = 1, column = 0, columnspan = 1, padx = 5, sticky = W)
 
txtLatitude = Entry(root, width = 50)
txtLatitude.grid(row=1,column = 1)
 
lblLongitude = Label(root, text = "Enter the Longitude")
lblLongitude.grid(row = 2, column = 0, columnspan = 1, padx = 5, sticky = W)
 
txtLongitude = Entry(root, width = 50)
txtLongitude.grid(row=2,column = 1, columnspan = 1, padx = 5, sticky = W)
 
btnSubmit = Button(root, text = "Submit", command = GetWeather)
btnSubmit .grid(row=7, columnspan = 3, pady=10)
 
root.mainloop()