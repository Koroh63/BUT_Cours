# Exercice 1 :
# Les noeuds sont a, b ou c et les feuilles les chiffres, les feuilles sont aussi des noeuds
# Les sous-arbres sont tous les noeuds venant de la droite pour les arbres gauches et inversement.
# Exercice 2 : 
#
# Question 1 : 
#
#     --4
#  --_
#     --3
# 5
#     --2
#  --_
#     --1

d1={}

d2={
    'e': 6,
    'fg': {},
    'fd': {}
}

d3={
    'e': 5,
    'fg': {'e': None,
        'fg': {'e': 1,
            'fg': {},
            'fd': {}},
        'fd': {'e': 2,
            'fg': {},
            'fd': {}}},
    'fd': {'e': None,
        'fg': {'e': 3,
            'fg': {},
            'fd': {}},
        'fd': {'e': 4,
            'fg': {},
            'fd': {}}}
}



d4 = {
    'e': 'a',
    'fg': {
        'e': 'b',
        'fg': {},
        'fd':{
            'e':2,
            'fg':{},
            'fd':{}
        }

    },
    'fd':{
        'e':'c',
        'fg':{
            'e':3,
            'fg':{
                'e':'d',
                'fg':{},
                'fd':{}
            },
            'fd':{}

        },
        'fd':{
            'e':4,
            'fg':{},
            'fd':{}
        }
        

    }
}

def ArbreNonVide(d):
    if(d=={}):
        return False
    else:
        return True
    
def Racine(d):
    if(ArbreNonVide(d)):
        return d['e']
    else:
        return None
    
def SousArbreGauche(d):
    if(ArbreNonVide(d)):
        return d['fg']
    else:
        return None
    
def SousArbreDroit(d):
    if(ArbreNonVide(d)):
        return d['fd']
    else:
        return None
    
def Feuille(d):
    if(ArbreNonVide(d) and d['fg'] == {} and d['fd']=={}):
        return True
    else:
        return False

# print('test arbre non vide avec d1 : ',ArbreNonVide(d1))
# print('test arbre non vide avec d2 : ',ArbreNonVide(d2))

# print('test racine avec d1 : ',Racine(d1))
# print('test racine avec d2 : ',Racine(d2))

# print('test arbre droit avec d3 : ',SousArbreDroit(d3))
# print('test arbre droit avec d4 : ',SousArbreDroit(d4))

# print('test arbre gauche avec d3 : ',SousArbreGauche(d3))
# print('test arbre gauche avec d4 : ',SousArbreGauche(d4))

# print('test feuille sur d1 : ',Feuille(d1))
# print('test feuille sur d2 : ',Feuille(d2))

def Prefixe(d):
    if(ArbreNonVide(d)):
        print(d['e'])
        Prefixe(d['fg'])
        Prefixe(d['fd'])
    else:
        return
    
def Infixe(d):
    if(ArbreNonVide(d)):
        Infixe(d['fg'])
        print(d['e'])
        Infixe(d['fd'])
    else:
        return
    
def Postfixe(d):
    if(ArbreNonVide(d)):
        Postfixe(d['fg'])
        Postfixe(d['fd'])
        print(d['e'])
    else:
        return

# print('Préfix : ')
# Prefixe(d4)
# print('Infix : ')
# Infixe(d4)
# print('Postfix : ')
# Postfixe(d4)

d5={
    'e':'-',
    'fg':{
        'e':'*',
        'fg':{
            'e':'4',
            'fg':{},
            'fd':{}
        },
        'fd':{
            'e':'+',
            'fg':{
                'e':'1',
                'fg':{},
                'fd':{}
            },
            'fd':{
                'e':'2',
                'fg':{},
                'fd':{}
            }
        }
    },
    'fd':{
        'e':'3',
        'fg':{},
        'fd':{}
    }
}

a = []
b = []
c = []

def Polonaise(d,res):
    if(ArbreNonVide(d)):
        res.append(d['e'])
        Polonaise(d['fg'],res)
        Polonaise(d['fd'],res)
    else:
        return
# print('Polonaise :')
# Polonaise(d5,a)
# print(a)
    
