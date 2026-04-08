from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = ["Sample Task"] # default task

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks", methods=["GET", "POST"])
def task_page():
    if request.method == "POST":
        task = request.form["task"]
        tasks.append(task)
        return redirect("/tasks")
    
    return render_template("tasks.html", tasks=tasks)

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/tasks")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()