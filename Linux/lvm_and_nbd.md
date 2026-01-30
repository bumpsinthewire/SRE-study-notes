---
title: "lvm_and_nbd"
date: "2026-01-30"
type: study_notes
tags: [study, linux]
---

# lvm_and_nbd

## Key Concepts

LVM (Logical Volume Manager) helps you manage multiple partitions within a disk
    PV - Physical Volume (the physical disk you are working with)
    VG - Volume Group (think of this like a virtual disk)
    LV - Logical Volume (user defined portion of a VG)
    PE - Physical Extents (smaller pieces of a VG that get assigned to an LV)

NBD (Network Block Devices) are remote partitions that you can use on your system
    uses a client-server model

## Commands & Examples

LVM:
`lvmdiskscan` will show you your PV's
`pvcreate [disk]` creates a PV from a disk
`pvremove [disk]` removes a PV from your system
`pvs` shows which PV's are currently attached to LVM and their size/free space
    `pvdisplay` is more in-depth

`vgcreate [name] [PVs]` creates a named group of PVs
`vgextend [name] [PVs]` adds additional PVs to an exisiting VG
`vgreduce [name] [PVs]` removes a PV from a VG (only if there is no data on it)
`vgs` shows information about our VGs
    `vgdisplay` is more in-depth

`lvcreate [options] [VG]` creates an LV
    `--size` specifies the size
    `--name` specifies the name
`lvs` list your LVs
`lvdisplay` is more in-depth
`lvresize` resize an LV
    `--extents` OR `-l` specifies how many PEs to use from the VG in percent form
        syntax is a bit weird here so consult the *man* page
    `--size` lets you specify the exact size you want the LV to be
    `--resizefs` also resizes any filesystem on the LV

NBD:
`/etc/nbd-server/config` is the location for the config file of the NBD server
    to give the NBD daemon *root* priveleges, you can change *nbd* to *root* or uncomment the *user* and *group* lines
        *ideal so that it can read and write from block devices*
    add `allowlist = true` in this [generic] section so that NBD can share what it has available
    you then add the partitions that you want to sure at the bottom of the file in this format:
    `[partition2]`
        exportname=/dev/sda1
use `systemctl restart nbd-server.service` to make changes take effect

`sudo modprobe nbd` extends the kernel to handle NBD (non-persistent)
edit the `/etc/modules-load.d/modules.conf` file with *nbd* to make it persistent

`nbd-client [IP/hostname] -N [name]` adds a remote partition
`nbd-client -d [device_name]` to detach a NBD
`nbd-client -l [IP/hostname]` lists available blocks on the remote system

## Questions & Notes

`sudo apt install lvm2` to install LVM
you can continue to add PVs to VGs while the system is running
the *path* to an LV is in the form of `/dev/name_of_vg/name_of_lv`

NBD utilities create a special file called `/dev/nbd0` that redirects to the remote block
`sudo apt install nbd-server` installs NBD server utility
`sudo apt install nbd-client` installs NBD client utility

### Parent Note

- [Linux Study Journey](./README.md)
