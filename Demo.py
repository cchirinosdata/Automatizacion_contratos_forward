import pandas as pd
from datetime import datetime


# Simulamos los datos que la IA extrajo del PDF "Contrato de Derivado Mayo 2026.pdf"
datos_extraidos_pdf = {
    "Razon_Social": "Banco ABC",
    "Tipo_Operacion": "VENTA",
    "Moneda_Principal": "USD",
    "Monto_Principal": 3000000.00,
    "TC_Contratado": 910.00,
    "Precio_Pactado": 2730000000.00,
    "Fecha_Inicio": "2026-05-20",
    "Fecha_Vencimiento": "2027-12-12"
}

print("✅ [Paso 1] Datos extraídos del PDF mediante IA de forma estructurada.")
print("⏳ [Paso 2] Ejecutando validación de riesgo financiero...")

calculo_interno = datos_extraidos_pdf["Monto_Principal"] * datos_extraidos_pdf["TC_Contratado"]

if calculo_interno != datos_extraidos_pdf["Precio_Pactado"]:
    print("❌ ERROR CRÍTICO: Discrepancia matemática en el contrato.")
    print(f"   Calculado: {calculo_interno} | Extraído: {datos_extraidos_pdf['Precio_Pactado']}")
    print("🚨 ACCIÓN: Flujo detenido. Enviando Adaptive Card a MS Teams para revisión manual.")
    exit() # Detiene el proceso
else:
    print("✅ [Paso 2] Validación matemática superada (Monto x TC = Precio Pactado).")
    print("⏳ [Paso 3] Buscando operación en el Core (Excel)...")

try:
    
    df_crudo = pd.read_excel("Insumo Registro de Operaciones Mayo 2026.xlsx")
    df_historico = df_crudo.set_index('Folio Operacion').T
    
    
    df_historico['Fecha Incio'] = pd.to_datetime(df_historico['Fecha Incio']).dt.strftime('%Y-%m-%d')
    df_historico['Fecha Finalización'] = pd.to_datetime(df_historico['Fecha Finalización']).dt.strftime('%Y-%m-%d')
    
    
    coincidencia = df_historico[
        (df_historico['Contraparte'] == datos_extraidos_pdf['Razon_Social']) &
        (df_historico['Tipo Movimiento'] == datos_extraidos_pdf['Tipo_Operacion']) &
        (df_historico['Monto Nominal'] == datos_extraidos_pdf['Monto_Principal']) &
        (df_historico['Fecha Finalización'] == datos_extraidos_pdf['Fecha_Vencimiento'])
    ]

    
    print("\n" + "="*50)
    print(" RESULTADO FINAL DE LA AUTOMATIZACIÓN ")
    print("="*50)

    if not coincidencia.empty:
        folio_encontrado = coincidencia.index[0]
        print(f"🟢 ESTADO: COINCIDENCIA TOTAL")
        print(f"   ► Operación emparejada con el Folio Excel: {folio_encontrado}")
        print("   ► Acción: Registro actualizado a 'CONCILIADO' en base de datos.")
    else:
        print(f"🔴 ESTADO: NO COINCIDENCIA")
        print("   ► No existe un registro con estos parámetros en el histórico.")
        print("   ► Acción: Alerta generada en tablero operativo por posible descuadre.")

except Exception as e:
    print(f"Error al procesar el archivo Excel: {e}")