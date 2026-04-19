from flask import Flask, jsonify, request
import uuid 
#===================Si tu veux travailler entièrement avec uuid changer tout ce qui est en rapport.
str(uuid.uuid4())
app = Flask(__name__)
@app.route("/tasks")
def home():
    return tasks



tasks=[]
task1 = { 
    "id": str(uuid.uuid4()),
    "title": "Learn Flask",
    "completed": False
    }
task2={
    "id": str(uuid.uuid4()),
    "title": "Build API",
    "completed": False
    }
task3={
    "id": str(uuid.uuid4()),
    "title": "Test with Postman",
    "completed": True
    }
        
tasks.append(task1)
tasks.append(task2)
tasks.append(task3)
task_id_counter = 4

@app.route("/tasks/<num_id>")
def id(num_id):
   
    for u in tasks:
      if num_id == u["id"]:
        return  jsonify(u)
    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks", methods=["POST"])
def create_task():
   

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "JSON body required"}), 400

    if "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_task = {
        "id": str(uuid.uuid4()),
        "title": data["title"],
        "completed": False
    }

    tasks.append(new_task)
    

    return jsonify(new_task), 201
    

@app.route("/tasks/<id>", methods=["PUT"])
def put_task(id):
 
    data = request.get_json() 
    if not data:
     return jsonify({"error": "JSON body required"}), 400

    if "title" not in data:
        return jsonify({"error": "Title is required"}), 400    
    
    
    for task in tasks:
        if id == task["id"]:
           task["title"]=data["title"]
           if "completed" in data:
                task["completed"]=data["completed"]  
        else:
            return jsonify({"error": "Task not found"}), 404
        return jsonify(task), 201
    
@app.route("/tasks/<id>", methods=["DELETE"])
def del_task(id):    
    for task in tasks:
        if id == task["id"]:
            tasks.remove(task)
            return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

   
    

   

# ==========================================================================================  
# print(tasks)


# task_counter = 0

# for task in tasks:
#     task_counter+=1
#     if task["id"] != task_id_counter:
#        valid_id =True
#     if task["completed"]==True:
#           valid_complet = True
#           break
#     if task != None:
#          task_On = True 
# print(task_counter)
# print(valid_id)        
# print(valid_complet)
# print(task_On)


if __name__ == "__main__":
    app.run(debug=True)