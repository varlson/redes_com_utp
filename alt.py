from processor import *
def alternative(graph, DataFrame):
    g_geocode = np.asarray(graph.vs['geocode'])
    df_geocode = np.asarray(list(DataFrame['Geocode']))
    
    cities=[]
    geocode=[]
    
    for index, geo in enumerate(g_geocode):
        if (not geo in geocode) and (geo in df_geocode):
            cities.append(DataFrame['Cidades'][index]) 
            geocode.append(geo)
    
    df = {}
    df['Cidades'] = cities
    df['Geocode'] = geocode
    df = pd.DataFrame(df)
    df.to_csv('Filtrados/alt_terrestrial.csv', index=False)
    
    

dataFrame = pd.read_csv('Separados/terrestrial/terrestrial.csv')
graph = ig.Graph.Read_GraphML('datas/terrestrial.GraphML')

alternative(graph, dataFrame)
    
    