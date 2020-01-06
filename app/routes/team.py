from app import app
from flask import jsonify
from flask_httpauth import HTTPBasicAuth
import requests
import xmltodict

auth = HTTPBasicAuth()


@app.route('/getAllTeams', methods=["GET"])
def get_all_teams():
    teams = []
    response = requests.get(
        'http://m7.tm00.com/tmpartnerservice/Services/PartnerDropdownlistService.svc/GetDropdownvaluesByHostIdAndListId/47/Team',
        headers={
            "Content-Type": "application/json",
            "Authorization": "18:E6LfjeMCP"
        },
    )

    responseContentJson = xmltodict.parse(response.content)
    if responseContentJson["PartnerDDLValue"] is not None:
        listItems = responseContentJson["PartnerDDLValue"]["ListItems"]["a:ListItem"]
        for item in listItems:
            teams.append(item["a:ListItemValue"])

    return jsonify(teams)
