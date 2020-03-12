#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
'''
print(len(enron_data))
print(len(enron_data["SKILLING JEFFREY K"]))

poi= [x for x,y in enron_data.items() if y['poi']]
print(len(poi))

poi_reader = open('../final_project/poi_names.txt','rb')
count=0
for i in poi_reader:
    if '(y)' in i or '(n)' in i:
        count+=1
print(count)

print(enron_data["PRENTICE JAMES"]["total_stock_value"])

print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

print(enron_data["SKILLING JEFFREY K"]["total_payments"])
print(enron_data["LAY KENNETH L"]["total_payments"])
print(enron_data["FASTOW ANDREW S"]["total_payments"])

print(enron_data['SKILLING JEFFREY K'])


print(len(dict((key, value) for key, value in enron_data.items() if value["salary"] != 'NaN')))

known_email = [x for x,y in enron_data.items() if y['email_address']!='NaN']
print(len(known_email))

no_payment=len(dict((key, value) for key, value in enron_data.items() if value["total_payments"] == 'NaN'))
print(float(no_payment)/len(enron_data))

poi= dict((x,y) for x,y in enron_data.items() if y['poi'])
num_poi=len(poi)
no_payment=len(dict((key, value) for key, value in poi.items() if value["total_payments"] == 'NaN'))
print(float(no_payment)/len(num_poi))

print(len(enron_data) + 10)
print(10 + len(dict((key, value) for key, value in enron_data.items() if value["total_payments"] == 'NaN')))
'''
poi= dict((x,y) for x,y in enron_data.items() if y['poi'])
print(10+len(poi))
print(10 + len(dict((key, value) for key, value in poi.items() if value["total_payments"] == 'NaN')))
