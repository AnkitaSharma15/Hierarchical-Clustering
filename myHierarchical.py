# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 00:20:22 2017

@author: erank
"""

import numpy as np


pointsDistance = []
def my_hierarchical(dist, data, cluster):
    #return minx,miny

    
    [minx,miny]= np.unravel_index(dist.argmin(),dist.shape)
    
    #node1 node 2
    n1= cluster[minx]
    n2= cluster[miny]
    
    nodeNew = ([n1, n2])
    del(cluster[minx])
    del(cluster[miny-1])
    cluster.insert(minx,nodeNew )
    pointsDistance.append(np.min(dist.min()))
    pointsNode=np.delete(dist,(miny), axis=0)
    pointsNode=np.delete(pointsNode,(miny), axis=1 )
    
    for i in range(pointsNode.shape[0]):
        pointsNode[minx,i]=np.min([dist[i,minx], dist[i,miny]])
        pointsNode[i,minx]=pointsNode[minx,i]
        pointsNode[i,i]=10000000
    
    if(pointsNode.shape[0]>1):
        my_hierarchical(pointsNode,data,cluster)
    else:
        print(pointsNode)
        print("Clusters are  %s"%cluster)
    

def main():
    dataset=np.genfromtxt("C:\\Users\\erank\\OneDrive\\Documents\\sample.csv",delimiter=",")
    data=dataset[1:,1:]
    print(data)
    
    zeros_array=np.zeros([data.shape[0],data.shape[0]])
    for i in range(data.shape[0]):
        for j in range(data.shape[0]):
            print(np.linalg.norm(data[i,:] - data[j,:]))
            zeros_array[i,j] = np.linalg.norm(data[i,:]-data[j,:])
            if(i==j):
                zeros_array[i,j]=10000000
    print(zeros_array)
    attributes = range(data.shape[0])
    my_hierarchical(zeros_array, data, attributes)
   
        
if __name__ == '__main__':
    main()
