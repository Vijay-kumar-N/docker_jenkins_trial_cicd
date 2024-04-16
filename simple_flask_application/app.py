from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def welcome():
  return "Welcome to our website"

@app.route('/name')
def name():
  return "This is name of website"

@app.route('/ip')
def ip():
  hostname = socket.gethostname()     ## getting the IP address using socket.gethostbyname() method 
  ip_address = socket.gethostbyname(hostname)     
  # return ip_address
  return ip_address

# printing the hostname and ip_address
# print(f"Hostname: {hostname}")
# print(f"IP Address: {ip_address}")



if __name__ == '__main__':
  # app.run(host="0.0.0.0", port="8080")
  app.run()