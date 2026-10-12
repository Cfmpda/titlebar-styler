#!/usr/bin/env bash
set -e

echo "==> A instalar o Titlebar Styler..."

TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT

git clone --depth 1 https://github.com/Cfmpda/titlebar-styler.git "$TMP_DIR/titlebar-styler"
cd "$TMP_DIR/titlebar-styler"

if [ -w "/usr/local" ]; then
    make install PREFIX=/usr/local
    echo "==> Instalado com sucesso em /usr/local/bin/titlebar-styler"
elif command -v sudo >/dev/null 2>&1 && sudo -v 2>/dev/null; then
    sudo make install PREFIX=/usr/local
    echo "==> Instalado com sucesso em /usr/local/bin/titlebar-styler"
else
    make install PREFIX="$HOME/.local"
    echo "==> Instalado com sucesso em $HOME/.local/bin/titlebar-styler"
fi

update-desktop-database "$HOME/.local/share/applications" 2>/dev/null || :
update-desktop-database /usr/local/share/applications 2>/dev/null || :
gtk-update-icon-cache -f -t "$HOME/.local/share/icons/hicolor" 2>/dev/null || :
gtk-update-icon-cache -f -t /usr/local/share/icons/hicolor 2>/dev/null || :

echo "==> Pronto! Podes abrir o 'Titlebar Styler' no menu de aplicações ou pelo terminal com 'titlebar-styler'."
