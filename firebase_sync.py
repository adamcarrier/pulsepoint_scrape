#!/usr/bin/env python3
# https://firebase.google.com/docs/database/admin/save-data

import json, firebase_admin
from firebase_admin import credentials, db
from firebase_config import service_account_key, firebase_database_url
from pulsepoint_incident_types import IncidentTypes

def init_db():
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate(service_account_key)

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': firebase_database_url
    })

def save_incident(agency_id, incident):
    # JSON to Python
    incidentJSON = json.loads(incident)

    # Get a database reference
    ref = db.reference('pulsepoint/agency_id/' + agency_id)

    # Set the destination firebase node
    node_ref = ref.child('incidents')

    # Save each item individually
    node_ref.child(incidentJSON['ID']).set({
        'AgencyID': incidentJSON['AgencyID'],
        'CallReceivedDateTime': incidentJSON['CallReceivedDateTime'],
        'FullDisplayAddress': incidentJSON['FullDisplayAddress'],
        'Latitude': incidentJSON['Latitude'],
        'Longitude': incidentJSON['Longitude'],
        'MedicalEmergencyDisplayAddress': incidentJSON['MedicalEmergencyDisplayAddress'],
        'PulsePointIncidentCallType': IncidentTypes[incidentJSON['PulsePointIncidentCallType']].value
    })