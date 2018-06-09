const outputYou = document.querySelector('.output-you');

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

recognition.lang = 'en-US';
recognition.interimResults = false;

document.querySelector('button').addEventListener('click', () => {
    recognition.start(); 
  });

  recognition.addEventListener('speechstart', () => {
    console.log('Speech has been detected.');
  });
  
  recognition.addEventListener('result', (e) => {
    console.log('Result has been detected.');
  
    let last = e.results.length - 1;
    let text = e.results[last][0].transcript;
  
    outputYou.textContent = text;
    console.log('Confidence: ' + e.results[0][0].confidence)});
    
    recognition.addEventListener('speechend', () => {
      recognition.stop();
    });