# Chatbot_Rasa


env: 
conda create -p venv3.10 python==3.10 -y
conda activate D:\Python\Chatbot_Rasa\Chatbot_Rasa\venv3.10

rasa: 
pip install rasa
rasa init

test prompt:
cd rasamdl
rasa shell

Run:
rasa run --enable-api --debug --cor "*"
python app.py