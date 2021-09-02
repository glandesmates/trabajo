# a)

limiteAlumnos = int(input('Ingrese la cantidad de usuarios a registrar: '))
while limiteAlumnos < 0:
    limiteAlumnos = int(input('Ingrese un número válido: '))
print()

alumnos = []; count = 0
for alumno in range(limiteAlumnos):
    count += 1
    alumno = input(f'Ingrese nombre del alumno ({count} de {limiteAlumnos}): ')
    while alumno == '':
        alumno = input(f'Ingrese nombre del alumno ¡VÁLIDO! ({count} de {limiteAlumnos}): ')
    alumnos.append(alumno)
    print()


print("""
    [1] Consultar           [3] Verificar Resultados
    [2] Ingresar datos      [4] Salir del programa
    """); desicion = input(" "*27); print()

if desicion == '2':
    
    def calificar(materia, limite):

        if materia == 'examen':
            evaluar = int(input(f'Ingrese calificación de {materia}: '))
            while evaluar > limite or evaluar < 0:
                evaluar = int(input(f'Ingrese calificación de {materia} (de 0 a {limite}): '))
        
        else:
            evaluar = int(input(f'Ingrese calificación de {materia}: '))
            while evaluar > limite or evaluar < 1:
                evaluar = int(input(f'Ingrese calificación de {materia} (de 1 a {limite}): '))

        return evaluar

    cata = []; cate = []
    cale = []; capr = []
    caex = []; cato = []

    for alumno in alumnos:
        print('Calificando ' + alumno)
        ta = calificar('tareas', 10)
        te = calificar('talleres', 15)
        le = calificar('lecciones', 20)
        pr = calificar('proyecto', 15)
        ex = calificar('examen', 40)
        to = ta+te+le+pr+ex
        print()

        cata.append(ta); cate.append(te)
        cale.append(le); capr.append(pr)
        caex.append(ex); cato.append(to)

    
    # d)
    nombre_mas_largo = len(max(alumnos))
    sep = " "*nombre_mas_largo

    print(f"Alumno        Tareas Talleres Lecciones Proyecto Examen")
    for alumno, a,b,c,d,e in zip(alumnos,cata,cate,cale,capr,caex):
        if nombre_mas_largo - len(alumno) != 0:
            print(f"{alumno + sep + ' '*(nombre_mas_largo - len(alumno))}{a}         {b}       {c}       {d}        {e}")
        else:
            print(f"{alumno + sep}{a}          {b}      {c}       {d}        {e}")
    # e)
    print('\nPromedio final: ' + str(sum(cato)/limiteAlumnos)); print()


    # f)
    
    for i in range(len(cato)):
        
        if nombre_mas_largo - len(alumnos[i]) != 0 and cato[i] < 70:
            print(f"{alumnos[i] + sep + ' '*(nombre_mas_largo - len(alumnos[i]))}   REPROBADO   | TOTAL {cato[i]}")
        elif nombre_mas_largo - len(alumnos[i]) != 0 and cato[i] > 70:    
            print(f"{alumnos[i] + sep + ' '*(nombre_mas_largo - len(alumnos[i]))}   APROBADOS   | TOTAL {cato[i]}")

        else:
            if cato[i] < 70:
                print(f"{alumno + sep}   REPROBADO   | TOTAL {cato[i]}")
            elif cato[i] > 70:
                print(f"{alumno + sep}   APROBADO   | TOTAL {cato[i]}")

    print()

    for i in range(len(cato)):
        if cato[i] == max(cato):
            print("El mejor estudiante de Fundamentos de la Programación: " + alumnos[i] + " | TOTAL: " + str(cato[i]))

elif desicion == '4':
    exit()

while desicion not in ['1','2','3','4']:
    desicion = input('Ingrese una opción válida: ')
