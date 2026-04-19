from flask import request, jsonify, Blueprint
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity
from models import tasks
import uuid


tasks_bp = Blueprint("tasks", __name__)



@tasks_bp.route("/tasks")
def home():
    return tasks
from http.client import InvalidURL

from flask import request, jsonify, Blueprint
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity
from models import tasks
from db import db
import uuid
from bson import ObjectId



tasks_bp = Blueprint("tasks", __name__)



@tasks_bp.route("/tasks", methods=["GET"])
def home():
    tasks = list(db.todo.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
    return jsonify(tasks), 200

@tasks_bp.route("/tasks/<num_id>")
def id(num_id):
    
    tasks = list(db.todo.find())

    for task in tasks:
        task["_id"] = str(task["_id"])
        if num_id == task["_id"]:
            return jsonify(task), 200

    raise NotFound("Task not found")
   
   
      
       
     

@tasks_bp.route("/tasks", methods=["POST"])
def create_task():
   

   
    # `silent=True` lets us raise our own JSON-friendly validation error.
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        raise BadRequest("request body must be json")
    if "title" not in data:
        raise BadRequest("title is required")
    title = data["title"]
    if not isinstance(title, str):
        raise BadRequest("title must be a string")
    if not title.strip():
        raise UnprocessableEntity("title must contain text")

    # New tasks get a generated id and start as incomplete.
    new_task = {
        "title": title.strip(),
        "completed": False  
    }
    
    db.todo.insert_one(new_task)
    
    """_summary_
    {
        _id: ObjectId("69e0c9f9e3d4fc8a309c49ac"),
        "title": title.strip(),
        "completed": False  
    }
    """
    
    new_task["_id"] = str(new_task["_id"])
    return jsonify({
        "success": True,
        "data": new_task
    }), 201
    

# @tasks_bp.route("/tasks/<id>", methods=["PUT"])
# def put_task(task_id):
     
#     data = request.get_json() 
#     if not isinstance(data, str):
#         raise BadRequest("Title must be a string") 

#     if "title" not in data:
#        raise ValueError("error you need title")   
    
#     keys = ("title", "completed")
#     data_keys = data.keys()
#     for key in data_keys:
#         if key not in keys:
#             raise BadRequest(f"not allowed to pass {key}")
#     for task in tasks:
#             if task_id == task["id"]:
#                 if "title" in data:
#                     if not isinstance(data["title"], str):
#                         raise BadRequest("title must be a string")
#                     if not data["title"].strip():
#                         raise UnprocessableEntity("title must contain text")
#                     # Trim whitespace so stored titles stay clean.
#                     task["title"] = data["title"].strip()
#                 if "completed" in data:
#                     if not isinstance(data["completed"], bool):
#                         raise BadRequest("completed must be a boolean")
#                     task["completed"] = data["completed"]
#                 return task
#     raise NotFound(f"{task_id} not found")

@tasks_bp.route("/tasks/<task_id>", methods= ["PUT"])    
def update(task_id):
    body = request.get_json(silent=True)
    
    if ObjectId.is_valid(task_id) == False:
        raise BadRequest("ID must be vaild ObjectId ")
     
    is_exist = db.tasks.find_one(
            {"_id": ObjectId(task_id)}
        )
    if is_exist == None:
        raise NotFound(f"Task with id -{task_id}- not found")

    if body is None:
        raise BadRequest("Missing JSON body")
   
    title = body.get("title")
    if title:
        if not isinstance(title, str):
            raise BadRequest("Title must be a string")
    
    completed = body.get("completed")
    if completed:
        if not isinstance(completed, bool):
            raise BadRequest("completed must be bool.")
                  
    
    if "title" in body:
        new_title= body["title"]
        db.tasks.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {"title":new_title}}
        )
    
    if "completed" in body:
        new_completed= body["completed"]
        db.tasks.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {"completed":new_completed}}
        )
    
    collection_tasks = db["tasks"]
    tasks = list(collection_tasks.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
        
    for task in tasks:
        if task["_id"] == task_id:
            return task   
   
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

@tasks_bp.route("/tasks/<task_id>", methods=["DELETE"])
def del_task(task_id):
    try:
        obj_id = ObjectId(task_id)
    except InvalidURL:
        raise BadRequest("invalid task id")

    task = db.todo.find_one({"_id": obj_id})
    if not task:
        raise NotFound(f"{task_id} not found")

    db.todo.delete_one({"_id": obj_id})

    return jsonify({
        "message": f"removed task {task['title']}"
    }), 200
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