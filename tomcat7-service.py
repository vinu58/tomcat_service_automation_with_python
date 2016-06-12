#!/usr/bin/python
# service status check with restart, stop and start options

import os
import subprocess

status = raw_input("what you need to do on tomcat service ? start or stop\n")

os.environ["JAVA_HOME"] = '/usr/lib/jvm/java-1.7.0-openjdk-amd64'
os.environ["CATALINA_HOME"] = '/root/tomcat7/apache-tomcat-7.0.69/'

if (status == "start"):
	os.getcwd()
	os.chdir("/root/tomcat7/apache-tomcat-7.0.69/bin")
	os.getcwd()
	subprocess.call ('sh catalina.sh start' , shell=True)
	print "Tomcat has started successfully"
else:
	os.getcwd()
        os.chdir("/root/tomcat7/apache-tomcat-7.0.69/bin")
        os.getcwd()
        subprocess.call ('sh catalina.sh stop' , shell=True)
        print "Tomcat has stopped successfully"


