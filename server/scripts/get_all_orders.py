import time
import numpy as np

# only keep the relevant columns from the master df 
commands = df_Phenix[["CO_DateCommande","EC_Id","RC_Id","CP_QuantiteTotale","CP_QuantiteUnite","P_food_group","Qty_val","Qty_unit"]].copy()

# convert column to relevant data type
print('----> cleaning data type ---->') 
start = time.clock()
commands["CO_DateCommande"]=pd.to_datetime(commands["CO_DateCommande"])
commands["EC_Id"]=commands["EC_Id"].astype(int)
commands["RC_Id"]=commands["RC_Id"].astype(int)
end = time.clock()
print('processing time: ',round(end - start),' seconds')

#add command total quantity in grams
print('----> adding quantities ---->')
start = time.clock()
commands['Qty_totale'] = np.where(np.isin(commands['CP_QuantiteUnite'],['Kg','kg','Kilo','Litre','Litres']), commands['CP_QuantiteTotale'] * 1000, np.where(np.logical_and(np.isin(commands['CP_QuantiteUnite'],['Unités','Unité','unité','unités','pièces','Pcs']),np.isin(commands['Qty_unit'],['g'])),commands['Qty_val'] * commands['CP_QuantiteTotale'],float('nan')))
end = time.clock()
print('processing time: ',round(end - start),' seconds')

#aggregate df at day x EC x RC x food group level & drop line without quantity in grams
print('----> group by ---->')
start = time.clock()
commands_agg = commands.groupby([pd.Grouper(key='CO_DateCommande', freq='D'),"EC_Id","RC_Id","P_food_group"]).agg({"Qty_totale":"sum"}).dropna().reset_index().set_index(["CO_DateCommande","EC_Id","RC_Id"])
end = time.clock()
print('processing time: ',round(end - start),' seconds')

#create a df with food groups and ids & replacing food groups in main df by ids
print('----> food group dictionnary ---->')
start = time.clock()
food_groups = commands_agg.reset_index()["P_food_group"].drop_duplicates().reset_index(drop=True)
food_groups_dict = dict(enumerate(food_groups.tolist()))
food_groups_inv = {v: k for k, v in food_groups_dict.items()}
commands_id = commands_agg.replace(to_replace={'P_food_group':food_groups_inv.astype(int)})
end = time.clock()
print('processing time: ',round(end - start),' seconds')

#aggregate df at day x EC x RC level by merging food groups and quantity into a list
print('----> to list ---->')
start = time.clock()
commands_list = commands_id.groupby(["CO_DateCommande","EC_Id","RC_Id"]).apply(lambda x: x[["P_food_group","Qty_totale"]].values.tolist()).reset_index()
end = time.clock()
print('processing time: ',round(end - start),' seconds')

#rename columns
commands_list.rename(columns={"CO_DateCommande":"date","EC_Id":"ec_id","RC_Id":"rc_id",0:"details"},inplace=True)

#save df to json
with open('./json/commands.json','w',encoding = "utf-8") as file:
    commands_list.to_json(file,'records',force_ascii=False)

with open('./json/foodgroups.json','w',encoding = "utf-8") as file:
    food_groups.to_json(file,force_ascii=False)