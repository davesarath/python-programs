class bat:
    # def __init__(self):
    #     pass

    def sum(self,a,b):
        self.k= a+b
        return self.k

# m1=bat()
# print m1.sum(20,30)

class sup(bat):
    def mul(self,a,b):
        self.l=a*b
        return self.l
# m2=sup()
# print m2.mul(10,20)
# print m2.sum(10,20)

class wonder(sup,bat):
    pass

# m3=wonder()
#
# print m3.mul(10,20)
# print m3.l
# print m3.sum(40,50)
# print m3.k
# print m3.l

class jl(sup):
    pass

m3=jl()

print m3.mul(10,20)
print m3.l
print m3.sum(40,50)
print m3.k
