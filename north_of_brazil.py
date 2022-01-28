from utilities import *
NORTH_START_GEO=[12, 16, 13, 17, 14, 11, 15]

def northBrazil_extractor(dataFrame, netwwork, output_path, isAereal=False):
    df_geocodes = list(dataFrame['Geocode'])
    cities=[]
    utp =[]
    geocode=[]
    for geocod in netwwork.vs['geocode']:
        
        state_geo = int(str(int(geocod))[:2])
        if state_geo in NORTH_START_GEO:
            try:
                index = df_geocodes.index(geocod)
                cities.append(dataFrame['Cidades'][index])
                geocode.append(df_geocodes[index])
                if isAereal:
                    utp.append(dataFrame['UTP'][index])
            except:
                pass
       
    
    df={}
    df['Cidades'] =cities
    df['Geocode'] = geocode
    if(len(utp)):
        df['utp']=utp
        
    df = pd.DataFrame(df)
    df.to_csv(output_path+'.csv', index=False)


# dataFrame = pd.read_csv('Separados/terrestrial/terrestrial.csv')
# graph = ig.Graph.Read_GraphML('datas/terrestrial.GraphML')

# pat =  'North_of_brazil/terrestrial'
# dirMaker(pat)
# northBrazil_extractor(dataFrame, graph, pat+'/terrestrial')

_tuple = []
graph = ig.Graph.Read_GraphML('datas/terrestrial.GraphML')

mobility = pd.read_csv('North_of_brazil/terrestrial/terrestrial.csv')
degree = teste(graph, "degree")
betweenness = teste(graph, "betweenness")
betweenness_w = teste(graph, "betweenness_w")
strength = teste(graph, "strength")

# print(f'degree: {degree}')
# print(f'betweenness: {betweenness}')
# print(f'betweenness_w: {betweenness_w}')
# print(f'strength: {strength}')

x_axis = indexFilter(list(mobility['Geocode']), graph)

cities_geocodeList = list(mobility['Geocode'])

graph_geocodeList = [x[3] for x in degree]
corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
spear = mapeador(mobility, degree, 'not_defined')
_tuple.append((x_axis, corresp, spear))


graph_geocodeList = [x[3] for x in betweenness]
corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
spear = mapeador(mobility, betweenness, 'not_defined')
_tuple.append((x_axis, corresp, spear))

graph_geocodeList = [x[3] for x in betweenness_w]
corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
spear = mapeador(mobility, betweenness_w, 'not_defined')
_tuple.append((x_axis, corresp, spear))


graph_geocodeList = [x[3] for x in strength]
corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
spear = mapeador(mobility, strength, 'not_defined')
_tuple.append((x_axis, corresp, spear))

graphPloter(_tuple, ["$k$","$b$", "$s$", "$b_{w}$"], 'north_brazil_terrestrial')