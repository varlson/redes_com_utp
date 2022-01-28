from processor import*
from scipy.stats import spearmanr
import matplotlib.pyplot as plt


"""
    sort_by_metric => Ordena os nós da rede de acordo com as metricas
    
    paramentros:
        graph => rede(Igraph)
        metric => metrica(string)
        
"""





def teste(graph, metric):
    
    peso = None
    
    if metric == "strength" or "betweenness_w":
        peso = graph.es['weight']
        peso = [0.001 if x <= 0 else x for x in peso]

    
    weighted =[]
    if metric == "strength":
        weighted =  graph.strength(weights=peso)
    else:
        # print(peso)
        weighted =  graph.betweenness(weights=peso)

    
    done =None
    
    if metric == "degree":
        temp =[]
        for x in range(graph.vcount()):
            temp.append([x, graph.degree(x), graph.vs['label'][x], graph.vs['geocode'][x]])
            done =temp
    elif metric == "betweenness":
        done = [[x, graph.betweenness(x), graph.vs['label'][x], graph.vs['geocode'][x]] for x in range(graph.vcount())]
        temp =[]
        for x in range(graph.vcount()):
            temp.append([x, graph.betweenness(x), graph.vs['label'][x], graph.vs['geocode'][x]])
            done =temp
            
    elif metric == "strength":
        temp =[]
        for index, x in enumerate(weighted):
            temp.append([index, x, graph.vs['label'][index], graph.vs['geocode'][index]])
            done =temp
    
    else:
        done = [[index, x, graph.vs['label'][index], graph.vs['geocode'][index]] for index, x in enumerate(weighted)]    
        temp=[]
        for index, x in enumerate(weighted):
            temp.append([index, x, graph.vs['label'][index], graph.vs['geocode'][index]])
            done =temp
            
    done = sorted(done, key=lambda data: data[1], reverse=True)
    return done


def sort_by_metric(graph, metric, name):
    peso = None
    
    if metric == "strength" or "betweenness_w":
        peso = graph.es['weight']
        peso = [0.001 if x <= 0 else x for x in peso]
    
    weighted =[]
    if metric == "strength":
        weighted =  graph.strength(weights=peso)
    else:
        # print(peso)
        weighted =  graph.betweenness(weights=peso)


    switcher = {

        "degree": [[x, graph.degree(x), graph.vs['label'][x], graph.vs['geocode'][x]] for x in range(graph.vcount())],
        "betweenness": [[x, graph.betweenness(x), graph.vs['label'][x], graph.vs['geocode'][x]] for x in range(graph.vcount())],
        "strength": [[index, x, graph.vs['label'][index], graph.vs['geocode'][index]] for index, x in enumerate(weighted)],
        "betweenness_w": [[index, x, graph.vs['label'][index], graph.vs['geocode'][index]] for index, x in enumerate(weighted)]    
    }
    

    done = switcher.get(metric)
    done = sorted(done, key=lambda data: data[1], reverse=True)

    return done




"""
    counter => Função auxialiador da função correspondence_builder,
        ela retorna a numero de aparição de n nós nos primeiros n cidades
        
    Paramentros:
        nodes => Nós da rede
        cities => lista de cidades de aparição de casos
"""

def counter(n, nodes,cities):
    count=0
    for node in nodes[:n]:
        if node in cities[:n]:
            count+=1
    
    return count



"""
    correspondence_builder => Estabele a relação entre as apariçoes de casos e nós da rede
    
    Parametros:
        cities => Lista de geocodigos de cidades extraido do DataFrame(pandas) 
        sorted_by_metric => Lista de geocodigos de cidades extraido do graph(igrap) ordenados de acordo com metrica
    
    Retorno:
        Retorna lista de correspondencia 
"""
def correspondence_builder(cities, sorted_by_metric):
    list_of_correspondence=[]
    
    for index, geocode in enumerate(cities):
        
        list_of_correspondence.append(float(counter(index+1, sorted_by_metric, cities)/(index+1)))
        
    return list_of_correspondence


"""
    mapeador function => A função cria e mapea indices de nós de acordo lista de nós ordenados pela metrica,
    criando e retornando assim o coeficiente de spearmman baseados nas listas de indices de cidades e de nós
    
    Paramentros:
        cites => DataFrame(pandas) de cidades com nomes, estados, geocodigos...
        sorted_by_metric => Matrix de nós ordenados pela metrica colunas com (indece de nó, valor de metrica, label, geocode)
        name =>  nome do ficheiro csv para guardar as duas listas
"""



def mapeador(cities, sorted_by_metrics, name):
    
    net_index=[]
    cid_index=[]
    ausentes=[]
    for index, node in enumerate(sorted_by_metrics):
        try:
            i = list(cities['Geocode']).index(node[3])
            cid_index.append(i)
            net_index.append(index)
        except:
            ausentes.append(node[3])
    
    print(f'cid : {len(cid_index)}')
    print(f'net : {len(net_index)}')
    return spearmanr(cid_index, net_index)


""" list_of_coord =>lista de tuplas de coordenadas x e y 
    label => lista de labels de legenda dos plots
    name => node do arquivo plot
"""
def graphPloter(list_of_coord, labels, name="teste"): 
    plt.clf()
    for index, coord in enumerate(list_of_coord):
        x = coord[0]
        y = coord[1]
        sper = coord[2]
        corr = "{:.8f}".format(sper[0])
        pval = "{:.8f}".format(sper[1])
        plt.plot(x, y, label=labels[index]+' sp: '+corr+' pv: '+pval, marker="1")
    
    plt.legend()
    plt.title(name)
    dirMaker('output')
    plt.savefig('output/'+name+'.png')



def indexFilter(geocodes, graph):
    index=0
    list_of_index=[]
    
    for geo in graph.vs['geocode']:
        if geo in geocodes:
            list_of_index.append(index)
            index+=1
    return list_of_index