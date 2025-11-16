def require(mod):
    mod = mod.replace(".", "/")
    mod = "python/" + mod + ".py"
    config.source(mod)

config.load_autoconfig(False)
require("settings.options")
require("settings.keymaps")
