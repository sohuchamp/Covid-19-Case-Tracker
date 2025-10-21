from flask import Flask, render_template
import Beautiful_Covid as bc
import AuxiliaryCode as covid
import os

path = os.environ.get('WorldCovidCases')

app = Flask(__name__)
app.secret_key = "password"


@app.route("/")
def home():
    return render_template("dropdown.html") + "<center><h1 style='background-color: #aaff80'> Welcome to COVID-19 Tracker!</h1></center>" + render_template('Announcements.html') + \
           f"<div style='background-color: #00bfff'><center><h4> {covid.World()}</h4> <img src=f'{path}'><h6>Data is from New York " \
           f"Times.</h6></center></div>"


@app.route('/india')
def India():
    return render_template("dropdown.html") + render_template("India.html") + f"<center><h4> {covid.India()}</h4></center>" '\n' + '<center>Data is from New York Times.</center>'


@app.route('/canada')
def Canada():
    return render_template("dropdown.html") + render_template("Canada.html") + f"<center><h4> {covid.Canada()}</h4></center>" + '\n' + '<center>Data is from New York Times.</center>'


@app.route('/germany')
def Germany():
    return render_template("dropdown.html") + render_template("EuropeanUnion.html") + f"<center><h4> {covid.Germany()}</h4></center>" + '\n' + '<center>Data is from New York Times.</center>'


@app.route('/brazil')
def Brazil():
    return render_template("dropdown.html") + render_template("South America.html") + f"<center><h4> {covid.Brazil()}</h4></center>" + '\n' + '<center>Data is from New York Times.</center>'


@app.route("/spain")
def Spain():
    return render_template("dropdown.html") + render_template("EuropeanUnion.html") + f"<center><h4> {covid.Spain()}</h4></center>" + '\n' + '<center>Data is from New York Times.</center>'


@app.route('/italy')
def Italy():
    return render_template("dropdown.html") + render_template("EuropeanUnion.html") + f"<center><h4> {covid.Italy()}</h4></center>" + '\n' + '<center>Data is from New York Times.</center>'


@app.route('/mexico')
def Mexico():
    return render_template("dropdown.html") + render_template("South America.html") + f"<center><h4> {covid.Mexico()}</h4></center>" + '\n' + '<center>Data is from New York Times.</center>'


@app.route('/france')
def France():
    return render_template("dropdown.html") + render_template("EuropeanUnion.html") + f"<center><h4> {covid.France()}</h4></center>" + '\n' + '<center>Data is from New York Times.</center>'


@app.route('/uk')
def UK():
    return render_template("dropdown.html") + render_template("UK.html") + f"<center><h4> {covid.UK()}</h4></center>" + '\n' + '<center>Data is from New York Times.</center>'


@app.route('/usa')
def USA():
    return render_template("dropdown.html") + render_template("USA.html") + f"<center><h4> {covid.USA()}</h4></center>" + '\n' + '<center>Data is from New York Times.</center>'


@app.route('/uae')
def UAE():
    return render_template('dropdown.html') + render_template("MiddleEast.html") + f"<center><h4> {bc.scrape_data('UAE')} </h4></center>" + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/greece')
def Greece():
    return render_template('dropdown.html') + render_template("EuropeanUnion.html") + f'<center><h4> {bc.scrape_data("Greece")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/turkey')
def Turkey():
    return render_template('dropdown.html') + render_template("MiddleEast.html") + f'<center> {bc.scrape_data("Turkey")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/japan')
def Japan():
    return render_template('dropdown.html') + render_template("EastCentralAsia.html") + f'<center><h4> {bc.scrape_data("Japan")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/china')
def China():
    return render_template('dropdown.html') + render_template("EastCentralAsia.html") + f'<center><h4> {bc.scrape_data("China")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/russia')
def Russia():
    return render_template('dropdown.html') + f'<center><h4> {bc.scrape_data("Russia")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/pakistan')
def Pakistan():
    return render_template('dropdown.html') + render_template("India.html") + f'<center><h4> {bc.scrape_data("Pakistan")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/indonesia')
def Indonesia():
    return render_template('dropdown.html') + render_template("Asia.html") + f'<center><h4> {bc.scrape_data("Indonesia")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/vietnam')
def Vietnam():
    return render_template('dropdown.html') + render_template("Asia.html") + f'<center><h4> {bc.scrape_data("Vietnam")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/thailand')
def Thailand():
    return render_template('dropdown.html') + render_template("Asia.html") + f'<center><h4> {bc.scrape_data("Thailand")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/saudi-arabia')
