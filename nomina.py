TSS_TOTAL = 5.91 / 100
BONIFICACION_PORC = 10 / 100

ISR_TRAMOS = [
    (416220.00, 0.00,   0.00),
    (624329.00, 0.15,   0.00),
    (867123.00, 0.20, 31205.00),
    (float('inf'), 0.25, 79775.00),
]

def calcular_isr_mensual(anual):
    if anual <= ISR_TRAMOS[0][0]:
        return 0
    for i in range(1, len(ISR_TRAMOS)):
        tope, pct, cuota = ISR_TRAMOS[i]
        if anual <= tope:
            excedente = anual - ISR_TRAMOS[0][0]
            return (excedente * pct + cuota) / 12
    # Excede todos los tramos
    excedente = anual - ISR_TRAMOS[2][0]
    return (excedente * ISR_TRAMOS[3][1] + ISR_TRAMOS[3][2]) / 12

def main():
    try:
        sueldo_bruto = float(input("Sueldo bruto mensual (RD$): "))
        otros_desc = float(input("Otros descuentos (RD$): "))
        bonificacion_activa = input("¿Quieres aplicar bonificación? (s/n): ").strip().lower() == 's'
        
        if sueldo_bruto <= 0:
            raise ValueError("Debe ser mayor que cero.")

        ss = sueldo_bruto * TSS_TOTAL
        isr = calcular_isr_mensual(sueldo_bruto * 12)
        bonif = sueldo_bruto * BONIFICACION_PORC if bonificacion_activa else 0
        neto = sueldo_bruto - ss - isr - otros_desc + bonif

        print("\n{:<8} {:<25} {:>12}".format("COD", "CONCEPTO", "VALOR (RD$)"))
        print("-" * 50)
        print("{:<8} {:<25} {:>12.2f}".format("SALARI", "SALARIO", sueldo_bruto))
        print("{:<8} {:<25} {:>12.2f}".format("TSS",    "SEG. SOCIAL", ss))
        print("{:<8} {:<25} {:>12.2f}".format("ISR",    "IMP. RENTA", isr))
        print("{:<8} {:<25} {:>12.2f}".format("OTROS",  "OTROS DESC.", otros_desc))
        if bonificacion_activa:
            print("{:<8} {:<25} {:>12.2f}".format("BONIF",  "BONIFICACIÓN", bonif))
        print("-" * 50)
        print("{:<8} {:<25} {:>12.2f}".format("",       "SUELDO NETO", neto))

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
