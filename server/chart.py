import matplotlib.pyplot as plt

def make_chart(data):
	x, y = [], []
	for i in data:
		x.append(i[0])
		y.append(i[1])

	plt.plot(x, y)
	plt.ylabel("Lumiere", fontsize=18)
	plt.xlabel("Temps", fontsize=16)
 	#plt.show()
 	plt.savefig("static/chart.png")

