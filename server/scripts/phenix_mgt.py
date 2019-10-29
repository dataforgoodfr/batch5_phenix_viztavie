#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Preparing Phenix data for visualisation
'''

__author__ = 'Thierry HA'
__license__ = 'MIT License'
__version__ = '0.1'
__maintainer__ = 'Thierry HA'
__status__ = 'Development'

import pandas as pd

def extract_Phenix_SQLtable2CSV(path='./Phenix_DB/'):
    """
    Save all Phenix SQL tables into raw CSV files
    Args:
        path (str): folder path where the csv will be saved
    Returns:
        done (bool): True if no errors
    """
    import pyodbc
    import pandas as pd
    con = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}',server = 'localhost\SQLEXPRESS' , database = 'PHX_D4G')
    
    lst_table = ['CategorieProduits',
                'CommandeProduits',
                'Commandes',
                'Comptes',
                'OffreProduits',
                'Offres',
                'Produits']
    
    for str_table in lst_table:
        data = pd.read_sql('select * from ' + str_table,con)
        data.to_csv(path+str_table+'.csv',sep='\t',encoding='utf-8')
        print(str_table + ' >> Done')
        
    return True

def get_CategorieProduits(path, prefix='CatP_', cleaned=False):
    """
    Read CSV (CategorieProduits) into Dataframe. All relevant columns are kept and renamed with prefix.
    Args:
        path (str): file path to CategorieProduits.csv
        prefix (str): All relevant columns are renamed with prefix
    Returns:
        df (Dataframe): Resulting dataframe
    """
    col = {'Id':prefix+'Id',
           'Compte_Id':'Compte_Id',
           'IsAlimentaire':prefix+'IsAlimentaire',
           'IsDangereux':prefix+'IsDangereux',
           'IsFresh':prefix+'IsFresh',
           'IsFrozen':prefix+'IsFrozen',
           'IsPerishable':prefix+'IsPerishable',
           'Nom':prefix+'Nom',
           'Descriptif':prefix+'Desc'}
    dt = {'Id': 'int64',
          'Compte_Id': 'float64',
          'IsAlimentaire': 'bool',
          'IsDangereux': 'bool',
          'IsFresh': 'bool',
          'IsFrozen': 'bool',
          'IsPerishable': 'bool',
          'Nom': 'object',
          'Descriptif': 'object'}
    if not cleaned:
        df = pd.read_csv(path, sep='\t', encoding='utf-8', usecols=list(col.keys()), dtype=dt)
        df = df.rename(index=str, columns=col)
    else:
        df = pd.read_csv(path, sep='\t', encoding='utf-8',index_col=0)
    return df

def get_CommandeProduits(path, prefix='CP_',cleaned=False):
    """
    Read CSV (CommandeProduits) into Dataframe. All relevant columns are kept and renamed with prefix.
    Args:
        path (str): file path to CommandeProduits.csv
        prefix (str): All relevant columns are renamed with prefix
    Returns:
        df (Dataframe): Resulting dataframe
    """
    col = {'Id':prefix+'Id',
           'Commande_Id':'Commande_Id',
           'OffreProduit_Id':'OffreProduit_Id',
           'QuantiteTotale':prefix+'QuantiteTotale',
           'QuantiteUnite':prefix+'QuantiteUnite',
           'QuantiteValeur':prefix+'QuantiteValeur',
           'MontantTotal':prefix+'MontantTotal',
           'Weight':prefix+'Weight'}
    dt = {'Id': 'int64',
          'Commande_Id': 'int64',
          'OffreProduit_Id':'int64',
          'QuantiteTotale':'float64',
          'QuantiteUnite':'object',
          'QuantiteValeur':'float64',
          'MontantTotal':'float64',
          'Weight':'float64'}
    if not cleaned:
        df = pd.read_csv(path, sep='\t', encoding='utf-8', usecols=list(col.keys()), dtype=dt)
        df = df.rename(index=str, columns=col)
    else:
        df = pd.read_csv(path, sep='\t', encoding='utf-8',index_col=0)
    return df

def get_Commandes(path, prefix = 'CO_', cleaned=False):
    """
    Read CSV (Commandes) into Dataframe. All relevant columns are kept and renamed with prefix.
    Args:
        path (str): file path to Commandes.csv
        prefix (str): All relevant columns are renamed with prefix
    Returns:
        df (Dataframe): Resulting dataframe
    """
    col = {'Id':prefix+'Id',
           'DateCommande':prefix+'DateCommande',
           'EstReceptionne':prefix+'EstReceptionne',
           'Statut':prefix+'Statut',
           'Offre_Id':'Offre_Id',
           'Recepteur_Id':'Recepteur_Id'}
    dt = {'Id':'int64',
           'DateCommande':'object',
           'EstReceptionne':'bool',
           'Statut':'int64',
           'Offre_Id':'int64',
           'Recepteur_Id':'int64'}
    if not cleaned:
        date = ['DateCommande']
        df = pd.read_csv(path, sep='\t', encoding='utf-8', usecols=list(col.keys()), dtype=dt, parse_dates=date)
        df = df.rename(index=str, columns=col)
    else:
        date = [prefix+'DateCommande']
        df = pd.read_csv(path, sep='\t', encoding='utf-8', parse_dates=date,index_col=0)
    return df

def get_Comptes(path, prefix = 'C_', cleaned=False):
    """
    Read CSV (Comptes) into Dataframe. All relevant columns are kept and renamed with prefix.
    Args:
        path (str): file path to Comptes.csv
        prefix (str): All relevant columns are renamed with prefix
    Returns:
        df (Dataframe): Resulting dataframe
    """
    col = {'Id':prefix+'Id',
           'Adresse_CodePostal':prefix+'Adresse_CodePostal',
           'Adresse_Ville':prefix+'Adresse_Ville',
           'Adresse_AdresseLigne1':prefix+'Adresse_AdresseLigne1',
           'Adresse_AdresseLigne2':prefix+'Adresse_AdresseLigne2',
           'Adresse_AdresseLigne3':prefix+'Adresse_AdresseLigne3',
           'Latitude':prefix+'Latitude',
           'Longitude':prefix+'Longitude',
           'Nom':prefix+'Nom',
           'TypeCompte':prefix+'TypeCompte'}
    dt = {'Id':'int64',
           'Adresse_CodePostal':'object',
           'Adresse_Ville':'object',
           'Latitude':'float64',
           'Longitude':'float64',
           'Nom':'object',
           'TypeCompte':'int64'}
    if not cleaned:
        df = pd.read_csv(path, sep='\t', encoding='utf-8', usecols=list(col.keys()), dtype=dt)
        df = df.rename(index=str, columns=col)
    else:
        df = pd.read_csv(path, sep='\t', encoding='utf-8',index_col=0)
        df = df.rename(index=str, columns=col)
    return df

def get_OffreProduits(path, prefix = 'OP_', cleaned=False):
    """
    Read CSV (OffreProduits) into Dataframe. All relevant columns are kept and renamed with prefix.
    Args:
        path (str): file path to OffreProduits.csv
        prefix (str): All relevant columns are renamed with prefix
    Returns:
        df (Dataframe): Resulting dataframe
    """
    col = {'Id':prefix+'Id',
           'Offre_Id':'Offre_Id',
           'Produit_Id':'Produit_Id',
           'EstInsecable':prefix+'EstInsecable',
           'EstUnDon':prefix+'EstUnDon',
           'QuantiteUnite':prefix+'QuantiteUnite',
           'QuantiteValeur':prefix+'QuantiteValeur',
           'QuantiteValeurParLot':prefix+'QuantiteValeurParLot'}
    dt = {'Id':'int64',
           'Offre_Id':'int64',
           'Produit_Id':'int64',
           'EstInsecable':'bool',
           'EstUnDon':'bool',
           'QuantiteUnite':'object',
           'QuantiteValeur':'float64',
           'QuantiteValeurParLot':'float64'}
    if not cleaned:
        df = pd.read_csv(path, sep='\t', encoding='utf-8', usecols=list(col.keys()), dtype=dt)
        df = df.rename(index=str, columns=col)
    else:
        df = pd.read_csv(path, sep='\t', encoding='utf-8',index_col=0)
    return df

def get_Offres(path, prefix = 'O_', cleaned=False):
    """
    Read CSV (Offres) into Dataframe. All relevant columns are kept and renamed with prefix.
    Args:
        path (str): file path to Offres.csv
        prefix (str): All relevant columns are renamed with prefix
    Returns:
        df (Dataframe): Resulting dataframe
    """
    col = {'Id':prefix+'Id',
           'Compte_Id':'Compte_Id'}
    dt = {'Id':'int64',
          'Compte_Id':'int64'}
    if not cleaned:
        df = pd.read_csv(path, sep='\t', encoding='utf-8', usecols=list(col.keys()), dtype=dt)
        df = df.rename(index=str, columns=col)
    else:
        df = pd.read_csv(path, sep='\t', encoding='utf-8',index_col=0)
    return df

def get_Produits(path, prefix = 'P_', cleaned=False):
    """
    Read CSV (Produits) into Dataframe. All relevant columns are kept and renamed with prefix.
    Args:
        path (str): file path to Produits.csv
        prefix (str): All relevant columns are renamed with prefix
    Returns:
        df (Dataframe): Resulting dataframe
    """
    col = {'Id':prefix+'Id',
           'Categorie_CategorieProduit_Id':'CategorieProduit_Id',
           'Compte_Compte_Id':'Compte_Id',
           'Ean':prefix+'EAN',
           'Nom':prefix+'Nom',
           'PoidsUnitaire':prefix+'PoidsUnitaire'}
    dt = {'Id':'int64',
          'Categorie_CategorieProduit_Id':'int64',
          'Compte_Compte_Id':'float64',   #### ERROR OF PARSING THIS COL IN INT64 --> USE FLOAT64 AND CORRECTION BELOW
          'Ean':'object',
          'Nom':'object',
          'PoidsUnitaire':'float64'}
    dt_c = {prefix+'Id':'int64',
          'CategorieProduit_Id':'int64',
          'Compte_Id':'float64',   #### ERROR OF PARSING THIS COL IN INT64 --> USE FLOAT64 AND CORRECTION BELOW
          prefix+'EAN':'object',
          prefix+'Nom':'object',
          prefix+'PoidsUnitaire':'float64'}
    if not cleaned:
        df = pd.read_csv(path, sep='\t', encoding='utf-8', usecols=list(col.keys()), dtype=dt, low_memory=False)
        df = df.rename(index=str, columns=col)
    else:
        df = pd.read_csv(path, sep='\t', encoding='utf-8',index_col=0, dtype=dt_c, low_memory=False)
        df = df.rename(index=str)
    df.Compte_Id = df.Compte_Id.fillna(0).astype('int64') #### CORRECTION HERE
    return df

def extract_diff_rows(df1, df2, on_columns=[]):
    """
    Create a DataFrame containing only rows with different values
    Args:
        df1 (DataFrame): Updated DataFrame (potentially with new/modified data)
        df2 (DataFrame): Reference DataFrame
        on_columns (list): Name of columns to compare both df1 and df2
    Returns:
        df_diff (Dataframe): Resulting dataframe
    """
    import numpy as np
    df1 = df1.replace([np.nan],[None])
    df2 = df2.replace([np.nan],[None])
    df_diff = pd.DataFrame(columns = df1.columns)

    if df1[on_columns].equals(df2[on_columns]):
        return pd.DataFrame(columns=df1.columns)    
    if df2.size == 0:
        return df1

    df = pd.concat([df1[on_columns], df2[on_columns]])
    df = df.reset_index(drop=True)
    df_gpby = df.groupby(on_columns)

    idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]
    df_diff = df.reindex(idx)

    return df_diff

def get_cleaned_df(df_P, df_EC, df_RC, fname_P, fname_EC, fname_RC):
    '''
    '''
    import os.path

    df_P_cleaned  = pd.DataFrame(columns=list(df_P.columns))
    df_EC_cleaned = pd.DataFrame(columns=list(df_EC.columns))
    df_RC_cleaned = pd.DataFrame(columns=list(df_RC.columns))

    if os.path.isfile(fname_P):
        df_P_cleaned    = get_Produits (fname_P, prefix='P_', cleaned=1)
    if os.path.isfile(fname_EC):
        df_EC_cleaned   = get_Comptes  (fname_EC, prefix='EC_', cleaned=1)
    if os.path.isfile(fname_RC):
        df_RC_cleaned   = get_Comptes  (fname_RC, prefix='RC_', cleaned=1)
        
    return df_P_cleaned, df_EC_cleaned, df_RC_cleaned

def create_diff_df(df_P, df_EC, df_RC, fname_P, fname_EC, fname_RC):
    '''
    '''
    # Compare 'Comptes' and 'Produits' tables with already corrected rows
    df_P_cleaned, df_EC_cleaned, df_RC_cleaned = get_cleaned_df(df_P, df_EC, df_RC, fname_P, fname_EC, fname_RC) 

    P_columns  = [c for c in list(df_P.columns) if c not in ('P_PoidsUnitaire','P_Nom')]
    EC_columns = [c for c in list(df_EC.columns) if c not in ('EC_Nom','EC_Latitude','EC_Longitude')]
    RC_columns = [c for c in list(df_RC.columns) if c not in ('RC_Nom','RC_Latitude','RC_Longitude')]

    df_P_diff  = extract_diff_rows(df_P, df_P_cleaned, on_columns=P_columns)
    df_EC_diff = extract_diff_rows(df_EC, df_EC_cleaned, on_columns=EC_columns)
    df_RC_diff = extract_diff_rows(df_RC, df_RC_cleaned, on_columns=RC_columns)
    
    return df_P_diff, df_EC_diff, df_RC_diff

def merge_tables(df1, df2, on_col=[], col_name='', how='inner', del_col=True):
    """
    Merge two DataFrames on different column names
    Args:
        df1 (Dataframe): file path to Produits.csv
        df2 (Dataframe): 
        on_col (list)  : Name of the columns in df1 and df2 to merge on [df1_colname, df2_colname]
        col_name (str) : Rename the column used for merging
        how (str)      : type of merge ('inner', 'outer', 'left', 'right')
        del_col (bool) : Delete the columns used for merging (True or False)
    Returns:
        df (Dataframe): Resulting merged dataframe
    """
    # merge tables with different column names
    df1 = df1.rename(index=str, columns={on_col[0]:col_name})
    df2 = df2.rename(index=str, columns={on_col[1]:col_name})
    df = pd.merge(df1, df2, how=how)
    if del_col:
        df.drop(col_name, axis=1, inplace=True)
    return df

def merge_loop_tables(dict_merge):
    """
    Merge multiple DataFrame in sequence
    Args:
        dict_merge (list of dict): Merge sequence
            dict: {df2      = Dataframe to merge,
                   on_col   = Name of columns to merge on
                   col_name = Rename the column used for merging
                   how      = Type of merge ('inner', 'outer', 'left', 'right')
                   del_col  = Delete the columns used for merging (True or False)
    Returns:
        df (Dataframe): Resulting merged dataframe
    """
    # Starting with empty DataFrame
    df = pd.DataFrame(columns=['Id'])
    
    # Merge loop using merge_tables() function
    for merge_step in dict_merge:
        df = merge_tables(df,merge_step['df2'] ,
                             on_col=merge_step['on_col'], 
                             col_name=merge_step['col_name'],
                             how=merge_step['how'], 
                             del_col=merge_step['del_col'])
        print('----> MERGE STEP ---->')
        print(list(df.columns))
        print(len(df))
    return df

##############################################################
### List of functions used for cleaning Comptes table and 
### geo positionning data (Longitidue and Latitude)
##############################################################
def geocode(query, IGN_API=''):
    from geopy.geocoders import IGNFrance
    geolocator = IGNFrance(api_key=IGN_API, referer='localhost', user_agent='Agent_tests')
    
    location = geolocator.geocode(query,maximum_responses=1,exactly_one=True)
    
    return (location.longitude, location.latitude)

def geotag_Compte(df, prefix='', IGN_API=''):
    """
    This function corrects Phenix original geo coordinates (longitude and latitude).
    This function uses IGN geocoding API to convert adresses into Longitude and Latitude coordinates. 
    Args:
        df (DataFrame): 'Comptes' DataFrame
        prefix (str): Prefix used in the 'Comptes' DataFrame
        IGN_API (str): IGN API key needed to access to IGN geocoding API
    Returns:
        df_matrix (DataFrame): Simplified version of 'Comptes' DataFrame with the following columns
            Nom              = Account name as in PhenixDB
            AdresseLigne3    = Account address as in PhenixDB
            Ville            = Account city as in PhenixDB
            CodePostal       = Account postal code as in PhenixDB
            old_lon, old_lat = Account original geo coordinate as in PhenixDB
            new_lon, new_lat = Account recalculated geo coordinate from IGN
            delta            = Distance (km) between old and new geo coordinates
    """
    from geopy.geocoders import IGNFrance
    from geopy.distance import lonlat, distance

    geolocator = IGNFrance(api_key=IGN_API, referer='localhost', user_agent='Agent_tests')
    matrix = []
    
    for index, value in df.iterrows():
        i = value[prefix+'Id']
        adresse1 = '' if str(value[prefix+'Adresse_AdresseLigne1'])=='nan' else str(value[prefix+'Adresse_AdresseLigne1'])
        adresse2 = '' if str(value[prefix+'Adresse_AdresseLigne2'])=='nan' else str(value[prefix+'Adresse_AdresseLigne2'])
        adresse3 = '' if str(value[prefix+'Adresse_AdresseLigne3'])=='nan' else str(value[prefix+'Adresse_AdresseLigne3'])
        ville = '' if str(value[prefix+'Adresse_Ville'])=='nan' else str(value[prefix+'Adresse_Ville'])
        CP = '' if str(value[prefix+'Adresse_CodePostal'])=='nan' else str(value[prefix+'Adresse_CodePostal'])
        query = adresse3 + ',' + ville + ',' + CP
        
        # check if geolocation is found
        try:
            location = geolocator.geocode(query,maximum_responses=1,exactly_one=True)
        except:
            print('(%s) %s --> location not found' % (i, query))
            element= dict(Id = value[prefix+'Id'],
                      delta=None,
                      Nom=value[prefix+'Nom'],
                      adresse1=value[prefix+'Adresse_AdresseLigne1'],
                      adresse2=value[prefix+'Adresse_AdresseLigne2'],
                      adresse3=value[prefix+'Adresse_AdresseLigne3'],
                      ville=value[prefix+'Adresse_Ville'],
                      CP=value[prefix+'Adresse_CodePostal'],
                      old_lon=value[prefix+'Longitude'],
                      old_lat=value[prefix+'Latitude'],
                      new_lon=None,
                      new_lat=None)
            matrix.append(element)
            continue
            
        # calculate distance old vs new geolocation
        old_lonlat = (value[prefix+'Longitude'], value[prefix+'Latitude'])
        new_lonlat = (location.longitude, location.latitude)
        delta = calc_geodistance(lonlat1=old_lonlat, lonlat2=new_lonlat)
        #### delta = distance(lonlat(*old_lonlat), lonlat(*new_lonlat)).km 
                                   
        element = dict(Id = value[prefix+'Id'],
                      delta=delta,
                      Nom=value[prefix+'Nom'],
                      adresse1=value[prefix+'Adresse_AdresseLigne1'],
                      adresse2=value[prefix+'Adresse_AdresseLigne2'],
                      adresse3=value[prefix+'Adresse_AdresseLigne3'],
                      ville=value[prefix+'Adresse_Ville'],
                      CP=value[prefix+'Adresse_CodePostal'],
                      old_lon=value[prefix+'Longitude'],
                      old_lat=value[prefix+'Latitude'],
                      new_lon=location.longitude,
                      new_lat=location.latitude)
        matrix.append(element)
    df_matrix = pd.DataFrame.from_dict(matrix)
    return df_matrix

def calc_geodistance(lonlat1=(), lonlat2=()):
    from geopy.distance import lonlat, distance
    
    dist = distance(lonlat(*lonlat1), lonlat(*lonlat2)).km 
    return dist

def calc_distance(df,col_name='CO_distance',pref_EC='EC_',pref_RC='RC_'):
    '''
    Adds a column of distance between Emetteur and Recepteur for each CommandeProduits.
    It requires Emetteur and Recepteur Comptes merged data.
    Args:
        df (DataFrame): Merged DataFrame of CommandeProduits, Emetteur and Recepteur Comptes
        col_name (str): Name of the distance column
        pref_EC and pref_RC (str): Prefix used in the Emetteur and Recepteur Comptes
    Returns:
        df (DataFrame): Resulting DataFrame with the added distance column
    '''
    from math import sin, cos, sqrt, atan2, radians
    df_calc = pd.DataFrame()
    
    # approximate radius of earth in km
    R = 6373.0
    
    df_calc['lat1'] = df[pref_EC+'Latitude' ].apply(lambda x: radians(x))
    df_calc['lon1'] = df[pref_EC+'Longitude'].apply(lambda x: radians(x))
    df_calc['lat2'] = df[pref_RC+'Latitude' ].apply(lambda x: radians(x))
    df_calc['lon2'] = df[pref_RC+'Longitude'].apply(lambda x: radians(x))
    
    df_calc['dlat'] = df_calc['lat2']-df_calc['lat1']
    df_calc['dlon'] = df_calc['lon2']-df_calc['lon1']
    
    df_calc['a'] = df_calc.apply(
        lambda row: sin(row['dlat'] / 2)**2 + cos(row['lat1']) * cos(row['lat2']) * sin(row['dlon'] / 2)**2, 
        axis=1)
    df_calc['c'] = df_calc.apply(lambda row: 2 * atan2(sqrt(row['a']), sqrt(1 - row['a'])),axis=1)
    df_calc[col_name] = df_calc['c'] * R
    
    df[col_name] = df_calc[col_name]
    
    return df

def manual_geotag(df_matrix):
    '''
    This function manually corrects geotags of Phenix accounts
    Args:
        df_matrix (DataFrame): DataFrame resulting of geotag_Comptes()
    Returns:
        df_matrix (DataFrame): Corrected geotags
    '''
    dict_manual = [
                   dict(Id=296,new_lon=-1.17891,new_lat=47.3720818), # E.Leclerc Ancenis
                   dict(Id=1301,new_lon=2.00594,new_lat=43.46403), # CASINO REVEL 31597
                   dict(Id=1880,new_lon=0.09723,new_lat=48.43538), # Carrefour Market - Alençon
                   dict(Id=2418,new_lon=2.35436,new_lat=48.84016), # Franprix SEBASTOPOL 5651
                   dict(Id=2438,new_lon=2.35781,new_lat=48.87406), # Franprix MAGENTA DISTR 5200
                   dict(Id=2440,new_lon=2.4097477,new_lat=48.8554594), # Franprix SOGI VINGT 5209
                   dict(Id=2468,new_lon=2.37312,new_lat=48.84913), # Franprix SUPERANT 6241
                   dict(Id=1970,new_lon=2.0014673,new_lat=43.45391), # Restos du coeur 31 - Centre de Revel
                   dict(Id=2555,new_lon=6.491198,new_lat=44.545372), # Intermarché Baratier
                   dict(Id=1983,new_lon=0.09723,new_lat=48.43538), # Banque Alimentaire 87o
                   dict(Id=2074,new_lon=2.001467,new_lat=43.45391), # SCF 78 Maisons Lafitte
                   dict(Id=2533,new_lon=2.35436,new_lat=48.84016), # RDC 25 Valdahon
                   dict(Id=2553,new_lon=2.35781,new_lat=48.87406), # CHU Altho
                   dict(Id=2583,new_lon=2.37312,new_lat=48.84913), # RdC 37 Joué-les-Tours
                   dict(Id=2113,new_lon=-3.02101,new_lat=47.8741), # Banque Alimentaire Baud
                   dict(Id=1552,new_lon=1.2749,new_lat=45.80956), # La Graine de l'Arbre du Voyageur
                   dict(Id=1985,new_lon=2.96303,new_lat=48.41848), # Le Campus de la transition
                   dict(Id=1525,new_lon=1.756843,new_lat=45.260449),  # Association Tulle Solidarité
                   dict(Id=2161,new_lon=-1.166043,new_lat=47.745453), # CCAS Ombrée d'Anjou (5 rue de l'hotel de ville)
                   dict(Id=1033,new_lon=2.9999,new_lat=43.18333), # Secours Populaire Français 11 - Antenne de Narbonne
                    # 1464- PARTAGE
                   ]
    for c in dict_manual:
        # Apply manual correction to df_matrix
        index = df_matrix[df_matrix.Id == c['Id']].index[0]
        df_matrix.loc[(index),['new_lat']] = c['new_lat']
        df_matrix.loc[(index),['new_lon']] = c['new_lon']

        # Calculate distance
        old_lat = df_matrix.loc[(index)].get_value('old_lat')
        old_lon = df_matrix.loc[(index)].get_value('old_lon')
        delta = calc_geodistance(lonlat1=(old_lon, old_lat), lonlat2=(c['new_lon'], c['new_lat']))
        df_matrix.loc[(index),['delta']] = delta
    return df_matrix

def replace_geotag(df, df_matrix, prefix='', threshold=1):
    """
    Using the df_matrix from geotag_Compte(), this function replaces old to new geo coordinates.
    It uses a threshold distance over which the old are replaced by new coordinates
    Args:
        df (DataFrame): 'Comptes' DataFrame
        df_matrix (DataFrame): DataFrame resulting of geotag_Comptes()
        prefix (str): Prefix used in the 'Comptes' DataFrame
        threshold (int): Threshold distance over which the old are replaced by new coordinates
    Returns:
        df (DataFrame): Simplified Comptes DataFrame with the following columns
    """
    df = pd.concat([df,pd.DataFrame(columns=[prefix+'Longitude',prefix+'Latitude'])])
    #print(df)
    # loop on geocoded elements that are further than the threshold
    for index, value in df_matrix[df_matrix.delta > threshold].iterrows():
        df_index = df[(df[prefix+'Id']==value.Id)].index

        df.loc[list(df_index),[prefix+'Longitude']] = value.new_lon
        df.loc[list(df_index),[prefix+'Latitude']] = value.new_lat
    
    # loop on elements that couldn't be geocoded
    for index, value in df_matrix[df_matrix.delta.isnull()].iterrows():
        df_index = df[(df[prefix+'Id']==value.Id)].index

        df.loc[list(df_index),[prefix+'Longitude']] = value.old_lon
        df.loc[list(df_index),[prefix+'Latitude']] = value.old_lat
    print('%d coordinates has been updated of %d' % (len(df_matrix[df_matrix.delta > threshold]), len(df_matrix)))
    
    return df

def plot_df_matrix(df_matrix):
    """
    Plot a map of all Phenix accounts before and after geocoding.
    This function requires plotly.
    Args:
        df_matrix (DataFrame): DataFrame resulting of geotag_Comptes()
    Returns:
        Map plot from Plotly
    """
    import plotly
    from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
    init_notebook_mode()
    
    trace_new = {
        'type':'scattergeo',
        'lat':df_matrix.new_lat.values.tolist(),
        'lon':df_matrix.new_lon.values.tolist(),
        'text':df_matrix.Nom.values.tolist(),
        'name':'NEW',
        'marker':{
            'color': 'blue',
        },
        'mode':'markers'
    }
    trace_old = {
        'type':'scattergeo',
        'lat':df_matrix.old_lat.values.tolist(),
        'lon':df_matrix.old_lon.values.tolist(),
        'text':df_matrix.Nom.values.tolist(),
        'name': 'OLD',
        'marker':{
            'color': 'red',
            'symbol':'x'
        },
        'mode':'markers'
    }
    layout = dict(
            title = 'Comparaison des positions des comptes (avant/après correction par geocoding)',
            width = 800,
            geo = dict(
                scope='europe',
                resolution=50,
                center= {'lon':2,'lat':46.5},
                framewidth=700,
                showland = True,
                landcolor = 'rgb(243, 243, 243)',
                countrycolor = 'rgb(204, 204, 204)'
                ),
        )

    fig = dict( data=[trace_old, trace_new], layout=layout)
    plotly.offline.iplot(fig) 
    return fig

##############################################################
### List of functions used for extracting quantity from Product name 
### and value (3€/kg average)
##############################################################
def add_product_qty(df_P):
    """
    STEP 1
    Get product quantity from Phenix product name
    Args:
        df_P (DataFrame): Product DataFrame
    Returns:
        df_P (DataFrame): Product DataFrame with updated quantity
    """
    import off_mgt as off
    print('-- Adding Product quantity column --')
    print('WARNING - This function is time consuming.')
    df_P1 = df_P.copy()
    
    # First try to extract quantity from product name
    df_P1['Qty'] = df_P1.P_Nom.apply(lambda name: off.convert_quantity(name))
    df_P1['Qty_val']    = [q.get('val') for q in df_P1.Qty]
    df_P1['Qty_unit']   = [q.get('unit') for q in df_P1.Qty]
    df_P1['Qty_std']    = [q.get('std') for q in df_P1.Qty]
    df_P1['Qty_approx'] = [q.get('approx') for q in df_P1.Qty]
    df_P1['Qty_method'] = 1
    print('STEP 1 - %d (not std) %d (std)' % (len(df_P1[df_P1.Qty_std==False]),len(df_P1[df_P1.Qty_std==True])))
    
    return df_P1

def get_qty_from_PhenixCol(df_P):
    """
    STEP 2
    Get product quantity from Phenix product quantity column (kg)
    Args:
        df_P (DataFrame): Product DataFrame
    Returns:
        df_P (DataFrame): Product DataFrame with updated quantity
    """
    """filter_ = (df_P.Qty_std==False) & (df_P.P_PoidsUnitaire.notnull())
    df_P.loc[filter_,'Qty_val']    = df_P[filter_].P_PoidsUnitaire * 1000
    df_P.loc[filter_,'Qty_unit']   = df_P[filter_].Qty_unit.apply(lambda x: 'g')
    df_P.loc[filter_,'Qty_approx'] = df_P[filter_].Qty_approx.apply(lambda x: bool(False))
    df_P.loc[filter_,'Qty_method'] = df_P[filter_].Qty_method.apply(lambda x: int(2))
    df_P.loc[filter_,'Qty_std'] = df_P[filter_].Qty_std.apply(lambda x: bool(True))"""
    df_P2 = df_P.copy()
    
    df_P2['Qty_val']    = df_P2.P_PoidsUnitaire * 1000
    filter_ = (df_P2.Qty_val>0)
    df_P2.loc[filter_,'Qty_unit']  = 'g'
    df_P2.loc[filter_,'Qty_approx'] = False
    df_P2.loc[filter_,'Qty_method'] = 2
    df_P2.loc[filter_,'Qty_std'] = True
    print('STEP 2 - %d (not std) %d (std)' % (len(df_P2[df_P2.Qty_std==False]),len(df_P2[df_P2.Qty_std==True])))
    return df_P2

def extrapolate_qty_from_productvalue(df_P, df_OP, df_CP):
    """
    STEP 3
    Extrapolate product quantity from the product value (€)
    Args:
        df_P (DataFrame): Product DataFrame
        df_OP (DataFrame): OffreProduit DataFrame
        df_CP (DataFrame): CommandeProduit DataFrame
    Returns:
        df_P (DataFrame): Product DataFrame with updated quantity
    """
    df_P3 = df_P.copy()
    df_P3 = pd.concat([df_P3,pd.DataFrame(columns=['Qty_val','Qty_unit','Qty_approx','Qty_method','Qty_std'])])
    
    #filter_ = (df_P.Qty_std==False) 
    df_OPF = df_OP[['OP_Id','OP_QuantiteValeur','OP_QuantiteUnite','Produit_Id']]
    df_CPF = df_CP[['CP_Id','OffreProduit_Id','CP_QuantiteValeur','CP_QuantiteTotale','CP_QuantiteUnite','CP_MontantTotal']]
    df_PF  = df_P3[['P_Id','P_food_group','Qty_val','Qty_unit','Qty_std','Qty_approx','Qty_method']]

    dict_merge = [{'df2':df_PF,  'on_col': ['Id','P_Id'],                 'col_name':'P_Id'  , 'how':'right','del_col':False},
                  {'df2':df_OPF, 'on_col': ['P_Id','Produit_Id'],         'col_name':'P_Id'  , 'how':'inner','del_col':False},
                  {'df2':df_CPF, 'on_col': ['OP_Id','OffreProduit_Id'],   'col_name':'OP_Id' , 'how':'inner','del_col':True},]

    df_F = merge_loop_tables(dict_merge)
    df_F.drop_duplicates('P_Id',inplace=True)                ##### Source d'erreurs
    df_F.set_index(['P_Id'],inplace=True,drop=False)
    df_P3.set_index(['P_Id'],inplace=True,drop=False)
    
    df_F1 = df_F.apply(lambda row: calc_qty_from_value(row),axis=1)
    df_P3.update(df_F1)
    print('STEP 3 - %d (not std) %d (std)' % (len(df_P3[df_P3.Qty_std==False]),len(df_P3[df_P3.Qty_std==True])))
    return df_P3

def get_qty_from_OFF(df_P, OFF_csv):
    """
    STEP 4
    Get product quantity from OFF database
    Args:
        df_P (DataFrame): Product DataFrame
        OFF_CSV (str): Path to OFF DB in csv
    Returns:
        df_P (DataFrame): Product DataFrame with updated quantity
    """
    import off_mgt as off
    
    ddf_OFF = load_OFF(OFF_csv,col=["code", "product_name","quantity"])
    df_OFF = ddf_OFF.compute()
    
    df_P4 = df_P.copy()
    df_P4 = pd.concat([df_P4,pd.DataFrame(columns=['Qty_val','Qty_unit','Qty_approx','Qty_method','Qty_std'])])
    
    #filter_ = (df_PC.Qty_std==False)
    #df_PF = df_PC[filter_]
    df_PF = merge_tables(df_P4,df_OFF,on_col=['P_EAN','code'],col_name='P_EAN',how='inner',del_col=False)
    df_PF.drop_duplicates('P_Id',inplace=True)
    
    df_PF['Q_'] = df_PF.quantity.apply(lambda name: off.convert_quantity(name))

    df_PF['Qty_val']    = [q.get('val')    for q in df_PF.Q_]
    df_PF['Qty_unit']   = [q.get('unit')   for q in df_PF.Q_]
    df_PF['Qty_std']    = [q.get('std')    for q in df_PF.Q_]
    df_PF['Qty_approx'] = [q.get('approx') for q in df_PF.Q_]
    df_PF['Qty_method'] = 4

    df_PF.drop(['product_name','quantity','Q_'],axis=1,inplace=True)
    df_PF.set_index(['P_Id'],inplace=True,drop=False)
    df_P4.set_index(['P_Id'],inplace=True,drop=False)
    
    df_P4.update(df_PF)
    print('STEP 4 - %d (not std) %d (std)' % (len(df_P4[df_P4.Qty_std==False]),len(df_P4[df_P4.Qty_std==True])))
    return df_P4

def calc_qty_from_value(row):
    """
    Estimates product quantity based on product value and food group
    Args:
        row (): see extrapolate_qty_from_productvalue() function
    Returns:
        qty (float): Product quantity estimation (g)
    """
    
    value = abs(row.CP_MontantTotal)
    food_group = row.P_food_group
    Q_unit = row.CP_QuantiteUnite
    Q_val = abs(row.CP_QuantiteTotale)
    #print(Q_unit)
    
    # Check if CP has already a weight. If so, use it.
    if Q_unit in ['Kg','kg','Kilo','Litre','Litres']:
        row['Qty_val']    = Q_val * 1000
        row['Qty_unit']   = 'g'
        row['Qty_approx'] = bool(False)
        row['Qty_method'] = 3.1
        row['Qty_std']    = bool(True)
        #print(row[['P_Id','Qty_val','Qty_unit','Qty_std','Qty_approx','Qty_method']])
        return row[['P_Id','Qty_val','Qty_unit','Qty_std','Qty_approx','Qty_method']]
    
    # Calculate weight from food group and product value
    if float(value)<=0:
        #print(row[['P_Id','Qty_val','Qty_unit','Qty_std','Qty_approx','Qty_method']])
        return row[['P_Id','Qty_val','Qty_unit','Qty_std','Qty_approx','Qty_method']]
    
    dict_euro_kilo = {
                        None:3,
                        'nan':3,
                        'Produits gras sucrés salés':3,
                        'Produits laitiers (hors fromage)':3,
                        'Féculents raffinés':2,
                        'Fruits':1.5,
                        'Exclus':3, 
                        'Plats préparés':3, 
                        'Légumes':1.5, 
                        'Viande, oeufs':3, 
                        'Fromage':3,
                        'Matières grasses ajoutées':3, 
                        'Féculents non raffinés':1.5, 
                        'Poisson':3}
    
    if (Q_unit in ['Unité','Unités','unité','unités','Pcs','pièces']) & (Q_val>0):
        if food_group in (dict_euro_kilo.keys()):
            row.Qty_val = (float(value) / dict_euro_kilo[food_group]) * 1000 / Q_val
            row.Qty_unit = 'g'
            row.Qty_approx = bool(False)
            row.Qty_method = 3.0
            row.Qty_std = bool(True)
        else:
            row.Qty_val = (float(value) / 3) * 1000 / Q_val
            row.Qty_unit = 'g'
            row.Qty_approx = bool(False)
            row.Qty_method = 3.0
            row.Qty_std = bool(True)
        return row[['P_Id','Qty_val','Qty_unit','Qty_std','Qty_approx','Qty_method']]
    else:
        return row[['P_Id','Qty_val','Qty_unit','Qty_std','Qty_approx','Qty_method']]
    #print(row[['P_Id','Qty_val','Qty_unit','Qty_std','Qty_approx','Qty_method']])
    return row[['P_Id','Qty_val','Qty_unit','Qty_std','Qty_approx','Qty_method']]

def prep_qty_val(df_P1, df_P2, df_P3, df_P4):
    """
    Takes all 4 quantity estimation methods into one DataFrame
    Args:
        df_P1,2,3,4 (DataFrame): DataFrame results of the 4 methods
    Returns:
        Qty_val (DataFrame): DataFrame
    """
    Qty_val = pd.concat([df_P1.P_Nom, df_P1.Qty_val,df_P2.Qty_val,df_P3.Qty_val,df_P4.Qty_val],axis=1)
    Qty_unit = pd.concat([df_P1.P_Nom, df_P1.Qty_unit,df_P2.Qty_unit,df_P3.Qty_unit,df_P4.Qty_unit],axis=1)
    Qty_std = pd.concat([df_P1.P_Nom, df_P1.Qty_std,df_P2.Qty_std,df_P3.Qty_std,df_P4.Qty_std],axis=1)
    
    col_name = ['P_Nom','1','2','3','4']
    Qty_val.columns = col_name
    Qty_unit.columns= col_name
    Qty_std.columns = col_name

    Qty_val['1'] = ([i=='g' for i in Qty_unit['1']] and [i==True for i in Qty_std['1']]) * Qty_val['1']
    Qty_val['2'] = ([i=='g' for i in Qty_unit['2']] and [i==True for i in Qty_std['2']]) * Qty_val['2']
    Qty_val['3'] = ([i=='g' for i in Qty_unit['3']] and [i==True for i in Qty_std['3']]) * Qty_val['3']
    Qty_val['4'] = ([i=='g' for i in Qty_unit['4']] and [i==True for i in Qty_std['4']]) * Qty_val['4']
    Qty_val = Qty_val.replace([0],[None])
    return Qty_val

def select_qty_method(Qty_val):
    """
    Select the appropriate quantity method
    Args:
        Qty_val (DataFrame): see prep_qty_val() function
    Returns:
        Qty_val (DataFrame): Adds Qty_val.value
    """
    # Use method 2 in priority
    filter_ = Qty_val['2'].replace([None],[0]) > 0
    Qty_val.loc[filter_,'value'] = Qty_val[filter_]['2'] 

    # Use method 1 or 4 if other is missing
    filter_ = (Qty_val['2'].replace([None],[0]) <= 0)
    filter_ = (Qty_val['4'].replace([None],[0]) <= 0) & (Qty_val['1'].replace([None],[0]) > 0) & filter_
    Qty_val.loc[filter_,'value'] = Qty_val[filter_]['1']

    filter_ = (Qty_val['2'].replace([None],[0]) <= 0)
    filter_ = (Qty_val['1'].replace([None],[0]) <= 0) & (Qty_val['4'].replace([None],[0]) > 0) & filter_
    Qty_val.loc[filter_,'value'] = Qty_val[filter_]['4']

    # Choose method 1 or 4 depending on their difference
    threshold = 1000 # grams

    filter_ = (Qty_val['2'].replace([None],[0]) <= 0)
    filter_ = (Qty_val['1'].replace([None],[0]) > 0) & (Qty_val['4'].replace([None],[0]) > 0) & filter_
    filter_ = (abs(Qty_val['1'] - Qty_val['4']) <= threshold) & filter_
    Qty_val.loc[filter_,'value'] = Qty_val[filter_]['1']

    filter_ = (Qty_val['2'].replace([None],[0]) <= 0)
    filter_ = (Qty_val['1'].replace([None],[0]) > 0) & (Qty_val['4'].replace([None],[0]) > 0) & filter_
    filter_ = (abs(Qty_val['1'] - Qty_val['4']) > threshold) & filter_
    Qty_val.loc[filter_,'value'] = Qty_val[['1','4']].min(axis=1)[filter_]

    # Use method 3 for the rest of products
    filter_ = (Qty_val['2'].replace([None],[0]) <= 0)
    filter_ = (Qty_val['3'].replace([None],[0]) > 0) & (Qty_val['value'].replace([None],[0]) == 0) & filter_
    Qty_val.loc[filter_,'value'] = Qty_val[filter_]['3']
    
    # Double check resulting 'value' with method 3 
    # Delta is > 1t, use method 3
    filter_ = (Qty_val['value'] - Qty_val['3'])>1000000
    Qty_val.loc[filter_,'value'] = Qty_val[filter_]['3']
    
    # Remove 'value' > 10t
    filter_ = Qty_val['value']>10000000
    Qty_val.loc[filter_,'value'] = None
    
    return Qty_val

##############################################################
### List of functions used for adding Food Groups to Products
### Uses Mehdi ML algo results (csv)
##############################################################
def add_foodgroup(df_P, csv_path=''):
    """
    Adds Food Group column in the Product table using Mehdi ML Algo results
    Args:
        df_P (DataFrame): Product DataFrame
        csv_path (str): CSV path to mehdi ML algo results
    Returns:
        df_P (DataFrame): Product DataFrame including the Food Group column
    """
    print('-- Adding Product food group column --')
    df_mehdi = pd.read_csv(csv_path, sep=';',encoding='utf-8')
    df_mehdi = df_mehdi.rename(columns={'EAN':'P_EAN','foodgroup':'P_food_group'})
    df_mehdi.drop('Produit_Nom',axis=1,inplace=True)
    df_mehdi.drop_duplicates('P_EAN',inplace=True)
    
    df_P = merge_tables(df_P,df_mehdi,on_col=['P_EAN','P_EAN'],col_name='P_EAN',how='left',del_col=False)
    print('--> COMPLETED ')
    return df_P


def load_OFF(OFF_csv,col=[]):
    # col = ["code", "product_name", "pnns_groups_1", "pnns_groups_2", "quantity","serving_quantity"]
    import dask
    import dask.dataframe as dd
    
    ddf_OFF = dd.read_csv("./OFF_DB/fr.openfoodfacts.org.products.csv", sep="\t", encoding="utf-8", low_memory=False,
                      usecols=col,
                      dtype={'allergens': 'object',
           'cities_tags': 'object',
           'emb_codes': 'object',
           'emb_codes_tags': 'object',
           'first_packaging_code_geo': 'object',
           'generic_name': 'object',
           'ingredients_from_palm_oil_tags': 'object',
           'labels': 'object',
           'labels_fr': 'object',
           'labels_tags': 'object',
           'manufacturing_places': 'object',
           'manufacturing_places_tags': 'object',
           'origins': 'object',
           'origins_tags': 'object',
           'stores': 'object',
           'code': 'object','allergens_fr': 'object',
           'cities': 'object',
           'created_t': 'object',
           'last_modified_t': 'object',
           'image_url': 'object',
           'image_small_url': 'object',
           'image_ingredients_url': 'object',
           'image_ingredients_small_url': 'object',
           'image_nutrition_url': 'object',
           'image_nutrition_small_url': 'object',
           'serving_quantity':'object'})
    return ddf_OFF