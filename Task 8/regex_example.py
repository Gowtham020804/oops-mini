

import re

text = "Contact us at support@gmail.com or admin@yahoo.com"

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)

print("Emails found:")
for email in emails:
    print(email)