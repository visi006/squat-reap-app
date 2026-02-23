const video = document.getElementById("video");

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
  })
  .catch(err => {
    alert("Camera access denied");
  });

// Dummy data (temporary)
let reps = 0;

setInterval(() => {
  reps++;
  document.getElementById("state").innerText = "STANDING";
  document.getElementById("reps").innerText = reps;
  document.getElementById("accuracy").innerText = "85%";
  document.getElementById("feedback").innerText = "Good posture 👍";
}, 2000);
