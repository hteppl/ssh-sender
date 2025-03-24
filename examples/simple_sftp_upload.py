from storage import JsonServerStorage, Secrets

secrets = Secrets()
storage = JsonServerStorage(secrets)

for server in storage.servers:
    try:
        # Upload a text file with some text replaces
        with open("../samples/sample_text.txt", "r") as file:
            contents = file.read()
            contents = contents.replace("{name}", "hteppl")
            contents = contents.replace("$name", "https://github.com/hteppl")
            server.upload_sftp_file("/root/sample_text.txt", contents)

        # Upload a binary file (e.g., an image)
        with open("../samples/cat.png", "rb") as file:
            server.upload_sftp_file("/root/cat.png", file.read())
    finally:
        server.close_sftp()
