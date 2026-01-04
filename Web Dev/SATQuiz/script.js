let questions = [];
let currentQuestion = 0;
let score = 0;
let ansswered = false;

// Load JSON
fetch('questions.json')
    .then(response => response.json())
    .then(data => {
        questions = data;
        showQuestion();
    })
    .catch(err => console.error("Failed to load questions:", err));

// Display question and options
function showQuestion() {
    answered = false;

    const q = questions[currentQuestion];
    document.getElementById('question').innerText = q.question;

    const optionsDiv = document.getElementById('options');
    optionsDiv.innerHTML = '';

    q.options.forEach(option => {
        const btn = document.createElement('button');
        btn.innerText = option;

        btn.addEventListener('click', () => checkAnswer(option, btn));

        optionsDiv.appendChild(btn);
    });
}

// Check answer and update score
function checkAnswer(selected, btn) {
    if (answered) return; 
    answered = true;

    const q = questions[currentQuestion];

    const optionButtons = document.querySelectorAll('#options button');
    optionButtons.forEach(b => {
        if (b.innerText === q.answer) {
            b.style.backgroundColor = '#06d6a0'; 
            b.style.color = '#1f4068';
        } else if (b === btn) {
            b.style.backgroundColor = '#e63946';
            b.style.color = '#1f4068';
        }
        b.disabled = true;
    })

    if (selected === q.answer) {
        score++;
        document.getElementById('score').innerText = `Score: ${score}`;
    }
}

// Next question
document.getElementById('next-btn').addEventListener('click', () => {
    currentQuestion++;
    if (currentQuestion >= questions.length) {
        alert(`Quiz finished! Final score: ${score}`);
        currentQuestion = 0;
        score = 0;
    }
    showQuestion();
});
