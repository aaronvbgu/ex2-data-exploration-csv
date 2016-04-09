EX2: Data exploration from a CSV file
=====================================

In this assignment I've chosen to explore the unemployment rate in US counties.
I've found the data online and used python in order to generate maps/graphs.

Dependencies
------------
  1. CSV Library
  2. Beautiful Soup Library
  3. Matplotlib Library


Steps
-----
  * Read the data from the csv file:
  
    ```python
    csv_reader = csv.reader(open('csv-source.csv'), delimiter=",")
    for row in csv_reader:
        id = row[1] + row[2]
        unemployment_rate = float(row[8].strip())
        unemployment_rate_list[id] = unemployment_rate
    ```

  * Define styles and map

  * Apply styles and generate map + histogram graph:
  
    ```python
    color_rate = get_rate(unemployment_rate)
    color = colors[color_rate]
    path['style'] = path_style + color
    data.append(unemployment_rate)
    target = open("final_map.svg", 'w')
    target.write(beautiful_soup.prettify())
    target.close()
    get_histogram(data)
    ```
  
  * Map and Graph functions:
  ```python
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
  ```
  
  ```python
  plt.hist(data_to_use, bins=20, normed=True)
  plt.title("Unemployment Rates in the US")
  plt.xlabel("Rate")
  plt.ylabel("Counties Percent")
  plt.legend()
  plt.show()
  ```
  
Results
-------

![Map](https://s3-eu-west-1.amazonaws.com/s3.mediafileserver.co.uk/carnation/WebFiles/RecipeImages/classicbanoffeepie_lg.jpg)


We can see that in most counties, the rate is about 7.5, which is pretty normal.
The problematic areas with a very high rate are:
This is not very surprising because those areas are known for...