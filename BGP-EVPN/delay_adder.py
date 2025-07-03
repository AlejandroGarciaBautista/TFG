import yaml
import subprocess

with open("topology.yml", "r") as file:
    data = yaml.safe_load(file)

links = data['topology']['links']

delay = "0.5ms"
# delay = "1.5ms"
# delay = "10ms"
# delay = "30ms"

for link in links:
    ep1, ep2 = link['endpoints']
    
    node1, iface1 = ep1.split(":")
    node2, iface2 = ep2.split(":")

    cmd1 = [
    "containerlab", "tools", "netem", "set",
    "-n", f"clab-tfg-frr-ansible-{node1}",
    "-i", iface1,
    "--delay", delay,
    "--rate", "1000000"
    ]

    print(f"Ejecutando: {' '.join(cmd1)}")
    subprocess.run(cmd1)

    cmd2 = [
    "containerlab", "tools", "netem", "set",
    "-n", f"clab-tfg-frr-ansible-{node2}",
    "-i", iface2,
    "--delay", delay,
    "--rate", "1000000"
    ]

    print(f"Ejecutando: {' '.join(cmd2)}")
    subprocess.run(cmd2)
