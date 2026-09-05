# Projects

This folder contains three AI projects demonstrating **machine learning, genetic algorithms, and search-tree algorithms**.

## 1. Data-Driven Project — Spotify Popularity Prediction

**Location:** [`Projects/DataDrivenProject/`](https://github.com/Yunnna005/mtu-ai/tree/main/Projects/DataDrivenProject)

This project predicts a song's **Spotify popularity score (0–100)** using Spotify audio features and Billboard Hot 100 data.

The project:

* Combines Spotify and Billboard datasets using song and artist information.
* Uses features such as danceability, energy, loudness, tempo, chart position, and weeks on the chart.
* Compares three regression models:

  * **Linear Regression**
  * **Random Forest**
  * **Gradient Boosting**
* Evaluates models using MAE, RMSE, and R².

**Random Forest** achieved the best performance, with an R² of approximately **0.65**, showing that combining audio and chart information can provide useful predictions of song popularity.

```text
DataDrivenProject/
├── DataDrivenProject.ipynb
├── dataset.csv
└── charts.csv
```

---

## 2. Genetic Algorithm — Dublin Airport Air Traffic Control

**Location:** [`Projects/Genetic_algorithm/`](https://github.com/Yunnna005/mtu-ai/tree/main/Projects/Genetic_algorithm)

This project uses a **Genetic Algorithm** to reduce potential aircraft conflicts around Dublin Airport.

The algorithm searches for adjustments to each aircraft's:

* Heading
* Speed
* Vertical rate

The goal is to maintain a minimum separation of **6 km**, while making the smallest possible changes to aircraft trajectories.

The algorithm works through:

1. Population generation
2. Fitness evaluation
3. Selection
4. Crossover
5. Mutation
6. Repeating over multiple generations

The project demonstrates how evolutionary optimisation can be applied to complex real-world problems involving multiple interacting aircraft.

```text
Genetic_algorithm/
├── Genetic_algorithm.ipynb
└── Data/
    ├── 50_flights.csv
    ├── dublin_runways.csv
    ├── flights_to_dublin.csv
    ├── new_flights.csv
    ├── getDublinFlights.py
    └── getDublinRunway.py
```

---

## 3. Search Tree — Gomoku AI

**Location:** [`Projects/SearchTree/`](https://github.com/Yunnna005/mtu-ai/tree/main/Projects/SearchTree)

This project implements a **Gomoku AI** using a search tree and the **Minimax algorithm**.

The game uses a **4×4 board**, with players attempting to get three consecutive pieces horizontally or vertically, or four diagonally.

The AI:

* Generates possible moves.
* Searches future game states.
* Uses Minimax to choose the best move.
* Evaluates non-terminal positions using a heuristic function.
* Searches up to **6 moves ahead**.
* Uses move ordering to consider promising moves first.

This project demonstrates how search algorithms can be used to make decisions in competitive games.

```text
SearchTree/
└── Search_tree.ipynb
```

---

## Summary

| Project                 | AI Technique              | Application                        |
| ----------------------- | ------------------------- | ---------------------------------- |
| **Data-Driven Project** | Machine Learning          | Spotify popularity prediction      |
| **Genetic Algorithm**   | Evolutionary Optimisation | Dublin Airport air-traffic control |
| **Search Tree**         | Minimax / Search          | Gomoku AI                          |
