import os
import socket
import threading
import subprocess

print(r"""
███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝     ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗     ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                       By GalacticPepino
""")

if os.name == "nt":
    ping_cmd = "ping -n 1 -w 500"
    null = "nul"
else:
    ping_cmd = "ping -c 1 -W 1"
    null = "/dev/null"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
s.close()
network = ".".join(local_ip.split(".")[:-1])

print(f"[INFO] Tu IP: {local_ip}")
print(f"[INFO] Escaneando red: {network}.0/24\n")

found_ips = set()
lock = threading.Lock()

def get_mac(ip):
    try:
        output = subprocess.check_output("arp -a", shell=True).decode("latin-1")
        for line in output.splitlines():
            parts = line.split()
            if len(parts) >= 2 and parts[0] == ip:
                return parts[1]
    except:
        pass
    return "Desconocida"

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Desconocido"

def ping_ip(ip):
    response = os.system(f"{ping_cmd} {ip} > {null} 2>&1")
    if response == 0:
        with lock:
            if ip in found_ips:
                return
            found_ips.add(ip)
        mac = get_mac(ip)
        hostname = get_hostname(ip)
        print(f"[+] {ip}\n    └─ MAC: {mac}\n    └─ Nombre: {hostname}")

threads = []
max_threads = 50

for i in range(1, 255):
    ip = f"{network}.{i}"
    t = threading.Thread(target=ping_ip, args=(ip,))
    threads.append(t)
    t.start()

    while threading.active_count() > max_threads:
        pass

for t in threads:
    t.join()

print(f"\n[INFO] Dispositivos encontrados: {len(found_ips)}")