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
            "lv_name,vg_name,data_percent",
        ],
        capture_output=True,
        text=True,
    )

    vgs = volume_groups.stdout.strip()
    lvs = logical_volumes.stdout.strip()

    vg_stats = vgs.strip(",")
    vg_stat = {}

    for vg, size in enumerate(vg_stats):
        vg_stat[vg] = size

    return vg_stat, lvs


stats = get_storage_stats()
print(stats)
