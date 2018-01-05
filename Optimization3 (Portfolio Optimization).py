# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 14:30:43 2017

@author: aditya
"""

import MySQLdb as mySQL

db = mySQL.connect(user='root', passwd='root',host='localhost',db='nasdaq')

cur = db.cursor()

cur.execute('select * from corr')

Q = {}

data = [row for row in cur.fetchall()]

for i in range(len(data)):
    Q[int(data[i][0]),int(data[i][1])] = float(data[i][2]) 
    

cur.execute('select * from r')

r = []
mean = [row for row in cur.fetchall()]

for i in range(len(mean)):
    r.append(mean[i][1])
    
l = [0]

for i in range(1,40):
    l.append(l[i-1] + 0.002)

v = []

for i in range(len(l)): 
    port_size = 1.0
    rtrn = l[i]
    
    from gurobipy import *
    m = Model("PorfolioOpt")
    
    m.ModelSense = GRB.MINIMIZE
    m.setParam('TimeLimit',7200)
    
    #Variables
    dvars = []
    for i in range(len(mean)):
        dvars.append(m.addVar(vtype=GRB.CONTINUOUS, name='a'+str(i), lb=0.0))
    m.update()
    
    #constraints
    m.addConstr(quicksum(dvars[i]*r[i] for i in range(len(mean)))/port_size, GRB.GREATER_EQUAL, rtrn,'Returns')
    m.addConstr(quicksum(dvars[i] for i in range(len(mean))), GRB.LESS_EQUAL, port_size,'PortfolioSize')
    
    #Objective
    m.setObjective(quicksum(dvars[i]*Q[(i + 1,j + 1)]*dvars[j] for i in range(len(mean)) for j in range(len(mean))), GRB.MINIMIZE)
    m.update()
    
    m.optimize()
    v.append(m.ObjVal)
    
for i in range(len(l)):
    print l[i], v[i]

for i in range(len(l)):
    cur.execute('insert into portfolio values (%s,%s)',(l[i],v[i]))

db.commit()

