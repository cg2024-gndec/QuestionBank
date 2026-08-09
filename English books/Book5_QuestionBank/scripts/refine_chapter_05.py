r"""
Refines all 6 Category files for Book 5 Chapter 05 ("The Invention of the Computer") for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH05_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_05")
os.makedirs(CH05_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Was the computer invented by a single person?", "(A) No, it was developed over many years by several brilliant minds", "(B) Yes, Charles Babbage built it all alone", "(C) Yes, Steve Jobs invented it in one day", "(D) Yes, Alan Turing built it in his garage", "(A)", "Developed over many years by several brilliant minds.", "Easy", "Remembering", "History Concept"),
    ("Who designed the Difference Engine in 1822?", "(A) Charles Babbage", "(B) Ada Lovelace", "(C) Alan Turing", "(D) John Mauchly", "(A)", "Charles Babbage designed the Difference Engine in 1822.", "Easy", "Remembering", "Pioneers"),
    ("What primary task was the Difference Engine designed to perform?", "(A) Mathematical calculations", "(B) Send text messages", "(C) Play audio music", "(D) Display color photographs", "(A)", "Designed to perform mathematical calculations.", "Easy", "Remembering", "Machine Function"),
    ("What was the name of the advanced machine planned by Charles Babbage that is considered the first concept of a modern computer?", "(A) The Analytical Engine", "(B) The Difference Engine", "(C) The ENIAC", "(D) The Apple I", "(A)", "The Analytical Engine is considered the first concept of a modern computer.", "Easy", "Remembering", "Concepts"),
    ("Why could Charles Babbage not complete his Analytical Engine?", "(A) Technology at the time was not advanced enough", "(B) He ran out of paper", "(C) He lost his interest in mathematics", "(D) The King of England forbade it", "(A)", "Technology at the time was not advanced enough.", "Easy", "Understanding", "Historical Barrier"),
    ("Who is known as the world's first computer programmer?", "(A) Ada Lovelace", "(B) Charles Babbage", "(C) Alan Turing", "(D) John Presper Eckert", "(A)", "Ada Lovelace wrote the first instructions/algorithms.", "Easy", "Remembering", "Pioneers"),
    ("What did Ada Lovelace write for Babbage's Analytical Engine?", "(A) The first computer instructions or algorithms", "(B) The first science fiction novel", "(C) A dictionary of numbers", "(D) A piano music composition", "(A)", "She wrote the first instructions or algorithms.", "Easy", "Remembering", "Achievement"),
    ("What machine did British scientist Alan Turing create during World War II?", "(A) A machine to break secret codes", "(B) The first digital pocket watch", "(C) A steam-powered calculator", "(D) A sound recording machine", "(A)", "Alan Turing created a machine that could break secret codes.", "Easy", "Remembering", "World War II"),
    ("What major theoretical field did Alan Turing's ideas help lay the foundation for?", "(A) Modern computers and thinking machines", "(B) Steam engine mechanics", "(C) Radio tower engineering", "(D) Chemical medicine", "(A)", "His ideas laid foundations for modern computers.", "Easy", "Understanding", "Theoretical Impact"),
    ("What was the name of the first electronic computer built in 1945?", "(A) ENIAC", "(B) Microchip", "(C) Analytical Engine", "(D) Difference Engine", "(A)", "ENIAC (Electronic Numerical Integrator and Computer) built in 1945.", "Easy", "Remembering", "Milestones"),
    ("Who built the first electronic computer ENIAC in 1945?", "(A) John Presper Eckert and John Mauchly", "(B) Charles Babbage and Ada Lovelace", "(C) Alan Turing and Bill Gates", "(D) Steve Jobs and Steve Wozniak", "(A)", "Built by John Presper Eckert and John Mauchly in the United States.", "Easy", "Remembering", "Inventors"),
    ("How large was the ENIAC computer when it was built?", "(A) Mammoth, filling an entire room", "(B) Small enough to fit on a wrist", "(C) The size of a handheld book", "(D) The size of a postage stamp", "(A)", "ENIAC was mammoth, filling an entire room.", "Easy", "Remembering", "Physical Size"),
    ("How did ENIAC's calculation speed compare to human speed?", "(A) It could perform calculations much faster than any human", "(B) It was ten times slower than a human", "(C) It made errors every minute", "(D) It calculated at the exact same speed as a child", "(A)", "It performed calculations much faster than any human.", "Easy", "Remembering", "Performance"),
    ("Which 1970s invention made personal computers possible?", "(A) The microchip", "(B) The mechanical disc", "(C) The vacuum tube", "(D) The telegraph key", "(A)", "The invention of the microchip in the 1970s made personal computers possible.", "Easy", "Remembering", "1970s Breakthrough"),
    ("Which companies helped bring computers into homes, schools, and offices around the world?", "(A) Apple, IBM, and Microsoft", "(B) Ford, Boeing, and General Motors", "(C) Sony, Nintendo, and Sega", "(D) Tesla, Space-X, and NASA", "(A)", "Companies like Apple, IBM, and Microsoft helped bring computers into homes.", "Easy", "Remembering", "Tech Companies"),
    ("Where can computers be found today according to Chapter 05?", "(A) On our desks, in our pockets, and even in watches", "(B) Only in secret underground bunkers", "(C) Only on large ocean ships", "(D) Only inside university laboratories", "(A)", "Computers are on desks, in pockets, and in watches.", "Easy", "Remembering", "Ubiquity"),
    ("What does the acronym ENIAC stand for?", "(A) Electronic Numerical Integrator and Computer", "(B) Electrical New Invention And Code", "(C) Engine Numbers In Automatic Calculation", "(D) Electronic National Information And Circuit", "(A)", "ENIAC stands for Electronic Numerical Integrator and Computer.", "Easy", "Remembering", "Acronym"),
    ("What does the word 'mammoth' mean in the vocabulary box?", "(A) Very big or huge in size", "(B) Very tiny or microscopic", "(C) Made of solid wood", "(D) Moving extremely fast", "(A)", "Mammoth means very big.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'integrator' mean?", "(A) Something which joins things so that they become one", "(B) A tool used to cut metal wires", "(C) A device that makes sounds quiet", "(D) A mathematical zero", "(A)", "Integrator means something joining things so they become one.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'algorithm' mean?", "(A) A step-by-step set of instructions for solving a problem", "(B) A physical gear inside a clock", "(C) A secret language used by birds", "(D) A type of computer monitor screen", "(A)", "Algorithm means step-by-step instructions for solving a problem.", "Easy", "Understanding", "Vocabulary"),
    ("In which century did Charles Babbage begin designing computing engines?", "(A) Early 19th century", "(B) 15th century", "(C) 21st century", "(D) 12th century", "(A)", "The journey began in the early 19th century.", "Easy", "Remembering", "Century"),
    ("In which year was Charles Babbage's Difference Engine designed?", "(A) 1822", "(B) 1750", "(C) 1945", "(D) 1999", "(A)", "Difference Engine was designed in 1822.", "Easy", "Remembering", "Dates"),
    ("What conflict led Alan Turing to build code-breaking machines?", "(A) World War II", "(B) World War I", "(C) The American Revolution", "(D) The Napoleonic Wars", "(A)", "Alan Turing created code-breaking machines during World War II.", "Easy", "Remembering", "Historical Event"),
    ("How have computers changed over time regarding size and cost?", "(A) They became smaller, faster, and more affordable", "(B) They became bigger, slower, and more expensive", "(C) They remained identical in size and price", "(D) They disappeared from human society", "(A)", "Over time, computers became smaller, faster, and more affordable.", "Easy", "Remembering", "Evolution Trend"),
    ("What title is given to Chapter 05?", "(A) The Invention of the Computer", "(B) The Invention of Television", "(C) The Missile Man of India", "(D) The Narmada River", "(A)", "Title is 'The Invention of the Computer'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Why is Charles Babbage called the 'Father of Modern Computing' despite not finishing the Analytical Engine?", "(A) His Analytical Engine design established the fundamental logical architecture used in modern computers", "(B) He built the first internet network", "(C) He founded Apple and Microsoft", "(D) He invented electricity", "(A)", "His Analytical Engine established fundamental logical computer architecture.", "Medium", "Analyzing", "Historical Significance"),
    ("What was the unique significance of Ada Lovelace's contribution to computing?", "(A) She realized machines could process symbols and data beyond pure arithmetic by using programmed algorithms", "(B) She manufactured the metal gears for Babbage", "(C) She invented the computer mouse", "(D) She wrote laws governing computer security", "(A)", "Realized machines could process symbolic data via algorithms.", "Medium", "Evaluating", "Lovelace Contribution"),
    ("How did World War II accelerate computer science through Alan Turing's work?", "(A) Urgent military necessity required automated code-breaking, driving creation of early programmable machines", "(B) Soldiers used computers to send emails", "(C) Computers were used to fly airplanes automatically", "(D) WWII stopped all scientific research", "(A)", "Urgent military code-breaking required automated programmable machines.", "Medium", "Analyzing", "Military Impact"),
    ("What made ENIAC a true 'electronic' computer unlike Babbage's engines?", "(A) ENIAC used vacuum tubes and electrical pulses instead of mechanical gears and rods to perform calculations", "(B) ENIAC ran on steam power", "(C) ENIAC used solar energy", "(D) Babbage used microchips while ENIAC used wood", "(A)", "Used vacuum tubes and electrical pulses instead of mechanical gears.", "Medium", "Comparing", "Technical Evolution"),
    ("How did the microchip transform the computer industry in the 1970s?", "(A) By shrinking millions of electronic circuits onto tiny silicon chips, allowing computers to become portable and affordable", "(B) By making computers run on water", "(C) By replacing computer screens with paper", "(D) By making computers room-sized again", "(A)", "Shrank circuits onto tiny chips, enabling portable, affordable personal computers.", "Medium", "Analyzing", "Microchip Revolution"),
    ("What role did companies like Apple, IBM, and Microsoft play in computer history?", "(A) They commercialized personal computer hardware and user-friendly software for homes, schools, and businesses", "(B) They invented mechanical engines in 1822", "(C) They built code-breaking machines for World War II", "(D) They manufactured radio towers", "(A)", "Commercialized PC hardware and software for homes, schools, and offices.", "Medium", "Understanding", "Commercial Impact"),
    ("Compare the physical footprint of ENIAC (1945) with a modern smartphone.", "(A) ENIAC filled an entire 1,800 sq ft room, whereas a modern smartphone fits in a pocket yet is exponentially faster", "(B) ENIAC was smaller than a smartphone", "(C) Both machines weighed 30 tons", "(D) Smartphones fill an entire classroom", "(A)", "ENIAC filled a room (30 tons), whereas a smartphone fits in a pocket.", "Medium", "Comparing", "Footprint Comparison"),
    ("Why is computer programming considered essential for computer operation?", "(A) Hardware cannot perform tasks without software algorithms telling it step-by-step what calculations to execute", "(B) Computers work automatically without any instructions", "(C) Programming is only used to color the computer case", "(D) Hardware creates its own algorithms automatically", "(A)", "Hardware requires software algorithms to direct calculation steps.", "Medium", "Understanding", "Software Concept"),
    ("What does the word 'mammoth' illustrate about 1940s computer hardware?", "(A) Thousands of large vacuum tubes, switches, and heavy cables required massive physical space", "(B) Computers were made from mammoth animal bones", "(C) 1940s computers were weak and tiny", "(D) Vacuum tubes were invisible to human eyes", "(A)", "Thousands of vacuum tubes and cables required massive room space.", "Medium", "Analyzing", "Hardware Context"),
    ("How do computers impact daily human productivity today?", "(A) By automating complex calculations, storing vast data, enabling instant communication, and providing digital learning", "(B) By forcing people to do all math manually", "(C) By eliminating the need for electricity", "(D) By replacing all human thoughts", "(A)", "Automating calculations, storing data, enabling communication, and digital learning.", "Medium", "Evaluating", "Societal Impact"),
    ("What limitation prevented 19th-century engineers from building Babbage's Analytical Engine?", "(A) Precision machining tools were not precise enough to manufacture thousands of intricate metal gears consistently", "(B) Paper was not invented yet", "(C) Engineers did not know mathematics", "(D) Babbage hid his design blueprints", "(A)", "Precision machining could not manufacture thousands of delicate gears consistently.", "Medium", "Understanding", "Engineering Constraint"),
    ("Why is Alan Turing considered a founding father of Artificial Intelligence (AI)?", "(A) He conceptualized 'thinking machines' and proposed criteria for testing machine intelligence (Turing Test)", "(B) He built robots that could walk and talk", "(C) He created the first internet website", "(D) He invented computer video games", "(A)", "Conceptualized thinking machines and criteria for machine intelligence.", "Medium", "Evaluating", "Turing & AI"),
    ("What is the primary difference between a calculator and a general-purpose computer?", "(A) A calculator performs specific fixed math; a general-purpose computer can run unlimited different programmed algorithms", "(B) A calculator uses electricity while a computer does not", "(C) A calculator is bigger than ENIAC", "(D) A computer can only add numbers 1 to 10", "(A)", "Computer runs unlimited programmed algorithms; calculator performs fixed math.", "Medium", "Comparing", "Device Comparison"),
    ("How did World War II code-breaking machines influence postwar civilian computing?", "(A) Wartime breakthroughs in high-speed electronic circuits directly informed the design of commercial computers like ENIAC", "(B) Code-breaking machines were destroyed and forgotten", "(C) Wartime machines were converted into television sets", "(D) Postwar computing returned to mechanical clockwork", "(A)", "Wartime electronic circuit breakthroughs informed commercial computer design.", "Medium", "Analyzing", "Postwar Transfer"),
    ("What lesson about collaborative innovation does Chapter 05 teach Class 5 students?", "(A) Major technological revolutions emerge from generations of inventors building upon each other's ideas over centuries", "(B) One genius invents everything without help", "(C) Innovation stops once a machine is built", "(D) Collaboration slows down scientific discovery", "(A)", "Revolutions emerge from generations of inventors building upon each other.", "Medium", "Evaluating", "Pedagogical Insight"),

    # Hard (41-50)
    ("Critique the transition from mechanical decimal computing (Babbage) to electronic binary computing (ENIAC/Turing).", "(A) Decimal mechanical gears were physically complex and slow, whereas binary electronic circuits (on/off voltage) allowed ultra-fast, reliable calculation", "(B) Decimal gears were faster than electronic voltage", "(C) Binary computing requires mechanical water wheels", "(D) Vacuum tubes only worked with decimal numbers", "(A)", "Binary electronic circuits (on/off voltage) allowed ultra-fast, reliable calculations over physical gears.", "Hard", "Evaluating", "HOTS Computing Architecture"),
    ("Deconstruct Moore's Law as presaged by the 1970s microchip revolution in Chapter 05.", "(A) Shrinking transistor size on microchips exponentially increased computer processing power while dramatically reducing cost and size", "(B) Microchips made computers ten times larger every decade", "(C) Transistors were replaced by mechanical clockwork in 1970", "(D) Computer power decreases as technology advances", "(A)", "Shrinking transistor size exponentially increased power while reducing cost and physical size.", "Hard", "Analyzing", "Moore's Law Analysis"),
    ("Evaluate the ethical and societal responsibility stemming from ubiquitous computing today.", "(A) Universal computer access requires protecting data privacy, preventing digital divides, and promoting responsible technology use", "(B) Computers should be restricted to university professors only", "(C) Data privacy is unimportant in modern society", "(D) Computers eliminate all ethical responsibilities", "(A)", "Requires data privacy protection, bridging digital divides, and responsible usage.", "Hard", "Evaluating", "Ethical Evaluation"),
    ("Compare Ada Lovelace's 1840s algorithmic concepts with modern software engineering.", "(A) Lovelace's loop and branching concepts for the Analytical Engine remain the foundational logic structures of modern coding languages", "(B) Lovelace's algorithms were written in Python", "(C) Modern software engineering uses no logic structures", "(D) Lovelace's work had no relation to programming logic", "(A)", "Lovelace's loop and branching logic concepts remain foundations of modern coding.", "Hard", "Comparing", "Comparative Logic Analysis"),
    ("Formulate a vision of future quantum or biological computing for Class 5 students.", "(A) 'Future computers may use quantum bits or DNA molecules to solve complex climate and medical problems in seconds.'", "(B) 'Future computers will return to room-sized vacuum tube boxes.'", "(C) 'Computers will be replaced by mechanical abacuses.'", "(D) 'Calculations will no longer be needed in science.'", "(A)", "Vision of quantum bits and bio-molecules solving complex global challenges.", "Hard", "Creating", "Future Computing Vision"),
    ("Assess the historical role of government funding in wartime computing breakthroughs.", "(A) Government funding during World War II provided resources for Turing and ENIAC teams, accelerating technology by decades", "(B) Wartime funding slowed down computer research", "(C) Governments banned computer development during wars", "(D) Computing breakthroughs occurred without any funding", "(A)", "Wartime funding accelerated computing breakthroughs by decades.", "Hard", "Evaluating", "Historical Funding Assessment"),
    ("Analyze how GUI (Graphical User Interface) developed by Apple/Microsoft transformed user accessibility.", "(A) GUIs replaced complex text command lines with visual icons and mouse clicks, making computers usable by non-experts", "(B) GUIs made computers harder to use for ordinary people", "(C) GUIs eliminated color screens", "(D) GUIs forced users to write binary code manually", "(A)", "Icons and mouse clicks made computers accessible to non-technical users.", "Hard", "Analyzing", "User Interface Analysis"),
    ("Synthesize how Chapter 05 integrates mathematics, history, and computer science concepts.", "(A) Combines mathematical origins (Babbage/Lovelace) with historical contexts (WWII/1970s) and computer science principles (algorithms/hardware)", "(B) Eliminates history to focus on arithmetic", "(C) Focuses solely on spelling computer terms", "(D) Replaces computer science with ancient geography", "(A)", "Integrates math origins, historical context, and computer science principles.", "Hard", "Synthesizing", "Cross-Disciplinary Synthesis"),
    ("Critique the claim: 'ENIAC was the world's first personal computer.'", "(A) Inaccurate; ENIAC was a room-sized, room-filling multi-user military calculation machine; personal computers emerged only in the 1970s microchip era", "(B) Completely true; ENIAC was built for home desks", "(C) False; ENIAC was a small pocket calculator", "(D) True; ENIAC was sold in retail stores in 1945", "(A)", "Inaccurate; ENIAC was a mammoth room-sized machine; PCs emerged in the 1970s microchip era.", "Hard", "Evaluating", "Historical Accuracy Critique"),
    ("Formulate a comprehensive essay prompt based on Chapter 05 for a Class 5 assessment.", "(A) 'Trace the development of the computer from Babbage's mechanical engines to modern microchips. Highlight the contributions of Babbage, Lovelace, Turing, and ENIAC.'", "(B) 'Write five sentences about your favorite video game.'", "(C) 'List ten brands of laptop computers.'", "(D) 'Draw a picture of a keyboard.'", "(A)", "Comprehensive essay prompt evaluating historical chronology, technical milestones, and pioneer contributions.", "Hard", "Creating", "Assessment Task Design")
]

mcq_content = f"# MCQs — Chapter 05: The Invention of the Computer\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH05_MCQ_{idx:03d}"
    q_txt, opt_a, opt_b, opt_c, opt_d, ans, exp, diff, bloom, topic = item
    mcq_content += f"### Question {idx}\n"
    mcq_content += f"- **Question ID**: {q_id}\n"
    mcq_content += f"- **Type**: MCQ\n"
    mcq_content += f"- **Difficulty**: {diff}\n"
    mcq_content += f"- **Bloom Level**: {bloom}\n"
    mcq_content += f"- **Topic**: {topic}\n"
    mcq_content += f"- **Marks**: 1\n\n"
    mcq_content += f"**Question**: {q_txt}\n\n"
    mcq_content += f"- {opt_a}\n- {opt_b}\n- {opt_c}\n- {opt_d}\n\n"
    mcq_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH05_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("The computer was not invented by one person but developed over many _______.", "years", "Developed over many years.", "Easy"),
    ("Charles Babbage designed the Difference Engine in the year _______.", "1822", "Designed in 1822.", "Easy"),
    ("Charles Babbage planned an advanced machine called the _______ Engine.", "Analytical", "Planned the Analytical Engine.", "Easy"),
    ("Babbage could not complete the Analytical Engine because _______ was not advanced enough.", "technology", "Technology was not advanced enough.", "Easy"),
    ("Ada Lovelace is recognized as the world's first computer _______.", "programmer", "World's first computer programmer.", "Easy"),
    ("Ada Lovelace wrote the first instructions or _______ for Babbage's machine.", "algorithms", "Wrote first instructions or algorithms.", "Easy"),
    ("Alan Turing created a machine during World War II to break secret _______.", "codes", "Machine to break secret codes.", "Easy"),
    ("The first electronic computer was called _______.", "ENIAC", "First electronic computer was ENIAC.", "Easy"),
    ("ENIAC was built in the year _______.", "1945", "Built in 1945.", "Easy"),
    ("ENIAC was built by John Presper Eckert and John _______ in the United States.", "Mauchly", "Built by Eckert and Mauchly.", "Easy"),
    ("ENIAC was _______, filling an entire room.", "mammoth", "ENIAC was mammoth.", "Easy"),
    ("The invention of the _______ in the 1970s made personal computers possible.", "microchip", "Microchip in 1970s.", "Easy"),
    ("Companies like Apple, IBM, and _______ brought computers into homes.", "Microsoft", "Apple, IBM, and Microsoft.", "Easy"),
    ("Today, computers can be found on our desks, in our pockets, and even in _______.", "watches", "Found in watches.", "Easy"),
    ("An integrator is defined as something which joins things so they become _______.", "one", "Joins things so they become one.", "Easy"),
    ("Mammoth means very _______.", "big", "Mammoth means very big.", "Easy"),
    ("Charles Babbage was a British _______.", "mathematician", "Babbage was a British mathematician.", "Easy"),
    ("Alan Turing was a British _______.", "scientist", "Alan Turing was a scientist.", "Easy"),
    ("The Difference Engine was built to perform mathematical _______.", "calculations", "Perform mathematical calculations.", "Easy"),
    ("ENIAC stands for Electronic Numerical Integrator and _______.", "Computer", "Integrator and Computer.", "Easy"),
    ("Personal computers entered homes, schools, and _______ around the world.", "offices", "Homes, schools, and offices.", "Easy"),
    ("Ada Lovelace worked closely with mathematician Charles _______.", "Babbage", "Worked with Charles Babbage.", "Easy"),
    ("Alan Turing's ideas laid the foundation for modern _______.", "computers", "Foundation for modern computers.", "Easy"),
    ("Microchips shrunk electronic circuits onto tiny silicon _______.", "wafers", "Shrunk circuits onto silicon wafers.", "Easy"),
    ("Chapter 05 is titled 'The Invention of the _______'.", "Computer", "Titled 'The Invention of the Computer'.", "Easy"),

    # Medium (26-40)
    ("Babbage's Analytical Engine established the conceptual framework for computer _______.", "architecture", "Established framework for computer architecture.", "Medium"),
    ("Algorithms provide logical step-by-step guidance for software _______.", "execution", "Guidance for software execution.", "Medium"),
    ("Wartime code-breaking accelerated developments in electronic digital _______.", "circuitry", "Accelerated developments in electronic circuitry.", "Medium"),
    ("ENIAC utilized thousands of vacuum tubes for high-speed numerical _______.", "computation", "Vacuum tubes for numerical computation.", "Medium"),
    ("Silicon microchips allowed millions of transistors to fit on one _______.", "chip", "Transistors fit on one chip.", "Medium"),
    ("Personal computing transformed daily education, office work, and global _______.", "communication", "Transformed work and communication.", "Medium"),
    ("Analytical Engine designs included an arithmetic unit and built-in _______.", "memory", "Included arithmetic unit and memory.", "Medium"),
    ("Lovelace envisioned computers processing non-numerical data such as _______.", "music", "Envisioned processing music and symbols.", "Medium"),
    ("Turing's theoretical model laid the groundwork for artificial _______.", "intelligence", "Groundwork for artificial intelligence.", "Medium"),
    ("Miniaturization reduced computer sizes from room-scale to hand-held _______.", "devices", "Reduced size to hand-held devices.", "Medium"),
    ("Early computers relied on punch cards for data input and program _______.", "loading", "Punch cards for program loading.", "Medium"),
    ("Postwar commercial computers automated business inventory and financial _______.", "accounting", "Automated business accounting.", "Medium"),
    ("User-friendly graphical interfaces simplified complex computer _______.", "commands", "Simplified computer commands.", "Medium"),
    ("Computing power doubled continuously while hardware costs steadily _______.", "decreased", "Hardware costs steadily decreased.", "Medium"),
    ("Chapter 05 illustrates the collaborative evolution of information _______.", "technology", "Evolution of information technology.", "Medium"),

    # Hard (41-50)
    ("Binary logic gate processing replaced mechanical gear digit _______.", "wheels", "Replaced gear digit wheels.", "Hard"),
    ("Micro-miniaturization catalyzed the global digital economic _______.", "transformation", "Catalyzed global economic transformation.", "Hard"),
    ("Data processing algorithms enable complex climate modeling and bio-chemical _______.", "simulations", "Enable complex simulations.", "Hard"),
    ("Lovelace's pioneering Bernoulli numbers program demonstrated algorithmic _______.", "looping", "Demonstrated algorithmic looping.", "Hard"),
    ("Turing's universal machine concept proved single hardware can run multi-purpose _______.", "software", "Proved hardware runs software.", "Hard"),
    ("Wartime secret code decryption demonstrated electronic calculation _______.", "superiority", "Demonstrated calculation superiority.", "Hard"),
    ("Transistor integration density defines modern microprocessor performance _______.", "benchmarks", "Defines performance benchmarks.", "Hard"),
    ("Ubiquitous computing embeds intelligent microchips into everyday consumer _______.", "appliances", "Embeds microchips into appliances.", "Hard"),
    ("Historical analysis reveals computing as a multi-century interdisciplinary _______.", "synthesis", "Multi-century interdisciplinary synthesis.", "Hard"),
    ("Chapter 05 demonstrates how mathematical theory translates into physical _______.", "innovation", "Translates theory into physical innovation.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 05: The Invention of the Computer\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH05_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH05_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("The computer was invented by a single person in one afternoon.", "False", "The computer was developed over many years by several brilliant minds.", "Easy"),
    ("Charles Babbage designed the Difference Engine in 1822.", "True", "Text confirms Charles Babbage designed the Difference Engine in 1822.", "Easy"),
    ("Charles Babbage completed the Analytical Engine and built thousands of them.", "False", "He could not complete it because technology at the time was not advanced enough.", "Easy"),
    ("Ada Lovelace is known as the world's first computer programmer.", "True", "Ada Lovelace wrote the first algorithms and is known as the first programmer.", "Easy"),
    ("Alan Turing built a code-breaking machine during World War II.", "True", "Text confirms Alan Turing created a machine to break secret codes.", "Easy"),
    ("The first electronic computer was named ENIAC.", "True", "Text confirms the first electronic computer was called ENIAC.", "Easy"),
    ("ENIAC was built in 1822 by Charles Babbage.", "False", "ENIAC was built in 1945 by John Presper Eckert and John Mauchly.", "Easy"),
    ("ENIAC was mammoth, filling an entire room.", "True", "ENIAC was mammoth and filled an entire room.", "Easy"),
    ("ENIAC calculated much slower than human mathematicians.", "False", "ENIAC performed calculations much faster than any human.", "Easy"),
    ("The invention of the microchip in the 1970s made personal computers possible.", "True", "Microchips made personal computers possible in the 1970s.", "Easy"),
    ("Apple, IBM, and Microsoft helped popularize personal computers.", "True", "These companies brought computers into homes, schools, and offices.", "Easy"),
    ("Today, computers can only be found inside large government laboratories.", "False", "Computers are everywhere—on desks, in pockets, and in watches.", "Easy"),
    ("'Integrator' means something which joins things so they become one.", "True", "Vocabulary definition: Integrator = Something joining things into one.", "Easy"),
    ("'Mammoth' means extremely small or microscopic.", "False", "Mammoth means very big.", "Easy"),
    ("Ada Lovelace worked together with mathematician Charles Babbage.", "True", "Ada Lovelace worked closely with Charles Babbage.", "Easy"),
    ("Alan Turing was a British scientist.", "True", "Alan Turing was a British scientist.", "Easy"),
    ("John Presper Eckert and John Mauchly built ENIAC in the United States.", "True", "Built by Eckert and Mauchly in the US.", "Easy"),
    ("Microchips were invented in the 1910s before World War I.", "False", "Microchips were invented in the 1970s.", "Easy"),
    ("Babbage's Analytical Engine is considered the first concept of a modern computer.", "True", "Analytical Engine is considered the first concept of a modern computer.", "Easy"),
    ("Computers have become larger and more expensive over time.", "False", "Computers became smaller, faster, and more affordable.", "Easy"),
    ("Ada Lovelace wrote algorithms for the Analytical Engine.", "True", "She wrote instructions/algorithms for the Analytical Engine.", "Easy"),
    ("Alan Turing's ideas laid the foundation for modern computers.", "True", "His ideas on thinking machines laid computer science foundations.", "Easy"),
    ("Chapter 05 is titled 'The Invention of the Computer'.", "True", "Chapter title is 'The Invention of the Computer'.", "Easy"),
    ("ENIAC stood for Electronic Numerical Integrator and Computer.", "True", "Full name: Electronic Numerical Integrator and Computer.", "Easy"),
    ("Personal computers became common in homes during the 1970s and 1980s.", "True", "Microchips in 1970s enabled PCs in homes and offices.", "Easy"),

    # Medium (26-40)
    ("Charles Babbage's Difference Engine was designed to process digital images.", "False", "Difference Engine was designed to perform mathematical calculations.", "Medium"),
    ("Ada Lovelace realized computers could process non-numerical symbols and data.", "True", "She envisioned algorithms processing music, text, and general data.", "Medium"),
    ("Wartime code-breaking machines established principles of programmable electronics.", "True", "Turing's code-breaking work advanced programmable computing.", "Medium"),
    ("ENIAC used silicon microchips to process information in 1945.", "False", "ENIAC used vacuum tubes; microchips were invented decades later in the 1970s.", "Medium"),
    ("The microchip allowed complex circuits to fit on tiny silicon wafers.", "True", "Microchips consolidated thousands of circuits onto tiny silicon wafers.", "Medium"),
    ("Personal computers reduced the reliance on room-sized mainframe computers.", "True", "PCs brought computing power directly to individual desks.", "Medium"),
    ("Babbage's designs lacked a memory unit for storing calculation steps.", "False", "The Analytical Engine design included a 'Store' (memory) and a 'Mill' (processor).", "Medium"),
    ("Alan Turing proposed theoretical concepts about machines that could solve problems.", "True", "His theoretical papers defined universal computing machines.", "Medium"),
    ("Computer algorithms are step-by-step instructions that direct software execution.", "True", "Algorithms provide step-by-step rules for software execution.", "Medium"),
    ("Eckert and Mauchly built ENIAC to assist in fast mathematical computations.", "True", "Built to perform high-speed numerical integration and calculation.", "Medium"),
    ("Microchips caused computers to become heavier and more expensive.", "False", "Microchips made computers smaller, faster, and far more affordable.", "Medium"),
    ("Software companies like Microsoft developed operating systems for personal computers.", "True", "Microsoft popularized operating software for personal computers.", "Medium"),
    ("Modern smartwatches contain more computing power than room-sized 1940s computers.", "True", "Modern microprocessors in watches exponentially surpass ENIAC's power.", "Medium"),
    ("Babbage's inability to build his machine proves his mathematical theory was wrong.", "False", "His theory was correct; 19th-century mechanical manufacturing was insufficient.", "Medium"),
    ("Chapter 05 shows that technological evolution involves continuous multi-generational effort.", "True", "Traces progress across Babbage, Lovelace, Turing, Eckert, Mauchly, and microchips.", "Medium"),

    # Hard (41-50)
    ("Mechanical gear computing was inherently faster than electron tube computing.", "False", "Vacuum tube electrical signals moved near light speed, far exceeding gear speeds.", "Hard"),
    ("Ada Lovelace's documentation contained the first published computer algorithm.", "True", "Her notes on the Analytical Engine contained the first published algorithm.", "Hard"),
    ("Turing's work at Bletchley Park was kept secret for many years after WWII.", "True", "Wartime code-breaking details were classified secret for decades.", "Hard"),
    ("ENIAC's programming was changed by rewiring cables manually rather than downloading software.", "True", "ENIAC required physical cable patchboard rewiring to change programs.", "Hard"),
    ("Silicon microchips integrated transistors, resistors, and capacitors onto one chip.", "True", "Integrated circuits consolidated all fundamental components onto one silicon die.", "Hard"),
    ("Computer miniaturization halted entirely after the 1980s.", "False", "Miniaturization continued rapidly into smartphones, wearables, and micro-sensors.", "Hard"),
    ("The Analytical Engine's separation of 'Mill' and 'Store' mirrors CPU and RAM today.", "True", "Babbage's 'Mill' parallels the CPU and his 'Store' parallels RAM/memory.", "Hard"),
    ("Chapter 05 highlights that technological barriers often temporarily delay correct scientific theories.", "True", "Babbage's theory was sound but delayed by 19th-century mechanical fabrication limitations.", "Hard"),
    ("Modern personal computers operate without any electrical energy.", "False", "All digital electronic computers require electric power.", "Hard"),
    ("Chapter 05 connects 19th-century mathematics with 21st-century digital lifestyle for Class 5.", "True", "Bridges historical mathematical foundations with modern daily computer use.", "Hard")
]

tf_content = f"# True / False — Chapter 05: The Invention of the Computer\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH05_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH05_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Was the computer invented by one single person? Explain.", "No, the computer was not invented by one person. It was developed over many years through the contributions of several brilliant mathematicians, scientists, and engineers.", "Easy", "Understanding"),
    ("Who was Charles Babbage and what machine did he design in 1822?", "Charles Babbage was a British mathematician who designed the Difference Engine in 1822 to perform mathematical calculations.", "Easy", "Remembering"),
    ("What was the Analytical Engine and why is it historically famous?", "The Analytical Engine was a machine planned by Charles Babbage that is considered the first concept of a modern general-purpose computer.", "Easy", "Remembering"),
    ("Why was Charles Babbage unable to complete his Analytical Engine?", "He could not complete it because manufacturing technology in the 19th century was not advanced enough to build the complex mechanical parts.", "Easy", "Understanding"),
    ("Who was Ada Lovelace and why is she called the world's first computer programmer?", "Ada Lovelace was a mathematician who worked with Babbage and wrote the first set of written instructions (algorithms) for the Analytical Engine.", "Easy", "Remembering"),
    ("What important contribution did Alan Turing make during World War II?", "Alan Turing created a machine that could break secret enemy codes, laying theoretical foundations for modern computer science.", "Easy", "Remembering"),
    ("What was ENIAC and in which year was it built?", "ENIAC (Electronic Numerical Integrator and Computer) was the first electronic general-purpose computer, built in 1945.", "Easy", "Remembering"),
    ("Who built the ENIAC electronic computer in the United States?", "John Presper Eckert and John Mauchly built the ENIAC in the United States in 1945.", "Easy", "Remembering"),
    ("Describe the physical size and calculation capability of the ENIAC computer.", "ENIAC was mammoth, filling an entire room, but it could perform numerical calculations much faster than any human mathematician.", "Easy", "Remembering"),
    ("What major 1970s invention made personal computers possible?", "The invention of the microchip in the 1970s made personal computers possible by shrinking complex electronic circuits.", "Easy", "Remembering"),
    ("Name three tech companies that helped popularize personal computers in homes and offices.", "Apple, IBM, and Microsoft helped popularize personal computers worldwide.", "Easy", "Remembering"),
    ("Where can computers be found in daily life today?", "Today computers are found everywhere—on our desks, in our pockets (smartphones), and even inside wristwatches.", "Easy", "Remembering"),
    ("What does the word 'mammoth' mean?", "'Mammoth' means very big, huge, or gigantic in physical size.", "Easy", "Understanding"),
    ("What does the word 'integrator' mean?", "'Integrator' means something that joins separate things together so they become one unified system.", "Easy", "Understanding"),
    ("What is an 'algorithm'?", "An algorithm is a step-by-step set of rules or instructions written to solve a specific problem or complete a task.", "Easy", "Understanding"),
    ("What task was Babbage's Difference Engine created to perform?", "It was created to perform accurate mathematical calculations and compile mathematical tables.", "Easy", "Remembering"),
    ("How did personal computers differ from early room-sized computers like ENIAC?", "Personal computers were compact, affordable, and easy for individuals to use on a desk, unlike room-sized ENIAC.", "Easy", "Understanding"),
    ("What role did vacuum tubes play in 1940s electronic computers?", "Vacuum tubes acted as fast electronic switches to process electrical signals and numbers far faster than mechanical gears.", "Easy", "Understanding"),
    ("In which century did Ada Lovelace write the first computer program?", "She wrote the first computer program in the 19th century (1840s).", "Easy", "Remembering"),
    ("What does the acronym ENIAC stand for?", "ENIAC stands for Electronic Numerical Integrator and Computer.", "Easy", "Remembering"),
    ("How did computers change regarding speed, size, and cost over time?", "Computers became drastically smaller in size, much faster in calculation speed, and far more affordable in cost.", "Easy", "Understanding"),
    ("Why did Alan Turing's work help create 'thinking machines'?", "He conceptualized machines that could follow logical rules to solve problems autonomously, establishing artificial intelligence concepts.", "Easy", "Understanding"),
    ("What contribution did IBM make to computer history?", "IBM helped manufacture and popularize business and personal computers for offices and schools around the world.", "Easy", "Remembering"),
    ("What contribution did Microsoft make to computer history?", "Microsoft developed user-friendly software and operating systems that allowed ordinary people to operate personal computers.", "Easy", "Remembering"),
    ("What title is given to Chapter 05?", "The title of Chapter 05 is 'The Invention of the Computer'.", "Easy", "Remembering"),

    # Medium (26-40)
    ("Explain why Charles Babbage's Analytical Engine is considered the true precursor to modern computers.", "It introduced the core architecture of modern computing: input, a processing unit ('Mill'), memory storage ('Store'), and output mechanisms, separating hardware from software logic.", "Medium", "Analyzing"),
    ("How did Ada Lovelace's vision go beyond Charles Babbage's original mathematical focus?", "Babbage focused on numerical math, whereas Lovelace realized the machine could process any symbols or data (including music and graphics) if represented algorithmically.", "Medium", "Analyzing"),
    ("Describe the historical significance of Alan Turing's code-breaking machine during World War II.", "His machine automated the decryption of complex military ciphers, saving millions of lives and proving that electronic machines could execute complex logical reasoning.", "Medium", "Evaluating"),
    ("Contrast the mechanical gears of Babbage's engines with the electronic circuits of ENIAC.", "Babbage's engines relied on physical metal wheels turning mechanically, which was slow and prone to wear. ENIAC used electronic vacuum tubes operating at light speed.", "Medium", "Comparing"),
    ("Why was the invention of the microchip in the 1970s a turning point for global society?", "It compressed millions of electronic components onto a small silicon chip, making computing powerful, portable, and cheap enough for individual ownership.", "Medium", "Evaluating"),
    ("How did companies like Apple and Microsoft change the way people interact with technology?", "They created graphical interfaces, personal computer hardware, and intuitive software, turning technical industrial machines into friendly consumer appliances.", "Medium", "Analyzing"),
    ("Why did Babbage's failure to complete the Analytical Engine not diminish his legacy?", "Because his written designs and logical concepts were mathematically sound and served as the architectural blueprint when electronics developed a century later.", "Medium", "Evaluating"),
    ("Describe how computers evolved from single-purpose tools to general-purpose devices.", "Early tools performed single tasks (math or code-breaking). General-purpose computers can run unlimited different software programs, performing tasks from word processing to gaming.", "Medium", "Analyzing"),
    ("How do algorithms govern the operation of modern smartphone applications?", "Algorithms process user inputs (touches, swipes), make logical calculations, retrieve data from servers, and display visual results on screen step-by-step.", "Medium", "Applying"),
    ("Summarize Chapter 05 in four concise sentences.", "The computer developed over centuries through contributions from several brilliant pioneers. Charles Babbage designed early calculation engines, while Ada Lovelace wrote the first algorithms. Alan Turing created wartime code-breaking machines, and ENIAC emerged as the first room-sized electronic computer in 1945. The 1970s microchip enabled Apple, IBM, and Microsoft to make personal computers ubiquitous worldwide.", "Medium", "Understanding"),
    ("Why were 1940s room-sized computers unsuitable for home or school use?", "They were immense (filling entire rooms), consumed huge electric power, generated intense heat, required team maintenance, and cost millions of dollars.", "Medium", "Understanding"),
    ("How did Ada Lovelace demonstrate that women played a vital role in early STEM history?", "At a time when female scientists were rare, her brilliant mathematical insights created computer programming, establishing women as founding pioneers of software engineering.", "Medium", "Evaluating"),
    ("What is the relationship between computer hardware and computer software?", "Hardware represents physical circuits, chips, and screens. Software represents written algorithmic instructions that tell the physical hardware what tasks to perform.", "Medium", "Comparing"),
    ("How have modern computers transformed the way students learn in schools?", "Computers provide instant access to digital libraries, interactive educational software, online research, global communication, and remote learning platforms.", "Medium", "Applying"),
    ("What advice would you give to a Class 5 student interested in learning computer programming?", "Start by learning basic logical step-by-step thinking, practice block-based coding, stay curious about how algorithms work, and build fun problem-solving projects.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the physical limitations of ENIAC's 18,000 vacuum tubes.", "Vacuum tubes burned out frequently, generated massive heat, consumed 150 kW of power, and required manual cable patchboard rewiring to change programs, making maintenance difficult.", "Hard", "Evaluating"),
    ("Deconstruct the transition from mechanical decimal computing to digital binary computing.", "Decimal mechanics required ten-position gears for digits 0-9. Digital binary uses two electrical voltage states (ON = 1, OFF = 0), enabling ultra-fast, reliable logic gates.", "Hard", "Analyzing"),
    ("Evaluate the impact of widespread computer access on global human collaboration.", "Universal computing connects global researchers, businesses, and communities instantly, allowing collaborative problem-solving across time zones and geographic borders.", "Hard", "Evaluating"),
    ("Compare Charles Babbage's 1822 Difference Engine with John Presper Eckert's 1945 ENIAC.", "Difference Engine: Mechanical, gear-driven, single-task math calculator. ENIAC: Electronic, vacuum tube-driven, high-speed multi-task numerical integrator.", "Hard", "Comparing"),
    ("Formulate a short story about a child visiting the room-sized ENIAC computer in 1945.", "'Ten-year-old Thomas stared in awe at tall metal cabinets filling the vast room. Thousands of glass vacuum tubes glowed red as heavy cables hummed, calculating artillery tables faster than fifty human mathematicians.'", "Hard", "Creating"),
    ("Assess the importance of open theoretical publishing in computer science history.", "Babbage and Lovelace published detailed notes that survived a century, allowing post-WWII scientists to revive and realize their visionary computing architecture.", "Hard", "Evaluating"),
    ("Analyze how software user interfaces (GUIs) democratized technology access.", "GUIs replaced cryptic text command lines with visual icons, folders, and mouse pointers, allowing people of all ages and education levels to operate computers easily.", "Hard", "Analyzing"),
    ("Synthesize how Chapter 05 integrates mathematics, engineering, and history.", "Combines 19th-century mathematics (Babbage/Lovelace), 20th-century history (WWII/1970s), and engineering breakthroughs (vacuum tubes/microchips).", "Hard", "Synthesizing"),
    ("Critique the claim: 'Computing technology has reached its ultimate limit today.'", "False; emerging fields like quantum computing, optical computing, and neural processors continue to expand processing power exponentially beyond current silicon limits.", "Hard", "Evaluating"),
    ("Formulate a 4-line stanza summarizing the history of computing.", "'Babbage planned engines of gears and steel,\nLovelace wrote code to make logic real;\nTuring and ENIAC brought electronic light,\nNow microchips put the world in our sight!'", "Hard", "Creating")
]

sa_content = f"# Short Answer Questions — Chapter 05: The Invention of the Computer\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH05_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH05_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe the early history of computing, detailing the contributions of Charles Babbage and Ada Lovelace in the 19th century.",
     "The journey of computer invention began in the early 19th century with British mathematician Charles Babbage. In 1822, Babbage designed the Difference Engine to perform mathematical calculations automatically. Later, he planned an advanced machine called the Analytical Engine, which included a processing unit, memory storage, and input mechanisms—making it the first true concept of a modern computer. However, Babbage could not complete building it because 19th-century manufacturing technology was not precise enough. Working alongside Babbage, Ada Lovelace studied the Analytical Engine and wrote the first set of written instructions, or algorithms, for it. Because of her visionary work, Ada Lovelace is celebrated as the world's first computer programmer.",
     "Easy", "Remembering"),

    ("Explain the contributions of Alan Turing, John Presper Eckert, and John Mauchly to 20th-century electronic computing.",
     "In the 20th century, computing transitioned from mechanical designs to practical electronic systems. During World War II, British scientist Alan Turing built a landmark machine that could break secret enemy military codes. His theoretical papers on machines that could follow logical rules laid the foundations for computer science and artificial intelligence. In 1945, American engineers John Presper Eckert and John Mauchly built ENIAC (Electronic Numerical Integrator and Computer), recognized as the first general-purpose electronic computer. Although ENIAC was mammoth and filled an entire room, its electronic vacuum tubes allowed it to calculate numerical problems infinitely faster than human mathematicians.",
     "Easy", "Remembering"),

    ("Describe how the 1970s microchip revolution and companies like Apple, IBM, and Microsoft brought computers into everyday life.",
     "For decades after ENIAC, computers remained room-sized mainframes used primarily by military and research institutions. The turning point arrived in the 1970s with the invention of the microchip, which compressed thousands of electronic circuits onto a tiny silicon wafer. Microchips enabled engineers to build compact, affordable 'personal computers' (PCs) suitable for individual desks. Tech companies played key roles in mass adoption: IBM manufactured reliable personal computers for corporate offices and schools, while Apple and Microsoft created user-friendly hardware and operating software. Together, these innovations brought computers into homes, classrooms, and businesses worldwide.",
     "Easy", "Understanding"),

    ("Trace the physical evolution of computers regarding size, speed, cost, and everyday accessibility from 1822 to today.",
     "Computer hardware underwent an astounding physical evolution over two centuries:\n1. **1822 (Babbage Era)**: Heavy mechanical gear engines built from brass and iron, slow and incomplete.\n2. **1945 (ENIAC Era)**: Room-sized mammoth electronic mainframes weighing 30 tons with 18,000 glowing vacuum tubes.\n3. **1970s (Microchip Era)**: Desktop personal computers enabled by silicon chips, fitting on study tables in homes and offices.\n4. **Today (Modern Era)**: Ultra-compact, inexpensive microprocessors embedded everywhere—on desks, in pocket smartphones, and inside wristwatches.",
     "Easy", "Understanding"),

    ("Explain the vocabulary words from Chapter 05: Integrator, Mammoth, and Algorithm with definitions and example sentences.",
     "1. **Integrator**: Something which joins separate parts together into a unified system. *Sentence*: ENIAC stood for Electronic Numerical Integrator and Computer.\n2. **Mammoth**: Extremely big or huge in physical size. *Sentence*: The ENIAC computer was mammoth and filled an entire room.\n3. **Algorithm**: A step-by-step set of written rules or instructions to solve a problem. *Sentence*: Ada Lovelace wrote the world's first computer algorithm.",
     "Easy", "Understanding"),

    ("Discuss why Ada Lovelace's work remains historically significant in computer science.",
     "Ada Lovelace's work is historically significant because she foresaw that computing machines were capable of more than mere arithmetic. While Charles Babbage viewed his engine as a high-speed calculator, Lovelace understood that if a machine could manipulate numbers, those numbers could represent music notes, letters, or symbols. By writing an algorithm to calculate Bernoulli numbers, she proved that software algorithms could direct hardware tasks, founding the discipline of computer programming.",
     "Easy", "Evaluating"),

    ("How did World War II accelerate computer science breakthroughs as described in Chapter 05?",
     "World War II created an urgent military necessity for rapid calculation and code-breaking. Manual encryption and ballistics math were too slow for warfare. This pressure drove governments to fund groundbreaking research, leading Alan Turing to build electromechanical code-breaking machines at Bletchley Park and Eckert and Mauchly to construct ENIAC. These wartime projects proved the speed of electronic computing, spurring the postwar commercial computer industry.",
     "Easy", "Analyzing"),

    ("Explain the difference between Charles Babbage's Difference Engine and his Analytical Engine.",
     "The Difference Engine (designed in 1822) was a specialized mechanical calculator built specifically to compute mathematical tables using polynomial addition. The Analytical Engine (planned later) was a general-purpose programmable machine. It included a central processing unit ('Mill'), memory storage ('Store'), punch-card data inputs, and sequential control—making it the true theoretical conceptual ancestor of modern computers.",
     "Easy", "Comparing"),

    ("Summarize Chapter 05 in five detailed bullet points.",
     "- The computer was developed over centuries by multiple brilliant mathematicians and scientists.\n- Charles Babbage designed the Difference Engine (1822) and Analytical Engine, while Ada Lovelace wrote the first algorithms.\n- Alan Turing created World War II code-breaking machines, establishing computer science foundations.\n- ENIAC, built in 1945 by Eckert and Mauchly, was the first mammoth room-sized electronic computer.\n- The 1970s microchip enabled Apple, IBM, and Microsoft to make personal computers affordable and ubiquitous worldwide.",
     "Easy", "Understanding"),

    ("How do computers help humans in work, learning, and communication today?",
     "Computers transform modern human life across three main areas:\n1. **Work**: Automating financial accounting, designing architecture, managing global supply chains, and storing data.\n2. **Learning**: Providing digital textbooks, educational research tools, interactive simulations, and distance learning platforms.\n3. **Communication**: Powering email, video conferencing, social networks, and instant messaging across global distances.",
     "Easy", "Applying"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why could Charles Babbage not complete the Analytical Engine during his lifetime?", "Babbage faced 19th-century engineering constraints. Metal machining was done by hand, making it impossible to produce thousands of identical cogwheels without friction errors. Additionally, government funding was withdrawn, leaving his masterwork unbuilt.", "Easy", "Understanding"),
    ("Explain how vacuum tubes allowed ENIAC to calculate faster than mechanical gears.", "Vacuum tubes have no moving physical parts. They manipulate streams of electrons at near-light speeds using electrical voltage, allowing ENIAC to perform 5,000 additions per second compared to a few additions per second on mechanical gears.", "Easy", "Understanding"),
    ("Describe the role of microchips in shrinking computer hardware.", "Microchips (integrated circuits) replace bulky wires, vacuum tubes, and separate transistors by printing millions of microscopic electronic components directly onto a tiny silicon wafer, dramatically reducing size and power consumption.", "Easy", "Understanding"),
    ("How did Apple, IBM, and Microsoft contribute to the personal computer revolution?", "IBM established standardized business PC hardware; Apple introduced intuitive graphical user interfaces and aesthetic design; Microsoft authored widespread operating software (MS-DOS/Windows) that made PCs easy to operate.", "Easy", "Understanding"),
    ("Compare the performance of ENIAC in 1945 with a modern smartphone.", "ENIAC weighed 30 tons, filled a room, consumed 150 kW of power, and did 5,000 operations/sec. A smartphone weighs a few ounces, fits in a pocket, runs on a tiny battery, and performs billions of operations/sec.", "Easy", "Comparing"),
    ("Why is computer software just as important as computer hardware?", "Hardware is merely physical machinery. Without software algorithms to direct signal paths and calculation steps, hardware cannot perform any useful tasks. Software gives hardware functional purpose.", "Easy", "Evaluating"),
    ("How did Alan Turing's code-breaking machine help shorten World War II?", "By automating the decryption of secret enemy military ciphers, Turing's machine provided vital intelligence about troop movements and naval plans, saving millions of lives and shortening the war.", "Easy", "Evaluating"),
    ("Explain the concept of an 'algorithm' using a daily life example.", "An algorithm is a step-by-step recipe. For example, a recipe for making tea (boil water → add tea leaves → pour milk → strain) is an algorithm that guarantees the same result when steps are followed in order.", "Easy", "Applying"),
    ("How does Chapter 05 illustrate the value of persistence in scientific research?", "Despite Babbage not seeing his engine built and Lovelace's notes being forgotten for decades, their theoretical persistence created ideas that eventually reshaped global civilization a century later.", "Easy", "Evaluating"),
    ("Discuss how computers are embedded in modern vehicles and household appliances.", "Modern cars, micro-ovens, washing machines, and smart TVs contain dedicated microcontrollers (tiny computers) that automatically regulate engine fuel, washing cycles, temperature, and video display.", "Easy", "Understanding"),
    ("Re-write the story of computing from the perspective of Ada Lovelace in 1843.", "'As I looked at Babbage's drawing of the Analytical Engine, I saw more than numbers. I saw that by weaving algorithms like a Jacquard loom weaves silk, this machine could process words, music, and thought itself!'", "Easy", "Creating"),
    ("What role does binary code (1s and 0s) play in modern digital computing?", "Binary code converts all data—text, images, sound, and video—into combinations of 1s (voltage ON) and 0s (voltage OFF), which microchips process at lightning speed through logic gates.", "Easy", "Understanding"),
    ("How did personal computers empower small businesses and independent workers?", "PCs allowed small businesses to handle accounting, graphic design, document printing, and customer records in-house without hiring expensive corporate computing services.", "Easy", "Analyzing"),
    ("Analyze why Chapter 05 is titled 'The Invention of the Computer' rather than 'The Inventor of the Computer'.", "The title uses 'Invention' to reflect that computing was not created by a single inventor, but evolved as a multi-stage collective achievement across centuries.", "Easy", "Analyzing"),
    ("What future fields of study are emerging from computer science today?", "Emerging fields include Artificial Intelligence (AI), Quantum Computing, Cybersecurity, Robotics, Data Science, and Bio-informatics.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Critically analyze how the separation of hardware and software enabled the software industry.",
     "When early computers (ENIAC) required physical rewiring for each new problem, software did not exist independently. The separation of hardware (central processing units and memory) from software (stored program algorithms) allowed computer code to be written, copied, distributed, and updated without altering physical circuits. This conceptual breakthrough gave birth to the global software industry led by companies like Microsoft.",
     "Medium", "Analyzing"),

    ("Examine the technological shift from mechanical gears (Babbage) to silicon microchips (1970s).",
     "The technological shift spans three mechanical-to-digital physics leaps:\n1. **Mechanical Gears**: Heavy, friction-bound, slow moving parts subject to mechanical wear and manufacturing tolerances.\n2. **Vacuum Tubes**: Frictionless electron streams in glass bulbs operating at kilohertz speeds, but fragile and heat-producing.\n3. **Silicon Microchips**: Solid-state micro-electronics integrating billions of microscopic transistors onto silicon dies, operating silently at gigahertz speeds.",
     "Medium", "Analyzing"),

    ("Evaluate the role of diversity and female leadership in computer history through Ada Lovelace.",
     "Ada Lovelace's foundational role demonstrates that computer science was co-created by female visionaries. At a time when women were excluded from formal scientific academies, Lovelace's intellectual partnership with Babbage produced the world's first published program. Celebrating her legacy inspires gender diversity in modern STEM disciplines.",
     "Medium", "Evaluating"),

    ("Discuss how the miniaturization of computers changed human social behavior.",
     "Miniaturization transformed computers from isolated institutional mainframes into personal companions. Carrying computers in pockets (smartphones) enables instant social networking, continuous navigation, immediate information retrieval, and remote work, blending digital technology seamlessly into daily human behavior.",
     "Medium", "Analyzing"),

    ("Design an interactive classroom debate topic based on Chapter 05.",
     "Debate Topic: 'Has the ubiquity of personal computers made human life better or more complicated?'\n- **Side A (Pro)**: Computers automate tedious labor, connect global families, provide instant education, and advance medicine.\n- **Side B (Con)**: Computers create digital addiction, cause data privacy risks, reduce physical activity, and blur work-life boundaries.",
     "Medium", "Creating"),

    ("How did Alan Turing's theoretical work resolve the problem of universal computation?", "Turing proved mathematically that a single machine ('Universal Turing Machine') could execute any computable task simply by reading different program instructions from tape, eliminating the need for dedicated single-purpose hardware.", "Medium", "Analyzing"),
    ("Contrast the commercial strategy of IBM with the commercial strategy of Apple in the 1970s/1980s.", "IBM targeted corporate businesses with standardized, open-architecture desktop PCs. Apple targeted creative individuals and schools with integrated, visually elegant, user-friendly hardware and software ecosystems.", "Medium", "Comparing"),
    ("Why was the invention of ENIAC kept confidential during its early development?", "ENIAC was developed during World War II under United States military sponsorship to calculate secret artillery firing tables, keeping design details classified until after the war.", "Medium", "Understanding"),
    ("Explain how computer algorithms enable modern search engines to find information.", "Search engine algorithms index billions of web pages, analyze search keywords in milliseconds, score relevancy using mathematical rules, and display the best answers instantly.", "Medium", "Applying"),
    ("How did Charles Babbage's use of punch cards originate from the textile industry?", "Babbage adapted punch cards from Joseph Marie Jacquard's automated weaving loom, which used hole-patterned cards to direct complex fabric patterns automatically.", "Medium", "Understanding"),
    ("Analyze why personal computers succeeded in the 1970s whereas earlier microcomputers failed.", "The 1970s brought affordable silicon microchips, standardized monitors, floppy disk storage, and accessible programming languages (BASIC), creating complete, practical systems.", "Medium", "Analyzing"),
    ("Evaluate the importance of error-checking in early computing machinery.", "Mechanical and vacuum tube systems frequently suffered calculation errors from gear slips or burnt tubes. Inventors designed internal mathematical checks to ensure reliable results.", "Medium", "Evaluating"),
    ("How do modern operating systems manage computer hardware resources?", "Operating systems act as software managers, allocating CPU processing time, RAM memory space, storage access, and peripheral device connections smoothly between running programs.", "Medium", "Understanding"),
    ("Describe the impact of computer development on space exploration.", "Computers processed complex orbital trajectory math, controlled spacecraft guidance systems in real time, and analyzed satellite imaging, enabling moon landings and deep space probes.", "Medium", "Analyzing"),
    ("Construct a fictional speech by Charles Babbage visiting a modern smartphone store.", "'I am astonished! In this palm-sized glass wafer lies an Analytical Engine billions of times faster than my brass cogs, running programs my dear Ada and I could only dream of!'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the structural limitations of the von Neumann computer architecture.",
     "The von Neumann architecture (separating CPU and memory via a shared bus) creates the 'von Neumann bottleneck'. Physical data transfer speed between memory and processor limits overall throughput. Modern hardware addresses this through multi-core CPUs, multi-level high-speed cache memory, and parallel processing.",
     "Hard", "Evaluating"),

    ("Deconstruct the mathematical concept of 'computability' pioneered by Alan Turing.",
     "Turing defined computability by proving which mathematical problems can be solved step-by-step by an automated machine and which cannot (the Halting Problem). This established the formal theoretical boundaries of computer science.",
     "Hard", "Analyzing"),

    ("Synthesize the historical arc of computing across three centuries.",
     "19th Century: Mechanical theory & mathematical algorithms (Babbage/Lovelace).\n20th Century: Electronic vacuum tubes, code-breaking, mainframes, & microchips (Turing/ENIAC/Apple/IBM/Microsoft).\n21st Century: Ubiquitous mobile, cloud, internet-of-things, & artificial intelligence computing.",
     "Hard", "Synthesizing"),

    ("Formulate an advanced assessment task for Class 5 students comparing TV and computer history.",
     "Task: Create a comparative timeline showing how television (Baird/Farnsworth) and computer (Babbage/Turing/ENIAC) technologies evolved in parallel during the 20th century to converge into modern smart devices.",
     "Hard", "Creating"),

    ("Evaluate the ecological and environmental impact of electronic computing hardware.", "While computers boost environmental research, electronic waste (e-waste), rare earth metal mining, and high data center energy consumption pose significant ecological challenges requiring sustainable recycling.", "Hard", "Evaluating"),

    ("Compare ENIAC's patchboard programming with modern high-level languages like Python.", "ENIAC required manual physical cable plugging and switch flipping to change logic. Python uses human-readable text code translated automatically into machine binary by compilers.", "Hard", "Comparing"),
    ("Discuss the philosophical implications of artificial intelligence as envisioned by Alan Turing.", "Turing posed the question 'Can machines think?', suggesting that if a machine behaves indistinguishably from a human in conversation, it exhibits artificial intelligence, sparking debate on consciousness.", "Hard", "Evaluating"),
    ("Analyze how cloud computing alters traditional personal computer storage.", "Cloud computing shifts data storage and heavy processing from local hard drives to remote data center servers connected via internet, allowing access from any device anywhere.", "Hard", "Analyzing"),
    ("Draft an analytical commentary on the line: 'The computer, one of the most important inventions in the world, has a fascinating history.'", "This opening sentence sets a tone of historical awe. It frames the computer not as a static consumer product, but as a dynamic, evolving human achievement shaping global civilization.", "Hard", "Evaluating"),
    ("Synthesize the ultimate educational value of Chapter 05 for primary school computer literacy.", "Chapter 05 teaches that computing is a human story of persistent problem-solving, intellectual collaboration, and continuous technological refinement, inspiring students to become creators of technology.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 05: The Invention of the Computer\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH05_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH05_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("The computer, one of the most important inventions in the world, has a fascinating history. It was not invented by one person but was developed over many years by several brilliant minds.",
     [
         ("What is described as one of the most important inventions in the world?", "The computer.", "Easy", "Remembering"),
         ("Was the computer invented by a single person?", "No, it was developed over many years by several brilliant minds.", "Easy", "Remembering"),
         ("How is the history of the computer characterized?", "It has a fascinating history.", "Easy", "Remembering"),
         ("Why did computer invention require multiple pioneers?", "Because it involved complex stages: mechanical design, algorithmic logic, electronic circuits, and microchips.", "Medium", "Understanding"),
         ("What lesson does this extract convey about major technological breakthroughs?", "Major breakthroughs result from multi-generational collaboration and continuous innovation.", "Medium", "Evaluating")
     ]),

    # Set 2
    ("The journey began in the early 19th century with a mathematician named Charles Babbage. He designed a machine called the Difference Engine in 1822, which could perform mathematical calculations.",
     [
         ("When did the journey of computer invention begin?", "In the early 19th century.", "Easy", "Remembering"),
         ("Who was Charles Babbage?", "A British mathematician.", "Easy", "Remembering"),
         ("What machine did Charles Babbage design in 1822?", "The Difference Engine.", "Easy", "Remembering"),
         ("What task was the Difference Engine created to perform?", "Mathematical calculations.", "Easy", "Remembering"),
         ("What does the word 'calculations' mean?", "Mathematical processes of counting or computing numbers.", "Easy", "Understanding")
     ]),

    # Set 3
    ("Later, he planned an even more advanced machine called the Analytical Engine, considered the first concept of a modern computer. However, Babbage could not complete it because technology at the time was not advanced enough.",
     [
         ("What advanced machine did Babbage plan after the Difference Engine?", "The Analytical Engine.", "Easy", "Remembering"),
         ("What is the Analytical Engine considered in computer history?", "The first concept of a modern computer.", "Easy", "Remembering"),
         ("Why could Babbage not complete the Analytical Engine?", "Because technology at the time was not advanced enough.", "Easy", "Remembering"),
         ("What engineering capability was lacking in the 19th century?", "Precision metal machining to build thousands of delicate gear parts.", "Medium", "Understanding"),
         ("Why is Babbage celebrated despite not completing his machine?", "Because his conceptual architecture established the theoretical blueprint for modern computers.", "Medium", "Evaluating")
     ]),

    # Set 4
    ("Another important figure was Ada Lovelace, who worked with Babbage. She wrote first instructions, or algorithms, for his Analytical Engine. This is why she is known as the world's first computer programmer.",
     [
         ("Who worked closely with Charles Babbage?", "Ada Lovelace.", "Easy", "Remembering"),
         ("What did Ada Lovelace write for the Analytical Engine?", "The first computer instructions, or algorithms.", "Easy", "Remembering"),
         ("What title is Ada Lovelace known by in computer history?", "The world's first computer programmer.", "Easy", "Remembering"),
         ("What is an 'algorithm'?", "A step-by-step set of instructions for solving a problem.", "Easy", "Understanding"),
         ("Why was Lovelace's achievement visionary?", "She foresaw that machines could process non-numerical data like music and graphics using algorithmic code.", "Medium", "Analyzing")
     ]),

    # Set 5
    ("In the 20th century, computers became more practical. During World War II, Alan Turing, a British scientist, created a machine that could break secret codes. His ideas about machines that could think and solve problems laid the foundation for modern computers.",
     [
         ("Who was Alan Turing?", "A British scientist.", "Easy", "Remembering"),
         ("During which historical event did Alan Turing build a code-breaking machine?", "During World War II.", "Easy", "Remembering"),
         ("What was the primary function of Turing's wartime machine?", "To break secret military codes.", "Easy", "Remembering"),
         ("What foundations did Turing's ideas lay for computing?", "Foundations for modern computers and thinking machines (artificial intelligence).", "Medium", "Understanding"),
         ("How did Turing's work change the nature of electronic machinery?", "He proved that electronic machines could execute complex logical problem-solving.", "Medium", "Analyzing")
     ]),

    # Set 6
    ("The first electronic computer, called ENIAC (Electronic Numerical Integrator and Computer), was built in 1945 by John Presper Eckert and John Mauchly in the United States. It was mammoth, filling an entire room, but it could perform calculations much faster than any human.",
     [
         ("What was the name of the first electronic computer?", "ENIAC.", "Easy", "Remembering"),
         ("In what year was ENIAC built?", "1945.", "Easy", "Remembering"),
         ("Who built ENIAC?", "John Presper Eckert and John Mauchly in the United States.", "Easy", "Remembering"),
         ("How large was the ENIAC computer physically?", "It was mammoth, filling an entire room.", "Easy", "Remembering"),
         ("What speed advantage did ENIAC have over human mathematicians?", "It performed calculations much faster than any human.", "Medium", "Understanding")
     ]),

    # Set 7
    ("Over time, computers became smaller, faster and more affordable. The invention of the microchip in the 1970s made it possible to create personal computers. Companies like Apple, IBM and Microsoft helped bring computers into homes, schools and offices around the world.",
     [
         ("Which 1970s invention enabled personal computers?", "The microchip.", "Easy", "Remembering"),
         ("How did computers change over time regarding size, speed, and cost?", "They became smaller, faster, and more affordable.", "Easy", "Remembering"),
         ("Name three tech companies mentioned that popularized personal computers.", "Apple, IBM, and Microsoft.", "Easy", "Remembering"),
         ("Where did personal computers enter people's lives?", "In homes, schools, and offices around the world.", "Easy", "Remembering"),
         ("Why was the microchip critical for desktop personal computers?", "It shrunk millions of electronic circuits onto tiny silicon wafers, reducing hardware size and cost.", "Medium", "Analyzing")
     ]),

    # Set 8
    ("Today, computers are everywhere—on our desks, in our pockets and even in watches! They help us work, learn, play and connect with people worldwide. The invention of the computer truly changed the way we live and work.",
     [
         ("Where can computers be found today according to this passage?", "On our desks, in our pockets, and in watches.", "Easy", "Remembering"),
         ("Name four ways computers help humans today.", "Help us work, learn, play, and connect with people worldwide.", "Easy", "Remembering"),
         ("What final statement describes the computer's overall impact?", "The invention of the computer truly changed the way we live and work.", "Easy", "Remembering"),
         ("What modern handheld device represents a computer 'in our pockets'?", "A smartphone.", "Medium", "Applying"),
         ("Why is the computer considered ubiquitous in modern human society?", "Because microprocessor technology is embedded across everyday work, learning, travel, and communication tools.", "Medium", "Evaluating")
     ]),

    # Set 9
    ("Word Meaning: Integrator: Something which joins things so that they become one. Mammoth: Very big.",
     [
         ("What is the definition of 'integrator'?", "Something which joins things so that they become one.", "Easy", "Remembering"),
         ("What is the definition of 'mammoth'?", "Very big.", "Easy", "Remembering"),
         ("Which computer name contained the word 'Integrator'?", "ENIAC (Electronic Numerical Integrator and Computer).", "Easy", "Remembering"),
         ("Why was the word 'mammoth' applied to ENIAC?", "Because it filled an entire 1,800-square-foot room and weighed 30 tons.", "Medium", "Understanding"),
         ("Use the word 'mammoth' in a complete original sentence.", "Constructing the bridge was a mammoth task that took five years.", "Medium", "Applying")
     ]),

    # Set 10
    ("Charles Babbage designed the Difference Engine... Ada Lovelace wrote first algorithms... Alan Turing created a code-breaking machine... ENIAC was built in 1945... Microchips in 1970s made personal computers possible.",
     [
         ("Who designed the Difference Engine?", "Charles Babbage.", "Easy", "Remembering"),
         ("Who wrote the first computer algorithms?", "Ada Lovelace.", "Easy", "Remembering"),
         ("Who built a code-breaking machine during World War II?", "Alan Turing.", "Easy", "Remembering"),
         ("What hardware breakthrough occurred in the 1970s?", "The invention of the microchip.", "Easy", "Remembering"),
         ("What pattern of technological progression is shown across these pioneers?", "Progressed from 19th-century mechanical theory to 20th-century electronic engineering and 1970s microchip commercialization.", "Hard", "Synthesizing")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 05: The Invention of the Computer\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH05_EXT_{q_counter:03d}"
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

with open(os.path.join(CH05_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 05 in {CH05_DIR}")
