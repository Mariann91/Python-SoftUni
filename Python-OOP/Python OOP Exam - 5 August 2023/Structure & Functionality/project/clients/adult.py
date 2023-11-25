from project.clients.base_client import BaseClient


class Adult(BaseClient):
    def __init__(self, name: str, client_id: str, income: float, interest: float = 4):
        super().__init__(name, client_id, income, interest)
        self.interest = interest

    @property
    def client_interest_increase(self):
        return 2
      
