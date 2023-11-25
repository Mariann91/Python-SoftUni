from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    VALID_CLIENTS = {
        "Student": Student,
        "Adult": Adult
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []
        self.loans_count_granted_to_clients = 0
        self.granted_sum = 0

    def add_loan(self, loan_type: str):

        if not BankApp.VALID_LOANS.get(loan_type):
            raise Exception("Invalid loan type!")

        self.loans.append(BankApp.VALID_LOANS[loan_type]())

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):

        if not BankApp.VALID_CLIENTS.get(client_type):
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        self.clients.append(BankApp.VALID_CLIENTS[client_type](
            name=client_name,
            client_id=client_id,
            income=income,
        ))

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):

        client = next(filter(lambda x: x.client_id == client_id, self.clients))

        invalid_client_loan_pairs = {
            "Student": "MortgageLoan",
            "Adult": "StudentLoan"
        }

        if invalid_client_loan_pairs[client.__class__.__name__] == loan_type:
            raise Exception("Inappropriate loan type!")

        for index in range(len(self.clients)):

            if self.loans[index].__class__.__name__ == loan_type:
                granted_loan = self.loans.pop(index)

                self.granted_sum += granted_loan.amount
                self.loans_count_granted_to_clients += 1

                client.loans.append(granted_loan)

                return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):

        try:
            client = next(filter(lambda x: x.client_id == client_id, self.clients))

        except StopIteration:
            raise Exception("No such client!")

        if not client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)

        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0

        for loan in self.loans:

            if loan.__class__.__name__ == loan_type:
                number_of_changed_loans += 1
                loan.increase_interest_rate()

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0

        for client in self.clients:

            if client.interest < min_rate:
                changed_client_rates_number += 1

                client.increase_clients_interest()

        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):

        avg_client_interest_rate = 0

        if len(self.clients) > 0:
            avg_client_interest_rate = sum(client.interest for client in self.clients) / len(self.clients)

        return "\n".join([
           f"Active Clients: {len(self.clients)}",
           f"Total Income: {sum(client.income for client in self.clients):.2f}",
           f"Granted Loans: {self.loans_count_granted_to_clients}, Total Sum: {self.granted_sum:.2f}",
           f"Available Loans: {len(self.loans)}, Total Sum: {sum(loan.amount for loan in self.loans):.2f}",
           f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        ])
