# LIGN167 Project FA22: Data Science Interview Tool
- This tool can be used by students and early career professionals as a comprehensive resource to revise their technical and non-technical interviewing skills.

## SQL Practice Tool
Files needed:
- [`sql_session.py`](https://github.com/apatankar22/LIGN167_Project/blob/main/sql_session.py)
  - Please enter in your OpenAI API key near the top of the file
- [`sql_prompt.txt`](https://github.com/apatankar22/LIGN167_Project/blob/main/sql_prompt.txt)
  - This file should be in the same directory as the [`sql_session.py`](https://github.com/apatankar22/LIGN167_Project/blob/main/sql_session.py) file.

To run a session of the SQL Practice Tool, open a Terminal or a Jupyter Notebook in the same directory as the above files and run the below code:
```
from sql_session import *
SQLSession('your-username-here')
```
You should see some printed output and will be prompted to enter in some input. 
  
## Python Practice Tool
Files needed:
- [`ds_algo_gpt3.py`](https://github.com/apatankar22/LIGN167_Project/blob/main/ds_algo_gpt3.py)
  - Please enter in your OpenAI API key near the top of the file
- [`python_prompt.txt`](https://github.com/apatankar22/LIGN167_Project/blob/main/python_prompt.txt)
  - This file should be in the same directory as the [`ds_algo_gpt3.py`](https://github.com/apatankar22/LIGN167_Project/blob/main/ds_algo_gpt3.py) file.
- [`python_comparison_prompt.txt`](https://github.com/apatankar22/LIGN167_Project/blob/main/python_comparison_prompt.txt)
  - This file should be in the same directory as the [`ds_algo_gpt3.py`](https://github.com/apatankar22/LIGN167_Project/blob/main/ds_algo_gpt3.py) file.

To run a session of the Python Practice Tool, open a Terminal or a Jupyter Notebook in the same directory as the above files and run the below code:
```
from ds_algo_gpt3.py import *
PythonCodingSession('your-username-here')
```
You should hee see printed output and will be prompted to enter in some input. 

## Behavorial Interview Practice Tool
Files needed:
- [`chatbot_to_submit.py`](https://github.com/apatankar22/LIGN167_Project/blob/main/ds_algo_gpt3.py)
  - Please enter in your OpenAI API key near the top of the file
- [`your_resume.pdf`]

To run a session of the Python Practice Tool, open a Terminal or a Jupyter Notebook in the same directory as the above files and run the below code:
```
from chatbot_to_submit.py import *
behavorial_questions()
```
You should see some printed output and will be prompted to enter in some input. 
