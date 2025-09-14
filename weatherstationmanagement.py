class WeatherRecord:
    def __init__(self, date, city, temperature):
        self.date = date
        self.city = city
        self.temperature = temperature

class WeatherStorage:
    def __init__(self, cities, dates):
        self.cities = cities
        self.dates = dates
        self.sentinel = -999.0
        # Initialize 2D array with sentinel values
        self.data = [[self.sentinel for _ in cities] for _ in dates]
        # Insert record
    def insert(self, city, date, temp):
        row = self.find_date(date)
        col = self.find_city(city)
        if row != -1 and col != -1:
            self.data[row][col] = temp
            print("Record inserted.")
        else:
            print("Invalid city or date.")
        # Delete record
    def remove(self, city, date):
        row = self.find_date(date)
        col = self.find_city(city)
        if row != -1 and col != -1:
            self.data[row][col] = self.sentinel
            print("Record deleted.")
        else:
            print("Invalid city or date.")
        # Retrieve record
    def retrieve(self, city, date):
        row = self.find_date(date)
        col = self.find_city(city)
        if row != -1 and col != -1:
            return self.data[row][col]
        return self.sentinel
    # Row-major traversal
    def row_major_access(self):
        print("\nRow-major traversal:")
        for i, date in enumerate(self.dates):
            for j, city in enumerate(self.cities):
                print(f"Date: {date}, City: {city}, Temp: {self.data[i][j]}")
    # Column-major traversal
    def column_major_access(self):
        print("\nColumn-major traversal:")
        for j, city in enumerate(self.cities):
            for i, date in enumerate(self.dates):
                print(f"Date: {date}, City: {city}, Temp: {self.data[i][j]}")
    # Handle sparse data
    def handle_sparse_data(self):
        missing = sum(
            1 for i in range(len(self.dates))
            for j in range(len(self.cities))
            if self.data[i][j] == self.sentinel
        )
        print(f"\nMissing records: {missing}")
    # Complexity analysis
    def analyze_complexity(self):
        print("\nComplexity Analysis:")
        print("Insert: O(1)")
        print("Delete: O(1)")
        print("Retrieve: O(1)")
        print("Row/Column traversal: O(m*n)")
        print("(m = dates, n = cities)")
    # Helper methods
    def find_city(self, city):
        try:
            return self.cities.index(city)
        except ValueError:
            return -1
    def find_date(self, date):
        try:
            return self.dates.index(date)
        except ValueError:
            return -1

# Demo with user input
if __name__ == "__main__":
    cities = input("Enter city names (comma separated): ").split(",")
    dates = input("Enter dates in dd/mm/yyyy format (comma separated): ").split(",")
    ws = WeatherStorage(cities, dates)
    while True:
        print("\nMenu:")
        print("1. Insert record")
        print("2. Retrieve record")
        print("3. Delete record")
        print("4. Row-major traversal")
        print("5. Column-major traversal")
        print("6. Handle sparse data")
        print("7. Complexity analysis")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            city = input("Enter city: ")
            date = input("Enter date (dd/mm/yyyy): ")
            temp = float(input("Enter temperature: "))
            ws.insert(city, date, temp)
        elif choice == "2":
            city = input("Enter city: ")
            date = input("Enter date (dd/mm/yyyy): ")
            temp = ws.retrieve(city, date)
            if temp != ws.sentinel:
                print(f"Temperature in {city} on {date}: {temp}")
            else:
                print("Record not found.")
        elif choice == "3":
            city = input("Enter city: ")
            date = input("Enter date (dd/mm/yyyy): ")
            ws.remove(city, date)
        elif choice == "4":
            ws.row_major_access()
        elif choice == "5":
            ws.column_major_access()
        elif choice == "6":
            ws.handle_sparse_data()
        elif choice == "7":
            ws.analyze_complexity()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
