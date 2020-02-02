class circle:
    def __init__(self,ra):
        self.ra=ra
    def __add__(self, other):
        return self.ra+other.ra

c1=circle(50)
c2=circle(20)
c3=c1+c2
print c3
