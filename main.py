import requests
import json
import os

city = input("Enter Your City: ")

url = f"http://api.weatherapi.com/v1/current.json?key=b38d0f4f94d14d78a3b84325230207&q={city}"

r = requests.get(url)
# print(r.text)
weather_dict = json.loads(r.text)
temp = weather_dict["current"]["temp_c"]
print(temp)
command = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('The current temperature of''{city}''{temp}')"
os.system(command)