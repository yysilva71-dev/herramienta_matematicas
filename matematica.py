import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_encabezado():
    print("┌────────────────────────────────────────────────────────┐")
    print("│     SISTEMA MATEMÁTICO: FINANZAS Y PROBABILIDAD        │")
    print("└────────────────────────────────────────────────────────┘")

while True:
    limpiar_pantalla()
    mostrar_encabezado()
    
    print("\n   [1] Interés Simple (Calcular I, C, i, t)")
    print("   [2] Interés Compuesto (Calcular M, C, i, t)")
    print("   [3] Probabilidad Avanzada (Eventos Excluyentes e Independientes)")
    print("   [4] Salir del Sistema")
    print("\n──────────────────────────────────────────────────────────")
    
    opcion = input(" ► Selecciona una opción (1-4): ").strip()
    
    if opcion == "1":
        limpiar_pantalla()
        mostrar_encabezado()
        print("\n [ INTERÉS SIMPLE: ¿Qué dato deseas calcular? ]\n")
        print("   a) Interés generado (I)")
        print("   b) Capital inicial (C)")
        print("   c) Tasa de interés anual (i)")
        print("   d) Tiempo en años (t)")
        
        sub = input("\n ► Elige una letra (a, b, c, d): ").strip().lower()
        print("\n" + "─"*50)

        try:
            if sub == "a":
                c = float(input(" • Capital inicial (C en S/): "))
                i = float(input(" • Tasa de interés anual (i en %): ")) / 100
                t = float(input(" • Tiempo (t en años): "))
                interes = c * i * t
                print(f"\n ► Resultado: Interés generado (I) = S/ {interes:.2f}")

            elif sub == "b":
                I = float(input(" • Interés ganado/generado (I en S/): "))
                i = float(input(" • Tasa de interés anual (i en %): ")) / 100
                t = float(input(" • Tiempo (t en años): "))
                capital = I / (i * t)
                print(f"\n ► Resultado: Capital inicial (C) = S/ {capital:.2f}")

            elif sub == "c":
                I = float(input(" • Interés ganado/generado (I en S/): "))
                c = float(input(" • Capital inicial (C en S/): "))
                t = float(input(" • Tiempo (t en años): "))
                tasa = (I / (c * t)) * 100
                print(f"\n ► Resultado: Tasa de interés (i) = {tasa:.2f}% anual")

            elif sub == "d":
                I = float(input(" • Interés ganado/generado (I en S/): "))
                c = float(input(" • Capital inicial (C en S/): "))
                i = float(input(" • Tasa de interés anual (i en %): ")) / 100
                tiempo = I / (c * i)
                print(f"\n ► Resultado: Tiempo necesario (t) = {tiempo:.2f} años")
            else:
                print("\n [!] Opción no válida.")
        except ZeroDivisionError:
            print("\n [!] Error: No se puede dividir entre cero. Revisa los datos.")
        except ValueError:
            print("\n [!] Error: Por favor ingresa solo números válidos.")

    
    elif opcion == "2":
        import math
        limpiar_pantalla()
        mostrar_encabezado()
        print("\n [ INTERÉS COMPUESTO: ¿Qué dato deseas calcular? ]\n")
        print("   a) Monto Final Acumulado (M)")
        print("   b) Capital Inicial (C)")
        print("   c) Tasa de Interés Anual (i)")
        print("   d) Tiempo en años (t) - Usando Logaritmos")
        
        sub = input("\n ► Elige una letra (a, b, c, d): ").strip().lower()
        print("\n" + "─"*50)

        try:
            if sub == "a":
                c = float(input(" • Capital inicial (C en S/): "))
                i = float(input(" • Tasa de interés anual (i en %): ")) / 100
                t = float(input(" • Tiempo (t en años): "))
                monto = c * ((1 + i) ** t)
                print(f"\n ► Resultado: Monto final (M) = S/ {monto:.2f}")

            elif sub == "b":
                monto = float(input(" • Monto final acumulado (M en S/): "))
                i = float(input(" • Tasa de interés anual (i en %): ")) / 100
                t = float(input(" • Tiempo (t en años): "))
                capital = monto / ((1 + i) ** t)
                print(f"\n ► Resultado: Capital inicial necesario (C) = S/ {capital:.2f}")

            elif sub == "c":
                monto = float(input(" • Monto final acumulado (M en S/): "))
                c = float(input(" • Capital inicial (C en S/): "))
                t = float(input(" • Tiempo (t en años): "))
                tasa = (((monto / c) ** (1 / t)) - 1) * 100
                print(f"\n ► Resultado: Tasa de interés requerida (i) = {tasa:.2f}% anual")

            elif sub == "d":
                monto = float(input(" • Monto final acumulado (M en S/): "))
                c = float(input(" • Capital inicial (C en S/): "))
                i = float(input(" • Tasa de interés anual (i en %): ")) / 100
                # Despeje de tiempo usando logaritmos: t = log(M/C) / log(1+i)
                tiempo = math.log(monto / c) / math.log(1 + i)
                print(f"\n ► Resultado: Tiempo requerido (t) = {tiempo:.2f} años")
            else:
                print("\n [!] Opción no válida.")
        except Exception:
            print("\n [!] Error al realizar el cálculo. Verifica los datos ingresados.")

   
    elif opcion == "3":
        limpiar_pantalla()
        mostrar_encabezado()
        print("\n [ PROBABILIDAD Y TEORÍA DE EVENTOS ]\n")
        print("   a) Eventos Mutuamente Excluyentes: P(A ∪ B) = P(A) + P(B)")
        print("   b) Eventos Independientes: P(A ∩ B) = P(A) × P(B)")
        print("   c) Probabilidad Clásica (Casos Favorables / Totales)")
        
        sub = input("\n ► Elige una opción (a, b, c): ").strip().lower()
        print("\n" + "─"*50)

        try:
            if sub == "a":
                print(" Eventos Mutuamente Excluyentes (No pueden ocurrir al mismo tiempo)\n")
                pa = float(input(" • Probabilidad de A - P(A) (en %): ")) / 100
                pb = float(input(" • Probabilidad de B - P(B) (en %): ")) / 100
                
                if (pa + pb) <= 1:
                    p_union = (pa + pb) * 100
                    print(f"\n ► Resultado: P(A ∪ B) = {p_union:.2f}%")
                else:
                    print("\n [!] Error: La suma de probabilidades no puede exceder el 100%.")

            elif sub == "b":
                print(" Eventos Independientes (Ocurrencia de A no afecta a B)\n")
                pa = float(input(" • Probabilidad de A - P(A) (en %): ")) / 100
                pb = float(input(" • Probabilidad de B - P(B) (en %): ")) / 100
                
                p_interseccion = (pa * pb) * 100
                print(f"\n ► Resultado: P(A ∩ B) = {p_interseccion:.2f}%")

            elif sub == "c":
                fav = float(input(" • Número de casos favorables: "))
                tot = float(input(" • Número total de casos posibles: "))
                if tot > 0 and fav <= tot:
                    prob = (fav / tot) * 100
                    print(f"\n ► Resultado: Probabilidad P(A) = {prob:.2f}%")
                else:
                    print("\n [!] Error: Casos inválidos.")
            else:
                print("\n [!] Opción no válida.")
        except ValueError:
            print("\n [!] Error: Por favor ingresa números válidos.")

    elif opcion == "4":
        print("\n ¡Éxito en la presentación! Nos vemos.\n")
        break

    else:
        print("\n [!] Opción no válida.")

    input("\n Presiona ENTER para volver al menú principal...")