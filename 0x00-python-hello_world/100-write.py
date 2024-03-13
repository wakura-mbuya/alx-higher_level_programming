#!/usr/bin/python3
import sys

def write_to_stderr(error_msg):
    """
    Writes to stderr and exits with status value 1
    """

    sys.stderr.write(error_msg)
    sys.stderr.write("\n")
    sys.exit(1)

error_msg = "and that piece of art is useful - Dora Korpar, 2015-10-19"
write_to_stderr(error_msg)
