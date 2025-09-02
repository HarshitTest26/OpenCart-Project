from faker import Faker
import json


class DataMockingTool:
    def __init__(self, locale='en_IN'):
        self.fake = Faker(locale)

    def generate_user_data(self, num_users=1):
        users = []
        for i in range(num_users):
            user = {
                "first_name": self.fake.first_name(),
                "last_name": self.fake.last_name(),
                "address": self.fake.address(),
                "email": self.fake.email(),
                "phone_number": self.fake.phone_number(),
                "job": self.fake.job(),
                "dob": self.fake.date_of_birth().isoformat()
            }
            users.append(users)
        return users

    def generate_transaction_data(self, num_transactions=1):
        transactions = []
        for _ in range(num_transactions):
            transaction = {
                "transaction_id": self.fake.uuid4(),
                "amount": self.fake.random_number(digits=5),
                "currency": self.fake.currency_code(),
                "date": self.fake.date_time_this_year().isoformat(),
                "status": self.fake.random_element(elements=("completed", "pending", "failed"))
            }
            transactions.append(transaction)
        return transactions

    def save_data_to_file(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)


# Example usage:
# if __name__ == "__main__":
#     tool = DataMockingTool()
#     users = tool.generate_user_data(num_users=5)
#     transactions = tool.generate_transaction_data(num_transactions=5)
#
#     tool.save_data_to_file(users, "mock_users.json")
#     tool.save_data_to_file(transactions, "mock_transactions.json")
#
#     print("Mock data generated and saved to files.")
