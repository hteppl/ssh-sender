import json
import os
from abc import ABC, abstractmethod
from typing import List

from secrets import Secrets
from server import Server


# Abstract base class for server storage
class ServerStorage(ABC):
    def __init__(self, secrets: Secrets) -> None:
        self.secrets: Secrets = secrets

    @abstractmethod
    def write(self, server: Server) -> None:
        pass


class JsonServerStorage(ServerStorage):
    def __init__(self, secrets: Secrets, filename: str = "servers.json") -> None:
        super().__init__(secrets)
        self.storage_file = filename
        self.servers: List[Server] = self._load_servers()  # Load existing servers

    def _load_servers(self) -> List[Server]:
        # Load servers from a JSON file if it exists
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as file:
                servers_data = json.load(file)
                return [
                    Server(
                        self.secrets,
                        server["name"],
                        server["hostname"],
                        server["username"],
                        server["password"],
                        server["port"],
                    )
                    for server in servers_data
                ]
        return []  # Return an empty list if no file exists

    def _save_servers(self) -> None:
        # Save the list of servers to a JSON file
        with open(self.storage_file, "w") as file:
            json.dump(
                [
                    {
                        "name": server.name,
                        "hostname": server.hostname,
                        "username": server.username,
                        "password": server.password,
                        "port": server.port,
                    }
                    for server in self.servers
                ],
                file,
                indent=2,
            )

    def write(self, server: Server) -> None:
        # Add a server to the list and save to storage
        self.servers.append(server)
        self._save_servers()
