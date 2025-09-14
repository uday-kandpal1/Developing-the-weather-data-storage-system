Report: Weather Record ADT System
1. Description of the Weather Record ADT

The Weather Record Abstract Data Type (ADT) is a logical representation of weather information for a given city and date.

Attributes:

date: It represents the date in dd/mm/yyyy format.

city: Name of the city where the temperature is recorded.

temperature: It is a floating-point number storing the temperature value.

Operations (Methods):

insert(city, date, temp): Add a temperature record for a specific city on a specific date.

remove(city, date): Delete a record (set it back to a sentinel value).

retrieve(city, date): Get the temperature for a given city and date.

row_major_access(): It Traverses the 2D structure row by row (date → cities).

column_major_access(): It traverse the 2D structure column by column (city → dates).

handle_sparse_data(): Identify and handle missing or unrecorded data.

analyze_complexity(): Provide theoretical time and space complexity of operations.

2. Strategy for Memory Representation (Row-Major vs. Column-Major)

The system uses a 2D array (list of lists in Python) where:

Rows correspond to dates.

Columns correspond to cities.

Thus, each entry data[row][col] represents the temperature of city col on date row.

Row-Major Traversal (Python default)

Row major traversal accesses elements row by row.

It is good for analyzing one date across all cities.

It is cache-friendly in Python since lists are stored row-contiguously.

Column-Major Traversal

It accesses elements column by column.

It is Good for analyzing one city across all dates.

It is less efficient in Python but useful for city-wise historical analysis.

3. Approach to Handling Sparse Data

Sparse data occurs when not all date–city combinations have recorded values.

Sentinel Value Approach (used here):

Missing values are stored as -999.0.

Easy to implement, memory-efficient, and allows fast checks for missing data.

4. Time and Space Complexity Analysis

Operation              Time Complexity	Explanation

Insert	               O(1)	            Direct index access (row & column lookup + assignment).

Delete	               O(1)	            Direct index access, replaced with sentinel.

Retrieve            	 O(1)	            Direct index access (row & column lookup + retrieval).

Row-Major Traversal 	 O(m × n)        	Must visit each entry (m = number of dates, n = number of cities).

Column-Major Traversal O(m × n)        	Must visit each entry.

Handle Sparse Data	   O(m × n)	        Must scan the entire 2D array to count missing records.

Space Complexity	     O(m × n)	        2D list of size (dates × cities).

Summary:

The Weather Record ADT provides a structured way to insert, delete, and retrieve temperature records efficiently.

Row-major traversal is cache-friendly in Python and best for date-wise queries, while column-major traversal is more suited for city-wise historical data.

Sparse data is managed with a sentinel value approach, though a dictionary-based method would be more memory-efficient in extremely sparse datasets.

In this program , insert, delete, and retrieve functions are constant time (O(1)), while traversal and sparse checks are O(m × n).
