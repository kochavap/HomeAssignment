## Tools and Libraries
- Programming Language: Python.
- SQLite: Used to store and retrieve the information about the scrambling process.
- PIL (Python Imaging Library): Used for image manipulation and processing.

## Import statements

"helper.py" file:
```python
from PIL import Image
```
"main.py" file:
```python
from helper import *
import sqlite3
```

## Explanation:
The functionality is divided into two files: "main.py" and "helper.py". The "main.py" file imports the functions from the "helper.py" file to perform the descrambling.
In the "helper.py" file, two helper functions are defined:
- convertDataToPixels: This function takes the row data from the SQLite table and converts it into pixel positions for the source and destination tiles, returning the left, upper, right, and lower pixel coordinates for both positions.
- rearrangeSquare: This function extracts a tile from the original image, rotates it based on the provided direction, and pastes it into the new image at the specified position.

After executing the "main.py" script, the code performs the following steps:

Connects to the SQLite database using sqlite3.connect() and retrieves the table name.
Opens the scrambled image using the PIL library's Image.open() function and creates a new blank image with the same dimensions.
Iterates through each row in the SQLite table using cursor.execute().
Converts the position data to pixels using the convertDataToPixels() function from the "helper.py" file.
Rearranges the squares in the new image based on the converted positions and rotation information using the rearrangeSquare() function.
Saves the resulting descrambled image as "descrambled_image.jpg" in the same directory using the new_image.save() method.
Closes the images, the cursor and connection to the SQLite database.

To run the code, ensure that the "assignment.jpg" image and "assignment.sqlite" database file are in the same directory as the Python files. Also, make sure to have the PIL library installed.
After running the "main.py" file, the descrambled image will be generated and saved as "descrambled_image.jpg" in the same directory.


