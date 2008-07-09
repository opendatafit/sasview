# class Loader  to load any king of file
import wx
import string,numpy
import logging
class Reader:
    """
        This class is loading values from given file or value giving by the user
    """
    ext=['.txt','.dat']  
    def _init_(self,filename=None,x=None,y=None,dx=None,dy=None):
        # variable to store loaded values
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.filename = filename
        
        
    def read(self,path, format=None):
        """ Store the values loaded from file in local variables 
            can read 3 columns of data
        """
        
        if not path == None:
            read_it = False
            
            for item in self.ext:
                if path.lower().find(item)>=0:
                    read_it = True
            #print "this is the flag",read_it, path.lower()
            if read_it==False:
                return None
            else:
                try:
                    input_f =  open(path,'r')
                except :
                    raise  RuntimeError,"TXT3_Reader cannot open %s"%(path)
                buff = input_f.read()
                lines = buff.split('\n')
                self.x=[]
                self.y=[]
                self.dx = [] 
                self.dy=[]
                for line in lines:
                    toks = line.split()
                    try:  
                        x = float(toks[0])
                        y = float(toks[1]) 
                        dy = float(toks[2])
                       
                        self.x.append(x)
                        self.y.append(y)
                        self.dy.append(dy)
                   
                    except:
                        pass
                        #print "READ ERROR", line
            
                    self.dx = numpy.zeros(len(self.x))
                    # Sanity check
                    if not len(self.x) == len(self.dx):
                        raise ValueError, "x and dx have different length"
                    if not len(self.y) == len(self.dy):
                        raise ValueError, "y and dy have different length"
               
                if (self.x==[] or self.y==[])and (self.dy==[]):
                    raise ValueError, "TXT3_Reader can't read %s"%path
                else:
                    #msg="txtReader  Reading:\n"+"this x :"+ str(self.x) +"\n"+"this y:"+str(self.y)+"\n"+"this dy :"+str(self.dy)+"\n"
                    #return msg
                    logging.info ("TXT3_Reader reading %s \n" %(path))
                    return self.x,self.y,self.dy
                
        return None
if __name__ == "__main__": 
    read= Reader()
    #read= Reader(filename="testdata_line.txt")
    print read.load("test.dat")
    
    
            