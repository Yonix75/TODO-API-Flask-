from flask import request, jsonify, Blueprint
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity
from models import tasks
import uuid


tasks_bp = Blueprint("tasks", __name__)



@tasks_bp.route("/tasks")
def home():
    return tasks

@tasks_bp.route("/tasks/<num_id>")
def id(num_id):
   
    for u in tasks:
      if num_id != u["id"]:
       raise ValueError("dude error Task not found")
      return  jsonify(u)

@tasks_bp.route("/tasks", methods=["POST"])
def create_task():
   

    data = request.get_json(silent=True)

    # if not data:
    #     ValueError("Title must be a string")
        
    if not isinstance(data, str):
        raise BadRequest("dude Title must be a string")    

    if "title" not in data:
        raise ValueError("error you need title")

    new_task = {
        "id": str(uuid.uuid4()),
        "title": data["title"],
        "completed": False
    }

    tasks.append(new_task)
    

    return jsonify(new_task), 201
    

@tasks_bp.route("/tasks/<id>", methods=["PUT"])
def put_task(id):
 
    data = request.get_json() 
    if not isinstance(data, str):
        raise BadRequest("Title must be a string") 

    if "title" not in data:
       raise ValueError("error you need title")   
    
    
    for task in tasks:
        if id == task["id"]:
           task["title"]=data["title"]
           if "completed" in data:
                task["completed"]=data["completed"]  
        else:
            raise ValueError("error Task not found")
        return jsonify(task), 201
   
   
@tasks_bp.route("/tasks/<id>", methods=["PATCH"])
def patch_task(id):
 
    data = request.get_json() 
    if not data:
        raise BadRequest("JSON body is required")

    if "completed" not in data:
        raise BadRequest("You need to provide 'completed'")

    if not isinstance(data["completed"], bool):
        raise BadRequest("Completed must be a boolean") 
    
    
    for task in tasks:
        if id == task["id"]:
           task["completed"]=data["completed"] 
        else:
            raise ValueError("error Task not found")
        return jsonify(task), 201

    
@tasks_bp.route("/tasks/<id>", methods=["DELETE"])
def del_task(id):    
    for task in tasks:
        if id != task["id"]:
            raise ValueError("error Task not found")
            
    tasks.remove(task)
    return jsonify(task), 200