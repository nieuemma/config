$env.config.show_banner = false
$env.PROMPT_COMMAND = ""
$env.config.edit_mode = 'vi'
$env.config.buffer_editor = '/usr/bin/helix'

source ~/.config/nushell/atuin.nu
source ~/.config/nushell/starship.nu
source ~/.config/nushell/yazi.nu
source ~/.config/nushell/zoxide.nu

alias cat = bat
alias calc = kalker
alias bm = hyperfine -Ni 
alias hx = helix
alias fetch = macchina
alias parallel = par-each
alias la = ls -a
alias si = silicon --to-clipboard -f "Messlo Term" -b "#39C5CF"
alias cs = sudo-rs compsize -x
alias su = su-rs
alias sudo = sudo-rs
alias archwiki = wiki-search
alias wiki = wiki-tui
