"""A snippet that runs blocking commands on remote nodes using SSH.

Requires paramiko
"""
import getpass
import hashlib
import paramiko

# Define a custom get_fingerprint function


def get_fingerprint_improved(self):
    """Declare that the use of MD5 encryption is not for security purposes,
    to overcome connection issues to servers with FIPS security standards.
    """
    return hashlib.md5(self.asbytes(), usedforsecurity=False).digest()


if __name__ == '__main__':
    try:
        ssh_user = input('Enter your username: ')
        ssh_password = getpass.getpass('Enter password: ')

        # Apply the monkey-patch
        paramiko.PKey.get_fingerprint = get_fingerprint_improved

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(hostname='localhost', username=ssh_user, password=ssh_password)

        stdin, stdout, stderr = client.exec_command('whoami; pwd; ls -la')
        print(f"Input: {stdin.read().decode()}")
        print(f"Output: {stdout.read().decode()}")
        print(f"Error: {stderr.read().decode()}")
    except (paramiko.SSHException) as e:
        print(f"Error: {str(e)}")
    finally:
        client.close()
