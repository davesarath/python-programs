import bs4
import requests
import pandas

page_url="https://www.weather-forecast.com/locations/Kunnamangalam/forecasts/latest"

page= requests.get(page_url)
# print(page)
soup = bs4.BeautifulSoup(page.content,'lxml')       # you need to pip install "xml"
# print(soup)

contain_class="b-metar__table-container columns"

scor =  soup.find_all(class_=contain_class)
print(scor)

row_Container="b-metar-table__body"

data_table=scor[0].find(class_=row_Container)
station_name=[i.get_text() for i in data_table.find_all(class_="b-metar-table__weather-station-name")]
print(station_name)
weather=[i.get_text() for i in data_table.find_all(class_="b-metar-table__weather-text")]
print(weather)
temp =[i.get_text() for i in data_table.find_all(class_="b-metar-table__temperature-value")]
print(temp)

weather_table= pandas.DataFrame({
    "Place":station_name,
    "Temperature":temp,
    "Weather":weather,
})
print(weather_table)
# weather_table.to_csv("dat.csv")

