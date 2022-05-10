
# No other modules apart from 'socket', 'BeautifulSoup', 'requests' and 'datetime'
# need to be imported as they aren't required to solve the assignment

# Import required module/s
import socket
from bs4 import BeautifulSoup
import requests
import datetime


# Define constants for IP and Port address of Server
# NOTE: DO NOT modify the values of these two constants
HOST = '127.0.0.1'
PORT = 24680
ERROR = 0


def fetchWebsiteData(url_website):
	"""Fetches rows of tabular data from given URL of a website with data excluding table headers.

	Parameters
	----------
	url_website : str
		URL of a website

	Returns
	-------
	bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""
	
	web_page_data = ''

	##############	ADD YOUR CODE HERE	##############
	req = requests.get(url_website)
	soup = BeautifulSoup(req.text, "lxml")
	tbody = soup.find_all("tbody")
	for rows in tbody:
		web_page_data = rows.find_all('tr')
	##################################################

	return web_page_data


def fetchVaccineDoses(web_page_data):
	"""Fetch the Vaccine Doses available from the Web-page data and provide Options to select the respective Dose.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers

	Returns
	-------
	dict
		Dictionary with the Doses available and Options to select, with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineDoses(web_page_data))
	{'1': 'Dose 1', '2': 'Dose 2'}
	"""

	vaccine_doses_dict = {}

	##############	ADD YOUR CODE HERE	##############
	doses = []
	for td in web_page_data:
		doses.append(td.find_all("td", {"class": "dose_num"})[0].text)

	doses = sorted(list(set(doses)))
	vaccine_doses_dict = {str(i+1): "Dose {}".format(doses[i]) for i in range(len(doses))}
	##################################################

	return vaccine_doses_dict


def fetchAgeGroup(web_page_data, dose):
	"""Fetch the Age Groups for whom Vaccination is available from the Web-page data for a given Dose
	and provide Options to select the respective Age Group.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Age Groups (for whom Vaccination is available for a given Dose) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchAgeGroup(web_page_data, '1'))
	{'1': '18+', '2': '45+'}
	>>> print(fetchAgeGroup(web_page_data, '2'))
	{'1': '18+', '2': '45+'}
	"""

	age_group_dict = {}

	##############	ADD YOUR CODE HERE	##############
	age = []
	for td in web_page_data:
		if(td.find_all("td", {"class": "dose_num"})[0].text == dose):
			age.append(td.find_all("td", {"class": "age"})[0].text)

	age = sorted(list(set(age)))
	age_group_dict = {str(i+1): "{}".format(age[i]) for i in range(len(age))}
	##################################################

	return age_group_dict


def fetchStates(web_page_data, age_group, dose):
	"""Fetch the States where Vaccination is available from the Web-page data for a given Dose and Age Group
	and provide Options to select the respective State.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the States (where the Vaccination is available for a given Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchStates(web_page_data, '18+', '1'))
	{
		'1': 'Andhra Pradesh', '2': 'Arunachal Pradesh', '3': 'Bihar', '4': 'Chandigarh', '5': 'Delhi', '6': 'Goa',
		'7': 'Gujarat', '8': 'Harayana', '9': 'Himachal Pradesh', '10': 'Jammu and Kashmir', '11': 'Kerala', '12': 'Telangana'
	}
	"""

	states_dict = {}

	##############	ADD YOUR CODE HERE	##############
	states = []
	for td in web_page_data:
		if(td.find_all("td", {"class": "age"})[0].text == age_group and 
				td.find_all("td", {"class": "dose_num"})[0].text == dose):
			states.append(td.find_all("td", {"class": "state_name"})[0].text)

	states = sorted(list(set(states)))
	states_dict = {str(i+1): "{}".format(states[i]) for i in range(len(states))}
	##################################################

	return states_dict


def fetchDistricts(web_page_data, state, age_group, dose):
	"""Fetch the District where Vaccination is available from the Web-page data for a given State, Dose and Age Group
	and provide Options to select the respective District.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Districts (where the Vaccination is available for a given State, Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchDistricts(web_page_data, 'Ladakh', '18+', '2'))
	{
		'1': 'Kargil', '2': 'Leh'
	}
	"""

	districts_dict = {}

	##############	ADD YOUR CODE HERE	##############
	district = []
	for td in web_page_data:
		if(td.find_all("td", {"class": "age"})[0].text == age_group and 
				td.find_all("td", {"class": "dose_num"})[0].text == dose and 
					td.find_all("td", {"class": "state_name"})[0].text == state):
			district.append(td.find_all("td", {"class": "district_name"})[0].text)

	district = sorted(list(set(district)))
	districts_dict = {str(i+1): "{}".format(district[i]) for i in range(len(district))}
	##################################################

	return districts_dict


def fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose):
	"""Fetch the Hospital and the Vaccine Names from the Web-page data available for a given District, State, Dose and Age Group
	and provide Options to select the respective Hospital and Vaccine Name.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Hosptial and Vaccine Names (where the Vaccination is available for a given District, State, Dose, Age Group)
		and Options to select, with Key as 'Option' and Value as another dictionary having Key as 'Hospital Name' and Value as 'Vaccine Name'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchHospitalVaccineNames(web_page_data, 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {
				'MedStar Hospital Center': 'Covaxin'
			}
	}
	>>> print(fetchHospitalVaccineNames(web_page_data, 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {
				'Eden Clinic': 'Covishield'
			}
	}
	"""
	
	hospital_vaccine_names_dict = {}

	##############	ADD YOUR CODE HERE	##############
	vaccine_name = []
	hospital_name = []
	for td in web_page_data:
		if(td.find_all("td", {"class": "age"})[0].text == age_group and 
				td.find_all("td", {"class": "dose_num"})[0].text == dose and 
					td.find_all("td", {"class": "state_name"})[0].text == state and 
						td.find_all("td", {"class": "district_name"})[0].text == district):
			vaccine_name.append(td.find_all("td", {"class": "vaccine_name"})[0].text)
			hospital_name.append(td.find_all("td", {"class": "hospital_name"})[0].text)

	vaccine_name = sorted(list(set(vaccine_name)))
	hospital_name = sorted(list(set(hospital_name)))
	hospital_vaccine_names_dict = {str(i+1): dict(zip(hospital_name, vaccine_name)) for i in range(len(hospital_name))}
	##################################################

	return hospital_vaccine_names_dict


def fetchVaccineSlots(web_page_data, hospital_name, district, state, age_group, dose):
	"""Fetch the Dates and Slots available on those dates from the Web-page data available for a given Hospital Name, District, State, Dose and Age Group
	and provide Options to select the respective Date and available Slots.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	hospital_name : str
		Name of Hospital where Vaccination is available for given District, State, Dose and Age Group
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Dates and Slots available on those dates (where the Vaccination is available for a given Hospital Name,
		District, State, Dose, Age Group) and Options to select, with Key as 'Option' and Value as another dictionary having
		Key as 'Date' and Value as 'Available Slots'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineSlots(web_page_data, 'MedStar Hospital Center', 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '81'}, '3': {'May 17': '109'}, '4': {'May 18': '78'},
		'5': {'May 19': '89'}, '6': {'May 20': '57'}, '7': {'May 21': '77'}
	}
	>>> print(fetchVaccineSlots(web_page_data, 'Eden Clinic', 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '137'}, '3': {'May 17': '50'}, '4': {'May 18': '78'},
		'5': {'May 19': '145'}, '6': {'May 20': '64'}, '7': {'May 21': '57'}
	}
	"""

	vaccine_slots = {}

	##############	ADD YOUR CODE HERE	##############
	slots = []
	for td in web_page_data:
		if(td.find_all("td", {"class": "age"})[0].text == age_group and 
				td.find_all("td", {"class": "dose_num"})[0].text == dose and 
					td.find_all("td", {"class": "state_name"})[0].text == state and 
						td.find_all("td", {"class": "district_name"})[0].text == district and
							td.find_all("td", {"class": "hospital_name"})[0].text == hospital_name):
			slots = [td.find_all("td", {"class": "may_{}".format(i+15)})[0].text for i in range(7)]

	date_list = [{"May {}".format(i+15): slots[i]} for i in range(len(slots))]
	vaccine_slots = {str(i+1): date_list[i] for i in range(len(slots))}
	##################################################

	return vaccine_slots


def openConnection():
	"""Opens a socket connection on the HOST with the PORT address.

	Returns
	-------
	socket
		Object of socket class for the Client connected to Server and communicate further with it
	tuple
		IP and Port address of the Client connected to Server
	"""

	client_socket = None
	client_addr = None

	##############	ADD YOUR CODE HERE	##############
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind((HOST, PORT))
		s.listen()
		client_socket, client_addr = s.accept()
	##################################################
	
	return client_socket, client_addr


def startCommunication(client_conn, client_addr, web_page_data):
	"""Starts the communication channel with the connected Client for scheduling an Appointment for Vaccination.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	client_addr : tuple
		IP and Port address of the Client connected to Server
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""

	##############	ADD YOUR CODE HERE	##############
	with client_conn:
		func_num = 1
		status = True
		while True:
			if func_num == 1:
				welcome_text = " ========================================================================\n|\n|                      Welcome to CoWin Chatbot                         |\n|\n ========================================================================\n\n\nSchedule an Appointment for Vaccination:\n"
				client_conn.send(welcome_text.encode('utf-8'))
				print("Client is connected at:  ('{}', {})".format(HOST,PORT))

			if func_num == 2:
				dose = getDose(client_conn)
				if dose == "2":
					dose = getSecondVaccinationDate(client_conn, dose)
				if dose == "quit":
					status = False
				if dose == "break":
					continue

			if func_num == 3:
				age_group = getAgeGroup(client_conn, dose)
				if age_group == "quit":
					status = False
				if age_group == "break":
					func_num -= 1
					continue

			if func_num == 4:
				state = getState(client_conn, dose, age_group)
				if state == "quit":
					status = False
				if state == "break":
					func_num -= 1
					continue

			if func_num == 5:
				district = getDistrict(client_conn, dose, age_group, state)
				if district == "quit":
					status = False
				if district == "break":
					func_num -= 1
					continue

			if func_num == 6:
				vaccine_center = getVaccineCenter(client_conn, dose, age_group, state, district)
				if vaccine_center == "quit":
					status = False
				if vaccine_center == "break":
					func_num -= 1
					continue

			if func_num == 7:
				slot = getSlot(client_conn, dose, age_group, state, district, vaccine_center)
				if slot == "quit":
					status = False
				if slot == "break":
					func_num -= 1
					continue

			if func_num == 8 or status == False:
				break

			func_num += 1

		stopCommunication(client_conn)
	##################################################


