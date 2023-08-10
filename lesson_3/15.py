import requests
try:
    my_file = requests.get("awdadeiheeofaf.txt")
except requests.exceptions.ConnectionError as e:
    print("invalid schema")
