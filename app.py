from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template, jsonify
from datetime import datetime
import os, binascii, uuid

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a007@localhost/camera'
db = SQLAlchemy(app)

#==================================  Importing the Models  =============================
from models import *

#==================================  Default Route  ====================================
@app.route('/')
def index():
	return render_template('index.html')

#===================================  Device Register API  =====================================
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

		#ran = binascii.hexlify(os.urandom(32))
		#token = jsonify(ran)
		uid1 = uuid.uuid4()
		uid2 = uuid.uuid4().hex
		data = request.get_json()
		#channel1 = 0
		#channel2 = 0
		#channel3 = 0
		#channel4 = 0

		print(data)
		print("\n")

		serialnum = data['serialnum']
		name = data['name']
		channelcount = data['channelcount']
		channeltype = data['channeltype']
		devicetype = data['devicetype']
		ip = data['ip']
		mac = data['mac']
		hardware = data['hardware']
		software = data['software']
		algorithm = data['algorithm']
		channel1 = channeltype['channel1']

		#for ch in channeltype:
		#	channel1 = ch['channel1']


		print('Serial number is : ', serialnum)
		print('Name is : ', name)
		print('Channel count is : ', channelcount)
		print('Channel type is : ', channeltype)
		print('Channel1 is : ', channel1)
		print('Device type is : ', devicetype)
		print('Ip is : ', ip)
		print('Mac is : ', mac)
		print('Hardware is : ', hardware)
		print('Software is : ', software)
		print('Algorithm : ', algorithm)
		print("\n")

		#========================================  Data Manipulation  ==========================================
		register = Register.query.filter_by(serial_no=serialnum).first()

		if register:
			register.last_updated=datetime.now()
			register.token=uid1
			db.session.commit()
		else:
			reg = Register(serial_no=serialnum, channel_count=channelcount, channel1=channel1, token=uid1, last_created=datetime.now(), last_updated=datetime.now(), name=name, device_type=devicetype, mac=mac, ip=ip, hardware=hardware, software=software, algorithm=algorithm)
			db.session.add(reg)
			db.session.commit()

		response = {        
   			"success":"true",
   			"token":uid1,
   			"code":123,
   			"msg":"ok"        
		}

		print("\n==========================  End Register Request  ===========================\n")

		return jsonify(response)

#========================================  Basic(data points) API  =====================
@app.route('/passenger/basic', methods=['GET', 'POST'])
def cam_basic():
	data = request.get_json()

	print("\n============================  Token ==============================\n")

	auth = request.headers['Authorization']

	print("\nThe token is : ", auth)
	print("\n")
	print(request.headers)
	
	print("\n============================  End Token ==============================\n")

	print("\n============================  Basic ==============================\n")
	
	print(data)

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

	#========================================  Data Manipulation  ==========================================

	result = Register.query.filter_by(serial_no=vasid).first()
	token = result.token
	db.session.rollback()
	if (token == auth):
		snapshot = Snapshot.query.filter_by(id=id).first()
		if snapshot:
			#==================  date update  ===================
			snapshot.last_updated=datetime.now()
			db.session.commit()
	        #==================  Entry in Basic Table  ==========
			bas = Basic(snap_id=id, age=age, direction=direction, face_direction=face_direction, face_type=face_type, gender=gender, match_score=matchscore, mood=mood, start_time=start_time, track_length=track_length, track_type=track_type)
			db.session.add(bas)
			db.session.commit()
        	
		else:
	    	#==================  Entry in Snapshot Table  =======
			ss = Snapshot(id=id, vasid=vasid, channel=channel, last_created=datetime.now(), last_updated=datetime.now())
			db.session.add(ss)
			db.session.commit()
	        #==================  Entry in Basic Table  ==========
			bas = Basic(snap_id=id, age=age, direction=direction, face_direction=face_direction, face_type=face_type, gender=gender, match_score=matchscore, mood=mood, start_time=start_time, track_length=track_length, track_type=track_type)
			db.session.add(bas)
			db.session.commit()

		response = {	
			"success":"true",
			"code":123,
			"msg":"ok"
		}
	else:
		response = {	
			"code":401
		}

	return jsonify(response)

