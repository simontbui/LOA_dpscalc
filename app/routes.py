from app import app
from flask import Flask, render_template, request, url_for
from app.engravings import engrav_list
from app.dps import final_dps
#from selections import Form

@app.route('/', methods=['GET', 'POST'])
def index():
    #selections = request.form.get('select')
    #form = Form()

    if request.method == "POST":
        #form = {'engravings': ['eng1', 'eng2', ---, ---, ...], 'lvl' = ['#', '#', ...],
        #        'crit-select': ['##' or ''], 'critdmg-select': ['##' or '']}
        form = request.form.to_dict(flat=False)
        engrav_input = form["engravings"]
        lvl_input = [int(x) for x in form["lvl"] if x != '---']
        crit_chance = [int(x) for x in form["crit-select"] if x is not None][0]
        crit_dmg  = [int(x) for x in form["critdmg-select"] if x is not None][0]
        multiplier = final_dps(engravings=engrav_input, engrav_lvl=lvl_input, c_rate=crit_chance,
                                c_dmg=crit_dmg).multiplier
    else:
        multiplier = 1

    return render_template('index.html', engrav_list=engrav_list, multiplier=multiplier)

# @app.route('/results', methods=['POST'])
# def display_multiplier():
#     #form = {'engravings': ['<eng1>', '<eng2>', ---, ---, ...], 'lvl' = ['<#>', '<#>', ...]}
#     form = request.form.to_dict(flat=False)

#     engrav_input = form["engravings"]
#     lvl_input = [int(x) for x in form["lvl"] if x != '---']
#     multiplier = final_dps(engravings=engrav_input, engrav_lvl=lvl_input).multiplier

#     return render_template('results.html', multiplier=multiplier)

