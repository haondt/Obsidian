# Proxmox baremetal setup

Download the latest version of proxmox and burn to usb using etcher.
Insert usb, boot up server and roll through setup. 

Navigate to `https://[proxmox_ip]:8006` in browser.

login: `root`
password: the one you entered during setup

Complete online setup.

Next checkout the template for a new Ubuntu container and set up some fundamental containers, such as
* An SQL Server
* An NFS Server
* An NGINX Server
