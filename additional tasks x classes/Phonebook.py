import pickle
import os

array = []
errors = (ValueError,KeyboardInterrupt)
os.system('color f0')


def cls():
	os.system('cls')


class Data:
	def __init__(self,years='',month='',day=''):
		self.years = years
		self.month = month
		self.day = day

	def printDate(self):
		print('Years: {}.{}.{}'.format(self.day,self.month,self.years))

class members:
	def __init__(self,name='',age = Data(),job='',number='',adress=''):
		self.name = name
		self.age = age
		self.job = job
		self.number = number
		self.adress = adress

	#Getters

	def getName(self):
		return self.name

	#Setters

	def setName(self,name): self.name = name
	def setAge(self,age): self.age = age
	def setJob(self,job): self.job = job
	def setNumber(self,number): self.number = number
	def setAdress(self,adress): self.adress = adress


	def printInfo(self):
		cls()
		print('Name:',self.name)
		self.age.printDate()
		print('Job:',self.job)
		print('Number:',self.number)
		print('Adress:',self.adress)
		input('')

def creatContact():
	cls()
	contact = members()
	contact.setName(input('Name: '))
	contact.setAge(Data(input('Years: '),input('Month: '),input('Day: ')))
	contact.setJob(input('Job: '))
	contact.setNumber(input('Number: '))
	contact.setAdress(input('Adress: '))
	array.append(contact)
	saveContact()

def deleteContact():
	cls()
	showName()
	try:
		idContact = int(input('Введите индекс вашего контакта: '))
		print('Контакт',array[idContact-1].name,'удален!')
		del array[idContact-1]

		input()
	except IndexError:
		print('\nВы ввели неверный индекс')
		input('Enter для продолжения')
	saveContact()


def editContact():
	cls()
	showName()
	try:
		idContact = int(input('Введите индекс вашего контакта: '))
		if array[idContact - 1]:
			runEdit = True
		else:
			runEdit = False
		while runEdit:
			cls()
			print('Меню редактирования \n')
			print('1) - name\n2) - age\n3) - job\n4) - number\n5) - adress\n6) - выйти\n')
			action = int(input(' --> '))
			if action == 1:
				array[idContact-1].setName(input('Новое имя: '))
			elif action == 2:
				array[idContact-1].setAge(Data(input('Новый год: '),input('Новый месяц: '),input('Новый день: ')))
			elif action == 3:
				array[idContact-1].setJob(input('Новая работа: '))
			elif action == 4:
				array[idContact-1].setNumber(input('Новый номер: '))
			elif action == 5:
				array[idContact-1].setAdress(input('Новый адрес: '))
			elif action == 6:
				runEdit = False
	except IndexError:
		print('\nВы ввели неверный индекс!')
		input('Enter для продолжения: ')

	saveContact()

def showContact():
	showName()
	try:
		idContact = int(input('Введите индекс вашего контакта, -1 для выхода: '))
		if idContact == -1:
			pass
		else:
			array[idContact - 1].printInfo()
	except IndexError:
		print('\nВы ввелине неверный индекс')
		input('Enter для продолжения: ')

def saveContact():
	global array

	with open('saveContact.dat','wb') as f:
		pickle.dump(array,f)

def initSaveContact():
	global array

	try:
		with open('saveContact.dat','rb') as f:
			array = pickle.load(f)
	except:
		array = []

def showName():
	cls()
	j = 1
	for i in array:
		print(str(j),')',i.getName())
		j+=1


def menuContact():
	if len(array) > 0:
		print('Всего контактов: ',len(array),'\n')
	else:
		print('Контаков нету!\n\n\n\n')

	if len(array) != 0:
		if len(array) == 1:
			showMenuName()
			print('\n\n')
		else:
			showMenuName()
			print('\n')

def showMenuName():
	if len(array) <= 4:
		for i in array:
			print(i.getName())
	else:
		i = 0
		while i <= 3:
			print(array[i].getName())
			i+=1

while True:
	cls()
	initSaveContact()
	menuContact()
	try:
		action = int(input('1 - добавить контакт\n2 - показать информацию\n3 - редактировать контакт\n4 - удалить контакт\n------------------>  '))
		if action == 1:
			creatContact()
		elif action == 2:
			showContact()
		elif action == 3:
			editContact()
		elif action == 4:
			deleteContact()
		elif action == 9:
			exit()
	except errors:
		print('\nВы ввели неверное значение')
		input('Enter для продолжения: ')
