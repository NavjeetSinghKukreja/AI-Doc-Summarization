# AI-Powered Article Summarization and Sentiment Analysis

This project implements an AI-powered web application that performs extractive and abstractive text summarization, along with sentiment analysis, on uploaded articles. The application uses BERT for extractive summarization and BART for abstractive summarization, combining the results for enhanced performance. The sentiment of the summarized content is then analyzed using a transformer-based sentiment analysis model.

## Features
- **Extractive Summarization**: Uses BERT to extract the most important information from the text.
- **Abstractive Summarization**: Leverages BART for generating a more coherent and concise summary.
- **Combined Summarization**: Combines extractive and abstractive summarization techniques for better overall results.
- **Sentiment Analysis**: Analyzes the sentiment (positive, negative, or neutral) of the summarized text.
- **Flask Web Application**: Provides an interactive web interface for users to upload articles and receive summaries and sentiment analysis results.

## Installation

### Requirements
- Python 3.6 or higher
- Flask
- Huggingface `transformers` library
- PyTorch
- `summarizer` library for BERT

### Steps
1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/ai-powered-summarization.git
    cd ai-powered-summarization
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Make sure you have CUDA enabled if you're using a GPU, or the app will run on the CPU by default.

## Usage

1. Run the Flask app:

    ```bash
    python app.py
    ```

2. Open your browser and go to `http://127.0.0.1:5000/` to access the application.

3. Upload your article in the input box on the homepage.

4. The app will display the **combined summary** and **sentiment analysis** of the uploaded article.

## How It Works

- **Data Preprocessing**: The user uploads an article through the web interface.
- **Extractive Summarization (BERT)**: The uploaded article is passed through a BERT-based summarizer to extract important sentences.
- **Abstractive Summarization (BART)**: The extractive summary is then fed into a BART model to generate an abstractive summary.
- **Combined Summary**: The final summary is a combination of the two techniques, providing a comprehensive summary of the article.
- **Sentiment Analysis**: The sentiment of the generated summary is analyzed and categorized as **Positive**, **Negative**, or **Neutral**.

## Code Explanation

- **`app.py`**: Contains the Flask application that handles user requests, generates summaries, and displays results.
- **`models.py`**: Includes the functions for extractive and abstractive summarization, as well as sentiment analysis using transformer-based models.
    - **`generate_extractive_summary`**: Uses BERT to generate extractive summaries.
    - **`generate_abstractive_summary`**: Uses BART to generate abstractive summaries.
    - **`generate_combined_summary`**: Combines the extractive and abstractive summaries.
    - **`get_sentiment`**: Analyzes the sentiment of the provided text using the Huggingface transformers sentiment pipeline.

## Technologies Used
- **Flask**: Web framework for building the web app.
- **BERT**: For extractive summarization.
- **BART**: For abstractive summarization.
- **Huggingface Transformers**: Library for easy access to pre-trained transformer models.
- **PyTorch**: Framework used for running transformer models

## Contributing

Feel free to open issues, submit pull requests, or suggest improvements to enhance the functionality of the project. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
