import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Gender' : 1, 'Age' : 40, 'BMI': 18, 'Blood Pressure (Systolic)':120, 
	'Blood Pressure (Diastolic)': 80, 'Respiration Rate(beats/minute)':20, 'Pulse Rate' : 70,  
	'Body Temperature':37,  'Chest Pain':0,  'Drinking/Smoking':1})

print(r.json())