"""
File for implementing the Hash Table.
Also handles loading csv file of packages into hash table.
"""

# Import necessery function from standard library.
import csv

# O(n)
class Hash_Implementation:

    # Constructor with high capacity
    # Assigns empty lists to each bucket
    # O(n)
    def __init__(self, capacity=64):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # Function for inserting an item into the hash table
    # O(1)
    def hashInsert(self, id, details):
        # Inserts item and details
        bucket = hash(id) % len(self.table)
        details[0] = int(details[0])
        list_bucket = self.table[bucket]
        list_bucket.append(details)
        if details[7].startswith("Delayed"):
            details.append("DELAYED")
        else:
            details.append("HUB")


    # Function for searching the hash table
    # O(1)
    def hashSearch(self, id):
        # Locate bucket containing id
        bucket = hash(id) % len(self.table)
        list_bucket = self.table[bucket]

        # Searches for id in bucket
        for package in list_bucket:
            if package[0] == id:
                return package
        return None

    # Function for removing items from the hash table
    # O(1)
    def hashRemove(self, id):
        # Locate bucket containing id
        bucket = hash(id) % len(self.table)
        list_bucket = self.table[bucket]

        # Removes id and details from bucket if it exists
        for package in list_bucket:
            if package[0] == id:
                list_bucket.remove(id)

# Function for creating a hash table using the Hash_Implementation class
# O(n)
def hashPackage(fileName):
    hashPackages = Hash_Implementation()
    with open(fileName) as csv_document:
        csv_loader = csv.reader(csv_document)
        for row in csv_loader:
            hashPackages.hashInsert(int(row[0]), row)
    return hashPackages

# Creates a hash table using the Packages csv
packagesTable = hashPackage("Packages.csv")