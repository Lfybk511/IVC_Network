import matplotlib.pyplot as plt

from mako.template import Template # pip install Mako

import PySpice.Logging.Logging as Logging
from string import Template
from MySpice import MySpice as spice
import random
import os
import glob

Text = []
#CR
Text.append("""* Qucs 0.0.21 
.INCLUDE "C:/Program Files (x86)/Qucs-S/share/qucs-s/xspice_cmlib/include/ngspice_mathfunc.inc"
* Qucs 0.0.21  
C1 _net0 0  $capacity1
R1 input _net0 $resistance1 
.control
echo "" > spice4qucs.cir.noise
echo "" > spice4qucs.cir.pz
exit
.endc
.END
""")
#CR1
Text.append("""* Qucs 0.0.21 
.INCLUDE "C:/Program Files (x86)/Qucs-S/share/qucs-s/xspice_cmlib/include/ngspice_mathfunc.inc"
* Qucs 0.0.21  
C1 0 input  $capacity1 
R1 0 input $resistance1 
.control
echo "" > spice4qucs.cir.noise
echo "" > spice4qucs.cir.pz
exit
.endc
.END
""")
#D
Text.append("""* Qucs 0.0.21 
.INCLUDE "C:/Program Files (x86)/Qucs-S/share/qucs-s/xspice_cmlib/include/ngspice_mathfunc.inc"
* Qucs 0.0.21  
D_1N4148_1 input 0 DMOD_D_1N4148_1 AREA=1.0 Temp=26.85
.MODEL DMOD_D_BAV756DW_1 D (Is=4.92e-08 N=2.34 Cj0=2.65e-12 M=0.333 Vj=$opening_voltage1 Fc=0.5 Rs=0.141 Tt=5.76e-09 Ikf=0 Kf=0 Af=1 Bv=7 Ibv=2.5e-06 Xti=3 Eg=1000.11 Tcv=0 Trs=0 Ttt1=0 Ttt2=0 Tm1=0 Tm2=0 Tnom=26.85 )
.control
echo "" > spice4qucs.cir.noise
echo "" > spice4qucs.cir.pz
exit
.endc
.END
""")
#DD
Text.append("""* Qucs 0.0.21 
.INCLUDE "C:/Program Files (x86)/Qucs-S/share/qucs-s/xspice_cmlib/include/ngspice_mathfunc.inc"
* Qucs 0.0.21  
D_BAV756DW_1 input 0 DMOD_D_BAV756DW_1 AREA=1.0 Temp=26.85
.MODEL DMOD_D_BAV756DW_1 D (Is=4.92e-08 N=2.34 Cj0=2.65e-12 M=0.333 Vj=$opening_voltage1 Fc=0.5 Rs=0.141 Tt=5.76e-09 Ikf=0 Kf=0 Af=1 Bv=75 Ibv=2.5e-06 Xti=3 Eg=1.11 Tcv=0 Trs=0 Ttt1=0 Ttt2=0 Tm1=0 Tm2=0 Tnom=26.85 )
D_BAV756DW_2 0 input DMOD_D_BAV756DW_2 AREA=1.0 Temp=26.85
.MODEL DMOD_D_BAV756DW_2 D (Is=4.92e-8 N=2.34 Cj0=2.65e-12 M=0.333 Vj=$opening_voltage2 Fc=0.5 Rs=0.141 Tt=5.76e-09 Ikf=0 Kf=0 Af=1 Bv=75 Ibv=2.5e-06 Xti=3 Eg=1.11 Tcv=0 Trs=0 Ttt1=0 Ttt2=0 Tm1=0 Tm2=0 Tnom=26.85 )
.control
echo "" > spice4qucs.cir.noise
echo "" > spice4qucs.cir.pz
exit
.endc
.END
""")
#DDC
Text.append("""* Qucs 0.0.21 
.INCLUDE "C:/Program Files (x86)/Qucs-S/share/qucs-s/xspice_cmlib/include/ngspice_mathfunc.inc"
* Qucs 0.0.21  
D_BAV756DW_1 input 0 DMOD_D_BAV756DW_1 AREA=1.0 Temp=26.85
.MODEL DMOD_D_BAV756DW_1 D (Is=4.92e-08 N=2.34 Cj0=2.65e-12 M=0.333 Vj=$opening_voltage1 Fc=0.5 Rs=0.141 Tt=5.76e-09 Ikf=0 Kf=0 Af=1 Bv=75 Ibv=2.5e-06 Xti=3 Eg=1000.11 Tcv=0 Trs=0 Ttt1=0 Ttt2=0 Tm1=0 Tm2=0 Tnom=26.85 )
D_BAV756DW_2 0 input DMOD_D_BAV756DW_2 AREA=1.0 Temp=26.85
.MODEL DMOD_D_BAV756DW_2 D (Is=4.92e-08 N=2.34 Cj0=2.65e-12 M=0.333 Vj=$opening_voltage1 Fc=0.5 Rs=0.141 Tt=5.76e-09 Ikf=0 Kf=0 Af=1 Bv=75 Ibv=2.5e-06 Xti=3 Eg=1000.11 Tcv=0 Trs=0 Ttt1=0 Ttt2=0 Tm1=0 Tm2=0 Tnom=26.85 )
C1 0 input  $capacity1
.control
echo "" > spice4qucs.cir.noise
echo "" > spice4qucs.cir.pz
exit
.endc
.END
""")
#R
Text.append("""* Qucs 0.0.21 
.INCLUDE "C:/Program Files (x86)/Qucs-S/share/qucs-s/xspice_cmlib/include/ngspice_mathfunc.inc"
* Qucs 0.0.21  
R1 0  input $resistance1
echo "" > spice4qucs.cir.noise
echo "" > spice4qucs.cir.pz
exit
.endc
.END
""")

