document.addEventListener("DOMContentLoaded", function () {
  const imgTriggers = document.querySelectorAll(".img-trigger");

  imgTriggers.forEach(function (trigger) {
    trigger.addEventListener("click", function () {
      const popup = this.nextElementSibling;
      popup.style.display = "block";
    });
  });

  const imgPopups = document.querySelectorAll(".img-popup-window");

  imgPopups.forEach(function (popup) {
    popup.addEventListener("click", function () {
      this.style.display = "none";
    });
  });
});
