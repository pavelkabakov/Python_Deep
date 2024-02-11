import os
from pathlib import Path
"""
Для изменения текущего каталога можно воспользоваться функцией os.chdir. Она
принимает на вход абсолютный или относительный путь до нового текущего
каталога.
"""
print(os.getcwd())
print(Path.cwd())
os.chdir('../..')
print(os.getcwd())
print(Path.cwd())
