import typing
from dataclasses import dataclass

from day7.filesystem import FileSystem


@dataclass
class Command(object):
    command: str
    output: typing.Optional[typing.List[str]]


def parse_output_filesystem(lines: typing.List[str]) -> FileSystem:
    fs = FileSystem()

    i = 0
    cwd = ''
    while i < len(lines):
        command = lines[i]

        output = []
        j = i + 1

        while j < len(lines) and (not lines[j].startswith('$')):
            output.append(lines[j])
            j = j + 1

        command = Command(command.replace('$ ', ''), output)

        if command.command.startswith('cd'):
            path = command.command.split(' ')[1]
            if path.startswith('/'):
                cwd = command.command.split(' ')[1]
            elif path == '..':
                cwd = f'/{"/".join(cwd[1:].split("/")[:-2])}'

                if cwd[-1] != '/':
                    cwd += '/'
            else:
                cwd += f'{path}/'

        elif command.command.startswith('ls'):
            for output in command.output:
                if not output.startswith('dir'):
                    size, name = output.split(' ')
                    fs.touch(f'{cwd}{name}', int(size))
        i = j

    return fs
