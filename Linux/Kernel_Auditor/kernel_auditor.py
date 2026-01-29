import subprocess


# dictionary of desired parameter settings
DESIRED_STATE = {
    "net.ipv4.ip_forward": "0",
    "kernel.kptr_restrict": "1",
    "net.ipv4.conf.all.accept_redirects": "0",
    "kernel.perf_event_paranoid": "2",
    "net.ipv4.icmp_echo_ignore_broadcasts": "1",
}


def param_value(parameter):
    """
    Returns the configured setting value for a parameter.
    """
    value = subprocess.run(["sysctl", "-n", parameter], capture_output=True, text=True)
    return value.stdout.strip()


def selinux_mode():
    """
    Returns status of SELinux.
    """
    mode = subprocess.run(["getenforce"], capture_output=True, text=True)
    return mode.stdout.strip()


total_params = len(DESIRED_STATE)
passed_count = 0

for parameter, expected in DESIRED_STATE.items():
    current_val = param_value(parameter)

    if current_val != expected:
        print(f"The value for {parameter} does not match the desired state!")
        print(f"Please use: 'sysctl -w {parameter}={expected}' to fix")
    else:
        passed_count += 1


print("\n--- SUMMARY ---")
print(f"Parameters in compliance: {passed_count}/{total_params}")

selinux_value = "Enforcing"
selinux_current = selinux_mode()
if selinux_current != selinux_value:
    print(f"\nWARNING: SELinux is {selinux_current}. Expected {selinux_value}")
