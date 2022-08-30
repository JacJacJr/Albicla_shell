import json
import datetime

def read_base():
	file = open("baza_user","r")
	data = file.read()
	data = json.loads(data)
	return data

def save_base(email, password):
	file_content = read_base()
	file_content["users"].append({ "email": email, "password": password }) 
	content_as_json = json.dumps(file_content)
	file = open('baza_user', 'w')
	file.write(content_as_json)
	file.close()

def check_email_presence(email, users):
	for user in users:
		if email == user["email"]:
			return email
	return False		

def check_password_presence(password, users):
	for user in users:
		if password == user["password"]:
			return True
	return False

def check_passwords():
	password = input("\nEnter your password: Min. 8 characters ")
	while len(password) < 8:
		password = input("\nPassword is too short! Try again: ")
	password2 = input("\nEnter password again: ")
	while password != password2:
			print("\nPassword incorrect! Try again: ")
			password = input("\nEnter your password: ")
			password2 = input("\nEnter password again: ")
	return password

def registration():
	email = input("Enter your email: ")
	users = read_base()["users"]
	if check_email_presence(email, users) == True:
		return False
	password = check_passwords()
	save_base(email, password)

def login():
	email = input("\nEnter your email: ")
	password = input("\nEnter your password: ")
	users = read_base()["users"]
	turn =1
	validated_email = check_email_presence(email,users)
	is_password_valid = check_password_presence(password, users)
	while not(validated_email and is_password_valid):
		turn += 1
		password = input("\nPassword incorrect! Try again ")
		if turn>1:
			print("\nLogin details incorrect! I'm calling the police!")
			return False
	print(f"\nHello {validated_email} !\n")
	return email

def generat_id():
	now = datetime.datetime.now()
	id = json.dumps(now.strftime('%H:%M, %d.%m.%y'))
	return id

def add_post(email, post, id):
	if not email :
		print('\nYou have not logged in yet!')
		return 
	file_content = read_base()
	file_content["posts"].append({ "email": email, "id": id, "post": post }) 
	content_as_json = json.dumps(file_content)
	file = open('baza_user', 'w')
	file.write(content_as_json)
	file.close()
	return True

def new_post(email):
	if not email :
		print('\nYou have not logged in yet!')
		return 
	post = input("\nWrite your post! MAx. 100 characters")
	if len(post)<=100:
		id = generat_id()
		add_post(email, post, id)
	else: 
		print("\nPost is too long!")

def show_post(email):
	if not email :
		print('\nYou have not logged in yet!')
		return 
	base = read_base()
	all_posts = base["posts"]
	for post in all_posts:
		if email == post.get('email'):
			print(f'{post.get("post")}, {post.get("id")}')

def show_wall(email):
	if not email :
		print('\nYou have not logged in yet!')
		return 
	base = read_base()
	all_posts = base["posts"]
	for post in all_posts:
		if email != post.get('email'):
			print(f'{post.get("post")}, {post.get("id")}')

def log_out(email):
	if not email :
		print('\nYou have not logged in yet!')
		return 
	else :
		email == False
		return email

#"INTERFACE"
action = int(input("""\n
	What do you want to do?
	1- Registration
	2- Log in
	3- Add new post
	4- Show your table
	5- Show your wall
	0- Log out
	\n"""))
while action != 0:
	if action == 1:
		registration()
	elif action == 2:
		email = login()
	elif action == 3:
		email = email
		new_post(email)
	elif action == 4:
		show_post(email)
	elif action == 5:
		show_wall(email)

	action = int(input('\nWhat next?: '))