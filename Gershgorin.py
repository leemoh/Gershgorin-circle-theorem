import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
def is_square(x):
    cols = len(x)
    for row in x:
        if len(row) != cols:
            return False
    return True
class Matrix:
    def __init__(self,x):
        self.x = x
   

    def __str__(self):
        enter = ""
        for i in self.x:
            for j in i:
                enter += str(j).rjust(4)
            enter +="\n"
        return enter
        
    
    def Gershgorin(self):
        if is_square(self.x)!=True:
            print('Please enter a square matrix')
            return []
        else:
            
            row_sum=[]
            list_diagonals=[]
            list_diagonals.append(np.array(self.x).diagonal())
            self.x=np.absolute(self.x)
        
            row_sum.append(np.array(self.x).sum(axis=1)- np.array(self.x).diagonal())
            y,z=row_sum, list_diagonals
            z= np.array(z).tolist()
            y= np.array(y).tolist()
            circles=list(map(list,zip(z[0],y[0])))
            index,radi = zip(*circles)
  
            Xupper = max(index) + np.std(index)
            Xlower = min(index) - np.std(index)
            Ylimit = max(radi) + np.std(index)
            fig, ax = plt.subplots()
           
            ax = plt.gca()
            
            ax.cla()
            ax.set_xlim((Xlower,Xupper))
            ax.set_ylim((-Ylimit,Ylimit))
            plt.xlabel('Real Axis')
            plt.ylabel('Imaginary Axis')
            plt.title('Gershgorin circles')
            for x in range(0,len(circles)):
               
                circ = plt.Circle((index[x],0), radius = radi[x])
                ax.add_artist(circ)
              
            ax.plot([Xlower,Xupper],[0,0],'k--')
            ax.plot([0,0],[-Ylimit,Ylimit],'k--')
            ax.yaxis.grid(True, linestyle="--")
            ax.xaxis.grid(True, linestyle="--")
            for i in index:
           
                plt.axvline(x=i, linestyle='--', color='r') # vertical lines

          
            
            plt.show()
     