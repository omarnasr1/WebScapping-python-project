import requests
import bs4

url1 = 'https://www.amazon.eg/s?k=horror+books+english&language=en&qid=1671304725&sprefix=%2Caps%2C1437&ref=sr_pg_1'
url2 = 'https://www.amazon.eg/-/en/s?k=horror+books+english&page=2&language=en&qid=1671305353&sprefix=%2Caps%2C1437&ref=sr_pg_2'

books_names = []
books_prices = []
books_authors = []
books_rates = []
page1 = requests.get(url1)
content1 = page1.content
soup1 = bs4.BeautifulSoup(content1, "html.parser")
page2 = requests.get(url2)
content2 = page2.content
soup2 = bs4.BeautifulSoup(content2, "html.parser")
names = soup1.findAll("span", {"class": "a-size-base-plus a-color-base a-text-normal"})+soup2.findAll("span", {"class": "a-size-base-plus a-color-base a-text-normal"})
prices = soup1.findAll("span", {"class": "a-price-whole"})+soup2.findAll("span", {"class": "a-price-whole"})
rates = soup1.findAll("div", {"class": "a-row a-size-small"})+soup2.findAll("div", {"class": "a-row a-size-small"})
auther = soup1.findAll("div", {"class": "a-section a-spacing-none a-spacing-top-small s-title-instructions-style"})+soup2.findAll("div", {"class": "a-section a-spacing-none a-spacing-top-small s-title-instructions-style"})

for i in range(len(names)):
    books_names.append(names[i].text)

for i in range(len(prices)):
    books_prices.append(prices[i].text[0:len(prices[i].text) - 1])

for i in range(len(rates)):
    rate = ''
    first = False
    for j in rates[i].text:
        if j == ')':
            break
        if first:
            rate += j
        if j == '(':
            first = True

    books_rates.append(rate + " out of 5")

for i in range(len(auther)):
    founded_author = ''
    found = False
    if auther[i].text.find("من"):
        for j in auther[i].text:
            if found and ('a' <= j <= 'z' or 'A' <= j <= 'Z'):
                founded_author += j
            if j == 'ن':
                found = True

    if found:
        books_authors.append(founded_author)
    else:
        books_authors.append("oops, author not founded")

count = 1
for i in zip(books_names, books_authors, books_prices, books_rates):
    print("=====> Details of book number", count)
    print("Name is ", i[0])
    print("author is ", 'by ' + i[1])
    print("Price is ", i[2])
    print("Rate is ", i[3])
    print()
    count += 1
