from utils.file_manager import output
from utils.file_manager import inputcontent
from os.path import splitext
from os.path import getsize

def make_list():
    listAsciiSize = 256
    listAscii = []
    for i in range(listAsciiSize):
        listAscii.insert(i, i.to_bytes(2, 'big'))
    return listAscii, listAsciiSize


def decompress(compressed):
    listAscii, listAsciiSize = make_list()
    uncompressed = []
    f = open('decode.txt', 'wb')
    w = compressed[0]
    compressed.remove(compressed[0])
    i = 0

    f.write(w)
    for byte in compressed:
        if int.from_bytes(byte, byteorder='big') < listAsciiSize:
            entry = listAscii[int.from_bytes(byte, byteorder='big')]
        elif (int.from_bytes(byte, byteorder='big')) == listAsciiSize:
            entry = w + w  # ERREUR
        else:
            raise ValueError('Bad uncompressed for: %s' % byte)

        print(entry)
        for b in entry:
            if i % 2 == 1:
                f.write(b.to_bytes(1, byteorder='big'))
            i += 1

        listAscii.insert(listAsciiSize, w + byte)
        listAsciiSize += 1
        w = entry
    f.close()


def file_decompressed(path):
    f = open(path, "rb")
    content = []
    for i in range(int(getsize(path)/2)):
        content.insert(i, f.read(2))
    decompress(content)
    f.close()

    # filename, file_extension = splitext(path)
    # original_file = output(uncompressed, filename + '.txt')
    # return original_file
