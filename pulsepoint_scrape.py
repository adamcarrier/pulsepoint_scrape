#!/usr/bin/env python3
# Main script for running the city data collection and firebase sync modules

from pulsepoint import PulsePoint

def main():
    pp = PulsePoint()

    # Define agencies (all Hampton Roads agencies)
    agency_list = [
        '70001',    # Newport News Fire Department (VA)
        '65000',    # Hampton Division of Fire & Rescue (VA)
        '09500',    # James City County Fire Department (VA)
        '83000',    # Williamsburg Fire Department (VA)
        '73500',    # Poquoson Fire Department (VA)
        '19900',    # York County Fire and Life Safety (VA)
        'EMS1264',  # Virginia Beach Department of EMS (VA)
        '71000',    # Norfolk Fire-Rescue VA (VA)
        '80000',    # Suffolk Fire and Rescue (VA)
        '55000'     # Chesapeake Fire Department (VA)
    ]
    for agency_id in agency_list:
        pp.get_incidents(agency_id)

if __name__ == "__main__":
    main()