import os
def parent_directory():
  relative_parent = os.path.join("./", "../")
  abs_path_parent = os.path.abspath(relative_parent)
  return abs_path_parent

print(parent_directory())
