function startHandler() {
    let text = document.getElementById("code-input").value;
    console.log(text);

    let canvas = document.getElementById("labyrinth-rendering");
    let context = canvas.getContext("2d");
    context.font = "30px Arial";
    context.strokeText("Poopybutthole", 10, 50);

}


