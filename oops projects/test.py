class strr(str):
    def __add__(self, other):
        other=strr(other)
        return super(strr, self).__add__(other)
    # def __str__(self):
    #     return super.__str__(self)

class intt(int):
    def __add__(self, other):
        m = strr(self)
        n = strr(other)
        return super(strr, m).__add__(n)

tmp="{} + {} = {} \n"

a=strr("qww")
b=strr("yyy")
c=a+b
print(tmp.format(a,b,c))

m=intt(2)
n=intt(999)
o=m+n
print(tmp.format(m,n,o))

p=strr("aaa")
q=intt(77)
r=p+q
print(tmp.format(p,q,r))

s=intt(77)
t=strr("aaa")
u=s+t
print(tmp.format(s,t,u))