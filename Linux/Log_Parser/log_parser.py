import re


log_line = "Jan 21 14:00:01 server sshd[123]: Failed password for root from 192.168.1.50 port 54321 ssh2"
ip_result = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log_line)

if ip_result:
    ip = ip_result.group()
    print(f"Found IP: {ip}")

failed_attempts = {}

with open("test_auth.log", "r") as f:
    for line in f:
        if ip in failed_attempts:
            failed_attempts[ip] += 1
        else:
            failed_attempts[ip] = 1

print(failed_attempts)
