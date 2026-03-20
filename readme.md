# 🚦 Smart Road AI

Smart Road AI is a lightweight research prototype that models traffic density and estimates pollution levels. It also provides simple rule-based suggestions and visualizations to help explore mitigation strategies.

## Features
- Traffic-based pollution estimation (simple model)
- Rule-based solution engine for mitigation suggestions
- Visualization of results (matplotlib)
- CSV input support for multi-road analysis

## Requirements
- Python 3.8+
- Install dependencies:
```bash
pip install -r requirements.txt
# or, if you don't have a requirements file:
pip install matplotlib
```

## Quickstart / Usage
1. Place your data in `data.csv` (see Data Format below) or run the demo example.
2. Run:
```bash
python main.py
```
- If `data.csv` is present, the script will process each road and show aggregated plots.
- Otherwise it will run a single-example simulation.

## Data Format (data.csv)
CSV with header and these columns (example):
```csv
road_id,vehicle_count,avg_speed,pollution_index
R1,120,35,72
R2,80,42,55
```
- `vehicle_count` is used by the default pollution model. `avg_speed` is optional (future models may use it).

## Project Structure
- `main.py` — runs the simulation and reads `data.csv` if present
- `pollution_model.py` — pollution estimation function
- `solution_engine.py` — rule-based suggestions based on pollution index
- `graph.py` — visualization utilities
- `data.csv` — example/sample data

Note: Ensure file names match the imports in `main.py` (e.g., `pollution_model.py`). There was a previous filename mismatch (double underscore) which should be corrected.

## Extending the project
- Replace the simple pollution model with ML-based estimator
- Add real-time sensor input / streaming data
- Improve solution engine with optimization or reinforcement learning
- Add unit tests and CI for reliability

## Contributing
Contributions, bug reports, and feature requests are welcome. Please open an issue or submit a PR.

## License
Add a LICENSE file (e.g., MIT) if you want to make the project open source.

## Author
Kishan Singh
