import csv
import random
import datetime

import RandDateTimeGen as gen

first_names = ['Zorita', 'Sara', 'Otto', 'Connor', 'Kato', 'Charles', 'Bruce', 'Orlando', 'Anjolie', 'Nora']
last_names = ['Moon', 'David', 'Morton', 'Davenport', 'Jenkins', 'Park', 'Parsons', 'King', 'Chavez', 'Ellison']
emails = ['zmoon@ncsu.edu', 'sdavid@ncsu.edu', 'omorton@ncsu.edu', 'cdavenp@ncsu.edu', 'kjenkin@ncsu.edu', 'cpark@ncsu.edu', 'bparson@ncsu.edu', 'oking@ncsu.edu', 'achavez@ncsu.edu', 'nelliso@ncsu.edu']
courses = ['E115', 'CSC116', 'CSC216', 'E298']
work_types = ['Office Hours', 'Grading', 'Proctoring', 'Lab', 'Communication', 'Meeting']

header = ['first_name', 'last_name', 'email', 'course', 'date', 'time_in', 'time_out', 'work_type']

data = []

for i in range(0, 10):
	course = random.choice(courses)
    
	for j in range(0, 21):
		new_date = gen.random_date(datetime.date(2025, 10, 1), datetime.date(2025, 10, 31)) 
		new_time_in, new_time_out = gen.random_timeframe(8, 17, 4)
  
		data.append({'first_name': first_names[i], 'last_name': last_names[i], 'email': emails[i], 'course': course, 'date': new_date, 'time_in': new_time_in, 'time_out': new_time_out, 'work_type': random.choice(work_types)})
    
with open('genData.csv', 'w', newline = '') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = header)
    writer.writeheader()
    writer.writerows(data)
   