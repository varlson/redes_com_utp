import igraph as ig
import pandas as pd
import numpy as np
from os import mkdir,path


"""
# Cria um diretorio caso o mesmo nao exista
# Entrada: nome de um ou diretorio com sub diretorios no formato: ex: "dados" caso um só, 
#   "dados/dados_importantes" diretorio com subdiretorio
"""
def dirMaker(dir):
    if not len(dir):
        print('invalid path')
        return 0
    
    subdirs = dir.split('/')
    fullPath =[]
    
    for index, dir in enumerate(subdirs):
        if not index:
            fullPath.append(dir)
        else:
            fullPath.append(fullPath[index-1]+'/'+dir)
    # print(fullPath)
    
    try:
        for p in fullPath:
            if not path.isdir(p):
                mkdir(p)
    except:
        print('Houve umerro, verifique o path inserito se esta no formato uma_pasta/outra_pasta/...')
        return 0


def extractor(file, network, full_path, name, isAereal): # This function extract 
    path = 'datas/'
    g = ig.Graph.Read_GraphML(path+network+'.GraphML')
    dataFrame = pd.read_csv(path+file+'.csv')
    
    
    # df_cities = dataFrame['city']
    # df_geocode = np.asarray(dataFrame['ibgeID'])
    
    # size = len(df_cities)
    
    g_cities = [x.lower() for x in g.vs['label']]
    g_geocode = [float(x) for x in g.vs['geocode']]
    
    geocode = []
    cities = []
    dates = []
    states =[]
    utp =[]
    
    for index in range(len(dataFrame['city'])):
        if(dataFrame['city'][index] !=  'TOTAL'):
            cid = dataFrame['city'][index].split('/')[0].lower()
            date = dataFrame['date'][index]
            geoc = float(dataFrame['ibgeID'][index])
            state = dataFrame['state'][index].upper()
            if cid in g_cities and geoc in g_geocode:
                geocode.append(geoc)
                cities.append(cid)
                dates.append(date)
                states.append(state)
                i = g_geocode.index(geoc)
                if isAereal:
                    utp.append(g.vs['utp'][i])
      
    
    df ={}
    
    df['Datas'] = dates
    df['Cidades'] = cities
    df['Estados'] = states
    df['Geocode'] = geocode
    if isAereal:
        df['UTP'] = utp
    
    df = pd.DataFrame(df)
    dirMaker(full_path)
    df.to_csv(full_path+'/'+name+'.csv', index=False)
    
    filter(g, pd.read_csv('Separados/'+name+'/'+name+'.csv'), name, isAereal)
    


def filter(network, city_cases, name, isAereal):
    length = len(city_cases['Geocode'])
    geocode =[]
    datas =[]
    utps=[]
    estados=[]
    cidades=[]
    
    for index in range(length):
        
        if not float(city_cases['Geocode'][index]) in geocode:
            geocode.append(float(city_cases['Geocode'][index]))
            datas.append(city_cases['Datas'][index])
            if isAereal:
                utps.append(city_cases['UTP'][index])
            estados.append(city_cases['Estados'][index])
            cidades.append(city_cases['Cidades'][index])
    
    df = {}
    df['Datas'] = datas
    df['Cidades'] = cidades
    df['Estados'] = estados
    df['Geocode'] = geocode
    if isAereal:
        df['UTP'] = utps
    df = pd.DataFrame(df)
    _path = 'Filtrados'
    dirMaker(_path)
    
    df.to_csv(_path+'/'+name+'.csv')
            