def stopCommunication(client_conn):
	"""Stops or Closes the communication channel of the Client with a message.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	"""

	##############	ADD YOUR CODE HERE	##############
	client_conn.send("\n<<< See ya! Visit again :)".encode('utf-8'))
	client_conn.close()
	##################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################


def getDose(client_conn):
	"""
		This function is used for the first question, 
		" Select dose of Vaccination ". This will take user input 
		and return choosen dose, or the ERROR according
		to the given input validation.
		------------
		Returns: str
	"""
	dose_choices = fetchVaccineDoses(web_page_data)
	question_1 = "\n>>> Select the Dose of Vaccination: \n{}\n".format(dose_choices)
	dose, flag = takeInput(client_conn, question_1, len(dose_choices))
	if flag:
		client_conn.send("\n<<< Invalid input provided {} time(s)! Try again.".format(3).encode('utf-8'))
		print("Invalid input detected {} time(s)!".format(3))
		print("Notifying the client and closing the connection!")
		return "quit"

	if dose == "quit":
		print("Client wants to quit!")
		print("Saying Bye to client and closing the connection!")
		return dose

	if dose == "break":
		return dose

	print("Dose selected: {}".format(dose))
	if dose == '2':
		client_conn.send("\n<<< Dose selected: {}\n".format(dose).encode('utf-8'))
		return dose

	client_conn.send("\n<<< Dose selected: {}".format(dose).encode('utf-8'))
	return dose


