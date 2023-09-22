output = document.getElementById('span').innerText
speech = new SpeechSynthesisUtterance(output)

btn = document.querySelector('.loud');
const handleClick = (e) => {
    speechSynthesis.speak(speech);
}
btn.addEventListener('click', handleClick);