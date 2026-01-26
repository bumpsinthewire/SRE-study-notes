import subprocess


DESIRED_STATE = {
    "net.ipv4.ip_forward": "0",
    "kernel.kptr_restrict": "1",
    "net.ipv4.conf.all.accept_redirects": "0",
    "kernel.perf_event_paranoid": "2",
    "net.ipv4.icmp_echo_ignore_broadcasts": "1",
}


def param_value(parameter):
    value = subprocess.run(["sysctl", "-n", parameter], capture_output=True, text=True)
    return value.stdout.strip()


def selinux_mode(expected_mode):
    mode = subprocess.run(["getenforce"], capture_output=True, text=True)
    current_mode = mode.stdout.strip()
    return current_mode == expected_mode


for parameter, expected in DESIRED_STATE.items():
    if param_value(parameter) != expected:
        print(f"The value for {parameter} does not match the desired state!")
        print(f"Please use: 'sysctl -w {parameter}={expected}' to fix")
