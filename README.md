# AI-chatbot-with-NLP

*COMPANY NAME*: CODTECH IT SOLUTION

*NAME*: YASODHA R

*INTERN ID*:CTIS0243

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR NAME*: NEELA SANTHOSH

**AI CHATBOT WITH NLP

The AI Chatbot project is a web-based application designed to simulate human-like conversation using natural language processing (NLP) techniques. The primary goal of this project is to create an intelligent system that can understand user input in natural language and provide appropriate responses dynamically. Unlike traditional hard-coded chatbots, this system leverages NLP preprocessing and similarity-based matching to enhance interaction quality and allow flexible user queries.

FRONTEND:
The frontend of the application is developed using HTML, CSS, and JavaScript, providing a clean and lightweight interface for the user. The interface includes a chatbox that displays the conversation history, an input field to type messages, and a send button to submit queries. CSS styling ensures a simple, responsive, and visually appealing design with light colors, rounded corners, and scrollable chat history. JavaScript handles sending messages asynchronously to the backend using the Fetch API, receiving responses, and updating the chat interface dynamically without reloading the page.

BACKEND:
The backend is built using the Flask framework in Python, which serves as a lightweight web server to handle client requests and route them appropriately. Flask enables rendering HTML templates, processing HTTP POST requests for incoming messages, and returning JSON-formatted responses to the frontend. The application structure includes separate folders for templates (HTML files) and static resources (CSS), maintaining modularity and clarity in code organization.

The chatbot engine employs Python and several NLP techniques to understand and process user queries. Preprocessing includes text cleaning, converting all input to lowercase, and removing punctuation to standardize messages. To implement more flexible understanding, the project uses TF-IDF (Term Frequency–Inverse Document Frequency) vectorization from the scikit-learn library to represent both user input and predefined questions as numerical vectors. Cosine similarity is calculated between the user query and all predefined questions to identify the most relevant response. If no sufficiently similar question is found, the chatbot returns a default message prompting the user to rephrase. This approach allows the system to handle variations in phrasing and minor differences in input while providing meaningful responses.

The project relies on several tools and libraries, including Python 3.x as the programming language, Flask for web backend, scikit-learn for TF-IDF vectorization and similarity computation, NumPy for numerical operations, and NLTK for optional NLP preprocessing such as tokenization and lemmatization. VS Code is used as the integrated development environment (IDE) for coding, testing, and debugging. The project is fully executable locally on any machine with Python installed, without requiring external APIs or internet connectivity for the core functionality.

SOURCES:
Sources and references include official documentation for Python (https://www.python.org/
), Flask (https://flask.palletsprojects.com/
), scikit-learn (https://scikit-learn.org/
), and NLTK (https://www.nltk.org/
). Additionally, standard online tutorials and examples for implementing chatbots, TF-IDF, and cosine similarity were consulted for understanding algorithm design and integration into the Flask framework.

In conclusion, this AI Chatbot project demonstrates a practical application of natural language processing in creating intelligent conversational agents. It combines a clean, user-friendly web interface with a backend capable of understanding flexible user input through NLP-based similarity matching. The project provides a foundational platform that can be further expanded with advanced machine learning models or API-based AI engines for more sophisticated conversational abilities. The modular design, use of open-source tools, and simplicity of the frontend ensure easy maintenance, scalability, and adaptability for future improvements.

