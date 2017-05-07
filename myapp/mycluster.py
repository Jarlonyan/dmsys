#coding:utf-8

from sklean.cluster import KMeans
from sklean.externals import joblib
import numpy

def clustering():
	X=numpy.loadtxt("data.txt")
	k=2
	model=Kmeans(n_clusters=k)
	model.fit(X)
	label=model.lables_