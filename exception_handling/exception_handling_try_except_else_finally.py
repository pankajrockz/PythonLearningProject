'''
Now as we are handling the Exception, it's also important to show/log the error message thrown with the exception.
We can handle either the specific exception like FileNotFoundError, ValueError, etc or the generic exception called
'Exception' basically which will handle all types of exception.
'''
import io

try:
    with open("my_file.txt", "rt") as fh:
        data = fh.read()
    print(data)
except FileNotFoundError as file_err:
    print("File that you are trying to open does not exists!!!!")
    print(file_err)

'''
Output:
File that you are trying to open does not exists!!!!
[Errno 2] No such file or directory: 'my_file.txt'
'''

'''
Else & Finally block with try except
Else: Else block after except is executed only after there is not exception occurred in try block. It generally required
when we only want to perform certain operation after the try block run without any exception.

Finally: Finally block after except is always executed after try and catch blocks. This block runs even when there is
exception or run without any exception in try. 

Else and Finally both can be used individually with try-except and also can be used togather after try-except.
'''

try:
    fh = open("../test_files/practice1.txt", "wt")
    # data = fh.read() # This will throw the io.UnsupportedOperation as we used w mode to open the file
    fh.write("Hello, we are working on try-except-else-finally")
except FileNotFoundError as file_err:
    print(f"File that you are trying to open doesn't exists: {file_err}")
except io.UnsupportedOperation as io_error:
    print(f"Operation that you are trying to perform is not supported: {io_error}")
except Exception as ex:
    print(f"Operation that you are trying to perform is failed because of: {ex}")
else: # In case of try runs successful, it calls else where we can perform some operations like logging.
    print("Else Block: File writing is successful!!!")
finally: # In any case of try-except we need to close the file object(fh) hence that can be called under finally
    print("Finally Block: Closing the file after use!!!")
    fh.close()

'''
Output: When try works fine
Else Block: File writing is successful!!!
Finally Block: Closing the file after use!!!

Output: When try has got exception
Operation that you are trying to perform is not supported: not readable
Finally Block: Closing the file after use!!!
'''