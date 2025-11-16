unbind = [
    "<Alt-1>",
    "<Alt-2>",
    "<Alt-3>",
    "<Alt-4>",
    "<Alt-5>",
    "<Alt-6>",
    "<Alt-7>",
    "<Alt-8>",
    "<Alt-9>",
    "J",
    "K",
    "H",
    "L",
]
for unbind_lhs in unbind:
    config.unbind(unbind_lhs) 

keymap = {
    "<Ctrl-1>": "tab-focus 1",
    "<Ctrl-2>": "tab-focus 2",
    "<Ctrl-3>": "tab-focus 3",
    "<Ctrl-4>": "tab-focus 4",
    "<Ctrl-5>": "tab-focus 5",
    "<Ctrl-6>": "tab-focus 6",
    "<Ctrl-7>": "tab-focus 7",
    "<Ctrl-8>": "tab-focus 8",
    "<Ctrl-9>": "tab-focus 9",
    "H": "tab-prev",
    "L": "tab-next",
    "<Ctrl-d>": "cmd-run-with-count 15 scroll down",
    "<Ctrl-u>": "cmd-run-with-count 15 scroll up",
}
for lhs, rhs in keymap.items():
    config.bind(lhs, rhs)
