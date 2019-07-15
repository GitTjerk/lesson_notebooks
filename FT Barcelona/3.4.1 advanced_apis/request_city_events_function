def request_city_events(request):

    import json
    city = request.args.get('city', '')
    starting_from = int(request.args.get('starting_from', 0))

    from flask import abort, jsonify
    print(request.headers)
    if "Authorization" not in request.headers or request.headers['Authorization'] != "Bearer AIzaSyDeDEXWk7bq0r0GYzz-Pmc6dWqRGVxJ2Zc":
        abort(401)
    if city == "Madrid":
        data = [
                   {
                       "snippet": "Learn to code and UX/UI design through one of our full time or part time courses. \nWeb Development "
                                  "Bootcamp and UX/UI Design Bootcamp in Madrid, ...",
                       "link": "https://www.ironhack.com/",
                       "title": "Ironhack Web Development Bootcamp & UX/UI Design Bootcamp",
                       "city": "madrid"
                   },
                   {
                       "snippet": "At Ironhack, we like to interview career professionals in order to bring our \naudience real industry insight. This time we decided not to reach out to a \nprofessional ...",
                       "link": "https://blog.ironhack.com/madrid-2/",
                       "title": "Madrid (EN) - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Enjoy a guided tour and discover some of the most popular places in Madrid. You\n'll also grab some beers in the city center. This is an optional activity, but you ...",
                       "link": "https://summit.ironhack.com/",
                       "title": "Ironhack Alumni Summit",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Dec 3, 2018 ... Our latest articles Inside Cabify – Our alumni experience by Alberto Marcos | Aug \n1, 2016 | Alumni, Madrid At Ironhack, we like to interview ...",
                       "link": "https://blog.ironhack.com/category/madrid-en/",
                       "title": "Madrid Archives - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Formez vous sur Madrid en Développement Web ou en UX/UI design grâce à \nnos bootcamps à temps plein ou temps partiel.",
                       "link": "https://www.ironhack.com/fr/campus/madrid",
                       "title": "Ironhack Madrid - Bootcamps en Développement Web et UX/UI ...",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ironhack is a global tech school with campuses in Miami, Madrid, Barcelona, \nParis, Berlin, Munich, Amsterdam, Mexico City, Lisbon, Bogotá, and São Paulo.",
                       "link": "https://blog.ironhack.com/es/madrid-2-2/",
                       "title": "Madrid (ES) | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "No Results Found. The page you requested could not be found. Try refining your \nsearch, or use the navigation above to locate the post.",
                       "link": "https://blog.ironhack.com/madrid-2/page/6/",
                       "title": "Madrid (EN) | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "In May this year, I was at a point in my life that many of you will identify with. I had \nbeen studying for the last 8 years of my life, architecture degree for 7 of them…",
                       "link": "https://blog.ironhack.com/es/madrid-2-2/page/3/",
                       "title": "Madrid (ES) | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ariel Deschapell aka @NotASithLord graduated Ironhack WebDev program in \n2016. He has gone on to work as a developer in the South Florida Tech industry.",
                       "link": "https://blog.ironhack.com/es/campus-de-madrid/page/4/",
                       "title": "Campus de Madrid - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "In May this year, I was at a point in my life that many of you will identify with. I had \nbeen studying for the last 8 years of my life, architecture degree for 7 of them…",
                       "link": "https://blog.ironhack.com/es/campus-de-madrid/page/5/",
                       "title": "Campus de Madrid - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Building.co is a collaborative workspace that accommodates local tech \ncompanies; it also happens to be home to the Ironhack Miami campus. It's loved \nfor the ...",
                       "link": "https://blog.ironhack.com/es/madrid-2-2/page/10/",
                       "title": "Madrid (ES) | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "First impressions count, and the window in which they're formed is usually small. \nThis is why we're mindful of every minute, from the moment the students walk ...",
                       "link": "https://blog.ironhack.com/es/campus-de-madrid/page/12/",
                       "title": "Campus de Madrid - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Jimmy: Alright, so we are recording. Welcome back to another Ironhack Student \nPodcast, I am Jimmy. And in case you don't know what Ironhack is we are a ...",
                       "link": "https://blog.ironhack.com/es/campus-de-madrid/page/10/",
                       "title": "Campus de Madrid - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Since 2013 Ironhack has been helping people answer the \\",
                       "link": "",
                       "title": "",
                       "city": ""
                   },
                   {
                       "snippet": "for me\\\" question. We've helped people change careers into the field of their ...\"",
                       "link": "https://blog.ironhack.com/es/madrid-2-2/page/8/",
                       "title": "Madrid (ES) | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Badi, a simple and practical app, connects tenants and their vacant rooms with \npeople searching for just that: rooms for rent in a shared space. Available on the\n ...",
                       "link": "https://blog.ironhack.com/es/madrid-2-2/page/9/",
                       "title": "Madrid (ES) | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "At Ironhack, we like to interview career professionals in order to bring our \naudience real industry insight. This time we decided not to reach out to a \nprofessional ...",
                       "link": "https://blog.ironhack.com/es/campus-de-madrid/page/11/",
                       "title": "Campus de Madrid - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Aug 1, 2016 ... At Ironhack, we like to interview career professionals in order to bring our \naudience real industry insight. This time we decided not to reach out ...",
                       "link": "http://blog.ironhack.com/category/madrid/",
                       "title": "Madrid Archives | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ariel Deschapell aka @NotASithLord graduated Ironhack WebDev program in \n2016. He has gone on to work as a developer in the South Florida Tech industry.",
                       "link": "https://blog.ironhack.com/es/madrid-2-2/page/2/",
                       "title": "Madrid (ES) | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "¿Cómo ser freelance y no morir en el intento? by Eva Peris | Tuesday, December \n4, 2018. Para venir al evento es IMPRESCINDIBLE APUNTARSE AQUÍ ...",
                       "link": "https://blog.ironhack.com/event_tag/madrid/",
                       "title": "madrid | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Apr 12, 2016 ... College students and graduates share a common predicament: insufficient \ngroundwork necessary to find a job. Despite students” exponential ...",
                       "link": "https://blog.ironhack.com/es/campus-de-madrid/page/13/",
                       "title": "Campus de Madrid - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ironhack is an international school with courses in Web Development and UX/UI \nDesign in Madrid, Barcelona, Miami, Paris, and Mexico City. Ironhack uses a ...",
                       "link": "https://www.ironhack.com/en/team",
                       "title": "Meet the Ironhack Team",
                       "city": "madrid"
                   },
                   {
                       "snippet": "29 May 2017 ... Diana Álvarez: Bueno, pues yo me llamo Diana Álvarez Concepción, hice el \nfullstack web developement bootcamp en Madrid. Jimmy Flores: ...",
                       "link": "https://blog.ironhack.com/es/campus-de-madrid/",
                       "title": "Campus de Madrid - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Amsterdam Barcelona Berlin Bogotá Lisbon Madrid Mexico City Miami Munich \nParis São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL 33132",
                       "link": "https://www.ironhack.com/en/legal-notice",
                       "title": "Development Bootcamp Legal notice | Ironhack",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Diana Álvarez: Bueno, pues yo me llamo Diana Álvarez Concepción, hice el \nfullstack web developement bootcamp en Madrid. Jimmy Flores: ¿Qué ha sido tu\n ...",
                       "link": "https://blog.ironhack.com/es/madrid-2-2/page/7/",
                       "title": "Madrid (ES) | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Amsterdam Barcelona Berlin Bogotá Lisbon Madrid Mexico City Miami Munich \nParis São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL 33132",
                       "link": "https://www.ironhack.com/en/web-barcelona-14",
                       "title": "Ironhack - Bootcamps and Courses in Web Coding and UX/UI Design",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Beca wallapop, 200,000€ para que mas mujeres estudien programación y \ndiseño en Ironhack. by Alberto Marcos | Wednesday, March 8, 2017 | Barcelona,\n ...",
                       "link": "https://blog.ironhack.com/es/category/madrid-es/",
                       "title": "Madrid Archives - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ironhack OpenHouse (Puertas abiertas) – Come Visit us! Ironhack Campus BCN \n- C/Pamplona, 96 - 08018. Next Events ». Check out our locations. Madrid ...",
                       "link": "https://blog.ironhack.com/",
                       "title": "Ironhack Blog: Home (EN)",
                       "city": "madrid"
                   },
                   {
                       "snippet": "A Semana de Contratação (Hiring Week), por Payvision María Cuesta Monge, \nHR Advisor Quando você se dedica aos Recursos Humanos, mais ...",
                       "link": "https://blog.ironhack.com/es/campus-de-madrid/page/8/",
                       "title": "Campus de Madrid - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Intro The JavaScript ecosystem is absolutely massive. JavaScript is everywhere \nand the community of developers surrounding it are constantly coming up with ...",
                       "link": "https://blog.ironhack.com/es/madrid-2-2/page/4/",
                       "title": "Madrid (ES) | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Hoje começamos a série de posts explicando coisas que você pode fazer \naprendendo Javascript. Você sabia que você pode aprender a voar drones \nsabendo ...",
                       "link": "https://blog.ironhack.com/es/madrid-2-2/page/5/",
                       "title": "Madrid (ES) | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Você já se perguntou o que a Ironhack tem de tão diferente da concorrência? No \nartigo de hoje vamos explicar por quais motivos ela é a melhor opção!",
                       "link": "https://blog.ironhack.com/es/campus-de-madrid/page/7/",
                       "title": "Campus de Madrid - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ironhack is a global tech school with campuses in Miami, Madrid, Barcelona, \nParis, Berlin, Munich, Amsterdam, Mexico City, Lisbon, Bogotá, and São Paulo.",
                       "link": "https://blog.ironhack.com/es/campus-de-madrid/page/2/",
                       "title": "Campus de Madrid - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Diana Álvarez: Bueno, pues yo me llamo Diana Álvarez Concepción, hice el \nfullstack web developement bootcamp en Madrid. Jimmy Flores: ¿Qué ha sido tu\n ...",
                       "link": "https://blog.ironhack.com/es/portal/",
                       "title": "Portal - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "28 ago. 2018 ... Se você está pensando em mergulhar no universo de desenvolvimento web, \nmuito provavelmente já teve uma dessas duas dúvidas – quem ...",
                       "link": "https://blog.ironhack.com/es/madrid-2-2/page/6/",
                       "title": "Madrid (ES) | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "27 Abr 2017 ... Este jueves 20 de abril, tuvimos el placer de recibir a las ganadoras de la Beca \nWallapop en nuestros Campus de Madrid y Barcelona.",
                       "link": "http://blog.ironhack.com/tag/campus-madrid/",
                       "title": "Campus Madrid Archives | Blog de Ironhack",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ironhack is an immersive bootcamp with locations in Madrid, Barcelona, and \nMiami, offering full-time and part-time courses in Web Development and UX/UI ...",
                       "link": "http://code.ironhack.com/ironhackscholars/",
                       "title": "The Ironhack Scholars Program: Learn in-demand tech skills and ...",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ganadoras Beca Wallapop Madrid. by Jimmy Flores on abril 27, 2017 in with 0 \nReplies. Recibimos a algunas de las ganadoras de la Beca Wallapop.",
                       "link": "http://blog.ironhack.com/ganadoras-beca-wallapop-en-campus-madrid-y-barcelona/wallapop-ganadoras/",
                       "title": "Ganadoras Beca Wallapop Madrid | Blog de Ironhack",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Apply to Ironhack Web Development Bootcamp and UX/UI Design Bootamp.",
                       "link": "https://www.ironhack.com/en/web-development-bootcamp/apply",
                       "title": "Apply to Ironhack's Coding or UX/UI Design Bootcamps",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Apr 18, 2016 ... Madrid and Barcelona can provide you with opportunities to learn academically, \nto learn a new language, and to advance your future career.",
                       "link": "https://blog.ironhack.com/2016/04/18/why-study-abroad-and-lean-to-code-in-spain/",
                       "title": "Why Study Abroad and Learn to Code in Spain? - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "full stack web development bootcamp madrid. by Jimmy Flores on mayo 29, 2017 \nin with 0 Replies · Previous Post Los títulos universitarios son una broma # ...",
                       "link": "http://blog.ironhack.com/los-titulos-universitarios-son-una-broma-tu-ironhack-bootcamp-si-sirve/full-stack-web-development-bootcamp-madrid/",
                       "title": "full stack web development bootcamp madrid | Blog de Ironhack",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Amsterdam Barcelona Berlin Bogotá Lisbon Madrid Ciudad de México Miami \nMunich Paris São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL ...",
                       "link": "https://www.ironhack.com/application/start.php?program=mobile-barcelona-14&lang=es",
                       "title": "Ironhack - Bootcamps y Cursos en Programación Web y Diseño UX/UI",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Our latest articles Inside Cabify – Our alumni experience by Alberto Marcos | Aug \n1, 2016 | Alumni, Madrid At Ironhack, we like to interview career professionals ...",
                       "link": "https://blog.ironhack.com/category/ironhack-general-en/",
                       "title": "Ironhack General Archives - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "20 Feb 2019 ... Estamos orgullosos de anunciar que el We/Code, el festival más grande de \nEuropa para iniciarse en la programación, vuelve a Madrid.",
                       "link": "https://blog.ironhack.com/wp-event/we-code-programa-tu-propia-landing-page/",
                       "title": "WE/CODE : Programa tu propia Landing page - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Nov 30, 2018 ... Of this many, one is particularly useful: Cabify offers a 10€ Boucher to take you \nfrom Madrid Atocha Station or Barcelona Sans Station to your ...",
                       "link": "http://materials.ironhack.com/s/BkcVZO-CQ",
                       "title": "Cabify Scholarships - UXUI Technical Challenge - HackMD",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Amsterdam Barcelona Berlijn Bogotá Lisbon Madrid Mexico Stad Miami Munich \nParijs São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL 33132",
                       "link": "https://www.ironhack.com/nl/locaties/bogota",
                       "title": "Ironhack Bogotá Web Development & UX/UI Design Bootcamps",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Amsterdam Barcelona Berlin Bogotá Lisbon Madrid Ciudad de México Miami \nMunich Paris São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL ...",
                       "link": "https://www.ironhack.com/es/cursos/data-analytics-bootcamp",
                       "title": "Curso de Data Analytics en Miami | Bootcamp de 9 Semanas ...",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Jun 1, 2016 ... Co-Founder of Mindly (made in Silicon Valley), Madrid native, woman and, of \ncourse, Ironhacker, Marta Fonda tells us about her Ironhack ...",
                       "link": "http://blog.ironhack.com/ironhack-experience-by-marta-fonda/",
                       "title": "Ironhack Experience By Marta Fonda | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Diana Álvarez: Bueno, pues yo me llamo Diana Álvarez Concepción, hice el \nfullstack web developement bootcamp en Madrid. Jimmy Flores: ¿Qué ha sido tu\n ...",
                       "link": "https://blog.ironhack.com/es/home-es/page/9/",
                       "title": "Home – (ES) | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ironhack is een internationale school met cursussen in Web Development en UX/\nUI Design in Madrid, Barcelona, Miami, Parijs en Mexico-stad. Ironhack maakt ...",
                       "link": "https://www.ironhack.com/nl/team",
                       "title": "Ontmoet het Ironhack-team",
                       "city": "madrid"
                   },
                   {
                       "snippet": "4 Ene 2019 ... Click to Register: Click to Register. Organizer. Ironhack Madrid. Website: \nOrganizer's Website. Venue. Matadero Madrid. Paseo de la Chopera, ...",
                       "link": "https://blog.ironhack.com/wp-event/uxperience-8-0-voice-user-interfaces-con-webedia-google-y-amazon/",
                       "title": "UXPERIENCE 8.0: Voice User Interfaces con Webedia, Google y ...",
                       "city": "madrid"
                   },
                   {
                       "snippet": "29 May 2017 ... Diana Álvarez: Bueno, pues yo me llamo Diana Álvarez Concepción, hice el \nfullstack web developement bootcamp en Madrid. Jimmy Flores: ...",
                       "link": "https://blog.ironhack.com/es/2017/05/29/entre-la-bbc-como-programadora-con-39-anos-y-sin-experiencia-previa/",
                       "title": "Entré a la BBC como programadora (con 39 años y sin experiencia ...",
                       "city": "madrid"
                   },
                   {
                       "snippet": "May 29, 2017 ... Diana Álvarez: Bueno, pues yo me llamo Diana Álvarez Concepción, hice el \nfullstack web developement bootcamp en Madrid. Jimmy Flores: ...",
                       "link": "https://blog.ironhack.com/es/home-es/5/",
                       "title": "Home – (ES) | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ironhack Campus BCN - C/Pamplona, 96 - 08018. Next Events » · « Previous \nEvents. Check out our locations. Madrid · Barcelona · Miami · Paris · Mexico City ...",
                       "link": "https://blog.ironhack.com/page/2/?wordfence_lh=1&hid=95086C728F811F0F73BC26F456EDC18F",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "La Data Week ha llegado a Madrid! Para celebrar nuestro nuevo Bootcamp de \nData Analytics, hemos organizado una conferencia muy especial: La Data Week.",
                       "link": "https://code.ironhack.com/data-week-madrid/",
                       "title": "Campus Ironhack Madrid",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Amsterdam Barcelona Berlin Bogotá Lisbon Madrid Mexiko-Stadt Miami Munich \nParis São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL 33132",
                       "link": "https://www.ironhack.com/de/standorte/berlin",
                       "title": "Ironhack Berlin Webentwicklungs- und UX/UI-Design-Bootcamps",
                       "city": "madrid"
                   },
                   {
                       "snippet": "... Design grâce à nos cours à temps plein ou partiel. Web Development \nBootcamp et formation en UX/UI Design à Madrid, Barcelona, Miami, Paris et \nMéxico.",
                       "link": "https://www.ironhack.com/fr",
                       "title": "Ironhack Tech School: Cours intensifs en Développement Web et ...",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Amsterdam Barcelona Berlin Bogotá Lisbon Madrid Mexiko-Stadt Miami Munich \nParis São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL 33132",
                       "link": "https://www.ironhack.com/de/standorte/paris",
                       "title": "Ironhack Paris Webentwicklungs- und UX/UI-Design-Bootcamps",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Amsterdã Barcelona Berlim Bogotá Lisbon Madrid Cidade do México Miami \nMunich Paris São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL ...",
                       "link": "https://www.ironhack.com/br/locais/barcelona",
                       "title": "Bootcamps de Desenvolvimento Web & UX/UI Design da Ironhack ...",
                       "city": "madrid"
                   },
                   {
                       "snippet": "... students at their new jobs to hear... read more · « Older Entries · Next Entries ». \nOur Upcoming Events. No Events are found. Check out our locations. Madrid ...",
                       "link": "https://blog.ironhack.com/page/4/?wordfence_lh=1&hid=E26218DBFFECFAD756F1161DDAF5D8BD",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Dec 20, 2018 ... At that time, I attended many Meetups, especially in the well-known Google \ncampus in Madrid where one day, by chance, I saw an event led by ...",
                       "link": "https://blog.ironhack.com/2018/12/20/change-your-life-from-architecture-to-ux-ui-design%E2%80%8A-%E2%80%8Amy-journey/",
                       "title": "Change your life! From architecture to UX/UI Design — My journey ...",
                       "city": "madrid"
                   },
                   {
                       "snippet": "... students at their new jobs to hear... read more · « Older Entries · Next Entries ». \nOur Upcoming Events. No Events are found. Check out our locations. Madrid ...",
                       "link": "https://blog.ironhack.com/page/4/?wordfence_lh=1&hid=E26218DBFFECFAD756F1161DDAF5D8BD",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Dec 20, 2018 ... At that time, I attended many Meetups, especially in the well-known Google \ncampus in Madrid where one day, by chance, I saw an event led by ...",
                       "link": "https://blog.ironhack.com/2018/12/20/change-your-life-from-architecture-to-ux-ui-design%E2%80%8A-%E2%80%8Amy-journey/",
                       "title": "Change your life! From architecture to UX/UI Design — My journey ...",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Amesterdão Barcelona Berlim Bogotá Lisbon Madrid Cidade do México Miami \nMunich Paris São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL ...",
                       "link": "https://www.ironhack.com/pt/cursos",
                       "title": "Aqui tens os nossos Bootcamps: Desenvolvimento Web e UX/UI ...",
                       "city": "madrid"
                   },
                   {
                       "snippet": "We do this through intensive courses in Web Development & UX/UI Design. \nIronhack Madrid campus: Paseo de la Chopera, 14 28045 – Madrid (Spain). \nContact ...",
                       "link": "https://blog.ironhack.com/es/page/10/",
                       "title": "Home – (ES) | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "by Alberto Marcos | April 18, 2016 | Barcelona, Madrid, Web Development | 0 \nComments. Learning a new language, building international connections, and ...",
                       "link": "https://blog.ironhack.com/page/6/?wordfence_lh=1&hid=179AACB67442C188378393C7015B9D1C",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Tú eliges cuándo y dónde quieres hacer estos estudios: puedes escoger entre \nMadrid o Barcelona y entre la modalidad a tiempo completo o a tiempo parcial.",
                       "link": "https://jobandtalent.ironhack.com/",
                       "title": "Ironhack + Jobandtalent",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Feb 7, 2017 ... Alumni · Amsterdam · Barcelona · Berlin · Berlin · Bootcamp · Campus life · Data \nAnalytics · HackShow · Ironhack General · Lisbon · Madrid ...",
                       "link": "https://blog.ironhack.com/2017/02/07/student-podcast-uxui-bootcamp-week-1-wrap/",
                       "title": "Student Podcast: UX/UI Bootcamp Week 1 Wrap Up - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Sonia RocaOutcomes Manager Madrid. Dina KemintzOutcomes Manager Paris. \nDaniel BritoOutcomes Manager Miami. Gemma GarrigaOutcomes Manager ...",
                       "link": "https://www.ironhack.com/es/soporte-de-carrera",
                       "title": "Búsqueda de Trabajo para ex-alumnos de Ironhack & Servicios de ...",
                       "city": "madrid"
                   },
                   {
                       "snippet": "by Alberto Marcos | August 1, 2016 | Alumni, Madrid | 0 Comments. At Ironhack, \nwe like to interview career professionals in order to bring our audience real ...",
                       "link": "https://blog.ironhack.com/page/3/?wordfence_lh=1&hid=36F7AD87CB646E75D7CCFB8F9CE74C7C",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "by Alberto Marcos | February 8, 2017 | Alumni, Desarrollo Web, Madrid | 0 \nComments. ¿Cómo te llamas y en que bootcamp estas? Me llamo Diana Álvarez,\n ...",
                       "link": "https://blog.ironhack.com/es/portal/page/12/",
                       "title": "Portal - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Please get your ticket here: http://bit.ly/2Sp1pUS Learn more about the event on \nour website: http://code.ironhack.com/wecode-lisbon/ After Madrid, Barcelona, ...",
                       "link": "https://blog.ironhack.com/event_category/lisbonevents/",
                       "title": "lisbonevents Archives - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ironhack is a global tech school with campuses in Miami, Madrid, Barcelona, \nParis, Berlin, Munich, Amsterdam, Mexico City, Lisbon, Bogotá, and São Paulo.",
                       "link": "https://blog.ironhack.com/es/page/2/",
                       "title": "Portal - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "... a través de uno de nuestros cursos a tiempo completo o a tiempo parcial. \nBootcamp en Desarrollo Web y Bootcamp en Diseño UX/UI en Madrid, \nBarcelona, ...",
                       "link": "https://www.ironhack.com/cursos/becaforocoches/",
                       "title": "Ironhack Bootcamp Programación Web & Bootcamp Diseño UX/UI",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ironhack OpenHouse (Puertas abiertas) – Come Visit us! Ironhack Campus BCN \n- C/Pamplona, 96 - 08018. « Previous Events. Check out our locations. Madrid ...",
                       "link": "https://blog.ironhack.com/page/3/?wordfence_lh=1&hid=97D063DACB6DCF9336556D1EB45634D8",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "by Alberto Marcos | March 8, 2017 | Barcelona, Desarrollo Web, Diseño UX/UI, \nMadrid | 0 Comments. Feliz día de la mujer! Lo vamos a celebrar anunciando la ...",
                       "link": "https://blog.ironhack.com/es/home-es/page/5/",
                       "title": "Home - (ES) - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "18 Ene 2019 ... Event Category: madridevents. Click to Register: Click to Register. Organizer. \nIronhack Madrid. Website: Organizer's Website. Para venir a este ...",
                       "link": "https://blog.ironhack.com/wp-event/la-fase-cero-de-tu-futuro-by-chechu-salas/",
                       "title": "LA FASE CERO DE TU FUTURO by Chechu Salas - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Jan 18, 2019 ... Alumni · Amsterdam · Barcelona · Berlin · Berlin · Bootcamp · Campus life · Data \nAnalytics · HackShow · Ironhack General · Lisbon · Madrid ...",
                       "link": "https://blog.ironhack.com/author/thomas/",
                       "title": "Thomas Jacquesson, Author at Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "When he's not mentoring students... read more · « Older Entries · Next Entries ». \nOur Upcoming Events. No Events are found. Check out our locations. Madrid ...",
                       "link": "https://blog.ironhack.com/page/5/?wordfence_lh=1&hid=1587FB7C6D51C39A9F409A42FA2421E7",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "by Alberto Marcos | Monday, July 18, 2016 | Barcelona, Madrid. This post was \nwritten by Ironhack co-founder Ariel Quiñones, originally published in September\n ...",
                       "link": "https://blog.ironhack.com/category/barcelona-en/page/2/",
                       "title": "Barcelona | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "read more · « Older Entries · Next Entries ». Our Upcoming Events. No Events are \nfound. Check out our locations. Madrid · Barcelona · Miami · Paris · Mexico City ...",
                       "link": "https://blog.ironhack.com/page/5/?wordfence_lh=1&hid=54C60309372A9A83DE9349FC5D9D9C3C",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "read more · « Older Entries · Next Entries ». Our Upcoming Events. No Events are \nfound. Check out our locations. Madrid · Barcelona · Miami · Paris · Mexico City ...",
                       "link": "https://blog.ironhack.com/page/5/?wordfence_lh=1&hid=54C60309372A9A83DE9349FC5D9D9C3C",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Aplica a Web Development Bootcamp y UX/UI Design Bootcamp de Ironhack.",
                       "link": "https://www.ironhack.com/es/cursos/data-analytics-bootcamp/aplicar",
                       "title": "Aplica a los Bootcamps de Ironhack de Programación o Diseño UX/UI",
                       "city": "madrid"
                   },
                   {
                       "snippet": "by Alberto Marcos | Monday, July 18, 2016 | Barcelona, Madrid. This post was \nwritten by Ironhack co-founder Ariel Quiñones, originally published in September\n ...",
                       "link": "https://blog.ironhack.com/tag/coding-en/",
                       "title": "coding Archives - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Dec 17, 2018 ... Ironhack es una escuela digital que ofrece cursos intensivos de Web \nDevelopment y UX/UI Design. Ya tenemos campus en Madrid, Barcelona, ...",
                       "link": "https://blog.ironhack.com/wp-event/page/10/",
                       "title": "Events Archive - Page 10 of 19 - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ironhack OpenHouse (Puertas abiertas) – Come Visit us! Ironhack Campus BCN \n- C/Pamplona, 96 - 08018. Next Events ». Check out our locations. Madrid ...",
                       "link": "http://blog.ironhack.com/?wordfence_lh=1&hid=0D1DB60599AB9AD578B4C6BE2A711E08",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Dec 21, 2018 ... Alumni · Amsterdam · Barcelona · Berlin · Berlin · Bootcamp · Campus life · Data \nAnalytics · HackShow · Ironhack General · Lisbon · Madrid ...",
                       "link": "https://blog.ironhack.com/category/data-analytics/",
                       "title": "Data Analytics Archives - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "18 Ene 2019 ... Event Category: madridevents. Click to Register: Click to Register. Organizer. \nIronhack Madrid. Website: Organizer's Website. Venue. Ironhack.",
                       "link": "https://blog.ironhack.com/wp-event/democratizando-el-iot-con-thinger-io/",
                       "title": "Democratizando el IoT con Thinger.io - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Dec 4, 2018 ... Ironhack has eight locations in Barcelona, Madrid, Paris, Mexico, Miami, Berlin, \nAmsterdam and Sao Paulo. Check it out our website: ...",
                       "link": "https://blog.ironhack.com/wp-event/ironhack-openhouse-puertas-abiertas-come-visit-us-13/",
                       "title": "Ironhack OpenHouse (Puertas abiertas) - Come Visit us! - Ironhack ...",
                       "city": "madrid"
                   },
                   {
                       "snippet": "by Alberto Marcos | Monday, July 18, 2016 | Barcelona, Madrid. This post was \nwritten by Ironhack co-founder Ariel Quiñones, originally published in September\n ...",
                       "link": "https://blog.ironhack.com/tag/miami-en/",
                       "title": "miami Archives - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ironhack is a global tech school with campuses in Miami, Madrid, Barcelona, \nParis, Berlin, Munich, Amsterdam, Mexico City, Lisbon, Bogotá, and São Paulo.",
                       "link": "https://blog.ironhack.com/tag/bootcamp-en/",
                       "title": "bootcamp Archives - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Ironhack is a global tech school with campuses in Miami, Madrid, Barcelona, \nParis, Berlin, Munich, Amsterdam, Mexico City, Lisbon, Bogotá, and São Paulo.",
                       "link": "https://blog.ironhack.com/tag/bootcamp-en/",
                       "title": "bootcamp Archives - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Feb 6, 2019 ... Ironhack is a global tech school with campuses in Miami, Madrid, Barcelona, \nParis, Berlin, Munich, Amsterdam, Mexico City, Lisbon, Bogotá, ...",
                       "link": "https://blog.ironhack.com/tag/ux-ui/",
                       "title": "UX/UI Archives - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Dec 4, 2018 ... Alumni · Amsterdam · Barcelona · Berlin · Berlin · Bootcamp · Campus life · Data \nAnalytics · HackShow · Ironhack General · Lisbon · Madrid ...",
                       "link": "https://blog.ironhack.com/wp-event/dataxperience/",
                       "title": "DataXperience - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Nuñez de Balboa, 120 - 28006 - Madrid. 636 176 382. mad@ironhack.com. ¿\nNecesitas ayuda para financiar el curso? Nuestras opciones de financiación te ...",
                       "link": "https://code.ironhack.com/web-dev-bootcamp-mad-es-sem/",
                       "title": "Career Support",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Diana Álvarez: Bueno, pues yo me llamo Diana Álvarez Concepción, hice el \nfullstack web developement bootcamp en Madrid. Jimmy Flores: ¿Qué ha sido tu\n ...",
                       "link": "https://blog.ironhack.com/es/category/desarrollo-web-es/",
                       "title": "Desarrollo Web | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Feb 6, 2019 ... Ironhack is a global tech school with campuses in Miami, Madrid, Barcelona, \nParis, Berlin, Munich, Amsterdam, Mexico City, Lisbon, Bogotá, ...",
                       "link": "https://blog.ironhack.com/2019/02/06/ironhack-aims-to-solve-the-tech-talent-gap-in-mexico/",
                       "title": "Ironhack Aims to Solve the Tech Talent Gap in Mexico - Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Inscreve-te no Bootcamp de Web Development e no Bootcamp de UX/UI Design \nda Ironhack.",
                       "link": "https://www.ironhack.com/pt/cursos/ux-ui-design-bootcamp-learn-ux-design/inscrever/curso/5b8fee1b3619ac001afced44",
                       "title": "Inscreve-te nos Bootcamps de Programação e UX/UI Design da ...",
                       "city": "madrid"
                   },
                   {
                       "snippet": "4 Dic 2018 ... Time: 06:30 pm - 08:00 pm. Event Category: madridevents. Event Tags: madrid. \nClick to Register: Click to Register. Organizer. Ironhack Madrid.",
                       "link": "https://blog.ironhack.com/wp-event/como-ser-freelance-y-no-morir-en-el-intento/",
                       "title": "¿Cómo ser freelance y no morir en el intento? | Ironhack Blog",
                       "city": "madrid"
                   },
                   {
                       "snippet": "by Alberto Marcos | August 1, 2016 | Alumni, Madrid | 0 Comments. At Ironhack, \nwe like to interview career professionals in order to bring our audience real ...",
                       "link": "https://blog.ironhack.com/page/7/",
                       "title": "Ironhack Blog | Preparing the next generation of digital creators",
                       "city": "madrid"
                   },
                   {
                       "snippet": "Sep 23, 2016 ... by Alberto Marcos | Monday, August 1, 2016 | Alumni, Madrid. At Ironhack, we \nlike to interview career professionals in order to bring our ...",
                       "link": "https://blog.ironhack.com/author/alberto/page/3/",
                       "title": "Alberto Marcos | Ironhack Blog",
                       "city": "madrid"
                   }][starting_from:starting_from + 10]
    if city == "Barcelona":
        data = [
                   {
                       "snippet": "... of our full time or part time courses. Web Development Bootcamp and UX/UI \nDesign Bootcamp in Madrid, Barcelona, Miami, Paris, Mexico City, Berlin, Bogotá\n, ...",
                       "link": "https://www.ironhack.com/",
                       "title": "Ironhack Web Development Bootcamp & UX/UI Design Bootcamp",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Amsterdam Barcelona Berlin Bogotá Lisbon Madrid Mexico City Miami Munich \nParis São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL 33132",
                       "link": "https://www.ironhack.com/en/web-barcelona-14",
                       "title": "Ironhack - Bootcamps and Courses in Web Coding and UX/UI Design",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Thor completed the Web Development Bootcamp in Ironhack Barcelona and has \nsince worked as a freelancer at our campus. It's been a pleasure having him ...",
                       "link": "https://blog.ironhack.com/locations-barcelona/",
                       "title": "Barcelona (EN) - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Join Ironhack. Do you want to study at Ironhack in Barcelona? Barcelona has an \namazing tech ecosystem with plenty of opportunities for our graduates, we'll ...",
                       "link": "https://www.ironhack.com/br/locais/barcelona",
                       "title": "Barcelona",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Join Ironhack. Do you want to study at Ironhack in Barcelona? Barcelona has an \namazing tech ecosystem with plenty of opportunities for our graduates, we'll ...",
                       "link": "https://www.ironhack.com/nl/locaties/barcelona",
                       "title": "Ironhack Barcelona Web Development & UX/UI Design Bootcamps",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Jan 10, 2019 ... Our latest articles How coding bootcamps crush the college grad unemployment \nproblem by Alberto Marcos | Feb 22, 2017 | Barcelona \\",
                       "link": "https://blog.ironhack.com/category/barcelona-en/",
                       "title": "Barcelona Archives - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Ironhack is a global tech school with campuses in Miami, Madrid, Barcelona, \nParis, Berlin, Munich, Amsterdam, Mexico City, Lisbon, Bogotá, and São Paulo.",
                       "link": "https://blog.ironhack.com/es/locations-barcelona-2/",
                       "title": "Barcelona (ES) | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Dec 20, 2016 ... Marc, our fearless campus manager here in Barcelona, did the honors of sharing \nwith the audience some of Ironhack's biggest wins over the ...",
                       "link": "https://blog.ironhack.com/2016/12/20/coding-bootcamp-graduation-ironhack-barcelona-hackshow/",
                       "title": "Coding Bootcamp Graduation - Ironhack's Barcelona HackShow ...",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Thor completed the Web Development Bootcamp in Ironhack Barcelona and has \nsince worked as a freelancer at our campus. It's been a pleasure having him ...",
                       "link": "https://blog.ironhack.com/es/locations-barcelona-2/page/10/",
                       "title": "Barcelona (ES) | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Learning a new language, building international connections, and gaining \nvaluable work experience are all possibilities when learning to code abroad. \nSpain is ...",
                       "link": "https://blog.ironhack.com/es/locations-barcelona-2/page/11/",
                       "title": "Barcelona (ES) | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Jimmy: Alright, so we are recording. Welcome back to another Ironhack Student \nPodcast, I am Jimmy. And in case you don't know what Ironhack is we are a ...",
                       "link": "https://blog.ironhack.com/es/campus-de-barcelona/page/10/",
                       "title": "Campus de Barcelona - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Since 2013 Ironhack has been helping people answer the \\",
                       "link": "",
                       "title": "",
                       "city": ""
                   },
                   {
                       "snippet": "for me\\\" question. We've helped people change careers into the field of their ...\"",
                       "link": "https://blog.ironhack.com/es/locations-barcelona-2/page/8/",
                       "title": "Barcelona (ES) | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "In May this year, I was at a point in my life that many of you will identify with. I had \nbeen studying for the last 8 years of my life, architecture degree for 7 of them…",
                       "link": "https://blog.ironhack.com/es/campus-de-barcelona/page/5/",
                       "title": "Campus de Barcelona - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "At Ironhack, we like to interview career professionals in order to bring our \naudience real industry insight. This time we decided not to reach out to a \nprofessional ...",
                       "link": "https://blog.ironhack.com/es/campus-de-barcelona/page/11/",
                       "title": "Campus de Barcelona - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Badi, a simple and practical app, connects tenants and their vacant rooms with \npeople searching for just that: rooms for rent in a shared space. Available on the\n ...",
                       "link": "https://blog.ironhack.com/es/locations-barcelona-2/page/9/",
                       "title": "Barcelona (ES) | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Ariel Deschapell aka @NotASithLord graduated Ironhack WebDev program in \n2016. He has gone on to work as a developer in the South Florida Tech industry.",
                       "link": "https://blog.ironhack.com/es/locations-barcelona-2/page/2/",
                       "title": "Barcelona (ES) | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Ironhack is an international school with courses in Web Development and UX/UI \nDesign in Madrid, Barcelona, Miami, Paris, and Mexico City. Ironhack uses a ...",
                       "link": "https://www.ironhack.com/en/team",
                       "title": "Meet the Ironhack Team",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Jul 18, 2016 ... Elina Nenonen completed the most recent cohort of the Web Development \nBootcamp in Barcelona and was one of the first students to be part ...",
                       "link": "https://blog.ironhack.com/category/barcelona-en/page/2/",
                       "title": "Barcelona | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Data Week is coming to Barcelona! To celebrate our newly created Data \nAnalytics Bootcamp we have organized a very special conference line-up: Data \nWeek.",
                       "link": "https://code.ironhack.com/data-week-barcelona/",
                       "title": "Campus Ironhack Barcelona",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Sep 23, 2016 ... Badi now is on TV with a spot and the app was developed by Alberto Betalla, ex-\nLead Instructor at Ironhack Barcelona, and two Ironhackers, ...",
                       "link": "https://blog.ironhack.com/2016/09/23/badi-ironhack-million-euro-investment/",
                       "title": "2 students and an ex-Lead Teacher from Ironhack develop new app ...",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Sep 23, 2016 ... by Alberto Marcos | Friday, June 17, 2016 | Barcelona. First impressions count, \nand the window in which they're formed is usually small. This is ...",
                       "link": "https://blog.ironhack.com/tag/barcelona-en/",
                       "title": "Barcelona Archives - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Jun 10, 2016 ... Elina Nenonen completed the most recent cohort of the Web Development \nBootcamp in Barcelona and was one of the first students to be part ...",
                       "link": "https://blog.ironhack.com/2016/06/10/elina-ux-designer-ironhacker/",
                       "title": "Elina: UX Designer & Ironhacker! - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Barcelona Ironhack Bootcamp. by Lilit D'Elia on July 22, 2016 in with 0 Replies · \nPrevious Post Program your future in Barcelona ...",
                       "link": "http://blog.ironhack.com/program-future-barcelona/hectorges-27-3/",
                       "title": "Barcelona Ironhack Bootcamp | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Amsterdam Barcelona Berlin Bogotá Lisbon Madrid Ciudad de México Miami \nMunich Paris São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL ...",
                       "link": "https://www.ironhack.com/application/start.php?program=mobile-barcelona-14&lang=es",
                       "title": "Ironhack - Bootcamps y Cursos en Programación Web y Diseño UX/UI",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Amsterdam Barcelona Berlijn Bogotá Lisbon Madrid Mexico Stad Miami Munich \nParijs São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL 33132",
                       "link": "https://www.ironhack.com/nl/locaties/bogota",
                       "title": "Ironhack Bogotá Web Development & UX/UI Design Bootcamps",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "12 Abr 2016 ... College students and graduates share a common predicament: insufficient \ngroundwork necessary to find a job. Despite students” exponential ...",
                       "link": "https://blog.ironhack.com/es/campus-de-barcelona/page/13/",
                       "title": "Campus de Barcelona - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "O ano já entrou em ritmo acelerado. Isso significa que é o momento de se \npreparar para os desafios profissionais do ano — principalmente, se você quiser \nse ...",
                       "link": "https://blog.ironhack.com/es/campus-de-barcelona/",
                       "title": "Campus de Barcelona - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Aprender Desenvolvimento Web ou Design UX/UI talvez seja a melhor escolha \npara um Gerente de Produto. Três ex-alunos da Ironhack Barcelona explicam ...",
                       "link": "https://blog.ironhack.com/es/locations-barcelona-2/page/7/",
                       "title": "Barcelona (ES) | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Entré a la BBC como programadora (con 39 años y sin experiencia previa). by \nAlberto Marcos | Monday, May 29, 2017 | Alumni, Barcelona, Desarrollo Web.",
                       "link": "https://blog.ironhack.com/es/category/barcelona-es/",
                       "title": "Barcelona | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Apply to Ironhack. And join a thriving community of people who love what they do\n. I want to attend this campus. Miami. Amsterdam, Barcelona, Berlin, Bogotá ...",
                       "link": "https://www.ironhack.com/en/web-development-bootcamp/apply",
                       "title": "Apply to Ironhack's Coding or UX/UI Design Bootcamps",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Apply to Ironhack. And join a thriving community of people who love what they do\n. I want to attend this campus. Miami. Amsterdam, Barcelona, Berlin, Bogotá ...",
                       "link": "https://www.ironhack.com/en/web-development-bootcamp/apply",
                       "title": "Apply to Ironhack's Coding or UX/UI Design Bootcamps",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Thor completed the Web Development Bootcamp in Ironhack Barcelona and has \nsince worked as a freelancer at our campus. It's been a pleasure having him ...",
                       "link": "https://blog.ironhack.com/page/2/?wordfence_lh=1&hid=468C0E8C2407061A891445490CC9DAEB",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "by Alberto Marcos | September 23, 2016 | Alumni, Barcelona | 0 Comments. Badi, \na simple and practical app, connects tenants and their vacant rooms with ...",
                       "link": "https://blog.ironhack.com/page/4/?wordfence_lh=1&hid=95086C728F811F0F73BC26F456EDC18F",
                       "title": "Coding Bootcamp Graduation – Ironhack's Barcelona HackShow",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "... OpenHouse (Puertas abiertas) – Come Visit us! Ironhack Campus BCN - C/\nPamplona, 96 - 08018. Next Events ». Check out our locations. Madrid · \nBarcelona ...",
                       "link": "https://blog.ironhack.com/",
                       "title": "Ironhack Blog: Home (EN)",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Três ex-alunos da Ironhack Barcelona explicam como impulsionaram suas \ncarreiras após ganharem habilidades digitais através de um bootcamp. Existem\n ...",
                       "link": "https://blog.ironhack.com/es/campus-de-barcelona/page/8/",
                       "title": "Campus de Barcelona - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Se você está pensando em mergulhar no universo de desenvolvimento web, \nmuito provavelmente já teve uma dessas duas dúvidas – quem sabe até ambas.",
                       "link": "https://blog.ironhack.com/es/locations-barcelona-2/page/6/",
                       "title": "Barcelona (ES) | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Amsterdam Barcelona Berlin Bogotá Lisbon Madrid Mexico City Miami Munich \nParis São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL 33132",
                       "link": "https://www.ironhack.com/en/legal-notice",
                       "title": "Development Bootcamp Legal notice | Ironhack",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Hoje começamos a série de posts explicando coisas que você pode fazer \naprendendo Javascript. Você sabia que você pode aprender a voar drones \nsabendo ...",
                       "link": "https://blog.ironhack.com/es/locations-barcelona-2/page/5/",
                       "title": "Barcelona (ES) | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Um uso muito popular de JavaScript é a criação de apresentações como se \nfossem websites. Quem precisa de PowerPoint? Usando a biblioteca RevealJS \nisso ...",
                       "link": "https://blog.ironhack.com/es/campus-de-barcelona/page/6/",
                       "title": "Campus de Barcelona - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "27 Abr 2017 ... Este jueves 20 de abril, tuvimos el placer de recibir a las ganadoras de la Beca \nWallapop en nuestros Campus de Madrid y Barcelona.",
                       "link": "http://blog.ironhack.com/tag/campus-barcelona/",
                       "title": "Campus Barcelona Archives | Blog de Ironhack",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Amsterdam Barcelona Berlijn Bogotá Lisbon Madrid Mexico Stad Miami Munich \nParijs São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL 33132",
                       "link": "https://www.ironhack.com/nl/locaties/bogota",
                       "title": "Ironhack Bogotá Web Development & UX/UI Design Bootcamps",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Apr 18, 2016 ... Madrid and Barcelona can provide you with opportunities to learn academically, \nto learn a new language, and to advance your future career.",
                       "link": "https://blog.ironhack.com/2016/04/18/why-study-abroad-and-lean-to-code-in-spain/",
                       "title": "Why Study Abroad and Learn to Code in Spain? - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Elina Nenonen completed the most recent cohort of the Web Development \nBootcamp in Barcelona and was one of the first students to be part of the new ...",
                       "link": "https://blog.ironhack.com/category/uxui-design/",
                       "title": "UX/UI Design Archives - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "With the help of JobsBCN, SeedRocket, Barcinno, The Barcelona PHP Meetup \nGroup and BarcelonaJS we connected the people […] Continue Reading ...",
                       "link": "http://blog.ironhack.com/tag/tech/",
                       "title": "tech Archives | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Elina Nenonen completed the most recent cohort of the Web Development \nBootcamp in Barcelona and was one of the first students to be part of the new ...",
                       "link": "https://blog.ironhack.com/page/4/?wordfence_lh=1&hid=468C0E8C2407061A891445490CC9DAEB",
                       "title": "Coding Bootcamp Graduation – Ironhack's Barcelona HackShow",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Thor completed the Web Development Bootcamp in Ironhack Barcelona and has \nsince worked as a freelancer at our campus. It's been a pleasure having him ...",
                       "link": "https://blog.ironhack.com/page/4/?wordfence_lh=1&hid=0B68DD2B9AFE967D94CF28B7B272C3BC",
                       "title": "Coding Bootcamp Graduation – Ironhack's Barcelona HackShow",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Dec 4, 2018 ... Ironhack Barcelona - UX Design & Tech School. Website: Organizer's Website. \nVenue. Ironhack Campus BCN. C/Pamplona, 96 - 08018.",
                       "link": "https://blog.ironhack.com/wp-event/from-ux-to-service-design/",
                       "title": "From UX to Service Design - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "by Alberto Marcos | May 29, 2017 | Alumni, Barcelona, Desarrollo Web | 0 \nComments. Diana Álvarez: Bueno, pues yo me llamo Diana Álvarez Concepción, \nhice ...",
                       "link": "https://blog.ironhack.com/es/portal/",
                       "title": "Portal - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Coding Bootcamp Graduation – Ironhack's Barcelona HackShow. Dec 20, 2016. \nThe 8-weeks of a coding bootcamp is never easy. Not for the students or for us, ...",
                       "link": "https://blog.ironhack.com/page/4/?wordfence_lh=1&hid=2B1B5868867FBD800CE00D22AD707D1A",
                       "title": "Coding Bootcamp Graduation – Ironhack's Barcelona HackShow",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Feb 23, 2017 ... by Alberto Marcos | Wednesday, February 22, 2017 | Barcelona. “53.6 percent, of \nbachelor's degree-holders under the age of 25 last year were ...",
                       "link": "https://blog.ironhack.com/author/alberto/page/2/",
                       "title": "Alberto Marcos | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Coding Bootcamp Graduation – Ironhack's Barcelona HackShow. Dec 20, 2016. \nThe 8-weeks of a coding bootcamp is never easy. Not for the students or for us, ...",
                       "link": "https://blog.ironhack.com/page/4/?wordfence_lh=1&hid=2B1B5868867FBD800CE00D22AD707D1A",
                       "title": "Coding Bootcamp Graduation – Ironhack's Barcelona HackShow",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Feb 23, 2017 ... by Alberto Marcos | Wednesday, February 22, 2017 | Barcelona. “53.6 percent, of \nbachelor's degree-holders under the age of 25 last year were ...",
                       "link": "https://blog.ironhack.com/author/alberto/page/2/",
                       "title": "Alberto Marcos | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Ironhack is een internationale school met cursussen in Web Development en UX/\nUI Design in Madrid, Barcelona, Miami, Parijs en Mexico-stad. Ironhack maakt ...",
                       "link": "https://www.ironhack.com/nl/team",
                       "title": "Ontmoet het Ironhack-team",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Amsterdam Barcelona Berlin Bogotá Lisbon Madrid Ciudad de México Miami \nMunich Paris São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL ...",
                       "link": "https://www.ironhack.com/es/cursos/data-analytics-bootcamp",
                       "title": "Curso de Data Analytics en Miami | Bootcamp de 9 Semanas ...",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Coding Bootcamp Graduation – Ironhack's Barcelona HackShow. Dec 20, 2016. \nThe 8-weeks of a coding bootcamp is never easy. Not for the students or for us, ...",
                       "link": "https://blog.ironhack.com/page/4/?wordfence_lh=1&hid=B321A3A8EC0FFBC2624B64E5871D3492",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Jun 17, 2016 ... For the last Barcelona cohort, we organized an oceanfront welcome party for \nOrientation. It all began back in the classroom, with a warm ...",
                       "link": "https://blog.ironhack.com/2016/06/17/nice-teach-first-day-ironhack/",
                       "title": "Nice to teach you! First day at Ironhack - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Sep 1, 2016 ... With the help of JobsBCN, SeedRocket, Barcinno, The Barcelona PHP Meetup \nGroup and ... Our Ironhack Barcelona Campus transforms […].",
                       "link": "http://blog.ironhack.com/category/events/",
                       "title": "Events Archives | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Ironhack Campus BCN - C/Pamplona, 96 - 08018. Next Events » · « Previous \nEvents. Check out our locations. Madrid · Barcelona · Miami · Paris · Mexico City ...",
                       "link": "https://blog.ironhack.com/page/2/?wordfence_lh=1&hid=937717490B4F08D0609479E758D08C27",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Amsterdam Barcelona Berlin Bogotá Lisbon Madrid Mexiko-Stadt Miami Munich \nParis São Paulo · Ironhack Logo 990 Biscayne Blvd. Ste 503 - Miami FL 33132",
                       "link": "https://www.ironhack.com/de/standorte/berlin",
                       "title": "Ironhack Berlin Webentwicklungs- und UX/UI-Design-Bootcamps",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Career Support. Immersive & In-person. Full-Time or Part-Time. MIAMI - \nBARCELONA - MADRID - PARIS - MEXICO. Course Syllabus - Full Stack Design\n ...",
                       "link": "https://code.ironhack.com/web-development-and-ux-ui-design-ironhack/",
                       "title": "Transform your career with intensive courses in Web Development ...",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "by Alberto Marcos | September 23, 2016 | Alumni, Barcelona | 0 Comments. Badi, \na simple and practical app, connects tenants and their vacant rooms with ...",
                       "link": "https://blog.ironhack.com/page/6/?wordfence_lh=1&hid=C501BCA28A7BD58C7E16208D6222BCB0",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "... (Puertas abiertas) – Come Visit us! Ironhack Campus BCN - C/Pamplona, 96 - \n08018. « Previous Events. Check out our locations. Madrid · Barcelona · Miami ...",
                       "link": "https://blog.ironhack.com/page/3/?wordfence_lh=1&hid=A4484A0CEBEC699DCDAE0571299D4D19",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "... our students built from scratch during... read more · Next Entries ». Our \nUpcoming Events. No Events are found. Check out our locations. Madrid · \nBarcelona ...",
                       "link": "https://blog.ironhack.com/page/6/?wordfence_lh=1&hid=E4908CEEEA6388B6B2E1BA9BFF58A395",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Thor completed the Web Development Bootcamp in Ironhack Barcelona and has \nsince worked as a freelancer at our campus. It's been a pleasure having him ...",
                       "link": "https://blog.ironhack.com/page/4/?wordfence_lh=1&hid=694745EAFF47F21D586429B84D384B5A",
                       "title": "Coding Bootcamp Graduation – Ironhack's Barcelona HackShow",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Dina KemintzOutcomes Manager Paris. Daniel BritoOutcomes Manager Miami. \nGemma GarrigaOutcomes Manager Barcelona. Únete a Ironhack ...",
                       "link": "https://www.ironhack.com/es/soporte-de-carrera",
                       "title": "Búsqueda de Trabajo para ex-alumnos de Ironhack & Servicios de ...",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Jun 1, 2016 ... Thor completed the Web Development Bootcamp in Ironhack Barcelona and has \nsince worked as a freelancer at our campus. It's been a ...",
                       "link": "http://blog.ironhack.com/2016/06/01/mr-thor-alumni-freelancer-ta/",
                       "title": "Mr Thor: Alumni, Freelancer & TA! | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Ironhack is a global tech school with campuses in Miami, Madrid, Barcelona, \nParis, Berlin, Munich, Amsterdam, Mexico City, Lisbon, Bogotá, and São Paulo.",
                       "link": "https://blog.ironhack.com/tag/bootcamp-en/",
                       "title": "bootcamp Archives - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "by Alberto Marcos | April 18, 2016 | Barcelona, Madrid, Web Development | 0 \nComments. Learning a new language, building international connections, and ...",
                       "link": "http://blog.ironhack.com/page/4/?wordfence_logHuman=1&hid=2FCDCAB0451670A4F5A2B5A3562AB602",
                       "title": "Ironhack Blog | Preparing the next generation of digital creators",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Thor completed the Web Development Bootcamp in Ironhack Barcelona and has \nsince worked as a freelancer at our campus. It's been a pleasure having him ...",
                       "link": "https://blog.ironhack.com/es/page/7/",
                       "title": "Barcelona",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "... OpenHouse (Puertas abiertas) – Come Visit us! Ironhack Campus BCN - C/\nPamplona, 96 - 08018. Next Events ». Check out our locations. Madrid · \nBarcelona ...",
                       "link": "http://blog.ironhack.com/?wordfence_lh=1&hid=9D2AC294FE8851F45516DEE1F70173AE",
                       "title": "Home (EN) - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "... a través de uno de nuestros cursos a tiempo completo o a tiempo parcial. \nBootcamp en Desarrollo Web y Bootcamp en Diseño UX/UI en Madrid, \nBarcelona, ...",
                       "link": "https://www.ironhack.com/cursos/becaforocoches/",
                       "title": "Ironhack Bootcamp Programación Web & Bootcamp Diseño UX/UI",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "by Alberto Marcos | Monday, May 29, 2017 | Alumni, Barcelona, Desarrollo Web | \n0 comments. Diana Álvarez: Bueno, pues yo me llamo Diana Álvarez ...",
                       "link": "https://blog.ironhack.com/es/2017/05/29/entre-la-bbc-como-programadora-con-39-anos-y-sin-experiencia-previa/",
                       "title": "Entré a la BBC como programadora (con 39 años y sin experiencia ...",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "by Alberto Marcos | Wednesday, March 8, 2017 | Barcelona, Desarrollo Web, \nDiseño UX/UI, Madrid | 0 comments. Feliz día de la mujer! Lo vamos a celebrar ...",
                       "link": "https://blog.ironhack.com/es/2017/03/08/beca-wallapop-ironhack/",
                       "title": "Beca wallapop, 200,000€ para que mas mujeres estudien ...",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Aplicar a Ironhack. Y únete a una comunidad de profesionales que aman su \ntrabajo. Quiero asistir a este campus. Miami. Amsterdam, Barcelona, Berlin, \nBogotá ...",
                       "link": "https://www.ironhack.com/es/cursos/data-analytics-bootcamp/aplicar",
                       "title": "Aplica a los Bootcamps de Ironhack de Programación o Diseño UX/UI",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "2 Dic 2016 ... C/Mossen Pere Ribot 84, Vilassar de Mar, Barcelona. B66279118​ de acuerdo \ncon las presentes bases. TERCERA.- ÁMBITO DE LA ...",
                       "link": "https://www.ironhack.com/assets/landing-pages/assets/meller/meller-scholarship-bases.pdf",
                       "title": "BASES LEGALES DE LA PROMOCIÓN “#Designyourfuture ...",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Elina Nenonen completed the most recent cohort of the Web Development \nBootcamp in Barcelona and was one of the first students to be part of the new ...",
                       "link": "https://blog.ironhack.com/page/4/",
                       "title": "Ironhack Blog | Preparing the next generation of digital creators",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Tú eliges cuándo y dónde quieres hacer estos estudios: puedes escoger entre \nMadrid o Barcelona y entre la modalidad a tiempo completo o a tiempo parcial.",
                       "link": "https://jobandtalent.ironhack.com/",
                       "title": "Ironhack + Jobandtalent",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Jun 24, 2016 ... Elina Nenonen completed the most recent cohort of the Web Development \nBootcamp in Barcelona and was one of the first students to be part ...",
                       "link": "http://blog.ironhack.com/category/en/page/2/",
                       "title": "English Archives | Page 2 of 2 | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Feb 8, 2017 ... Thor completed the Web Development Bootcamp in Ironhack Barcelona and has \nsince worked as a freelancer at our campus. It's been a ...",
                       "link": "https://blog.ironhack.com/es/portal/page/12/",
                       "title": "Portal - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Jul 18, 2016 ... Elina Nenonen completed the most recent cohort of the Web Development \nBootcamp in Barcelona and was one of the first students to be part ...",
                       "link": "https://blog.ironhack.com/tag/tech-en/",
                       "title": "tech Archives - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Jul 18, 2016 ... Elina Nenonen completed the most recent cohort of the Web Development \nBootcamp in Barcelona and was one of the first students to be part ...",
                       "link": "https://blog.ironhack.com/tag/tech-en/",
                       "title": "tech Archives - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Jun 16, 2016 ... During this last Hiring Week in Barcelona, we passed by the letgo offices, a \nSpanish app that allows […] Continue Reading. Alberto Marcos ...",
                       "link": "http://blog.ironhack.com/tag/ironhackers/",
                       "title": "ironhackers Archives | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "May 29, 2017 ... Thor completed the Web Development Bootcamp in Ironhack Barcelona and has \nsince worked as a freelancer at our campus. It's been a ...",
                       "link": "https://blog.ironhack.com/es/home-es/page/10/",
                       "title": "Home – (ES) | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Jun 17, 2016 ... During this last Hiring Week in Barcelona, we passed by the letgo offices, a \nSpanish app that allows […] Continue Reading. Alberto Marcos ...",
                       "link": "http://blog.ironhack.com/tag/education/",
                       "title": "education Archives | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Jul 18, 2016 ... Elina Nenonen completed the most recent cohort of the Web Development \nBootcamp in Barcelona and was one of the first students to be part ...",
                       "link": "https://blog.ironhack.com/author/alberto/page/4/",
                       "title": "Alberto Marcos | Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Elina Nenonen completed the most recent cohort of the Web Development \nBootcamp in Barcelona and was one of the first students to be part of the new ...",
                       "link": "https://blog.ironhack.com/tag/ironhack-en/page/2/",
                       "title": "ironhack Archives - Page 2 of 2 - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "E junta-te a uma comunidade vibrante de pessoas que adoram o que fazem. \nQuero frequentar este campus. Miami. Amesterdão, Barcelona, Berlim, Bogotá ...",
                       "link": "https://www.ironhack.com/pt/cursos/ux-ui-design-bootcamp-learn-ux-design/inscrever/curso/5b8fee1b3619ac001afced44",
                       "title": "Inscreve-te nos Bootcamps de Programação e UX/UI Design da ...",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Jan 18, 2019 ... Alumni · Amsterdam · Barcelona · Berlin · Berlin · Bootcamp · Campus life · Data \nAnalytics · HackShow · Ironhack General · Lisbon · Madrid ...",
                       "link": "https://blog.ironhack.com/author/thomas/",
                       "title": "Thomas Jacquesson, Author at Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Dec 21, 2018 ... Alumni · Amsterdam · Barcelona · Berlin · Berlin · Bootcamp · Campus life · Data \nAnalytics · HackShow · Ironhack General · Lisbon · Madrid ...",
                       "link": "https://blog.ironhack.com/category/data-analytics/",
                       "title": "Data Analytics Archives - Ironhack Blog",
                       "city": "barcelona"
                   },
                   {
                       "snippet": "Jul 19, 2016 ... Alumni · Amsterdam · Barcelona · Berlin · Berlin · Bootcamp · Campus life · Data \nAnalytics · HackShow · Ironhack General · Lisbon · Madrid ...",
                       "link": "https://blog.ironhack.com/2016/07/19/emergence-ux-design/",
                       "title": "The Emergence of UX Design - Ironhack Blog",
                       "city": "barcelona"
                   }
               ][starting_from:starting_from + 10]
    return jsonify(results=data)
