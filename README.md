# SSH Sender

![GitHub License](https://img.shields.io/github/license/hteppl/ssh-sender)
![Python Version](https://img.shields.io/badge/python-3.x-blue)

SSH Sender is a lightweight and efficient tool for executing SSH commands across multiple Linux servers.
It helps automate server management tasks, making administration simpler and more efficient.

## Features

- Execute commands on multiple servers simultaneously
- Basic secure password storage to avoid hardcoding credentials
- Support for SFTP file upload and download
- Asynchronous execution for better performance
- Easily customizable and extendable example scripts
- Secure and lightweight solution for remote server management
- Built-in base logging for better debugging and monitoring

## How to use

It's important to note that this project is not a standalone Python module. Instead, it provides a collection of base
classes with example scripts to help you automate server management tasks.
Example scripts can be found in the [Examples](https://github.com/hteppl/ssh-sender/tree/master/examples) folder.

## Installation

Clone this repository locally:

```bash
git clone https://github.com/hteppl/ssh-sender.git
cd ssh-sender
```

Create a virtual environment:

```bash
python -m venv .venv
```

### Activate the Virtual Environment

On Linux/macOS:

```bash
source .venv/bin/activate
```

On Windows (cmd):

```bash
.venv\Scripts\activate
```

### Install Dependencies

To install the required dependencies in your virtual environment:

```bash
pip install -r requirements.txt
```

Now you can test some example scripts
from the [Examples](https://github.com/hteppl/ssh-sender/tree/master/examples) folder!

## Contribute

Contributions to ssh-sender are warmly welcomed. Whether it's bug fixes, new features, or documentation
improvements, your input helps make this project better. Here's a quick guide to contributing:

1. **Fork & Branch**: Fork this repository and create a branch for your work.
2. **Implement Changes**: Work on your feature or fix, keeping code clean and well-documented.
3. **Test**: Ensure your changes maintain or improve current functionality, adding tests for new features.
4. **Commit & PR**: Commit your changes with clear messages, then open a pull request detailing your work.
5. **Feedback**: Be prepared to engage with feedback and further refine your contribution.

Happy contributing! If you're new to this, GitHub's guide
on [Creating a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
is an excellent resource.