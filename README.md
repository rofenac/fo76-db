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

5. NOTE: There is also a super light GUI frontend to view the database. It is the "one liner" file. It contains the command to spin up a super lightweight web server that can be accessed at "localhost:8080" Just make sure it is exectuable and run is as a bash script.

## What the Program Does

1. **Tests Machine Learning:** Uses HuggingFace's sentiment analysis to analyze game-related text
2. **Creates Database:** Sets up a SQLite database with a table for game items
3. **Loads Data:** Adds Fallout 76 items (Stimpak, 10mm Pistol, Combat Armor, etc.)
4. **Analyzes Data:** Answers questions like:
   - What are the most valuable items?
   - What's the average value by item type?

NOTE: The interactivity of the model is finicky at best. It's a bit, like from the original TRON movie. The model I used can be found [here.](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)

## Sample Output
```
Top Items by Value:
- Laser Rifle (Weapon): 175 caps
- Combat Armor (Armor): 100 caps
- 10mm Pistol (Weapon): 50 caps
- Stimpak (Medicine): 25 caps
- Nuka Cola (Drink): 10 caps
```

## Development Log

### Week 1
- Scrambled to get my life together

### Week 2
- **03OCT2025** Created this starter project in one fell swoop. It took all day, even with help from LLMs

## Data Source
Initial data is hard-coded based on Fallout 76 wiki information. Future versions will scrape data from:
- Fallout Wiki
- Game databases
- Community resources

## Future Improvements
- Add more items to the database
- Migrate data to a dedicated Docker/MySQL server
- Create a web scraper for automatic updates
- Build a recommendation system for players
- Add more complex ML models for price prediction

## What I Learned
- How to set up a Python development environment
- How to use pre-trained ML models from HuggingFace  
- How to create and query SQL databases
- How to manage code with Git and GitHub
- How to use AI tools (ChatGPT 5 "Agent" Mode and Claude Opus 4.1 w/Github access) for development

## Challenges Overcome
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
GitHub: rofenac
