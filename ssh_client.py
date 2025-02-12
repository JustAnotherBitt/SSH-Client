import paramiko

host = input("IP adress (press ENTER for localhost): ")
user = input("Username: ")
passwd = input("Password: ")
localhost = "localhost"

# Creates an SSH client instance
client = paramiko.SSHClient()

# Makes the host known to allow connection
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Establishes SSH connection
if host.strip():
    print(f"Connecting to {host}...")
    client.connect(hostname=host, username=user, password=passwd)
else:
    print("Connecting to localhost...")
    client.connect(hostname=localhost, username=user, password=passwd)

while True:

    # Captures the user's command and removes extra spaces
    cmd = input("-# ").strip()

    if cmd.lower() == "exit":
        print("Bye...")
        client.close()
        break

    # Sends the command to the server via SSH
    stdin, stdout, stderr = client.exec_command(cmd)
    stdin.channel.shutdown_write()

    # Displays the output of the command
    for line in stdout:
        print(line.strip())

    # Displays errors, if any
    error_message = stderr.readlines()
    if error_message:
        print("Error:", "".join(error_message).strip())
