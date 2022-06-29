from flask import Flask, render_template, request, url_for
from maths.engravings import engrav_list
from maths.dps import final_dps

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        #form = {'engravings': ['eng1', 'eng2', ---, ---, ...], 'lvl' = ['#', '#', ...],
        #        'crit-select': ['##' or ''], 'critdmg-select': ['##' or '']}
        form = request.form.to_dict(flat=False)
        engrav_input = [x for x in form["engravings"] if x != '---']
        lvl_input = [int(x) for x in form["lvl"] if x != '---']
        crit_chance = [int(x) for x in form["crit-select"] if x is not None][0]
        crit_dmg  = [int(x) for x in form["critdmg-select"] if x is not None][0]
        multiplier = final_dps(engravings=engrav_input, engrav_lvl=lvl_input, c_rate=crit_chance,
                                c_dmg=crit_dmg).multiplier

        return render_template('index.html', engrav_list=engrav_list, multiplier=multiplier,
                        crit_chance=crit_chance, crit_dmg=crit_dmg, engrav_input=engrav_input,
                        lvl_input=lvl_input)
    else:
        crit_chance = 0
        crit_dmg = 200
        multiplier = 1.0

        return render_template('index.html', engrav_list=engrav_list, multiplier=multiplier,
                                crit_chance=crit_chance, crit_dmg=crit_dmg)

if __name__ == '__main__':
    app.run(debug=True)
