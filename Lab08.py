import paramiko
import time

router_ip = "192.168.1.1"
username = "admin"
password = "Admin!"

commands = [
    "enable",
    "configure terminal",
    "username november password HelloWorld! privilege 15",
]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(router_ip, username=username, password=password, timeout=5)
    print("Connected to the router.")

    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(command)
        time.sleep(1)
        print(f"Command: {command}")
        print(stdout.read().decode())

except Exception as e:
    print(f"Error: {e}")

finally:
    ssh.close()
