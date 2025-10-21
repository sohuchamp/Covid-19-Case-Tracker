import pandas as pd

# ***************** CODE CAN BE USED ON THE WEBSITE *****************
# ***************** THIS CODE BELONGS TO SOHAM SETHI AND ARUSH KHARE ****************
usa = ["usa", "america", "united states of america", "us", "united states", "estados unidos"]
britain = ["uk", "united kingdom", "great britain", "britain", "u.k.", "g.b.", "brit", "br"]
canada = ["canada", "can"]
india = ["india", "ind", "bharat", "hindustan"]
germany = ["german republic", "germany"]
france = ["france", "french republic", "fra", "fr"]
italy = ["italy", "italia", "italian republic"]
spain = ["españa", "spain", "spanish republic", "espana"]
brazil = ["brazilian republic", "brazil"]
mexico = ["mex", "mexican republic", "mexico"]
world = ["earth", "globe", "planet", "world", "global cases", "cases worldwide"]

place = ''


def external_input(string: str):
    global place
    place = string.lower()


"""def display_cases():
    if place in world:
        World()
        return "The data is from the New York Times"
    elif place in usa:
        USA()
        return "The data is from the New York Times"
    elif place in britain:
        UK()
        return "The data is from the New York Times"
    elif place in canada:
        Canada()
        return "The data is from the New York Times"
    elif place in india:
        India()
        return "The data is from the New York Times"
    elif place in germany:
        Germany()
        return "The data is from the New York Times"
    elif place in france:
        France()
        return "The data is from the New York Times"
    elif place in italy:
        Italy()
        return "The data is from the New York Times"
    elif place in spain:
        Spain()
        return "The data is from the New York Times"
    elif place in brazil:
        Brazil()
        return "The data is from the New York Times"
    elif place in mexico:
        Mexico()
        return "The data is from the New York Times"
    else:
        return "Could not find place with that name"
"""


