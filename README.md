# Práctica 03 - Análisis de Datos Tributarios SRI

## 📋 Descripción
Proyecto del análisis de datos del formulario 104 del SRI para el año 2024, implementando procesamiento de datos y pruebas unitarias.

## 🏗️ Estructura del Proyecto
practica-03/
├── datos/
│ └── sri_ventas_2024.csv
├── src/
│ └── procesador.py
├── test/
│ └── test_procesador.py
├── app.py
└── README.md


## 🚀 Funcionalidades Implementadas

### Funcionalidades Principales
1. **Ventas totales por provincia** - Agrupa y suma TOTAL_VENTAS por PROVINCIA
2. **Ventas por provincia específica** - Consulta individual por provincia

### Extensiones Adicionales
1. **Exportaciones totales por mes** - Suma de EXPORTACIONES agrupadas por MES
2. **Provincia con mayor importaciones** - Identifica la provincia con mayor volumen de IMPORTACIONES

## 🧪 Pruebas Unitarias

Se implementaron 14 pruebas unitarias que validan:
- Coherencia en el número de provincias (25 incluyendo 'ND')
- Valores numéricos y no negativos
- Estructura correcta de diccionarios
- Existencia de provincias consultadas
- Manejo de errores para provincias inexistentes
- Correcto funcionamiento de las extensiones

## 📊 Cobertura de Código

Se utilizó la librería `coverage` para medir la cobertura de código:

```bash
# 1 Instalación
pip install coverage
# 2 Ejecución
coverage run -m unittest discover -s test -v
# 3 Reporte
coverage report