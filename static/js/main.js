window.onload = function () {
  var hum = document.getElementById("hum");
  var menu = document.getElementById("menu" );
  var isOpen = false;

  hum.addEventListener("click", () => {
    if (isOpen == false) {
      isOpen = true;

      // Humberger style
      hum.classList.add("open");
      hum.style.zIndex = "10";

      menu.classList.add("aditionalStyle");
    } else {
      isOpen = false;

      // Humberger style
      hum.classList.remove("open");
      hum.style.zIndex = "10";

      menu.classList.remove("aditionalStyle");
    }
  });

  var navbtn = [...document.getElementsByClassName("link")];

  navbtn.forEach(element => {
    element.addEventListener('click', () => {

      isOpen = false;

      // Humberger style
      hum.classList.remove("open");
      hum.style.zIndex = "10";

      menu.classList.remove("aditionalStyle");

    })
  });
};
