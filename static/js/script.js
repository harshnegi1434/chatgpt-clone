sendButton.addEventListener("click", () => {
    const questionInput = document.getElementById("questionInput").value;
    document.getElementById("questionInput").value = "";
    document.querySelector(".right2").style.display = "block";        
    document.querySelector(".right1").style.display = "none";
        
    question1.InnerHTML = questionInput;
    question2.InnerHTML = questionInput;
});

