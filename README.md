
markdown
Copiar código
# NBA Shot Chart API

This is a Flask-based API that provides NBA shot chart data using the `nba_api` Python package. It allows you to fetch the shot charts of players for a specific season and season progress.

## Requirements

- Python 3.8 or higher
- Flask
- nba_api
- pandas

## Setup

Follow the steps below to set up the project on your local machine.

### 1. Create a Virtual Environment
Create a virtual environment to isolate dependencies:

```
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
Install the required dependencies using pip:

```
pip install -r requirements.txt
```
### 3. Run the API
To run the API, execute the following command:

```
python app.py
```

This will start a local development server at http://localhost:5000.

### 4. Use the API
The API exposes the following endpoint:

```
GET /shot-chart/<player_name>/<season_id>/<season_progress>
```

Example
To get the shot chart data for LeBron James in the 2023-24 season during the Regular Season:

```
http://localhost:5000/shot-chart/LeBron%20James/2023-24/Regular%20Season
```

The API will return a JSON object containing the shot chart data for the specified player, season, and season progress.

### 5. Testing
You can test the API using any HTTP client, such as Postman or directly through your browser. Just replace the player name, season ID, and season progress with the desired values.

Additional Notes
The API relies on the nba_api package, which fetches data from the NBA Stats API.
Make sure to activate the virtual environment whenever you work on this project to ensure that the correct dependencies are used.
