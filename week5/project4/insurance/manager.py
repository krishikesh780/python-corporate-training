from .customer import Customer
from .utils import read_customers, write_customers
from .exceptions import CustomerNotFoundError

class CustomerManager:
    def __init__(self):
        self.customers = []
        self.load_customers()

    def load_customers(self):
        raw_data = read_customers()
        self.customers = [
            Customer(c["id"], c["name"], c["policy_number"], c["policy_type"], c["premium"], c.get("status", "Alive"))
            for c in raw_data
        ]

    # ============ READ ============
    def list_customers(self):
        for c in self.customers:
            print(c)

    def find_customer(self, policy_number):
        for c in self.customers:
            if c.policy_number == policy_number:
                return c
        raise CustomerNotFoundError(f"❌ Customer with policy {policy_number} not found.")

    # ============ CREATE ============
    def add_customer(self, cid, name, policy_number, policy_type, premium, status="Alive"):
        if any(c.policy_number == policy_number for c in self.customers):
            print(f"❌ Policy {policy_number} already exists.")
            return
        new_c = Customer(cid, name, policy_number, policy_type, premium, status)
        self.customers.append(new_c)
        print(f"✅ New customer added: {new_c}")

    # ============ UPDATE ============
    def update_customer(self, policy_number, new_premium=None, new_type=None, new_status=None):
        customer = self.find_customer(policy_number)
        if new_premium:
            customer.update_premium(new_premium)
        if new_type:
            customer.update_policy_type(new_type)
        if new_status:
            customer.update_status(new_status)
        print(f"✅ Updated: {customer}")

    # ============ DELETE ============
    def delete_customer(self, policy_number):
        try:
            customer = self.find_customer(policy_number)
            self.customers.remove(customer)
            print(f"🗑️ Deleted: {customer}")
        except CustomerNotFoundError as e:
            print(e)

    # ============ SAVE ============
    def save(self):
        write_customers([c.to_dict() for c in self.customers])
