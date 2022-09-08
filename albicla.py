import json
import datetime

data_base = "user_data_base"
def read_data_base():
	file = open(data_base,"r")
	data = file.read()
	data = json.loads(data)
	return data

def save_data_base(email, password):
	file_content = read_data_base()
	file_content["users"].append({ "email": email, "password": password }) 
	content_as_json = json.dumps(file_content)
	file = open(data_base, 'w')
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
	password_conf = input("\nEnter password again: ")
	while password != password_conf:
			print("\nPassword incorrect! Try again: ")
			password = input("\nEnter your password: ")
			password_conf = input("\nEnter password again: ")
	return password

def registration():
	email = input("Enter your email: ")
	users = read_data_base()["users"]
	if check_email_presence(email, users) == True:
		return print('Invalid data!')
	password = check_passwords()
	save_data_base(email, password)

def login():
	email = input("\nEnter your email: ")
	password = input("\nEnter your password: ")
	users = read_data_base()["users"]
	attempt = 0
	validated_email = check_email_presence(email,users)
	is_password_valid = check_password_presence(password, users)
	while not(validated_email and is_password_valid):
		attempt += 1
		password = input("\nPassword incorrect! Try again: ")
		if attempt>1:
			print("\nLogin details incorrect! I'm calling the police!\n")
			return False
	print(f"\nHello {validated_email} !\n")
	return email

def generate_id():
	now = datetime.datetime.now()
	id = json.dumps(now.strftime('%H:%M, %d.%m.%y'))
	return id

def add_post(email, post, id):
	if not email:
		print('\nYou have not logged in yet!\n')
		return 
	file_content = read_data_base()
	file_content["posts"].append({ "email": email, "id": id, "post": post}) 
	content_as_json = json.dumps(file_content)
	file = open(data_base, 'w')
	file.write(content_as_json)
	file.close()
	return True

def new_post(email):
	if not email:
		print('\nYou have not logged in yet!\n')
		return 
	post = input("\nWrite your post! Max. 100 characters:\n")
	if len(post)<=100:
		id = generate_id()
		add_post(email, post, id)
	else: 
		print("\nPost is too long!\n")

def show_post(email):
	if not email:
		print('\nYou have not logged in yet!\n')
		return 
	base = read_data_base()
	all_posts = base["posts"]
	for post in all_posts:
		if email == post.get('email'):
			print(f'\n{post.get("post")}, {post.get("id")}')

def show_wall(email):
	if not email:
		print('\nYou have not logged in yet!\n')
		return 
	base = read_data_base()
	all_posts = base["posts"]
	for post in all_posts:
		if email != post.get('email'):
			print(f'\n{post.get("post")}, {post.get("id")}')

def log_out(email):
	if not email:
		print('\nYou have not logged in yet!\n')
		return 
	else:
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
