# 🏥 Scripts de Gestión para Salud Digital

Repositorio de utilidades y scripts en Python diseñados para automatizar tareas operativas en entornos de Salud (RIS/PACS, Listas de trabajo, Reportes).

## 📂 Contenido del Repositorio

### 1. `date_converter.py` (Conversor de Fechas)
* **Problema:** Los reportes exportados de sistemas HIS/RIS suelen traer fechas en formatos numéricos (ej. `15-01-2025`) que no son amigables para gráficos o resúmenes ejecutivos.
* **Solución:** Script que transforma cadenas de fecha al nombre del mes en español.
* **Aplicación:** Útil para la generación automatizada de **Reportes Estadísticos Mensuales (REM)** o agrupación de estudios imagenológicos por periodo.
  
### 2. `dicom_metadata.py` (Lector de Cabeceras DICOM)
* **Problema:** Verificar rápidamente si un archivo `.dcm` contiene los tags correctos antes de subirlo al PACS o para auditoría de calidad (QA).
* **Solución:** Script que utiliza la librería `pydicom` para extraer y mostrar en consola los metadatos críticos (Nombre, ID, Modalidad, Fabricante).
* **Requisito:** `pip install pydicom`
  
## 🛠️ Tecnologías
* **Python 3.x**
* Librerías estándar (`datetime`)

---
Desarrollado por **Luis Cabrera** | *Tecnólogo Médico & Health IT Specialist*
