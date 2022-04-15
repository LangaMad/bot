class Women_shoesSQL():

    def __init__(self, cursor):
        self.cursor = cursor

    
    def add_new_women_shoes(self, value,price):
        query = f"""
        INSERT INTO women_shoes(shoes_name,price) 
        VALUES('{value}',{price});

        """
        self.cursor.execute(query)
        print("добавленo!")


    def get_women_shoes(self):
        query = f"""
        SELECT id,shoes_name,price FROM women_shoes ;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def get_all_women_shoes(self):
        query = """
        SELECT * FROM women_shoes;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()