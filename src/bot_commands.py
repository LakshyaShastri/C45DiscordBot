
import subprocess
import requests
import plugins

from __init__ import cfg


def exec_command(command):
    # Find the associated plugin
    plugin = plugins.find_plugin(command)
    if plugin is not None:
        message = plugin.exec(command)
        return message

    if command.startswith("exec"):
        cmd = command[4:]
        print("Exec: " + str(cmd))
        # return subprocess.getoutput(cmd)
        return "Exec is down, changes being made."
    elif command.startswith("python3"):
        cmad = command[7:]
        if (cmad.find("os") == -1 and
                cmad.find("subprocess") == -1 and
                cmad.find("open(") == -1):
            try:
                return eval(cmad)
            except:
                return "error in eval"
        else:
            return "For safety, this command cannot be run"
    elif command.lower() == "ip:route":
        return subprocess.getoutput("route")
    elif command.lower() == "wall":
        msg = command[4:]
        subprocess.getoutput("wall " + msg)
        return "Done tty (titty)"
    elif command.lower() == "ip:route6":
        return subprocess.getoutput("route -6")
    elif command.lower() == "ip:if":
        return subprocess.getoutput("ifconfig")
    elif command.lower() == "ip:arp":
        return subprocess.getoutput("arp")
    elif command.lower() == "ip:neigh":
        return subprocess.getoutput("ip neigh")
    elif command.startswith("ls"):
        dirLS = command[2:]
        return subprocess.getoutput("ls " + dirLS)
    elif command.lower().startswith("ip:ping"):
        ip = command[7:]
        return subprocess.getoutput("ping " + ip + " -c 3")
    elif command.lower().startswith("ip:arping"):
        ip = command[9:]
        return subprocess.getoutput("arping -c 3 " + ip)
    elif command.lower().startswith("ip:trace"):
        ip = command[8:]
        return subprocess.getoutput("traceroute " + ip)
    elif command.lower().startswith("fetch"):
        url = command[5:]
        body = requests.get(url).text
        return body
    elif command == "brink":
        return "EXACTLY - Old Khaki.com"
    elif command == "help":
        f = open("./resources/help.menu")
        strings = f.readlines()
        msg = ""
        for s in strings:
            msg += s
        return msg
    elif command.startswith("add_feature"):
        line = command[12:]
        print("adding feature: " + line)
        f = open("./resources/features.txt", "a")
        f.write(str(line + "\n"))
        f.close()
        return "feature request recorded"
    else:
        print("\"" + str(command) + "\"" + " released, not a valid command")
        return "Not a command you chop"
