import requests
import matplotlib.pyplot as plt
import datetime
import pandas as pd



lat = 20.8625
lon = 92.3050
today = datetime.date.today()
monthago = today - datetime.timedelta(days=30)
strtime = monthago.strftime("%Y-%m-%d")
endtime = today.strftime("%Y-%m-%d")
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&start={strtime}T00:00:00Z&end={endtime}T23:59:59Z"
response = requests.get(url)
data = response.json()

#processing data with pandas
df = pd.DataFrame({
    'date': pd.to_datetime(data['daily']['time']),
    'max_temp': data['daily']['temperature_2m_max'],
    'min_temp': data['daily']['temperature_2m_min']
})
df['avg_temp'] = (df['max_temp'] + df['min_temp']) / 2
#creating visualization
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['avg_temp'], marker='o', label='Average Temperature')
plt.title('Average Daily Temperature in Teknaf (Last 30 Days)')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

