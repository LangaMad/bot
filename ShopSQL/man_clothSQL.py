class Men_clothSQL():

    def __init__(self, cursor):
        self.cursor = cursor

    
    def add_new_men_cloth(self, value,price):
        query = f"""
        INSERT INTO man_cloth(cloth_name,price) 
        VALUES('{value}',{price});

        """
        
        self.cursor.execute(query)
        print("Новая одежда успешно добавлена!")

    def get_men_cloth(self):
        query = f"""
        SELECT id,cloth_name,price FROM man_cloth ;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_all_men_cloth(self):
        query = """
        SELECT * FROM man_cloth;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()