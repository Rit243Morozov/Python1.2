import requests

city = input("Введите название города: ")

url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    "q": city,
    "units": "metric",
    "lang": "ru",
    "appid": "79d1ca96933b0328e1c7e3e7a26cb347"
}

weather_data = requests.get(url, params=params).json()

temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
temperature_min = round(weather_data['main']['temp_min'])
temperature_max = round(weather_data['main']['temp_max'])
pressure = weather_data['main']['pressure']
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']
wind_deg = weather_data['wind']['deg']
weather_description = weather_data['weather'][0]['description']
clouds = weather_data['clouds']['all']
visibility = weather_data.get('visibility', 0) // 1000

wind_direction = ""
if 0 <= wind_deg < 90:
    wind_direction = "северо-восточный"
elif 90 <= wind_deg < 180:
    wind_direction = "юго-восточный"
elif 180 <= wind_deg < 270:
    wind_direction = "юго-западный"
else:
    wind_direction = "северо-западный"

wind_message = f"ветер {wind_direction}, {wind_speed} м/с"

print("=" * 40)
print(f"Город: {city}")
print("=" * 40)
print(f"Температура: {temperature}°C")
print(f"Ощущается как: {temperature_feels}°C")
print(f"Минимальная: {temperature_min}°C")
print(f"Максимальная: {temperature_max}°C")
print(f"Давление: {pressure} мм рт. ст.")
print(f"Влажность: {humidity}%")
print(f"{wind_message}")
print(f"Облачность: {clouds}%")
print(f"Видимость: {visibility} км")
print(f"Погода: {weather_description}")
print("=" * 40)