import matplotlib.pyplot as plt
import numpy as np

# DATA ------------------------------------------------------
years = ["2010", "2011", "2012", "2013", "2014",
         "2015", "2016", "2017", "2018", "2019"]

level1 = np.random.rand(10) * 100
level2 = np.random.rand(10) * 200 + 100
level3 = np.random.rand(10) * 300 + 200
level4 = np.random.rand(10) * 400 + 300
level5 = np.random.rand(10) * 500 + 400

# Graphs ---------------------------------------------------

# Line graph (default)
# ----------------------------------------------------------------------------------------------------------------------
plt.plot(years, level1, label="level1", color="red", marker="<", linestyle="-")
plt.plot(years, level2, label="level2", color="blue", marker="*", linestyle="--")
plt.plot(years, level3, label="level3", color="green", marker="^", linestyle=":")
plt.plot(years, level4, label="level4", color="pink", marker=".", linestyle="-.")
plt.plot(years, level5, label="level5", color="black", marker="+", linestyle=" ")
# Activate legends
plt.legend()
# Graph title
plt.title("Examen de Certificacion")
# Labels of axis
plt.xlabel("Años que se ha realizado el examen")
plt.ylabel("Puntaje obtenido")
# Y axis limits
plt.yticks(np.arange(0, 1001, 50))
# Show grid
plt.grid()
plt.minorticks_on()

# plt.show()    # Uncomment to show the graph

# Vertical bar graph
# ----------------------------------------------------------------------------------------------------------------------
plt.clf()
eje_x = np.arange(0, 10)

plt.bar(eje_x, level5, width=1/5)
plt.bar(eje_x + 0.2, level4, width=1/5)
plt.bar(eje_x + 0.4, level3, width=1/5)
plt.bar(eje_x + 0.6, level2, width=1/5)
plt.bar(eje_x + 0.8, level1, width=1/5)

# plt.show()    # Uncomment to show the graph

# Horizontal bar graph
# ----------------------------------------------------------------------------------------------------------------------
plt.clf()
plt.barh(eje_x+0.8, level5, height=1/5)
plt.barh(eje_x+0.6, level4, height=1/5)
plt.barh(eje_x+0.4, level3, height=1/5)
plt.barh(eje_x+0.2, level2, height=1/5)
plt.barh(eje_x, level1, height=1/5)

# plt.show()    # Uncomment to show the graph

# Stacked bar graph
# ----------------------------------------------------------------------------------------------------------------------
plt.clf()
plt.bar(eje_x, level5)
plt.bar(eje_x, level4, bottom=level5)
plt.bar(eje_x, level3, bottom=level4+level5)
plt.bar(eje_x, level2, bottom=level3+level4+level5)
plt.bar(eje_x, level1, bottom=level2+level3+level4+level5)

# plt.show()    # Uncomment to show the graph

# Scatter plot
# ----------------------------------------------------------------------------------------------------------------------
plt.clf()
plt.scatter(eje_x, level1, marker="*")
plt.scatter(eje_x, level2, marker=".")
plt.scatter(eje_x, level3, marker="^")
plt.scatter(eje_x, level4, marker="v")
plt.scatter(eje_x, level5, marker=">")

# plt.show()    # Uncomment to show the graph

# Pie chart
# ----------------------------------------------------------------------------------------------------------------------
plt.clf()
plt.pie(level1,
        labels=["México", "Colombia", "Perú", "Chile", "Argentina",
                "Ecuador", "Bolivia", "Venezuela", "Uruguay", "Paraguay"])
# plt.show()    # Uncomment to show the graph

# Combined graphs
# ----------------------------------------------------------------------------------------------------------------------
plt.clf()

plt.bar(eje_x, level1, width=1/5)
plt.bar(eje_x + 0.2, level2, width=1/5)

plt.plot(years, level3)

plt.scatter(eje_x, level4)
plt.scatter(eje_x, level5)

# plt.show()    # Uncomment to show the graph
