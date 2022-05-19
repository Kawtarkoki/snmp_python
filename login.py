import paramiko

#Create object of SSHClient and connecting to SSH
ssh = paramiko.SSHClient()
ssh.connect('172.21.220.143', port=22, username='admin', password='ivG1z3!LL', timeout = 3)

#To add new host key to the local HostKeys object if missing
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Execute command on SSH terminal using exec_command
stdin, stdout, stderr = ssh.exec_command('get system status')

for name in stdout:
   print (name)
