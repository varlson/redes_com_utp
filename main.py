from utilities import *

# extractor('cases-brazil-cities-time', 'aerialUTP', 'Separados/aerialUTP', 'aerialUTP', True)
# extractor('cases-brazil-cities-time', 'fluvial', 'Separados/fluvial', 'fluvial', False)
# extractor('cases-brazil-cities-time', 'terrestrial', 'Separados/terrestrial', 'terrestrial', False)

# g = ig.Graph.Read_GraphML('datas/terrestrial.GraphML')
# dataframe = pd.read_csv('Separados/terrestrial/terrestrial.csv')
# filter(g, dataframe, 'terrestrial')




# all_process = ["aerialUTP", "fluvial", "terrestrial"]
# for process in all_process[2:]:
    
#     name = process
    
    # mobility = pd.read_csv('Filtrados/'+name+'.csv')
    # graph = ig.Graph.Read_GraphML('datas/terrestrial.GraphML')

    # degree = sort_by_metric(graph, "degree", name)
    # betweenness = sort_by_metric(graph, "betweenness", name)
    # betweenness_w = sort_by_metric(graph, "betweenness_w", name)
    # strength = sort_by_metric(graph, "strength", name)

    
    
    # _tuple = []
    
    # x_axis = [x for x in range(graph.vcount())]
    # cities_geocodeList = list(mobility['Geocode'])

    # graph_geocodeList = [x[3] for x in degree]
    # corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
    # spear = mapeador(mobility, degree, name)
    # _tuple.append((x_axis, corresp, spear))
    
    # graph_geocodeList = [x[3] for x in betweenness]
    # corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
    # spear = mapeador(mobility, betweenness, name)
    # _tuple.append((x_axis, corresp, spear))
    
    
    # graph_geocodeList = [x[3] for x in strength]    
    # corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
    # spear = mapeador(mobility, strength, name)
    # _tuple.append((x_axis, corresp, spear))

    # graph_geocodeList = [x[3] for x in betweenness_w]    
    # corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
    # spear = mapeador(mobility, betweenness_w, name)
    # _tuple.append((x_axis, corresp, spear))

    # graphPloter(_tuple, ["$k$", "$b$", "$s$", "$b_{w}$"], name)


# _tuple = []
# graph = ig.Graph.Read_GraphML('datas/fluvial.GraphML')

# mobility = pd.read_csv('Filtrados/fluvial.csv')
# degree = teste(graph, "degree")
# betweenness = teste(graph, "betweenness")
# betweenness_w = teste(graph, "betweenness_w")
# strength = teste(graph, "strength")

# x_axis = [x for x in range(graph.vcount())]

# cities_geocodeList = list(mobility['Geocode'])

# graph_geocodeList = [x[3] for x in degree]
# corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
# spear = mapeador(mobility, degree, 'fluvial')
# _tuple.append((x_axis, corresp, spear))

# graph_geocodeList = [x[3] for x in betweenness]
# corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
# spear = mapeador(mobility, betweenness, 'fluvial')
# _tuple.append((x_axis, corresp, spear))

# graph_geocodeList = [x[3] for x in strength]
# corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
# spear = mapeador(mobility, strength, 'fluvial')
# _tuple.append((x_axis, corresp, spear))


# graph_geocodeList = [x[3] for x in betweenness_w]
# corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
# spear = mapeador(mobility, betweenness_w, 'fluvial')
# _tuple.append((x_axis, corresp, spear))


# graphPloter(_tuple, ["$k$", "$b$", "$s$", "$b_{w}$"], 'fluvial')


''' AJUSTES PARA REDE TERRESTRE '''


_tuple = []
graph = ig.Graph.Read_GraphML('datas/terrestrial.GraphML')

mobility = pd.read_csv('Filtrados/terrestrial.csv')
degree = teste(graph, "degree")
betweenness = teste(graph, "betweenness")
betweenness_w = teste(graph, "betweenness_w")
strength = teste(graph, "strength")

ausentes = pd.read_csv('Filtrados/ausentes_terrestrial.csv')
ausentes = list(ausentes['Ausentes'])
x_axis = [i for i, x in enumerate(graph.vs['geocode']) if x not in ausentes]

cities_geocodeList = list(mobility['Geocode'])

graph_geocodeList = [x[3] for x in degree]
corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
spear = mapeador(mobility, degree, 'terrestrial')
_tuple.append((x_axis, corresp, spear))

graph_geocodeList = [x[3] for x in betweenness]
corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
spear = mapeador(mobility, betweenness, 'terrestrial')
_tuple.append((x_axis, corresp, spear))

graph_geocodeList = [x[3] for x in strength]
corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
spear = mapeador(mobility, strength, 'terrestrial')
_tuple.append((x_axis, corresp, spear))


graph_geocodeList = [x[3] for x in betweenness_w]
corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
spear = mapeador(mobility, betweenness_w, 'terrestrial')
_tuple.append((x_axis, corresp, spear))



graphPloter(_tuple, ["$k$", "$b$", "$s$", "$b_{w}$"], 'terrestrial')