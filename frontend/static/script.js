// script.js
let isDefinitionVisible = false;

function toggleDisplay() {
    isDefinitionVisible = !isDefinitionVisible;

    if (isDefinitionVisible) {
        fetchDefinition();
        // Fetch and display definition
        // You can use fetch() or another AJAX library to make a request to your FastAPI backend.
    } else {
        hideDefinition();
        // Fetch and display examples
    }

    document.getElementById("examples-button").innerText = "Examples";
}

function fetchDefinition() {
    // Replace this with the actual API endpoint for fetching the definition
    // For simplicity, let's assume it returns a static definition for now
    //const definition = "Example Definition 1";
    // Animation: Move the word up by 40px
    document.getElementById("word-container").style.transform = "translateY(-10px)";
    document.getElementById("definition-container").style.transform = "translateY(-10px)";
    // Display the definition below the word
    document.getElementById("definition").innerText = definition.innerText;
    document.getElementById("definition-container").classList.remove("hidden");    
}

function hideDefinition(){     
    // Animation: Move the word down to its original position
    document.getElementById("word-container").style.transform = "translateY(0)";
    document.getElementById("definition-container").style.transform = "translateY(0)";
    
    // Hide the definition container
    document.getElementById("definition-container").classList.add("hidden");    
}

function showExamples() {
    // Check if the current state is to show examples or definition
    if (document.getElementById("examples-button").innerText === "Examples") {
        // Fetch and display examples logic here
        // For simplicity, let's assume it returns a static example for now
        //const examples = "Example 1: Sentence 1\nExample 2: Sentence 2";

        const example1Paragraph = document.getElementById("example1");
        const example2Paragraph = document.getElementById("example2");
      
        // Display the examples
        //document.getElementById("definition").innerText = examples;
        //document.getElementById("definition-container").classList.remove("hidden");
        document.getElementById("example1").innerText = example1.innerText;
        document.getElementById("example2").innerText = example2.innerText;
        //example1Paragraph.innerText = example1;  // Set example1 text
        //example2Paragraph.innerText = example2; 
        document.getElementById("definition").classList.add("hidden");
        example1Paragraph.classList.remove("hidden");
        example2Paragraph.classList.remove("hidden");
        // Change the button text to "Definition"
        document.getElementById("examples-button").innerText = "Definition";
    } else {
        // Show the definition instead
        fetchDefinition();
        document.getElementById("examples-button").innerText = "Examples";
        document.getElementById("definition").classList.remove("hidden");
        document.getElementById("example1").classList.add("hidden");
        document.getElementById("example2").classList.add("hidden");
    }
}

function showSpotify() {
    // Open Spotify logic here
    window.open("https://open.spotify.com/search/" + encodeURIComponent(word.innerText), "_blank");

}
