from storage import JsonServerStorage, Secrets

secrets = Secrets()
storage = JsonServerStorage(secrets)

commands0 = ["whoami", "hostname"]

for server in storage.servers:
    server.execute_ssh_commands(commands0)
