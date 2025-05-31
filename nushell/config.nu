# environment variables
$env.config.buffer_editor = '/usr/bin/helix'
$env.config.edit_mode = 'vi'
$env.PROMPT_COMMAND = ""
$env.config.show_banner = false
$env.PATH = ($env.PATH | split row (char esep) | append "/home/emma/.atuin/bin/")

# external configurations
source ~/.config/nushell/zoxide.nu
source ~/.config/nushell/starship.nu
source ~/.config/nushell/atuin.nu
source ~/.config/nushell/yazi.nu

# command aliases
alias cat = bat
alias hx = helix
alias la = ls -a
alias wiki = wiki-tui
alias cs = sudo-rs compsize -x
alias su = su-rs
alias sudo = sudo-rs
alias fetch = macchina
