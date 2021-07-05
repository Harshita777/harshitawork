function getUserInput(){
    var userInput = document.getElementById("inputField").value
    window.location=`http://localhost:8000/cgi-bin/file.py?var=${userInput}`;
}