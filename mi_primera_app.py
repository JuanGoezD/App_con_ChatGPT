import streamlit as st

# Título y autor
st.title("Conversor de Unidades")
st.write("Esta app fue elaborada por \"Tu Nombre\".")

# Lista desplegable para seleccionar el tipo de conversión
opcion_conversion = st.selectbox("Seleccione el tipo de conversión:",
                                 ["Temperatura", "Longitud", "Masa", "Volumen",
                                  "Tiempo", "Velocidad", "Área", "Energía",
                                  "Presión", "Tamaño de Datos"])

# Mostrar el tipo de conversión seleccionado
st.write(f"Ha seleccionado la conversión de {opcion_conversion}.")

# Definir las opciones de conversión según el tipo seleccionado
opciones_siguientes = []

if opcion_conversion == "Temperatura":
    opciones_siguientes = ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"]
    # Mostrar la lista de opciones siguientes
    conversion_especifica = st.selectbox("Seleccione la conversión:", opciones_siguientes)
    
    # Área para ingresar la cantidad a convertir
    cantidad = st.number_input("Ingrese la cantidad a convertir:")
    resultado = 0.0  # Inicializar el resultado
    
    # Realizar la conversión según la opción seleccionada
    if conversion_especifica == "Celsius a Fahrenheit":
        resultado = (cantidad * 9/5) + 32
    elif conversion_especifica == "Fahrenheit a Celsius":
        resultado = (cantidad - 32) * 5/9
    elif conversion_especifica == "Celsius a Kelvin":
        resultado = cantidad + 273.15
    elif conversion_especifica == "Kelvin a Celsius":
        resultado = cantidad - 273.15

    st.write(f"Resultado: {resultado:.4f}")

elif opcion_conversion == "Longitud":
    opciones_siguientes = ["Pies a Metros", "Metros a Pies", "Pulgadas a Centímetros", "Centímetros a Pulgadas"]
    conversion_especifica = st.selectbox("Seleccione la conversión:", opciones_siguientes)
    
    # Área para ingresar la cantidad a convertir
    cantidad = st.number_input("Ingrese la cantidad a convertir:")
    resultado = 0.0  # Inicializar el resultado
    
    # Realizar la conversión según la opción seleccionada
    if conversion_especifica == "Pies a Metros":
        resultado = cantidad * 0.3048
    elif conversion_especifica == "Metros a Pies":
        resultado = cantidad / 0.3048
    elif conversion_especifica == "Pulgadas a Centímetros":
        resultado = cantidad * 2.54
    elif conversion_especifica == "Centímetros a Pulgadas":
        resultado = cantidad / 2.54
    
    # ... (continuar con las demás conversiones)
    
    st.write(f"Resultado: {resultado:.4f}")

elif opcion_conversion == "Masa":
    opciones_siguientes = ["Libras a Kilogramos", "Kilogramos a Libras", "Onzas a Gramos", "Gramos a Onzas"]
    conversion_especifica = st.selectbox("Seleccione la conversión:", opciones_siguientes)

    # Área para ingresar la cantidad a convertir
    cantidad = st.number_input("Ingrese la cantidad a convertir:")
    resultado = 0.0  # Inicializar el resultado

    # Realizar la conversión según la opción seleccionada
    if conversion_especifica == "Libras a Kilogramos":
        resultado = cantidad * 0.453592
    elif conversion_especifica == "Kilogramos a Libras":
        resultado = cantidad / 0.453592
    elif conversion_especifica == "Onzas a Gramos":
        resultado = cantidad * 28.3495
    elif conversion_especifica == "Gramos a Onzas":
        resultado = cantidad / 28.3495

    st.write(f"Resultado: {resultado:.4f}")

