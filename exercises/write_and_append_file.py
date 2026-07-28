import io

filePath = "../test_files/output.txt"
first_line = input("Enter text to write to the file: ")
try:
    with open(filePath, 'wt') as fh:
        fh.write(first_line + '\n')
    print(f'Data successfully written to {filePath}.\n')

    second_line = input("Enter additional text to append: ")
    with open(filePath,'at') as fh:
        fh.write(second_line)
    print(f'Data successfully appended.\n')

    with open(filePath, 'rt') as fh:
        final_content = fh.read()
    print(f'Final content of {filePath}: \n{final_content}')
except FileNotFoundError as fileError:
    print(f'File not found: {fileError}')
except io.UnsupportedOperation as unsupportedError:
    print(f'Operation not supported: {unsupportedError}')
except Exception as exception:
    print(f'Failed while performing operation: {exception}')