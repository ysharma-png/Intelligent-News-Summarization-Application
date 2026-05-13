let speech = null;
let words = [];
let currentWordIndex = 0;
let fullText = "";
let isPaused = false;

// Play Speech
function playSpeech() {
    const textElement = document.getElementById("summaryText");
    const language = document.getElementById("languageSelect").value;

    if (!textElement) {
        alert("No summary available!");
        return;
    }

    fullText = textElement.innerText.trim();
    if (!fullText) return;

    // Stop previous speech
    window.speechSynthesis.cancel();

    words = fullText.split(" ");
    currentWordIndex = 0;
    isPaused = false;

    speakFromIndex(currentWordIndex, language);
    updateSlider();
}

// Speak from specific position (Forward/Backward pointer)
function speakFromIndex(index, language) {
    if (index >= words.length) return;

    const remainingText = words.slice(index).join(" ");
    speech = new SpeechSynthesisUtterance(remainingText);

    const langMap = {
        "en": "en-US",
        "hi": "hi-IN",
        "fr": "fr-FR",
        "es": "es-ES",
        "de": "de-DE"
    };

    speech.lang = langMap[language] || "en-US";
    speech.rate = 1;
    speech.pitch = 1;

    speech.onboundary = function (event) {
        if (event.name === "word") {
            currentWordIndex++;
            updateSlider();
        }
    };

    window.speechSynthesis.speak(speech);
}

// Pause
function pauseSpeech() {
    if (window.speechSynthesis.speaking) {
        window.speechSynthesis.pause();
        isPaused = true;
    }
}

// Resume
function resumeSpeech() {
    if (isPaused) {
        window.speechSynthesis.resume();
        isPaused = false;
    }
}

// Stop
function stopSpeech() {
    window.speechSynthesis.cancel();
    currentWordIndex = 0;
    updateSlider();
}

// Clear Text Area
function clearText() {
    document.getElementById("newsText").value = "";
}

// 🎚 Slider (Forward & Backward Control)
document.addEventListener("DOMContentLoaded", function () {
    const slider = document.getElementById("audioSlider");

    if (slider) {
        slider.addEventListener("input", function () {
            if (!words.length) return;

            window.speechSynthesis.cancel();
            currentWordIndex = parseInt(slider.value);

            const language = document.getElementById("languageSelect").value;
            speakFromIndex(currentWordIndex, language);
        });
    }
});

// Update slider dynamically
function updateSlider() {
    const slider = document.getElementById("audioSlider");
    if (slider && words.length > 0) {
        slider.max = words.length;
        slider.value = currentWordIndex;
    }
}