def dataset(v, Vm, R, MyList,vid,k0,j0,l0):
    for i in range(len(Classes)):
        l = -1
        for k in range(k0):
            resistance1 = 500 * 10 ** random.uniform(-1, 1)
            resistance2 = 1
            capacity1 = (1 / (500 * v)) * 10 ** random.uniform(-2, 1)
            capacity2 = 1
            opening_voltage1 = random.uniform(0, 2)
            opening_voltage2 = random.uniform(0, 2)
            parameters = [resistance1, capacity1, opening_voltage1, opening_voltage2]
            #name_prog = str(dir + '\' + Classis[i][0] +'\'+ name_file'\')
            template_string = Template(Text[i])
            prepared_string = template_string.substitute(resistance1=resistance1, resistance2=resistance2,
                                                         capacity1=capacity1, capacity2=capacity2,
                                                         opening_voltage1=opening_voltage1, opening_voltage2=opening_voltage2)
            #print(MyList[i])
            with open(MyList[i], "w") as file:
                file.write(prepared_string)
            for j in range(j0):
                print(Classes[i][0])
                l = -1
                circuit = spice.LoadFile(MyList[i])
                input_data = spice.Init_Data(v, Vm, R)
                analysis = spice.CreateCVC1(circuit, input_data, 100, name="input", Vmax=Vm, Imax=Vm / R, cycle=100)
                template1 = Template('main_dir/'+ vid +'/$cl/${cl}_${name}_${name1}_${name2}.txt')
                #print('cchjsdjgc')
                #print(template1.substitute(cl=Classes[i][0], name1=j + 1, name=k+1,  name2=j1+1))
                spice.SaveFile(analysis, template1.substitute(cl=Classes[i][0], name1=j + 1, name=k+1,  name2=l+1))
                with open(template1.substitute(cl=Classes[i][0], name1=j + 1, name=k+1,  name2=l+1), "a") as file:
                    print(*parameters, file=file, sep=';')
                    #print(*Y, file=file, sep=';')
            for l in range(l0):
                with open(template1.substitute(cl=Classes[i][0], name1=j + 1, name=k+1,  name2=0)) as file:
                    line = file.readlines()
                    x = line[0].split(sep=";")
                    X = list(map(float, x))
                    y = line[2].split(sep=";")
                    Y = list(map(float, y))

                    length = len(X)
                    shift = random.randrange(1, length, 1)
                    X = X[-shift:] + X[:-shift]
                    Y = Y[-shift:] + Y[:-shift]

                with open(template1.substitute(cl=Classes[i][0], name1=j + 1, name=k+1,  name2=l+1), "w") as file:
                    print(*X, file=file, sep=';', end='\n\n')
                    print(*Y, file=file, sep=';', end='\n\n')
                    print(*parameters, file=file, sep=';')
    for i in range(len(Classes)):
        #print(MyList[i])
        if os.path.isfile(MyList[i]):
            os.remove(MyList[i])
            print("success")
        else:
            print("File doesn't exists!")

