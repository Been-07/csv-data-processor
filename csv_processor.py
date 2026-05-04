# ======================================|
# Author: Benjamin Shojaee              |
# GitHub: https://github.com/Been-07    |
# ORCID: 0009-0005-2756-7140            |
# ======================================|
import csv
import os

def get_next_outfail(base = "outfail"):
     counter = 1
     while True:
          fail_name = f"{base}_{counter}.csv"
          if not os.path.exists(fail_name):
               return fail_name
          counter +=1

def formol(data,outfail):
        all_fild = []
        rieder = csv.DictReader(data)
        print(rieder.fieldnames)
        value_price = input("Enter the name of the price column (e.g. price or unit_price): ")
        value_quantity = input("Enter the name of the number column (e.g. quantity or count): ")
        for lines in rieder:
            try:

                Price = int(lines[value_price])
                Quantity = int(lines[value_quantity])
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
            print(f"Seve to {outfail}")
            return True
        else:
            print("No data available")
            return False

def get_failname():
    while True:
        print("=" * 130)
        print("Enter the address of the desired file, otherwise enter 0 to use the default file (products.csv) or type exit to exit the program".center(130))
        print("=" * 130)
        address_user = input("\nPlease enter the address (for exit: exit, for default address: 0): ").strip().capitalize()
        if address_user == "Exit":
            return None
        if address_user == "0":
            file_name = "products.csv"
        else:
            file_name = address_user

        if os.path.exists(file_name):
            return file_name
        else:
            print(f"File{file_name} not found, try again")
                        
def main():
    print("=" * 130)
    print("CSV-Data-Processor".center(130))
    print("Calculates Price × Quantity = Total".center(130))
    print("=" * 130)
    counter = 1
    while True:
        print(f"--- Processing Session_{counter} ---".center(130))
        deta = get_failname()
        if deta is None:
            print("bye bye")
            break
        outfail = get_next_outfail()
        print(f"File saved with name {outfail}")
        try:
            with open(deta,mode="r") as file:
                formol(file,outfail)
        except Exception as error:
            print(f"Error File: {error}")
        counter += 1
        print("\n" + "-" * 100)
        again = input("Do you want to process another file? (Yes/No): ").strip().lower()
        if again != "yes":
            print("bye bye")
            break



if __name__ == "__main__":
    main()
