from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os, json

app = Flask(__name__)

#load env variables from .env file
load_dotenv()

db_url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    os.getenv('databaseUser'),
    os.getenv('databasePswd'),
    os.getenv('host'),
    os.getenv('port'),
    os.getenv('databaseName')
)

#connect to database
engine = create_engine(db_url)

#create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.route('/test', methods=['GET'])
def test():
    """
    Test method to check application status
    :return: json
    """
    path = os.getcwd() + "/database/config.json"
    with open(path) as f:
        d = json.load(f)
    # return jsonify(message='Endpoint test successful!')
    return jsonify(d)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)