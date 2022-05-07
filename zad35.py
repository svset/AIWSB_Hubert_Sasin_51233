from random import randint

import numpy as np

vector1 = np.array([3, 8, 9, 10, 12])
vector2 = np.array([8, 7, 7, 5, 6])


def addVectors(vec1, vec2):
    return vec1 + vec2

def multiplyVectors(vec1, vec2):
    return vec1 * vec2


def dotProduct(vec1, vec2):
    return vec1.dot(vec2)


def euclideanLength(vec):
    return np.linalg.norm(vec)


def createVector():
    arr = []
    for elem in range(50):
        arr.append(randint(0, 100))
    return np.array(arr)


def calculateAverage():
    vector = createVector()
    return sum(vector) / len(vector)

def getMin():
    vector = createVector()
    return min(vector)

def getMax():
    vector = createVector()
    return max(vector)

def getDeviation():
    vector = createVector()
    return np.std(vector)

def normalize():
    vector = createVector()
    return (vector - np.min(vector)) / (np.max(vector) - np.min(vector))


print(addVectors(vector1, vector2))

print(multiplyVectors(vector1, vector2))

print(dotProduct(vector1, vector2))

print(euclideanLength(vector1))

print(createVector())

print(calculateAverage())
print(getMin())
print(getMax())
print(getDeviation())

print(normalize())