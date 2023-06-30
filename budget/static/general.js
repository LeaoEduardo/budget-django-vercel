function updateProgressBar(selectedProgress) {
    const progressBarContainers = document.getElementById("progress-bar-container").children;

    for (let i = 0; i < progressBarContainers.length; i++) {
      progressBarContainers[i].style.display = "none";
    }

    document.getElementById(selectedProgress).style.display = "block";
}