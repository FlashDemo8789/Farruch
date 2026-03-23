import re

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{TITLE} — Maison Farruch</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=Inter:wght@300;400;500;600&display=swap">
  <link rel="stylesheet" href="css/maison-farruch.css">
  <link rel="icon" href="images/logo-farruch.png" type="image/png">
  <style>
    .page-collection .hero-sub {
      background: linear-gradient(rgba(10,10,10,0.4), rgba(10,10,10,0.8)), url('images/banner03.jpg') center/cover no-repeat;
    }
    .collection-image {
      width: 100%;
      height: 60vh;
      min-height: 400px;
      object-fit: cover;
      margin-bottom: 2rem;
      border: 1px solid var(--border);
    }
    .collection-content {
      max-width: 900px;
      margin: 0 auto;
    }
  </style>
</head>
<body class="page-collection">
  <header class="hero hero-sub">
    <nav class="nav">
      <a class="brand" href="index.html">FARRUCH</a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="nav-menu">
        <span></span>
        <span></span>
      </button>
      <ul class="nav-links" id="nav-menu">
        <li><a href="index.html" data-page="home">Global Export</a></li>
        <li><a href="maison.html" data-page="maison">The Maison</a></li>
        <li><a href="craft.html" data-page="craft">Craft</a></li>
        <li><a href="runway.html" data-page="runway">Runway</a></li>
        <li><a href="services.html" data-page="services">Services</a></li>
        <li><a href="commissions.html" data-page="commissions">Commissions</a></li>
        <li><a href="index.html#contact" data-page="contact">Contact</a></li>
      </ul>
    </nav>
    <div class="hero-content">
      <p class="eyebrow">Luxury Collection</p>
      <h1>{TITLE}</h1>
      <p class="lede">{LEDE}</p>
    </div>
    <div class="hero-overlay"></div>
  </header>

  <main>
    <section class="section reveal">
      <div class="collection-content">
        <img src="images/{IMAGE_SRC}" alt="{TITLE}" class="collection-image">
        <h2 style="font-family:var(--serif); font-size:2.5rem; margin-bottom:1.5rem;">Sourcing & Provenance: {HEADING}</h2>
        <p style="font-size:1.15rem; line-height:1.8; color:var(--muted); margin-bottom:1.5rem;">{PARAGRAPH_1}</p>
        <p style="font-size:1.15rem; line-height:1.8; color:var(--muted); margin-bottom:2.5rem;">{PARAGRAPH_2}</p>
        <a class="btn btn-primary" style="border: 1px solid var(--text); color: var(--text); background: transparent;" href="index.html#products">Return to Collection</a>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div>
      <span class="brand">FARRUCH</span>
      <p>Luxury import & export, and haute couture since 1904.</p>
    </div>
    <div class="footnote">
      <p>&copy; 2025 Farruch Exports. All rights reserved.</p>
    </div>
  </footer>

  <script src="js/maison-farruch.js"></script>
