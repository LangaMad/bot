class Adress_cash():
    def __init__(self, cursor):
        self.cursor = cursor

    def add_cash(self,create_time,number,text):
        query = f"""
        INSERT INTO adress_cash(adress_time,adress,number) 
        VALUES('{create_time}','{text}','{number}');
        """
        self.cursor.execute(query)

    def get_id(self):
        query =f"""
        SELECT * FROM feedback ORDER BY id DESC LIMIT 1;
        """
        return self.cursor.execute(query)