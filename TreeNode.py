class RBN(object):
    def __init__(self, data):
        self.data = data
        self.color = 0
        self.left = None
        self.rigth = None
        self.parent = None

class RBT(object):
    def __init__(self):
        self.root = None

    def midTraverse(self, x):
        if x == None:
            return
        self.midTraverse(x.left)
        colorStr = 'negro'
        if x.color == 1:
            colorStr = 'negro'
        else:
            colorStr = 'rojo'
        self.midTraverse(x.rigth)

    def add(self, x):
        if self.root == None:
            self.root = x
            x.color = 1
            print('Agregar nodo raiz', x.data)
            return
        
        p = self.root
        while p != None:
            if x.data < p.data:
                if p.left == None:
                    p.left = x
                    x.parent = p
                    print('Agragar y rotar al nodo izquierdo')
                    self.addFix(x)
                    break
                p = p.left
            else:
                if p.rigth == None:
                    p.rigth = x
                    x.parent = p
                    print('Agragar y rotar al nodo derecho')
                    self.addFix(x)
                    break
                p = p.rigth
            
        def addFix(self, x):
            while True:
                if x == self.root:
                    x.color = 1
                    return
                p = x.parent
                if p.color == 1 or x.color == 1:
                    return
                g = p.parent
                u = g.left if p == g.rigth else g.rigth
                if u != None and u.color == 0:
                    u.color = p.color = 1
                    g.color = 0
                    x = g
                    continue

                if p == g.left and x == p.left:
                    self.rotateRigth(p)
                elif p == g.left and x == p.rigth:
                    self.rotateLeft(x)
                    self.rotateRight(x)
                elif p == g.rigth and x == p.rigth:
                    self.rotateLeft(p)
                elif p == g.rigth and x == p.left:
                    self.rotateRigth(x)
                    self.rotateLeft(x)



    

    if __name__ == '__main__':
        rbt = RBT()

        datas = [10, 20, 30, 15, 25, 5, 35]

        for dato in datas:
            rbt.add(RBN(dato))

        rbt.midTraverse(rbt.root)

            
    
