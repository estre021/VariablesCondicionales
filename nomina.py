TSS_TOTAL = 5.91 / 100
BONIFICACION_PORC = 10 / 100
ISR_TRAMOS = [
    (416220.00, 0.00,   0.00),
    (624329.00, 0.15,   0.00),
    (867123.00, 0.20, 31205.00),
    (float('inf'), 0.25, 79775.00),
]

def calcular_isr_mensual(anual):
    for tope, pct, cuota in ISR_TRAMOS:
        if anual <= tope:
            excedente = max(anual - 416220.01, 0)
            return (excedente * pct + cuota) / 12
    return 0

def main():
    try:
        sueldo_bruto = float(input("Sueldo bruto mensual (RD$): "))
        otros_desc = float(input("Otros descuentos (RD$): "))
        if sueldo_bruto <= 0:
            raise ValueError("Debe ser mayor que cero.")

        # Cálculos
        ss = sueldo_bruto * TSS_TOTAL
        isr = calcular_isr_mensual(sueldo_bruto * 12)
        bonif = sueldo_bruto * BONIFICACION_PORC
        neto = sueldo_bruto - ss - isr - otros_desc + bonif

        # Salida tipo tabla
        print("\n{:<8} {:<25} {:>12}".format("COD", "CONCEPTO", "VALOR (RD$)"))
        print("-" * 50)
        print("{:<8} {:<25} {:>12.2f}".format("SALARI", "SALARIO", sueldo_bruto))
        print("{:<8} {:<25} {:>12.2f}".format("TSS",    "SEG. SOCIAL", ss))
        print("{:<8} {:<25} {:>12.2f}".format("ISR",    "IMP. RENTA", isr))
        print("{:<8} {:<25} {:>12.2f}".format("OTROS",  "OTROS DESC.", otros_desc))
        print("{:<8} {:<25} {:>12.2f}".format("BONIF",  "BONIFICACIÓN", bonif))
        print("-" * 50)
        print("{:<8} {:<25} {:>12.2f}".format("",       "SUELDO NETO", neto))

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()