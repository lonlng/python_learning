topHitters={"Gehrig":{"atBats":8061,"hits":2721},"Ruth":{"atBats":8399,"hits":2873},"Willams":{"atBats":7706,"hits":2654}}
print(topHitters['Gehrig']['hits']/topHitters['Gehrig']['atBats'])
print(topHitters['Ruth']['hits']/topHitters['Ruth']['atBats'])
print(topHitters['Willams']['hits']/topHitters['Willams']['atBats'])

print((topHitters['Gehrig']['hits']+topHitters['Ruth']['hits']+topHitters['Willams']['hits'])/3)
print("max")
if topHitters['Gehrig']['hits']>topHitters['Ruth']['hits']and topHitters['Ruth']['hits'] >topHitters['Willams']['hits']:
    print(topHitters['Gehrig']['hits'])
elif topHitters['Ruth']['hits']>topHitters['Gehrig']['hits']and topHitters['Ruth']['hits']>topHitters['Willams']['hits']:
    print(topHitters['Ruth']['hits'])
else:
    print(topHitters['Willams']['hits'])
