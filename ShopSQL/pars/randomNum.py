class RandomSQL():

    def __init__(self, cursor):
        self.cursor = cursor

    
    def add_new_shoes(self, random):
        query = f"""
        INSERT INTO random(number) 
        VALUES('{random}');

        """
        self.cursor.execute(query)
        print("добавленo!")