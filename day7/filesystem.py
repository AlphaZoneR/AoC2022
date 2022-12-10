import typing

from day7.node import DirectoryNode, FileNode, Node

TAB = '  '


class FileSystem:
    root: DirectoryNode

    def __init__(self) -> None:
        self.root = DirectoryNode('/')

    def mkdir(self, absolute_path: str) -> DirectoryNode:
        components = [
            component for component in absolute_path.split('/') if component]
        iterator = self.root

        for component in components:
            if iterator.get_named_child(component):
                iterator = iterator.get_named_child(component)
            else:
                new_directory = DirectoryNode(component)
                iterator.add_child(new_directory)
                iterator = new_directory

        return iterator

    def touch(self, absolute_path: str, size: int):
        components = [
            component for component in absolute_path.split('/') if component]
        parent_dir_components = components[:-1]
        folder_node = self.mkdir(f'/{"/".join(parent_dir_components)}')
        new_file_child = FileNode(components[-1], size)
        folder_node.add_child(new_file_child)

        return new_file_child

    def nodes_matching(self, filter_func: typing.Callable[['Node'], bool]) -> typing.List[Node]:
        result: typing.List[Node] = []

        def recursive_function(root: Node, result: typing.List[Node]):
            if filter_func(root):
                result.append(root)

            for child in root.children:
                recursive_function(child, result)

        recursive_function(self.root, result)

        return result

    def __repr__(self) -> str:
        result: typing.List[str] = []

        def recursive_printer(root: 'Node', result: typing.List[str], depth=0):
            tabs = ''
            for _ in range(depth):
                tabs += '|' + TAB
            result.append(f'{tabs}{root.__repr__()}')
            for child in root.children:
                recursive_printer(child, result, depth=depth+1)

        recursive_printer(self.root, result)

        return '\n'.join(result)

    def __str__(self) -> str:
        return self.__repr__()