def USA():
    dataframeUS = pd.read_html("https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html")
    """states = {
        "alabama": "https://www.nytimes.com/interactive/2020/us/alabama-coronavirus-cases.html",
        "alaska": "https://www.nytimes.com/interactive/2020/us/alaska-coronavirus-cases.html",
        "arizona": "https://www.nytimes.com/interactive/2020/us/arizona-coronavirus-cases.html",
        "arkansas": "https://www.nytimes.com/interactive/2020/us/arkansas-coronavirus-cases.html",
        "california": "https://www.nytimes.com/interactive/2020/us/california-coronavirus-cases.html",
        "colorado": "https://www.nytimes.com/interactive/2020/us/colorado-coronavirus-cases.html",
        "connecticut": "https://www.nytimes.com/interactive/2020/us/connecticut-coronavirus-cases.html",
        "delaware": "https://www.nytimes.com/interactive/2020/us/delaware-coronavirus-cases.html",
        "florida": "https://www.nytimes.com/interactive/2020/us/florida-coronavirus-cases.html",
        "georgia": "https://www.nytimes.com/interactive/2020/us/georgia-coronavirus-cases.html",
        "hawaii": "https://www.nytimes.com/interactive/2020/us/hawaii-coronavirus-cases.html",
        "idaho": "https://www.nytimes.com/interactive/2020/us/idaho-coronavirus-cases.html",
        "illinois": "https://www.nytimes.com/interactive/2020/us/illinois-coronavirus-cases.html",
        "indiana": "https://www.nytimes.com/interactive/2020/us/indiana-coronavirus-cases.html",
        "iowa": "https://www.nytimes.com/interactive/2020/us/iowa-coronavirus-cases.html",
        "kansas": "https://www.nytimes.com/interactive/2020/us/kansas-coronavirus-cases.html",
        "kentucky": "https://www.nytimes.com/interactive/2020/us/kentucky-coronavirus-cases.html",
        "louisiana": "https://www.nytimes.com/interactive/2020/us/louisiana-coronavirus-cases.html",
        "maine": "https://www.nytimes.com/interactive/2020/us/maine-coronavirus-cases.html",
        "maryland": "https://www.nytimes.com/interactive/2020/us/maryland-coronavirus-cases.html",
        "massachusetts": "https://www.nytimes.com/interactive/2020/us/massachusetts-coronavirus-cases.html",
        "michigan": "https://www.nytimes.com/interactive/2020/us/michigan-coronavirus-cases.html",
        "minnesota": "https://www.nytimes.com/interactive/2020/us/minnesota-coronavirus-cases.html",
        "mississippi": "https://www.nytimes.com/interactive/2020/us/mississippi-coronavirus-cases.html",
        "missouri": "https://www.nytimes.com/interactive/2020/us/missouri-coronavirus-cases.html",
        "montana": "https://www.nytimes.com/interactive/2020/us/montana-coronavirus-cases.html",
        "nebraska": "https://www.nytimes.com/interactive/2020/us/nebraska-coronavirus-cases.html",
        "nevada": "https://www.nytimes.com/interactive/2020/us/nevada-coronavirus-cases.html",
        "new hampshire": "https://www.nytimes.com/interactive/2020/us/new-hampshire-coronavirus-cases.html",
        "new jersey": "https://www.nytimes.com/interactive/2020/us/new-jersey-coronavirus-cases.html",
        "new mexico": "https://www.nytimes.com/interactive/2020/us/new-mexico-coronavirus-cases.html",
        "new york": "https://www.nytimes.com/interactive/2020/us/new-york-coronavirus-cases.html",
        "north carolina": "https://www.nytimes.com/interactive/2020/us/north-carolina-coronavirus-cases.html",
        "north dakota": "https://www.nytimes.com/interactive/2020/us/north-dakota-coronavirus-cases.html",
        "ohio": "https://www.nytimes.com/interactive/2020/us/ohio-coronavirus-cases.html",
        "oklahoma": "https://www.nytimes.com/interactive/2020/us/oklahoma-coronavirus-cases.html",
        "oregon": "https://www.nytimes.com/interactive/2020/us/oregon-coronavirus-cases.html",
        "pennsylvania": "https://www.nytimes.com/interactive/2020/us/pennsylvania-coronavirus-cases.html",
        "rhode island": "https://www.nytimes.com/interactive/2020/us/rhode-island-coronavirus-cases.html",
        "south carolina": "https://www.nytimes.com/interactive/2020/us/south-carolina-coronavirus-cases.html",
        "south dakota": "https://www.nytimes.com/interactive/2020/us/south-dakota-coronavirus-cases.html",
        "tennessee": "https://www.nytimes.com/interactive/2020/us/tennessee-coronavirus-cases.html",
        "texas": "https://www.nytimes.com/interactive/2020/us/texas-coronavirus-cases.html",
        "utah": "https://www.nytimes.com/interactive/2020/us/utah-coronavirus-cases.html",
        "vermont": "https://www.nytimes.com/interactive/2020/us/vermont-coronavirus-cases.html",
        "virginia": "https://www.nytimes.com/interactive/2020/us/virginia-coronavirus-cases.html",
        "washington": "https://www.nytimes.com/interactive/2020/us/washington-coronavirus-cases.html",
        "d.c.": "https://www.nytimes.com/interactive/2020/us/washington-dc-coronavirus-cases.html",
        "west virginia": "https://www.nytimes.com/interactive/2020/us/west-virginia-coronavirus-cases.html",
        "wisconsin": "https://www.nytimes.com/interactive/2020/us/wisconsin-coronavirus-cases.html",
        "wyoming": "https://www.nytimes.com/interactive/2020/us/wyoming-coronavirus-cases.html"
    }"""
    cases = (dataframeUS[0].iloc[0][1] + " total number of cases in the United States of America.")
    dailycases = (str(dataframeUS[0].iloc[0][2]) + " total number of cases today in United States of America.")
    deaths = (dataframeUS[0].iloc[1][1] + ' total deaths in United States of America')
    m1 = ''
    try:
        if int(dataframeUS[0].iloc[0][3].strip('%')) > 0:
            m1 = ("Stay home and avoid going outside. If you must go outside, please put on a mask. " + "14-day-change: " +
                  dataframeUS[0].iloc[0][3] + "\n")
    except:
        m1 = ("Stay safe. Please be careful. 14-day-change: " + str(dataframeUS[0].iloc[0][3]))
    return cases + ' ' +'<br>' + ' Advice Based on Covid Data: ' + m1 + '<br>' + deaths + '<br>' + dailycases
    # yn = (input("Do you want case data from USA states (yes/no)?: ")).lower()
    # if yn == "yes":
    # state = (input("Name a state: ")).lower()
    # if state in states:
    # dataframe50 = pd.read_html(states[state])
    # flash(str(dataframe50[1].iloc[0][1]) + "cases in" + state)
    # else:
    # flash("Could not find a U.S. state with that name")"""


