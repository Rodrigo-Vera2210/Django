from cursos.models import *

class Carrito():
    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get('skey')
        if 'skey' not in request.session:
            carrito = self.session['skey'] = {'curso': {}, 'recurso': {}}
        self.carrito = carrito

    def add(self, product, tipo):
        productoId = product.id
        if productoId not in self.carrito:
            if tipo == 'cursos':
                self.carrito['curso'][productoId] = {'titulo': product.titulo, 'precio': float(product.precio), 'cant': 1}
            elif tipo == 'recursos':
                self.carrito['recurso'][productoId] = {'titulo': product.titulo, 'precio': float(product.precio), 'cant': 1}
        self.session.modified = True

    def __iter__(self):
        productIds = self.carrito['curso'].keys()
        cursos = Cursos.objects.filter(id__in = productIds)
        carrito = self.carrito.copy()
        for curso in cursos:
            carrito['curso'][str(curso.id)]['product'] = curso
        for item in carrito['curso'].values(): 
            carrito['curso'] = item
            yield carrito 
            
    def __len__(self):
        totalCursos = sum(item['cant'] for item in self.carrito['curso'].values())
        totalRecursos = sum(item['cant'] for item in self.carrito['recurso'].values())
        return totalCursos + totalRecursos
    
    def getTotal(self):
        totalCursos = sum(item['precio'] for item in self.carrito['curso'].values())
        totalRecursos = sum(item['precio'] for item in self.carrito['recurso'].values())
        return totalCursos + totalRecursos
    

    def delete(self, productId, tipo):
        if str(productId) in self.carrito['curso']:
            del self.carrito[tipo][str(productId)]
            print(self.carrito)
            self.session.modified = True