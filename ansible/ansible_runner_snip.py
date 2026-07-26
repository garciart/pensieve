"""A snippet that used CLI arguments.

Usage:
- python -B ansible_runner_snip.py
"""
import os
import ansible_runner

cwd = os.getcwd()

# Run a playbook
r = ansible_runner.run(private_data_dir=cwd, playbook='say_hello.yml', rotate_artifacts=1)
# r is an ansible_runner Runner class object,
# not a Transmitter, Worker, or Processor class object
# Ignore any Pylance issues that may appear
print(f"Status: {r.status}")
print(f"Final stdout: {r.stdout.read()}")  # type: ignore[reportAttributeAccessIssue]

# Run an ad-hoc command
out, err, rc = ansible_runner.interface.run_command(
    executable_cmd='ansible',
    cmdline_args=['all', '--module-name', 'ansible.builtin.ping', '--inventory', 'inventory.ini']
)

# Run another ad-hoc command
out, err, rc = ansible_runner.interface.run_command(
    executable_cmd='ansible',
    cmdline_args=['all', '-m', 'ansible.builtin.debug',
                  '-a', "msg='Hello, World!'", '-i', 'inventory.ini']
)
