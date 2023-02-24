def cargarContactos():
    info_contactos = leerArchivo()
    # print(info_contactos)
    contactos = []
    for linea in info_contactos:
        linea = linea.replace("\n", "")
        # print(linea)
        c = linea.split(",")
        contactos.append(c)
    print(contactos)

    return contactos


def leerArchivo():
    try:
        nombre_archivo = "contactos" + ".txt"
        archivo = open("Archivos/" + nombre_archivo)
        contenido = archivo.readlines()
        # print(contenido)
        return contenido
    except Exception as error:
        print(error)
        return None
