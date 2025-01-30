import requests

url = 'https://restcountries.com/v3.1/'


class Country:
    def __init__(self, country_dict):
        self.name_en = country_dict['name']['common']
        if 'nativeName' in country_dict['name']:
            self.name_native = [country_dict['name']['nativeName'][n]['official']
                                for n in country_dict['name']['nativeName']]
        self.name_ru = country_dict['translations']['rus']['official']
        if 'ccn3' in country_dict:
            self.code = country_dict['ccn3']
        if 'currencies' in country_dict:
            self.currencies = country_dict['currencies']
        if 'capital' in country_dict:
            self.capital = country_dict['capital']
        self.coords = country_dict['latlng']
        if 'languages' in country_dict:
            self.lang = country_dict['languages']
        self.maps = country_dict['maps']
        self.population = country_dict['population']
        self.area = country_dict['area']
        self.continents = country_dict['continents']
        self.flags = country_dict['flags']
        self.capital_info = country_dict['capitalInfo']
        self.region = country_dict['region']


def countries_all():
    r = requests.get(url + 'all', verify=False)
    # print(r.json())
    countries = [Country(c) for c in r.json()]
    return countries



def countries_name(name):
    r = requests.get(url + f'name/{name}', verify=False)
    # print(r.json())
    country = Country(r.json()[0])
    return country

def regions_api():
    countries = countries_all()
    regions = {c.region for c in countries}
    return regions


def capitals_api():
    countries = countries_all()
    capitals = []
    for c in countries:
        if "capital" in c:
            capitals.append(c.capital)
        else:
            continue
    return capitals

if __name__ == '__main__':
    countries_all()
    c = countries_name('South Georgia')
    print(c.name_ru)
    print(regions_api())
