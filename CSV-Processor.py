import csv

all_fild = []
with open("products.csv", mode="r") as file:
    rieder = csv.DictReader(file)
    for lines in rieder:
                Price = int(lines['Price'])
                Quantity = int(lines['Quantity'])
                lines['total'] = Price * Quantity
                all_fild.append(lines)
             
with open("outfail.csv", mode='w', newline='') as outfail:
            write = csv.DictWriter(outfail, fieldnames=all_fild[0])
            write.writeheader()
            write.writerows(all_fild)
