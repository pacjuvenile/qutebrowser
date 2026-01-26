def require(mod):
    mod = mod.replace(".", "/")
    mod = "python/" + mod + ".py"
    config.source(mod)

config.load_autoconfig(False)
require("core.options")
require("core.keymaps")
