import re

from Productos import Productos
global listaProductos


class analizadorSintactico:

    def obtenerClaves(self, entrada):
        patron = r'"(.*?)"'
        separaUno = entrada.split("Claves = [\n")
        separados = separaUno[1].split("\n]\n")
        separatres = separados[0]
        listaClaves = re.findall(patron,separatres)
        claves = ",".join(listaClaves)
        claves = (claves+"\n")
        return claves
    
    def obtenerRegistros(self, entrada):
        patron = r'{(.*?)}'
        separaUno = entrada.split("Registros = [\n")
        separados = separaUno[1].split("\n]\n")
        separatres = separados[0]
        listaClaves = re.findall(patron,separatres)
        claves = "\n".join(listaClaves)
        claves = (claves+"\n")
        return claves
    
    def obtenerListaRegisto(self, entrada):
        global listaProductos
        patron = r'{(.*?)}'
        separaUno = entrada.split("Registros = [\n")
        separados = separaUno[1].split("\n]\n")
        separatres = separados[0]
        listaClaves = re.findall(patron,separatres)
        claves = "#".join(listaClaves)
        patronDos = r'"(.*?)"'
        listaProductos = []
        for cla in range(len(listaClaves)):
            separada = listaClaves[cla].split(",")
            codigo = str(separada[0])
            producto = re.findall(patronDos,separada[1])[0]
            compra = separada[2]
            venta = separada[3]
            stock = separada[4]
            producto = Productos(codigo, producto, compra, venta, stock)
            listaProductos.append(producto)
        return listaProductos
    
    def promedioStock(self, entrada):
        global listaProductos
        promedio = 0
        if 'promedio("stock")' in entrada:
            for produc in range(len(listaProductos)):
                promedio += float(listaProductos[produc].getStock())
            noProductos = float(len(listaProductos))
            promedio = str((promedio)/(noProductos))
            promedio = (promedio+"\n")
            return promedio
    
    def promedioCompra(self, entrada):
        global listaProductos
        promedio = 0
        if 'promedio("precio_compra")' in entrada:
            for produc in range(len(listaProductos)):
                promedio += float(listaProductos[produc].getCompra())
            noProductos = float(len(listaProductos))
            promedio = str((promedio)/(noProductos))
            promedio = (promedio+"\n")
            return promedio

    def promedioVenta(self, entrada):
        global listaProductos
        promedio = 0
        if 'promedio("precio_venta")' in entrada:
            for produc in range(len(listaProductos)):
                promedio += float(listaProductos[produc].getVenta())
            noProductos = float(len(listaProductos))
            promedio = str((promedio)/(noProductos))
            promedio = (promedio+"\n")
            return promedio

    def obtenerNoRegis(self, entrada):
        patron = r'{(.*?)}'
        separaUno = entrada.split("Registros = [\n")
        separados = separaUno[1].split("\n]\n")
        separatres = separados[0]
        listaClaves = re.findall(patron,separatres)
        claves = str(len(listaClaves))
        claves = (claves + "\n")
        return claves
    
    def obtenerImprimir(self, entrada):
        separaUno = entrada.split("imprimir(")
        separaDos = separaUno[1]
        separaTres = separaDos.split(");")
        palabra = separaTres[0]
        patron = r'"(.*?)"'
        palabraImp = re.findall(patron,palabra)
        Imp = "\n".join(palabraImp)
        Imp = (Imp+"\n")
        return Imp
    
    def obtenerImprimirln(self, entrada):
        separaUno = entrada.split("imprimirln(")
        separaDos = separaUno[1]
        separaTres = separaDos.split(");")
        palabra = separaTres[0]
        patron = r'"(.*?)"'
        palabraImp = re.findall(patron,palabra)
        Imp = "\n".join(palabraImp)
        Imp = (Imp+"\n")
        return Imp
    
    def contarsi(self, entrada):
        global listaProductos
        if "contarsi" in entrada:
            separaUno = entrada.split("contarsi(")
            separaDos = separaUno[1].split(",")
            pComillas = separaDos[0]
            patron = r'"(.*?)"'
            palabraa = str(re.findall(patron,pComillas)[0])
            num = str(separaDos[1].split(")")[0])
            cuenta = 0
            for busca in range(len(listaProductos)):
                if palabraa == "stock":
                    if str(listaProductos[busca].getStock()) == num:
                        cuenta += 1
                if palabraa == "precio_venta":
                    if str(listaProductos[busca].getVenta()) == num:
                        cuenta += 1
                if palabraa == "precio_compra":
                    if str(listaProductos[busca].getcompra()) == num:
                        cuenta += 1
            cuenta = (str(cuenta)+"\n")
            return cuenta
    
    def obtenerComentarios(self, entrada):
        separaUno = entrada.split("#")
        separaDos = separaUno[1]
        separaTres = separaDos.split("\n")
        palabra = separaTres[0]
        palabra = (palabra+"\n")
        return palabra

    def obtenerMultilinea(self, entrada):
        separaUno = entrada.split("'''\n")
        separaDos = separaUno[1]
        separaTres = separaDos.split("\n'''")
        palabra = separaTres[0]
        palabra = (palabra+"\n")
        return palabra

    def obtenerMaximo(self, entrada):
        global listaProductos
        listaMax = []
        if "max(" in entrada:
            separaUno = entrada.split("max(")
            separaDos = separaUno[1].split(",")
            pComillas = separaDos[0]
            patron = r'"(.*?)"'
            palabraa = str(re.findall(patron,pComillas)[0])
            for busca in range(len(listaProductos)):
                if palabraa == "stock":
                    listaMax.append(float(listaProductos[busca].getStock()))
                if palabraa == "precio_venta":
                    listaMax.append(float(listaProductos[busca].getVenta()))
                if palabraa == "precio_compra":
                    listaMax.append(float(listaProductos[busca].getCompra()))
            maxi = str(max(listaMax))
            return maxi
    
    def obtenerMinimo(self, entrada):
        global listaProductos
        listaMax = []
        if "min(" in entrada:
            separaUno = entrada.split("min(")
            separaDos = separaUno[1].split(",")
            pComillas = separaDos[0]
            patron = r'"(.*?)"'
            palabraa = str(re.findall(patron,pComillas)[0])
            for busca in range(len(listaProductos)):
                if palabraa == "stock":
                    listaMax.append(float(listaProductos[busca].getStock()))
                if palabraa == "precio_venta":
                    listaMax.append(float(listaProductos[busca].getVenta()))
                if palabraa == "precio_compra":
                    listaMax.append(float(listaProductos[busca].getCompra()))
            maxi = str(min(listaMax))
            return maxi
    
    def generarRepo(self, entrada):
        global listaProductos
        separaUno = entrada.split('exportarReporte("')
        separaDos = separaUno[1]
        separaTres = separaDos.split('");')
        titulo = separaTres[0]
        file = open("Reporte Productos.html", "w")
        head = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="reporte.css" type="text/css" />
                <title>Document</title>
                </head>
                <body>
                <h1><span class="blue">&lt;</span>{titulo}<span class="blue">&gt;</span></h1>
                <h3>Productos</h3>
                <table class="container">
                 <thead>
                 <tr>
                 <th>
                 <h1>Codigo</h1>
                 </th>
                 <th>
                 <h1>Producto</h1>
                 </th>
                 <th>
                 <h1>precio_compra</h1>
                 </th>
                 <th>
                 <h1>precio_venta</h1>
                 </th>
                 <th>
                 <h1>stock</h1>
                 </th>
                 </tr>
                 </thead>
                 <tbody>
                """
        file.write(head)
        for x in range(len(listaProductos)):
            linea = f"""
            <tr>
            <td>{listaProductos[x].getCodigo()}</td>
            <td>{listaProductos[x].getProducto()}</td>
            <td>{listaProductos[x].getCompra()}</td>
            <td>{listaProductos[x].getVenta()}</td>
            <td>{listaProductos[x].getStock()}</td>
            </tr>
            """
            file.write(linea)
        end1 = f"""
        </tbody>
        </table>
        """
        file.write(end1)
        endd = f"""
        </body>
        </html>
        """
        file.write(endd)
        file.close()
