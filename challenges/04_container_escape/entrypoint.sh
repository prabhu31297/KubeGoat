#!/bin/sh

echo "[+] Welcome to Container Escape Challenge!"
echo "[+] This container might have access to the host filesystem..."

echo "[+] Try exploring /mnt/root or /mnt/etc to find secrets."


echo "[*] Starting vulnerable container in privileged mode..."
exec python app.py
