import requests
from bs4 import BeautifulSoup

def loading():
    for i in range(11, 51):
        f = open("page" + str(i) + '.txt', 'w', encoding='utf-8')
        r = requests.get('https://cargo.rzd.ru/ru/9800/page/4821?f2705_pagesize=100&f2705_pagenumber=' + str(i))
        f.write(r.text)
        f.close()

def bs():
    names = open("names.txt", 'w')
    for i in range(11, 51):
        with open("page" + str(i) + ".txt", 'r', encoding='utf-8') as f:
            contents = f.read()

            soup = BeautifulSoup(contents, 'html')
            for child in soup.find_all("td")[2::5]:
                names.write(child.text + '\n')
    names.close()


if __name__ == "__main__":
    bs()