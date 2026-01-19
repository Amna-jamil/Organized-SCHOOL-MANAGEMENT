# Moving Python files to src directory
import shutil
import os

# Define source and destination
source_dir = '.'
destination_dir = 'src'

# Move all Python files
for file_name in os.listdir(source_dir):
    if file_name.endswith('.py') and file_name != 'README.md' and file_name != '.gitignore':
        shutil.move(file_name, os.path.join(destination_dir, file_name))