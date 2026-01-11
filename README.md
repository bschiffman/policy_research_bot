# policy_research_bot
This is a Bot that will send me a short list of policy/econ articles daily that have been filtered and summarized by ChatGPT for prioritization. As of today, the output lives in the GitHub actions logs - so anyone can fork and get this running in just a few minutes!

# Overview
This project runs on weekdays via GitHub actions. It uses RSS feeds to source academic articles and policy related content from [arXiv](https://arxiv.org/) and [VoxEU](https://cepr.org/voxeu). Each source's article is checked against a persistent "seen items" tracker to prevent repetition, and a subset of new articles are selected and summarized via an OpenAI API call. 

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

### Author
**Ben Schiffman, MPP**  
AI agents and applied systems • public policy • economics  
LinkedIn: https://www.linkedin.com/in/ben-schiffman/

## License

This project is licensed under the [MIT License](LICENSE).  

You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of this software, provided that the original copyright notice and this permission notice are included in all copies or substantial portions of the software.

