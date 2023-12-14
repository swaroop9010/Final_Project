from bottle import route, post, run, template, redirect, request
from bottle import TEMPLATE_PATH, static_file
import database

# Set the path to your templates
TEMPLATE_PATH.append('./templates')

# Call set_up_database to create tables and insert sample data
# database.set_up_database()

@route("/")
def get_index():
    redirect("/list")

@route("/list")
def get_list():
    # Fetch data from both tables using a JOIN
    items = database.get_industries_and_divisions()
    return template("list.tpl", data=items)

@route("/add")
def get_add():
    return template("add_industry_division.tpl")

@post("/add")
def post_add():
    division_name = request.forms.get("division_name")
    company = request.forms.get("company")
    headquarter = request.forms.get("headquarter")

    # Add industry and division
    database.add_industry_and_division(division_name, company, headquarter)
    redirect("/list")

@route("/update/<id>")
def get_update(id):
    items = database.get_industries_and_divisions(id)
    return template("update_industry_division.tpl", item=items[0])

@post("/update")
def post_update():
    division_name = request.forms.get("division_name")
    company = request.forms.get("company")
    headquarter = request.forms.get("headquarter")
    id = request.forms.get("id")

    # Update industry and division
    database.update_industry_and_division(id, division_name, company, headquarter)
    redirect("/list")

@route("/delete/<id>")
def get_delete(id):
    # Delete industry and related divisions
    database.delete_industry_and_division(id)
    redirect("/list")

# Search option for industries and divisions
@route('/search', method='POST')
def search():
    search_term = request.forms.get('search_term')

    # Fetch search results for both Industries and Divisions
    items = database.search_industries_and_divisions(search_term)

    return template('list.tpl', data=items)

# Static Routes
@route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./static')

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True, reloader=True)
