from flask import Flask
from flask import request, redirect, url_for, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
'''
@app.route('/api/v1/camera/register', methods=['GET', 'POST'])
def cam_reg():

	if request.method == 'POST':
		print(request.data)

		return Res('This is POST request')

	else:
		print(request.data)

		return print('This is GET request')
'''

'''
@app.route('/api/v1/camera/register', methods=['GET', 'POST'])
def cam_reg():

	if request.method == 'POST':
		print(request.headers)

		return print('This is POST request')

	else:
		print(request.headers)

		return print('This is GET request')
'''

'''  =================  BASIC  ====================
@app.route('/api/v1/camera/passenger/basic', methods=['GET', 'POST'])
def cam_basic():

	if request.method == 'POST':
		print(request.headers)

		return print('This is POST request')

	else:
		print(request.headers)

		return print('This is GET request')
'''

'''  ============================  LATEST RESGISTER   ===================================
@app.route('/api/v1/camera/register', methods=['GET', 'POST'])
def cam_reg():

	if request.method == 'GET':
		data = request.stream.read()

		return data
'''


'''
@app.route('/api/v1/camera/passenger/basic', methods=['GET'])
def cam_basic():

	data = request.get_json()

	id = data['id']
	face_type = data['face_type']
	age = data['age']
	gender = data['gender']

	return jsonify({'result' : 'Success!', 'id' : id, 'face_type' : face_type, 'age' : age, 'gender' : gender})
'''



''' if request.method == 'GET':
		res = request.get_data()

		return res 

'''

'''  ==================================     BASIC LATEST     ================================'''

'''@app.route('/passenger/basic', methods=['GET', 'POST'])
@app.route('/passenger/face', methods=['GET', 'POST'])'''
'''
@app.route('/passenger/<name>', methods=['GET', 'POST'])
def cam_data(name):

	print (request.get_json())
	response = {
   			"success":"true",
   			"msg":"ok"
		}
	return jsonify(response)



@app.route('/passenger/<username>', methods=['GET', 'POST'])
def cam_basic():
	print(request.get_json())
	response = {
   			"success":"true",
   			"msg":"ok"
		}
	return jsonify(response)



'''

@app.route('/passenger/basic', methods=['GET', 'POST'])
def cam_basic():
	data = request.get_json()
	print("\n============================  Basic ==============================\n")
	
	#print(data)

	id = data['id']
	age = data['age']
	vasid = data['vasid']
	body_pic = data['body_pic']
	channel = data['channel']
	direction = data['direction']
	face_direction = data['face_direction']
	face_pic = data['face_pic']
	face_type = data['face_type']
	gender = data['gender']
	matchscore = data['matchscore']
	mood = data['mood']
	start_time = data['start_time']
	track_length = data['track_length']
	track_type = data['track_type']
	
	print("\n")
	print('Id is : ', id)
	print('Age is : ', age)
	print('Vasid is : ', vasid)
	print('Body_pic is : ', body_pic)
	print('Channel is : ', channel)
	print('Direction is : ', direction)
	print('Face_direction is : ', face_direction)
	print('Face_pic is : ', face_pic)
	print('Face_type is : ', face_type)
	print('Gender is : ', gender)
	print('Matchscore is : ', matchscore)
	print('Mood is : ', mood)
	print('Start_time is : ', start_time)
	print('Track_length is : ', track_length)
	print('Track_type is : ', track_type)
	print("\n")
	print("\n==========================  End Basic ============================\n")

	'''
	for firstkey, big_list in dict.items():
    	print('print dict: ' + str(firstkey))
    for pair in big_list:
        print('print sets in dict: ' + str(pair))
        nextdict = pair
        for nextkey, small_list in nextdict.items():
            print('print each: ' + str(nextkey)+ '->' + str(small_list))
            #address each one
            print('pull just data: ' + str(nextdict[nextkey]))
	'''
	response = {
   			"success":"true",
   			"msg":"ok"
		}
	return jsonify(response)


