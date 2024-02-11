import os
from pathlib import Path

"""
если необходимо
создать несколько вложенных друг в друга каталогов, код будет следующим:
"""

os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir()  # FileNotFoundError
Path('some_dir/dir/new_path_dir').mkdir(parents=True)
