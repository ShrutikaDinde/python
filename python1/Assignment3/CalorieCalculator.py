import tkinter as tk
from tkinter import ttk

# Sample food data, you can expand this or load it from a file
food_data = {
    "protein shake": {"calories": 262, "carbs": 12, "fats": 6, "protein": 40},
    "sprouts": {"calories": 152, "carbs": 13, "fats": 8, "protein": 7},
    "banana": {"calories": 96, "carbs": 23, "fats": 0, "protein": 1},
    "nuts": {"calories": 105, "carbs": 3, "fats": 9, "protein": 3},
    "ice cream": {"calories": 195, "carbs": 21, "fats": 11, "protein": 3},
    # Add more items as needed
}

class CalorieCalculator:
    def _init_(self, root):
        self.root = root
        self.root.title("Calorie Calculator")
        self.calorie_limit = 2000
        self.total_calories = 0
        
        # Set up the interface
        self.setup_ui()

    def setup_ui(self):
        # Calorie Limit and Total
        self.calorie_label = tk.Label(self.root, text=f"Calorie Limit: {self.calorie_limit}")
        self.calorie_label.pack()

        self.total_calories_label = tk.Label(self.root, text=f"Total Calories Consumed: {self.total_calories}")
        self.total_calories_label.pack()

        self.remaining_calories_label = tk.Label(self.root, text=f"Remaining: {self.calorie_limit - self.total_calories}")
        self.remaining_calories_label.pack()
        
        # Search and Add Food Item
        self.search_label = tk.Label(self.root, text="Search Food Item:")
        self.search_label.pack()

        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()

        self.search_button = tk.Button(self.root, text="Search", command=self.search_food)
        self.search_button.pack()

        # Display Food Tracker Table
        columns = ("fooditem", "calories", "carbs", "fats", "protein")
        self.food_table = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.food_table.heading(col, text=col.capitalize())
        self.food_table.pack()

    def search_food(self):
        food_item = self.search_entry.get().lower()
        if food_item in food_data:
            # Add food item to the tracker
            self.add_food(food_item)
        else:
            tk.messagebox.showinfo("Not Found", "Food item not found in the database.")

    def add_food(self, food_item):
        item_data = food_data[food_item]
        self.food_table.insert("", "end", values=(food_item, item_data["calories"], item_data["carbs"],
                                                  item_data["fats"], item_data["protein"]))
        
        # Update total calories and labels
        self.total_calories += item_data["calories"]
        self.total_calories_label.config(text=f"Total Calories Consumed: {self.total_calories}")
        self.remaining_calories_label.config(text=f"Remaining: {self.calorie_limit - self.total_calories}")

# Main application
root = tk.Tk()
app = CalorieCalculator(root)
root.mainloop()