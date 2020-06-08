# -*- coding: utf-8 -*-

import os
import json


from flask import Flask  
from flask import request
app = Flask(__name__)

cluster_list = {"clusters":[]}

with open('cluster.list.json') as json_data:
    cluster_list = json.load(json_data)

@app.route("/")
def hello():  
    return "<b>Cluster API</b>"

@app.route("/cluster_list", methods=['GET'])
def web_cluster_list():
   return json.dumps(cluster_list)

@app.route("/cluster_get", methods=['GET'])
def web_cluster_get():
    cluster_id = request.args.get('cluster_id')
   
    if cluster_id:
        for cluster in cluster_list["clusters"]:
            if cluster["cluster_id"] == cluster_id:
                return json.dumps(cluster)
        return "unknown cluster"
    else:
        return "no cluster_id defined"

@app.route("/cluster_start", methods=['GET','POST'])
def web_cluster_start():
    cluster_id = request.args.get('cluster_id')
   
    if cluster_id:
        for cluster in cluster_list["clusters"]:
            if cluster["cluster_id"] == cluster_id:
                if cluster["state"]=="RUNNING":
                    result = {"cluster_id": cluster_id, "state": "RUNNING",	"error": "Cluster already running"}
                    return json.dumps(result)
                elif cluster["state"]=="TERMINATING" or cluster["state"]=="TERMINATED":
                    cluster["state"]="RUNNING"
                    result = {"cluster_id":cluster_id, "state": "RUNNING"}
                    return json.dumps(result)
                else:
                    return "Invalid cluster state"

        return "unknown cluster"
    else:
        return "no cluster_id defined"

@app.route("/cluster_stop", methods=['GET','POST'])
def web_cluster_stop():
    cluster_id = request.args.get('cluster_id')
   
    if cluster_id:
        for cluster in cluster_list["clusters"]:
            if cluster["cluster_id"] == cluster_id:
                if cluster["state"]=="TERMINATED":
                    result = {"cluster_id": cluster_id, "state": "TERMINATED",	"error": "Cluster already stopped"}
                    return json.dumps(result)
                elif cluster["state"]=="TERMINATING" or cluster["state"]=="RUNNING":
                    cluster["state"]="TERMINATED"
                    result = {"cluster_id":cluster_id, "state": "TERMINATED"}
                    return json.dumps(result)
                else:
                    return "Invalid cluster state"
        return "unknown cluster"
    else:
        return "no cluster_id defined"

if __name__ == "__main__":  
    app.run(host='0.0.0.0',debug=True,port=os.getenv("PORT", 8080))
