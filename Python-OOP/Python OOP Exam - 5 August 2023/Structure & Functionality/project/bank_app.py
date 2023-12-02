from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    VALID_LOAN_TYPES = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan,
    }

    VALID_CLIENT_TYPES = {
        "Student": Student,
        "Adult": Adult,
    }

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans: list = []
        self.clients: list = []

    @staticmethod
    def find_client(cl_id, clients_list):

        for client in clients_list:

            if client.client_id == cl_id:
                return client

    @staticmethod
    def find_loan(loan_type, loans_list):

        for loan in loans_list:

            if loan.__class__.__name__ == loan_type:

                return loan

    def add_loan(self, loan_type: str):

        if loan_type not in BankApp.VALID_LOAN_TYPES.keys():
            raise Exception("Invalid loan type!")

        self.loans.append(BankApp.VALID_LOAN_TYPES[loan_type]())

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):

        if client_type not in BankApp.VALID_CLIENT_TYPES.keys():
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        self.clients.append(BankApp.VALID_CLIENT_TYPES[client_type](client_name, client_id, income))

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):

        not_valid_loan_type_client = {
            "StudentLoan": "Adult",
            "MortgageLoan": "Student",
        }

        client = self.find_client(client_id, self.clients)
        loan = self.find_loan(loan_type, self.loans)

        if not_valid_loan_type_client[loan_type] == client.__class__.__name__:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):

        client = self.find_client(client_id, self.clients)

        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)

        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0

        for loan in self.loans:

            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0

        for client in self.clients:
            if client.interest < min_rate:

                client.increase_clients_interest()
                changed_client_rates_number += 1

        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):

        total_clients_count = len(self.clients)
        total_clients_income = 0
        loans_count_granted_to_clients = 0
        granted_sum = 0
        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum(loan.amount for loan in self.loans)
        avg_client_interest_rate = 0 if len(self.clients) == 0\
            else sum(client.interest for client in self.clients) / len(self.clients)

        for client in self.clients:

            total_clients_income += client.income
            loans_count_granted_to_clients += len(client.loans)
            granted_sum += sum(loan.amount for loan in client.loans)

        result = [
            f"Active Clients: {total_clients_count}",
            f"Total Income: {total_clients_income:.2f}",
            f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}",
            f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}",
            f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        ]

        return "\n".join(result)
