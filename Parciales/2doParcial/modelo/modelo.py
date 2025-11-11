class Modelo:
    def __init__(self):
        self.pila_num = []
        self.pila_op = []

    def limpiar(self):
        self.pila_num = []
        self.pila_op = []

    def precedencia(self, op):
        if op in ['+', '-']:
            return 1
        elif op in ['*', '/']:
            return 2
        else:
            return 0
    def aplicar_operador(self, op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b

    def obt_exp(self, exp):
        num = ""
        for c in exp:
            if c.isdigit():
                num += c
            else: 
                if num:
                    self.pila_num.append(int(num))
                    num = ""
                self.pila_op.append(c)
        if num:
            self.pila_num.append(int(num))

    def prefija(self):
        ops = self.pila_op.copy()
        nums = [str(n) for n in self.pila_num]
        op_pila = []

        for c in ops:
            while op_pila and self.precedencia(op_pila[-1]) >= self.precedencia(c):
                op = op_pila.pop()
                a = nums.pop(0)
                b = nums.pop(0)
                nums.insert(0, op + a + b)
            op_pila.append(c)

        while op_pila:
            op = op_pila.pop()
            a = nums.pop(0)
            b = nums.pop(0)
            nums.insert(0, op + a + b)

        return nums[0]
    
    def evaluar(self):
        ops = self.pila_op.copy()
        nums = self.pila_num.copy()
        op_pila = []

        def aplicar(op, a, b):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return a / b

        for c in ops:
            while op_pila and self.precedencia(op_pila[-1]) >= self.precedencia(c):
                op = op_pila.pop()
                a = nums.pop(0)
                b = nums.pop(0)
                nums.insert(0, aplicar(op, a, b))
            op_pila.append(c)

        while op_pila:
            op = op_pila.pop()
            a = nums.pop(0)
            b = nums.pop(0)
            nums.insert(0, aplicar(op, a, b))

        return nums[0]