def getAgeGroup(client_conn, dose):
	"""
		This function is used for the second question, 
		" Select the Age Group ". This will take user input 
		and return choosen age group as "age_group", or the 
		ERROR according to the given input validation.
		-------------
		Returns: str
	"""
	age_group_choices = fetchAgeGroup(web_page_data, dose)
	question_2 = "\n>>> Select the Age Group: \n{}\n".format(age_group_choices)
	age_group, flag = takeInput(client_conn, question_2, len(age_group_choices))
	if flag:
		client_conn.send("\n<<< Invalid input provided {} time(s)! Try again.".format(3).encode('utf-8'))
		print("Invalid input detected {} time(s)!".format(3))
		print("Notifying the client and closing the connection!")
		return "quit"

	if age_group == "quit":
		print("Client wants to quit!")
		print("Saying Bye to client and closing the connection!")
		return age_group

	if age_group == "break":
		return age_group

	age_group = fetchAgeGroup(web_page_data, dose)[age_group]
	print("Age Group selected: {}".format(age_group))
	client_conn.send("\n<<< Selected Age Group: {}".format(age_group).encode('utf-8'))
	return age_group


def getState(client_conn, dose, age_group):
	"""
		This function is used for the third question, 
		" Select the State ". This will take user input 
		and return choosen state, or the ERROR according 
		to the given input validation.
		-------------
		Returns: str
	"""
	state_choices = fetchStates(web_page_data, age_group, dose)
	question_3 = "\n>>> Select the State: \n{}\n".format(state_choices)
	state, flag = takeInput(client_conn, question_3, len(state_choices))
	if flag:
		client_conn.send("\n<<< Invalid input provided {} time(s)! Try again.".format(3).encode('utf-8'))
		print("Invalid input detected {} time(s)!".format(3))
		print("Notifying the client and closing the connection!")
		return "quit"

	if state == "quit":
		print("Client wants to quit!")
		print("Saying Bye to client and closing the connection!")
		return state

	if state == "break":
		return state

	state = fetchStates(web_page_data, age_group, dose)[state]
	print("State selected: {}".format(state))
	client_conn.send("\n<<< Selected State: {}".format(state).encode('utf-8'))
	return state


