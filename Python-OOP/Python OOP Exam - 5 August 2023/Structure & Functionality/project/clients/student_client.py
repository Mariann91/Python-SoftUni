from project.clients.base_client import BaseClient


class Student(BaseClient):
    def __init__(self, name: str, client_id: str, income: float, interest: float = 2):
        super().__init__(name, client_id, income, interest)
        self.interest = interest

    @property
    def client_interest_increase(self):
        return 1
