# Setup
pip install -r requirements.txt

# To run:
python -m venv venv
# source venv/bin/activate  no Linux
# venv\Scripts\activate no Windows com cmd/ps
# source venv/Scripts/activate no Windows com gitbash

# Set .env
cp .env_example .env
    # Change the file

python run.py
