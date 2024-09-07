# Kanye West Conversational AI - Fine-Tuning TinyLlama-1.1B

This project involves fine-tuning the `TinyLlama-1.1B` model to generate Kanye West-style conversational responses. The dataset is generated using OpenAI's GPT-4 API, and the fine-tuning process is performed using LoRA (Low-Rank Adaptation) for efficient model adaptation. The project demonstrates how to fine-tune a language model and evaluate its performance using perplexity.

## Project Overview

- **Objective**: Create a conversational agent that mimics Kanye West's speech style by fine-tuning the `TinyLlama-1.1B` model.
- **Model**: We use `TinyLlama-1.1B`, a smaller version of the LLaMA architecture.
- **Dataset**: The dataset is generated using the GPT-4 API and consists of 1000 prompt-response pairs in Kanye West's style, stored in `kanye_1000_conversations.json`.
- **Evaluation**: The model's performance is evaluated by computing the average perplexity of generated responses.

## Repository Structure

```plaintext
├── kanye_llm.ipynb            # Jupyter notebook with the full fine-tuning process
├── data_generation.py         # Script to generate dataset using OpenAI GPT-4 API
├── kanye_1000_conversations.json # Dataset containing 1000 prompt-response pairs
├── README.md                  # Project documentation

## Instructions to Run

1. **Clone the Repository**  
   Clone the repository to your local machine and navigate into the project directory:

2. **Upload dataset and ipynb notebook to google colab and use the GPU there to run the entire notebook for faster execution**

