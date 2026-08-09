r"""
Refines all 6 Category files for Book 5 Chapter 04 ("The Invention of Television") for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH04_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_04")
os.makedirs(CH04_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("What entertainment media did people rely on before television was invented?", "(A) Listening to news, music, and shows on the radio", "(B) Reading news on smartphones", "(C) Watching streaming shows on laptops", "(D) Watching color movies on private home projectors", "(A)", "People could only listen to news, music, and shows on the radio.", "Easy", "Remembering", "Pre-TV Era"),
    ("Who created the first working mechanical television system in 1925?", "(A) John Logie Baird", "(B) Philo Farnsworth", "(C) Charles Babbage", "(D) Alexander Graham Bell", "(A)", "John Logie Baird created the first working mechanical TV system in 1925.", "Easy", "Remembering", "Inventors"),
    ("What nationality was television pioneer John Logie Baird?", "(A) Scottish", "(B) American", "(C) French", "(D) German", "(A)", "He was a Scottish inventor.", "Easy", "Remembering", "Inventor Details"),
    ("Which components did John Logie Baird use to transmit moving images?", "(A) Spinning discs, light, and electricity", "(B) Microchips, lasers, and fiber optics", "(C) Vacuum tubes, copper wire, and gas", "(D) Solar batteries, mirrors, and lenses", "(A)", "Baird used spinning discs, light, and electricity.", "Easy", "Remembering", "Technology"),
    ("Who transmitted the first electronic television image in 1927?", "(A) Philo Farnsworth", "(B) John Logie Baird", "(C) Alan Turing", "(D) Thomas Edison", "(A)", "Philo Farnsworth transmitted the first electronic image in 1927.", "Easy", "Remembering", "Inventors"),
    ("What nationality was Philo Farnsworth?", "(A) American", "(B) Scottish", "(C) Italian", "(D) Canadian", "(A)", "Farnsworth was an American inventor.", "Easy", "Remembering", "Inventor Details"),
    ("How did Philo Farnsworth's electronic image compare to Baird's mechanical version?", "(A) It was much clearer", "(B) It was black and invisible", "(C) It was blurrier and slower", "(D) It had no sound output", "(A)", "Farnsworth's electronic image was much clearer.", "Easy", "Remembering", "Comparison"),
    ("By which decade did many families have televisions in their homes?", "(A) 1950s", "(B) 1910s", "(C) 1890s", "(D) 2010s", "(A)", "By the 1950s, many families had televisions in their homes.", "Easy", "Remembering", "Historical Timeline"),
    ("What entertainment content became accessible at home because of television?", "(A) News, movies, sports, and cartoons", "(B) Only weather reports", "(C) Radio dramas without video", "(D) Printed newspaper text", "(A)", "Families watched news, movies, sports, and cartoons at home.", "Easy", "Remembering", "Content Types"),
    ("What modern features define televisions today?", "(A) Flat screens, smart TVs, and internet connectivity", "(B) Spinning metal discs and steam power", "(C) Black-and-white screens without audio", "(D) Water tanks and copper levers", "(A)", "Modern TVs have flat screens, smart capabilities, and internet connectivity.", "Easy", "Remembering", "Modern TV"),
    ("What does the word 'spinning' mean in the vocabulary box?", "(A) Turning round quickly", "(B) Flying in a straight line", "(C) Standing completely still", "(D) Floating in water", "(A)", "Spinning means turning round quickly.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'transmit' mean?", "(A) To send out electronic signals or images", "(B) To break something into pieces", "(C) To paint a portrait on canvas", "(D) To listen quietly", "(A)", "Transmit means to send out electronic signals or images.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'version' mean?", "(A) A different presentation or model of the same content", "(B) An exact duplicate of a radio", "(C) A mathematical equation", "(D) A heavy iron box", "(A)", "Version means a different presentation of the same content.", "Easy", "Understanding", "Vocabulary"),
    ("Why was Baird's television system called 'mechanical'?", "(A) It relied on moving physical parts like spinning discs", "(B) It was built entirely by industrial robots", "(C) It ran on a car engine", "(D) It was sold exclusively to mechanics", "(A)", "Mechanical because it relied on moving physical parts like spinning discs.", "Easy", "Understanding", "Technology Concept"),
    ("What main advantage did electronic television have over mechanical television?", "(A) It eliminated physical moving discs, resulting in sharper and clearer images", "(B) It operated without any electrical power", "(C) It was made of folded paper", "(D) It only played radio audio", "(A)", "Electronic TV had no moving discs, producing sharper, clearer images.", "Easy", "Understanding", "Advancement"),
    ("Where did people go to watch movies before television brought them into homes?", "(A) Theatres", "(B) Libraries", "(C) Factories", "(D) Parks", "(A)", "People had to go to the theatre before home TV.", "Easy", "Remembering", "Social History"),
    ("In which year did John Logie Baird create his working mechanical TV system?", "(A) 1925", "(B) 1900", "(C) 1945", "(D) 1980", "(A)", "Created the first working mechanical system in 1925.", "Easy", "Remembering", "Dates"),
    ("In which year did Philo Farnsworth transmit the first electronic image?", "(A) 1927", "(B) 1915", "(C) 1939", "(D) 1960", "(A)", "Transmitted the first electronic image in 1927.", "Easy", "Remembering", "Dates"),
    ("What limitation did radios have that inspired inventors to create television?", "(A) Radio listeners could hear sound but could not see what was happening", "(B) Radios were too heavy to carry", "(C) Radios could only play for five minutes", "(D) Radios required water to run", "(A)", "Listeners could hear audio but could not see pictures.", "Easy", "Understanding", "Invention Cause"),
    ("How did Baird's invention make people feel when they first saw moving pictures from far away?", "(A) They felt it was almost like magic", "(B) They felt terrified and ran away", "(C) They felt bored and uninterested", "(D) They thought it was a trick mirror", "(A)", "Showing pictures from far away felt almost like magic.", "Easy", "Remembering", "Public Reaction"),
    ("What type of content can smart TVs stream today thanks to internet connectivity?", "(A) Countless online programs, movies, and live broadcasts from home", "(B) Printed books on paper", "(C) Radio signals from 1920", "(D) Morse code signals", "(A)", "Smart TVs stream countless programs from home via internet.", "Easy", "Remembering", "Modern Capability"),
    ("Who are the two main inventors highlighted in Chapter 04?", "(A) John Logie Baird and Philo Farnsworth", "(B) Thomas Edison and Alexander Graham Bell", "(C) Charles Babbage and Ada Lovelace", "(D) Isaac Newton and Albert Einstein", "(A)", "Chapter 04 highlights Baird and Farnsworth.", "Easy", "Remembering", "Historical Figures"),
    ("What role does light play in transmitting television images?", "(A) Light patterns are converted into electrical signals and reconstructed into visible images", "(B) Light warms up the TV cabinet", "(C) Light turns radio waves into sound", "(D) Light makes the TV heavy", "(A)", "Light patterns convert to electrical signals to display moving images.", "Easy", "Understanding", "Science Concept"),
    ("What title is given to Chapter 04?", "(A) The Invention of Television", "(B) The Invention of the Computer", "(C) Fountain Pen", "(D) Invention of Steam Engine", "(A)", "Title is 'The Invention of Television'.", "Easy", "Remembering", "Chapter Title"),
    ("What summary statement concludes Chapter 04 about television's overall impact?", "(A) Television truly changed the way the world stays informed and entertained", "(B) Television was replaced completely by newspapers", "(C) Television is no longer used by anyone", "(D) Television only works in Scotland", "(A)", "Changed the way the world stays informed and entertained.", "Easy", "Remembering", "Conclusion"),

    # Medium (26-40)
    ("Why was Philo Farnsworth's electronic system a major breakthrough compared to Baird's mechanical system?", "(A) Electronic beams move at the speed of light without mechanical wear, creating vastly clearer image resolution", "(B) Farnsworth's system used wooden wheels instead of metal", "(C) Farnsworth's system worked without electricity", "(D) Mechanical systems were banned by law", "(A)", "Electronic scanning provided far greater clarity and reliability without mechanical parts.", "Medium", "Analyzing", "Technical Superiority"),
    ("How did home televisions change family entertainment habits in the 1950s?", "(A) Families gathered together in living rooms to watch visual entertainment, reducing reliance on public theatres", "(B) Families stopped talking to each other completely", "(C) People stopped watching sports events", "(D) Families moved into movie theatres", "(A)", "Home viewing shifted entertainment from public venues to private family living rooms.", "Medium", "Analyzing", "Social Change"),
    ("Compare the transmission principles of radio and television.", "(A) Radio transmits audio signals through electromagnetic waves; television transmits both audio and synchronized visual signals", "(B) Radio uses light, while television uses sound only", "(C) Radio requires wires, while television is completely wire-free", "(D) Both transmit printed paper texts", "(A)", "Radio = audio signals; Television = synchronized audio and visual signals.", "Medium", "Comparing", "Technology Comparison"),
    ("Why is John Logie Baird's 1925 experiment considered a historical milestone despite being mechanical?", "(A) It proved for the first time that live moving images could be captured and transmitted electronically across distance", "(B) It was the first color cinema film", "(C) It created the internet", "(D) It replaced electric lights in Scotland", "(A)", "Proved the fundamental feasibility of remote moving image transmission.", "Medium", "Evaluating", "Historical Significance"),
    ("How does modern smart TV technology build upon the vision of early pioneers like Baird and Farnsworth?", "(A) Early pioneers established image transmission; modern smart TVs integrate digital processing, high definition, and global internet streaming", "(B) Smart TVs still use spinning discs inside", "(C) Modern TVs have eliminated screens", "(D) Early vision was to eliminate pictures", "(A)", "Modern smart TVs combine early transmission concepts with digital internet connectivity.", "Medium", "Synthesizing", "Technological Continuity"),
    ("What does the word 'mechanical' imply about early 1920s television technology?", "(A) It relied on physical moving machinery like motor-driven spinning discs to scan images", "(B) It was powered by steam engines", "(C) It was designed by automotive mechanics", "(D) It was dangerous to touch", "(A)", "Relied on physical moving parts like motor-driven spinning discs.", "Medium", "Understanding", "Concept Analysis"),
    ("How did mass adoption of television in the 1950s impact global journalism?", "(A) News became visual and immediate, allowing citizens to see live video footage of global events in real time", "(B) Newspapers stopped printing news", "(C) Journalists could no longer report news", "(D) News was restricted to radio only", "(A)", "Visual news coverage increased immediacy and emotional impact.", "Medium", "Analyzing", "Impact on Media"),
    ("What challenge did early inventors face when trying to show pictures along with sound?", "(A) Synchronizing high-speed visual frame transmission with clear audio signals without blurring", "(B) Radios were too loud", "(C) Light could not travel through copper wires", "(D) Television screens burned paper", "(A)", "Synchronizing rapid image frames with audio signals accurately.", "Medium", "Understanding", "Technical Challenge"),
    ("Why did Philo Farnsworth's electronic image transmission usher in the modern era of broadcasting?", "(A) Electronic cathode-ray/circuit scanning allowed scalable, high-resolution broadcasting suitable for mass production", "(B) Farnsworth made TV free for everyone", "(C) Electronic TV worked without antennas", "(D) It eliminated the need for camera lenses", "(A)", "Electronic scanning allowed scalable, high-resolution mass broadcasting.", "Medium", "Evaluating", "Broadcasting Evolution"),
    ("How does television serve a dual purpose as described in the chapter title summary?", "(A) It keeps the global public both informed (news/educational) and entertained (movies/sports/cartoons)", "(B) It cooks food and cleans house", "(C) It generates electricity and lights rooms", "(D) It prints books and newspapers", "(A)", "Keeps society informed (news) and entertained (shows).", "Medium", "Understanding", "Dual Purpose"),
    ("What role did spinning discs play in Baird's mechanical television?", "(A) They had perforated holes that swept across an image, breaking it into lines of light for transmission", "(B) They played music records", "(C) They cooled down the electric light bulb", "(D) They stored recorded video on tape", "(A)", "Perforated spinning discs swept across images to scan light lines.", "Medium", "Understanding", "Mechanism Detail"),
    ("What distinguishes a 'smart TV' from a traditional 1950s television set?", "(A) Smart TVs have built-in microprocessors and internet connectivity to stream on-demand digital content", "(B) Traditional 1950s TVs had color screens while smart TVs are black-and-white", "(C) Smart TVs use spinning metal discs", "(D) Traditional TVs connected to Wi-Fi", "(A)", "Smart TVs feature microprocessors and internet streaming capabilities.", "Medium", "Comparing", "Technological Comparison"),
    ("Why did people consider watching far-away pictures on early TVs 'almost like magic'?", "(A) Instantaneous visual transmission across miles defied previous human experience before the 1920s", "(B) Magicians performed on TV every day", "(C) The TV set disappeared when turned off", "(D) Images appeared without any electricity", "(A)", "Instant visual transmission across distance defied prior human experience.", "Medium", "Evaluating", "Cultural Perception"),
    ("How did television contribute to democratic awareness in society?", "(A) By broadcasting political debates, news events, and documentaries visually to millions of citizens simultaneously", "(B) By forcing people to vote on TV", "(C) By replacing government leaders", "(D) By stopping all public speeches", "(A)", "Simultaneous visual broadcasting of news and debates informed citizens.", "Medium", "Analyzing", "Civic Impact"),
    ("What lesson about technological progress can Class 5 students draw from Chapter 04?", "(A) Great inventions result from continuous improvements by multiple inventors building on each other's ideas", "(B) Inventions happen overnight by one person alone", "(C) Old inventions should be thrown away instantly", "(D) Technology never changes once invented", "(A)", "Progress results from continuous improvements across generations of inventors.", "Medium", "Evaluating", "Educational Insight"),

    # Hard (41-50)
    ("Critique the transition from mechanical to electronic television scanning from a physics perspective.", "(A) Mechanical disc speed was physically limited by inertia and friction, whereas electron beam scanning achieved thousands of lines per second effortlessly", "(B) Mechanical discs used too much water", "(C) Electronic scanning was slower than mechanical wheels", "(D) Electron beams destroyed camera lenses", "(A)", "Mechanical discs were limited by inertia/friction; electron beams achieved high-speed resolution effortlessly.", "Hard", "Evaluating", "HOTS Technical Analysis"),
    ("Deconstruct the socio-economic shift caused by affordable home televisions in the post-WWII era.", "(A) Mass manufacturing lowered TV costs, democratizing entertainment and creating a shared national cultural identity", "(B) TVs made movies extremely expensive", "(C) Only kings could afford TVs in the 1950s", "(D) Televisions destroyed the global economy", "(A)", "Affordable mass manufacturing democratized visual culture and created shared identity.", "Hard", "Analyzing", "Socio-Economic Analysis"),
    ("Evaluate the impact of internet integration on traditional linear television broadcasting.", "(A) Internet integration shifted viewing from scheduled linear broadcasts to on-demand, personalized streaming anytime", "(B) Internet integration made TV screens turn off completely", "(C) Traditional broadcasting eliminated internet use", "(D) It forced TVs to return to mechanical spinning discs", "(A)", "Shifted viewing from fixed linear schedules to personalized on-demand streaming.", "Hard", "Evaluating", "Media Evolution Analysis"),
    ("Compare John Logie Baird's approach with Philo Farnsworth's approach to image transmission.", "(A) Baird adapted existing mechanical optics (Nipkow discs), while Farnsworth conceptualized pure electronic beam scanning (Image Dissector)", "(B) Baird used software while Farnsworth used wood", "(C) Baird worked in space while Farnsworth worked underwater", "(D) Both inventors built identical machines", "(A)", "Baird adapted mechanical optics; Farnsworth invented pure electronic beam scanning.", "Hard", "Comparing", "Comparative Innovation Analysis"),
    ("Formulate a vision of future display technology beyond current smart TVs for Class 5 students.", "(A) 'Future displays may feature 3D holographic projections, ultra-flexible transparent screens, and direct neural visual interfaces.'", "(B) 'Future TVs will return to spinning wooden discs.'", "(C) 'TVs will be replaced by paper flyers.'", "(D) 'Screens will disappear and only audio will remain.'", "(A)", "Innovative vision featuring holograms, flexible displays, and neural interfaces.", "Hard", "Creating", "Future Technology Vision"),
    ("Assess the pedagogical value of teaching invention histories like television to primary students.", "(A) Fosters scientific curiosity, demonstrates perseverance through trial-and-error, and illustrates iterative engineering growth", "(B) Teaches children how to repair electrical wires without tools", "(C) Forces children to watch TV five hours a day", "(D) Discourages students from studying science", "(A)", "Fosters curiosity, demonstrates perseverance, and shows iterative engineering.", "Hard", "Evaluating", "Pedagogical Value"),
    ("Analyze how television transformed global sports into a multi-billion dollar cultural phenomenon.", "(A) Live multi-angle video broadcasting allowed millions of remote fans to experience matches, attracting global sponsorships", "(B) TV forced sports players to stay home", "(C) Sports were invented only after TV", "(D) TV made sports grounds obsolete", "(A)", "Live video broadcasting brought remote audiences to sports, driving global sponsorship.", "Hard", "Analyzing", "Cultural Analysis"),
    ("Synthesize how Chapter 04 connects language learning with STEM (Science, Technology, Engineering, Math) awareness.", "(A) Combines technical vocabulary (transmit, mechanical, electronic) with historical narrative and scientific evolution", "(B) Replaces English reading with complex algebra", "(C) Eliminates vocabulary in favor of drawing lines", "(D) Focuses exclusively on grammar rules", "(A)", "Integrates technical vocabulary with historical narrative and engineering concepts.", "Hard", "Synthesizing", "STEM Integration"),
    ("Critique the statement: 'Philo Farnsworth alone invented television.'", "(A) Inaccurate; while Farnsworth perfected electronic transmission, he built upon decades of work by pioneers like Baird, Nipkow, and Rosing", "(B) Completely accurate; no one else worked on TV", "(C) False; television was invented by ancient Romans", "(D) True; Baird copied Farnsworth's work", "(A)", "Inaccurate; television was an iterative breakthrough built on multiple pioneers.", "Hard", "Evaluating", "Historical Accuracy Critique"),
    ("Formulate a comprehensive essay prompt based on Chapter 04 for a Class 5 English assessment.", "(A) 'Trace the technological journey of television from radio to smart TVs. Explain how inventors improved picture clarity and how TV impacts our daily lives.'", "(B) 'Write five sentences about your favorite cartoon character.'", "(C) 'List ten brands of television sets.'", "(D) 'Draw a picture of a radio.'", "(A)", "Structured essay prompt evaluating historical recall, technical understanding, and thematic analysis.", "Hard", "Creating", "Assessment Task Design")
]

mcq_content = f"# MCQs — Chapter 04: The Invention of Television\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH04_MCQ_{idx:03d}"
    q_txt, opt_a, opt_b, opt_c, opt_d, ans, exp, diff, bloom, *rest = item
    mcq_content += f"### Question {idx}\n"
    mcq_content += f"- **Question ID**: {q_id}\n"
    mcq_content += f"- **Type**: MCQ\n"
    mcq_content += f"- **Difficulty**: {diff}\n"
    mcq_content += f"- **Bloom Level**: {bloom}\n"
    mcq_content += f"- **Topic**: Technology & History\n"
    mcq_content += f"- **Marks**: 1\n\n"
    mcq_content += f"**Question**: {q_txt}\n\n"
    mcq_content += f"- {opt_a}\n- {opt_b}\n- {opt_c}\n- {opt_d}\n\n"
    mcq_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH04_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("Before television was invented, people could only listen to news, music, and shows on the _______.", "radio", "Listened to news, music, and shows on the radio.", "Easy"),
    ("John Logie Baird was a _______ inventor who created the first working television system.", "Scottish", "Baird was a Scottish inventor.", "Easy"),
    ("Baird created the first working mechanical television system in the year _______.", "1925", "Created the system in 1925.", "Easy"),
    ("Baird used spinning discs, light, and _______ to transmit moving images.", "electricity", "Used spinning discs, light, and electricity.", "Easy"),
    ("Philo Farnsworth was an _______ inventor who developed electronic television.", "American", "Farnsworth was an American inventor.", "Easy"),
    ("Philo Farnsworth successfully transmitted the first electronic image in the year _______.", "1927", "Transmitted electronic image in 1927.", "Easy"),
    ("Farnsworth's electronic image was much _______ than Baird's mechanical version.", "clearer", "Electronic image was much clearer.", "Easy"),
    ("By the _______, many families had televisions in their homes.", "1950s", "Common in homes by 1950s.", "Easy"),
    ("Televisions allowed families to watch news, movies, sports, and _______ at home.", "cartoons", "Watched news, movies, sports, and cartoons.", "Easy"),
    ("Modern televisions feature flat screens, smart TVs, and _______ connectivity.", "internet", "Feature internet connectivity.", "Easy"),
    ("Spinning is defined in the vocabulary list as turning round _______.", "quickly", "Spinning means turning round quickly.", "Easy"),
    ("To transmit means to send out electronic _______ or images.", "signals", "Transmit means to send out electronic signals.", "Easy"),
    ("A version is defined as a different presentation of the same _______.", "contents", "Version means different presentation of contents.", "Easy"),
    ("Baird showed the world how they could watch pictures from far away, almost like _______.", "magic", "Watch pictures almost like magic.", "Easy"),
    ("People could watch movies on TV without having to go to the _______.", "theatre", "Watch movies without going to the theatre.", "Easy"),
    ("Baird's system relied on moving physical parts called _______ discs.", "spinning", "Relied on spinning discs.", "Easy"),
    ("Electronic television eliminated the need for mechanical _______ parts.", "moving", "Eliminated mechanical moving parts.", "Easy"),
    ("Philo Farnsworth's invention used _______ scanning instead of spinning discs.", "electronic", "Used electronic scanning.", "Easy"),
    ("Television transformed how the world stays informed and _______.", "entertained", "Stays informed and entertained.", "Easy"),
    ("John Logie Baird used light and electricity alongside spinning _______.", "discs", "Used spinning discs.", "Easy"),
    ("By 1950, television had become a major form of household _______.", "entertainment", "Major form of household entertainment.", "Easy"),
    ("Smart TVs allow users to access online streaming _______.", "programs", "Access online streaming programs.", "Easy"),
    ("Baird and Farnsworth are remembered as great _______ of television.", "inventors", "Remembered as great inventors.", "Easy"),
    ("Radio broadcasts provided audio but could not show moving _______.", "pictures", "Radio could not show moving pictures.", "Easy"),
    ("Chapter 04 is titled 'The Invention of _______'.", "Television", "Titled 'The Invention of Television'.", "Easy"),

    # Medium (26-40)
    ("The transition from mechanical to electronic television vastly improved image _______.", "clarity", "Improved image clarity.", "Medium"),
    ("Electronic television permitted high-resolution broadcasting without mechanical _______.", "wear", "Broadcasting without mechanical wear.", "Medium"),
    ("Home viewing on television altered traditional family _______ habits.", "leisure", "Altered family leisure habits.", "Medium"),
    ("Baird's 1925 demonstration proved that remote image _______ was achievable.", "transmission", "Proved image transmission was achievable.", "Medium"),
    ("Modern smart TVs integrate microprocessors to run operating _______.", "systems", "Run operating systems.", "Medium"),
    ("Mechanical televisions were limited by the physical speed of rotating _______.", "discs", "Limited by rotating discs.", "Medium"),
    ("Farnsworth's electronic system used cathode-ray tubes for image _______.", "reconstruction", "Used cathode-ray image reconstruction.", "Medium"),
    ("Mass production in the 1950s made television sets financially _______.", "affordable", "Made TV sets affordable.", "Medium"),
    ("Television unified cultural experiences by broadcasting simultaneous live _______.", "events", "Broadcasted simultaneous live events.", "Medium"),
    ("Streaming technology relies on high-speed internet to deliver video _______.", "data", "Delivers video data via internet.", "Medium"),
    ("Early TV pioneers solved the complex problem of synchronizing sound and _______.", "video", "Synchronized sound and video.", "Medium"),
    ("Television news broadcasts brought immediate visual awareness to global _______.", "citizens", "Brought visual awareness to citizens.", "Medium"),
    ("Flat-screen technology replaced bulky cathode-ray tube cabinet _______.", "televisions", "Replaced cathode-ray tube televisions.", "Medium"),
    ("Continuous innovation transformed primitive mechanical boxes into modern smart _______.", "displays", "Transformed primitives into smart displays.", "Medium"),
    ("Chapter 04 highlights how human ingenuity fulfills dreams of visual _______.", "communication", "Fulfills dreams of visual communication.", "Medium"),

    # Hard (41-50)
    ("Scanning speed in electronic systems overcomes mechanical inertia _______.", "barriers", "Overcomes mechanical inertia barriers.", "Hard"),
    ("Broadcast media democratization fostered a shared national cultural _______.", "identity", "Fostered a shared cultural identity.", "Hard"),
    ("On-demand digital streaming disrupted traditional scheduled linear _______.", "broadcasting", "Disrupted linear broadcasting.", "Hard"),
    ("Baird's Nipkow disc adaptation marked the genesis of electro-mechanical _______.", "telecasting", "Genesis of electro-mechanical telecasting.", "Hard"),
    ("Farnsworth's image dissector tube represented a leap in electronic _______.", "optics", "Leap in electronic optics.", "Hard"),
    ("Iterative engineering improvements drive the evolution of consumer _______.", "electronics", "Drive evolution of consumer electronics.", "Hard"),
    ("Live sports telecasts transformed athletic events into global commercial _______.", "spectacles", "Transformed sports into commercial spectacles.", "Hard"),
    ("Integrating audio and visual signals created an immersive media _______.", "medium", "Created an immersive media medium.", "Hard"),
    ("Historical analysis reveals television as a collaborative multi-inventor _______.", "achievement", "Collaborative multi-inventor achievement.", "Hard"),
    ("Chapter 04 demonstrates the profound power of STEM innovations in daily _______.", "life", "Demonstrates STEM innovations in daily life.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 04: The Invention of Television\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH04_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH04_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("Before television was invented, people could watch movies on their radios.", "False", "Radios could only transmit audio (sound), not moving pictures.", "Easy"),
    ("John Logie Baird created the first working mechanical television system in 1925.", "True", "Text confirms Baird created the first working system in 1925.", "Easy"),
    ("John Logie Baird was an American inventor born in New York.", "False", "Baird was a Scottish inventor.", "Easy"),
    ("Baird used spinning discs, light, and electricity to transmit images.", "True", "Text states Baird used spinning discs, light, and electricity.", "Easy"),
    ("Philo Farnsworth transmitted the first electronic television image in 1927.", "True", "Farnsworth transmitted the first electronic image in 1927.", "Easy"),
    ("Philo Farnsworth was a Scottish inventor.", "False", "Philo Farnsworth was an American inventor.", "Easy"),
    ("Baird's mechanical television image was clearer than Farnsworth's electronic image.", "False", "Farnsworth's electronic image was much clearer than Baird's mechanical version.", "Easy"),
    ("Televisions became common household items in many homes by the 1950s.", "True", "By the 1950s, many families had televisions in their homes.", "Easy"),
    ("Television allowed families to watch news, sports, and cartoons at home.", "True", "Families could watch news, movies, sports, and cartoons without going to theatres.", "Easy"),
    ("Modern televisions still use spinning metal discs to display images.", "False", "Modern TVs use flat screens, microchips, and digital technology.", "Easy"),
    ("Smart TVs today can connect to the internet to stream content.", "True", "Modern smart TVs connect to the internet for streaming.", "Easy"),
    ("'Spinning' means turning round quickly.", "True", "Vocabulary definition: Spinning = Turning round quickly.", "Easy"),
    ("'Transmit' means to destroy an electronic signal.", "False", "Transmit means to send out electronic signals or images.", "Easy"),
    ("'Version' means a different presentation of the same content.", "True", "Vocabulary definition: Version = A different presentation of same contents.", "Easy"),
    ("Radio was invented after television had already become popular.", "False", "Radio came first; television was invented later to add pictures to sound.", "Easy"),
    ("Philo Farnsworth's electronic television used moving mechanical wheels.", "False", "Electronic TV eliminated moving mechanical wheels.", "Easy"),
    ("Television changed the way the world stays informed and entertained.", "True", "Closing sentence confirms TV changed information and entertainment.", "Easy"),
    ("In the 1950s, people had to travel to theatres to watch cartoons.", "False", "By the 1950s, people could watch cartoons at home on television.", "Easy"),
    ("Baird showed the world how to watch pictures from far away.", "True", "Baird demonstrated watching pictures from far away.", "Easy"),
    ("Philo Farnsworth's electronic image transmission occurred in 1827.", "False", "Farnsworth's transmission occurred in 1927, not 1827.", "Easy"),
    ("Light and electricity were used alongside spinning discs in Baird's system.", "True", "Baird combined spinning discs, light, and electricity.", "Easy"),
    ("Televisions in the 1950s had internet connectivity built-in.", "False", "Internet connectivity was developed much later for modern smart TVs.", "Easy"),
    ("Chapter 04 is titled 'The Invention of Television'.", "True", "Chapter title is 'The Invention of Television'.", "Easy"),
    ("John Logie Baird and Philo Farnsworth worked together in the same room.", "False", "They worked independently; Baird in Scotland/UK, Farnsworth in the US.", "Easy"),
    ("Television combines moving images with audio sound.", "True", "Inventors dreamed of a device showing pictures along with sound.", "Easy"),

    # Medium (26-40)
    ("Mechanical televisions failed to gain popularity because they could not display motion.", "False", "Mechanical TVs did display motion, but electronic TVs offered superior resolution.", "Medium"),
    ("Farnsworth's electronic TV replaced physical spinning components with electronic beams.", "True", "Electronic TV scanned images using electron beams instead of physical discs.", "Medium"),
    ("The mass adoption of TV in the 1950s reduced reliance on public movie theatres.", "True", "Families could enjoy movies at home, reducing theatre visits.", "Medium"),
    ("Smart TVs rely on internal microprocessors and wireless networking.", "True", "Modern smart TVs contain processors and Wi-Fi modules.", "Medium"),
    ("Baird's 1925 demonstration was considered a failure by scientists.", "False", "It was celebrated as a breakthrough that proved image telecasting was possible.", "Medium"),
    ("Television broadcasts played a crucial role in creating shared national news experiences.", "True", "Millions watched the same news events simultaneously from their homes.", "Medium"),
    ("Electronic scanning is slower than mechanical disc spinning.", "False", "Electronic scanning moves at incredible speeds, far faster than mechanical discs.", "Medium"),
    ("Baird used cathode-ray tubes in his 1925 mechanical demonstration.", "False", "Baird used spinning Nipkow discs; cathode-ray tubes were used in electronic systems.", "Medium"),
    ("Television expanded entertainment options by bringing sports and cartoons to living rooms.", "True", "Home viewers gained access to diverse programming including sports and cartoons.", "Medium"),
    ("The word 'transmit' applies to sending radio waves carrying video data.", "True", "Transmission involves sending electromagnetic waves carrying audio/video data.", "Medium"),
    ("Philo Farnsworth was only 21 years old when he transmitted the first electronic image.", "True", "Farnsworth achieved his breakthrough as a brilliant young inventor in 1927.", "Medium"),
    ("Modern flat-screen displays use gas plasma, LCD, or OLED technology.", "True", "Modern flat screens rely on advanced LCD, LED, OLED, or plasma tech.", "Medium"),
    ("Radio and television use identical hardware to display visual information.", "False", "Radios lack display screens and image scanning components.", "Medium"),
    ("Continuous technological improvement is a central theme of Chapter 04.", "True", "The chapter traces progress from radio to mechanical TV, electronic TV, and smart TVs.", "Medium"),
    ("Baird's mechanical TV produced color images in 1925.", "False", "Early mechanical TVs produced dim, low-resolution black-and-white images.", "Medium"),

    # Hard (41-50)
    ("Mechanical disc speed limitations placed a hard physical ceiling on image resolution.", "True", "Spinning discs could not rotate fast enough to produce high-definition resolution.", "Hard"),
    ("Farnsworth's image dissector tube laid the foundation for modern camera sensors.", "True", "Electronic image scanning concepts evolved into modern CCD/CMOS camera sensors.", "Hard"),
    ("On-demand streaming services have completely eliminated traditional television hardware.", "False", "Streaming has changed content delivery, but television hardware (screens) remains essential.", "Hard"),
    ("Baird's system synchronized light intensity with mechanical disc aperture positioning.", "True", "Light passing through disc holes was converted into varying electric current.", "Hard"),
    ("The transition to electronic television represents a paradigm shift in telecommunications.", "True", "Moving from mechanical mechanics to solid-state electronics transformed telecommunications.", "Hard"),
    ("Television's advent had no effect on print newspaper circulation in the 20th century.", "False", "Immediate visual TV news significantly impacted print newspaper reading habits.", "Hard"),
    ("Farnsworth's electronic TV concept was inspired by plowed farm field lines.", "True", "Farnsworth famously conceived scanning lines while plowing farm fields in rows.", "Hard"),
    ("Chapter 04 illustrates that major technological breakthroughs are often developed in parallel by different inventors.", "True", "Baird in Scotland and Farnsworth in the US developed TV technologies during the same era.", "Hard"),
    ("Modern smart TVs operate without electrical power.", "False", "All televisions require electrical energy to operate.", "Hard"),
    ("Chapter 04 integrates historical timeline analysis with technological comprehension for Class 5.", "True", "Combines historical chronology with technological understanding.", "Hard")
]

tf_content = f"# True / False — Chapter 04: The Invention of Television\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH04_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH04_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("What entertainment media did people use before television was invented?", "Before television was invented, people could only listen to news, music, and shows on the radio without any visual pictures.", "Easy", "Remembering"),
    ("Who was John Logie Baird and what did he accomplish in 1925?", "John Logie Baird was a Scottish inventor who created the first working mechanical television system in 1925 using spinning discs, light, and electricity.", "Easy", "Remembering"),
    ("Who was Philo Farnsworth and what was his major breakthrough in 1927?", "Philo Farnsworth was an American inventor who transmitted the first electronic television image in 1927, which was much clearer than mechanical versions.", "Easy", "Remembering"),
    ("How did Philo Farnsworth's electronic television differ from Baird's mechanical system?", "Farnsworth's system used electronic beams instead of moving mechanical discs, producing a much clearer picture.", "Easy", "Understanding"),
    ("When did televisions become common features in residential homes?", "Televisions became common features in residential homes during the 1950s.", "Easy", "Remembering"),
    ("What types of programming could families enjoy on television in the 1950s?", "Families could watch news broadcasts, feature movies, sporting events, and cartoons right from their living rooms.", "Easy", "Remembering"),
    ("Name three modern features found on contemporary television sets today.", "Modern televisions feature flat screens, smart TV operating systems, and direct internet connectivity for streaming.", "Easy", "Remembering"),
    ("What does the word 'spinning' mean?", "'Spinning' means turning round or rotating very quickly.", "Easy", "Understanding"),
    ("What does the word 'transmit' mean?", "'Transmit' means to send out electronic signals, sounds, or images through space or wires.", "Easy", "Understanding"),
    ("What does the word 'version' mean?", "'Version' means a particular form or variation of something differing from other forms.", "Easy", "Understanding"),
    ("Why did early viewers consider watching television 'almost like magic'?", "Because seeing live moving pictures transmitted from miles away onto a screen had never been experienced before.", "Easy", "Understanding"),
    ("What limitation of the radio prompted inventors to design television?", "Radios could only broadcast audio sounds, leaving listeners unable to see what was taking place.", "Easy", "Understanding"),
    ("What components did John Logie Baird combine to create mechanical TV?", "He combined spinning metal discs, light beams, and electric currents to transmit images.", "Easy", "Remembering"),
    ("How did television affect public movie theatre attendance?", "It reduced the need to visit movie theatres since families could watch movies and shows conveniently at home.", "Easy", "Understanding"),
    ("In which country was John Logie Baird born?", "John Logie Baird was born in Scotland (Scottish inventor).", "Easy", "Remembering"),
    ("In which country was Philo Farnsworth born?", "Philo Farnsworth was born in the United States (American inventor).", "Easy", "Remembering"),
    ("What summary statement concludes Chapter 04 regarding television's impact?", "Television changed the way the world stays informed and entertained.", "Easy", "Remembering"),
    ("What does a 'smart TV' allow users to do today?", "It allows users to connect to the internet and stream digital shows, movies, and online videos on demand.", "Easy", "Understanding"),
    ("Why were spinning discs used in Baird's 1925 television?", "The spinning discs had holes arranged in a spiral to scan images line by line as they rotated rapidly.", "Easy", "Understanding"),
    ("How many years elapsed between Baird's 1925 mechanical system and Farnsworth's 1927 electronic image?", "Two years elapsed between Baird's mechanical achievement (1925) and Farnsworth's electronic transmission (1927).", "Easy", "Remembering"),
    ("Why is electronic television superior to mechanical television?", "Electronic TV has no moving physical parts to wear out and scans at much higher speeds for sharper picture resolution.", "Easy", "Understanding"),
    ("What role do flat screens play in modern televisions?", "Flat screens make televisions thin, lightweight, space-saving, and capable of displaying high-definition digital pictures.", "Easy", "Understanding"),
    ("How does television help keep the world informed?", "By broadcasting live news reports, weather updates, and educational documentaries directly to viewers.", "Easy", "Understanding"),
    ("What main lesson about innovation is taught in Chapter 04?", "Technological progress happens when different inventors continuously improve ideas over time to solve human needs.", "Easy", "Understanding"),
    ("What title is given to Chapter 04?", "The title of Chapter 04 is 'The Invention of Television'.", "Easy", "Remembering"),

    # Medium (26-40)
    ("Analyze how television transformed global news coverage compared to newspapers.", "Newspaper news was delayed by printing times and text-based. Television brought immediate, visual, live video coverage into living rooms, making news visual and instantaneous.", "Medium", "Analyzing"),
    ("Why was Farnsworth's electronic TV able to produce a clearer image than Baird's mechanical TV?", "Farnsworth used electron beams that scanned thousands of lines per second without physical friction, whereas Baird's mechanical discs were physically limited in speed and hole density.", "Medium", "Analyzing"),
    ("Discuss how home television changed family living room dynamics in the 1950s.", "The television set became the focal point of the living room. Families gathered around it in the evenings, shifting leisure time from outdoor venues or quiet reading to shared visual watching.", "Medium", "Analyzing"),
    ("Explain the difference between mechanical spinning discs and electronic cathode-ray scanning.", "Mechanical discs physical rotate to sweep light across a scene. Electronic cathode-ray scanning uses magnetic fields to steer invisible streams of electrons rapidly across a phosphorescent screen.", "Medium", "Comparing"),
    ("How did television democratize access to sports and performing arts?", "Before TV, only people who bought stadium or theatre tickets could watch matches or plays. TV allowed millions of people of all economic backgrounds to watch events for free from home.", "Medium", "Evaluating"),
    ("Why did it take until the 1950s for televisions to become widespread in homes after being invented in the 1920s?", "Refining manufacturing, establishing broadcast towers, lowering production costs, and overcoming delays from World War II delayed mass residential adoption until the 1950s.", "Medium", "Analyzing"),
    ("What role does internet connectivity play in transforming traditional TV into Smart TV?", "Internet connectivity liberates TV from fixed broadcast schedules, enabling viewers to stream on-demand content, pause live shows, and access global digital video libraries.", "Medium", "Analyzing"),
    ("How did early inventors overcome the challenge of synchronizing audio with visual images?", "They routed audio radio signals and video electronic signals through connected electrical channels so sound and picture reached the receiver simultaneously.", "Medium", "Understanding"),
    ("What makes Baird and Farnsworth complementary pioneers in television history?", "Baird proved the initial concept of telecasting moving images, while Farnsworth developed the electronic scanning technology essential for modern high-definition displays.", "Medium", "Evaluating"),
    ("Summarize Chapter 04 in four concise sentences.", "Before television, people listened to news and music on radios without visuals. In 1925, John Logie Baird invented the first mechanical TV, followed by Philo Farnsworth's clearer electronic version in 1927. By the 1950s, televisions entered millions of homes, offering news, movies, and sports. Today, smart TVs connect to the internet, keeping the world informed and entertained.", "Medium", "Understanding"),
    ("How did television impact the film industry when home adoption soared in the 1950s?", "Film studios initially feared losing audiences to home TVs, but eventually adapted by producing high-budget widescreen spectacles and licensing movies for television broadcasting.", "Medium", "Analyzing"),
    ("Describe how spinning discs scan an image line by line.", "A Nipkow disc has spiral holes. As it spins fast, each hole sweeps across one horizontal line of the subject, converting light variations into electric pulses line by line.", "Medium", "Understanding"),
    ("Why is visual information more impactful for human understanding than audio alone?", "Human brains process visual images rapidly. Combining visual body language, facial expressions, and live action with audio creates deeper comprehension and emotional connection.", "Medium", "Evaluating"),
    ("How has television technology contributed to distance learning and education?", "Educational TV channels and streaming documentaries bring science, geography, history, and language lessons directly to students in remote areas without access to physical libraries.", "Medium", "Applying"),
    ("What advice would you give to young inventors studying Chapter 04?", "I would advise them to observe current limitations, study past inventors' attempts, persevere through technical failures, and embrace new technologies to create better solutions.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the technological limitations of Baird's mechanical television.", "Baird's mechanical system suffered from low frame rates, flickering dim images, noisy motor operation, and small screen sizes due to the physical inertia of rotating discs.", "Hard", "Evaluating"),
    ("Deconstruct the transition of television from a broadcast medium to an interactive smart medium.", "Initial TV was a one-way, linear broadcast where networks controlled schedules. Smart TV transformed it into a two-way, interactive digital platform where users control what, when, and how they watch.", "Hard", "Analyzing"),
    ("Evaluate the cultural impact of televised international events like the Olympic Games.", "Televised global events unite worldwide audiences simultaneously, fostering global awareness, cultural exchange, and international solidarity across geographic boundaries.", "Hard", "Evaluating"),
    ("Compare the role of Scottish innovation (Baird) and American innovation (Farnsworth) in early telecommunications.", "Scottish innovation focused on clever mechanical engineering adaptations, while American innovation focused on pioneering electronic optics and vacuum tube physics.", "Hard", "Comparing"),
    ("Formulate a story about a child in 1955 seeing a color television for the first time.", "'Ten-year-old Leo gasped as the grey screen burst into vivid red and blue. Watching a colorful clown parade in his own living room felt like stepping straight into a magical wonderland.'", "Hard", "Creating"),
    ("Assess the psychological effects of screen time management for Class 5 students.", "While TV provides educational news and quality entertainment, excessive unmonitored screen time can reduce physical activity, sleep quality, and face-to-face social interaction.", "Hard", "Evaluating"),
    ("Analyze how mass media advertising on television shaped modern consumer economies.", "Commercial TV broadcasts brought visual product demonstrations directly into living rooms, building nationwide brand awareness and driving mass consumer demand.", "Hard", "Analyzing"),
    ("Synthesize how Chapter 04 integrates physics, history, and media literacy.", "It connects historical timelines (1920s-1950s) with physics concepts (light, electricity, electronic scanning) and media literacy (how news and shows reach audiences).", "Hard", "Synthesizing"),
    ("Critique the claim: 'Television has rendered books obsolete.'", "False; while TV provides quick visual entertainment, books develop deep reading comprehension, critical thinking, active imagination, and detailed analytical skills that visual media cannot replace.", "Hard", "Evaluating"),
    ("Formulate a 4-line poem capturing the evolution of television.", "'From radio sounds to spinning discs of light,\nBaird brought moving pictures to our sight;\nThen Farnsworth made electronic screens so clear,\nNow smart TVs bring the world right here!'", "Hard", "Creating")
]

sa_content = f"# Short Answer Questions — Chapter 04: The Invention of Television\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH04_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH04_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe the early days of entertainment before television and explain how John Logie Baird created the first working TV system.",
     "Long ago, before television existed, people relied solely on radios for audio broadcasts such as news, music, and radio dramas. Although radio was popular, listeners could not see pictures of what was happening. Inventors dreamed of creating a device that could transmit moving pictures alongside sound. In 1925, Scottish inventor John Logie Baird achieved a historical milestone by creating the first working mechanical television system. Baird utilized rapidly spinning metal discs perforated with holes, light beams, and electrical currents to scan and transmit moving images across a distance. He demonstrated to the world that watching live pictures from far away was possible, which felt almost like magic to early audiences.",
     "Easy", "Remembering"),

    ("Explain Philo Farnsworth's breakthrough in 1927 and how electronic television improved upon mechanical television.",
     "In 1927, American inventor Philo Farnsworth achieved a revolutionary breakthrough by transmitting the first electronic television image. Unlike John Logie Baird's mechanical system, which relied on physical spinning discs, Farnsworth's system used streams of electron beams inside glass tubes to scan and display images. Electronic television eliminated mechanical noise, friction, and motor speed limitations. As a result, Farnsworth's electronic image was vastly clearer, sharper, and more detailed than Baird's mechanical version. This electronic scanning technology established the foundation for modern television broadcasting.",
     "Easy", "Remembering"),

    ("Trace the rise of home television in the 1950s and describe how it transformed family entertainment.",
     "Following improvements in manufacturing and broadcasting technology, televisions became widely affordable and advanced by the 1950s. Millions of families purchased television sets for their living rooms. This transformed family entertainment by bringing news, feature films, live sporting events, and animated cartoons directly into the home. Families no longer needed to travel to public theatres or stadiums to watch visual events. The television set became the central gathering point for household leisure, keeping families entertained and informed together.",
     "Easy", "Understanding"),

    ("Describe the features of modern smart televisions today and compare them with early 1950s television sets.",
     "Today's modern televisions are drastically different from early 1950s sets. While 1950s televisions were bulky wooden cabinets with small, black-and-white, low-resolution screens receiving basic antenna channels, modern televisions feature sleek, ultra-thin flat screens displaying high-definition color video. Furthermore, modern smart TVs contain built-in microprocessors and internet connectivity, allowing viewers to stream on-demand digital shows, connect to global video platforms, and run interactive apps from the comfort of their homes.",
     "Easy", "Understanding"),

    ("Explain the vocabulary words from Chapter 04: Spinning, Transmit, and Version with definitions and example sentences.",
     "1. **Spinning**: Turning round or rotating very quickly. *Sentence*: Baird used spinning discs to scan light images.\n2. **Transmit**: To send out electronic signals, sounds, or images over distance. *Sentence*: Satellite towers transmit television signals into our homes.\n3. **Version**: A particular form or variation of something differing from another. *Sentence*: Farnsworth created an electronic version of television that was much clearer than Baird's mechanical version.",
     "Easy", "Understanding"),

    ("Discuss how television keeps the world informed and entertained as highlighted in Chapter 04.",
     "Television serves a vital dual role in modern human society. First, it keeps the world informed by broadcasting live news reports, educational documentaries, weather updates, and political debates visually, enabling citizens to witness global events instantly. Second, it keeps the world entertained by delivering diverse cultural programming, including feature movies, music concerts, drama series, live sports, and children's cartoons. Together, these functions make television one of the most influential mass communication inventions in human history.",
     "Easy", "Analyzing"),

    ("Explain how John Logie Baird used spinning discs, light, and electricity to display pictures.",
     "John Logie Baird's mechanical television operated by passing bright light through a rapidly spinning Nipkow disc. The disc contained small holes arranged in a spiral pattern. As the disc spun, each hole swept across a narrow line of the subject, converting variations in reflected light into fluctuating electrical currents. At the receiving end, a matching synchronized spinning disc recreated the lines of light on a screen, assembling a crude moving picture.",
     "Easy", "Understanding"),

    ("Why did Philo Farnsworth's invention win the technological race over mechanical television systems?",
     "Farnsworth's electronic system won because physical spinning discs had severe physical limitations: they could not spin fast enough or contain enough small holes to produce high-resolution pictures without breaking or making loud noise. Farnsworth's electronic system used invisible electron beams controlled by magnetic fields, which moved at near-light speeds, producing bright, sharp, high-definition images effortless without mechanical parts.",
     "Easy", "Evaluating"),

    ("Summarize Chapter 04 in five detailed points.",
     "1. Before TV, people relied on audio radios without visual images.\n2. In 1925, Scottish inventor John Logie Baird built the first mechanical TV using spinning discs.\n3. In 1927, American inventor Philo Farnsworth transmitted the first electronic TV image, offering superior clarity.\n4. By the 1950s, televisions entered millions of homes, bringing news, sports, and movies to living rooms.\n5. Today, internet-connected smart TVs offer flat screens and global streaming, keeping the world informed and entertained.",
     "Easy", "Understanding"),

    ("What obstacles did early television inventors face when developing the technology?",
     "Early inventors faced immense technical obstacles, including amplifying weak electric signals, synchronizing fast-moving mechanical components with audio sound, capturing sufficient light from subjects, obtaining financial funding, and proving to a skeptical public that transmitting live pictures across distance was physically possible.",
     "Easy", "Understanding"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Compare the role of radio versus television in mass media broadcasting.", "Radio relies exclusively on audio, requiring listeners to use imagination to picture events. Television combines synchronized high-definition video with audio, providing immediate visual proof, emotional resonance, and richer engagement for global news and entertainment.", "Easy", "Comparing"),
    ("Explain why the 1950s is considered the 'Golden Age' of home television adoption.", "During the 1950s, post-war manufacturing reduced television prices, broadcast networks built extensive transmission towers, and popular programming (sitcoms, sports, news) exploded, turning TV into an essential household fixture across millions of homes.", "Easy", "Understanding"),
    ("How do flat screens improve the television viewing experience compared to old cathode-ray tube sets?", "Flat screens (LED/OLED) utilize microscopic light-emitting diodes to display crisp, high-definition color pictures with wide viewing angles, thin profiles, low energy consumption, and large screen sizes, replacing heavy, bulky glass vacuum tube cabinets.", "Easy", "Understanding"),
    ("Describe the impact of live sports broadcasting on global sports fandom.", "Live sports broadcasting allows millions of fans to watch matches simultaneously from home. Multi-camera angles, slow-motion replays, and expert commentary create an exciting stadium atmosphere in living rooms, transforming regional sports into global cultural events.", "Easy", "Analyzing"),
    ("How did television change the way political news and elections are communicated?", "Television allowed voters to see political leaders directly, observe body language during televised debates, and watch live breaking news unfold, making political coverage more visual, immediate, and impactful.", "Easy", "Analyzing"),
    ("Explain how modern smart TVs integrate with home Wi-Fi networks.", "Smart TVs contain internal Wi-Fi antennas and network chips that connect wirelessly to home internet routers, allowing built-in software apps to stream digital video data from remote servers directly to the screen.", "Easy", "Understanding"),
    ("What lessons about perseverance can students learn from John Logie Baird's career?", "Baird faced poor health, lack of money, and skepticism, yet he persevered by experimenting with improvised materials (cardboard, bicycle lenses, darning needles) until he successfully demonstrated the world's first working TV in 1925.", "Easy", "Evaluating"),
    ("How did cartoons and children's programming on TV impact childhood culture?", "Dedicated children's television shows and morning cartoons provided shared cultural stories, educational lessons, and moral storytelling for young viewers, creating memorable childhood experiences across generations.", "Easy", "Understanding"),
    ("Discuss how television contributed to global cultural exchange.", "By broadcasting international movies, travel documentaries, and news reports, television allowed people to see life, traditions, and environments in foreign countries, broadening global understanding and empathy.", "Easy", "Evaluating"),
    ("How does Chapter 04 fulfill ICSE/CBSE English learning outcomes for Class 5?", "It blends technical STEM knowledge with chronological narrative, expands formal vocabulary (transmit, version, mechanical), and develops critical reading skills through factual recall, cause-effect analysis, and thematic reflection.", "Easy", "Understanding"),
    ("Re-write the story of television's invention from the perspective of a family getting their first TV in 1952.", "'On a cold evening in 1952, Dad carried a heavy wooden cabinet into our living room. When he turned the dial, a glowing black-and-white picture of a news anchor appeared. We sat together on the rug in awe, realizing the world was now right inside our home.'", "Easy", "Creating"),
    ("Explain why Philo Farnsworth's childhood farm experience inspired his TV invention.", "While plowing potato fields back and forth in straight parallel rows at age 14, Farnsworth realized that an electronic beam could scan an image line by line in the exact same pattern, inspiring his electronic TV concept.", "Easy", "Remembering"),
    ("How does television help disseminate emergency warnings during natural disasters?", "Television networks broadcast urgent visual maps, weather radar images, and emergency alert banners, giving citizens instant visual instructions to evacuate or seek shelter during storms, floods, or fires.", "Easy", "Applying"),
    ("Analyze the phrase 'watch pictures from far away, almost like magic'.", "This phrase captures the wonder felt by early 20th-century audiences. Before telecommunications, seeing events occurring miles away in real time seemed physically impossible, making TV feel like supernatural magic.", "Easy", "Analyzing"),
    ("What future advancements might replace flat-screen smart TVs in the coming decades?", "Future display technology may evolve into 3D holographic projections floating in air, lightweight augmented reality glasses, flexible rollable screens, or direct neural visual interfaces.", "Easy", "Creating"),

    # Medium (26-40)
    ("Critically analyze the socio-cultural impact of television on local communities.",
     "The widespread adoption of home television transformed community social structures:\n1. **Home-Centric Leisure**: Families spent more evenings indoors watching TV rather than attending community halls, public lectures, or local theatre performances.\n2. **Shared Cultural Touchstones**: Watching identical national broadcasts created unified cultural references, shared news awareness, and common language idioms across diverse regions.\n3. **Information Democratization**: Visual news brought world events, political debates, and scientific achievements directly to citizens regardless of literacy levels.",
     "Medium", "Analyzing"),

    ("Examine the technological progression from mechanical scanning to solid-state digital displays.",
     "The technical progression of television spans three distinct eras:\n1. **Mechanical Era (1920s)**: Rotating perforated discs scanned images using physical movement, producing low-resolution, dim, flickering pictures.\n2. **Electronic/Cathode-Ray Era (1930s-1990s)**: High-speed electron beams scanned phosphor-coated glass screens, achieving sharp black-and-white and later vibrant color broadcasts.\n3. **Digital/Solid-State Era (2000s-Present)**: Flat liquid crystal (LCD), light-emitting diode (LED), and OLED micro-displays process digital data packets, integrating internet streaming and 4K ultra-high definition.",
     "Medium", "Analyzing"),

    ("Evaluate the dual role of television as an educational tool and an entertainment medium.",
     "Television balances education and entertainment effectively. As an educational tool, it broadcasts wildlife documentaries, historical reenactments, science demonstrations, and news reports, making complex topics visually clear for students. As an entertainment medium, it provides relaxation through comedy shows, sports, and feature films. When balanced properly, television enriches human knowledge while providing wholesome leisure.",
     "Medium", "Evaluating"),

    ("Discuss how the competitive rivalry between mechanical and electronic TV pioneers accelerated innovation.",
     "Competition between Baird's mechanical approach and Farnsworth's electronic approach accelerated development. Baird's early success pushed electronic researchers to demonstrate superior image quality quickly, while Farnsworth's electronic breakthrough forced the industry to adopt electronic standards, rapidly advancing global telecommunications within a single decade.",
     "Medium", "Analyzing"),

    ("Design a primary school science project centered on the principles of light and image transmission from Chapter 04.",
     "Project Title: 'Building a Simple Flip-Book and Pinhole Viewer'\n1. **Objective**: Understand how fast-moving static images create the illusion of motion.\n2. **Activity 1**: Students draw 20 sequential drawings on paper corners to create a flip-book animation.\n3. **Activity 2**: Construct a simple pinhole box to project upside-down light images onto tracing paper.\n4. **Discussion**: Connect flip-book frame rates and pinhole light projection to Baird's spinning disc mechanism.",
     "Medium", "Creating"),

    ("How did television influence the global music and dance industry?", "TV introduced music videos, televised talent shows, and live concert broadcasts, allowing musical artists to reach global audiences visually and transforming music into a visual art form.", "Medium", "Analyzing"),
    ("Contrast the experience of reading a news article versus watching a live televised news broadcast.", "Reading news relies on text comprehension and mental visualization, allowing deep reflection. Live televised news provides immediate visual footage, ambient audio, and emotional body language, offering vivid, real-time immersion.", "Medium", "Comparing"),
    ("Explain why Philo Farnsworth's electronic system was less prone to mechanical failure.", "Because it contained no motor, belts, or spinning metal wheels to wear out, misalign, or break; electronic beams operated silently inside sealed vacuum tubes controlled by magnetic fields.", "Medium", "Understanding"),
    ("How did television help bridge the gap between urban and rural entertainment access?", "Rural communities that lacked theatres or stadiums gained equal access to high-quality films, national sports, and cultural performances through television signals broadcast across long distances.", "Medium", "Evaluating"),
    ("Analyze how television commercials shaped post-war consumer culture.", "By demonstrating new household appliances, vehicles, and food products with appealing visuals and catchy jingles, TV advertising stimulated consumer interest and expanded global retail markets.", "Medium", "Analyzing"),
    ("Why was the invention of color television in the 1960s another major milestone?", "Color television restored natural visual realism to broadcasts, making nature documentaries, sports, fashion, and cinema dramatically more engaging than black-and-white programming.", "Medium", "Understanding"),
    ("Evaluate the importance of patent protection for inventors like John Logie Baird and Philo Farnsworth.", "Patents protected their intellectual property from unauthorized copying by large corporations, ensuring independent inventors received credit and financial rewards for their original breakthroughs.", "Medium", "Evaluating"),
    ("How can Class 5 students practice critical media literacy when watching television?", "Students should ask: Who created this show? What is the main message? Is the information factual or opinion? How do visual techniques make the content feel exciting or persuasive?", "Medium", "Applying"),
    ("Deconstruct the structural organization of Chapter 04 from pre-TV to modern smart TVs.", "Chronological Structure: Introduction (Radio Era) → Section 1 (Baird's 1925 Mechanical System) → Section 2 (Farnsworth's 1927 Electronic System) → Section 3 (1950s Home Adoption) → Conclusion (Modern Smart TVs & Global Impact).", "Medium", "Analyzing"),
    ("Construct a fictional interview between a student journalist and inventor Philo Farnsworth in 1930.", "'Journalist: Mr. Farnsworth, how did a farm boy invent electronic TV?' 'Farnsworth: While plowing farm rows, I realized electron beams could scan images line by line just like farm furrows. Electrical science made it possible!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the transformation of television from a shared family hearth to individualized mobile screen consumption.",
     "In the 1950s-1990s, the television set served as a physical 'hearth' around which families gathered, fostering collective discussions and shared media experiences. The modern rise of personalized smart TVs, tablets, and smartphones has fragmented this shared experience, allowing family members to consume customized content individually. While this maximizes personal choice, it reduces shared family commentary and collective cultural bonding.",
     "Hard", "Evaluating"),

    ("Deconstruct the physics of electron beam scanning in cathode-ray tube (CRT) technology.",
     "CRT technology operates by accelerating a beam of electrons through an electric field toward a glass screen coated with phosphorescent materials. Magnetic deflection coils steer the electron beam rapidly line by line across the screen (raster scanning). When electrons strike the phosphor coating, light is emitted, forming glowing pixels that assemble into a complete visual frame thirty to sixty times per second.",
     "Hard", "Analyzing"),

    ("Synthesize how Chapter 04 demonstrates the interdisciplinary nature of modern technological breakthroughs.",
     "Chapter 04 demonstrates that television required combining optics (light manipulation), mechanical engineering (spinning discs), electrical engineering (signal amplification), physics (electron beam dynamics), and computer science (modern digital networking), proving that major innovations emerge from cross-disciplinary synthesis.",
     "Hard", "Synthesizing"),

    ("Formulate a comprehensive assessment rubric for evaluating Class 5 student research projects on inventions.",
     "- **Historical Chronology (25%)**: Accurately mapping key dates, inventors, and developmental stages.\n- **Technical Understanding (25%)**: Explaining underlying mechanisms (mechanical vs. electronic vs. digital).\n- **Impact Analysis (25%)**: Evaluating how the invention transformed society, communication, and culture.\n- **Presentation Clarity (25%)**: Utilizing precise scientific vocabulary and creative visual aids.",
     "Hard", "Creating"),

    ("Evaluate how visual media consumption affects cognitive attention spans in young learners.", "While visual TV content enhances immediate engagement and visual processing speed, fast-paced commercial editing can reduce sustained attention spans required for deep reading and complex problem-solving if not balanced with traditional print reading.", "Hard", "Evaluating"),

    ("Compare the evolutionary path of television with the evolutionary path of the telephone.", "Both telecommunications technologies originated with analog/mechanical systems in the late 19th/early 20th century (Baird's TV / Bell's telephone), transitioned to electronic network infrastructure, and ultimately converged into digital, internet-driven smart devices.", "Hard", "Comparing"),
    ("Discuss the ethical responsibilities of television broadcasters toward young audiences.", "Broadcasters have an ethical duty to ensure age-appropriate programming, restrict violent or deceptive content, provide accurate educational news, and promote positive social values for young viewers.", "Hard", "Evaluating"),
    ("Analyze how live satellite telecasting in the 1960s created the concept of a 'Global Village'.", "Satellite telecasting allowed live video signals to cross oceans instantly, enabling millions across continents to watch events (like the 1969 moon landing) simultaneously, creating a globally connected human consciousness.", "Hard", "Analyzing"),
    ("Draft an analytical commentary on the line: 'Thanks to the hard work of inventors like Baird and Farnsworth, we can enjoy countless programs from the comfort of our homes.'", "This sentence honors the enduring human legacy of innovation. It connects decades of painstaking historical research and technical sacrifice with the everyday comfort and convenience enjoyed by modern families globally.", "Hard", "Evaluating"),
    ("Synthesize the ultimate pedagogical lesson of Chapter 04 for Class 5 English curriculum.", "Chapter 04 teaches students that everyday conveniences like television are the fruits of human curiosity, scientific rigor, and persistent collaboration, inspiring young minds to appreciate history and pursue innovation.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 04: The Invention of Television\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH04_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH04_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("A long time ago, people could only listen to news, music and shows on the radio. They couldn't see what was happening. But some brilliant inventors dreamed of a device that could show pictures along with sound.",
     [
         ("What entertainment device did people rely on long ago?", "The radio.", "Easy", "Remembering"),
         ("What limitation did radios have according to this passage?", "People could only listen to sound and could not see pictures of what was happening.", "Easy", "Remembering"),
         ("What dream did brilliant inventors have?", "They dreamed of a device that could show moving pictures along with sound.", "Easy", "Remembering"),
         ("How did television solve the radio's limitation?", "By combining moving visual images with synchronized audio sound.", "Medium", "Understanding"),
         ("What impact did visual news have on global communication?", "It made news coverage visual, immediate, and far more engaging for global audiences.", "Medium", "Analyzing")
     ]),

    # Set 2
    ("One of the first steps toward the invention of television was taken by a Scottish inventor named John Logie Baird. In 1925, he created the first working television system. Baird used spinning discs light and electricity to transmit moving images.",
     [
         ("Who took one of the first steps toward inventing television?", "John Logie Baird.", "Easy", "Remembering"),
         ("What was Baird's nationality?", "Scottish.", "Easy", "Remembering"),
         ("In which year did Baird create the first working television system?", "1925.", "Easy", "Remembering"),
         ("What three elements did Baird use to transmit moving images?", "Spinning discs, light, and electricity.", "Easy", "Remembering"),
         ("What type of television system did Baird build?", "A mechanical television system.", "Medium", "Understanding")
     ]),

    # Set 3
    ("He showed the world how they could watch pictures from far away, almost like magic. At the same time, other inventors like Philo Farnsworth in the United States were working on electronic television.",
     [
         ("How did early audiences view Baird's demonstration of watching pictures from far away?", "They viewed it as 'almost like magic'.", "Easy", "Remembering"),
         ("Who was working on electronic television in the United States at the same time?", "Philo Farnsworth.", "Easy", "Remembering"),
         ("What type of television was Farnsworth developing?", "Electronic television.", "Easy", "Remembering"),
         ("Where was Philo Farnsworth located?", "In the United States.", "Easy", "Remembering"),
         ("Why was Farnsworth's work on electronic TV important?", "Because electronic scanning eliminated mechanical moving discs, leading to modern TV.", "Medium", "Analyzing")
     ]),

    # Set 4
    ("In 1927, Farnsworth successfully transmitted the first electronic image, which was much clearer than Baird's mechanical version.",
     [
         ("In which year did Farnsworth transmit the first electronic image?", "1927.", "Easy", "Remembering"),
         ("What kind of image did Farnsworth transmit?", "The first electronic image.", "Easy", "Remembering"),
         ("How did Farnsworth's image compare to Baird's image?", "It was much clearer than Baird's mechanical version.", "Easy", "Remembering"),
         ("What does the word 'version' mean in this text?", "A different presentation or model of the same content.", "Easy", "Understanding"),
         ("Why was electronic transmission clearer than mechanical transmission?", "Electronic beams scanned at higher speeds without friction or mechanical blurring.", "Medium", "Analyzing")
     ]),

    # Set 5
    ("Soon, televisions became more advanced and by the 1950s, many families had them in their homes. People could now watch news, movies, sports, and cartoons without going to the theatre.",
     [
         ("By which decade did many families have televisions in their homes?", "The 1950s.", "Easy", "Remembering"),
         ("Name four types of programs people could watch at home on television.", "News, movies, sports, and cartoons.", "Easy", "Remembering"),
         ("Where did people previously have to go to watch movies before TV?", "To the theatre.", "Easy", "Remembering"),
         ("How did home TV affect family leisure time in the 1950s?", "Families gathered at home in living rooms to watch entertainment together.", "Medium", "Understanding"),
         ("What socio-economic factor allowed families to buy TVs in the 1950s?", "Mass production lowered manufacturing costs, making TVs affordable.", "Medium", "Analyzing")
     ]),

    # Set 6
    ("Today, television has changed a lot. We have flat screens, smart TVs and even internet-connected devices. Thanks to the hard work of inventors like Baird and Farnsworth, we can enjoy countless programs from the comfort of our homes.",
     [
         ("Name three modern developments in television technology mentioned here.", "Flat screens, smart TVs, and internet-connected devices.", "Easy", "Remembering"),
         ("Which two inventors are specifically thanked in this passage?", "John Logie Baird and Philo Farnsworth.", "Easy", "Remembering"),
         ("Where can we now enjoy countless television programs?", "From the comfort of our homes.", "Easy", "Remembering"),
         ("What makes a TV 'smart' today?", "Its built-in microprocessor and direct internet connectivity for streaming.", "Medium", "Understanding"),
         ("How does modern streaming differ from 1950s TV watching?", "Modern streaming allows on-demand watching anytime, whereas 1950s TV relied on fixed broadcast schedules.", "Medium", "Comparing")
     ]),

    # Set 7
    ("Television truly changed the way the world stays informed and entertained!",
     [
         ("What summary conclusion is stated about television?", "Television changed the way the world stays informed and entertained.", "Easy", "Remembering"),
         ("In what way does television keep the world 'informed'?", "By broadcasting live news, weather, documentaries, and global events.", "Easy", "Understanding"),
         ("In what way does television keep the world 'entertained'?", "By delivering movies, sports, cartoons, drama series, and music shows.", "Easy", "Understanding"),
         ("Why is television considered one of the most influential mass media inventions?", "Because it reaches billions of people visually and simultaneously across the globe.", "Medium", "Evaluating"),
         ("What literary tone does this concluding sentence express?", "An appreciative, celebratory, and authoritative tone.", "Medium", "Analyzing")
     ]),

    # Set 8
    ("Word Meaning: Spinning: Turning round quickly. Transmit: To send out electronic signals. Version: A different presentation of same contents.",
     [
         ("What is the definition of 'spinning'?", "Turning round quickly.", "Easy", "Remembering"),
         ("What is the definition of 'transmit'?", "To send out electronic signals or images.", "Easy", "Remembering"),
         ("What is the definition of 'version'?", "A different presentation of the same contents.", "Easy", "Remembering"),
         ("Use the word 'transmit' in a complete sentence of your own.", "Satellites transmit live sports signals across the globe.", "Medium", "Applying"),
         ("Which inventor created a mechanical 'version' of television?", "John Logie Baird.", "Easy", "Understanding")
     ]),

    # Set 9
    ("In 1925, Baird used spinning discs light and electricity... In 1927, Farnsworth transmitted the first electronic image... By the 1950s, many families had them in their homes.",
     [
         ("What event happened in 1925?", "Baird created the first mechanical TV system using spinning discs.", "Easy", "Remembering"),
         ("What event happened in 1927?", "Farnsworth transmitted the first electronic image.", "Easy", "Remembering"),
         ("What milestone was achieved by the 1950s?", "Televisions became widespread in millions of family homes.", "Easy", "Remembering"),
         ("How many years passed between Baird's invention and widespread 1950s home adoption?", "Approximately 25 to 30 years.", "Medium", "Understanding"),
         ("What pattern of technological adoption does this timeline illustrate?", "Inventions begin with experimental prototypes, transition through technical refinements, and achieve mass residential adoption over decades.", "Hard", "Analyzing")
     ]),

    # Set 10
    ("We have flat screens, smart TVs and even internet-connected devices. Thanks to the hard work of inventors like Baird and Farnsworth...",
     [
         ("What physical screen design replaced old bulky TV boxes?", "Flat screens.", "Easy", "Remembering"),
         ("What technology connects modern TVs to digital video platforms?", "Internet connectivity.", "Easy", "Remembering"),
         ("What key attitude allowed Baird and Farnsworth to succeed?", "Hard work, perseverance, and dedication to innovation.", "Easy", "Understanding"),
         ("Why is it important to remember early inventors today?", "Because modern digital tools are built upon the foundational work of past pioneers.", "Medium", "Evaluating"),
         ("Summarize the main message of Chapter 04 in one sentence.", "Television evolved from mechanical and electronic inventions into smart internet devices that revolutionize global communication.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 04: The Invention of Television\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH04_EXT_{q_counter:03d}"
        ext_content += f"\n\n### Question {q_counter}\n"
        ext_content += f"- **Question ID**: {q_id}\n"
        ext_content += f"- **Type**: Extract Based\n"
        ext_content += f"- **Difficulty**: {diff}\n"
        ext_content += f"- **Bloom Level**: {bloom}\n"
        ext_content += f"- **Marks**: 1\n\n"
        ext_content += f"**Question**: {sub_q}\n\n"
        ext_content += f"- **Answer Key**: {sub_a}\n"
        q_counter += 1
    ext_content += "\n\n---\n\n"

with open(os.path.join(CH04_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 04 in {CH04_DIR}")
