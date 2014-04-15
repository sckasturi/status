import subprocess


def size(num):
    for x in ['bytes','KB','MB','GB','TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def proc(cmd):
    return subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode().strip()
