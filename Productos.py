
class Productos():

    def __init__(self, codigo, producto, compra, venta, stock):
        self.codigo = codigo
        self.producto = producto
        self.compra = compra
        self.venta = venta
        self.stock = stock
    
    def getCodigo(self):
        return self.codigo

    def getProducto(self):
        return self.producto
    
    def getCompra(self):
        return self.compra

    def getVenta(self):
        return self.venta
    
    def getStock(self):
        return self.stock