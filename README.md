# policy_research_bot
This is a Bot that will send me a short list of policy/econ articles daily that have been filtered and summarized by ChatGPT for prioritization. As of today, the output lives in the GitHub actions logs - so anyone can fork and get this running in just a few minutes!

# Overview

## Repo Strucutre
```text
poicy_reasearch_bot/
|-- README.md                     # Project Overview and Setup
|-- requirements.txt              # Python dependencies
|-- .github/
  | -- workflows/
    |-- daily.yml                 # Instructions for GitHub actions (weekday runs 7:30 am eastern)   
|-- data/
  |-- seen_items.json             # Tracker of articles previously included
|-- src
  |-- main.py                     # Orchestrates fetch -> summary -> output and tracking
  |-- fetch_sources.py            # fetches primary sources (arXiv)
  |-- fetch_voxeu.py              # fetches backup sources (VoxEu)
  |-- state.py                    # writes seen items into tracker
  |-- prompts.py                  # Holds system and item summary prompts


```

## Startup and Personalization Guide

# Author
