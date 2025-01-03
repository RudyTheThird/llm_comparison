
# LLM Model Comparison Framework

## Overview
This project evaluates GPT-4, Claude 2, and Gemini Pro across five key metrics:
1. Reasoning
2. Coding
3. Creativity
4. Instruction Following
5. Knowledge Retrieval

📌 Task 2025-01-03_03:37__BV23
Date: 03 Jan 2025 03:37
Priority: 900
Proposal:
Create a quantitative comparison matrix of GPT-4, Claude 2, and Gemini Pro by building a Python testing framework that evaluates each model across 5 key metrics (reasoning, coding, creativity, instruction following, and knowledge retrieval). Submit a GitHub repository containing the testing framework, results in CSV format, and a markdown analysis of the findings.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/llm_comparison.git
   cd llm_comparison
   ```

2. **Install Dependencies:**
   ```bash
   pip install requests
   ```

3. **Set OpenRouter API Key:**
   ```bash
   export OPENROUTER_API_KEY="your_api_key_here"
   ```

4. **Run the Comparison:**
   ```bash
   python compare_llms.py
   ```

5. **View Results:**
   - Open `results.csv` for raw data.
   - Open `analyze_results.md` for insights.

## License
MIT
