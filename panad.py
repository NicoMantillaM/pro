menu =dict({ 
    "Panes": {
        "Productos":list([
            {"nombre":"Pan blanco","valor": 2000},
            {"nombre":"Pan integral", "valor": 3000},
            {"nombre":"Bollos de pan", "valor":2800},
            {"nombre":"Baguette", "valor":1500},
            {"nombre":"Pan de centeno", "valor":5000},
            {"nombre":"Pan de semillas", "valor":1000},
            {"nombre":"Pan de ajo", "valor":2300},
            {"nombre":"Pan de cebolla", "valor":4000},
            {"nombre":"Pan de maíz", "valor":7000},
            {"nombre":"Pan de aceitunas", "valor":5500}
        ]),

        "promociones":list([ 
            {"codigo": 0, "promocion": "desc5", "balor":0.35},
            {"codigo": 1, "promocion": "desc6", "balor":0.15}
         ])

    },

     "Postres": {
        "Productos":list([
            {"nombre":"Croissants","valor": 1000},
            {"nombre":"Magdalenas", "valor": 2500},
            {"nombre":"Donas", "valor":1500},
            {"nombre":"Tortas", "valor":2500},
            {"nombre":"Galletas", "valor":1000},
            {"nombre":"Brownies", "valor":1200},
            {"nombre":"Empanadas dulces", "valor":2600},
            {"nombre":"Rosquillas", "valor":1300},
            {"nombre":"Palmeritas", "valor":2200},
            {"nombre":"Tartaletas", "valor":3500}
        ]),

        "promociones":list([ 
            {"codigo": 0, "promocion": "desc3", "balor":0.20},
            {"codigo": 1, "promocion": "desc4", "balor":0.25}
         ])
        
    },

     "Galletas": {
        "Productos":list([
            {"nombre":"Galletas de chocolate","valor": 1400},
            {"nombre":"Galletas de avena", "valor": 1200},
            {"nombre":"Galletas de mantequilla", "valor":1000},
            {"nombre":"Galletas de jengibre", "valor":1500},
            {"nombre":"Galletas de almendras", "valor":1200},
            {"nombre":"Galletas de nueces", "valor":1500},
            {"nombre":"Galletas de coco", "valor":1000},
            {"nombre":"Galletas de pasas", "valor":1300},
            {"nombre":"Galletas de miel", "valor":1500},
            {"nombre":"Galletas de vainilla", "valor":1200}
        ]),

        "promociones":list([ 
            {"codigo": 0, "promocion": "desc1", "balor":0.17},
            {"codigo": 1, "promocion": "desc2", "balor":0.23}
         ]),
     
    },
    
})


#mostrar las opciones de categorias
print ("Sea usted bienvenido a Panaderia ElbuenPan")
print ("seleccione la categoria de productos que desea adquirir")
listaCategoria = list(menu. keys())
for i, val in enumerate(menu. keys()):
    print(f"       {i}. {val}")

opcionCategoria = int(input())

#obtener los datos de la categoria seleccionada
datosCategoria = menu.get(listaCategoria[opcionCategoria])
productosCategoria=datosCategoria["Productos"]


#correcion segun clase
print(f"seleccione el producto de la categoria {listaCategoria[opcionCategoria]} que deseas comprar")
for i, val in enumerate(productosCategoria):
  nombre = val["nombre"]
  vale = val["valor"]
  print(f"{i} {nombre} con precio de {vale}")

opcionproducto = int(input())

muestra = productosCategoria [opcionproducto]. get ("nombre")
muestrap= productosCategoria [opcionproducto]. get ("valor")


datosCategoria = menu.get(listaCategoria[opcionCategoria])
promocionesProducto=datosCategoria["promociones"]


#preguntar que cantidad de productos desea adquirir
print ("Ingrese la cantidad de unidades del producto que desea adquirir: ")
cantidad = int(input())
promocionesProductos = list()

for val in promocionesProducto:
    if (val.get("codigo") == opcionproducto):
        promocionesProductos.append(val)
descu= val["promocion"]
valos= val["balor"]
des=int(valos*100)
vari= muestrap*cantidad
pres1= vari*valos
pres2= vari-pres1


if (len(promocionesProductos) == 0):
    print(f"No hay promociones para el producto {muestra}")   
    print ("Su producto cuesta : $",vari)
else:  
    print(f"Promociones del producto{muestra}") 
    print(f"el producto{muestra} tiene {descu} del",des,  "% de descuento")
    print (f"Desea aplicar el descuento disponible para {muestra}?, Ingrese 1, Si su opcion es Si, Ingrese 2, Si su opcion es No ")
deci= int(input())
if deci== 1:
    print("Usted escogio aplicar el descuento al producto" )
    print("valor sin descuento: ", vari )
    print("valor con descuento: ",int(pres2) )
    vari= int(pres2)
else:
    print("valor sin descuento: ", vari )


dinero = int(input ("ingrese la cantidad de dinero disponible: "))
vueltos = dinero-vari
if dinero >= vari:
   print(f"Usted compro el producto '{muestra}' con valor de ${vari}, sus vueltos son ${vueltos}")
else: 
    print(f"lo sentimos el producto '{muestra}' con un valor de ${vari}, esta fuera de su presupuesto")


   



