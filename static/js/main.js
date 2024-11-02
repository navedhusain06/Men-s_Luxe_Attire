const menuBtn = document.getElementById("menu-btn");
const navLinks = document.getElementById("nav-links");
const menuBtnIcon = menuBtn.querySelector("i");

menuBtn.addEventListener("click", (e) => {
  navLinks.classList.toggle("open");

  const isOpen = navLinks.classList.contains("open");
  menuBtnIcon.setAttribute("class", isOpen ? "ri-close-line" : "ri-menu-line");
});

navLinks.addEventListener("click", (e) => {
  navLinks.classList.remove("open");
  menuBtnIcon.setAttribute("class", "ri-menu-line");
});

const scrollRevealOption = {
  origin: "bottom",
  distance: "50px",
  duration: 1000,
};

ScrollReveal().reveal(".header__image img", {
  ...scrollRevealOption,
  origin: "right",
});
ScrollReveal().reveal(".header__content h1", {
  ...scrollRevealOption,
  delay: 500,
});
ScrollReveal().reveal(".header__content p", {
  ...scrollRevealOption,
  delay: 1000,
});
ScrollReveal().reveal(".header__btns", {
  ...scrollRevealOption,
  delay: 1500,
});

const banner = document.querySelector(".banner__container");

const bannerContent = Array.from(banner.children);

bannerContent.forEach((item) => {
  const duplicateNode = item.cloneNode(true);
  duplicateNode.setAttribute("aria-hidden", true);
  banner.appendChild(duplicateNode);
});

ScrollReveal().reveal(".arrival__card", {
  ...scrollRevealOption,
  interval: 500,
});

ScrollReveal().reveal(".sale__image img", {
  ...scrollRevealOption,
  origin: "left",
});
ScrollReveal().reveal(".sale__content h2", {
  ...scrollRevealOption,
  delay: 500,
});
ScrollReveal().reveal(".sale__content p", {
  ...scrollRevealOption,
  delay: 1000,
});
ScrollReveal().reveal(".sale__content h4", {
  ...scrollRevealOption,
  delay: 1000,
});
ScrollReveal().reveal(".sale__btn", {
  ...scrollRevealOption,
  delay: 1500,
});

ScrollReveal().reveal(".favourite__card", {
  ...scrollRevealOption,
  interval: 500,
});



setTimeout(() => {
  const toastElements = document.querySelectorAll('[id^="toast-"]');
  toastElements.forEach((toast) => {
    toast.style.display = 'none';
  });
}, 3000);  // 3000 ms yaani 3 seconds ke liye show kare


function checkPasswordStrength() {
  var password = document.getElementById("password").value;
  var strengthStatus = document.getElementById("password-strength-status");
  
  var strength = 0;

  // Conditions to increase strength level
  if (password.length >= 8) strength += 1;  // Length check
  if (/[A-Z]/.test(password)) strength += 1;  // Uppercase letter check
  if (/[a-z]/.test(password)) strength += 1;  // Lowercase letter check
  if (/[0-9]/.test(password)) strength += 1;  // Number check
  if (/[@$!%*?&]/.test(password)) strength += 1;  // Special character check

  // Update the strength status based on strength level
  if (strength === 0) {
      strengthStatus.innerHTML = "<span style='color: grey;'>Enter a password</span>";
  } else if (strength === 1) {
      strengthStatus.innerHTML = "<span style='color: red;'>Simple Password</span>";
  } else if (strength === 2 || strength === 3) {
      strengthStatus.innerHTML = "<span style='color: orange;'>Medium Password</span>";
  } else if (strength === 4) {
      strengthStatus.innerHTML = "<span style='color: blue;'>Good Password</span>";
  } else if (strength === 5) {
      strengthStatus.innerHTML = "<span style='color: green;'>Strong Password</span>";
  }
}





