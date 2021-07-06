import os
import hashlib
import time

# compute sha256 hash of the content
def sha256HashFunc(content):
    return hashlib.sha256(content).hexdigest()

if __name__ == '__main__':
    # ask the user for directory to be traversed
    print('Please define the directory to be traversed:')
    directory = input()

    # status message
    print('I will traverse: ' + directory + ' and its subdirectories')

    # all jpeg files will be stored here
    jpeg_files = dict()

    # traverse the sub
    for (dirpath, dirnames, filenames) in os.walk(directory):
        for file in filenames:
            fullFilePath = os.path.join(dirpath, file)
            try:
                with open(fullFilePath, 'rb') as f:
                    # read all the content of the file
                    content = f.read()
                    # compare the first four bytes with ffd8ffe0
                    if(content[:4] == b'\xff\xd8\xff\xe0'):
                        # append to the dictionary, name of file, sha256 hash, last modified time
                        # last access time and creation time, use full file path as key
                        jpeg_files[fullFilePath] = [file, sha256HashFunc(content),
                                           time.ctime(os.path.getmtime(fullFilePath)),
                                           time.ctime(os.path.getatime(fullFilePath)),
                                           time.ctime(os.path.getctime(fullFilePath))]
            except:
                print ("File", fullFilePath, "can not be read, ignoring it")

if len(jpeg_files) == 0:
    print ("No JPEG files found")
else:
    try:
        # dump all the information in comma separated format
        # with each line representing one jpeg file
        with open("AliOutput.txt", 'w') as f:
            # traverse each element of list
            for jpeg_file in jpeg_files:
                fileData = jpeg_files[jpeg_file]
                # traverse all but last data of jpeg_file
                for i in range(len(fileData) - 1):
                    f.write('%s,' % fileData[i])
                # print the last data point in jpeg_file
                f.write(fileData[-1])
                f.write('\n')
    except:
        print ("File writing failed")

print ("The script was completed at", time.ctime())
