# från uppgiften Scourgify från CS50
import csv, sys

def main():
    if valid_input():
        convert()

def convert():

    try:
        #opening before file in read mode
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            # opening after file in write mode
            with open(sys.argv[2], "w") as output:
                # set order of output
                writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
                writer.writeheader()
                # reads each row in before file and writes it to after file converted
                for row in reader:
                    last, first = row["name"].split(",")
                    writer.writerow({"first": first.strip(), "last": last.strip(), "house": row["house"]})

    except FileNotFoundError:
        sys.exit("File does not exist")


def valid_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" in sys.argv[1] and ".csv" in sys.argv[2]:
        return True
    else:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
