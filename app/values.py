import subprocess
cmd = subprocess.check_output('uptime', stderr=subprocess.STDOUT).decode().strip().replace('\n', '')

def uptime():
    uptime = "".join("".join(cmd.split(',', maxsplit=3)[:2]).split("up")[1:]).replace(" days", "").split()
    uptim = uptime[1].split(":")
    return "%s days, %s hours, %s minutes" % (uptime[0], uptim[0], uptim[1])
