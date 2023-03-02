import os
import docker

client = docker.from_env()

def main(msg: str) -> str:
    container = client.containers.run('hello-world', detach=True)
    return 'Container started: ' + container.short_id