#========================================  Face API  ================================
@app.route('/passenger/face', methods=['GET', 'POST'])
def cam_face():
	
	info = request.get_json()

	auth = request.headers['Authorization']

	print("\n============================  Face ==============================\n")
	#print (info)
	print("\n")

	id = info['id']
	vasid = info['vasid']
	channel = info['channel']
	face_pic = info['face_pic']

	print('Id is : ', id)
	print('Vasid is : ', vasid)
	print('Channel is : ', channel)
	print("==============================  Raw Face Pic  =========================\n")
	print('Face_pic is : ', face_pic)
	print("==============================  End Raw Face Pic  =========================\n")
	print("\n\n")

	#========================================  Data Manipulation  ==========================================

	result = Register.query.filter_by(serial_no=vasid).first()
	token = result.token
	db.session.rollback()
	if (token == auth):
		snapshot = Snapshot.query.filter_by(id=id).first()
		if snapshot:
			#==================  date update  ===================
			snapshot.last_updated=datetime.now()
			db.session.commit()
	        #==================  Entry in Face Table  ==========
			for fp in face_pic:
				data = fp['data']
				face_score = fp['face_score']
				filename = fp['filename']
				key_point = fp['key_point']
				type = fp['type']
				face = Face(snap_id=id, data=data, face_score=face_score, filename=filename, type=type)
				db.session.add(face)
				db.session.commit()
		else:
	    	#==================  Entry in Snapshot Table  =======
			ss = Snapshot(id=id, vasid=vasid, channel=channel, last_created=datetime.now(), last_updated=datetime.now())
			db.session.add(ss)
			db.session.commit()
	        #==================  Entry in Face Table  ==========
			for fp in face_pic:
				data = fp['data']
				face_score = fp['face_score']
				filename = fp['filename']
				key_point = fp['key_point']
				type = fp['type']
				face = Face(snap_id=id, data=data, face_score=face_score, filename=filename, type=type)
				db.session.add(face)
				db.session.commit()

		response = {	
			"success":"true",
			"code":123,
			"msg":"ok"
		}
	else:
		response = {	
			"code":401
		}

	'''for fp in face_pic:
		data = fp['data']
		face_score = fp['face_score']
		filename = fp['filename']
		key_point = fp['key_point']
		type = fp['type']
		print('Data is : ', data)
		print("\n")
		print('Face Score is : ', face_score)
		print('Filename is : ', filename)
		print('Key point is : ', key_point)
		print('Type is : ', type)
		print("\n")''' 
	print("\n==========================  End Face ============================\n")

	'''response = {
   			"success":"true",
   			"msg":"ok"
		}'''
	return jsonify(response)

#=======================================  Body API  ====================================
@app.route('/passenger/body', methods=['GET', 'POST'])
def cam_body():
	
	info = request.get_json()

	auth = request.headers['Authorization']

	print("\n============================  Body ==============================\n")
	#print (info)
	print("\n")

	id = info['id']
	vasid = info['vasid']
	channel = info['channel']
	body_pic = info['body_pic']

	print('Id is : ', id)
	print('Vasid is : ', vasid)
	print('Channel is : ', channel)
	print("==============================  Raw Body Pic  =========================\n")
	print('Body_pic is : ', body_pic)
	print("==============================  End Raw Body Pic  =========================\n")
	print("\n")

	#========================================  Data Manipulation  ==========================================

	result = Register.query.filter_by(serial_no=vasid).first()
	token = result.token
	db.session.rollback()
	if (token == auth):
		snapshot = Snapshot.query.filter_by(id=id).first()
		if snapshot:
			#==================  date update  ===================
			snapshot.last_updated=datetime.now()
			db.session.commit()
	        #==================  Entry in Body Table  ==========
			for bp in body_pic:
				body_roi = bp['body_roi']
				data = bp['data']
				face_roi = bp['face_roi']
				filename = bp['filename']
				body = Body(snap_id=id, data=data, filename=filename)
				db.session.add(body)
				db.session.commit()
		else:
	    	#==================  Entry in Snapshot Table  =======
			ss = Snapshot(id=id, vasid=vasid, channel=channel, last_created=datetime.now(), last_updated=datetime.now())
			db.session.add(ss)
			db.session.commit()
	        #==================  Entry in Body Table  ==========
			for bp in body_pic:
				body_roi = bp['body_roi']
				data = bp['data']
				face_roi = bp['face_roi']
				filename = bp['filename']
				body = Body(snap_id=id, data=data, filename=filename)
				db.session.add(body)
				db.session.commit()

		response = {	
			"success":"true",
			"code":123,
			"msg":"ok"
		}
	else:
		response = {	
			"code":401
		}

	'''for bp in body_pic:
		body_roi = bp['body_roi']
		data = bp['data']
		face_roi = bp['face_roi']
		filename = bp['filename']
		print("\n")
		print('Body Roi is : ', body_roi)
		print('Data is : ', data)
		print('Face Roi is : ', face_roi)
		print('Filename is : ', filename)
		print("\n")'''
	print("\n========================== End Body ============================\n")

	response = {
			"success":"true",
			"msg":"ok"
		}
	return jsonify(response)

#================================ API not hitting so far  ===============================
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

#====================================  API not hitting so far  ===========================
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

#=====================================  API not hitting so far  ==========================
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

#======================================  API not hitting so far  ==========================
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

#==============================  Get Request Time API ====================================
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

#=========================  Test Route  ===================================
@app.route('/check')
def check():
	return print('This is just for Check')

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8080)