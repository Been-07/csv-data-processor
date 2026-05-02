


import csv



def formol(data,outfail='outfail.csv'):
        all_fild = []
        rieder = csv.DictReader(data)
        for lines in rieder:
            try:
                Price = int(lines['Price'])
                Quantity = int(lines['Quantity'])
                lines['total'] = Price * Quantity
                all_fild.append(lines)
            except(ValueError,KeyError) as Error:
                 print(f"Error processing row: {Error}")
                 continue
            
        if all_fild:    
            with open(outfail, mode='w', newline='') as outfail:
                write = csv.DictWriter(outfail, fieldnames=all_fild[0])
                write.writeheader()
                write.writerows(all_fild)
        else:
                 print("No data available")

def main():
    masir = input("Enter the address of the desired file, otherwise enter 0 to use the default file : ").strip()
    if masir =="0":
        with open("products.csv", mode="r") as file:
                formol(file)
    else:
        try:
            with open(masir, 'r') as file:
                formol(file)
        except FileNotFoundError:
            print(f"File '{masir}' not found!")
        except Exception as e:
            print(f"Error: {e}")



if __name__ == "__main__":
     main()
