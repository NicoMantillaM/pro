menu =dict({ 
    "Panes": {
        "Productos":list([
            {"nombre":"Pan blanco","valor": 2.000},
            {"nombre":"Pan integral", "valor": 3.000},
            {"nombre":"Bollos de pan", "valor":2.800},
            {"nombre":"Baguette", "valor":1.500},
            {"nombre":"Pan de centeno", "valor":5.000},
            {"nombre":"Pan de semillas", "valor":1.000},
            {"nombre":"Pan de ajo", "valor":2.300},
            {"nombre":"Pan de cebolla", "valor":4.000},
            {"nombre":"Pan de maíz", "valor":7.000},
            {"nombre":"Pan de aceitunas", "valor":5.500}
        ]),

        "promociones":list([ 
            {"codigo": 0, "nombre": "compre 5", "valor":7.900},
            {"codigo": 1, "nombre": "compre 3", "valor":5.200}
         ])

    },

     "Postres": {
        "Productos":list([
            {"nombre":"Croissants","valor": 1.000},
            {"nombre":"Magdalenas", "valor": 2.500},
            {"nombre":"Donas", "valor":1.500},
            {"nombre":"Tortas", "valor":2.500},
            {"nombre":"Galletas", "valor":1.000},
            {"nombre":"Brownies", "valor":1.200},
            {"nombre":"Empanadas dulces", "valor":2.600},
            {"nombre":"Rosquillas", "valor":1.300},
            {"nombre":"Palmeritas", "valor":2.200},
            {"nombre":"Tartaletas", "valor":3.500}
        ]),

        "promociones":list([ 
            {"codigo": 0, "nombre": "compre 4", "valor":8.000},
            {"codigo": 1, "nombre": "compre 7", "valor":10.000}
         ])
        
    },

     "Galletas": {
        "Productos":list([
            {"nombre":"Galletas de chocolate","valor": 1.400},
            {"nombre":"Galletas de avena", "valor": 1.200},
            {"nombre":"Galletas de mantequilla", "valor":1.000},
            {"nombre":"Galletas de jengibre", "valor":1.500},
            {"nombre":"Galletas de almendras", "valor":1.200},
            {"nombre":"Galletas de nueces", "valor":1.500},
            {"nombre":"Galletas de coco", "valor":1.000},
            {"nombre":"Galletas de pasas", "valor":1.300},
            {"nombre":"Galletas de miel", "valor":1.500},
            {"nombre":"Galletas de vainilla", "valor":1.200}
        ]),

        "promociones":list([ 
            {"codigo": 0, "nombre": "compre 6", "valor":5.000},
            {"codigo": 1, "nombre": "compre 3", "valor":3.900}
         ]),
     
    },
    
})


#mostrar las opciones de categorias
print ("Sea usted bienvenido a Panderia ElbuenPan")
print ("selecione la categoria de productos que desea adquirir")
listaCategoria = list(menu. keys())
for i, val in enumerate(menu. keys()):
    print(f"       {i}. {val}")

opcionCategoria = int(input())

#obtener los datos de la categoria seleccionada
datosCategoria = menu.get(listaCategoria[opcionCategoria])
productosCategoria=datosCategoria["Productos"]
promocionesCategoria=datosCategoria["promociones"]

print (f"usuario usted selecciono la categoria {listaCategoria[opcionCategoria]} ")

#mostrar los productos de la categoria seleccionada
print ("\nProductos disponibles:")
for producto in productosCategoria:
    print("- Nombre:", producto["nombre"], "| Valor:", producto["valor"])

#mostrar las promociones de la categoria seleccionada
print ("\npromociones disponibles:")  
for promocion in promocionesCategoria:
    print("- Nombre:", promocion["nombre"], "| Valor:", promocion["valor"]) 

#permitir al usuario elegir el producto o la promocion de la categoria
escogProductoPromo = input("Seleccione el número del producto/promoción que desea adquirir:")

 












