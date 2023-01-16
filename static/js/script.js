// Get the button element
let button = document.getElementById("myButton");

// Add a click event listener to the button
button.addEventListener("click", function() {
    // Get the input element
    let input = document.getElementById("myInput");

    // Get the value of the input
    let inputValue = input.value;

    // Get the paragraph element
    let paragraph = document.getElementById("myParagraph");

    // Update the text content of the paragraph
    paragraph.textContent = "You entered: " + inputValue;
});
