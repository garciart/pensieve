# Setup SSH Keys

> **NOTE**
>
> - The directions are for OpenSSH, not other remoting applications, such as WinRM.
> - I try to use the CLI as much as possible (i.e., Bash for Linux and PowerShell for Windows).
> - I wrote the Linux commands for Red Hat Enterprise Linux 8+ systems, but you can modify them to run on other Linux distributions.

-----

## Linux Node to Linux Node

Before starting:

- Ensure that an SSH client is running on the host node (e.g., `ps aux | grep ssh`) and an SSH server is running on the remote node (e.g., `sudo systemctl status sshd` or `ps aux | grep sshd`).
- If the client is not running on the host node, install an SSH-client-server application, such as OpenSSH (e.g., `sudo dnf install openssh-clients -y`).
- If the server is not running on the remote node:

  - Install an SSH-client-server application, such as OpenSSH (e.g., `sudo dnf install openssh-server -y`).
  - You may also have to enable the service (e.g., `sudo systemctl enable --now sshd`).
  - You may also have to allow incoming traffic over port 22 (e.g., `sudo firewall-cmd --zone=public --permanent --add-service=ssh && sudo firewall-cmd --reload`).

- Determine the asymmetric (public-key) cryptography system (e.g., `ecdsa`, `ed25519`, `rsa`, etc.) that both nodes can use (e.g., run `ssh -Q key` on both systems and compare.)

Steps:

1. Log into the host node as the user who will perform actions on the remote node.
2. Run `ssh-keygen`, specifying the asymmetric (public-key) cryptography system to use, the size of the key in bits, and a location for the key file; do not create a passphrase (e.g., `ssh-keygen -t rsa -b 4096 -f '~/.ssh/id_rsa' -N ""`). This will create an SSH key pair on the host node at `~/.ssh/id_rsa` and `~/.ssh/id_rsa.pub` (private and public keys, respectively).
3. Copy the key to the remote node:

    - Use `ssh-copy-id` to copy the key to the remote node (e.g., `ssh-copy-id username@remote.node.ip`). The default location on the remote node will be `~/.ssh/authorized_keys`.
    - If that does not work, try `cat ~/.ssh/id_rsa.pub | ssh username@remote.node.ip "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"`.

4. Attempt to connect to the remote node (e.g., `ssh username@remote.node.ip`).

    - The first time you connect to the remote node, you will be asked to confirm the host's authenticity. Type `yes` and press <kbd>ENTER</kbd>.
    - Next, you will be prompted to enter the password for the user who will perform actions on the remote node. Type in the password and press <kbd>ENTER</kbd>.

5. Once connected, enter `whoami` to ensure you are logged in as the user who will perform actions on the remote node.
6. Enter `exit` to log out of the remote node.
7. Reattempt to log in. You should not need to enter a password.

-----

## Linux Node to Windows Node

Before starting:

- Ensure that an SSH client is running on the host node (e.g., `ps aux | grep ssh`) and an SSH server is running on the Windows node (e.g., `Get-Service sshd`).
- If the client is not running on the host node, install an SSH-client-server application, such as OpenSSH (e.g., `sudo dnf install openssh-clients -y`).
- If the server is not running on the Windows node (example commands are in PowerShell):

  - Install an SSH-client-server application, such as OpenSSH (e.g., `Get-WindowsCapability -Online | ? Name -like 'OpenSSH.Server*' | Add-WindowsCapability -Online`).
  - You may also have to enable the service (e.g., `Start-Service sshd && Set-Service -Name sshd -StartupType 'Automatic'`).
  - You may also have to allow incoming traffic over port 22 (e.g., `New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22`).

- Determine the asymmetric (public-key) cryptography system (e.g., `ecdsa`, `ed25519`, `rsa`, etc.) that both nodes can use (e.g., run `ssh -Q key` on both systems and compare.)

Steps:

1. Log into the host node as the user who will perform actions on the Windows node.
2. Run `ssh-keygen`, specifying the asymmetric (public-key) cryptography system to use, the size of the key in bits, and a location for the key file; do not create a passphrase (e.g., `ssh-keygen -t rsa -b 4096 -f '~/.ssh/id_rsa' -N ""`). This will create an SSH key pair on the host node at `~/.ssh/id_rsa` and `~/.ssh/id_rsa.pub` (private and public keys, respectively).
3. Copy the key to the Windows node:

   - View and copy the public key on the host node (e.g., `cat ~/.ssh/id_rsa.pub`).
   - Log into the Windows node in a separate shell or window as the user who will perform actions on the Windows node.
   - Check if an `authorized_keys` file exists on the Windows node (e.g., `cat $env:USERPROFILE\.ssh\authorized_keys`). If not, create the `.ssh` directory on the Windows node (e.g., `New-Item -ItemType Directory -Force -Path $env:USERPROFILE\.ssh`).
   - Open the `authorized_keys` file on the Windows node (e.g., `notepad.exe $env:USERPROFILE\.ssh\authorized_keys`).
   - Append the contents of the public key from the host node into the `authorized_keys` file on the Windows node and save the file.
   - Assign the file the correct permissions (e.g., `icacls $env:USERPROFILE\.ssh\authorized_keys /inheritance:r /grant:r "${env:USERNAME}:(R)"`)

4. Attempt to connect to the Windows node (e.g., `ssh username@windows.node.ip`).

    - The first time you connect to the Windows node, you will be asked to confirm the host's authenticity. Type `yes` and press <kbd>ENTER</kbd>.
    - Next, you will be prompted to enter the password for the user who will perform actions on the Windows node. Type in the password and press <kbd>ENTER</kbd>.

5. Once connected, enter `whoami` to ensure you are logged in as the user who will perform actions on the Windows node.
6. Enter `exit` to log out of the Windows node.
7. Reattempt to log in. You should not need to enter a password.
