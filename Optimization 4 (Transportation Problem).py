# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:27:13 2017

@author: adity
"""

import MySQLdb as mySQL
db = mySQL.connect(user=, passwd=,host=,db='opt')
cur = db.cursor()

cur.execute('select * from mileage')
data = {}
x = [row for row in cur.fetchall()]
for i in range(len(x)):
    data[int(x[i][0]),int(x[i][1])] = float(x[i][2]) 
    
cur.execute('select * from store')
dem = []
req = [row for row in cur.fetchall()]
for i in range(len(req)):
    dem.append(int(req[i][1]))

cur.execute('select * from dc')
cap = []
capacity = [row for row in cur.fetchall()]
for i in range(len(capacity)):
    cap.append(int(capacity[i][1]))
    
    
from gurobipy import *
m = Model("Prototype")

m.ModelSense = GRB.MINIMIZE
m.setParam('TimeLimit',7200)

#Variables
dvars = {}
for i in range(len(cap)):
    for j in range(len(dem)):
        dvars[(i,j)] = m.addVar(vtype=GRB.BINARY, name='dc'+str(i)+',store'+str(j), lb=0.0)
m.update()

#constraints
for i in range(len(cap)):
  m.addConstr(quicksum(dvars[(i,j)]*dem[j] for j in range(len(dem))),GRB.LESS_EQUAL, cap[i],'dc_capacity')
  
for j in range(len(dem)):
  m.addConstr(quicksum(dvars[(i,j)]*dem[j] for i in range(len(cap))),GRB.EQUAL, dem[j],'store_demand')
  

#Objective
m.setObjective(sum(dem)*200 + quicksum(data[(i,j)]*dvars[(i,j)]*dem[j] for i in range(len(cap)) for j in range(len(dem)))*1.5, GRB.MINIMIZE)
m.update()

m.optimize()
m.ObjVal

out = []
for i in range(len(cap)):
    for j in range(len(dem)):
        if dvars[(i,j)].x > 0:
            out.append([i,j])

for i in range(len(out)):
    cur.execute('insert into results values (%s,%s)',(out[i][0],out[i][1]))

db.commit()
        