def UK():
    dataframeUK = pd.read_html(
        "https://www.nytimes.com/interactive/2020/world/europe/united-kingdom-coronavirus-cases.html")
    cases = (str(dataframeUK[0].iloc[0][1]) + " total cases in the United Kingdom.")
    dailycases = (str(dataframeUK[0].iloc[0][2]) + " total number of cases today in the United Kingdom.")
    deaths = (str(dataframeUK[0].iloc[1][1]) + ' total deaths in United Kingdom.')
    m1 = ''
    try:
        if int(dataframeUK[0].iloc[0][3].strip('%')) > 0:
            m1 = ("Stay home and avoid going outside. If you must go outside, please put on a mask. " + "14-day-change: " + str(dataframeUK[0].iloc[0][3]) + "\n")
    except:
        m1 = ("Stay safe. Please be careful. 14-day-change: " + str(dataframeUK[0].iloc[0][3]))
    return cases + ' ' +'<br>' + ' Advice Based on Covid Data: ' + m1 + '<br>' + deaths + '<br>' + dailycases
    # yesno = (input("Do you want cases data from the UK regions (yes/no)?: ")).lower()
    # if yesno == "yes":
    # area = input("Name an area: ")
    # if area.lower() == "wales":
    # flash(dataframeUK[1].iloc[0][1] + "cases in Wales")
    # if area.lower() == "northern ireland":
    # flash(dataframeUK[1].iloc[1][1] + "cases in Northern Ireland")
    # if area.lower() == "england":
    # flash(dataframeUK[1].iloc[2][1] + "cases in England")
    # if area.lower() == "scotland":
    # flash(dataframeUK[1].iloc[3][1] + "cases in Scotland")


def Canada():
    dataframeCAN = pd.read_html("https://www.nytimes.com/interactive/2020/world/canada/canada-coronavirus-cases.html")
    cases = str(dataframeCAN[0].iloc[0][1]) + " cases in Canada."
    dailycases = (str(dataframeCAN[0].iloc[0][2]) + " total number of cases today in Canada")
    deaths = str(dataframeCAN[0].iloc[1][1]) + ' deaths in Canada.'
    m1 = ''
    try:
        if int(dataframeCAN[0].iloc[0][3].strip('%')) > 0:
            m1 = "Stay home and avoid going outside. If you must go outside, please put on a mask. " + "14-day-change: " + str(dataframeCAN[0].iloc[0][3]) + "\n"
    except:
        m1 = "Stay safe. Please be careful. 14-day-change: " + str(dataframeCAN[0].iloc[0][3])
    return cases + ' ' +'<br>' + ' Advice Based on Covid Data: ' + m1 + '<br>' + deaths + '<br>' + dailycases


