import time
from concurrent.futures import ThreadPoolExecutor

from storage import JsonServerStorage, Secrets

secrets = Secrets()
storage = JsonServerStorage(secrets)

commands0 = ["whoami", "hostname"]
delay = 0  # Increase delay as you needed


def process_server_with_delay(server, commands: list, index: int) -> None:
    time.sleep(index * delay)
    server.execute_ssh_commands(commands)


# Execute async commands
for server in storage.servers:
    with ThreadPoolExecutor(max_workers=4) as executor:  # or use max_workers=len(storage.servers)
        for index, server in enumerate(storage.servers):
            executor.submit(process_server_with_delay, server, commands0, index)
