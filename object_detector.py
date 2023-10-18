from ultralytics import YOLO
from flask import request, Flask, jsonify
from waitress import serve
from PIL import Image
import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def root():
    """
    Site main page handler function.
    :return: Content of index.html file
    """
    with open("index.html") as file:
        return file.read()


@app.route("/detect", methods=["POST"])
def detect():
    """
        Handler of /detect POST endpoint
        Receives uploaded file with a name "image_file", passes it
        through YOLOv8 object detection network and returns and array
        of bounding boxes.
        :return: a JSON array of objects bounding boxes in format [[x1,y1,x2,y2,object_type,probability],..]
    """
    buf = request.files["image_file"]
    boxes = detect_objects_on_image(buf.stream)
    return jsonify(boxes)


def detect_objects_on_image(buf):
    """
    Function receives an image,
    passes it through YOLOv8 neural network
    and returns an array of detected objects
    and their bounding boxes
    :param buf: Input image file stream
    :return: Array of bounding boxes in format [[x1,y1,x2,y2,object_type,probability],..]
    """
    model = YOLO("best.pt")
    results = model.predict(Image.open(buf))
    result = results[0]
    output = []
    for box in result.boxes:
        x1, y1, x2, y2 = [
            round(x) for x in box.xyxy[0].tolist()
        ]
        class_id = box.cls[0].item()
        prob = round(box.conf[0].item(), 2)
        
        story = create_user_stories(result.names[class_id])

        output.append([
            x1, y1, x2, y2, result.names[class_id], prob,story
        ])
    return output


def create_user_stories(user_text):    
    genericPrompt = "You are a business analyst  and want to define user story for ecommerce website. Please generate user story for development of "
    # completions = ai.Completion.create(
    #     engine='gpt-3.5-turbo',  # Determines the quality, speed, and cost.
    #     temperature=0.5,            # Level of creativity in the response
    #     prompt= genericPrompt+user_text,           # What the user typed in
    #     max_tokens=100,             # Maximum tokens in the prompt AND response
    #     n=1,                        # The number of completions to generate
    #     stop=None,                  # An optional setting to control response generation
    # )
    f = open('/Users/sdhillon/D/Projects/hackathon/FigmatoStory/prompt.json')
    data = json.load(f)
    if user_text in data:
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a business analyst, skilled in writing e-commerce user stories for e-commerce website development."},
            {"role": "user", "content": "Compose a user story that explains "+data[user_text]}
        ]
    )
    
    f.close()

    return completion.choices[0].message

serve(app, host='0.0.0.0', port=8081)