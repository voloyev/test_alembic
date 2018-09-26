from datetime import date
from account import Account
from base import Session, engine, Base


Base.metadata.create_all(engine)
session = Session()
bob = Account("Bob", date(1992, 2, 17))
session.add(bob)
session.commit()

accounts = session.query(Account).all()

for a in accounts:
    print('name: {},  account: {}'.format(a.name, a.account))
