import matplotlib.pyplot as plt


from mako.template import Template # pip install Mako

import PySpice.Logging.Logging as Logging

from MySpice import MySpice as spice
import random

#logger = Logging.setup_logging()
znac = []
f = open('C_3','r')
for line in f:
 znac.append(line)

template = Template('C1 0 input  ${resistance}\n')
f.close()

v = 1000
Vm = 12
R = 500
for i in range(1):
    context = {'resistance':(1/(500*v))*10**random.uniform(-2.5, 1)}
    znac[3] = template.render(**context)
    with open("C_3", "w") as file:
      print(*znac, file=file, sep ='')
    circuit = spice.LoadFile('C_3')
    input_data = spice.Init_Data(v, Vm, R)
    analysis = spice.CreateCVC1(circuit, input_data, 100, name="input", Vmax=Vm, Imax=Vm/500, cycle=10)
    template1 = Template('C${ name }.txt')
    spice.SaveFile(analysis, template1.render(name=i+1))
    
    with open(template1.render(name=i+1)) as file:
      line = file.readlines()
      x = line[0].split(sep = ";")
      X = list(map(float,x))
      y = line[2].split(sep = ";")
      Y = list(map(float,y))
 
      length = len(X)
      shift = random.randrange(1, length, 1)
      X = X[-shift:] + X[:-shift]
      Y = Y[-shift:] + Y[:-shift]
   
    with open(template1.render(name=i+1), "w") as file:
      print(*X, file=file,sep=';',end='\n\n')
      print(*Y, file=file,sep=';')
      
      
  
