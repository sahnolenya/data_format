import json
import csv
from datetime import datetime


json_file_path = 'data/Saint-Petersburg24.09.06.json'
csv_file_path = 'data/weather_data_08_09_2024.csv'

def extract_weather_data(json_path, output_csv, target_date):
    
    with open(json_path, 'r', encoding='utf-8') as file:
        weather_data = json.load(file)

    
    hourly_data = []
    for forecast in weather_data.get("forecasts", []):
        if forecast.get("date") == target_date:
            for hour in forecast.get("hours", []):
                hourly_data.append({
                    "hour": hour.get("hour"),
                    "condition": hour.get("condition"),
                    "pressure_mm": hour.get("pressure_mm")
                })

    
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["hour", "condition", "pressure_mm"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(hourly_data)

    print(f"Данные сохранены в файл {output_csv}")


target_date = "2024-09-08"


extract_weather_data(json_file_path, csv_file_path, target_date)
