def ej1crea_un_diccionario1(datos):#usando setdefault
 datos= input("Ingrese los datos: nombre, edad o salir para acabar")
 #nom=[]
 #ed=[]
 dicc={}
 while datos != "salir":
   #datos= input("Ingrese los datos: nombre, edad o salir para acabar")
   nombres,edad= datos.split(",")
   edad=int(edad)
   dicc.setdefault(nombres,edad)
   #nom.append(nombres)
   #ed.append(edad)
   datos=input("Ingrese los datos: nombre, edad o salir para acabar")
 print(dicc)




def ej1crea_un_diccionario2(datos):#solucion del profe
  datos=""
  d={}
  while datos != "salir":
    datos=input("Ingrese los datos: nombre, edad o salir para acabar")
    if datos != "salir":
      nom,ed= datos.split(",")
      ed= int(ed)
      d[nom]= ed

  print (d)


       


def ej2contar_cadena (cadena):#usando update
  cadena= input("Ingrese una cadena de caracteres")
  dic={}
  for caracter in cadena:
    if caracter not in dic:
      dic.update({caracter:1})
    else:
      dic[caracter]+=1
  return dic
    


def ej3PresentacioDiccionario(diccionario):
  diccionario= ej2contar_cadena ("cadena")
  a=diccionario.items()
  lst=list(a)
  for clave, valor in lst:
    print(" {}   {}  ".format(clave,valor))


notas={202009973:[3,3,4,5], 202312345:[5,4,3,2], 202345678:[5,5,5,5]}

def calificaciones (notas, matricula):
  matricula = input ("ingrese matricula")
  if matricula not in notas:
    n1=int(input("ingrese tres notas separadas por comas"))
    lst_cal=[]
    lst_cal.append(n)
    notas.update({matricula:lst_cal})
  else:
    n2=int(input("ingrese una nota adicional"))
    alumno= notas.get(matricula)
    nueva_nota=[]
    for calif in alumno:
      nueva_nota.append(calif)
    nueva_nota.append(n2)
    notas[matricula]=nueva_nota
  print(notas)

  
      


      





















#ej1crea_un_diccionario1("datos")
#ej1crea_un_diccionario2("datos")
#ej2contar_cadena("cadena")
#ej3PresentacioDiccionario("diccionario")
calificaciones("notas","matricula")