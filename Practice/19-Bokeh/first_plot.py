from bokeh.plotting import figure
from bokeh.io import output_file, show

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9 ,10]

output_file("Linegraph.html")

f = figure()

f.line(x, y)

show(f)