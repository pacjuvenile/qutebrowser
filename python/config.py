def require(mod):
    mod = mod.replace(".", "/")
    mod = "python/" + mod + ".py"
    config.source(mod)

require("core.options")
require("core.keymaps")
