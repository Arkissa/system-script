#!/bin/python3

import subprocess
import sys


arg = "".join(sys.argv[1:])
coproc = "coproc (~/scripts/bin/{})"
tool = {
    "  Open Music": coproc.format("music.sh"),
    "  Open Translate": coproc.format("translate/run.sh"),
    "  Open Picom": coproc.format("picom.sh"),
    "  Open Notify": coproc.format("notify.sh"),
    "  Set Backgrounds": "feh --randomize --bg-fill ~/Pictures/background/*",
    "  Update statusbar": "$DWM/statusbar/statusbar.py updateall",
}

check_command = {
    "  Open Music": "ps -u $USER -o pid,comm | grep 'mpd' | awk '{print $1}'",
    "  Open Translate": r"ps aux | grep 'translate.py' | grep -v 'grep\|rofi\|nvim'",
    "  Open Notify": r"ps aux | grep dunst | grep -v 'grep\|rofi\|nvim'",
    "  Open Picom": r"ps aux | grep picom | grep -v 'grep\|rofi\|nvim'",
}


def run(command) -> str:
    byte, _ = subprocess.Popen(
        ["/bin/bash", "-c", command], stdout=subprocess.PIPE
    ).communicate()
    return byte != b"" and byte.decode() or ""


def check(ps: str, pop: str, command: str):
    key, value = (
        run(ps) and tool.pop(pop) and pop.replace("Open", "Close"),
        command,
    )

    return key != "" and (True, key, value) or (False, "", "")


for key, value in check_command.items():
    ok, menu, command = check(value, key, tool[key])
    if ok:
        tool[menu] = command


if arg:
    run(tool[arg])
else:
    for name, _ in tool.items():
        print(name)
