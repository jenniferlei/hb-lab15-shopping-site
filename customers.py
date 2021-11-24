"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(
        self,
        email,
        password,
        first_name,
        last_name
    ):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

        
def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of email and password.

    Dictionary will be {email: customer object}
    """

# Jane|Melonista|jane@jane.com|secret

    customer_data = {}

    with open(filepath) as file:
        for line in file:
            (
                first_name,
                last_name,
                email,
                password
            ) = line.strip().split("|")

            customer_data[email] = Customer(
                email,
                password,
                first_name,
                last_name,
            )

    return customer_data

    
def get_by_email(email, customer_data):
    """Return a Customer object, given the email"""

    return customer_data[email]


customer_data = read_customers_from_file("customers.txt")