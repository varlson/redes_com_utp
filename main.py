from utilities import *

# extractor('cases-brazil-cities-time', 'aerialUTP', 'Separados/aerialUTP', 'aerialUTP', True)
# extractor('cases-brazil-cities-time', 'fluvial', 'Separados/fluvial', 'fluvial', False)
# extractor('cases-brazil-cities-time', 'terrestrial', 'Separados/terrestrial', 'terrestrial', Fal2s)

all_process = ["aerialUTP", "fluvial", "terrestrial"]
for process in all_process[]:
    
    name = process
    
    mobility = pd.read_csv('Filtrados/'+name+'.csv')
    graph = ig.Graph.Read_GraphML('datas/'+name+'.GraphML')

    degree = sort_by_metric(graph, "degree", name)
    betweenness = sort_by_metric(graph, "betweenness", name)
    betweenness_w = sort_by_metric(graph, "betweenness_w", name)
    strength = sort_by_metric(graph, "strength", name)

    _tuple = []
    
    x_axis = [x for x in range(graph.vcount())]
    cities_geocodeList = list(mobility['Geocode'])

    graph_geocodeList = [x[3] for x in degree]
    corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
    spear = mapeador(mobility, degree, name)
    _tuple.append((x_axis, corresp, spear))
    
    graph_geocodeList = [x[3] for x in betweenness]
    corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
    spear = mapeador(mobility, betweenness, name)
    _tuple.append((x_axis, corresp, spear))
    
    
    graph_geocodeList = [x[3] for x in strength]    
    corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
    spear = mapeador(mobility, strength, name)
    _tuple.append((x_axis, corresp, spear))

    graph_geocodeList = [x[3] for x in betweenness_w]    
    corresp = correspondence_builder(cities_geocodeList, graph_geocodeList)
    spear = mapeador(mobility, betweenness_w, name)
    _tuple.append((x_axis, corresp, spear))

    graphPloter(_tuple, ["$k$", "$b$", "$s$", "$b_{w}$"], name)
