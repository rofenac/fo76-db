"""
Simple all-in-one script for IS 330 Assignment
This does everything you need in one file!
"""

import sqlite3
from transformers import pipeline

print("="*50)
print("FALLOUT 76 DATABASE PROJECT - IS 330")
print("="*50)

# PART 1: Test a simple ML model from HuggingFace
print("\n1. Testing HuggingFace Model...")
try:
    # This loads a tiny sentiment analysis model
    classifier = pipeline("sentiment-analysis")
    result = classifier("Fallout 76 is a fun game!")
    print(f"   ✓ Model works! Result: {result[0]['label']}")
except:
    print("   Note: Model download might take a minute on first run")

# PART 2: Create a simple database
print("\n2. Creating Database...")
conn = sqlite3.connect('fallout76.db')
cursor = conn.cursor()

# Create a simple table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY,
        name TEXT,
        type TEXT,
        value INTEGER
    )
''')

# PART 3: Add some Fallout 76 data
print("\n3. Adding Fallout 76 Items...")
items = [
    ('Stimpak', 'Medicine', 25),
    ('10mm Pistol', 'Weapon', 50),
    ('Combat Armor', 'Armor', 100),
    ('Nuka Cola', 'Drink', 10),
    ('Laser Rifle', 'Weapon', 175)
]

cursor.execute("DELETE FROM items")  # Clear old data
cursor.executemany("INSERT INTO items (name, type, value) VALUES (?, ?, ?)", items)
conn.commit()
print(f"   ✓ Added {len(items)} items")

# PART 4: Answer an interesting question about the data
print("\n4. Answering Questions About Data...")
print("\n   Question: What are the most valuable items?")
cursor.execute("SELECT name, type, value FROM items ORDER BY value DESC")
results = cursor.fetchall()

print("\n   Top Items by Value:")
for name, item_type, value in results:
    print(f"   - {name} ({item_type}): {value} caps")

# Question 2
cursor.execute("SELECT type, AVG(value) FROM items GROUP BY type")
results = cursor.fetchall()
print("\n   Average Value by Type:")
for item_type, avg_value in results:
    print(f"   - {item_type}: {avg_value:.0f} caps")

conn.close()

print("\n" + "="*50)
print("✓ ASSIGNMENT COMPLETE!")
print("Database saved as: fallout76.db")
print("="*50)
