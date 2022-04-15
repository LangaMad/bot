


import requests
from bs4 import BeautifulSoup as BS








def get_response(url):
    response = requests.get(url)
    if response.status_code == 200: 
        return response.text
    else:
        return "Error"


def get_links(html):
    links = []
    soup = BS(html, 'html.parser')
    content = soup.find("div", {"class":"product-grid css-pz797i"})
    # list = content.find("div", {"class":"product-card__body"})
    posts = content.find_all("div", {"class":"product-card__body"})
   
    for post in posts:
        link=post.find("a", {"class":"product-card__link-overlay"}).get("href")
        full_link = link
        links.append(full_link)
    
    return links 
    



    

def get_page_data2(html):
    soup = BS(html, 'html.parser')
    content = soup.find("div", {"id":"react-root"})
    title = content.find("div", {"class":"pr2-sm css-1ou6bb2"}).find("h1").text.strip()
    title = title.replace("'","")
    try:
        price = content.find("div", {"class":"pr2-sm css-1ou6bb2"}).find("div", {"class":"product-price css-11s12ax is--current-price css-tpaepq"}).text.strip()
    except AttributeError :
        price = content.find("div", {"class":"pr2-sm css-1ou6bb2"}).find("div", {"class":"product-price is--current-price css-s56yt7 css-xq7tty"}).text.strip()
    price = price.replace("$","")
    float(price)
    data = {
        "name":title,
        "price":price,
    }
    
    return data






def main():
    cloth_list =[]
    URL = "https://www.nike.com/w/mens-clothing-6ymx6znik1"
    html=get_response(url=URL)
    post_links=get_links(html)
    for link in post_links: 
        page = get_response(link)
        data = get_page_data2(page)
        cloth_list.append(data)
        print(cloth_list)
    return cloth_list


    

# def main2():
#     shoes_list = []
#     URL = "https://www.nike.com/w/mens-shoes-nik1zy7ok"
#     html=get_response(url=URL)
#     post_links=get_links(html)
#     for link in post_links: 
#         page = get_response(link)
#         data2 = get_page_data2(page)
#         shoes_list.append(data2)
#         print(shoes_list)
#     return shoes_list


def main3():
    women_shoes_list = []
    URL = "https://www.nike.com/w/womens-shoes-5e1x6zy7ok"
    html=get_response(url=URL)
    post_links=get_links(html)
    for link in post_links: 
        page = get_response(link)
        data2 = get_page_data2(page)
        women_shoes_list.append(data2)
        print(women_shoes_list)
    return women_shoes_list

def main4():
    women_cloth_list = []
    URL = "https://www.nike.com/w/womens-clothing-5e1x6z6ymx6"
    html=get_response(url=URL)
    post_links=get_links(html)
    for link in post_links: 
        page = get_response(link)
        data2 = get_page_data2(page)
        women_cloth_list.append(data2)
        
    return women_cloth_list




        



       
        

        

        
    


        
   

