# DNF to Homebrew Commands

Map of DNF commands to Homebrew commands.

---

## System Updates & Maintenance

| Task                         | DNF Command                    | Homebrew Equivalent  | Notes                                                        |
| ---------------------------- | ------------------------------ | -------------------- | ------------------------------------------------------------ |
| Refresh package lists        | `dnf check-update / makecache` | `brew update`        | Updates Homebrew itself and its package definitions.         |
| Upgrade all packages         | `sudo dnf upgrade`             | `brew upgrade`       | Upgrades all outdated packages to their latest versions.     |
| Upgrade a single package     | `sudo dnf upgrade <pkg>`       | `brew upgrade <pkg>` | Upgrades only the named package.                             |
| Check for outdated packages  | `dnf check-update`             | `brew outdated`      | Lists installed packages that have newer versions available. |
| Clean cache and old versions | `sudo dnf clean all`           | `brew cleanup`       | Removes cached downloads and old package versions.           |
| Check system health          | `dnf check`                    | `brew doctor`        | Diagnoses common configuration and path issues.              |

---

## Package Management

| Task                       | DNF Command                | Homebrew Equivalent         | Notes                                        |
| -------------------------- | -------------------------- | --------------------------- | -------------------------------------------- |
| Install a package          | `sudo dnf install <pkg>`   | `brew install <pkg>`        | Homebrew does not use sudo.                  |
| Install a GUI app          | `sudo dnf install <pkg>`   | `brew install --cask <app>` | Casks apply to macOS desktop applications.   |
| Remove a package           | `sudo dnf remove <pkg>`    | `brew uninstall <pkg>`      | Removes the specified package.               |
| Remove unused dependencies | `sudo dnf autoremove`      | `brew autoremove`           | Cleans up orphaned dependencies.             |
| Search for a package       | `dnf search <term>`        | `brew search <term>`        | Searches available formulae and casks.       |
| Show package details       | `dnf info <pkg>`           | `brew info <pkg>`           | Displays version, dependencies, and caveats. |
| List installed packages    | `dnf list --installed`     | `brew list`                 | Lists all installed formulae and casks.      |
| Reinstall a package        | `sudo dnf reinstall <pkg>` | `brew reinstall <pkg>`      | Rebuilds or re-downloads the package.        |

---

## Repositories & Services

| Task                       | DNF Command                     | Homebrew Equivalent              | Notes                                                             |
| -------------------------- | ------------------------------- | -------------------------------- | ----------------------------------------------------------------- |
| Add a repository           | `dnf config-manager --add-repo` | `brew tap <user/repo>`           | Adds third-party Git repositories (taps) to Homebrew.             |
| List repositories          | `dnf repolist`                  | `brew tap`                       | Displays all currently tapped repositories.                       |
| Manage background services | `systemctl start/stop <svc>`    | `brew services start/stop <svc>` | Wraps launchctl on macOS or systemctl on Linux.                   |
| Export/Import package list | `dnf history userinstalled`     | `brew bundle dump`               | Creates a Brewfile that can be restored with brew bundle install. |
