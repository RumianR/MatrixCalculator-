#Matrix Class

class Matrix(object):
    """ Making a matrix class"""
    
    def __init__(self,rows):
        
        self.rows = rows
        
        self.r = len(rows)
        self.c = len(rows[0])
       
   
    def __repr__(self): 
        """Representing matrix"""

        res = ''
        for row in self.rows:
            s = [str(val)+ ' ' for val in row]
            res = res + ''.join(s)+'\n'
        return res
 
                
    def __mul__(self, other):
        """Multiplication method creation"""
        if self.c == other.r:
            result= initial(self.r,other.c)
            for i in range(self.r):
                           for j in range(other.c):
                               for k in range(other.r):
                                   result[i][j]+= self.rows[i][k] * other.rows[k][j]
            return Matrix(result)

        else:
            print("Unfortunately the matrix sizes are not appropriate, \n{} columns and {} rows."\
                  .format(self.c,other.r))


def identity(n):
    """Identity Matrix Creation Function"""
    res = [[0]*n for i in range(n)]
    for i in range(n):
        res[i][i] = 1
    return Matrix(res)

transpose = lambda mat:[list(x) for x in zip(*mat.rows)] #Transpose Function

                
def initial(r,c): #Table of 0 Function
    b = [[0]*c for x in range(r)]
    return b

if __name__ == "__main__": #5 case scenario test

    print("1. Matrix creation\n")
    m=Matrix([[1,2,3],[3,4,5],[6,7,8]])
    print(m)

    print("2. Matrix Transpose\n")
    print(Matrix(transpose(m)))

    print("3. Creation of Identity Matrix\n")
    print(identity(3))

    print("4. Matrix Multiplication of\n")
    print(m)
    print("     and\n")
    i= identity(3)
    print(i)
    print("-----------------")
    print(m*i)

    print("4. Matrix Multiplication of\n")
    print(m)
    print("     and\n")
    n= [[3,2,1],[6,5,4],[9,8,7]]
    n=Matrix(n)
    print(n)
    print("----------------")
    print(m*n)

    print("5. Matrix Multiplication of\n")
    print(m)
    print("     and\n")
    n= [[6,5,4],[9,8,7]]
    n=Matrix(n)
    print(n)
    print("----------------")
    print(m*n)
            
