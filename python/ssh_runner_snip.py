"""A snippet that runs blocking commands on remote nodes using SSH.

NOTE:

- The script requires the sshpass binary, but it can be modified to use SSH keys.
- Use `;`, `&&`, `||`, or `|` to run, evaluate, or pipe multiple commands.

TODO:

- Replace sshpass with SSH keys.

Usage:

CLI - python -B ssh_runner_snip.py
From code:
    try:
        runner = SSHRunner(target='10.1.23.45', username='alice', password='password')
        result, err = runner.run(command='ls -la; whoami', shell=bash)
        msg = err if result is None else result
        print(msg)
    except (TypeError, ValueError, subprocess.TimeoutExpired, subprocess.CalledProcessError):
        print(f"Error: {str(e)}")
"""
import getpass
import os
import subprocess


class SSHRunner:
    """Class for running commands on remote nodes using SSH."""

    VALID_SHELLS = ['bash', 'photonos', 'powercli', 'powershell', 'pwsh', 'sh', 'zsh']
    INVALID_SHELL_MSG = f"Invalid shell. Must be one of the following: {VALID_SHELLS}"
    PARAMETER_ERR_MSG = "Error: '{0}' is an invalid type or has an invalid value."

    def __init__(self, target: str, username: str, password: str) -> None:
        """Instantiate object and initialize class variables.

        :param str target: The hostname or IPv4 address of the remote node.
        :param str username: Specifies the user to log in as on the remote machine.
        :param str password: The SSH password.

        :raises TypeError: If a parameter is the wrong type or empty.
        """
        # Validate inputs
        for _k, _v in locals().items():
            if _k != 'self' and (not isinstance(_v, str) or str(_v).strip() == ''):
                raise TypeError(self.PARAMETER_ERR_MSG.format(_k))

        # Set class variables
        self.target = target
        self.username = username
        self.password = password

    def run(self, command: str, shell: str = 'bash', timeout: int = 30) -> tuple:
        """Run commands on remote nodes using SSH.

        :param str command: The command to run.
        :param str shell: The shell to use, defaults to 'bash'.
        :param int timeout: The time limit in seconds, defaults to 30 seconds.

        :return tuple: The result of the command and any errors.

        :raises TypeError: If a parameter is the wrong type or empty.
        :raises ValueError: If the request shell is not supported.
        """
        # Validate inputs
        if not isinstance(command, str) or str(command).strip() == '':
            raise TypeError(self.PARAMETER_ERR_MSG.format(command))
        if not isinstance(shell, str) or str(shell) not in self.VALID_SHELLS:
            raise ValueError(self.INVALID_SHELL_MSG)
        if not isinstance(timeout, int) or int(timeout) < 1:
            raise TypeError(self.PARAMETER_ERR_MSG.format(timeout))

        try:
            # Put the password in an environment variable
            # so it does not appear in history or the process list
            _env = os.environ.copy()
            _env['SSHPASS'] = self.password

            if (command.split())[0].lower() in self.VALID_SHELLS:
                return None, 'Do not include the shell in the command.'

            # If PowerShell, add options
            _ps_tuple = ('powercli', 'powershell', 'pwsh')
            if shell in _ps_tuple:
                command = f"pwsh -NoProfile -Command {command}"

            # Build the command
            # Use `sshpass -e` to read the SSHPASS env variable
            # Use `User` option to enter emails as usernames
            _ssh_command = [
                'sshpass',
                '-e',
                'ssh',
                '-o', 'StrictHostKeyChecking=no',
                '-o', 'UserKnownHostsFile=/dev/null',
                '-o', f"User={self.username}",
                f"{self.target}",
                command
            ]

            # Run the command
            # NOTE: Set check to False to prevent exceptions due to the result of the command
            _result = subprocess.run(
                _ssh_command,
                shell=False,
                text=True,
                capture_output=True,
                timeout=timeout,
                env=_env,
                check=False
            )
            _output, _error = _result.stdout, _result.stderr

            return _output, _error
        except subprocess.TimeoutExpired:
            return None, 'Command timed out'
        # # Only needed if subprocess.run(check=True)
        # except subprocess.CalledProcessError as e:
        #     return None, f"Error: {e.stderr}"
        finally:
            if _env and 'SSHPASS' in _env:
                del _env['SSHPASS']


if __name__ == '__main__':
    try:
        ssh_user = input('Enter your username: ')
        ssh_password = getpass.getpass('Enter password: ')
        ssh_runner = SSHRunner(target='localhost', username=ssh_user, password=ssh_password)
        result, err = ssh_runner.run(command='whoami; pwd; ls -la', shell='bash')
        msg = err if str(result).strip() == '' else result
        print(msg)
    except (EOFError, TypeError, ValueError, subprocess.TimeoutExpired,
            subprocess.CalledProcessError) as e:
        print(f"Error: {str(e)}")
