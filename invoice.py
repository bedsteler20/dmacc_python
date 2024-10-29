class Invoice:
    invoice_id: int
    customer_id: int
    last_name: str
    first_name: str
    phone_number: str
    address: str
    items_with_price: dict[str, float]

    def __init__(
        self,
        invoice_id: int,
        customer_id: int,
        last_name: str,
        first_name: str,
        phone_number: str,
        address: str,
        items_with_price: dict[str, float] = {},
    ):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address
        self.items_with_price = items_with_price

    def add_item(self, data: dict[str, float]):
        self.items_with_price.update(data)

    def __str__(self):
        out = ""
        out += f"Invoice ID: {self.invoice_id}\n"
        out += f"{self.first_name} {self.last_name}\n"
        out += f"{self.address}\n"
        out += f"{self.phone_number}\n"
        out += "Items:\n"
        for item, price in self.items_with_price.items():
            out += f"{item}: ${price}\n"

        return out

    def __repr__(self):
        return self.__str__()

    def create_invoice(self):
        print(str(self))


if __name__ == "__main__":
    # Driver code
    invoice = Invoice(
        invoice_id=1,
        customer_id=123,
        address="1313 Disneyland Dr, Anaheim, CA 92802",
        last_name="Mouse",
        first_name="Minnie",
        phone_number="555-867-5309",
    )
    invoice.add_item({"iPad": 799.99})
    invoice.add_item({"Surface": 999.99})
    invoice.create_invoice()
