import requests
from lxml import html

def weather():
    
    url = 'https://weather.com/de-CH/weather/today/l/abe831aec41f7d9432bf812060276a8299e180c4e5a33f822acdbeb9715acc7c'
    page = requests.get(url)
    tree = html.fromstring(page.content)

    weather = tree.xpath('//div[@data-testid = "wxPhrase"]/text()')[0]
    temperature = tree.xpath('//span[@data-testid = "TemperatureValue"]/text()')[0]

    output = ("Ort: " + "Zürich" + "\n" + "Wetter: " + weather + ", " + temperature)
    return output
