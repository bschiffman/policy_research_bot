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
### Quickstart 
``` bash
cd /path/to/your/folder/policy_research_bot
pip install -r requirements.txt
```
### Necessities:
You will need to have API access to a LLM provider, or an LLM you can call locally. I suggest OpenAI for ease of use, since you can insert your API key as an environment variable without changing the source code. Ensure to keep your personal keys safe, for example as a secret environment variable in your GitHub repo. See this discussion for some guidance. [How to pass secrets variables to your private github packages?](https://github.com/orgs/community/discussions/64585)

### Customization options:
- **Prompt Customization:** both the system prompt and summary prompts can be customized to fit your goals and instruct the ChatBot with regards to how you want information to be summarized for your needs.
- **Source Customization:** The sources chosen for this project fit my personal goals of
  1) Easy access via RSS
  2) Academic or other well respected sources
  3) Topic and interests (economics/econometrics, AI/ML, public policy)

  Feel free to pursue other sources.
- **LLM Model:** This project uses GPT-4.0-mini for fast, low-cost summarization. You may want to use a newer model for deeper or more modern insight.

# Ownership and Creative details

### Author
**Ben Schiffman, MPP**  
AI agents and applied systems • public policy • economics  
LinkedIn: https://www.linkedin.com/in/ben-schiffman/

## License

This project is licensed under the [MIT License](LICENSE).  

You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of this software, provided that the original copyright notice and this permission notice are included in all copies or substantial portions of the software.

