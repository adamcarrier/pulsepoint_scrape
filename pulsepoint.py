#!/usr/bin/env python3
# Gets active and recent PulsePoint incidents for an agency_id

import base64, hashlib, json
from urllib import request
from firebase_sync import save_incident, init_db

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class PulsePoint:
    def __init__(self):
        # Init the Firebase DB (only do this once)
        init_db()

    def get_incidents(self, agency_id):
        data = json.loads(request.urlopen("https://web.pulsepoint.org/DB/giba.php?agency_id=" + agency_id).read().decode())

        ct = base64.b64decode(data.get("ct"))
        iv = bytes.fromhex(data.get("iv"))
        salt = bytes.fromhex(data.get("s"))

        # Build the password
        t = ""
        e = "CommonIncidents"
        t += e[13] + e[1] + e[2] + "brady" + "5" + "r" + e.lower()[6] + e[5] + "gs"

        # Calculate a key from the password
        hasher = hashlib.md5()
        key = b''
        block = None
        while len(key) < 32:
            if block:
                hasher.update(block)
            hasher.update(t.encode())
            hasher.update(salt)
            block = hasher.digest()

            hasher = hashlib.md5()
            key += block

        # Create a cipher and decrypt the data
        backend = default_backend()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()
        out = decryptor.update(ct) + decryptor.finalize()

        # Clean up output data
        out = out[1:out.rindex(b'"')].decode()  # Strip off extra bytes and wrapper quotes
        out = out.replace(r'\"', r'"')  # Un-escape quotes

        data = json.loads(out)
        active = data.get("incidents", {}).get("active", {})
        recent = data.get("incidents", {}).get("recent", {})

        # Write JSON to Firebase
        if (active != None):
            for a in active:
                save_incident(agency_id, json.dumps(a))
        if (recent != None):
            for r in recent:
                save_incident(agency_id, json.dumps(r))