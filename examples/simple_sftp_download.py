from storage import JsonServerStorage, Secrets

secrets = Secrets()
storage = JsonServerStorage(secrets)

for server in storage.servers:
    # Download a files
    server.download_sftp_file("/root/sample_text.txt", "../samples/downloaded_text.txt")
    server.download_sftp_file("/root/cat.png", "../samples/downloaded_cat.png")
