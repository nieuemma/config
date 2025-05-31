# Run as user with sudo privileges, not as root.

def main [] {
    setup_rust
    get_paru
    install_pkg
    configure
}

def setup_rust [] {
    sudo pacman -S rustup
    rustup default stable
}

def get_paru [] {
    sudo pacman -S --needed base-devel
    git clone https://aur.archlinux.org/paru.git
    cd paru
    makepkg -si
    cd ..
    rm -rf paru
}

def install_pkg [] {
    paru -S --needed $pkg
}

def configure [] {
    rm -rf ~/.config
    git clone https://github.com/nieuemma/config ~/.config
}

let pkg = [
    7zip
    atuin
    bottom
    bp-bin
    choose
    clipse-bin
    compsize
    cmus
    fend-bin
    ffmpeg
    fzf
    git
    github-cli
    helix
    hypridle
    hyprland
    hyprlock
    hyprnome
    hyprnotify
    hyproled-git
    hyprpaper
    hyprpicker
    hyprshot
    hyprsunset
    iamb-bin
    just
    jq
    kitty
    mpv
    ouch
    paruz
    poppler
    qutebrowser
    resvg
    skim
    starship
    sudo-rs
    vesktop
    wl-clipboard
    yazi
    zoxide
]

main
