from datetime import datetime

def fecha_a_mes_espanol(fecha_str):
    """
    Toma una fecha en formato DD-MM-YYYY (ej. 15-01-2025)
    y devuelve el nombre del mes en español.
    Útil para la gestión de reportes REM y estadísticas mensuales.
    """
    meses = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    
    try:
        # Intentamos convertir el texto a un objeto fecha
        fecha_obj = datetime.strptime(fecha_str, "%d-%m-%Y")
        return meses[fecha_obj.month]
    except ValueError:
        return "Error: Formato de fecha incorrecto"

# --- Bloque de prueba (Ejecución local) ---
if __name__ == "__main__":
    # Simulación de fechas extraídas de una base de datos o Excel
    fechas_prueba = ["15-01-2025", "28-02-2025", "10-11-2025"]
    
    print("--- Procesando Fechas ---")
    for f in fechas_prueba:
        resultado = fecha_a_mes_espanol(f)
        print(f"Fecha: {f} -> Mes: {resultado}")
