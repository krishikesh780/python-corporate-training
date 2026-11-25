class Customer:
    def __init__(self, cid, name, policy_number, policy_type, premium, status="Alive"):
        self.cid = cid
        self.name = name
        self.policy_number = policy_number
        self.policy_type = policy_type
        self.premium = premium
        self.status = status

    def update_premium(self, new_premium):
        self.premium = new_premium

    def update_policy_type(self, new_type):
        self.policy_type = new_type

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Customer({self.cid}, {self.name}, {self.policy_number}, {self.policy_type}, {self.premium}, {self.status})"

    def to_dict(self):
        return {
            "id": self.cid,
            "name": self.name,
            "policy_number": self.policy_number,
            "policy_type": self.policy_type,
            "premium": self.premium,
            "status": self.status
        }
