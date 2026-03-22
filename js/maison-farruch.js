(() => {
  const navToggle = document.querySelector(".nav-toggle");
  const navLinks = document.querySelector(".nav-links");
  const navItems = navLinks?.querySelectorAll("a");
  const pageMap = {
    "": "home",
    "index.html": "home",
    "maison.html": "maison",
    "craft.html": "craft",
    "runway.html": "runway",
    "commissions.html": "commissions",
    "initiatives.html": "initiatives",
    "archive.html": "archive",
  };
  const currentPath = window.location.pathname.split("/").pop() ?? "";
  const currentKey = pageMap[currentPath] ?? null;
  const currentHash = window.location.hash;

  if (navToggle && navLinks) {
    navToggle.addEventListener("click", () => {
      const expanded = navToggle.getAttribute("aria-expanded") === "true";
      navToggle.setAttribute("aria-expanded", String(!expanded));
      navLinks.classList.toggle("open");
      navToggle.classList.toggle("open");
    });

    navItems?.forEach((link) => {
      link.addEventListener("click", () => {
        navLinks.classList.remove("open");
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.classList.remove("open");
      });
      const targetPage = link.dataset.page ?? null;
      const isContactHash = targetPage === "contact" && currentHash === "#contact";
      if (targetPage && (targetPage === currentKey || isContactHash)) {
        link.classList.add("is-active");
      }
      if (!currentKey && targetPage === "home") {
        link.classList.add("is-active");
      }
    });
  }

  const toggleSpans = navToggle?.querySelectorAll("span");
  if (navToggle && toggleSpans?.length === 2) {
    navToggle.addEventListener("click", () => {
      if (navToggle.classList.contains("open")) {
        toggleSpans[0].style.transform = "translateY(7px) rotate(45deg)";
        toggleSpans[1].style.transform = "translateY(-7px) rotate(-45deg)";
      } else {
        toggleSpans[0].style.transform = "";
        toggleSpans[1].style.transform = "";
      }
    });
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  document.querySelectorAll(".reveal").forEach((section) => observer.observe(section));
})();
