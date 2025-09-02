def hola():
    print ("hola ya se imprimir datos")


#funciones 
#diseñar una encuesta para 6 personas 
#nombre
#carrera
#idea de proyecto



nombres= ["wilman,kevin,stive"]
carreras= ["ing electronica,ing electronica,ing mecatronica"]
idea_de_proyecto= ["no sabe,sistema de gestion para una tienda,tampoco sabe"]
def programa():

    
    nombre= input("ingresa tu nombre: ") 
    nombres.append(nombre)
    carrera= input("que carrera estas estudiando: ")
    carreras.append(carrera)
    idea_proyecto= input("que tienes pesado hacer de proyecto: ")
    idea_de_proyecto.append(idea_proyecto)


    print(nombres,carreras,idea_de_proyecto)

    





























def main():

    #hola()
    programa()
main()