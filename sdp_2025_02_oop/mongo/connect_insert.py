import pymongo

from model.instructor import Instructor
from model.student import Student

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["sdp_2025_testing"]

users_col = mydb["users"]

# sample data
trayan = Instructor('Trayan Iliev', 'Sofia 1000', '0887453214', 'trayan@gmail.com',
                    '', '305', courses=['UP', 'SDP', 'IA with Gen AI'])
george = Student('George', fn='0PH23235', semester=1)
ana = Student('Ana', fn='0MI123456', semester=2)

# insert users in mongodb
ins_res = users_col.insert_one(trayan.__dict__)
print('Inserted User with ID:', ins_res.inserted_id)
ins_res = users_col.insert_one(george.__dict__)
print('Inserted User with ID:', ins_res.inserted_id)
ins_res = users_col.insert_one(ana.__dict__)
print('Inserted User with ID:', ins_res.inserted_id)

# find all users
print(myclient.list_database_names())
print('\nAll students:')
for x in users_col.find():
  print(x)