from faker import Faker
from dotenv import load_dotenv
import os

load_dotenv()
faker = Faker()


class Payloads:

    @staticmethod
    def auth_payload():
        return {
            "username": os.getenv('USERNAME'),
            "password": os.getenv('PASSWORD')
        }

    @staticmethod
    def product_payload():
        return {
            "title": faker.sentence(nb_words=3),
            "price": faker.pyfloat(right_digits=2, positive=True, max_value=100),
            "description": faker.text(max_nb_chars=20),
            "category": "World",
            "image": "http://example.com"
        }

    @staticmethod
    def user_payload():
        return {
            "username": faker.user_name(),
            "email": faker.email(),
            "password": faker.password(length=8)
        }

    @staticmethod
    def cart_payload(userid, products: list[int]):
        return {
            "userId": userid,
            "products": [{'productId': prod_id} for prod_id in products]
        }