@app.route('/passenger/face', methods=['GET', 'POST'])
def cam_face():
	
	data = request.get_json()
	print("\n============================  Face ==============================\n")
	#print (data)
	print("\n")

	id = data['id']
	vasid = data['vasid']
	channel = data['channel']
	face_pic = data['face_pic']
	#Face properties

	print('Id is : ', id)
	print('Vasid is : ', vasid)
	print('Channel is : ', channel)
	print('Face_pic is : ', face_pic)
	print("\n")
	print("\n==========================  End Face ============================\n")

	response = {
   			"success":"true",
   			"msg":"ok"
		}
	return jsonify(response)

@app.route('/passenger/body', methods=['GET', 'POST'])
def cam_body():
	
	data = request.get_json()
	print("\n============================  Body ==============================\n")
	#print (data)
	print("\n")

	id = data['id']
	vasid = data['vasid']
	channel = data['channel']
	body_pic = data['body_pic']

	print('Id is : ', id)
	print('Vasid is : ', vasid)
	print('Channel is : ', channel)
	print('Body_pic is : ', body_pic)
	print("\n")
	print("\n========================== End Body ============================\n")

	response = {
   			"success":"true",
   			"msg":"ok"
		}
	return jsonify(response)

@app.route('/passenger/feature', methods=['GET', 'POST'])
def cam_feature():

	data = request.get_json()
	print("\n============================  Feature ==============================\n")
	print (data)
	print("\n")
	print("\n==========================  End Feature ============================\n")
	
	response = {
   			"success":"true",
   			"msg":"ok"
		}
	return jsonify(response)


@app.route('/passenger', methods=['GET', 'POST'])
def cam_passenger():

	data = request.get_json()
	print("\n============================  IN/OUT ==============================\n")
	print (data)
	print("\n")
	print("\n==========================  End IN/OUT ============================\n")
	
	response = {
   			"success":"true",
   			"msg":"ok"
		}
	return jsonify(response)


@app.route('/thermodynamicChartBaseMap', methods=['GET', 'POST'])
def cam_chartBasemap():

	data = request.get_json()
	print("\n============================  Chart Basemap ==============================\n")
	print (data)
	print("\n")
	print("\n==========================  End Chart Basemap ============================\n")
	
	response = {
   			"success":"true",
   			"msg":"ok"
		}
	return jsonify(response)

@app.route('/thermodynamicChartData', methods=['GET', 'POST'])
def cam_chartData():

	data = request.get_json()
	print("\n============================  Chart Data ==============================\n")
	print (data)
	print("\n")
	print("\n==========================  End Chart Data ============================\n")
	
	response = {
   			"success":"true",
   			"msg":"ok"
		}
	return jsonify(response)


@app.route('/register', methods=['GET', 'POST'])
def cam_reg():

	if request.method == 'GET':

		response = {        
   			"success":"true",                     
   			"msg":"ok"                 
		}

		return response
	else:
		print("\n============================  Register Request  =============================\n")
		print(request.get_json())
		response = {        
   			"success":"true",
   			"token":"eryui34987321i",
   			"code":123,
   			"msg":"ok"        
		}
		print("\n==========================  End Register Request  ===========================\n")
		return jsonify(response)

'''   ============================  BASIC INFO JSON ret "NULL"  =================================

@app.route('/api/v1/camera/passenger/basic', methods=['GET', 'POST'])
def cam_basic():

	if request.method == 'GET':
		data = request.stream.read()

		return data

	else:
		print(request.headers)

		return print('This is POST request')


'''

'''
@app.route('/api/v1/camera/register', methods=['GET', 'POST'])
def cam_reg():

	if request.method == 'GET':
		res = request.data

		return jsonify(res)
'''


@app.route('/api/v1/camera/time', methods=['GET'])
def cam_time():
    response = {
   "success":"true",             
   "timestamp":15623652145625,  
   "time": datetime,
   "timezone":5,             
   "code":123,               
   "msg":"ok"
}
    return jsonify(response)


@app.route('/check')
def check():
	return print('This is just for Check')

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8080)