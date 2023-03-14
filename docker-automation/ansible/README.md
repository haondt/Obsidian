Some ansible commands:

- Test connection by pinging
  ```bash
  ansible -i inventory.yml all -m ping
  ```
- Ping nodes in a specific group
  ```bash
  ansible -i inventory.yml docker_hosts -m ping
  ```
- Print the full compiled config of your inventory
  ```bash
  ansible-inventory -i inventory.yml --list
  ```