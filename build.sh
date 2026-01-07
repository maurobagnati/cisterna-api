#!/usr/bin/env bash
# Salir si hay un error
set -o errexit

# Instalar las librerías de Python
pip install -r requirements.txt

# Instalar solo el navegador Chromium (sin intentar instalar dependencias de sistema)
playwright install chromium
