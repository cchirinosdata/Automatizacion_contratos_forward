# Automatización de Validación de Contratos Forward

## Propósito
Esta solución automatiza la validación de contratos financieros tipo Forward mediante un motor de lógica programada. El objetivo principal es reducir la carga operativa de 100 HH/mes del equipo de operaciones, mitigar el riesgo financiero mediante validaciones matemáticas preventivas y estandarizar el proceso de conciliación contra el histórico transaccional de Credicorp Capital.

## Arquitectura de la Solución
La solución opera bajo un enfoque de Inteligencia Aumentada:

- **Ingestión:** Procesamiento asíncrono de contratos PDF.
- **Motor Lógico:** Validación aritmética obligatoria (Regla de negocio: Monto * TC = Precio).
- **Conciliación:** Cruce automatizado contra el registro histórico en Excel.
- **Gestión de Excepciones:** Protocolo Human-in-the-Loop vía MS Teams para casos con baja confianza en la extracción de datos o discrepancias operativas.

## Requisitos de Ejecución
- Python 3.x
- Librerías: `pandas`, `openpyxl`

## Instalación de dependencias:
```bash
pip install pandas openpyxl
