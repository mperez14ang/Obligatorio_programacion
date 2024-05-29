# main.py

from Utils.alta_especialidad import alta_especialidad
from Utils.alta_socio import alta_socio
from Utils.alta_medico import alta_medico
from Utils.alta_consulta import alta_consulta

def main():
    while True:
        print("Seleccione una opción del menú:")
        print("1. Dar de alta una especialidad")
        print("2. Dar de alta un socio")
        print("3. Dar de alta un médico")
        print("4. Dar de alta una consulta médica")
        print("5. Emitir un ticket de consulta")
        print("6. Realizar consultas")
        print("7. Salir del programa")

        opcion = input()
        if opcion == "1":
            alta_especialidad()
        elif opcion == "2":
            alta_socio()
        elif opcion == "3":
            alta_medico()
        elif opcion == "4":
            alta_consulta()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("La opción seleccionada no es correcta, vuelva a intentar con otra opción.")

if __name__ == "__main__":
    main()
