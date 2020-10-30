import requests
import json
BASE_URL='http://127.0.0.1:8000/'
END_POINT='api/'



def get_resource(id=None):
	data={}
	if id is not None:
		data = {'id':id}
	response = requests.get(BASE_URL+END_POINT,data=json.dumps(data))
	print(response.json())
	print(response.status_code)

#get_resource(1)


def create_resource():
	eno=int(input("Enter the Employee no: "))
	ename=input("Enter the Employee name: ")
	esalary=int(input("Enter the Employee salary: "))
	eaddress=input("Enter the Employee address: ")
	post_data = {'eno':eno,'ename':ename,'esalary':esalary,'eaddress':eaddress}

	response = requests.post(BASE_URL+END_POINT,data=json.dumps(post_data))
	print(response.json())
	print(response.status_code)

#create_resource()
def update_resource(id):
	eno=int(input("Enter the Employee no: "))
	ename=input("Enter the Employee name: ")
	esalary=int(input("Enter the Employee salary: "))
	eaddress=input("Enter the Employee address: ")
	update_data = {'id':id,'eno':eno,'ename':ename,'esalary':esalary,'eaddress':eaddress}
	response = requests.put(BASE_URL+END_POINT,data=json.dumps(update_data))
	print(response.json())
	print(response.status_code)


#update_resource(1)



def delete_resource(id):
	delete_data={'id':id}
	response = requests.delete(BASE_URL+END_POINT,data=json.dumps(delete_data))
	print(response.json())
	print(response.status_code)
#delete_resource(1)

if __name__ == '__main__':
	
	print("Select any of the below options:\n 1 :(get)\n 2 :(post)\n 3 :(update)\n 4 :(delete)\n")
	choice=int(input("Enter any of the above options: "))
	if choice==1:
		id=int(input("Enter id: "))
		get_resource(id)


	elif choice==2:
		create_resource()


	elif choice==3:
		id=int(input("Enter id: "))
		update_resource(id)

	elif choice==4:
		id=int(input("Enter id: "))
		delete_resource(id)


	else:
		print("Invalid option")
	

