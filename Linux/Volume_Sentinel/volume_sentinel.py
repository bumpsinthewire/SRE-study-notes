import subprocess
import shutil


def get_storage_stats():
    volume_groups = subprocess.run(
        ["sudo", "vgs", "--noheadings", "--separator", ",", "-o", "vg_name,vg_free"],
        capture_output=True,
        text=True,
    )
    logical_volumes = subprocess.run(
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

    vgs = volume_groups.stdout.strip().split(",")
    lvs = logical_volumes.stdout.strip().split(",")

    vg_dict = {vgs[0]: vgs[1].replace("<", "")}
    lv_path = lvs[0]

    usage = shutil.disk_usage(lv_path)
    lv_dict = {lvs[1]: usage}

    return vg_dict, lv_dict


stats = get_storage_stats()
print(stats)