</body>
</html>
"""

pages = [
    {
        "filename": "collection-jewelry.html",
        "TITLE": "Fine Jewelry",
        "LEDE": "Acquiring the most exquisite, unblemished diamonds and sapphires from ethical French and international markets.",
        "IMAGE_SRC": "luxury_jewelry_1774180208176.png",
        "HEADING": "Precision at its Peak",
        "PARAGRAPH_1": "Farruch orchestrates the logistics and secure transport of high-value jewelry for private collectors and haute couture runways alike. Operating under absolute confidentiality, our sourcing network spans the legendary Ateliers of Paris and the diamond districts of Geneva.",
        "PARAGRAPH_2": "Every gemstone and precious metal is meticulously verified for clarity, color, cut, and carat weight through our elite certification agents. We provide armored transit and white-glove delivery, ensuring pristine integrity upon arrival."
    },
    {
        "filename": "collection-textiles.html",
        "TITLE": "Luxury Textiles",
        "LEDE": "Mastering the sourcing of lush silks, structured brocades, and our signature heavy crystal embroidery fabrics.",
        "IMAGE_SRC": "luxury_textiles_embroidery_1774226197168.png",
        "HEADING": "The Fabric of Couture",
        "PARAGRAPH_1": "Textiles are the backbone of Maison Farruch. Our expertise was forged in the demanding environment of haute couture embroidery. From sourcing pure spun gold threads in India to procuring the finest emerald silk in Italy, we comprehend tactile value.",
        "PARAGRAPH_2": "We offer dedicated export pipelines for designers seeking uncut bolts of exclusive tulle dripping with thousands of hand-stitched crystals. These dense, heavy fabrics are securely rolled, climate-controlled, and transported securely to ateliers globally."
    },
    {
        "filename": "collection-leather.html",
        "TITLE": "Artisanal Leather",
        "LEDE": "Securing handcrafted leather luggage, briefcases, and accessories born from centuries-old Tuscan craftsmanship.",
        "IMAGE_SRC": "luxury_leather_1774180235744.png",
        "HEADING": "A Legacy of Hide & Hardware",
        "PARAGRAPH_1": "Our leather acquisition network runs deep through the traditional tanneries of Florence, Italy. We identify makers who adhere to meticulous vegetable-tanning processes and bespoke brass hardware finishing to ensure goods age beautifully.",
        "PARAGRAPH_2": "Because high-end leather is susceptible to atmospheric fluctuations, Farruch strictly enforces climate and humidity-controlled logistics from the workbench to your private vault. Our team manages all CITES documentation if exotic skins are requested."
    },
    {
        "filename": "collection-timepieces.html",
        "TITLE": "Luxury Timepieces",
        "LEDE": "Curating mechanical marvels and limited-edition tourbillons from the Swiss masters of horology.",
        "IMAGE_SRC": "luxury_timepiece_1774180252618.png",
        "HEADING": "Chronometric Mastery",
        "PARAGRAPH_1": "Securing a limited-run Swiss mechanical watch requires leveraging discreet industry relationships. Farruch’s horological division accesses allocations of grand complications and tourbillons directly from Geneva's most private salons.",
        "PARAGRAPH_2": "Each mechanical movement is subjected to extreme logistical care during export. Our vault-to-vault secure routing utilizes bespoke shock-absorbent, pressure-regulated transit cases, preserving the delicate gear train calibrations throughout the journey."
    },
    {
        "filename": "collection-crystal.html",
        "TITLE": "Crystal Artworks",
        "LEDE": "Importing breathtaking faceted crystal sculptures and decanters defined by their geometric brilliance.",
        "IMAGE_SRC": "luxury_crystal_sculpture_1774221685461.png",
        "HEADING": "Prismatic Purity",
        "PARAGRAPH_1": "Hand-cut crystal masterpieces demand a reverence for fragility and form. Sourced actively from historic Bohemian glassworks in Prague and exclusive studios across Europe, these heavy monolithic sculptures encapsulate pure luxury.",
        "PARAGRAPH_2": "Exporting fine crystal is an intricate logistical ballet. Farruch utilizes proprietary suspended-tension crating solutions that isolate the artwork from microscopic vibrations during transit, delivering the multifaceted clarity and sharp refractive edges entirely unscathed."
    },
    {
        "filename": "collection-collectibles.html",
        "TITLE": "Rare Collectibles",
        "LEDE": "Tracking down antiquarian artifacts, historic gold astrolabes, and irreplaceable cultural objects from global private estates.",
        "IMAGE_SRC": "luxury_collectibles_1774180291121.png",
        "HEADING": "The Artifact Dossier",
        "PARAGRAPH_1": "For the esoteric collector, Farruch operates a discrete acquisitions wing dedicated to antiquities, rare scientific instruments, and historical artifacts. True one-of-a-kind collectibles require exhaustive provenance investigations.",
        "PARAGRAPH_2": "Our specialists handle complex heritage and cultural export legislations across dozens of jurisdictions. Accompanied by full historical dossiers and structural condition reports, you are guaranteed undisputed ownership of the world’s most fascinating objects."
    }
]

import os
target_dir = "/Users/sf/aamirbeading.com/www.aamirbeading.com/"
for p in pages:
    content = template
    for k, v in p.items():
        if k != "filename":
            content = content.replace(f"{{{k}}}", v)
    
    with open(os.path.join(target_dir, p["filename"]), "w") as f:
        f.write(content)

print("Generated all 6 collection pages.")
