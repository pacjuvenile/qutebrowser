unbind = [
    # 默认标签页切换
    "<Alt-1>",
    "<Alt-2>",
    "<Alt-3>",
    "<Alt-4>",
    "<Alt-5>",
    "<Alt-6>",
    "<Alt-7>",
    "<Alt-8>",
    "<Alt-9>",
    "H",
    "J",
    "K",
    "L"
]
for unbind_lhs in unbind:
    config.unbind(unbind_lhs)

keymap = {
    # 标签页切换
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
    # 历史记录
    "J": "forward",
    "K": "back",
    # 平滑滚动版翻半页
    "<Ctrl-d>": "cmd-run-with-count 15 scroll down",
    "<Ctrl-u>": "cmd-run-with-count 15 scroll up",
    # 清除消息通知
    "<Ctrl-l>": "clear-messages",
    # 模拟鼠标悬停
    "<Ctrl-h>": "hint all hover",
    # 复制链接url
    "<Ctrl-y>": "hint links yank",
    # 用mpv播放视频
    "<Ctrl-m>": "hint videos spawn mpv chint-url} --keep-open=yes --geometry=80%+200+200",
}
for lhs, rhs in keymap.items():
    config.bind(lhs, rhs)
