from not_interesting.dal.dal import DAL
from not_interesting.utils import Utils

class Manager:
    def __init__(self):
        self.dal = DAL()

    def insert_data_to_db(self, data):
        return self.dal.insert_data(data)

    def get_data_from_db(self):
        data = self.dal.get_all_data()
        data = Utils.correct_the_id(data)
        return data