elif opcion_conversion == "Volumen":
    opciones_siguientes = ["Galones a Litros", "Litros a Galones", "Pulgadas cúbicas a Centímetros cúbicos", "Centímetros cúbicos a Pulgadas cúbicas"]
  # Mostrar la lista de opciones siguientes
    conversion_especifica = st.selectbox("Seleccione la conversión:", opciones_siguientes)
    
    # Área para ingresar la cantidad a convertir
    cantidad = st.number_input("Ingrese la cantidad a convertir:")
    resultado = 0.0  # Inicializar el resultado
    
    # Realizar la conversión según la opción seleccionada
    if conversion_especifica == "Galones a Litros":
        resultado = cantidad * 3.78541
    elif conversion_especifica == "Litros a Galones":
        resultado = cantidad / 3.78541
    elif conversion_especifica == "Pulgadas cúbicas a Centímetros cúbicos":
        resultado = cantidad * 16.3871
    elif conversion_especifica == "Centímetros cúbicos a Pulgadas cúbicas":
        resultado = cantidad / 16.3871
  
  # ... (continuar con las demás conversiones)
  
    st.write(f"Resultado: {resultado:.4f}")

elif opcion_conversion == "Tiempo":
    opciones_siguientes = ["Horas a Minutos", "Minutos a Segundos", "Días a Horas", "Semanas a Días"]
    conversion_especifica = st.selectbox("Seleccione la conversión:", opciones_siguientes)
    
    # Área para ingresar la cantidad a convertir
    cantidad = st.number_input("Ingrese la cantidad a convertir:")
    resultado = 0.0  # Inicializar el resultado
    
    # Realizar la conversión según la opción seleccionada
    if conversion_especifica == "Horas a Minutos":
        resultado = cantidad * 60
    elif conversion_especifica == "Minutos a Segundos":
        resultado = cantidad * 60
    elif conversion_especifica == "Días a Horas":
        resultado = cantidad * 24
    elif conversion_especifica == "Semanas a Días":
        resultado = cantidad * 7
  
  # ... (continuar con las demás conversiones)
  
    st.write(f"Resultado: {resultado:.4f}")

elif opcion_conversion == "Velocidad":
    opciones_siguientes = ["Millas por hora a Kilómetros por hora", "Kilómetros por hora a Metros por segundo", "Nudos a Millas por hora", "Metros por segundo a Pies por segundo"]
    conversion_especifica = st.selectbox("Seleccione la conversión:", opciones_siguientes)
    
    # Área para ingresar la cantidad a convertir
    cantidad = st.number_input("Ingrese la cantidad a convertir:")
    resultado = 0.0  # Inicializar el resultado
    
    # Realizar la conversión según la opción seleccionada
    if conversion_especifica == "Millas por hora a Kilómetros por hora":
        resultado = cantidad * 1.60934
    elif conversion_especifica == "Kilómetros por hora a Metros por segundo":
        resultado = cantidad * 0.277778
    elif conversion_especifica == "Nudos a Millas por hora":
        resultado = cantidad * 1.15078
    elif conversion_especifica == "Metros por segundo a Pies por segundo":
        resultado = cantidad * 3.28084
    
    # ... (continuar con las demás conversiones)
    
    st.write(f"Resultado: {resultado:.4f}")

elif opcion_conversion == "Área":
    opciones_siguientes = ["Metros cuadrados a Pies cuadrados", "Pies cuadrados a Metros cuadrados", "Kilómetros cuadrados a Millas cuadradas", "Millas cuadradas a Kilómetros cuadrados"]
    # Mostrar la lista de opciones siguientes
    conversion_especifica = st.selectbox("Seleccione la conversión:", opciones_siguientes)
    
    # Área para ingresar la cantidad a convertir
    cantidad = st.number_input("Ingrese la cantidad a convertir:")
    resultado = 0.0  # Inicializar el resultado
    
    # Realizar la conversión según la opción seleccionada
    if conversion_especifica == "Metros cuadrados a Pies cuadrados":
        resultado = cantidad * 10.7639
    elif conversion_especifica == "Pies cuadrados a Metros cuadrados":
        resultado = cantidad / 10.7639
    elif conversion_especifica == "Kilómetros cuadrados a Millas cuadradas":
        resultado = cantidad * 0.386102
    elif conversion_especifica == "Millas cuadradas a Kilómetros cuadrados":
        resultado = cantidad / 0.386102
    
    # ... (continuar con las demás conversiones)
    
    st.write(f"Resultado: {resultado:.4f}")

