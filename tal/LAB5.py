dite_names={"yarin":25000,"liron":30000,"yaniv":35000,"leah":40000,"ron":45000}
print(dite_names)
summay=dite_names["yarin"]+dite_names["ron"]
print("the summary is: " + str(summay))
dite_names["eli"]=summay
print(dite_names)
print("Number of entires: " + str(len(dite_names)))
print("idan" in dite_names)