import csv
from BeautifulSoup import BeautifulSoup
import matplotlib.pyplot as plt


def get_rate(rate_to_check):
    if rate_to_check > 25:
        return 7
    elif rate_to_check > 20:
        return 6
    elif rate_to_check > 15:
        return 5
    elif rate_to_check > 10:
        return 4
    elif rate_to_check > 5:
        return 3
    elif rate_to_check > 3:
        return 2
    elif rate_to_check > 1:
        return 1
    else:
        return 0


def get_histogram(data_to_use):
    plt.hist(data_to_use, bins=20, normed=True)
    plt.title("Unemployment Rates in the US")
    plt.xlabel("Rate")
    plt.ylabel("Counties Percent")
    plt.legend()
    plt.show()

# read info from csv
unemployment_rate_list = {}
min_value = 100
max_value = 0
csv_reader = csv.reader(open('ex2-csv-source.csv'), delimiter=",")
for row in csv_reader:
    id = row[1] + row[2]
    unemployment_rate = float(row[8].strip())
    unemployment_rate_list[id] = unemployment_rate

# define styles and US map
map_svg = open('map.svg', 'r').read()
beautiful_soup = BeautifulSoup(map_svg, selfClosingTags=['defs', 'sodipodi:namedview'])
paths = beautiful_soup.findAll('path')
colors = ["#005C02", "#00A803", "#37FF00", "#F2FF00", "#CFCB00", "#FF5900", "#FF0000", "#8F0000"]
path_style = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;' \
             'stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;' \
             'stroke-dasharray:none;stroke-linecap:butt;' \
             'marker-start:none;stroke-linejoin:bevel;fill:'

# apply styles according to the info from the csv file
data = []
for path in paths:
    if path['id'] not in ["State_Lines", "separator"]:
        try:
            unemployment_rate = unemployment_rate_list[path['id']]
        except:
            continue
        color_rate = get_rate(unemployment_rate)
        color = colors[color_rate]
        path['style'] = path_style + color
        data.append(unemployment_rate)

target = open("final_map.svg", 'w')
target.write(beautiful_soup.prettify())
target.close()

get_histogram(data)
