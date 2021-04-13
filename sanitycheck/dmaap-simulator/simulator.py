import json
import logging as sys_logging

from flask import Flask, request, logging, Response

app = Flask(__name__)

sys_logging.basicConfig(level=sys_logging.DEBUG)
logger = logging.create_logger(app)
events = {}


@app.route("/events/<path:topic>", methods=['POST'])
def event_sec_fault_output(topic):
    return handle_new_event(topic, request)


@app.route("/events", methods=['GET'])
def get_events():
    resp = Response(json.dumps(events))
    resp.headers['Content-Type'] = 'application/json'
    return resp


@app.route("/events", methods=['DELETE'])
def clear_events():
    events.clear()
    return {}, 200


@app.route("/events/<path:topic>", methods=['GET'])
def get_events_from_topic(topic):
    resp = Response(json.dumps(get_events_from_map(topic)))
    resp.headers['Content-Type'] = 'application/json'
    return resp


def handle_new_event(topic, http_request):
    receive_events = decode_request_data(http_request.data)
    for event in receive_events:
        add_event_to_map(topic, json.loads(event))
    return {}, 200


def decode_request_data(request_data):
    data = request_data.decode("utf-8")
    receive_events = data.split("\n")
    receive_events = receive_events[:-1]
    logger.info("received events: " + str(receive_events))
    correct_events = []
    for event in receive_events:
        logger.info("received event: " + str(event))
        correct_events.append(get_correct_json(event))
    return correct_events


def get_correct_json(incorrect_json):
    json_start_position = incorrect_json.find("{")
    correct_json = incorrect_json[json_start_position:]
    correct_json = correct_json.replace("\r", "").replace("\t", "").replace(" ", "")
    return correct_json


def add_event_to_map(topic, event):
    if events.__contains__(topic):
        events[topic].append(event)
    else:
        events[topic] = [event]


def get_events_from_map(topic):
    if events.__contains__(topic):
        return events[topic]
    else:
        return []


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3904)
