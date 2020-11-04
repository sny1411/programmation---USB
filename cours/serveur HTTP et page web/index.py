#coding:utf-8
import cgi
import time

print("Content-type: text/html; charset=utf-8\n")

vrb = time.strftime("%c")

html = f"""<!DOCTYPE html>
<head>
	<meta charset="utf-8">
	<title>Ma page Web</title>
</head>
<body>
	<h1>COUCOU</h1>
	<form method="post" action="result.py">
	<p><input type="text" name="nom utilisateur">
	<input type="submit" value="Envoyer"></p>
	</form>
	<p>il est : {vrb}</p>
</body>
</html>
"""
print(html)