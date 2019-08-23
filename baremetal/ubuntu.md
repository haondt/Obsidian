# Basic Ubuntu Container Setup

Create a new container 
* Open Proxmox web interface

```
https://[Proxmox server ip]:8006/
```

* Click `Create CT`
* Walk through the steps of creating a new container. Use default settings unless
otherwise mentioned
  * General
    * Set a hostname
    * Set a password
  * Template
    * If you don't have any available yet:
      * Close the container creation window
      * on the left hand toolbar navigate to Datacenter > pve > local (pve)
      * Content > click `Templates` > find Ubuntu 16.04
      * Click `Download`
      * Start over
    * Template > Ubuntu 16.04
  * Root Disk
    * Disk Size > Whatever you want, I usually leave at 8 GB
  * CPU
    * Cores: Choose whatever is appropriate for your application. I default to 2.
  * Memory
    * Memory: Same as above. I default to 4096.
  * Network
    * IPv4: DHCP
    * IPv6: DHCP
  * DNS
  * Confirm
* Start container

---

Configure the new container

Install some common apps

```
apt-get update
locale-gen "en_US.UTF-8"
apt-get install vim openssh-server python3-pip
```
    
Enable ssh

```
vim /etc/systemd/system/network-online.target.wants/networking.service
```

Change `TimeoutStartSec=5min` to `TimeoutStartSec=1sec`

Finish enabling ssh

```
systemctl enable ssh
systemctl start ssh
```

Add a user for whatever application you are running

```
adduser [username]
usermod -aG sudo [username]
```

Check the servers ip address and gateway

```
up addr show | grep 192 && route | grep default
```

Set the ip as static in your router settings, if you need a static ip.
