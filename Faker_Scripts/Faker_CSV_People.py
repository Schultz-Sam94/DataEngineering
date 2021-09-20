import csv

from faker import Faker

output = open('data.csv','w+')

fake=Faker()

header =['name','age', 'street', 'city', 'state', 'zip', 'lng', 'lat']
writer = csv.writer(output)

writer.writerow(header)
for r in range(1000):
    writer.writerow([fake.name(), fake.random_int(min=18, max=80, step=1), fake.street_address(), fake.city(), fake.state(), fake.zipcode(), fake.longitude(), fake.latitude()])
output.close()
