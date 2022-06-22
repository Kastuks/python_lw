import numpy as np
import sympy
import matplotlib

# 1.	Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis.

interval1 = [-1.3, 2.5]
split_num = 64

def split_interval(interval, n):
    list = []
    for i in range(n):
        list.append((interval[1] - interval[0]) / (n-1) * (i ) + interval[0])
    return list

def split_interval_numpy(interval, n):
    list = np.linspace(interval[0], interval[1], num=n)
    return list

d = split_interval(interval1, split_num)
# print(d)

b = split_interval_numpy(interval1, split_num)
# print(b)

# 2.	Sukonstruokite pasikartojantį masyvą pagal duotą N.
# Duotas masyvas [1, 2, 3, 4] ir N = 3
# Rezultatas [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# Masyvas gali būti bet kokio dydžio ir atsitiktinai sugeneruojamas.


given_arr = [1, 2, 3, 4]
N = 3

def rep_array(arr, n):
    return np.tile(arr, n)
    
answer = rep_array(given_arr, N)
print(answer)


# 3.	Sukurkite masyvą iš pasikartojančių elementų.
# Duotas skaičius 3 ir pasikartojimų skaičius 4.
# Rezultatas [3, 3, 3, 3]

element = 3
N = 4

def rep_elem(elem, n):
    return np.repeat(elem, n)
    
answer = rep_elem(element, N)
print(answer)

# 4.	Sukurkite masyvą dydžio 10 x 10 iš nulių "įrėmintų" vienetais.
# Užuomina - pad.

arr = np.zeros((8,8))
arr = np.pad(arr, (1,1), mode='constant', constant_values=(1, 1))
print(arr)

# 5.	Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka.

# x = np.ones((3,3))
x = np.zeros((8,8),dtype=int)
# print(x)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)

# 6.	Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j.

def create_arr(n):
    x = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            x[i][j] = i+j
    return x        


b = create_arr(5)
print(b)

# 7.	Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5). 
# Surūšiuokite eilutes pagal antrąjį stulpelį. 
# Užuominos - slicing, argsort, indexing.

x = np.random.rand(5, 5)
print("Before sorting")
print(x)

a = np.argsort(x[1][:])
# print(a)

y = []

for i in range(len(x)):
    nums = [x[i][j] for j in a]
    y.append(nums)
    
print("After sorting")
for a in y:
    print(a)
# print(y)

# 8.	Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių.
from numpy.linalg import eig

a = np.array([[0, 2], 
              [2, 3]])
w,v=eig(a)
print('E-value:', w)
print('E-vector', v)

a = np.array([[2, 2, 4], 
              [1, 3, 5],
              [2, 3, 4]])
w,v=eig(a)
print('E-value:', w)
print('E-vector', v)


# Eigenvalues
# Eigenvectors

# 9.	Apskaičiuokite funkcijos 0.5*x**2 + 5 * x + 4 išvestines su numpy ir sympy paketais.
# Užuominos - poly1d, deriv, diff

from sympy import *

x = Symbol('x')

f = 0.5*x**2+5*x+4
f_prime = f.diff(x)

print("Funkcija: ", f)

print("Funkcijos isvestine: ", f_prime)

# 10.	Apskaičiuokite funkcijos e-x apibrėžtinį, intervale [0,1], ir neapibrėžtinį integralus.

fun = exp(x)

integrate_nobounds = integrate(fun, x)
integrate_withbounds = integrate(fun, (x, 0, 1))

print("Neapibreztinis integralas: ", integrate_nobounds)
print("Apibreztinis integralas: ", integrate_withbounds)


# 11.	Pasinaudodami polinėmis koordinatėmis nupieškite kardioidę.

from matplotlib import pyplot as plt

theta = np.linspace(0, 2*np.pi, 1000)

r = 5 - 5 * np.sin(theta)

plt.polar(theta, r, 'r')
plt.show()

# 12.	Sugeneruokite masyvą iš 1000 atsitiktinių skaičių, pasiskirsčiusių pagal normalųjį dėsnį su duotais vidurkiu V ir dispersija D. Nupieškite jų histogramą.

V = 2
D = 5

s = np.random.normal(V, D, 1000)
# print(s)

count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(D * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - V)**2 / (2 * D**2) ),
         linewidth=2, color='r')
plt.show()
