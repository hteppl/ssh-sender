from storage import JsonServerStorage, Secrets

secrets = Secrets()
storage = JsonServerStorage(secrets)

commands0 = ["whoami", "hostname"]

for server in storage.servers:
    try:
        # Execute commands list
        server.execute_ssh_commands(commands0)
    finally:
        server.close_ssh()
