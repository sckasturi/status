import app.utils as utils
import psutil

def uptime():
    cmd = utils.proc('uptime').replace('\n', '')
    uptime = "".join("".join(cmd.split(',', maxsplit=3)[:2]).split("up")[1:]).replace(" days", "").split()
    uptim = uptime[1].split(":")
    output = {
        'day': uptime[0],
        'hour':  uptim[0],
        'min':  uptim[1]
    }
    return output

def loadaverage():
    cmd = utils.proc(['cat', '/proc/loadavg']).replace('\n', '').split()[:3]
    output = {
        '1m': cmd[0],
        '5m': cmd[1],
	'15m': cmd[2]
    }
    return output

def memory():
    cmd = psutil.phymem_usage()
    output = {
        'percent': str(cmd[2]),
	'total': utils.size(cmd[0]),
	'available': utils.size(cmd[1])
    }
    return output

def users():
    cmd = utils.proc(['who', '-q']).split("\n")
    return list(set(cmd[0].split()))

def hostname():
    return utils.proc('hostname').replace("\n", "")
