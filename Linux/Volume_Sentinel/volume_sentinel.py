import subprocess


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

    vgs = volume_groups.stdout.strip()
    lvs = logical_volumes.stdout.strip()

    return vgs, lvs


stats = get_storage_stats()
print(stats)
