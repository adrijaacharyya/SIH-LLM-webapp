submit = document.querySelector('.submit');
list = document.querySelector('.sum-more');
typeOfText = document.getElementById('type');

tasks = document.getElementsByName('rd');
let selectedTask;
let model;


const handleSubmit = (e) => {
    for(const selected of tasks) {
        if(selected.checked) {
            selectedTask = selected.value;
            break;
        }
    }
    if (selectedTask === 'summarize') {
        let text = typeOfText.value;
        model = text;
    } 
    if (selectedTask === 'grammar') {
        model = selectedTask;
    }
    const req = new XMLHttpRequest();
    req.open('POST',`/ProcessModel/${JSON.stringify(model)}`)
    req.send();
}

tasks.forEach(function(input) {
    input.addEventListener("click", function() {
        let inputValue = input.value;
        if (inputValue === 'summarize') {
            list.style.display = 'block';
        }
        if (inputValue === 'grammar') {
            list.style.display = 'none';
        }
    });
});
  

submit.addEventListener('click', handleSubmit);


//Text to speech
output = document.getElementById('span').innerText
speech = new SpeechSynthesisUtterance(output)

btn = document.querySelector('.loud');
const handleClick = (e) => {
    speechSynthesis.speak(speech);
}
btn.addEventListener('click', handleClick);


//feedback

const buttons = document.querySelectorAll(".fa-button");

buttons.forEach(function(button) {
    button.addEventListener("click", function() {
        // Remove the 'selected' class from all buttons
        buttons.forEach(function(btn) {
            btn.classList.remove("selected");
        });

        // Add the 'selected' class to the clicked button
        button.classList.add("selected");
    });
});