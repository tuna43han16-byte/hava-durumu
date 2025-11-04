import requests
import sys

def get_weather_data(city):
    base_url = f"https://wttr.in/{city}?format=j1"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Hatasi: Sehir bulunamadi veya API sorunu.")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Baglanti Hatasi: Internet baglantinizi kontrol edin.")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Bir Hata Olustu: {err}")
        return None

def display_weather(data, city):
    if not data:
        return

    try:
        current_condition = data['current_condition'][0]
        weather_desc = current_condition['weatherDesc'][0]['value']
        temp_c = current_condition['temp_C']
        feels_like_c = current_condition['FeelsLikeC']
        humidity = current_condition['humidity']
        wind_speed = current_condition['windspeedKmph']
        
        print("\n" + "=" * 30)
        print(f" {city.upper()} Icin Hava Durumu Raporu")
        print("=" * 30)
        
        print(f" Durum:         {weather_desc}")
        print(f" Sicaklik:      {temp_c}°C")
        print(f" Hissedilen:    {feels_like_c}°C")
        print(f" Nem Orani:     %{humidity}")
        print(f" Ruzgar Hizi:   {wind_speed} km/s")
        print("=" * 30)
        
        print("\n Bugunun Tahmini:")
        today_forecast = data['weather'][0]
        print(f" Min Sicaklik:  {today_forecast['mintempC']}°C")
        print(f" Max Sicaklik:  {today_forecast['maxtempC']}°C")
        
        hourly = today_forecast['hourly']
        print("\n Saatlik Durum:")
        print("  Saat  | Sicaklik | Durum")
        print("  ------|----------|-----------------")
        for hour_data in [hourly[2], hourly[4], hourly[6]]: # 06:00, 12:00, 18:00
            time_str = str(int(hour_data['time']) // 100).zfill(2) + ":00"
            temp_str = f"{hour_data['tempC']}°C".ljust(8)
            desc_str = hour_data['weatherDesc'][0]['value']
            print(f"  {time_str} | {temp_str} | {desc_str}")

    except (KeyError, IndexError, TypeError):
        print("API'den gelen veri yapisi beklenmedik. Veri ayrıştırılamadı.")

def main():
    if len(sys.argv) > 1:
        city_name = " ".join(sys.argv[1:])
    else:
        city_name = input("Lutfen bir sehir adi girin (orn: Istanbul): ")
        
    if not city_name:
        print("Sehir adi girmediniz. Cikiliyor.")
        return
        
    weather_data = get_weather_data(city_name)
    
    if weather_data:
        display_weather(weather_data, city_name)

if __name__ == "__main__":
    main()
