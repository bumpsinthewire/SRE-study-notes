import subprocess


def get_listening_ports():
    ports_list = subprocess.run(["ss", "-tunl"], capture_output=True, text=True)
    lines = ports_list.stdout.strip().split("\n")

    listening_ports = []

    for line in lines[1:]:
        columns = line.split()
        local_address = columns[4]
        port = local_address.rsplit(":", 1)[-1]
        listening_ports.append(port)

    return set(listening_ports)


def check_ssh_config():
    try:
        with open("/etc/ssh/sshd_config", "r") as f:
            for line in f:
                clean_line = line.lstrip()

                if "PermitRootLogin" in clean_line and not clean_line.startswith("#"):
                    if "no" in clean_line:
                        return "SECURE"
                    else:
                        return "INSECURE"
            return "DEFAULT"
    except FileNotFoundError:
        return "FILE NOT FOUND"


if __name__ == "__main__":
    print("--- NETWORK EXPOSURE AUDIT ---")

    ports = get_listening_ports()
    ALLOWED_PORTS = ["22", "80", "443"]

    print("\n[+] Checking Listening Ports...")
    found_unauthorized = False
    for port in ports:
        if port not in ALLOWED_PORTS:
            print(f"[!] ALERT: UNRECOGNIZED PORT EXPOSED: {port}")
            found_unauthorized = True

    if not found_unauthorized:
        print(" [x] All listening ports are within policy.")

    print("\n[+] Checking SSH Configuration...")
    ssh_audit = check_ssh_config()

    if ssh_audit == "SECURE":
        print(" [x] SSH Policy: PermitRootLogin is DISABLED.")
    elif ssh_audit == "INSECURE":
        print(" [!] ALERT: SSH Policy: PermitRootLogin is ENABLED!")
    else:
        print(f"[-] NOTICE: SSH Policy is set to {ssh_audit}.")
