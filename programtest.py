'''Sofware que captura calificaciones de las materias
Jonatan Caleb Rico Granados
6519150034
EVALUACIÓN Y MEJORA PARA EL DESARROLLO DE SOFTWARE (MARCO MUÑOZ)
'''
#Funcion para mostrar las calificaciones
def showgrades(n, grades):
    for i in range(0, len(grades)):
        print(grades[i])

#Funcion para obtener el promedio de las calificaciones guardadas
def mean(n,grades):
    subtotal = 0
    for i in range(0, len(grades)):
            subtotal += grades[i]

    average = subtotal / n
    print(average)

if __name__ == '__main__':
    #Pide al usuario la cantidad de materias
    n = int(input("Introduce subjects amount: "))
    grades = []
    num = 0

    #Ciclo para introducir las calificaciones de la materia
    for i in range(1,n+1):
        num = int(input("Subject {} grade: ".format(i)))
        grades.append(num)

    choice = int(input('''Choose the option you want to see:
        [1]Show grades
        [2]Show Mean of grades
        [3]Both
        '''))
    if choice == 1:
        showgrades(n,grades)
    elif choice == 2:
        mean(n, grades)
    elif choice == 3:
        showgrades(n,grades)
        mean(n,grades)
    else:
        print("Try again with a number between 1-3")