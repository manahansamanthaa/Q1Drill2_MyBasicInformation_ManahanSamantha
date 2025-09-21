from pyscript import display


title= "My Basic Information"
description= "Input your name, age and hobby! :))"

display(title, target="webtitle")
display(description, target="desc1")



from pyscript import document, display


def generate(e): #we put e for event handling
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    hobby = document.getElementById("hobby").value

 #multiline
    profile = f"""
Profile: 
    Name    : {name}
    Age     : {age}
    hobby  : {hobby}

Notes:
    {name} is currently {age} years old loves to {hobby}.\nThis information was gathered through input fields and displayed\nusing a multiline string in Python via PyScript.
    """

    document.getElementById("message").innerText = profile