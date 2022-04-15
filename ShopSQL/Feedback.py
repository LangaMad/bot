class Feedback():

    def __init__(self, cursor):
        self.cursor = cursor

    def add_feedback(self,create_time,user,text):
        query = f"""
        INSERT INTO feedback(create_time,user,text) 
        VALUES('{create_time}','{user}','{text}');
        """
        self.cursor.execute(query)

    def get_id(self):
        query =f"""
        SELECT * FROM feedback ORDER BY id DESC LIMIT 1;
        """
        return self.cursor.execute(query)
        

    

       