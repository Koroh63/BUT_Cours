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
print('Polonaise :')
Polonaise(d5,a)
print(a)
    
def PolonaiseInverse(d,res):
    if(ArbreNonVide(d)):
        PolonaiseInverse(d['fg'],res)
        PolonaiseInverse(d['fd'],res)
        res.append(d['e'])
    else:
        return

print('PolonaiseInverse : ')
PolonaiseInverse(d5,b)
print(b)
    
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
    Expression(d,tab)
    stack = [] 
    for ele in expression:
        
        # ele is a number
        if ele not in '/*+-':
            stack.append(int(ele))
        
        # ele is an operator
        else:
        # getting operands
            right = stack.pop()
        left = stack.pop()
            
        # performing operation according to operator
        if ele == '+':
            stack.append(left + right)
            
        elif ele == '-':
            stack.append(left - right)
            
        elif ele == '*':
            stack.append(left * right)
            
        elif ele == '/':
            stack.append(int(left / right))
        
    # return final answer.
    return stack.pop()

print(Eval(d5,0))