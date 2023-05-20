const computer = document.getElementById("computer-choice");
const user = document.getElementById("user-choice");
const result = document.getElementById("result");
const combinations = document.querySelectorAll(".rpsButtons");
let usersChoice;
let cpuChoice;

const someFunction = (event) => {
  usersChoice = event.target.id; //
  user.innerHTML = usersChoice;
  generateComputerChoice();
  displayResult();
};

const displayResult = () => {
  if (usersChoice === cpuChoice && usersChoice === "paper") {
    // paper tie
    result.innerHTML = '<img src="img/paper.jpg" width="300px" height="200px">';
    result.style.color = "green";
    user.style.color = "green";
    computer.style.color = "green";
  } else if (usersChoice === cpuChoice && usersChoice === "scissors") {
    // scissors tie
    result.innerHTML = "If you're into that.";
    result.style.color = "green";
    user.style.color = "green";
    computer.style.color = "green";
  } else if (usersChoice === cpuChoice && usersChoice === "rock") {
    // rock tie
    result.innerHTML =
      '<img src="img/theRock.jpg" width="300px" height="200px">';
    result.style.color = "green";
    user.style.color = "green";
    computer.style.color = "green";
  } else {
    if (
      (usersChoice === "rock" && cpuChoice === "paper") ||
      (usersChoice === "paper" && cpuChoice === "rock")
    ) {
      paperCoversRock(usersChoice);
    } else if (
      (usersChoice === "rock" && cpuChoice === "scissors") ||
      (usersChoice === "scissors" && cpuChoice === "rock")
    ) {
      rockBeatsScissors(usersChoice);
    } else if (
      (usersChoice === "scissors" && cpuChoice === "paper") ||
      (usersChoice === "paper" && cpuChoice === "scissors")
    ) {
      scissorsCutsPaper(usersChoice);
    }
  }
};

const paperCoversRock = (usersChoice) => {
  result.innerHTML = "Paper covers rock.";
  usersChoice === "rock"
    ? ((user.style.color = "red"),
      (computer.style.color = "blue"),
      (result.style.color = "red"))
    : ((user.style.color = "blue"),
      (computer.style.color = "red"),
      (result.style.color = "blue"));
};

const rockBeatsScissors = (usersChoice) => {
  result.innerHTML = "Rock beats scissors.";
  usersChoice === "scissors"
    ? ((user.style.color = "red"),
      (computer.style.color = "blue"),
      (result.style.color = "red"))
    : ((user.style.color = "blue"),
      (computer.style.color = "red"),
      (result.style.color = "blue"));
};

const scissorsCutsPaper = (usersChoice) => {
  result.innerHTML = "Scissors cuts paper.";
  usersChoice === "paper"
    ? ((user.style.color = "red"),
      (computer.style.color = "blue"),
      (result.style.color = "red"))
    : ((user.style.color = "blue"),
      (computer.style.color = "red"),
      (result.style.color = "blue"));
};

const generateComputerChoice = () => {
  const randomNumber = Math.random();
  if (randomNumber > 0.66) {
    cpuChoice = "rock";
  } else if (randomNumber > 0.33) {
    cpuChoice = "paper";
  } else {
    cpuChoice = "scissors";
  }
  computer.innerHTML = cpuChoice;
};

combinations.forEach((combination) => {
  combination.addEventListener("click", someFunction);
});
