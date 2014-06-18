from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row = hackbright_app.get_student_by_github(student_github)
    html = render_template("student_info.html", first_name=row[0],
                                                last_name=row[1],
                                                github=row[2])
    return html

@app.route("/")
def get_github():
    return render_template("git_github.html")

@app.route("/get_student")
def get_student_grades():
    hackbright_app.connect_to_db()
    firstname = request.args.get("first_name")
    lastname= request.args.get("last_name")
    rows = hackbright_app.grades_for_student(firstname, lastname)
    return render_template("student_grades.html", firstname=firstname, lastname=lastname, rows=rows)


if __name__ == "__main__":
    app.run(debug=True)