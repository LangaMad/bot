import mysql.connector
from women_clothSQL import Women_clothSQL
from women_shoesSQL import Women_shoesSQL
from shoesSQL import ShoesSQL
from man_clothSQL import Men_clothSQL
from pars.randomNum import RandomSQL
from pars.parsing import main,main4,main3

import random   
import string  
import secrets  
num = 10

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="271711hasan",
    db="telegrambot_1",
    autocommit = True
)

cursor = db.cursor()




shoes_maneger = ShoesSQL(cursor=cursor)
men_cloth_maneger = Men_clothSQL(cursor)
women_cloth_maneger = Women_clothSQL(cursor)
women_shoes_maneger = Women_shoesSQL(cursor)
random_maneger = RandomSQL(cursor)



res = ''.join(secrets.choice(string.digits) for x in range(num))  
# Print the Secure string using string.digits  
print("Secure random string is :"+ str(res)) 
random_maneger.add_new_shoes(res)

# shoes_list = main2()
# men_cloth_list = main()
# women_cloth_list = main3()
# women_shoes_list = main4()



# for data in men_cloth_list:
#     name = data["name"]
#     price = data["price"]
    
#     men_cloth_maneger.add_new_men_cloth(value=name, price=price)

# for data in shoes_list:
#     name = data["name"]
#     price = data["price"]
    
#     shoes_maneger.add_new_shoes(value=name, price=price)    

# for data in women_cloth_list:
#     name = data["name"]
#     price = data["price"]
    
#     women_cloth_maneger.add_new_women_cloth(value=name, price=price)

# for data in women_shoes_list:
#     name = data["name"]
#     price = data["price"]
    
#     women_shoes_maneger.add_new_women_shoes(value=name, price=price)


# brand_maneger.add_new_brand("Nike")
# brand_maneger.add_new_brand("Adidas")
# brand_maneger.add_new_brand("Rebook")
# brand_maneger.add_new_brand("Supreme")

# category_maneger.add_new_category("Обувь")
# category_maneger.add_new_category("Носки")
# category_maneger.add_new_category("Аксессуары")




