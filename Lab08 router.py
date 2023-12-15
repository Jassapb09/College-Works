import paramiko
import time

router_ip = "192.168.0.1"
ssh_username = "admin"
ssh_password = "Admin123"

commands_to_execute = [
    "enable",
    "configure terminal",
    "username november password HelloWorld! privilege 15",
]

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh_connection.connect(router_ip, username=ssh_username, password=ssh_password, timeout=5)
    print("Connection established with the router.")

    for cmd in commands_to_execute:
        stdin, stdout, stderr = ssh_connection.exec_command(cmd)
        time.sleep(1)
        print(f"Executing command: {cmd}")
        print(stdout.read().decode())

except Exception as error:
    print(f"Error occurred: {error}")

finally:
    ssh_connection.close()
