import random
##-----------------------------------------------
## DEFINICION DEL GEN PARA EL CROMOSOMA
##-----------------------------------------------
tamaño_poblacion = 3
profesores = ["Rubén", "Ana", "Luis"]


materias = ["Español", "Matemáticas", "Inglés"]

horarios = [
    "Lunes 8-10",
    "Lunes 10-12",
    "Martes 8-10"
]

aulas = ["Aula1"]

def generar_gen():

    materia = random.choice(materias)
    profesor = random.choice(profesores)
    horario = random.choice(horarios)
    aula = random.choice(aulas)
    return {
        "materia": materia,
        "profesor": profesor,
        "aula": aula,
        "horario": horario
    }

##-----------------------------------------------

##-----------------------------------------------
## DEFINICION DEL COMOSOMA gracias a los GEN (TODO EL HORARIO (1))
##-----------------------------------------------
def generar_cromosoma():    
    gen1 = generar_gen()
    gen2 = generar_gen()
    gen3 = generar_gen()
    return([gen1, gen2, gen3])

##-----------------------------------------------

##-----------------------------------------------
## DEFINICION DE POBLACION gracias a los CROMOSOMAS (CONJUNTO DE HORARIOS a evaluar)
##-----------------------------------------------
def generar_poblacion():    
    cromosoma1 = generar_cromosoma()
    cromosoma2 = generar_cromosoma()
    cromosoma3 = generar_cromosoma()
    return([cromosoma1, cromosoma2, cromosoma3])

##-----------------------------------------------

##-----------------------------------------------
## OBTENCION DEL FITNESS POR FUNCION OBJETIVO
##-----------------------------------------------

##FITNESS 
def fitness(horario):
    penalizacion = 0
    # print("horario: ",horario)

    for i in range(len(horario)):
        for j in range(i + 1, len(horario)):

            clase1 = horario[i]
            clase2 = horario[j]

            # DOCENTE en mismo horario
            if (clase1["profesor"] == clase2["profesor"] and
                clase1["horario"] == clase2["horario"]):
                penalizacion += 1000

            # AULA en mismo horario
            if (clase1["aula"] == clase2["aula"] and
                clase1["horario"] == clase2["horario"]):
                penalizacion += 1000

    print("penalizacion de horario:", penalizacion)
    return -penalizacion

##-----------------------------------------------

##===============================================
## FUNCIONES INDIVIDUALES
##===============================================
def seleccionar(poblacion):
    return random.choice(poblacion)

def crossover(padre1, padre2):
    punto = random.randint(1, len(padre1)-1)

    hijo = padre1[:punto] + padre2[punto:]

    return hijo

def mutar(hijo):
    i = random.randint(0, len(hijo)-1)

    # cambiar aula o horario
    hijo[i]['aula'] = random.choice(aulas)
    hijo[i]['horario'] = random.choice(horarios)

    return hijo

##===============================================

##-----------------------------------------------
#   AUTOMATIZADO 
##-----------------------------------------------
poblacion = generar_poblacion()

mejor_global = None
mejor_fitness = float('-inf')

for generacion in range(2):

    # 1. Ordenar población
    poblacion_ordenada = sorted(poblacion, key=fitness, reverse=True)
    # print("POBLACION ORDENADA: ", poblacion_ordenada)
    # print("terminó")
    mejor_actual = poblacion_ordenada[0]
    # print(mejor_actual)
    # exit()
    fit_actual = fitness(mejor_actual)
    # se guardar mejor solucion global
    if fit_actual > mejor_fitness:
        mejor_fitness = fit_actual
        mejor_global = mejor_actual
    print("======================================================")
    print(f"Generación {generacion} - Mejor fitness: {fit_actual}")
    print("======================================================")
    for horario in poblacion_ordenada[0]:
        print("Horario 1: ", horario)
    
    # print(poblacion_ordenada)

    nueva_poblacion = [mejor_actual]

    # generamos hijos
    while len(nueva_poblacion) < tamaño_poblacion:
        padre1 = seleccionar(poblacion)
        padre2 = seleccionar(poblacion)

        hijo = crossover(padre1, padre2)
        hijo = mutar(hijo)

        nueva_poblacion.append(hijo)
    
    # establecemos la nueva problacion sobre la anterior
    poblacion = nueva_poblacion

print("\nMEJOR HORARIO ENCONTRADO:")
print("Fitness:", mejor_fitness)

for clase in mejor_global:
    print(clase)

exit()
