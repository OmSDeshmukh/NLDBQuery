# NLDBQuery

Welcome to the Gemini Pro Large Language Model (LLM) NLP project! This project aims to facilitate interaction with a database using plain English queries through Google's free Gemini Pro LLM. Various frameworks such as Lang Chain and Hugging Face were employed to enhance model accuracy using few-shot learning techniques. Additionally, vector databases(ChromaDB) were utilized in the process to further refine the results.

![Image description](example.png)

## Installation

To get started with the project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/OmSDeshmukh/NLDBQuery
```

2. Navigate to directory:

```bash
cd NLDBQuery
```

3. Create a virtual environment:

```bash
python3 -m venv .venv
```

4. Activate the virtual environment:

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

5. Download Dependencies:

```bash
pip install -r requirements.txt
```

6. Create database:

```bash
# Login
mysql -u username -p password

# Create Database
CREATE DATABASE atliq_tshirts < db_creation_atliq_t_shirts.sql;
```


7. Configure .env files accordingly with the required API keys and password of the database

## Usage

To run inference and interact with the database, follow these instructions:

Ensure you're in the project directory and the virtual environment is activated.

Run the following script:
```bash
streamlit run main.py
```
## Aknowledgement
Special thanks to Codebasics whose YouTube video provided valuable insights and guidance in creating this project.


## License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to customize it further according to your project's specific details and requirements.