def SaudiArabia():
    return render_template('dropdown.html') + render_template("MiddleEast.html") + f'<center><h4> {bc.scrape_data("Saudi Arabia")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/israel')
def Israel():
    return render_template('dropdown.html') + render_template("MiddleEast.html") + f'<center><h4> {bc.scrape_data("Israel")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/south-korea')
def SouthKorea():
    return render_template('dropdown.html') + render_template("EastCentralAsia.html") + f'<center><h4> {bc.scrape_data("South Korea")}</h4></center>' + '\n' + '<center>Data is from ' \
                                                                                                                                                             'Worldometer.</center>'


@app.route('/kazakhstan')
def Kazakhstan():
    return render_template('dropdown.html') + render_template("EastCentralAsia.html") + f'<center><h4> {bc.scrape_data("Kazakhstan")}</h4></center>' + '\n' + '<center>Data is from ' \
                                                                                                                                                             'Worldometer.</center>'


@app.route('/guatemala')
def Guatemala():
    return render_template('dropdown.html') + render_template("South America.html") + f'<center><h4> {bc.scrape_data("Guatemala")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/colombia')
def Colombia():
    return render_template('dropdown.html') + render_template("South America.html") + f'<center><h4> {bc.scrape_data("Colombia")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/argentina')
def Argentina():
    return render_template('dropdown.html') + render_template("South America.html") + f'<center><h4> {bc.scrape_data("Argentina")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/south-africa')
def SouthAfrica():
    return render_template('dropdown.html') + render_template("Africa.html") + f'<center><h4> {bc.scrape_data("South Africa")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/morocco')
def Morocco():
    return render_template('dropdown.html') + render_template("Africa.html") + f'<center><h4> {bc.scrape_data("Morocco")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/egypt')
def Egypt():
    return render_template('dropdown.html') + render_template("Africa.html") + f'<center><h4> {bc.scrape_data("Egypt")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/drcongo')
def DRCongo():
    return render_template('dropdown.html') + render_template("Africa.html") + f'<center><h4> {bc.scrape_data("drcongo")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/nigeria')
def Nigeria():
    return render_template('dropdown.html') + render_template("Africa.html") + f'<center><h4> {bc.scrape_data("Nigeria")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/somalia')
def Somalia():
    return render_template('dropdown.html') + render_template("Africa.html") + f'<center><h4> {bc.scrape_data("Somalia")}</h4></center>' + '\n' + '<center>Data is from Worldometer.</center>'


@app.route('/ukraine')
def Ukraine():
    return render_template('dropdown.html') + f'<center><h4> {bc.scrape_data("Ukraine")} </h4></center>' + '\n' + '<center>Data is from Worldometer.</center>  '


@app.route('/norway')
def Norway():
    return render_template('dropdown.html') + render_template("Europe.html") + f'<center><h4> {bc.scrape_data("Norway")} </h4></center>' + '\n' + '<center>Data is from Worldometer.</center>  '


@app.route('/switzerland')
def Switzerland():
    return render_template('dropdown.html') + f'<center><h4> {bc.scrape_data("Switzerland")} </h4></center>' + '\n' + '<center>Data is from Worldometer.</center>  '


@app.route('/sweden')
def Sweden():
    return render_template('dropdown.html') + render_template("EuropeanUnion.html") + f'<center><h4> {bc.scrape_data("Sweden")} </h4></center>' + '\n' + '<center>Data is from Worldometer.</center>  '


@app.route('/denmark')
def Denmark():
    return render_template('dropdown.html') + render_template("EuropeanUnion.html") + f'<center><h4> {bc.scrape_data("Denmark")} </h4></center>' + '\n' + '<center>Data is from Worldometer.</center>  '


@app.route('/austria')
def Austria():
    return render_template('dropdown.html') + render_template("EuropeanUnion.html") + f'<center><h4> {bc.scrape_data("Austria")} </h4></center>' + '\n' + '<center>Data is from Worldometer.</center>  '


@app.route('/poland')
def Poland():
    return render_template('dropdown.html') + render_template("EuropeanUnion.html") + f'<center><h4> {bc.scrape_data("Poland")} </h4></center>' + '\n' + '<center>Data is from Worldometer.</center>  '


@app.route('/portugal')
def Portugal():
    return render_template('dropdown.html') + render_template(
        "EuropeanUnion.html") + f'<center><h4> {bc.scrape_data("Portugal")} </h4></center>' + '\n' + '<center>Data is from Worldometer.</center>  '


@app.route('/about-us')
def AboutUs():
    return render_template('dropdown.html') + render_template('AboutUsandVirus.html')


if __name__ == "__main__":
    app.run(debug=True)
