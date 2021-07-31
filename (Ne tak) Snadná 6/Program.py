import requests
import lxml.html

def get_page(url):
    # Pošleme HTTP GET požadavek na zadanou adresu
    response = requests.get(url, stream=True)
    # Můžeme zkontrolovat návratový kód, 200 je ok, 404 například znamená, že
    # stránka neexistuje
    if response.status_code != 200:
        # print(f"Něco se pokazilo, request na URL '{url}' vrátil {response.status_code}")
        return False
    # Vrátíme tělo odpovědi
    response.raw.decode_content = True
    tree = lxml.html.parse(response.raw)
    return tree


i = 0
base = "http://i.protab.cz/static/ulohy/01f/"
url = "tridgivgzbxgrzaglrcrcscyrorjjdvheucleyfxnpgidobfgdxphycqzsdruzlcstjovypkkm.html"
while i < 50:
    i += 1
    print(chr(len(url)-5), end="")
    tree = get_page(base + url)
    soup = tree.xpath('/html/body/iframe[2]')
    url = soup[0].attrib['src']
