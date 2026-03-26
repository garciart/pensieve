# Ansible Notes

-----

## ansible.cfg Notes

- Run `ansible-config init --disabled` to view all available default options.
- Run `ansible-config init --disabled -t all` to include plugin options.
- Run `ansible-config init --disabled > ansible_default.cfg` or `ansible-config init --disabled -t all > ansible_with_plugins.cfg` to capture all options in a file. For safety, all options will be commented and inactive.

-----

## Inventory Notes

- `inventory.ini`

  - To view groups and nodes, use `ansible-inventory --inventory inventory.ini --graph`.
  - To convert to YAML, use `ansible-inventory -i inventory.ini --list --yaml`.

- `inventory.yml`
  - To view groups and nodes, use `ansible-inventory --inventory inventory.yml --graph`.