def PolonaiseInverse(d,res):
    if(ArbreNonVide(d)):
        PolonaiseInverse(d['fg'],res)
        PolonaiseInverse(d['fd'],res)
        res.append(d['e'])
    else:
        return

# print('PolonaiseInverse : ')
# PolonaiseInverse(d5,b)
# print(b)
    
def Expression(d,res):
    if(ArbreNonVide(d)):
        if(d['e']=='-' or d['e']=='+'):
            res.append('(')
        Expression(d['fg'],res)
        res.append(d['e'])

        Expression(d['fd'],res)
        if(d['e']=='-' or d['e']=='+'):
            res.append(')')
    else:
        return
    
# print('Expression : ')
# Expression(d5,c)
# print(c)

# print('Préfix : ')
# Prefixe(d5)
# print('Infix : ')
# Infixe(d5)
# print('Postfix : ')
# Postfixe(d5)
    
def Eval(d,res):
    tab = []
    Polonaise(d,tab)
    stack = [] 
    for ele in tab:
        
        
        if ele not in '/*+-':
            stack.append(int(ele))
        
        
        else:
       
            right = stack.pop()
        left = stack.pop()
            
        
        if ele == '+':
            stack.append(left + right)
            
        elif ele == '-':
            stack.append(left - right)
            
        elif ele == '*':
            stack.append(left * right)
            
        elif ele == '/':
            stack.append(int(left / right))
        
    
    return stack.pop()

#print(Eval(d5,0))
d6={
    'e':15,
    'fg':{
        'e':6,
        'fg':{
            'e':3,
            'fg':{
                'e':2,
                'fg':{},
                'fd':{}
            },
            'fd':{
                'e':4,
                'fg':{},
                'fd':{}
            }
        },
        'fd':{
            'e':7,
            'fg':{},
            'fd':{
                'e':13,
                'fg':{
                    'e':9,
                    'fg':{},
                    'fd':{}
                },
                'fd':{}
            }
        }
    },
    'fd':{
        'e':18,
        'fg':{
            'e':17,
            'fg':{},
            'fd':{}
        },
        'fd':{
            'e':20,
            'fg':{},
            'fd':{}
        }
    }
}

def Rechercher(d,x):
    if(ArbreNonVide(d)):
        if(d['e']==x):
            return True
        elif(Feuille(d)):
            return False
        elif(d['e']>x):
            return Rechercher(d['fg'],x)
        else : 
            return Rechercher(d['fd'],x)
    else:
        return False
            

# print(Rechercher(d1,1))
# print(Rechercher(d2,1))
# print(Rechercher(d2,6))
# print(Rechercher(d6,13))
# print(Rechercher(d6,17))
# print(Rechercher(d6,40))

def Min(d):
    if(ArbreNonVide(d)):
        if(Feuille(d) or d['fg']=={}):
            return d['e']
        else:
            return Min(d['fg']) 
    else : 
        return

# print(Min(d1))
# print(Min(d2))
# print(Min(d6))

def Max(d):
    if(ArbreNonVide(d)):
        if(Feuille(d) or d['fd']=={}):
            return d['e']
        else:
            return Max(d['fd']) 
    else : 
        return

# print(Max(d1))
# print(Max(d2))
# print(Max(d6))



# Postfixe(d6)
# Prefixe(d6)
# Infixe(d6)

def Afficher(d,res):
    if(ArbreNonVide(d)):
        Afficher(d['fg'],res)
        res.append(d['e'])
        Afficher(d['fd'],res)
    else:
        return


def Inserer(d,x):
    if(ArbreNonVide(d)):
        if(d['e']>x):
            return Inserer(d['fg'],x)
        elif (d['e']<x):
            return Inserer(d['fd'],x)
        else : 
            return
    else : 
        d.update({
            'e': x,
            'fg': {},
            'fd': {}
        })
# Inserer(d6,10)

    
L1=[5,1,8,0,9,6,-1,25,11]

# L1.sort()

# for i in L1:
#     Inserer(d1,i)

tab = []
# print(d1)
# print(tab)

def Construire(L):
    d = {}
    for i in L:
        Inserer(d,i)
    
    return d

dh = Construire(L1)


Afficher(dh,tab)

print(tab)