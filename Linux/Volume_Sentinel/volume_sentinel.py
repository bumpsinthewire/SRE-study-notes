import subprocess


def get_storage_stats():
    volume_groups = subprocess.run(
        ["vgs", "--noheadings", "--separator", ",", "-o", "vg_name,vg_free"],
        capture_output=True,
        text=True,
    )
    logical_volumes = subprocess.run(
        [
            "lvs",
            "--noheadings",
            "--separator",
            ",",
            "-o",
            "lv_name,vg_name,data_percent",
        ],
        capture_output=True,
        text=True,
    )

    vgs = volume_groups.stdout.strip(",")
    lvs = logical_volumes.stdout.strip(",")

    return vgs, lvs


print(get_storage_stats())
