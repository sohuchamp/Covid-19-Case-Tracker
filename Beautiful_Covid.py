import requests
from bs4 import BeautifulSoup


def process_data(url: str) -> list:
    result = requests.get(url)
    src = result.text
    soup = BeautifulSoup(src, "html.parser")
    spans = list(soup.find_all('span'))
    spans = [str(x) for x in spans]
    #print(spans)
    return [spans[3][24::].strip('</span>') + ' cases ', spans[4][6::].strip('</span>') + ' deaths']


def scrape_data(place: str) -> str:
    countries = {'turkey':'https://www.worldometers.info/coronavirus/country/turkey/',
                 'guatemala':'https://www.worldometers.info/coronavirus/country/guatemala',
                 'japan':'https://www.worldometers.info/coronavirus/country/japan/',
                 'argentina':'https://www.worldometers.info/coronavirus/country/argentina/',
                 'colombia':'https://www.worldometers.info/coronavirus/country/colombia/',
                 'south africa':'https://www.worldometers.info/coronavirus/country/south-africa/',
                 'morocco':'https://www.worldometers.info/coronavirus/country/morocco/',
                 'egypt':'https://www.worldometers.info/coronavirus/country/egypt/',
                 'drcongo':'https://www.worldometers.info/coronavirus/country/democratic-republic-of-the-congo/',
                 'nigeria':'https://www.worldometers.info/coronavirus/country/nigeria/',
                 'somalia': 'https://www.worldometers.info/coronavirus/country/somalia',
                 'china':'https://www.worldometers.info/coronavirus/country/china/',
                 'russia':'https://www.worldometers.info/coronavirus/country/russia/',
                 'pakistan' : 'https://www.worldometers.info/coronavirus/country/pakistan/',
                 'indonesia': 'https://www.worldometers.info/coronavirus/country/indonesia/',
                 'vietnam' : 'https://www.worldometers.info/coronavirus/country/viet-nam/',
                 'thailand': 'https://www.worldometers.info/coronavirus/country/thailand/',
                 'norway' : 'https://www.worldometers.info/coronavirus/country/norway/',
                 'saudi arabia': 'https://www.worldometers.info/coronavirus/country/saudi-arabia/',
                 'israel': 'https://www.worldometers.info/coronavirus/country/israel/',
                 'switzerland': 'https://www.worldometers.info/coronavirus/country/switzerland/',
                 'denmark': 'https://www.worldometers.info/coronavirus/country/denmark/',
                 'uae': 'https://www.worldometers.info/coronavirus/country/united-arab-emirates/',
                 'south korea': 'https://www.worldometers.info/coronavirus/country/south-korea/',
                 'greece' : 'https://www.worldometers.info/coronavirus/country/greece/',
                 'portugal' : 'https://www.worldometers.info/coronavirus/country/portugal/',
                 'ukraine' : 'https://www.worldometers.info/coronavirus/country/ukraine/',
                 'austria' : 'https://www.worldometers.info/coronavirus/country/austria/',
                 'poland' : 'https://www.worldometers.info/coronavirus/country/poland/',
                 'sweden' : 'https://www.worldometers.info/coronavirus/country/sweden/',
                 'kazakhstan' : 'https://www.worldometers.info/coronavirus/country/kazakhstan/'
    }
    # [poland, sweden, norway, kazakhstan]
    # add deaths, hospital cases, and graphs (forecasts)
    # About US!
    if place.lower() in countries:
        simple = place.lower()
        writing = process_data(countries[simple])
        return writing[0] + ' and ' + writing[1] + ' in ' + place
    else:
        return 'could not find place with that name'
