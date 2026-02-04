c.fonts.default_size = "10pt"
# c.colors.webpage.preferred_color_scheme = "dark"
# c.colors.webpage.darkmode.enabled = True

c.content.headers.accept_language = "zh-CN,en-US"
c.content.headers.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
# c.content.headers.user_agent = "Mozilla/5.0 (windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0
# c.content.headers.user_agent = "Mozilla/5.0 (Android 13; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"

c.url.default_page = "https://bing.com/"
c.url.start_pages = "https://bing.com"
c.url.searchengines = {"DEFAULT": "https://google.com/search?q={}"}

c.scrolling.bar = "overlay"
c.scrolling.smooth = True

c.statusbar.padding = {"bottom": 1, "left": 3, "right": 3, "top": 1}
c.statusbar.widgets = ["search_match", "text:|", "url", "text:|", "scroll", "text:|", "tabs"]

c.tabs.padding = {"top": 5, "bottom": 5, "left": 1, "right": 0}
c.tabs.position = "left"
c.tabs.width = "5%"

c.window.hide_decoration = True

c.zoom.default = "75%"
c.zoom.levels = ["20%", "30%", "40%", "50%", "60%","70%","75%", "80%","85%", "90%", "100%", "110", "120", "130", "140%", "150%", "160%", "170%", "180%", "190%", "200%"]

c.hints.padding = {"bottom": 1, "left": 1, "right": 1, "top": 1}
c.hints.border = "none"
c.hints.chars = "asdfghjklqwertyuiopzxcvbnm"
c.hints.selectors["videos"] = ["video"]
