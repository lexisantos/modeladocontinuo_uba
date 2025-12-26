import os
import glob

paths = glob.glob('nb*.ipynb')
for i, path in enumerate(paths):
    os.rename(path, path.replace(f'nb{(i+1):02d}', 'Lab'))
