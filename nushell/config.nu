$env.config.buffer_editor = '/usr/bin/helix'
$env.config.show_banner = false
$env.PROMPT_COMMAND_RIGHT = ""
$env.PROMPT_COMMAND = ""
$env.PROMPT_INDICATOR = ":"
$env.TRANSIENT_PROMPT_COMMAND = ""

source ~/.config/nushell/zoxide.nu
source ~/.config/nushell/starship.nu

alias cat = bat
alias hx = helix
alias ls = ls -a
alias cd = z