def India():
    dataframeIndia = pd.read_html("https://www.nytimes.com/interactive/2020/world/asia/india-coronavirus-cases.html")
    cases = (str(dataframeIndia[0].iloc[0][1]) + " cases in India.")
    dailycases = (str(dataframeIndia[0].iloc[0][2]) + " total number of cases today in India")
    deaths = (str(dataframeIndia[0].iloc[1][1]) + ' total deaths in India')
    m1 = ''
    try:
        if int(dataframeIndia[0].iloc[0][3].strip('%')) > 0:
            m1 = ("Stay home and avoid going outside. If you must go outside, please put on a mask. " + "14-day-change: " + str(dataframeIndia[0].iloc[0][3]) + "\n")
    except:
        m1 = ("Stay safe. Please be careful. 14-day-change: " + str(dataframeIndia[0].iloc[0][3]))
    return cases + ' ' +'<br>' + ' Advice Based on Covid Data: ' + m1 + '<br>' + deaths + '<br>' + dailycases


def Germany():
    dataframeGermany = pd.read_html(
        'https://www.nytimes.com/interactive/2020/world/europe/germany-coronavirus-cases.html#:~:text=There%20have%20been%20at%20least,morning%2C%2019%2C932%20people%20had%20died.')
    cases = (str(dataframeGermany[0].iloc[0][1]) + " cases in Germany.")
    dailycases = (str(dataframeGermany[0].iloc[0][2]) + " total number of cases today in Germany.")
    deaths = (str(dataframeGermany[0].iloc[1][1]) + ' total deaths in Germany.')
    m1 = ''
    try:
        if int(dataframeGermany[0].iloc[0][3].strip('%')) > 0:
            m1 = ("Stay home and avoid going outside. If you must go outside, please put on a mask. " + "14-day-change: " +
                  str(dataframeGermany[0].iloc[0][3]) + "\n")
    except:
        m1 = ("Stay safe. Please be careful. 14-day-change: " + str(dataframeGermany[0].iloc[0][3]))
    return cases + ' ' +'<br>' + ' Advice Based on Covid Data: ' + m1 + '<br>' + deaths + '<br>' + dailycases


def France():
    dataframeFRANCE = pd.read_html(
        "https://www.nytimes.com/interactive/2020/world/europe/france-coronavirus-cases.html")
    cases = (str(dataframeFRANCE[0].iloc[0][1]) + " cases in France.")
    dailycases = (str(dataframeFRANCE[0].iloc[0][2]) + " total number of cases today in France.")
    deaths = (str(dataframeFRANCE[0].iloc[1][1]) + ' total deaths in France.')
    m1 = ''
    try:
        if int(dataframeFRANCE[0].iloc[0][3].strip('%')) > 0:
            m1 = ("Stay home and avoid going outside. If you must go outside, please put on a mask. " + "14-day-change: " +
                  str(dataframeFRANCE[0].iloc[0][3]) + "\n")
    except:
        m1 = ("Stay safe. Please be careful. 14-day-change: " + str(dataframeFRANCE[0].iloc[0][3]))
    return cases + ' ' +'<br>' + ' Advice Based on Covid Data: ' + m1 + '<br>' + deaths + '<br>' + dailycases


def Italy():
    dataframeIT = pd.read_html("https://www.nytimes.com/interactive/2020/world/europe/italy-coronavirus-cases.html")
    cases = (str(dataframeIT[0].iloc[0][1]) + " cases in Italy.")
    dailycases = (str(dataframeIT[0].iloc[0][2]) + " total number of cases today in Italy.")
    deaths = (str(dataframeIT[0].iloc[1][1]) + ' total deaths in Italy.')
    m1 = ''
    try:
        if int(dataframeIT[0].iloc[0][3].strip('%')) > 0:
            m1 = ("Stay home and avoid going outside. If you must go outside, please put on a mask. " + "14-day-change: " +
                  str(dataframeIT[0].iloc[0][3]) + "\n")
    except:
        m1 = ("Stay safe. Please be careful. 14-day-change: " + str(dataframeIT[0].iloc[0][3]))
    return cases + ' ' +'<br>' + ' Advice Based on Covid Data: ' + m1 + '<br>' + deaths + '<br>' + dailycases


