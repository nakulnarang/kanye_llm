# kanye_llm
# Kanye West Conversational AI - Fine-Tuning TinyLlama-1.1B

This project involves fine-tuning the `TinyLlama-1.1B` model to generate Kanye West-style conversational responses. The dataset is generated using OpenAI's GPT-4 API, and the fine-tuning process is performed using LoRA (Low-Rank Adaptation) for efficient model adaptation. The project demonstrates how to fine-tune a language model and evaluate its performance using perplexity.

## Project Overview

- **Objective**: Create a conversational agent that mimics Kanye West's speech style by fine-tuning the `TinyLlama-1.1B` model.
- **Model**: We use `TinyLlama-1.1B`, a smaller version of the LLaMA architecture.
- **Dataset**: The dataset is generated using the GPT-4o API and consists of 1000 prompt-response pairs in Kanye West's style.
- **Evaluation**: The model's performance is evaluated by computing the average perplexity of generated responses.

## Repository Structure

```plaintext
├── kanye_llm.ipynb            # Jupyter notebook with the full fine-tuning process
├── data_generation.py     # Script to generate dataset
├── README.md                   # Project documentation

