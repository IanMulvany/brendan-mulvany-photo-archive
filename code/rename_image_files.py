#!/Users/devian/opt/anaconda3/envs/bm_archive/bin/python
"""
Rename the captured image files based on the process setp

"""

def rename_file(image_path, new_name):
    import os
    os.rename(image_path, new_name)
    return new_name

