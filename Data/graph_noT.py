import matplotlib.pyplot as plt
import pandas
import bokeh.layouts as layouts
from bokeh.plotting import figure, show, output_file, save

#replace file path as necessary,
df = pandas.read_csv(r'NCSR1412.CSV', names=['Time(s)', 'V1', 'V2', 'V3', '�C'])

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

p = figure(title = 'Negative Controls', x_axis_label = "time(s)", y_axis_label="E.M.F.(V)", x_range=(0, 11300), y_range=(0, 1), sizing_mode="scale_both", tooltips = Tooltips)

p.line('Time(s)', 'V1', source = source1, color = "green", legend_label = "Plastic", name='Plastic (from Ziploc bag)')
p.line('Time(s)', 'V2', source = source2, color = "red", legend_label = "Aluminium Foil", name = "Aluminium Foil")
p.line('Time(s)', 'V3', source = source3, color = "blue", legend_label = "Filter Paper", name = "Filter Paper")
#p.line('Time(s)', 'Vavg', source = source4, color = "black", legend_label = "Average", name = "Average")
p.legend.location = "top_right"
p.legend.click_policy = "hide"

#p1 = figure(title = 'Temperature', x_axis_label = "time(s)", y_axis_label="Temperature (�C)", x_range=(0, 86400), y_range=(18, 25), sizing_mode="scale_both", tooltips = Tooltips)
#p1.line('Time(s)', '�C', color = 'black', source = source5)

output_file(filename="NegativeControls.html", title="NCSR1412.CSV, 14/12/2022")
#show(layouts.row(children = [p, p1], sizing_mode = "scale_both"))
#save(layouts.row(children = [p, p1], sizing_mode = "scale_both"))
show(p, sizing_mode = "scale_height")
save(p)