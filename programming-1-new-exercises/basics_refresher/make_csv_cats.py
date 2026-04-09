import csv

with open('/home/xmakaco/cimec/programming_1/programming-1-new-exercises/basics_refresher/cats_csv.csv', 'w', newline = '') as f:
    writer = csv.writer(f, delimiter = ',')
    writer.writerow(['name', 'fur_color', 'weather_at_birth'])
    writer.writerow(['bianca', 'white', 'sunny'])
    writer.writerow(['sparkle', 'tabby', 'sunny'])
    writer.writerow(['felix', 'black', 'stormy'])
    writer.writerow(['jewel', 'calico', 'sunny'])
    writer.writerow(['speedy', 'black', 'sunny'])
    writer.writerow(['garfield', 'tabby', 'sunny'])
    writer.writerow(['luna', 'black', 'stormy'])
    writer.writerow(['boots', 'calico', 'stormy'])


print("CSV written")