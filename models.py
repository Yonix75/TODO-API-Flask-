import uuid


str(uuid.uuid4())
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





def home():
    return tasks


def id(num_id):
   
    for u in tasks:
      if num_id == u["id"]:
       return  u
      


def create_task(data):
   
    new_task = {
        "id": str(uuid.uuid4()),
        "title": data["title"],
        "completed": False
    }
    
    tasks.append(new_task)
    

    return new_task
    


def put_task(id,data):
     
    for task in tasks:
        if id == task["id"]:
           task["title"]=data["title"]
           if "completed" in data:
                task["completed"]=data["completed"]  
      
        return task
   
   

def patch_task(id,data):
    
    for task in tasks:
        if id == task["id"]:
           task["completed"]=data["completed"] 
        
        return task

    

def del_task(id):    
    for task in tasks:
        if id == task["id"]:
           tasks.remove(task)
            
    return task
    