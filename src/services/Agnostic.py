import os.path
from pathlib import Path


def create_path(path):
    return str(Path(path))


class Agnostic:

    @staticmethod
    def path(folder_path):
        return create_path(folder_path)

    @staticmethod
    def paths(*paths):
        folder_paths = [create_path(path) for path in paths]
        return os.path.join(*folder_paths)
