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
            {"codigo": 0, "nombre": "compre 5", "valor":7900},
            {"codigo": 1, "nombre": "compre 3", "valor":5200}
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
            {"codigo": 0, "nombre": "compre 4", "valor":8000},
            {"codigo": 1, "nombre": "compre 7", "valor":10000}
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
            {"codigo": 0, "nombre": "compre 6", "valor":5000},
            {"codigo": 1, "nombre": "compre 3", "valor":3000}
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
print(f"seleccione el producto de la categoria{listaCategoria[opcionCategoria]} que deseas comprar")
precioProd = ["valor"]
for i, val in enumerate(productosCategoria):
  nombre = val["nombre"]
  valor = val["valor"]

  print(f"{i} {nombre} con precio de {valor}")

opcionproducto = int(input())
datosCategoria = menu.get(listaCategoria[opcionCategoria])
promocionesProducto=datosCategoria["promociones"]

promocionesProductos = list()
for val in promocionesProducto:
    if (val.get("codigo") == opcionproducto):
        promocionesProductos.append(val)
if (len(promocionesProductos) == 0):
    print(f"No hay promociones para el producto{datosCategoria['Productos'][opcionproducto]}")   
else:  
    print(f"Promociones del producto{datosCategoria['Productos'][opcionproducto]}") 
    print (promocionesProducto) 

        
#preguntar que cantidad de productos desea adquirir
while True:
    n= int(input("Ingrese la cantidad del producto que desea adquirir: "))
    if n >= 1:
        break

print(f"Usted desea adquirir {n} unidad/es del producto")

dinero = int(input("ingrese la cantidad de dinero disponible: "))
if dinero >= valor:
   vueltos = dinero-valor
   print(f"Usted compro el producto '{opcionproducto}' con valor de ${valor}, sus vueltos son ${vueltos}")
else: 
    print(f"lo sentimos el producto '{opcionproducto}' con un valor de ${valor}, esta fuera de su presupuesto")

   



