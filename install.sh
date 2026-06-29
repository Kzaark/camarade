#!/bin/bash

set -e

REPO="https://github.com/Kzaark/camarade.git"
INSTALL_DIR="/usr/local/share/camarade"
BIN_DIR="/usr/local/bin"

echo "Installation de camarade..."

if [ -d "$INSTALL_DIR/.git" ]; then
    echo "Dépôt existant détecté, mise à jour..."
    git -C "$INSTALL_DIR" pull
else
    echo "Clonage du dépôt..."
    git clone "$REPO" "$INSTALL_DIR"
fi

cat > "$BIN_DIR/camarade" << 'SCRIPT'
#!/bin/bash
python3 /usr/local/share/camarade/camarade.py "$@"
SCRIPT

chmod +x "$BIN_DIR/camarade"
echo "✓ camarade installé avec succès !"
echo "  Lance : camarade"
