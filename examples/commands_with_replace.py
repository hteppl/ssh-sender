from storage import JsonServerStorage, Secrets

secrets = Secrets()
storage = JsonServerStorage(secrets)

commands0 = ["hostname", "hostnamectl set-hostname {host}", "hostname"]

for server in storage.servers:
    # Create a new list with replaced values
    commands = [command.replace("{host}", server.name) for command in commands0]

    # Execute the updated list of commands
    server.execute_ssh_commands(commands)
