from collections import defaultdict

d=defaultdict(lambda:{'admission':0, 'discharge':0})


l={
  'raj':{'admissions':'Y','discharges':'N'},
  'jai':{'admissions':'Y','discharges':'Y'},
  'lik':{'admissions':'Y','discharges':'Y'}
  }

for names,data in l.items():
  
  if data['admissions']=='Y':
    d[names]['admission']+=1
  if data['discharges']=='Y':
    d[names]['discharge']+=1



d=dict(d)
print(d)
print(type(d))





# for k in d.items():
#   if d[k]%2==0:
#     l.appemd(k)
#   else:
