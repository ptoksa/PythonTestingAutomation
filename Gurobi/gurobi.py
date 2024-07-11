import gurobipy as gp
from gurobipy import GRB

# Create a new model
model = gp.Model("factory")

# Create variables
x1 = model.addVar(vtype=GRB.CONTINUOUS, name="x1")
x2 = model.addVar(vtype=GRB.CONTINUOUS, name="x2")

# Set objective
model.setObjective(5*x1 + 4*x2, GRB.MAXIMIZE)

# Add constraints
model.addConstr(2*x1 + 3*x2 <= 8, "c0")
model.addConstr(x1 + 2*x2 <= 6, "c1")

# Optimize model
model.optimize()

# Print the solution
for v in model.getVars():
    print(f'{v.varName} {v.x}')

print(f'Obj: {model.objVal}')
