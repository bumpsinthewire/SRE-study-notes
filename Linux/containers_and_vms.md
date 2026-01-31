---
title: "containers_and_VMs"
date: "2026-01-24"
type: study_notes
tags: [study, linux]
---

# containers_and_VMs

## Key Concepts

VM's run on a hypervisor and let you chunk up the resources of the host system  
Containers are extremely portable and lightweight. They contain everything you need to run a full application independent of the host system

## Commands & Examples

For dealing with images:  
`docker search [image]` lets you find a pre-built container  
`docker pull [image]` pulls down the container that you want  
`docker images` shows you the images on your system currently  
`docker rmi [image]` to remove an image from your system  
`docker build` allows you to allows you to create an image from a dockerfile  

For dealing with containers:  
`docker run [options] [image]` to start a container on your system  
`-d` to "detach" from the container and run it in the background  
`-p [incoming:outgoing]` sort of like NAT. you specify traffic coming in on a port that goes out to a different port in the container  
`--name [name]` lets you specify the name you want the container to have on your system  
add `--restart always` to ensure the container is always persistent  
`docker ps` shows you the running containers on your system  
`-a` shows ALL containers on your system, even ones that are not running  
`docker start [container]` will start a container that is not running (get the container ID from `docker ps (-a)`)  
`docker stop [container]` will stop a running container  
`docker rm [container]` will remove a container from your system  

For dealing with VMs:
`virsh` lets you manage VMs from the CLI  
`virsh define [definition_file]` creates the VM to be used later (inactive)  
`virsh list` shows the VMs on your system  
`--all` shows even the ones that are powered off  
`virsh start [VM_name]` starts a VM. If the name contains spaces, wrap it in ""  
`virsh reboot [VM_name]` reboots a VM  
`virsh reset [VM_name]` forces a reboot on a VM  
`virsh shutdown [VM_name]` shuts down a VM  
`virsh destroy [VM_name]` forces a shutdown (equivalent to unplugging a physical machine)  
`virsh undefine [VM_name]` deletes a VM, but not its data  
`--remove-all-storage` deletes a VM and its data  
`virsh autostart [VM_name]` tells a VM to autostart on boot  
`--disable` disables the autostart functionality  
`virsh dominfo [VM_name]` gives you information about the resources set for a VM  
`virsh set[command] [VM_name]` lets you change configuration for a VM. Note that the "set" command is not 2 words, it is combined with the rest of the command (like "setvcpus")  
there are options and commands that are often needed after the `VM_name` in this command as well  
changes do not take effect until the VM has been cycled  
`virsh edit [VM_name]` opens a config file for the VM that you can edit instead of using individual commands  
`virsh console [VM_name]` lets you open a console session to a VM  

`virt-install` is used to create a VM and its definition file through the command and some options (there are A LOT of options)  
`--memory [memory_amount]` set how much memory you want the VM to have  
`--name [VM_name]` set the name for the VM  

## Questions & Notes

add your user to the `docker` group so that you don't have to preface every signle `docker` command with `sudo`  
you can add a tag when you `docker pull` by adding ":[version_number]" to the name of the container/image you are pulling  
instead of just using `docker --help`, you can also use `docker [command] --help` for additional information  
while `run` and `start` seem similar, `run` is more for building a container and then starting it, while `start` just starts a container that was previously created  
you must `rm` (remove) a container before `rmi` (removing) it's image. you also have to stop a container before removing it  
use `virsh help [command]` for additional help

## Resources

[Docker Hub](https://hub.docker.com)

## Next Steps

Building a Dockerfile  
Docker Compose is used for defining multi-container applications on a single host  
Docker Swarm is used for managing multiple Docker hosts as one entity  

### Parent Note

- [Linux Study Journey](./README.md)
