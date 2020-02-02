class test:
    def __init__(self,na):
        self.nam=na
        print "const",self.nam
    def dis(self):
        print self.nam

ob=test("Degeneration Sarath")
print ob.nam
ob.dis()