def getDistrict(client_conn, dose, age_group, state):
	"""
		This function is used for the fourth question, 
		" Select the District ". This will take user input 
		and return choosen district, or the ERROR according 
		to the given input validation.
		-------------
		Returns: str
	"""
	district_choices = fetchDistricts(web_page_data, state, age_group, dose)
	question_4 = "\n>>> Select the District: \n{}\n".format(district_choices)
	district, flag = takeInput(client_conn, question_4, len(district_choices))
	if flag:
		client_conn.send("\n<<< Invalid input provided {} time(s)! Try again.".format(3).encode('utf-8'))
		print("Invalid input detected {} time(s)!".format(3))
		print("Notifying the client and closing the connection!")
		return "quit"

	if district == "quit":
		print("Client wants to quit!")
		print("Saying Bye to client and closing the connection!")
		return district

	if district == "break":
		return district

	district = fetchDistricts(web_page_data, state, age_group, dose)[district]
	print("District selected: {}".format(district))
	client_conn.send("\n<<< Selected District: {}".format(district).encode('utf-8'))
	return district


def getVaccineCenter(client_conn, dose, age_group, state, district):
	"""
	This function is used for the fifth question, 
		" Select the Vaccination Center Name ". This will take user input 
		and return choosen vaccine center as "vaccine_center", or the 
		ERROR according to the given input validation.
		-------------
		Returns: str
	"""
	hospital_vaccine_choices = fetchHospitalVaccineNames(web_page_data,district, state, age_group, dose)
	question_5 = "\n>>> Select the Vaccination Center Name: \n{}\n".format(hospital_vaccine_choices)
	vaccine_center, flag = takeInput(client_conn, question_5, len(hospital_vaccine_choices))
	if flag:
		client_conn.send("\n<<< Invalid input provided {} time(s)! Try again.".format(3).encode('utf-8'))
		print("Invalid input detected {} time(s)!".format(3))
		print("Notifying the client and closing the connection!")
		return "quit"

	if vaccine_center == "quit":
		print("Client wants to quit!")
		print("Saying Bye to client and closing the connection!")
		return vaccine_center

	if vaccine_center == "break":
		return vaccine_center

	vaccine_center = fetchHospitalVaccineNames(web_page_data,district, state, age_group, dose)[vaccine_center].popitem()[0]
	print("Hospital selected: {}".format(vaccine_center))
	client_conn.send("\n<<< Selected Vaccination Center: {}".format(vaccine_center).encode('utf-8'))
	return vaccine_center


