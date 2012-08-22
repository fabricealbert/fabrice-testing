import paramiko
import sys
import getpass


    
user = raw_input("enter user")
pwd = getpass.getpass()
host = '172.21.1.1'
cmd = "sh proc cpu"
print user
print pwd


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=user, password=pwd) 
stdin, stdout, stderr = ssh.exec_command(cmd)
for line in stdout.readlines():
    print line
ssh.close()