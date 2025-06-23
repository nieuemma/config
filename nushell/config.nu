$env.config.show_banner = false
$env.PROMPT_COMMAND = ""
$env.config.edit_mode = 'vi'
$env.config.buffer_editor = 'hx'

source ~/.config/nushell/atuin.nu
source ~/.config/nushell/yazi.nu
source ~/.config/nushell/zoxide.nu

alias fetch = macchina
alias parallel = par-each
alias la = ls -a
alias si = silicon --to-clipboard -f "Messlo Term" --no-line-number --no-window-controls --pad-horiz 0 --pad-vert 0

uwsm check may-start; exec uwsm start default