def getSlot(client_conn, dose, age_group, state, district, vaccine_center):
	"""
	This function is used for the sixth question, 
		" Select one of the available slots to schedule the Appointment ". 
		This will take user input and return choosen slot, or the 
		ERROR according to the given input validation.
		-------------
		Returns: str
	"""
	vaccine_slot_choices = fetchVaccineSlots(web_page_data, vaccine_center, district, state, age_group, dose)
	question_6 = "\n>>> Select one of the available slots to schedule the Appointment: \n{}\n".format(vaccine_slot_choices)
	slot, flag = takeInput(client_conn, question_6, len(vaccine_slot_choices))
	if flag:
		client_conn.send("\n<<< Invalid input provided {} time(s)! Try again.".format(3).encode('utf-8'))
		print("Invalid input detected {} time(s)!".format(3))
		print("Notifying the client and closing the connection!")
		return "quit"

	if slot == "quit":
		print("Client wants to quit!")
		print("Saying Bye to client and closing the connection!")
		return slot

	if slot == "break":
		return slot


	slot = fetchVaccineSlots(web_page_data, vaccine_center, district, state, age_group, dose)[slot]
	for key, val in slot.items():
		date = key
		available_slots = val

	print("Vaccination Date selected: {}".format(date))
	print("Available Slots on that date: {}".format(available_slots))
	client_conn.send("\n<<< Selected Vaccination Appointment Date: {}".format(date).encode("utf-8")) 
	client_conn.send("<<< Available Slots on the selected Date: {}".format(available_slots).encode("utf-8")) 
	if available_slots == "0":
		client_conn.send("<<< Selected Appointment Date has no available slots, select another date!".encode('utf-8'))
		getSlot(client_conn, dose, age_group, state, district, vaccine_center)
	else:
		client_conn.send("<<< Your appointment is scheduled. Make sure to carry ID Proof while you visit Vaccination Center!".encode('utf-8'))


