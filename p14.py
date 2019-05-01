import math as m

def route(n,m_):
    return m.factorial(n+m_)/(m.factorial(n)*m.factorial(m_))

print(route(20,20))