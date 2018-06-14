class Contact:

    def __init__(self, customer_details):
        self.customer_details = customer_details
        self.full_name = {}
        self.company_name = {}
        self.email = {}
        self.phone = {}
        self.address = {}
        self.website = {}
        self.social_network = {}

    def update_details(self):
        for k, v in self.customer_details:
            setattr(self, k, v)
