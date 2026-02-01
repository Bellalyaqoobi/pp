herefrom flask import Flask

app = Flask(name)

PHONE = "84776115200"  # شماره تو بدون +

@app.route("/")
def home():
    return f"""
<!DOCTYPE html>
<html lang="fa">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AghayeRobat</title>

<style>
body {{
    margin: 0;
    padding: 0;
    height: 100vh;
    background: linear-gradient(135deg,#000000,#0f2027,#203a43);
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial;
}}

.btn {{
    padding: 25px 40px;
    font-size: 22px;
    background: #25D366;
    color: white;
    border: none;
    border-radius: 15px;
    text-decoration: none;
    box-shadow: 0px 0px 20px #25D366;
}}

.btn:hover {{
    background: #1ebe5d;
}}
</style>

</head>

<body>

<a class="btn" href="https://wa.me/{PHONE}?text=سلام" target="_blank">
💬 کلیک کن برای پیام واتساپ
</a>

</body>
</html>
"""

if name == "main":
    app.run(host="0.0.0.0", port=5000)
