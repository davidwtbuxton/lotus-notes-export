Lotus Notes export
==================

This is a [Python][python] script to export messages from a [Lotus Notes][notes] structured text archive to plain text files, one for each message in the archive. The files are created in the current directory.

Usage
-----

Export messages from Notes in structured text format, and choose the form-feed character as the message
separator, ASCII 12. Then run the script with the archive filename.

    python notesexport.py my-notes-export.txt

A file will be created for each message.

This script has been tested with Python 2.7.


[python]: https://www.python.org/
[notes]: http://www-01.ibm.com/software/lotus/
[export]: http://www-01.ibm.com/support/knowledgecenter/SSKTWP_8.0.1/com.ibm.notes.help.doc/DOC/H_EXPORTING_INTO_STRUCTURED_TEXT_FILES_OVER.html?lang=en
