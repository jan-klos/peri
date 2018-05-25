import matplotlib.pyplot as plt
import os

chart_path = "/home/komp/peri/server/static/chart.png"

def make_chart(data):
	x, y = [], []
	j = 0
	for i in data:
		y.append(i[0])
		x.append(j)
		j += 1

	plt.plot(x, y)
	plt.ylabel("Luminosity", fontsize=18)
	plt.xlabel("Temps", fontsize=16)
	print "dupa"
	#if os.path.isfile(chart_path):
 	os.remove(chart_path)
 	plt.savefig(chart_path)

