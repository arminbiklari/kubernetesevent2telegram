import urllib3
import json
import os
import time
import cryptography
from flask import Flask, render_template, request, send_file
from json_pars import kuber_event_pars
from datetime import datetime
from telegram import send_message


log_file = f"all_webhooks_detailed{datetime.today().strftime('%Y-%m-%d')}.json"
dir = "jsonLogs"
save_webhook_output_file = os.path.join(dir, log_file)

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def wbhook():
    if request.method == "POST":
        print("webhook recieved\n")
        request_json = request.json
        # print the received notification
        print('Payload: ')
        print(json.dumps(request_json,indent=4))
        with open(save_webhook_output_file, 'a') as filehandle:
            filehandle.write('%s\n' % json.dumps(request_json,indent=4))
        final_message = kuber_event_pars(request_json)
        send_message(final_message)    
        return 'Webhook notification received', 202
    else:
        return 'POST Method not supported', 405
@app.route("/log", methods=['GET'])  # create a route for /log, method GET
def log():
    with open(save_webhook_output_file, "r") as f: 
        content_of_file = f.read() 
    return render_template('bootstrap.html', content_var = content_of_file, filename_var = save_webhook_output_file)

# Download the logs file
@app.route("/download", methods=['GET'])  # create a route for /download, method GET
def download():
    return send_file(save_webhook_output_file, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5443)
