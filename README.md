## Project Description
I built a database to store and analyze Fallout 76 game items. The project uses machine learning to analyze text and a SQL database to store game data.

## What I Built
- A SQLite database containing Fallout 76 items (weapons, armor, consumables)
- A Python script that analyzes the data
- Integration with HuggingFace AI models for text analysis

## Technologies Used
- **Database:** SQLite
- **Programming Language:** Python 3
- **ML Framework:** HuggingFace Transformers
- **Development Environment:** VSCode on WSL Ubuntu

## How to Run

1. Clone this repository:
```bash
git clone https://github.com/[your-username]/fo76-db.git
cd fo76-db
```

2. Set up Python environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install transformers torch pandas
```

4. Run the program:
```bash
python assignment_complete.py
```

## What the Program Does

1. **Tests Machine Learning:** Uses HuggingFace's sentiment analysis to analyze game-related text
2. **Creates Database:** Sets up a SQLite database with a table for game items
3. **Loads Data:** Adds Fallout 76 items (Stimpak, 10mm Pistol, Combat Armor, etc.)
4. **Analyzes Data:** Answers questions like:
   - What are the most valuable items?
   - What's the average value by item type?

## Sample Output
```
Top Items by Value:
- Laser Rifle (Weapon): 175 caps
- Combat Armor (Armor): 100 caps
- 10mm Pistol (Weapon): 50 caps
- Stimpak (Medicine): 25 caps
- Nuka Cola (Drink): 10 caps
```

## Files in This Project
- `assignment_complete.py` - Main Python script
- `fallout76.db` - SQLite database (created when you run the script)
- `README.md` - This file
- `.gitignore` - Tells Git what files to ignore

## Development Log

### Week 1
- **Day 1:** Set up GitHub repository
- **Day 2:** Configured VSCode with GitHub Copilot
- **Day 3:** Created Python virtual environment on WSL
- **Day 4:** Successfully tested HuggingFace sentiment analysis model
- **Day 5:** Implemented SQLite database with items table
- **Day 6:** Added Fallout 76 game data
- **Day 7:** Created data analysis queries

### Week 2
- **Day 8:** Tested all functionality
- **Day 9:** Documented project in README
- **Day 10:** Submitted assignment

## Data Source
Initial data is hard-coded based on Fallout 76 wiki information. Future versions will scrape data from:
- Fallout Wiki
- Game databases
- Community resources

## Future Improvements
- Add more items to the database
- Create a web scraper for automatic updates
- Build a recommendation system for players
- Add more complex ML models for price prediction

## What I Learned
- How to set up a Python development environment
- How to use pre-trained ML models from HuggingFace  
- How to create and query SQL databases
- How to manage code with Git and GitHub
- How to use AI tools (GitHub Copilot) for development

## Challenges Overcome
- Learning to use WSL and virtual environments
- Understanding database concepts
- Getting HuggingFace models to work
- Managing Python package installations

## Assignment Requirements Met ✓
- [x] Set up AI-powered development environment (VSCode + Copilot)
- [x] Created GitHub repository
- [x] Tested ML model from HuggingFace
- [x] Installed database system (SQLite)
- [x] Chose data source (Fallout 76 game items)
- [x] Ingested data into database
- [x] Wrote program to answer questions about data
- [x] Created README with development log

## Contact
GitHub: [your-github-username]
