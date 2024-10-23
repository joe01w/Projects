Plant Watering Schedule Task

This is a program that creates a 12 week plant watering schedule when given JSON data (plant name and watering frequency).

Installation Instructions: 
You can install required libraries in bash using: pip install prettytable
Ensure that the JSON file is in the same location/folder as the python file, and that the file name is correct. 

Overview:
Your task is to create an application that generates a watering schedule for the next 12
weeks for all our plants. We encourage you to be creative and present the schedule in a
way that is easy for a plant caretaker to understand. The schedule should clearly show
which plants need watering on which dates.
You are free to use any language and platform you're comfortable with. The solution can
be a User Interface (UI), command-line tool, or even a schedule written to a file—
whatever suits your style. Remember to include a README with instructions on how to
run your code, as well as any known issues or complexities. Additionally, feel free to
describe any extra features you would have liked to add.

Requirements:
• The schedule should cover the next 12 weeks, starting from next Monday.
• Plants should not be watered on Saturdays or Sundays (work-life balance!).
• Each plant has a watering frequency, and the application should generate a
schedule based on that.
• Every plant should be watered on the first day of the schedule (next Monday),
after which its specific schedule should be followed as closely as possible.
• You’ve been provided with a JSON file containing data about the plants,
including their watering frequency (in days).

For this task, I used Python, as it's the language I am most comfortable with. 
I initially juggled with a few ideas on how to output the schedule, while keeping the requirements in mind and making sure it's readable to all.
I started with the schedule being saved as an CSV file, but the formatting was a little off. 
Then I tried to output the schedule as a list of dates in the terminal, which worked, but wasn't very easy to read.
After some research, and some digging through my own python work, I eventually settled on using PrettyTable.
This is a python package that prints tables in a very organised, aesthetic and legible way. This is the method I settled on.
The date format is ISO standard date format, but I could alter this to display a day of the week if this helped legibility.
