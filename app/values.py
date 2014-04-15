import subprocess
import psutil

def uptime():
    cmd = subprocess.check_output('uptime', stderr=subprocess.STDOUT).decode().strip().replace('\n', '')
    uptime = "".join("".join(cmd.split(',', maxsplit=3)[:2]).split("up")[1:]).replace(" days", "").split()
    uptim = uptime[1].split(":")
    return "%s days, %s hours, %s minutes" % (uptime[0], uptim[0], uptim[1])

def loadaverage():
    cmd = subprocess.check_output(['cat', '/proc/loadavg'], stderr=subprocess.STDOUT).decode().strip().replace('\n', '')
    #loadaverage = cmd.split(',', maxsplit=3)[3].strip().replace(",", "")
    return cmd

def memory():
    #svmem(total=620265472, available=190590976, percent=69.3, used=531537920, free=88727552, active=421326848, inactive=57815040, buffers=19206144, cached=82657280)
    mem = psutil.phymem_usage()
    return ["%s%s memory avaliable." % (mem[2], "%"), "Total: %s, Avaliable: %s, Used %s" % (mem[0], mem[1], mem[4])]

def users():
    cmd = subprocess.check_output(['who', '-q'], stderr=subprocess.STDOUT).decode().strip().split("\n")
    return cmd[0]

def hostname():
    return subprocess.check_output('hostname', stderr=subprocess.STDOUT).decode().strip().replace("\n", "")
