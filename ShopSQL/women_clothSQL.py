class Women_clothSQL():

    def __init__(self, cursor):
        self.cursor = cursor

    
    def add_new_women_cloth(self, value,price):
        query = f"""
        INSERT INTO women_cloth(cloth_name,price) 
        VALUES('{value}',{price});

        """
        
        self.cursor.execute(query)
        print("Новая одежда успешно добавлена!")
    
    def get_women_cloth(self):
        query = f"""
        SELECT id,cloth_name,price FROM women_cloth ;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_all_women_cloth(self):
        query = """
        SELECT * FROM women_cloth;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    
    
    