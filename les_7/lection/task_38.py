import os
from pathlib import Path

"""
Перемещение файлов
"""

os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir', 'new_name.py'))
old_file = Path('new_name.py')
new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)