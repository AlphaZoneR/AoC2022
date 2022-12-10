# --- Part Two ---
# Now, you're ready to choose a directory to delete.

# The total disk space available to the filesystem is 70000000. To run the update, you 
# need unused space of at least 30000000. You need to find a directory you can delete 
# that will free up enough space to run the update.

# In the example above, the total size of the outermost directory (and thus the total 
# amount of used space) is 48381165; this means that the size of the unused space must 
# currently be 21618835, which isn't quite the 30000000 required by the update. 
# Therefore, the update still requires a directory with total size of at least 8381165 to 
# be deleted before it can run.

# To achieve this, you have the following options:
# Delete directory e, which would increase unused space by 584.
# Delete directory a, which would increase unused space by 94853.
# Delete directory d, which would increase unused space by 24933642.
# Delete directory /, which would increase unused space by 48381165.
# Directories e and a are both too small; deleting them would not free up enough space. 
# However, directories d and / are both big enough! Between these, choose the smallest: 
# d, increasing unused space by 24933642.

# Find the smallest directory that, if deleted, would free up enough space on the 
# filesystem to run the update. What is the total size of that directory?
import typing

from day7.common import parse_output_filesystem
from day7.filesystem import FileSystem
from day7.node import DirectoryNode, Node
from utils import get_lines

# INPUT = 'day7/example'
INPUT = 'day7/input'

FS_SIZE = 70_000_000
UPDATE_SIZE = 30_000_000

lines = get_lines(INPUT, trim=True)
fs: FileSystem = parse_output_filesystem(lines)


def is_directory_and_larger_than_builder(size_limit: int) -> typing.Callable:
    def actual_func(node: Node):
        return type(node) == DirectoryNode and node.size > size_limit

    return actual_func

used_space = fs.root.size
free_space = FS_SIZE - used_space
missing_space = UPDATE_SIZE - free_space

matching_folders = fs.nodes_matching(
    is_directory_and_larger_than_builder(missing_space))

print(missing_space)
print(min(node.size for node in matching_folders))
