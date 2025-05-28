# environment variables
$env.config.buffer_editor = '/usr/bin/helix'
$env.config.edit_mode = 'vi'
$env.PROMPT_COMMAND = ""
$env.config.show_banner = false
$env.PATH = ($env.PATH | split row (char esep) | append "/home/emma/.atuin/bin/")

# external configurations
source ~/.config/nushell/zoxide.nu
source ~/.config/nushell/starship.nu
source ~/.local/share/atuin/init.nu

# command aliases
alias cat = bat
alias hx = helix
alias ls = ls -a
alias cd = z

# commands to run on start
atuin sync | ignore
