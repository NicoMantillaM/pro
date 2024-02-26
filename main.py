#informacion
nombre= input("ingrese su nombre: ")
edad= input("ingrese su edad: ")
altura= input ("ingrese su altura: ")
info= tuple ((nombre, edad, altura))
print (f"""El usuario {info[0]} tiene {info [1]} años y mide {info[ 2]} cm""")
 
 #direccion
dirca= input("ingrese su direccion de hogar: ")
dirtra= input("ingrese la direccion de su trabajo: ")
dirAle= input("ingrese la direccion de sus hogares aledaños: ")
direcciones= tuple((dirca, dirtra, dirAle))
print (f""" La direccion de su hogar es {direcciones[0]} su trabajo esta ubicado en {direcciones[1]} y su residencia aledaña es en {direcciones[2]}""")

#educacion
nve=input("ingrese su nivel de estudios: ")
cur= input("ingrese los cursos con los que cuenta: ")
prof= input("ingrese la profesion que tenga: ")
edu= tuple((nve,cur,prof))
print (f""" El usuario cuenta con un nivel de estudio {edu[0]} cuenta con cursos de {edu[1]}  y tiene de profesion o titulos en {edu[2]}""")

#expelab
exp= input("cuenta con experiencia laboral: ")
labs= input("en que trabajos tiene experiencia: ")
expla= tuple((exp, labs))
print (f"""El usuario cuenta con experiencia laboral {expla[0]} y ha trabajado en {expla[1]}""")




