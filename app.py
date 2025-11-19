from src.procesador import Analizador

def main():
    archivo = "datos/sri_ventas_2024.csv"
    analizador = Analizador(archivo)

    print("=== ANÁLISIS SRI VENTAS 2024 ===\n")
    
    print("1. Ventas totales por provincia:")
    resumen = analizador.ventas_totales_por_provincia()
    for prov, total in resumen.items():
        print(f"   {prov}: ${total:.2f}")

    print("\n2. Exportaciones por mes:")
    exportaciones = analizador.exportaciones_totales_por_mes()
    for mes, total in sorted(exportaciones.items()):
        print(f"   Mes {mes}: ${total:,.2f}")

    print("\n3. Provincia con mayor importaciones:")
    provincia_import = analizador.provincia_mayor_importaciones()
    if provincia_import:
        provincia, valor = provincia_import
        print(f"   {provincia}: ${valor:,.2f}")

    print("\n4. Consulta individual por provincia:")
    provincia = input("   Ingrese el nombre de una provincia: ")
    
    try:
        ventas = analizador.ventas_por_provincia(provincia)
        print(f"   Ventas de {provincia}: ${ventas:,.2f}")
    except KeyError:
        print(f"   Error: La provincia '{provincia}' no existe en los datos")
    
if __name__ == "__main__":
    main()