# Computing-Image-Hashes-

1. Summary:
This script will traverse a directory and its subdirectories and examine the
files within them looking for .JPG files. This will be done by examining each file's
header and not by scanning the extensions. Once .JPG files are found, the script will
will compute the SHA256 hash of the file, get the files' MAC times, and store them to
Alioutput.txt.

2. How to use it:
Open the script using Python in either terminal (on MAC), CMD (on Windows),
or an IDE. Make sure your Python library has the following modules installed
before running the script: Hashlib.

The OS and Time modules are standard modules and should already exist within your
Python program.

Run the script and then find the output in hw3Ali.py

3. Usage:
This script is great to find .jpg's based on their file headers, in case
original files extensions have been tampered. It is also great to use to compute
the SHA256 hashes of files.

4. Changes:
You can use this script in the future to find different file formats based on their magic
numbers instead of just .JPG. All you would have to do would be to change
b'\xff\xd8\xff\xe0' in line 29 to whatever magic number you want, depending on the files
you are scanning for.

You can also change the hash function in line 7 from SHA256 to another
hash function that exists in the Hashlib module.
