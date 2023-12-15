from netmiko import ConnectHandler

# Part 1: Creating Router Configuration Files
router_count = 3

for i in range(1, router_count + 1):
    filename = f"router_config_{i}.txt"
    with open(filename, 'w') as file:
        file.write(f"Router{i}\n")  # Hostname
        file.write("admin\n")  # Username
        file.write("password123\n")  # Password
        file.write("22\n")  # Port

# Part 2: Creating OSPF Routing Protocol File
ospf_filename = "ospf_routing_protocol.txt"

with open(ospf_filename, 'w') as file:
    file.write("router ospf 1\n")
    file.write("network 0.0.0.0 0.0.0.0 area 0\n")
    file.write("distance 110\n")  
    file.write("default-information originate\n")

# Part 3: Connecting to Routers and Configuring OSPF
router_ips = ['192.168.1.1', '192.168.1.2', '192.168.1.3']
password_secret_key = 'password123'  

for i, router_ip in enumerate(router_ips, start=1):
    device = {
        'device_type': 'cisco_ios',
        'ip': router_ip,
        'username': 'admin',
        'password': 'password123',
        'secret': password_secret_key,
        'port': 22,
    }

    # Establish SSH connection
    with ConnectHandler(**device) as ssh_conn:
        # Configure OSPF
        ospf_commands = [
            'router ospf 1',
            'network 0.0.0.0 0.0.0.0 area 0',
            f'distance 110',  
            'default-information originate',
        ]

        output = ssh_conn.send_config_set(ospf_commands)
        print(f"Router {i} OSPF Configuration Output:\n{output}")
