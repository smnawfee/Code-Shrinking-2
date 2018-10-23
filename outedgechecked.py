#import operator  
import random
import matplotlib.pyplot


agents = []
num_of_agents = 10
num_of_iterations = 100


for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
print (agents)

# move every agent num_of_iterations times...
for j in range (num_of_iterations):
    for i in range(num_of_agents):
    #change y value...    
        if random.random() < 0.5:
            agents[i][0] +=1
        else:
            agents[i][0] -=1
    #change x value...    
        if random.random() < 0.5:
            agents[i][1] +=1
        else:
            agents[i][1] -=1
    # Check if off edge and adjust.
        if agents[i][0] < 0:
            agents[i][0] = 0
        if agents[i][1] < 0:
            agents[i][0] = 0
        if agents[i][0] > 99:
            agents[i][0] = 99
        if agents[i][1] > 99:
            agents[i][0] = 99
    

#if random.random() < 0.5:
#    agents[1][0] +=1
#else:
#    agents[1][0] -=1
#    
#if random.random() < 0.5:
#    agents[1][1] +=1
#else:
#    agents[1][1] -=1
    
print (agents) 



matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#m = max(agents, key=operator.itemgetter(1))
#matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()