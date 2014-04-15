import app.utils as utils
import psutil

def uptime():
    cmd = utils.proc('uptime').replace('\n', '')
    uptime = "".join("".join(cmd.split(',', maxsplit=3)[:2]).split("up")[1:]).replace(" days", "").split()
    uptim = uptime[1].split(":")
    return "%s days, %s hours, %s minutes" % (uptime[0], uptim[0], uptim[1])

def loadaverage():
    cmd = utils.proc(['cat', '/proc/loadavg']).replace('\n', '')
    #loadaverage = cmd.split(',', maxsplit=3)[3].strip().replace(",", "")
    return cmd.split()

def memory():
    #svmem(total=620265472, available=190590976, percent=69.3, used=531537920, free=88727552, active=421326848, inactive=57815040, buffers=19206144, cached=82657280)
    cmd = psutil.phymem_usage()
    mem = [cmd[2], utils.size(cmd[0]), utils.size(cmd[1])]
    #return ["%s%s memory avaliable." % (mem[2], "%"), "Total: %s, Avaliable: %s, Used %s" % (mem[0], mem[1], mem[3])]
    return mem

def users():
    cmd = utils.proc(['who', '-q']).split("\n")
    return list(set(cmd[0].split()))

def hostname():
    return utils.proc('hostname').replace("\n", "")
