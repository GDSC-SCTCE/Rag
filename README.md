 **# Rag**

**A web application harnessing the power of Google AI's Gemini generative model for creative text generation and exploration.**

**## Description**

This open-source project provides a user-friendly interface to interact with Gemini's capabilities through a Streamlit web app with additional pdf chat and more

**## Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/GDSC-SCTCE/Rag.git
   ```

2. **Install dependencies:**

   ```bash
   cd Rag
   pip install -r requirements.txt
   ```

3. **Set up Pinecone API key (optional):**

   - If you want to use Pinecone for vector search, create a free account at [https://www.pinecone.io/](https://www.pinecone.io/) and get your API key.
   - Set the API key as an environment variable:

     ```bash
     export PINECONE_API_KEY=YOUR_API_KEY
     ```

**## Usage**

1. **Run the app:**

   ```bash
   streamlit run main.py
   ```

2. **Access the app in your browser:**

   - Open http://localhost:8501/ in your web browser.


**## Contributing**

We welcome contributions and feedback! Feel free to open issues or pull requests to enhance the project.

**## License**

Rag is licensed under the MIT License.
