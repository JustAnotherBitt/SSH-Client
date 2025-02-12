# SSH Client with Paramiko

## Overview
This is a simple SSH client written in Python using the `paramiko` library. It allows users to connect to a remote server via SSH, execute commands, and receive output directly in the terminal.

## Features
- Connects to a remote host via SSH
- Allows execution of shell commands
- Displays command output and error messages
- Supports connection to `localhost`
- Exits cleanly when `exit` is entered

## Requirements
- Python 3.x
- `paramiko` library (install using `pip install paramiko`)

## Installation
1. Clone this repository or download the script.
2. Ensure you have Python installed.
3. Install the required dependency:
   ```sh
   pip install paramiko
   ```

## Usage
1. Run the script:
   ```sh
   python script.py
   ```
2. Enter the required connection details:
   - **IP Address** (Press ENTER for localhost)
   - **Username**
   - **Password**
3. After connecting, you can enter commands to execute on the remote server.
4. Type `exit` to close the connection.

## Example
```
IP address (press ENTER for localhost): 192.168.1.10
Username: user
Password: ******
Connecting to 192.168.1.10...
-# ls
file1.txt  file2.txt  script.py
-# whoami
user
-# exit
Bye...
```
<p align="center">
<img src="https://github.com/user-attachments/assets/7dbdb5a0-7105-4224-a976-1fbea907d5c2" alt="" width="500">
</p>


## Notes
- Ensure SSH is enabled on the target machine.
  You can use the following commands:
  ```
  sudo systemctl start ssh
  ssh user@127.0.01
  ```
- The script uses `AutoAddPolicy` to accept unknown hosts automatically.
- It is recommended to use SSH keys instead of passwords for better security.



