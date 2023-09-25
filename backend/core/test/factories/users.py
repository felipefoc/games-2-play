import factory
from pytest_factoryboy import register
from models.users import User
from faker import Factory as FactoryFaker

faker = FactoryFaker.create()

@register
class UserFactory(factory.Factory):
    username = factory.LazyAttribute(lambda x: faker.name())
    class Meta:
        model = User
