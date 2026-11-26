"""A snippet that runs blocking commands on remote nodes using SSH.

Requires asyncssh
"""
import asyncio
import getpass

import asyncssh

VALID_SHELLS = ['bash', 'photonos', 'powercli', 'powershell', 'pwsh', 'sh', 'zsh']


async def run_ssh_cmd(command: str, username: str, password: str, target: str,
                      port: int = 22, shell: str = 'sh') -> asyncssh.SSHCompletedProcess:
    """Run an SSH command on a remote node and collect the output.

    :param str command: The command(s) to run.
    :param str username: The SSH username.
    :param str password: The SSH password.
    :param str target: The node where the command(s) will be executed.
    :param int port: The port to use, defaults to 22.
    :param str shell: The command shell, defaults to 'sh'.
    :return asyncssh.SSHCompletedProcess: A tuple containing the stdout, stderr, and rc.
    """
    if (command.split())[0].lower() in VALID_SHELLS:
        raise ValueError('Do not include the shell in the command.')

    # If PowerShell, add options
    _ps_tuple = ('powercli', 'powershell', 'pwsh')
    if shell in _ps_tuple:
        command = f"pwsh -NoProfile -Command {command}"

    print('Command: ', command)

    _conn = await asyncssh.connect(target, port=port,
                                   username=username, password=password,
                                   client_keys=None, known_hosts=None)
    _output = await _conn.run(command)
    _conn.close()
    return _output

if __name__ == '__main__':
    try:
        ssh_user = input('Enter your username: ')
        ssh_password = getpass.getpass('Enter password: ')

        output = asyncio.run(run_ssh_cmd(command='whoami; pwd; ls -la', shell='bash',
                                         target='localhost',
                                         username=ssh_user,
                                         password=ssh_password))
        print(f"Output: {output.stdout.strip()}")
        print(f"Error: {output.stderr.strip()}")
        print(f"Exit Status: {output.exit_status}")
    except (ValueError, asyncssh.Error) as e:
        print(f"Error: {str(e)}")
