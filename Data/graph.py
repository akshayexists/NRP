import matplotlib.pyplot as plt
import pandas
import bokeh.layouts as layouts
from bokeh.plotting import figure, show, output_file, save

inputPath = r'Cellophane\Raw\CLX21312.CSV'
names=['Time(s)', 'V1', 'V2', 'V3', 'Vavg', '�C']
df = pandas.read_csv(inputPath, names= names)
outputPath = "Cellophane\Graph\CellophaneDouble_Run1.html"
Title = inputPath.split("\\")[2]+", 13/12/2022"
source1=df
source2=df
source3=df
source4=df
source5=df

Tooltips = [
    ("index", "$index"),
    ("MFC", "$name"),
    ("Time (s)", "$x"),
    ("E.M.F (V)", "$y")
]

p = figure(title = 'Cellophane Double', x_axis_label = "time(s)", y_axis_label="E.M.F.(V)", x_range=(0, 86400), y_range=(0, 1), sizing_mode="scale_both", tooltips = Tooltips)

p.line('Time(s)', 'V1', source = df, color = "green", legend_label = "MFC1", name='MFC1', line_width = 3)
p.line('Time(s)', 'V2', source = df, color = "red", legend_label = "MFC2", name = "MFC2", line_width = 3)
p.line('Time(s)', 'V3', source = df, color = "blue", legend_label = "MFC3", name = "MFC3", line_width = 3)
p.line('Time(s)', 'Vavg', source = df, color = "black", legend_label = "Average", name = "Average", line_width = 3)
p.legend.location = "top_right"
p.legend.click_policy = "hide"

p1 = figure(title = 'Temperature', x_axis_label = "time(s)", y_axis_label="Temperature (�C)", x_range=(0, 86400), y_range=(18, 25), sizing_mode="scale_both", tooltips = Tooltips)
p1.line('Time(s)', '�C', color = 'black', source = df) 

output_file(filename=outputPath, title=Title)
#save(p)
save(layouts.row(children = [p, p1], sizing_mode = "scale_both"))