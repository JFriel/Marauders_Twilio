from redis import Redis
r = Redis()



#listofMachines = r.lrange("drillhall-machines",0,-1)
#listofRowsColumns = r.hgetall("drillhall")
listOfMachines = [[{'hostname': 'pipit', 'col': '0', 'row': '0'}, {'hostname': 'giudicelli', 'col': '1', 'row': '0'}, {'hostname': 'crow', 'col': '2', 'row': '0'}, {'hostname': 'courfeyrac', 'col': '3', 'row': '0'}, {'hostname': 'joly', 'col': '4', 'row': '0'}, {'hostname': 'angelotti', 'col': '5', 'row': '0'}, {'hostname': 'velletri', 'col': '6', 'row': '0'}, {'hostname': 'pontremoli', 'col': '7', 'row': '0'}, {'hostname': 'morales', 'col': '8', 'row': '0'}, {'hostname': 'avellino', 'col': '9', 'row': '0'}, {'hostname': 'velma', 'col': '10', 'row': '0'}, {'hostname': 'vicenza', 'col': '11', 'row': '0'}, {'hostname': 'savona', 'col': '12', 'row': '0'}, {'hostname': 'giry', 'col': '13', 'row': '0'}, {'hostname': 'scarecrow', 'col': '14', 'row': '0'}, {'hostname': 'dove', 'col': '15', 'row': '0'}], [{'hostname': 'bluthner', 'col': '4', 'row': '1'}, {'hostname': 'mocha', 'col': '5', 'row': '1'}, {'hostname': 'bechstein', 'col': '6', 'row': '1'}, {'hostname': 'ravenna', 'col': '7', 'row': '1'}, {'hostname': 'palestrina', 'col': '8', 'row': '1'}, {'hostname': 'pollenzo', 'col': '9', 'row': '1'}, {'hostname': 'zoser', 'col': '10', 'row': '1'}, {'hostname': 'thenardier', 'col': '11', 'row': '1'}, {'hostname': 'frosch', 'col': '12', 'row': '1'}, {'hostname': 'aida', 'col': '13', 'row': '1'}, {'hostname': 'gabriel', 'col': '14', 'row': '1'}, {'hostname': 'rosilande', 'col': '15', 'row': '1'}], [{'hostname': 'messina', 'col': '0', 'row': '2'}, {'hostname': 'carmen', 'col': '1', 'row': '2'}, {'hostname': 'parma', 'col': '2', 'row': '2'}, {'hostname': 'nehebka', 'col': '3', 'row': '2'}, {'hostname': 'enjolras', 'col': '4', 'row': '2'}, {'hostname': 'spoletta', 'col': '5', 'row': '2'}, {'hostname': 'tosca', 'col': '6', 'row': '2'}, {'hostname': 'montparnarsse', 'col': '7', 'row': '2'}, {'hostname': 'claquesous', 'col': '8', 'row': '2'}, {'hostname': 'yvan', 'col': '9', 'row': '2'}, {'hostname': 'allonby', 'col': '10', 'row': '2'}, {'hostname': 'ostiglia', 'col': '11', 'row': '2'}, {'hostname': 'seascale', 'col': '12', 'row': '2'}, {'hostname': 'lowick', 'col': '13', 'row': '2'}, {'hostname': 'danicaire', 'col': '14', 'row': '2'}, {'hostname': 'ceilingcat', 'col': '15', 'row': '2'}], [{'hostname': 'amanasro', 'col': '4', 'row': '3'}, {'hostname': 'babet', 'col': '8', 'row': '3'}, {'hostname': 'amneris', 'col': '9', 'row': '3'}, {'hostname': 'cavaradossi', 'col': '10', 'row': '3'}, {'hostname': 'scarpia', 'col': '11', 'row': '3'}, {'hostname': 'falke', 'col': '12', 'row': '3'}, {'hostname': 'palermo', 'col': '13', 'row': '3'}, {'hostname': 'luni', 'col': '14', 'row': '3'}, {'hostname': 'lodi', 'col': '15', 'row': '3'}], [{'hostname': 'penguin', 'col': '1', 'row': '4'}, {'hostname': 'owl', 'col': '3', 'row': '4'}, {'hostname': 'daae', 'col': '4', 'row': '4'}, {'hostname': 'goro', 'col': '5', 'row': '4'}, {'hostname': 'lesgles', 'col': '6', 'row': '4'}, {'hostname': 'yakuside', 'col': '7', 'row': '4'}, {'hostname': 'roxanne', 'col': '8', 'row': '4'}, {'hostname': 'lilas', 'col': '10', 'row': '4'}, {'hostname': 'ciociosan', 'col': '11', 'row': '4'}, {'hostname': 'raven', 'col': '12', 'row': '4'}, {'hostname': 'falcon', 'col': '13', 'row': '4'}, {'hostname': 'wigton', 'col': '14', 'row': '4'}, {'hostname': 'parrot', 'col': '15', 'row': '4'}], [{'hostname': 'amelia', 'col': '4', 'row': '5'}, {'hostname': 'falconara', 'col': '5', 'row': '5'}, {'hostname': 'spoleto', 'col': '6', 'row': '5'}, {'hostname': 'mantua', 'col': '7', 'row': '5'}, {'hostname': 'marsala', 'col': '8', 'row': '5'}, {'hostname': 'lavello', 'col': '9', 'row': '5'}, {'hostname': 'micaela', 'col': '10', 'row': '5'}, {'hostname': 'escamillo', 'col': '11', 'row': '5'}, {'hostname': 'remendado', 'col': '12', 'row': '5'}, {'hostname': 'combeferre', 'col': '13', 'row': '5'}, {'hostname': 'pharoah', 'col': '14', 'row': '5'}, {'hostname': 'brujon', 'col': '15', 'row': '5'}], [{'hostname': 'stork', 'col': '1', 'row': '6'}, {'hostname': 'hart', 'col': '2', 'row': '6'}, {'hostname': 'albenga', 'col': '3', 'row': '6'}, {'hostname': 'gosforth', 'col': '5', 'row': '6'}, {'hostname': 'enna', 'col': '6', 'row': '6'}, {'hostname': 'swanland', 'col': '7', 'row': '6'}, {'hostname': 'twite', 'col': '8', 'row': '6'}, {'hostname': 'wideopen', 'col': '9', 'row': '6'}, {'hostname': 'tivoli', 'col': '10', 'row': '6'}, {'hostname': 'ascoli', 'col': '11', 'row': '6'}, {'hostname': 'vervecelli', 'col': '12', 'row': '6'}, {'hostname': 'radames', 'col': '13', 'row': '6'}, {'hostname': 'mereb', 'col': '14', 'row': '6'}, {'hostname': 'orlofsky', 'col': '15', 'row': '6'}], [{'hostname': 'pavia', 'col': '4', 'row': '7'}, {'hostname': 'trento', 'col': '5', 'row': '7'}, {'hostname': 'venosa', 'col': '6', 'row': '7'}]]

while(len(listofMachines)% 15 != 0):
    listofMachines.append("no_Machine")


def genTable():
    labtable = [[]]
    for i in range(0,6):
        for j in range(0,14):
            labtable[i][j] = listofMachines[(i*15)+j]
    print(listofMachines)
    return labtable

print(genTable())