elif opcion_conversion == "Energía":
    opciones_siguientes = ["Julios a Calorías", "Calorías a Kilojulios", "Kilovatios-hora a Megajulios", "Megajulios a Kilovatios-hora"]
      # Mostrar la lista de opciones siguientes
    conversion_especifica = st.selectbox("Seleccione la conversión:", opciones_siguientes)
    
    # Área para ingresar la cantidad a convertir
    cantidad = st.number_input("Ingrese la cantidad a convertir:")
    resultado = 0.0  # Inicializar el resultado
    
    # Realizar la conversión según la opción seleccionada
    if conversion_especifica == "Julios a Calorías":
        resultado = cantidad * 0.239006
    elif conversion_especifica == "Calorías a Kilojulios":
        resultado = cantidad / 0.239006
    elif conversion_especifica == "Kilovatios-hora a Megajulios":
        resultado = cantidad * 3.6
    elif conversion_especifica == "Megajulios a Kilovatios-hora":
        resultado = cantidad / 3.6
    
    # ... (continuar con las demás conversiones)
    
    st.write(f"Resultado: {resultado:.4f}")

elif opcion_conversion == "Presión":
    opciones_siguientes = ["Pascales a Atmósferas", "Atmósferas a Pascales", "Barras a Libras por pulgada cuadrada", "Libras por pulgada cuadrada a Bares"]
    # Mostrar la lista de opciones siguientes
    conversion_especifica = st.selectbox("Seleccione la conversión:", opciones_siguientes)
    
    # Área para ingresar la cantidad a convertir
    cantidad = st.number_input("Ingrese la cantidad a convertir:")
    resultado = 0.0  # Inicializar el resultado
    
    # Realizar la conversión según la opción seleccionada
    if conversion_especifica == "Pascales a Atmósferas":
        resultado = cantidad / 101325
    elif conversion_especifica == "Atmósferas a Pascales":
        resultado = cantidad * 101325
    elif conversion_especifica == "Barras a Libras por pulgada cuadrada":
        resultado = cantidad * 14.5038
    elif conversion_especifica == "Libras por pulgada cuadrada a Bares":
        resultado = cantidad / 14.5038
    
    # ... (continuar con las demás conversiones)
    
    st.write(f"Resultado: {resultado:.4f}")

elif opcion_conversion == "Tamaño de Datos":
    opciones_siguientes = ["Megabytes a Gigabytes", "Gigabytes a Terabytes", "Kilobytes a Megabytes", "Terabytes a Petabytes"]
    # Mostrar la lista de opciones siguientes
    conversion_especifica = st.selectbox("Seleccione la conversión:", opciones_siguientes)
    
    # Área para ingresar la cantidad a convertir
    cantidad = st.number_input("Ingrese la cantidad a convertir:")
    resultado = 0.0  # Inicializar el resultado
    
    # Realizar la conversión según la opción seleccionada
    if conversion_especifica == "Megabytes a Gigabytes":
        resultado = cantidad * 0.001
    elif conversion_especifica == "Gigabytes a Terabytes":
        resultado = cantidad * 0.001
    elif conversion_especifica == "Kilobytes a Megabytes":
        resultado = cantidad * 0.001
    elif conversion_especifica == "Terabytes a Petabytes":
        resultado = cantidad * 0.001
    
    # ... (continuar con las demás conversiones)
    
    st.write(f"Resultado: {resultado:.4f}")


