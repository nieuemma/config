#!/usr/bin/env sh
# Run as user with sudo privileges, not as root.

pkg=(
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
        nushell
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
)

main() {
        setup_rust
        get_paru
        install_pkg
        configure
}

setup_rust() {
        sudo pacman -S rustup
        rustup default stable
}

get_paru() {
        sudo pacman -S --needed base-devel
        git clone https://aur.archlinux.org/paru.git
        cd paru
        makepkg -si
}

install_pkg() {
        paru -S ${pkg[@]}
}

configure() {
        rm -rf ~/.config
        git clone https://github.com/nieuemma/config ~/.config
        chsh -s /usr/bin/nu
        
}

main
