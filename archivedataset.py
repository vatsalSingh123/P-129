import csv

#opening dataset file in read mode and appending into data list variable
data=[]
with open("archive_dataset.csv","r")as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        data.append(i)
       
# extracting colomun names into header variables and rows data into planet_data variable
headers = data[0]
planet_data = data[1:]

#converting planet names to lower case
for i in planet_data:
    i[2] = i[2].lower()
    
# sorting the planet data
planet_data.sort(key = lambda planet_data:planet_data[2])

# creating a new csv  of sorted planet data in writing mode
with open("archive_dataset_sorted.csv","a+")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

#removing blank line from new csv
with open("archive_dataset_sorted.csv")as input,open("archive_dataset_sorted1.csv",'w',newline='')as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row): 
            writer.writerow(row)

    