def getSecondVaccinationDate(client_conn, dose):
	"""
		This function is used for the seventh question, 
		" Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g. 12/5/2021 ". 
		This will take user input and returns the routine as per the validation.
		-------------
		Returns: str
	"""
	global ERROR
	client_conn.send("\n>>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g. 12/5/2021".encode("utf-8"))
	date = client_conn.recv(1024).decode('utf-8')
	if date == 'q' or date == 'Q':
		print("Client wants to quit!")
		print("Saying Bye to client and closing the connection!")
		return "quit"

	if date == 'b' or date == 'B':
		return "break"

	if date.isalpha() or "/" not in date:
		ERROR += 1
		if ERROR < 3:
			client_conn.send("\n<<< Invalid input provided {} time(s)! Try again.\n".format(ERROR).encode('utf-8'))
			print("Invalid input detected {} time(s)!".format(ERROR))
			return getSecondVaccinationDate(client_conn, dose)
		else:
			client_conn.send("\n<<< Invalid input provided {} time(s)! Try again.".format(ERROR).encode('utf-8'))
			print("Invalid input detected {} time(s)!".format(3))
			print("Notifying the client and closing the connection!")
			return "quit"

	day, month, year = date.split("/")
	try:
		date_format = datetime.date(int(year), int(month), int(day))
	except ValueERROR: 
		client_conn.send("\n<<< Invalid Date provided of First Vaccination Dose: {}\n".format(date).encode("utf-8"))
		return getSecondVaccinationDate(client_conn, dose)

	no_of_weeks = getWeeks(date)
	if datetime.date.today() < date_format :
		client_conn.send("\n<<< Invalid Date provided of First Vaccination Dose: {}".format(date).encode("utf-8"))
		return getSecondVaccinationDate(client_conn, dose)

	client_conn.send("\n<<< Date of First Vaccination Dose provided: {}".format(date).encode("utf-8")) 
	client_conn.send("\n<<< Number of weeks from today: {}".format(no_of_weeks).encode("utf-8"))

	if no_of_weeks >= 4 and no_of_weeks <= 8:
		client_conn.send("\n<<< You are eligible for 2nd Vaccination Dose and are in the right time-frame to take it.".encode("utf-8"))
		return dose

	if no_of_weeks > 8 :
		# client_conn.send("<<< You are eligible for 2nd Vaccination Dose and are in the right time-frame to take it.\n".encode("utf-8"))
		client_conn.send("<<< You have been late in scheduling your 2nd Vaccination Dose by {} weeks.".format(no_of_weeks - 8).encode("utf-8"))
		return dose

	if no_of_weeks < 4 :
		client_conn.send("\n<<< You are not eligible right now for 2nd Vaccination Dose! Try after {} weeks.".format(4 - no_of_weeks).encode("utf-8"))
		return "quit"


def getWeeks(date):
	"""
		This utility function is used to get the number of weeks
		between input date and today's date.
		-------------------------------
		Returns: Integer( No of weeks )
	"""
	formatted_date = datetime.datetime.strptime(date, "%d/%m/%Y")
	today = datetime.date.today()
	days = abs(datetime.date(int(today.year), int(today.month), int(today.day)) - datetime.date(int(formatted_date.year), int(formatted_date.month), int(formatted_date.day))).days
	return days//7


def takeInput(client_conn, question, dict_length):
	"""
		This utility function is used to take input from client,
		and check each case of validation and returns two variables
		data and Flag according to the cases.
		---------------------------------
		Returns: data = str, flag = bool
	"""
	global ERROR
	flag = False
	while True:
		client_conn.send(question.encode('utf-8'))
		data = client_conn.recv(1024).decode('utf-8')
		if data == 'q' or data == 'Q':
			data = "quit"
			return data, flag

		if data == 'b' or data == 'B':
			data = "break"
			return data, flag

		elif (data.isalpha()) or (not data.isalnum()) or (not data.isdigit()):
			ERROR += 1
			if ERROR < 3: 
				client_conn.send("\n<<< Invalid input provided {} time(s)! Try again.\n".format(ERROR).encode('utf-8'))
				print("Invalid input detected {} time(s)!".format(ERROR))
				continue
			if ERROR >= 3:
				flag = True
				return data, flag

		elif dict_length < int(data) or int(data) <= 0:
			ERROR += 1
			if ERROR < 3: 
				client_conn.send("\n<<< Invalid input provided {} time(s)! Try again.\n".format(ERROR).encode('utf-8'))
				print("Invalid input detected {} time(s)!".format(ERROR))
				continue
			if ERROR >= 3:
				flag = True
				return data, flag
		else:
			return data, flag
##############################################################


if __name__ == '__main__':
	"""Main function, code begins here
	"""
	url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	web_page_data = fetchWebsiteData(url_website)
	client_conn, client_addr = openConnection()
	startCommunication(client_conn, client_addr, web_page_data)
