import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time


def analyzer(product, price, review, link): 

    product_ = product
    price_ = price
    review_ = review
    reviews = []
    prices = []
    links = link
    ## analyzer lists
    low_price_review5 = []
    product_name_review5 = []
    link_review5 = []
    reviews_5 = []


    for i in review_:
        reviews.append(float(i))
    for i in price_:
        prices.append(int(i))
    
    print("[*] Products with a review 5.0:")
    print()
    for a,b,c,d in zip(product_,prices,reviews, links):
        if c == 5.0:
            print("[*] Product:", a, "|", "Price:", b, "|", "Review: ", c)
            print("[L] Link -> ", d)
            print()
            product_name_review5.append(a)
            low_price_review5.append(b)
            link_review5.append(d)
            reviews_5.append(c)
    print()
    print("*"*20)
    print()
    print("[*] Products with a review between 4.5 and 4.9:")
    print()
    for a,b,c,d in zip(product_,prices,reviews, links):
        if c >= 4.5 and c<= 4.9:
            print("[*] Product:", a, "|", "Price: ", b, "|", "Review: ", c)
            print("[L] Link -> ", d)
            print()
    print()
    print("*"*20)
    print()
    print("[*] Products with a review between 4.0 and 4.5:")
    print()
    for a,b,c,d in zip(product_, prices, reviews, links):
        if c <= 4.5 and c >= 4.0:
            print("[*] Product:", a, "|", "Price: ", b, "|", "Review: ", c)
            print("[L] Link -> ", d)
            print()
    
    print()
    print("*"*20)
    print()

    
    print("[*] Products with a review between 4.0 and below:")
    print()
    for a,b,c,d in zip(product_, prices, reviews, links):
        if c < 4.0:
            print("[*] Product:", a, "|", "Price: ", b, "|", "Review: ", c)
            print("[L] Link -> ", d)
            print()
    
    short_prices = list(prices)
    short_prices.sort()
    low_price_review5.sort()
    print("low_price sort = ", low_price_review5)
    print("Product_5 = ", product_name_review5, "low_price_review5 = ", low_price_review5, "review 5 = ",reviews_5)

    print("Analyzer: ")
    print("[!] Lower price for review of 5.0: ")
    for a,b in zip(product_name_review5,low_price_review5):
        print(a, b)
    

    
driver = webdriver.Firefox()
print("[*] Loading...")
driver.get("http://amazon.com.br")

if "Amazon" in driver.title:

    print("[*] Connected to amazon...")
    search = input("[*] Search product: ")
    driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']").send_keys(search, Keys.ENTER)
    time.sleep(3)
    current_link = driver.current_url
    print("[*] Current link: ", current_link)
    html = urlopen(current_link)

    soup = BeautifulSoup(html, "html.parser")
    time.sleep(3)

    all_products_list = []
    all_prices_list = []
    all_reviews_list = []
    counter = 0
    links_list = []
    repeated = set()

            
    for i in soup.findAll("span", {"class":"a-size-base-plus a-color-base a-text-normal"}): ## Get the names of products 
        if counter == 25:
            break
        all_products_list.append(i.get_text())
        counter = counter + 1
    
    counter = 0

    for i in soup.findAll("span", {"class":"a-price-whole"}): ## Get the price of the products

        if counter == 25:
            break
        all_prices_list.append(i.get_text().replace(",", "").replace(".", ""))
        counter = counter + 1

    counter = 0

    for i in soup.findAll("span", {"class":"a-icon-alt"}):
        if counter == 25:
            break
        all_reviews_list.append(i.get_text().replace(',', '.')[0:3].replace("Dua", "2.0").replace("Trê", "3.0").replace("Qua", "4.0").replace('1 E', '1.0'))
        counter = counter + 1
    
    counter = 0

    for i in soup.findAll("a", {"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}):
        if counter == 25:
            break
        if i.attrs['href'] not in repeated:
            links_list.append("http://amazon.com.br"+i.attrs['href'])
            repeated.add(i.attrs['href'])
            counter = counter + 1
        


    analyzer(all_products_list, all_prices_list, all_reviews_list, links_list)

    # Issue happened right after I added links... Why? 
    ###It happened because amazon changed a class name
    



    
