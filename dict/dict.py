# -*- coding: utf-8 -*-

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print tel
print tel['jack']

del tel["sape"]
print tel

tel["irv"] = 4127
print tel
print tel.keys()
print 'guido' in tel
print tel.has_key('guido')

# if key not exist, next statement will throw error
# print tel['not_in']

# if key not exist, will get default value
print tel.get('kkk', 0)

# construct
print dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print dict.fromkeys(['a', 'b'], 0)
print dict(zip(['a','b','c'],[1,2,3]))
print zip(['a','b','c'],[1,2,3])
print {k:v for (k,v) in zip(['a','b','c'],[1,2,3])}
print {x: x**2 for x in (2, 4, 6)}
print dict(a=1,b=2,c=3)
print {c:c*4 for c in 'JoinQuant'} #默认是集合
print {c:c*4 for c in ['JoinQuant']}
print {c.lower():c*4+'!' for c in 'JoinQuant'}
