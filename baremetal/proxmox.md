# Proxmox baremetal setup

Throughout this guide, anything written in `[square brackets]` is supposed to be replaced by you. Replace all 
of the text, including the brackets, unless otherwise mentioned.

Download the latest version of proxmox and burn to usb using etcher.
Insert usb, boot up server and roll through setup. 

Navigate to `https://[proxmox_ip]:8006` in browser.

login: `root`
password: the one you entered during setup

Complete online setup.

Next checkout the [template](./ubuntu.md) for a new Ubuntu container and set up some fundamental containers, such as
* [An SQL Server](../database/)
* An NFS Server
* An NGINX Server
