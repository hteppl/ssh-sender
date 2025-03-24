from typing import Optional, Tuple, List, Union

from paramiko.client import SSHClient, AutoAddPolicy
from paramiko.sftp_client import SFTPClient

from storage import Secrets


class Server:
    def __init__(
        self,
        secrets: Secrets,
        name: str,
        hostname: str,
        username: str,
        password: str,
        port: int = 22,
    ) -> None:
        self.secrets = secrets
        self.name = name
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        self.ssh_client: Optional[SSHClient] = None
        self.sftp_client: Optional[SFTPClient] = None

    def _connect_ssh(self) -> None:
        # Connect to the server via SSH
        if self.ssh_client is None or not self._is_connected_ssh():
            self.ssh_client = SSHClient()
            self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
            self.ssh_client.connect(
                hostname=self.hostname,
                port=self.port,
                username=self.username,
                password=self.secrets.decrypt(self.password),
            )

    def _connect_sftp(self) -> None:
        # Connect to the server via SFTP using an existing SSH connection
        self._connect_ssh()  # Ensure SSH is connected
        if self.sftp_client is None or self.sftp_client.get_channel().closed:
            self.sftp_client = self.ssh_client.open_sftp()

    def _is_connected_ssh(self) -> bool:
        # Check if the SSH connection is active
        return (
            self.ssh_client is not None
            and self.ssh_client.get_transport() is not None
            and self.ssh_client.get_transport().is_active()
        )

    def _is_connected_sftp(self) -> bool:
        # Check if the SFTP connection is active
        return self.sftp_client is not None and not self.sftp_client.get_channel().closed

    def execute_ssh_commands(self, commands: List[str]) -> None:
        # Execute multiple SSH commands
        print(f" — Processing server {self.hostname} ({self.name}):")
        for command in commands:
            self.execute_ssh_command(command)

    def execute_ssh_command(self, command: str) -> Tuple[str, str]:
        # Execute a single SSH command and return output/errors
        self._connect_ssh()
        print(f' — "{command}" >>> {self.hostname} ({self.name})')
        _, stdout, stderr = self.ssh_client.exec_command(command)

        out_data = stdout.read().decode()
        err_data = stderr.read().decode()

        if out_data:
            print(f" — OUTPUT <<< {self.hostname} ({self.name})\n | {out_data}")
        if err_data:
            print(f" — ERROR <<< {self.hostname} ({self.name})\n | {err_data}")

        return out_data, err_data

    def upload_sftp_file(self, remote_path: str, contents: Union[str, bytes]) -> None:
        # Upload a file to the server via SFTP
        self._connect_sftp()
        try:
            # Convert string to bytes if necessary
            if isinstance(contents, str):
                contents = contents.encode("utf-8")

            with self.sftp_client.open(remote_path, "wb") as remote_file:
                remote_file.write(contents)

            print(f" — SFTP >>> {self.hostname} ({self.name}) >>> {remote_path}")

        except Exception as e:
            print(f" — ERROR SFTP >>> {self.hostname} ({self.name}) - {str(e)}")
            self.close_sftp()

    def download_sftp_file(self, remote_path: str, local_path: str) -> None:
        # Download a file from the server via SFTP
        self._connect_sftp()
        try:
            self.sftp_client.get(remote_path, local_path)
            print(f" — {local_path} <<< {remote_path} SFTP {self.hostname} ({self.name})")

        except Exception as e:
            print(f" — ERROR SFTP <<< {self.hostname} ({self.name}) - {str(e)}")
            self.close_sftp()

    def close_ssh(self) -> None:
        # Close the SSH connection
        if self.ssh_client:
            self.ssh_client.close()
            self.ssh_client = None

    def close_sftp(self) -> None:
        # Close the SFTP connection
        if self.sftp_client:
            self.sftp_client.close()
            self.sftp_client = None
