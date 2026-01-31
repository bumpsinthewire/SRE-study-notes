import subprocess
import shutil


def get_storage_stats():
    # Gather data
    vg_raw = (
        subprocess.run(
            [
                "sudo",
                "vgs",
                "--noheadings",
                "--separator",
                ",",
                "-o",
                "vg_name,vg_free",
            ],
            capture_output=True,
            text=True,
        )
        .stdout.strip()
        .split(",")
    )

    lv_raw = (
        subprocess.run(
            [
                "sudo",
                "lvs",
                "--noheadings",
                "--separator",
                ",",
                "-o",
                "lv_path,vg_name",
            ],
            capture_output=True,
            text=True,
        )
        .stdout.strip()
        .split(",")
    )

    # Separate VG data
    vg_name = vg_raw[0].strip()
    vg_free = vg_raw[1].replace("<", "").replace("g", "").strip()

    # Get the path for the LV
    lv_path = lv_raw[0].strip()

    # Calculate usage
    total, used, free = shutil.disk_usage("/")
    percent_used = (used / total) * 100

    # output logic
    if percent_used > 80:
        print(f"\n[!] ALERT: Logical volume {lv_path} is at {percent_used:.2f}%!")
        print(f"    Volume Group '{vg_name}' has {vg_free}GB free.")
        print(f"    ACTION: Run 'sudo lvextend -r -L +5G {lv_path}' to expand.")
    else:
        print(f"\n[x] Storage Health: {lv_path} is at {percent_used:.2f}% capacity.")

    return vg_free, percent_used


vg_free_space, current_usage = get_storage_stats()
