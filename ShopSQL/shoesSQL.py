class ShoesSQL():

    def __init__(self, cursor):
        self.cursor = cursor

    
    def add_new_shoes(self, value,price):
        query = f"""
        INSERT INTO shoes(name,price) 
        VALUES('{value}',{price});

        """
        self.cursor.execute(query)
        print("добавленo!")

    def get_shoes(self):
        query = f"""
        SELECT id,name,price FROM shoes ;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_all_shoes(self):
        query = """
        SELECT * FROM shoes;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()