"""
Interactive Fallout 76 Database Query Tool
Ask questions about your items!
"""

import sqlite3
from transformers import pipeline

def setup_ml():
    """Setup the ML model for text analysis"""
    print("Loading AI model...")
    return pipeline("sentiment-analysis")

def query_database():
    """Interactive database query tool"""
    conn = sqlite3.connect('fallout76.db')
    cursor = conn.cursor()
    
    print("\n" + "="*50)
    print("FALLOUT 76 DATABASE QUERY TOOL")
    print("="*50)
    print("\nYou can ask questions like:")
    print("  1. Show all items")
    print("  2. Show weapons")
    print("  3. Show items worth more than 50")
    print("  4. What's the most valuable item?")
    print("  5. Analyze [any text] (uses AI)")
    print("  6. Custom SQL query")
    print("  Type 'quit' to exit\n")
    
    classifier = setup_ml()
    
    while True:
        question = input("\nWhat would you like to know? > ").lower().strip()
        
        if question == 'quit':
            break
            
        # PRE-BUILT QUERIES
        elif question == '1' or 'show all' in question:
            cursor.execute("SELECT * FROM items")
            results = cursor.fetchall()
            print("\nAll Items:")
            for row in results:
                print(f"  {row[1]} ({row[2]}): {row[3]} caps")
                
        elif question == '2' or 'weapon' in question:
            cursor.execute("SELECT name, value FROM items WHERE type='Weapon'")
            results = cursor.fetchall()
            print("\nWeapons:")
            for name, value in results:
                print(f"  {name}: {value} caps")
                
        elif question == '3' or 'worth more' in question:
            cursor.execute("SELECT name, value FROM items WHERE value > 50")
            results = cursor.fetchall()
            print("\nValuable Items (>50 caps):")
            for name, value in results:
                print(f"  {name}: {value} caps")
                
        elif question == '4' or 'most valuable' in question:
            cursor.execute("SELECT name, value FROM items ORDER BY value DESC LIMIT 1")
            result = cursor.fetchone()
            print(f"\nMost Valuable: {result[0]} worth {result[1]} caps")
            
        elif question.startswith('5') or question.startswith('analyze'):
            # Use ML to analyze sentiment
            text = input("Enter text to analyze: ")
            result = classifier(text)[0]
            print(f"\nAI Analysis: {result['label']} (confidence: {result['score']:.2%})")
            
        elif question == '6' or 'sql' in question:
            # Let user write custom SQL
            print("Enter your SQL query (or 'back' to return):")
            sql = input("SQL> ")
            if sql.lower() != 'back':
                try:
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    for row in results:
                        print(row)
                except Exception as e:
                    print(f"Error: {e}")
                    
        else:
            # Try to interpret the question
            if 'how many' in question:
                cursor.execute("SELECT COUNT(*) FROM items")
                count = cursor.fetchone()[0]
                print(f"\nTotal items: {count}")
                
            elif 'average' in question:
                cursor.execute("SELECT AVG(value) FROM items")
                avg = cursor.fetchone()[0]
                print(f"\nAverage value: {avg:.0f} caps")
                
            elif 'cheapest' in question:
                cursor.execute("SELECT name, value FROM items ORDER BY value ASC LIMIT 1")
                result = cursor.fetchone()
                print(f"\nCheapest: {result[0]} worth {result[1]} caps")
                
            else:
                print("\nI don't understand that question. Try:")
                print("  - Type 1-6 for preset queries")
                print("  - Ask about 'weapons', 'most valuable', 'average', etc.")
                print("  - Type '6' to write your own SQL query")
    
    conn.close()
    print("\nGoodbye!")

if __name__ == "__main__":
    query_database()
