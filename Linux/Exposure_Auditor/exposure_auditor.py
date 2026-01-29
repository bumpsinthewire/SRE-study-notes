import subprocess


def get_listening_ports():
    ports_list = subprocess.run(["ss", "-tunlp"], capture_output=True, text=True)
    ports = ports_list.stdout.strip()
    return ports


output = get_listening_ports()

print(output)
