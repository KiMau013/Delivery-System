"""
File for implementing a Graph function.
Also handles loading in csv file of distances for the graph.
"""

# Import necessery function from standard library.
import csv

# Creates a class for implementing a Graph data structure
# O(n^2)
class Graph_Implementation:

    # Constructor
    # Assigns empty dictionaries for graph and edge weights
    # O(1)
    def __init__(self):
        self.graphDict = {}
        self.edgeWeight = {}

    # Function for adding a vertex
    # O(1)
    def addVertex(self, vertex):
        self.graphDict[vertex] = []

    # Function for adding an Edge
    # O(1)
    def addEdge(self, vertex1, vertex2, weight=1.0):
        self.edgeWeight[(vertex1, vertex2)] = weight

    # Function for Loading a hash table into the graph dictionary
    # O(n^2)
    def vertexLoad(self, hashTable):
        for bucket in hashTable.table:
            for package in bucket:
                self.graphDict[package[1]].append(package)

# Function for loading in a csv to determine distances
# O(n)
def csvReadDistances(fileName):
    csvData = []
    with open(fileName) as csv_document:
        csv_loader = csv.reader(csv_document)
        for row in csv_loader:
            csvData.append(row)
    return csvData

# Function for loading a csv into the graph function
# O(n^2)
def csvLoadGraph(fileName):
    data = csvReadDistances(fileName)
    distances = Graph_Implementation()
    for row in data:
        distances.addVertex(row[0])
    for row in data:
         for i in range(1, len(row)):
            distances.addEdge(row[0], data[i-1][0], float(row[i]))
    return distances

# Creates usable graph from Distances csv
graph = csvLoadGraph("Distances.csv")