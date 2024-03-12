import os
import unittest
from src.services.Agnostic import Agnostic


def is_windows():
    return os.name == 'nt'


class AgnosticTest(unittest.TestCase):

    def test_agnostic_path(self):
        if is_windows():
            expected_folder = f"c:\\Users\\random-user\\Pictures\\favorite-pictures"
            actual_folder = Agnostic.path(expected_folder)
            self.assertEqual(expected_folder, actual_folder)
        else:
            expected_folder = f"c:/Users/random-user/Pictures/favorite-pictures"
            actual_folder = Agnostic.path(expected_folder)
            self.assertEqual(expected_folder, actual_folder)

    def test_appending_of_strings(self):
        if is_windows():
            expected_folder = f"folder_1\\folder_2\\folder_3"
            actual_folder = Agnostic.path(expected_folder)
            actual_folder_paths = Agnostic.paths("folder_1", "folder_2", "folder_3")
            self.assertEqual(expected_folder, actual_folder)
            self.assertEqual(expected_folder, actual_folder_paths)
        else:
            expected_folder = f"folder_1/folder_2/folder_3"
            actual_folder = Agnostic.path(expected_folder)
            actual_folder_paths = Agnostic.paths("folder_1", "folder_2", "folder_3")
            self.assertEqual(expected_folder, actual_folder)
            self.assertEqual(expected_folder, actual_folder_paths)

    def test_agnostic_paths(self):
        if is_windows():
            expected_folder = f"c:\\Users\\random-user\\Pictures\\favorite-pictures"
            actual_folder = Agnostic.paths("c:/Users", "random-user", "Pictures", "favorite-pictures")
            self.assertEqual(expected_folder, actual_folder)
        else:
            expected_folder = f"c:/Users/random-user/Pictures/favorite-pictures"
            actual_folder = Agnostic.paths("c:/Users", "random-user", "Pictures", "favorite-pictures")
            self.assertEqual(expected_folder, actual_folder)


if __name__ == '__main__':
    unittest.main()
