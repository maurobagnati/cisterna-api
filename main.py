from fastapi import FastAPI
from playwright.sync_api import sync_playwright

app = FastAPI()

def obtener_nivel_tanque():
    with sync_playwright() as p:
        # Aquí usamos headless=True porque el servidor no necesita mostrar la ventana
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox"])
        page = browser.new_page()
        
        # --- TU LÓGICA DE LOGIN ---
        page.goto("http://181.114.212.66:8088/data/perspective/client/CG")
        page.fill("input", "scadaguatrache")
        page.keyboard.press("Enter")
        page.wait_for_selector("input[type='password']")
        page.fill("input[type='password']", "scadaguatrache")
        page.keyboard.press("Enter")
        
        # --- EXTRACCIÓN DEL DATO ---
        page.wait_for_selector("text=m", timeout=20000)
        valor = page.inner_text("text=/\\d+\\.\\d+\\s*m/")
        
        browser.close()
        return valor

@app.get("/nivel")
def get_nivel():
    # Esta es la ruta que llamará tu celular
    dato = obtener_nivel_tanque()
    return {"nivel": dato, "unidad": "metros", "estado": "ok"}