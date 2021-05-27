# Hampton Roads PulsePoint Incident Scraper

This project allows you to gather and save all the active (i.e., on-going) and recent (i.e., cleared) [PulsePoint](https://web.pulsepoint.org/) incidents for the fire and EMS agencies in the Hampton Roads area. It saves them to a Realtime Firebase database.

If you simply want to see the scraped data and/or save it to a local JSON file, add the following lines to the end of the `pulsepoint.py` Python script:

```
        # Be sure to indent properly!!!
        # Print human-readable output
        [print("%s @ %s" % (c.get("PulsePointIncidentCallType"), c.get("FullDisplayAddress"))) for c in active]
        [print("%s @ %s" % (c.get("PulsePointIncidentCallType"), c.get("FullDisplayAddress"))) for c in recent]

        # Write JSON to file
        with open('pulsepoint.json', 'w') as f:
            f.write('[') # start array
            for a in active:
                f.write(json.dumps(a, sort_keys=True, indent=4))
                f.write(',')
            for r in recent:
                if (recent[-1] is (r)): # if last incident
                    f.write(json.dumps(r, sort_keys=True, indent=4))
                    f.write(']') # end array
                else:
                    f.write(json.dumps(r, sort_keys=True, indent=4))
                    f.write(',')
```

To configure the project to write to your Firebase database:

 1. Download your Firebase JSON service account key, and put it into the same folder as this project.
 2. Rename the `firebase_config_sample.py` file to `firebase_config.py`.
 3. In the `firebase_config.py` file, change the `'serviceAccountKey.json'` filename to match your service key's filename.
 4. Change the `firebase_database_url` to your Firebase database's URL.

 To run the script:
 ```
 % python3 pulsepoint_scrape.py
 ```
