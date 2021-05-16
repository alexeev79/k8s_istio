from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/')
def get_order():
	
	cust_serv_url=os.environ.get('CUST_SVC_URL')
	prod_serv_url=os.environ.get('PROD_SVC_URL')
	
	serv_name=os.environ.get('SVC_NAME')	
	serv_ver=os.environ.get('SVC_VER')	

	resp = '{"Service":"'+ serv_name +'", "Version":' + serv_ver + '}\n'
	resp = resp + requests.get(cust_serv_url).content.decode('utf-8')
	resp = resp + requests.get(prod_serv_url).content.decode('utf-8')

	return resp

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=3030)