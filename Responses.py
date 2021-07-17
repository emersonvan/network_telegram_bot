from datetime import datetime
import os
from netmiko import ConnectHandler
import re

def sample_responses(input_text):
	user_message = str(input_text).lower()

	if user_message in ("hello", "hi"):
		return "Hello, how are you?"
	if user_message in ("name", "name?"):
		return "I'm Network Automation BOT, AKA NWBOT!"
	if user_message in ("time", "time?","time now?"):
		now = datetime.now()
		date_time = now.strftime("%d/%m/%y, %H:%M:%S")
		return str(date_time)
	if "ping" in user_message:
		hostname = user_message
		hostname.replace("ping","")
		print(hostname)
		response_ping = os.system("ping -n 1 " +str(hostname.strip("ping ")))
		if response_ping ==0:
			print(hostname, "is up")
			hostup = (hostname, "is up")
		else:
			print(hostname, "is down")
			hostup = (hostname, "is down")
		return str(hostup)

	if "ssh " in user_message:
		ip_addr = user_message
		device_IP = re.sub('[^0-9,.]','', ip_addr)
		cli_input = re.sub('[0-9,.]','', ip_addr)
		command_cli = cli_input.strip("ssh")
		

		output_cli=user_message.strip("ssh ")
		iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': device_IP,
    'username': 'admin',
    'password': 'cisco123',
		}
		
		net_connect = ConnectHandler(**iosv_l2_s1)
		output = net_connect.send_command("terminal length 0")
		output = net_connect.send_command(command_cli)
		return output
		print(output)
	

		
	return "I didn't understand, please try again or type /help"

