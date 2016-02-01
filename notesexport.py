#!/usr/bin/env python
"""Creates useful files from a Lotus Notes structured text export.

Export your mailbox and choose the form-feed character as the message
separator, ASCII 12.
"""
import sys
import re


FORMFEED = chr(12)


def readlines(filename, endings, chunksize=4096):
    """Returns a generator that splits on lines in a file with the given
    line-ending.
    """
    line = ''
    while True:
        buf = filename.read(chunksize)
        if not buf:
            yield line
            break

        line = line + buf

        while endings in line:
            idx = line.index(endings) + len(endings)
            yield line[:idx]
            line = line[idx:]


def notes_headers(msg):
    """Returns a dictionary of some interesting notes headers."""
    d = {
        'Subject': None,
        'PostedDate': None,
        'From': None,
        'SentTo': None,
    }
    for line in msg.splitlines():
        if None not in d.values():
            return d
        for k in d:
            if d[k] is None:
                if line.startswith(k + ':  '):
                    d[k] = line[len(k + ':  '):]
    else:
        return d


def normalize(s):
    """Cleans up a string for use on the file system."""
    return re.sub(r'[- :!,\./\\]+', '-', s.strip())


def main(argv):
    for count, message in enumerate(readlines(open(argv[1]), endings=FORMFEED)):
        headers = notes_headers(message)
        print count
        d, m, y = headers['PostedDate'][:10].split('/')
        s = normalize(headers['Subject'])
        filename = '%s-%s-%s %s %s.txt' % (y, m, d, count, s)
        f = open(filename, 'wb')
        f.write(message)
        f.close()


def usage(argv):
    sys.stdout.write("""Usage: %(prog)s <archive>

Write files for individual messages in a Notes structured text archive.
The files will be created in the current directory.
""" % {'prog': argv[0]})


if __name__ == "__main__":
    main(sys.argv)
