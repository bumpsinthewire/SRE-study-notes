import re
from collections import Counter


failed_attempts: Counter = Counter()

try:
    with open("test_auth.log", "r") as f:
        for line in f:
            ip_result = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            if ip_result:
                failed_attempts[ip_result.group()] += 1
except FileNotFoundError:
    print("Error: The log file 'test_auth.log' was not found.")
    exit(1)

print("--- SSH Attack Report ---")
print(f"{'IP Address':<18} | {'Attempts'}")
print("-" * 30)

for ip, count in failed_attempts.most_common(3):
    print(f"{ip:<18} | {count}")
