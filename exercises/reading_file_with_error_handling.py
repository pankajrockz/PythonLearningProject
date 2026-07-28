filePath = "../test_files/sample.txt"
try:
    with open(filePath, 'rt') as fh:
        data = fh.readlines()
except FileNotFoundError:
    print(f'Error: The file {filePath} was not found.')
except Exception as exception:
    print(f'Error reading the file: {exception}')
else:
    for line in range(len(data)):
        print(f'Line {line}: {data[line].rstrip('\n')}')
