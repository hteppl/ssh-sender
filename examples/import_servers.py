import traceback

from server import Server
from storage import JsonServerStorage, Secrets

secrets = Secrets()
storage = JsonServerStorage(secrets)

while True:
    # Prompt for the server details
    name = input("\n1. Enter server name: ")
    hostname = input("2. Enter hostname: ")
    username = input("3. Enter username (default: root): ") or "root"
    password = input("4. Enter password: ")
    port = input("5. Enter port (default 22): ")
    port = int(port) if port.isdigit() else 22

    # Create a new Server instance with encrypted password
    server = Server(
        secrets=secrets,
        name=name,
        hostname=hostname,
        username=username,
        password=secrets.encrypt(password),
        port=port,
    )

    try:
        # Attempt to execute an SSH command to verify the server connection
        out_data, err_data = server.execute_ssh_command("hostname")

        # If the command executes successfully, save the server
        if out_data and not err_data:
            storage.write(server)
            print(f" — Server {server.name} successfully added to the servers list!")
        else:
            print(f" — Server {server.name} failed to add:\n{err_data}")

    except Exception:
        print(f" — Server {server.name} failed to add:\n{traceback.format_exc()}")

    finally:
        server.close_ssh()  # Ensure the SSH connection is closed
