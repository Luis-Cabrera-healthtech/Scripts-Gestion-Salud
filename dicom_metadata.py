import pydicom
from pydicom.data import get_testdata_file

def leer_cabecera_dicom(ruta_archivo):
    """
    Lee un archivo .dcm y muestra los metadatos esenciales.
    Requiere la librería: pip install pydicom
    """
    try:
        # Cargamos el archivo DICOM (dataset)
        ds = pydicom.dcmread(ruta_archivo)
        
        print(f"--- INFO DEL ARCHIVO: {ruta_archivo} ---")
        print(f"Paciente: {ds.PatientName}")
        print(f"ID: {ds.PatientID}")
        print(f"Modalidad: {ds.Modality}") # Ej: MG (Mamografía), DX, CT
        print(f"Fecha Estudio: {ds.StudyDate}")
        print(f"Fabricante: {ds.Manufacturer}")
        
        # Ejemplo de acceso a tags privados o específicos
        if 'InstitutionName' in ds:
            print(f"Institución: {ds.InstitutionName}")
            
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado. Verifique la ruta.")
    except Exception as e:
        print(f"Ocurrió un error al leer el DICOM: {e}")

# --- Bloque de Prueba ---
if __name__ == "__main__":
    # Usamos un archivo de prueba incluido en la librería pydicom para demostrar funcionalidad
    print("Iniciando lectura de prueba...")
    
    # pydicom trae archivos de ejemplo, usamos uno de resonancia (MR)
    archivo_demo = get_testdata_file("MR_small.dcm")
    
    leer_cabecera_dicom(archivo_demo)
