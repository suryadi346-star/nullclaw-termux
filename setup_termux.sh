#!/bin/bash
set -e
echo "📦 Updating Termux..."
pkg update -y && pkg upgrade -y
pkg install python git ca-certificates -y

echo "🔧 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Setup selesai. Edit config.json lalu jalankan: python main.py"
