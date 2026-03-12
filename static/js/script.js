function showAlert(){
    alert("Post Published Successfully!");
}

function validateForm(){
    let title = document.getElementById("title").value;
    let author = document.getElementById("author").value;

    if(title === "" || author === ""){
        alert("Please fill all fields!");
        return false;
    }
    return true;
}