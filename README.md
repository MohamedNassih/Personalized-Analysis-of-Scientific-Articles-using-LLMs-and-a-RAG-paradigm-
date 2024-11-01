# Personalized Analysis of Scientific Articles with LLM and RAG

This project implements a scientific research assistant capable of answering questions based on the user's profile (student or researcher). It uses an embedding-based paradigm to identify the most relevant paragraphs in a database of scientific articles and generates personalized answers using Ollama, a pre-trained language model.

## Features

* **Article Collection and Segmentation:** Automatic collection of scientific articles from arXiv, PDF content extraction, segmentation of articles into relevant sections and paragraphs.
* **Embedding Generation:** Uses DistilBERT to generate high-quality embeddings for each paragraph, capturing the semantic meaning of the text.
* **Vector Storage and Search:** Stores embeddings and associated metadata in Chroma, a vector database optimized for similarity search.
* **Personalized Answer Generation:**  Utilizes Ollama, a pre-trained language model, to generate answers to user queries based on their profile (student or researcher) and the context extracted from Chroma.
* **User Interface:**  Simple and user-friendly interface developed with Streamlit, allowing users to ask questions and receive personalized answers.

## Files

```
|- Code
  |- associer_lien_excel.py
  |- collecte_data.py
  |- segmented.py
  |- embedding.py
  |- search_and_recovery.py
  |- response.py
|- Notebooks
  |- Associer_Lien_Excel.ipynb
  |- Collecte_data.ipynb
  |- segmented.ipynb
  |- embedding.ipynb
  |- search_and_recovery.ipynb
  |- response.ipynb
|- Documentary_Sheets
  |- Collecte_des_données.pdf
  |- Segmented_files.pdf
  |- Embedding.pdf
  |- Search_and_recovery.pdf
  |- Response.pdf
|- FAQ.md
|- Rapport.pdf
|- README.md
|- requirements.txt
```

## Project Structure

The project is organized into several Python modules:

* **`collecte_data.py`:** Collects scientific articles from arXiv, downloads PDFs, extracts textual content, and structures the data in an Excel file.
* **`segmented.py`:** Segments scientific articles into relevant sections and paragraphs.
* **`embedding.py`:** Generates embeddings for each paragraph using DistilBERT and stores them in Chroma.
* **`search_and_recovery.py`:** Queries Chroma to extract the most relevant paragraphs based on a user query.
* **`response.py`:** Uses Ollama to generate personalized answers based on the user profile and context extracted from Chroma.
* **`associer_lien_excel.py`:** Associates links to corresponding files in the Excel file.


## Installation

**1. Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-project-name.git
   ```

**2. Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

**3. Set up the environment:**
   * Mount Google Drive to access files and store data.
   * Configure Chroma for persistent storage of embeddings.
   * Install Ollama locally via Docker.

## Usage

**1. Start the Ollama server:**
   ```bash
   docker run -p 11434:11434 ollama/llama2 
   ```

**2. Run the Streamlit application:**
   ```bash
   streamlit run response.py
   ```

**3. Access the user interface in your browser:**
   ```
   http://localhost:8501
   ```

## Contributors


* **Bachou Brahim:** Responsible for data collection and download automation.
* **Benlahcen Souad:** Responsible for scientific article segmentation.
* **Nassih Mohamed:** Responsible for embedding generation.
* **Baticha Youssef:** Responsible for backend integration.
* **Elmzouri Fatimazahra:** Responsible for developing analysis tools.
* **Bouaamar Ayman:** Responsible for answer generation with Ollama.
* **Rahhou Hakim:** Responsible for the user interface.


## Contact

For any questions or suggestions, please contact `medisnas002@gmail.com`.

## Acknowledgements

We would like to thank **Mr. Thierry Bertin Gardelle** for his valuable guidance during this project.