def Spain():
    dataframeSP = pd.read_html("https://www.nytimes.com/interactive/2020/world/europe/spain-coronavirus-cases.html")
    cases = (str(dataframeSP[0].iloc[0][1]) + " cases in Spain.")
    dailycases = (str(dataframeSP[0].iloc[0][2]) + " total number of cases today in Spain.")
    deaths = (str(dataframeSP[0].iloc[1][1]) + ' total deaths in Spain.')
    m1 = ''
    try:
        if int(dataframeSP[0].iloc[0][3].strip('%')) > 0:
            m1 = ("Stay home and avoid going outside. If you must go outside, please put on a mask. " + "14-day-change: " +
                  str(dataframeSP[0].iloc[0][3]) + "\n")
    except:
        m1 = ("Stay safe. Please be careful. 14-day-change: " + str(dataframeSP[0].iloc[0][3]))
    return cases + ' ' +'<br>' + ' Advice Based on Covid Data: ' + m1 + '<br>' + deaths + '<br>' + dailycases


def Brazil():
    dataframeBRAZIL = pd.read_html(
        "https://www.nytimes.com/interactive/2020/world/americas/brazil-coronavirus-cases.html")
    cases = (str(dataframeBRAZIL[0].iloc[0][1]) + " cases in Brazil.")
    dailycases = (str(dataframeBRAZIL[0].iloc[0][2]) + " total number of cases today in Brazil.")
    deaths = (str(dataframeBRAZIL[0].iloc[1][1]) + ' total deaths in Brazil.')
    m1 = ''
    try:
        if int(dataframeBRAZIL[0].iloc[0][3].strip('%')) > 0:
            m1 = ("Stay home and avoid going outside. If you must go outside, please put on a mask. " + "14-day-change: " +
                  str(dataframeBRAZIL[0].iloc[0][3]) + "\n")
    except:
        m1 = ("Stay safe. Please be careful. 14-day-change: " + str(dataframeBRAZIL[0].iloc[0][3]))
    return cases + ' ' +'<br>' + ' Advice Based on Covid Data: ' + m1 + '<br>' + deaths + '<br>' + dailycases


def Mexico():
    dataframeMEX = pd.read_html("https://www.nytimes.com/interactive/2020/world/americas/mexico-coronavirus-cases.html")
    cases = (str(dataframeMEX[0].iloc[0][1]) + " cases in Mexico.")
    dailycases = (str(dataframeMEX[0].iloc[0][2]) + " total number of cases today in Mexico.")
    deaths = (str(dataframeMEX[0].iloc[1][1]) + ' total deaths in Mexico.')
    m1 = ''
    try:
        if int(dataframeMEX[0].iloc[0][3].strip('%')) > 0:
            m1 = ("Stay home and avoid going outside. If you must go outside, please put on a mask. " + "14-day-change: " +
                  str(dataframeMEX[0].iloc[0][3]) + "\n")
    except:
        m1 = ("Stay safe. Please be careful. 14-day-change: " + str(dataframeMEX[0].iloc[0][3]))
    return cases + ' ' +'<br>' + ' Advice Based on Covid Data: ' + m1 + '<br>' + deaths + '<br>' + dailycases


def World():
    dataframeEARTH = pd.read_html("https://www.nytimes.com/interactive/2020/world/coronavirus-maps.html")
    cases = (str(dataframeEARTH[0].iloc[0][1]) + " cases worldwide.")
    dailycases = (str(dataframeEARTH[0].iloc[0][2]) + " total number of cases today worldwide.")
    deaths = (str(dataframeEARTH[0].iloc[1][1]) + ' total deaths worldwide.')
    m1 = ''
    try:
        if int(dataframeEARTH[0].iloc[0][3].strip('%')) > 0:
            m1 = ("Stay home and avoid going outside. If you must go outside, please put on a mask. " + "14-day-change: " +
                  str(dataframeEARTH[0].iloc[0][3]) + "\n")
    except:
        m1 = ("Stay safe. Please be careful. 14-day-change: " + str(dataframeEARTH[0].iloc[0][3]))
    return cases + ' ' +'<br>' + ' Advice Based on Covid Data: ' + m1 + '<br>' + deaths + '<br>' + dailycases
