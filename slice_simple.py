def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.
    primeras_tres_letras = texto[:3].lower()
    medio_siendo_tres = texto[2:5].lower()
    Todo_lower = texto[:].lower()
    
    print(primeras_tres_letras)
    print(medio_siendo_tres)
    print(Todo_lower)
slice_simple()

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`

# Mariano Faraldo