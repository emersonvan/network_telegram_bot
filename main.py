import Constants as keys
from telegram.ext import *
import Responses as R
import os
#from napalm import get_network_driver
from netmiko import ConnectHandler

print("BOT STARTED...")

def start_command(update, context):
	update.message.reply_text("Say something to start, /help for help:")

def help_command(update, context):
	update.message.reply_text("Please type time for current time \nping + IP or Hostname to perform ping basic connectivity test \n/ssh to run SSH commands.")
def ssh_command(update, context):
	update.message.reply_text("Type /uptime to check switch uptime\n/version to check switch Version")

def uptime_command(update, context):
	iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.56.90',
    'username': 'admin',
    'password': 'cisco123',
}

	net_connect = ConnectHandler(**iosv_l2_s1)
	output = net_connect.send_command('show version | include uptime')
	print(output)
	update.message.reply_text(output)


def version_command(update, context):
	iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.56.90',
    'username': 'admin',
    'password': 'cisco123',
}

	net_connect = ConnectHandler(**iosv_l2_s1)
	output = net_connect.send_command('show version')
	print(output)
	update.message.reply_text(output)


## this is being used for NAPALM SCRIPT def ssh_command(update, context):
	#update.message.reply_text("Type uptime to check switch uptime\n ")
	#driver = get_network_driver('ios')
	#iosvl2 = driver('192.168.56.90', "admin", "cisco123")
	#iosvl2.open()

	#ios_output = iosvl2.get_facts()
	#print (ios_output)
	#update.message.reply_text(ios_output)

def handle_message(update, context):
	text = str(update.message.text).lower()
	response = R.sample_responses(text)

	update.message.reply_text(response)

def error(update, context):
	print(f"update {update} caused error {context.error}")


def main():
	updater = Updater(keys.API_KEY, use_context=True)
	dp = updater.dispatcher
	
	dp.add_handler(CommandHandler("start", start_command))
	dp.add_handler(CommandHandler("help", help_command))
	dp.add_handler(CommandHandler("ssh", ssh_command))
	dp.add_handler(CommandHandler("uptime", uptime_command))
	dp.add_handler(CommandHandler("version", version_command))
	dp.add_handler(MessageHandler(Filters.text, handle_message))

	dp.add_error_handler(error)
	updater.start_polling()
	updater.idle()

main()