V = 1000
VM = 12
r = 500
name_file = 'prog.txt'
dir_train = "C:/Users/danil/OneDrive/Рабочий стол/Сеть/IVC_Network/main_dir/train/*"
dir_val = "C:/Users/danil/OneDrive/Рабочий стол/Сеть/IVC_Network/main_dir/val/*"
Classes = [['CR'],["CR1"],["D"],["DD"],["DDC"],["R"]]
for i in range(len(Classes)):
  filename = 'main_dir/train/' + Classes[i][0] + '/prog.txt'
  if not os.path.exists(os.path.dirname(filename)):
      dir_name = os.path.dirname(filename)
      os.makedirs(dir_name)
      with open(filename, "w") as f:
          f.write(Text[i])
  filename = 'main_dir/val/' + Classes[i][0] + '/prog.txt'
  if not os.path.exists(os.path.dirname(filename)):
      dir_name = os.path.dirname(filename)
      os.makedirs(dir_name)
      with open(filename, "w") as f:
          f.write(Text[i])

MyList_train = glob.glob(dir_train + "/*")
MyList_val = glob.glob(dir_val + "/*")

print(MyList_train)

dataset(v=V, Vm=VM, R=r, MyList=MyList_train, vid='train', k0=200, j0=5, l0=5,)
dataset(v=V, Vm=VM, R=r, MyList=MyList_val, vid='val', k0=30, j0=5, l0=5,)

#logger = Logging.setup_logging()
#
# znac = []
# f = open(name_file,'r')
# for line in f:
#  znac.append(line)
#
# templateR1 = Template('R1 0 input ${resistance} \n')
# templateC1 = Template('C1 0 input  ${resistance} \n')
# f.close()

# for i in range(1):
#     context = {'resistance': (1 / (500 * v)) * 10 ** random.uniform(3.6, 6)}
#     znac[3] = templateC1.render(**context)
#     context = {'resistance': (1 / ( 500 )) * 10 ** random.uniform(-1, 1)}
#     znac[4] = templateR1.render(**context)
#
#     with open(name_file, "w") as file:
#       print(*znac, file=file, sep ='')
#     circuit = spice.LoadFile(name_file)
#     input_data = spice.Init_Data(v, Vm, R)
#     analysis = spice.CreateCVC2(circuit, input_data, 100, name="input", Vmax=Vm, Imax=Vm/R, cycle=100)
#     template1 = Template('CR1${ name }.txt')
#     spice.SaveFile(analysis, template1.render(name=i+1))
#
#     with open(template1.render(name=i+1)) as file:
#       line = file.readlines()
#       x = line[0].split(sep = ";")
#       X = list(map(float,x))
#       y = line[2].split(sep = ";")
#       Y = list(map(float,y))
#
#       length = len(X)
#       shift = random.randrange(1, length, 1)
#       X = X[-shift:] + X[:-shift]
#       Y = Y[-shift:] + Y[:-shift]
#
#     with open(template1.render(name=i+1), "w") as file:
#       print(*X, file=file,sep=';',end='\n\n')
#       print(*Y, file=file,sep=';')
      
      