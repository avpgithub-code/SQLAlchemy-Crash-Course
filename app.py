from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

new_user1 = User(first_name="Ben",last_name="Smith",age=66)
new_user2 = User(first_name="Bob",last_name="Smith",age=34)
new_user3 = User(first_name="Kevin",last_name="Smith",age=76)
new_user4 = User(first_name="John",last_name="Smith",age=56)
new_user5 = User(first_name="Rambo",last_name="Smith",age=66)

# session.add(new_user)
session.add_all([new_user1, new_user2, new_user3, new_user4, new_user5])
session.commit()
print(f"Added new users with IDs: {new_user1.id}, {new_user2.id}, {new_user3.id}, {new_user4.id}, {new_user5.id}")

# Verify by querying the database
users = session.query(User).all()
for user in users:
    print(f"User ID: {user.id}, Name: {user.first_name}, Age: {user.age}")

# Update a user
user_to_update = session.query(User).filter_by(first_name="Bob").first()
if user_to_update:
    user_to_update.age = 99
    session.commit()
    print(f"Updated User ID: {user_to_update.id}, New Age: {user_to_update.age}")

