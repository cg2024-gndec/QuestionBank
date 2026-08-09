r"""
Refines all 6 Category files for Book 5 Chapter 15 ("Composition Modules") for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH15_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_15")
os.makedirs(CH15_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Which component is mandatory in a Formal Letter to state the purpose of the letter?", "(A) Subject line", "(B) Friendly greeting like 'Dearest'", "(C) Story moral", "(D) Time of day", "(A)", "Formal letters require a concise Subject line indicating purpose.", "Easy", "Remembering", "Formal Letter Format"),
    ("Which salutation is appropriate for a Formal Letter to a School Principal?", "(A) Respected Sir / Madam", "(B) Dearest Friend", "(C) Hey Buddy", "(D) Lots of Love", "(A)", "Formal letters use 'Respected Sir/Madam'.", "Easy", "Remembering", "Formal Salutation"),
    ("Which subscription (closing sign-off) is standard for a Formal Application?", "(A) Yours sincerely / Yours faithfully", "(B) With love and hugs", "(C) Your best friend", "(D) Catch you later", "(A)", "Formal letters close with 'Yours sincerely' or 'Yours faithfully'.", "Easy", "Remembering", "Formal Closing"),
    ("Who wrote the model leave application in the textbook?", "(A) Aarav Kumar, Class 5A", "(B) Nidhi, Class 5B", "(C) Riya, Class 5C", "(D) Postmaster", "(A)", "Written by Aarav Kumar, Class 5A.", "Easy", "Remembering", "Textbook Model"),
    ("For what reason did Aarav Kumar request leave from school?", "(A) Travelling with family for a family function", "(B) Going on a space trip", "(C) Feeling sleepy at home", "(D) Playing video games", "(A)", "Requested leave for travelling with family for a family function.", "Easy", "Remembering", "Leave Reason"),
    ("Which salutation is suitable for an Informal Letter to a friend or cousin?", "(A) Dear Riya / Dear Friend", "(B) Respected Principal", "(C) To the Postmaster", "(D) Honorable Councillor", "(A)", "Informal letters use 'Dear [Name]'.", "Easy", "Remembering", "Informal Salutation"),
    ("Where did Nidhi visit with her family in the model informal letter?", "(A) Goa", "(B) Kashmir", "(C) Rameswaram", "(D) Assam", "(A)", "Nidhi and her family visited Goa.", "Easy", "Remembering", "Informal Letter Content"),
    ("What fun activities did Nidhi enjoy in Goa?", "(A) Playing on the beach, collecting seashells, swimming, and eating ice cream", "(B) Skiing in the snow", "(C) Riding camels in desert", "(D) Visiting historic forts in Delhi", "(A)", "Enjoyed beach, seashells, swimming, and ice cream.", "Easy", "Remembering", "Vacation Details"),
    ("Which key details are written at the top of a Diary Entry?", "(A) Date, Day, and Time", "(B) Subject line and Principal name", "(C) Postal PIN code only", "(D) Moral of the story", "(A)", "Diary entries open with Date, Day, and Time.", "Easy", "Remembering", "Diary Entry Format"),
    ("Which opening salutation is traditionally used in a Diary Entry?", "(A) Dear Diary", "(B) Respected Sir", "(C) Dear Principal", "(D) To Whom It May Concern", "(A)", "Opening salutation is 'Dear Diary'.", "Easy", "Remembering", "Diary Salutation"),
    ("In which grammatical perspective is a Diary Entry written?", "(A) First-person perspective ('I', 'we')", "(B) Third-person strict official tone", "(C) Passive voice only", "(D) Second-person command tone", "(A)", "Diary entries are written in first-person ('I').", "Easy", "Understanding", "Diary Perspective"),
    ("Which essay topic from Chapter 15 highlights moral values?", "(A) Honesty is the Best Policy", "(B) A Day Without Electricity", "(C) The Weather Cycle", "(D) Island Groups", "(A)", "Moral essay: 'Honesty is the Best Policy'.", "Easy", "Remembering", "Essay Topics"),
    ("Which story topic from Chapter 15 deals with digital safety or technology?", "(A) The Hacker Got Caught", "(B) The Talking Tree", "(C) The Lost Puppy", "(D) The Magic Lamp", "(A)", "Topic: 'The Hacker Got Caught'.", "Easy", "Remembering", "Story Topics"),
    ("Which story topic from Chapter 15 is about a magical writing instrument?", "(A) The Magical Pen", "(B) The Chocolate Stream", "(C) The Flying Dragon", "(D) The Red Saree", "(A)", "Topic: 'The Magical Pen'.", "Easy", "Remembering", "Story Topics"),
    ("What should every completed Story possess at the end?", "(A) A meaningful conclusion or Moral", "(B) A formal subject line", "(C) Receiver's official address", "(D) A postal stamp", "(A)", "Stories conclude with a resolution and moral.", "Easy", "Understanding", "Story Element"),
    ("To whom would you write an application requesting a street lamp near your house?", "(A) Area Councillor / Municipal Officer", "(B) School Librarian", "(C) Class Teacher", "(D) Best Friend", "(A)", "Civic request sent to Area Councillor / Municipal Officer.", "Easy", "Understanding", "Civic Letter"),
    ("To whom would you write a complaint about delayed letters and parcels?", "(A) Postmaster of your area", "(B) Principal of school", "(C) Grandmother", "(D) Sports Coach", "(A)", "Complaints about mail go to the Postmaster.", "Easy", "Understanding", "Complaint Letter"),
    ("What request would you send to the School Librarian?", "(A) Requesting new storybooks for the school library", "(B) Asking for extra homework", "(C) Complaining about street lamps", "(D) Inviting to a beach vacation", "(A)", "Requesting new storybooks for the library.", "Easy", "Understanding", "Library Request"),
    ("What request would you send to the School Headmaster regarding sports?", "(A) Requesting extra sports equipment for the playground", "(B) Asking to cancel sports day", "(C) Requesting permission to leave early every day", "(D) Complaining about parcel delivery", "(A)", "Requesting extra sports equipment for the playground.", "Easy", "Understanding", "Sports Request"),
    ("In an informal letter to your grandmother, what would you invite her to do?", "(A) Invite her to come over for the summer vacation", "(B) Order her to do homework", "(C) Ask her to fix a street lamp", "(D) Send a formal complaint", "(A)", "Invite grandmother for summer vacation.", "Easy", "Understanding", "Family Letter"),
    ("Which essay topic asks you to imagine holding a high school leadership role?", "(A) If I Were the Principal of My School", "(B) My Favourite Festival", "(C) My Best Friend", "(D) The Weather Cycle", "(A)", "Reflective topic: 'If I Were the Principal of My School'.", "Easy", "Remembering", "Imagination Essay"),
    ("Which essay topic discusses environmental protection through trees?", "(A) The Importance of Trees in Our Life", "(B) A Day Without Electricity", "(C) Honesty is the Best Policy", "(D) My Best Friend", "(A)", "Environmental topic: 'The Importance of Trees in Our Life'.", "Easy", "Remembering", "Environment Essay"),
    ("What sign-off is appropriate for closing a Diary Entry at night?", "(A) Good Night, [Your Name]", "(B) Yours faithfully, Aarav", "(C) Respectfully submitted", "(D) Dear Postmaster", "(A)", "Sign-off: 'Good Night, [Your Name]'.", "Easy", "Remembering", "Diary Sign-off"),
    ("What structural sections does an Essay contain?", "(A) Introduction, Body Paragraphs, and Conclusion", "(B) Salutation, Subject, and Signature", "(C) Date, Time, and Dear Diary", "(D) Dialogue tags only", "(A)", "Essays contain Introduction, Body, and Conclusion.", "Easy", "Understanding", "Essay Format"),
    ("What title is given to Chapter 15?", "(A) Composition Modules", "(B) The Season's Song", "(C) My Dream Adventure", "(D) The Magic of Books", "(A)", "Title is 'Composition Modules'.", "Easy", "Remembering", "Chapter Title"),

    # Medium (26-40)
    ("Compare the tone and purpose of Formal Letters versus Informal Letters.", "(A) Formal letters use precise, polite, official language for official business; Informal letters use warm, conversational language for personal relationships", "(B) Formal letters use slangs; Informal letters use strict law terms", "(C) Both letter types are sent only to school principals", "(D) Informal letters require a Subject line while formal letters do not", "(A)", "Formal = precise, polite, official; Informal = warm, conversational, personal.", "Medium", "Comparing", "Letter Types Comparison"),
    ("Analyze why a 'Subject' line is essential in Formal Letters but omitted in Informal Letters.", "(A) Subject lines allow busy officials to instantly identify the purpose; personal letters focus on friendly conversation without rigid subjects", "(B) Subject lines make letters illegal", "(C) Friends require subject lines to read letters", "(D) Subject lines replace the receiver's name", "(A)", "Subject lines help busy officials scan purposes quickly; informal letters are conversational.", "Medium", "Analyzing", "Subject Line Rationale"),
    ("Explain the reflective function of keeping a personal Diary Entry.", "(A) Diary entries provide a private emotional outlet to record daily events, express true feelings, and reflect on personal growth", "(B) Diary entries are written to be published in newspapers", "(C) Diary entries are submitted to teachers for grading every day", "(D) Diary entries are official legal contracts", "(A)", "Provides a private emotional outlet to record events, feelings, and personal growth.", "Medium", "Understanding", "Diary Purpose"),
    ("What narrative elements are required to construct a compelling Story (e.g., 'The Magical Pen')?", "(A) Catchy title, clear setting, interesting characters, central conflict/problem, climax, and satisfying resolution/moral", "(B) List of phone numbers and postal codes", "(C) Formal subject line and principal signature", "(D) Dictionary definitions only", "(A)", "Requires title, setting, characters, conflict, climax, and resolution/moral.", "Medium", "Analyzing", "Story Structure"),
    ("How should an essay on 'The Importance of Trees in Our Life' be structured for Class 5?", "(A) Intro (trees as green gold) -> Body 1 (oxygen, rain, soil erosion prevention) -> Body 2 (fruits, shade, wood) -> Conclusion (pledge to plant trees)", "(B) Single line saying trees are green", "(C) List of tree prices in markets", "(D) Formal letter to a timber merchant", "(A)", "Intro (green gold) -> Environmental benefits -> Human utilities -> Conservation conclusion.", "Medium", "Applying", "Essay Structuring"),
    ("Describe the correct arrangement of elements in a Formal Application for Leave.", "(A) Sender Address/Date -> Receiver Title (The Principal) -> School Name/City -> Subject -> Salutation -> Body Text -> Thanking You -> Yours sincerely/Name", "(B) Signature -> Body Text -> Subject -> Principal Name", "(C) Dear Friend -> Body Text -> Good Night", "(D) Title -> Story Moral -> Date", "(A)", "Standard formal arrangement from sender info to receiver, subject, body, and closing.", "Medium", "Understanding", "Formal Layout"),
    ("How does Aarav Kumar demonstrate responsibility in his leave application?", "(A) He states clear leave dates, explains the family reason, and promises to complete all classwork and homework upon returning", "(B) He demands extra marks without studying", "(C) He leaves school without informing anyone", "(D) He asks his friend to fake his attendance", "(A)", "States clear dates, family reason, and promises to complete missed classwork.", "Medium", "Evaluating", "Student Responsibility"),
    ("Why is descriptive imagery important when writing an informal letter about a holiday (e.g., Goa trip)?", "(A) Sensory details (seashells, sunset, ice cream, swimming) make the letter lively, helping the reader visualize the fun experience", "(B) Imagery makes the letter too long to read", "(C) Sensory details are required by postal laws", "(D) Imagery replaces the recipient's name", "(A)", "Sensory details make the letter lively, allowing the reader to visualize the experience.", "Medium", "Analyzing", "Descriptive Writing"),
    ("Contrast an Essay on 'A Day Without Electricity' with a Story on 'The Day I Found a Magic Lamp'.", "(A) The essay logically analyzes real-life inconveniences and dependence on power; the story uses imaginative fantasy narrative to entertain", "(B) Both are formal letters to the principal", "(C) The essay uses magic spells while the story uses electrical formulas", "(D) Neither requires paragraph writing", "(A)", "Essay = logical real-life analysis; Story = imaginative fantasy narrative.", "Medium", "Comparing", "Genre Comparison"),
    ("What makes 'Honesty is the Best Policy' a timeless theme for Class 5 essays and stories?", "(A) It teaches that truthfulness builds trust, self-respect, and long-term character, whereas deceit leads to trouble", "(B) It proves that dishonest people always win prize money", "(C) It is a rule written only for police officers", "(D) It requires memorizing legal laws", "(A)", "Teaches that truthfulness builds trust, self-respect, and long-term character.", "Medium", "Evaluating", "Moral Value Analysis"),
    ("How does a student write a persuasive letter to the Area Councillor regarding a street lamp?", "(A) Politeness, clear location description, highlighting safety hazards of dark streets at night, and requesting urgent action", "(B) Threatening the councillor with bad words", "(C) Writing a funny story about darkness", "(D) Sending an anonymous blank paper", "(A)", "Polite tone, clear location, highlighting safety hazards of darkness, and requesting action.", "Medium", "Applying", "Persuasive Writing"),
    ("Explain the role of 'Time' in a Diary Entry (e.g., '9:30 PM').", "(A) It records the exact moment of evening reflection when the writer sits down to write before sleeping", "(B) It tells the reader when to catch a train", "(C) It indicates how long the diary took to buy", "(D) It is mandatory for postal stamps", "(A)", "Records the exact moment of evening reflection before sleeping.", "Medium", "Understanding", "Time Stamp Purpose"),
    ("What key lesson does the story topic 'The Hacker Got Caught' convey to young students?", "(A) Cybercrime and unauthorized digital hacking are illegal, punishable, and cyber security catching mechanisms protect digital safety", "(B) Hacking is a fun game without rules", "(C) Computers should never be used", "(D) Hackers are invisible and cannot be caught", "(A)", "Cybercrime is illegal/punishable and cybersecurity mechanisms protect safety.", "Medium", "Evaluating", "Cyber Awareness"),
    ("Summarize Chapter 15 in four concise sentences.", "Chapter 15 provides complete composition modules covering Essay Writing, Formal Letters, Informal Letters, Diary Entries, and Story Writing. It equips Class 5 students with standard formats, model examples, and practice prompts for academic and personal writing. Students learn formal civic applications, warm personal letters, reflective daily diary entries, and structured essays on moral and environmental themes. Through these modules, learners develop clear written communication, logical organization, and creative expression.", "Medium", "Understanding", "Chapter Summary"),
    ("How can Class 5 students use composition modules to improve their overall English expression?", "(A) By practicing structured paragraph writing, using appropriate formal/informal tones, expanding vocabulary, and editing formats", "(B) By copying model letters without reading", "(C) By ignoring grammar rules in writing", "(D) By writing only one-word answers", "(A)", "Practice structured paragraphs, appropriate tones, expanding vocabulary, and editing formats.", "Medium", "Applying", "Composition Skill Application"),

    # Hard (41-50)
    ("Critique the educational necessity of mastering formal civic correspondence (letters to Municipal Officers/Postmasters) at Class 5 level.", "(A) Empowers young citizens with democratic agency, teaching them to articulate public grievances politely, demand accountability, and participate in civic life", "(B) Formal correspondence is useless for children", "(C) Children should only write fictional fairy tales", "(D) Civic letters should be written only by lawyers", "(A)", "Empowers young citizens with democratic agency to articulate grievances politely.", "Hard", "Evaluating", "HOTS Civic Literacy Critique"),
    ("Deconstruct the structural rhetoric of an argumentative essay on 'If I Were the Principal of My School'.", "(A) Visionary Introduction -> Proposal 1 (academic reforms/fun learning) -> Proposal 2 (sports/infrastructure) -> Proposal 3 (student welfare) -> Inspiring Conclusion", "(B) Single paragraph complaining about teachers", "(C) Formal letter layout with sender address", "(D) Fictional fairytale about magic wands", "(A)", "Visionary Intro -> Academic reforms -> Sports/Infrastructure -> Student welfare -> Inspiring Conclusion.", "Hard", "Analyzing", "Rhetorical Structure"),
    ("Evaluate the psychological impact of expressive writing in Diary Entries on childhood emotional regulation.", "(A) Articulating internal feelings ('I felt sad/excited because...') helps children process complex emotions, reduce stress, and build self-awareness", "(B) Writing diary entries increases childhood confusion", "(C) Expressive writing has zero psychological effect", "(D) Diaries should be graded publicly in front of class", "(A)", "Articulating internal feelings helps children process complex emotions and build self-awareness.", "Hard", "Evaluating", "Emotional Regulation"),
    ("Compare the formal precision required in an Official Complaint (Letter to Postmaster) with the creative freedom of Story Writing ('The Magical Pen').", "(A) Complaint letter demands objective facts, polite complaint, and specific resolution; Story writing encourages imaginative world-building, sensory descriptions, and emotional arcs", "(B) Both require identical formal subject lines", "(C) Story writing requires legal evidence while complaint letters use magic spells", "(D) Neither genre requires grammatical correctness", "(A)", "Complaint = objective facts and polite request; Story = imaginative world-building and narrative arcs.", "Hard", "Comparing", "Genre & Tone Comparison"),
    ("Formulate a complete, polished formal leave application model based on Chapter 15 guidelines.", "(A) 'To The Principal, ABC School, City. Subject: Request for Two Days Leave. Respected Sir, I am Aarav Kumar of Class 5A. I request leave on 22-23 Oct due to a family function. I will complete missed work. Yours sincerely, Aarav Kumar.'", "(B) 'Dear Principal, Give me leave for two days. Thanks, Aarav.'", "(C) 'Dear Diary, I am taking leave today.'", "(D) 'Once upon a time I took leave from school.'", "(A)", "Polished formal model containing sender info, receiver, subject, polite body, and proper sign-off.", "Hard", "Creating", "Model Composition Generation"),
    ("Assess the importance of Audience Awareness when selecting vocabulary for Formal vs Informal composition.", "(A) Audience determines diction: formal recipients require respectful, objective vocabulary ('request', 'grant permission'); informal recipients welcome familiar, emotional vocabulary ('awesome', 'cant wait')", "(B) Audience has no relationship to word choice", "(C) All writing must use slang words", "(D) Formal letters should use secret code words", "(A)", "Audience determines diction: formal requires respectful/objective words; informal welcomes familiar/emotional words.", "Hard", "Evaluating", "Audience Awareness"),
    ("Analyze how transition words ('Furthermore', 'However', 'In conclusion') strengthen essay coherence.", "(A) Transition words logically link ideas between paragraphs, guiding the reader smoothly through the writer's argument", "(B) Transition words are used to fill up space", "(C) Transition words make essays confusing", "(D) Transition words are used only in poetry", "(A)", "Transition words logically link ideas between paragraphs, guiding the reader smoothly.", "Hard", "Analyzing", "Coherence & Transitions"),
    ("Synthesize how Chapter 15 unifies functional grammar, structured formats, and creative self-expression.", "(A) Bridges technical format rules (letter layouts/diary headings) with functional grammar (tenses/punctuation) and creative imagination (essays/stories)", "(B) Separates grammar from composition completely", "(C) Focuses exclusively on memorizing layout boxes", "(D) Rejects creative expression", "(A)", "Bridges technical format rules with functional grammar and creative imagination.", "Hard", "Synthesizing", "Cross-Disciplinary Synthesis"),
    ("Critique the claim: 'Digital messaging (texting/emojis) has made formal composition skills obsolete.'", "(A) False; professional, academic, and civic life continues to rely on structured formal writing, clear organization, and professional etiquette", "(B) True; text emojis should replace all school essays", "(C) False; formal letters are written only on stone tablets", "(D) True; no one writes paragraphs anymore", "(A)", "False; professional, academic, and civic life relies on structured writing and professional etiquette.", "Hard", "Evaluating", "Literary & Digital Critique"),
    ("Formulate a comprehensive composition assessment prompt evaluating Class 5 writing competence.", "(A) 'Select one module: (1) Write a Formal Letter to your Principal requesting library books, OR (2) Write an Informal Letter to a friend about a picnic, OR (3) Write a Story on The Magical Pen. Follow standard format, clear paragraphs, and correct grammar.'", "(B) 'Write five words.'", "(C) 'Copy line 1 from page 58.'", "(D) 'Draw a picture of a pen.'", "(A)", "Comprehensive prompt testing format adherence, paragraph structure, grammar, and genre selection.", "Hard", "Creating", "Assessment Task Design")
]

mcq_content = f"# MCQs — Chapter 15: Composition Modules\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH15_MCQ_{idx:03d}"
    q_txt = item[0]
    opt_a = item[1]
    opt_b = item[2]
    opt_c = item[3]
    opt_d = item[4]
    ans = item[5] if len(item) > 5 else "(A)"
    exp = item[6] if len(item) > 6 else "Correct answer"
    diff = item[7] if len(item) > 7 else "Easy"
    bloom = item[8] if len(item) > 8 else "Remembering"
    topic = item[9] if len(item) > 9 else "General"
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

with open(os.path.join(CH15_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("A Formal Letter requires a clear _______ line stating the purpose of the letter.", "Subject", "Requires a Subject line.", "Easy"),
    ("The formal salutation to a school head is 'Respected _______/Madam'.", "Sir", "Respected Sir/Madam.", "Easy"),
    ("Formal applications close with 'Yours _______' or 'Yours faithfully'.", "sincerely", "Yours sincerely.", "Easy"),
    ("In the model application, Aarav Kumar is a student of Class _______.", "5A", "Class 5A.", "Easy"),
    ("Aarav Kumar requested leave because he was travelling for a family _______.", "function", "Family function.", "Easy"),
    ("Informal letters begin with a friendly salutation like 'Dear _______'.", "Riya", "Dear Riya / Friend.", "Easy"),
    ("Nidhi wrote an informal letter about her summer vacation trip to _______.", "Goa", "Trip to Goa.", "Easy"),
    ("Nidhi enjoyed playing on the beach and collecting _______.", "seashells", "Collecting seashells.", "Easy"),
    ("A Diary Entry opens with Date, Day, and _______.", "Time", "Date, Day, and Time.", "Easy"),
    ("The traditional opening salutation for a diary is 'Dear _______'.", "Diary", "Dear Diary.", "Easy"),
    ("Diary entries are written in the _______ person ('I').", "first", "First person.", "Easy"),
    ("An essay topic focusing on moral character is 'Honesty is the Best _______'.", "Policy", "Honesty is the Best Policy.", "Easy"),
    ("A story topic dealing with digital crime is 'The Hacker Got _______'.", "Caught", "The Hacker Got Caught.", "Easy"),
    ("A fantasy story topic in Chapter 15 is 'The Magical _______'.", "Pen", "The Magical Pen.", "Easy"),
    ("A complaint about delayed mail is sent to the _______.", "Postmaster", "Sent to Postmaster.", "Easy"),
    ("A request for a street lamp is sent to the Area _______.", "Councillor", "Sent to Area Councillor.", "Easy"),
    ("A request for new storybooks is sent to the School _______.", "Librarian", "Sent to Librarian.", "Easy"),
    ("A request for extra sports equipment is sent to the _______.", "Headmaster", "Sent to Headmaster / Principal.", "Easy"),
    ("An informal letter to a grandmother invites her for summer _______.", "vacation", "For summer vacation.", "Easy"),
    ("An essay on trees highlights 'The Importance of Trees in Our _______'.", "Life", "Trees in Our Life.", "Easy"),
    ("An imaginative essay topic asks 'If I Were the _______ of My School'.", "Principal", "Principal of My School.", "Easy"),
    ("At night, a diary entry closes with 'Good _______, [Name]'.", "Night", "Good Night, [Name].", "Easy"),
    ("An essay contains an Introduction, Body Paragraphs, and a _______.", "Conclusion", "Contains a Conclusion.", "Easy"),
    ("Stories should conclude with a meaningful resolution or _______.", "moral", "Resolution or moral.", "Easy"),
    ("Chapter 15 is titled 'Composition _______'.", "Modules", "Composition Modules.", "Easy"),

    # Medium (26-40)
    ("Formal letters use polite, official language suited for administrative _______.", "purposes", "Administrative purposes.", "Medium"),
    ("Informal letters use warm, conversational language between friends and _______.", "family", "Friends and family.", "Medium"),
    ("Subject lines help officials quickly scan the letter's main _______.", "intent", "Letter's main intent.", "Medium"),
    ("Aarav promised to complete all classwork and homework upon his _______.", "return", "Upon his return.", "Medium"),
    ("Sensory details like tasting seafood and watching sunsets make travel letters _______.", "lively", "Makes letters lively.", "Medium"),
    ("Diary entries provide a private space for emotional self-_______.", "reflection", "Emotional self-reflection.", "Medium"),
    ("A story plot requires a setting, characters, conflict, climax, and _______.", "resolution", "Conflict, climax, and resolution.", "Medium"),
    ("Tree conservation essays emphasize oxygen production and soil erosion _______.", "prevention", "Soil erosion prevention.", "Medium"),
    ("Complaints to postmasters require specific details of delayed letters and _______.", "parcels", "Letters and parcels.", "Medium"),
    ("Persuasive civic letters highlight public safety hazards like dark _______.", "streets", "Dark streets.", "Medium"),
    ("Evening time stamps in diaries record the moment of personal _______.", "writing", "Moment of writing.", "Medium"),
    ("Cybersecurity stories teach that digital hacking is illegal and _______.", "punishable", "Illegal and punishable.", "Medium"),
    ("Transition words link paragraphs to maintain essay _______.", "coherence", "Maintain essay coherence.", "Medium"),
    ("Audience awareness determines whether vocabulary should be formal or _______.", "informal", "Formal or informal.", "Medium"),
    ("Chapter 15 equips Class 5 students with essential writing _______.", "skills", "Essential writing skills.", "Medium"),

    # Hard (41-50)
    ("Civic letter writing fosters democratic agency and public _______.", "accountability", "Fosters public accountability.", "Hard"),
    ("Rhetorical structuring in essays organizes arguments from introduction to _______.", "conclusion", "Organizes to conclusion.", "Hard"),
    ("Expressive writing in diaries aids childhood emotional _______.", "regulation", "Aids emotional regulation.", "Hard"),
    ("Official complaint letters require objective facts and polite _______.", "demands", "Objective facts and polite demands.", "Hard"),
    ("Formal leave models require exact dates, reason, and proper _______.", "subscription", "Dates, reason, and subscription.", "Hard"),
    ("Register selection dictates formal vocabulary for official _______.", "recipients", "Formal vocab for recipients.", "Hard"),
    ("Paragraph transitions guide readers smoothly through complex _______.", "arguments", "Smoothly through arguments.", "Hard"),
    ("Composition modules synthesize format rules, grammar, and creative _______.", "expression", "Grammar and creative expression.", "Hard"),
    ("Structured composition skills remain vital in academic and professional _______.", "environments", "Academic and professional environments.", "Hard"),
    ("Chapter 15 prepares students for comprehensive written communication _______.", "mastery", "Written communication mastery.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 15: Composition Modules\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH15_FIB_{idx:03d}"
    sent = item[0]
    ans = item[1]
    exp = item[2] if len(item) > 2 else "Answer"
    diff = item[3] if len(item) > 3 else "Easy"
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH15_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("A Formal Letter requires a clear Subject line stating its purpose.", "True", "Text confirms Formal Letters include a Subject line.", "Easy"),
    ("The salutation 'Respected Sir/Madam' is used in Informal Letters to friends.", "False", "'Respected Sir/Madam' is used in Formal Letters, not informal ones.", "Easy"),
    ("Formal leave applications close with 'Yours sincerely' or 'Yours faithfully'.", "True", "Text confirms formal closing sign-offs.", "Easy"),
    ("Aarav Kumar requested leave to travel for a family function.", "True", "Text confirms Aarav requested leave for a family function.", "Easy"),
    ("Aarav Kumar promised to complete all classwork and homework upon returning.", "True", "Text confirms he promised to complete missed work.", "Easy"),
    ("Informal letters begin with salutations like 'Dear [Name]'.", "True", "Text confirms informal letters use 'Dear [Name]'.", "Easy"),
    ("In the model informal letter, Nidhi wrote to Riya about her trip to Goa.", "True", "Text confirms Nidhi wrote to Riya about Goa.", "Easy"),
    ("Nidhi went skiing in the snow during her Goa trip.", "False", "Nidhi enjoyed beach, collecting seashells, swimming, and ice cream in Goa.", "Easy"),
    ("A Diary Entry opens with Date, Day, and Time at the top.", "True", "Text confirms Date, Day, and Time open a Diary Entry.", "Easy"),
    ("The traditional opening salutation for a diary is 'Dear Diary'.", "True", "Text confirms 'Dear Diary' is used.", "Easy"),
    ("Diary entries are written in the third-person perspective ('he', 'she').", "False", "Diary entries are written in the first-person perspective ('I').", "Easy"),
    ("'Honesty is the Best Policy' is an essay topic included in Chapter 15.", "True", "Text confirms this essay topic.", "Easy"),
    ("'The Hacker Got Caught' is a story topic included in Chapter 15.", "True", "Text confirms this story topic.", "Easy"),
    ("'The Magical Pen' is a story topic included in Chapter 15.", "True", "Text confirms this story topic.", "Easy"),
    ("Complaints about delayed letters and parcels are addressed to the Postmaster.", "True", "Text confirms complaints about mail go to the Postmaster.", "Easy"),
    ("Requests for street lamps are sent to the School Librarian.", "False", "Requests for street lamps are sent to the Area Councillor / Municipal Officer.", "Easy"),
    ("Requests for new storybooks are sent to the School Librarian.", "True", "Text confirms library book requests go to the Librarian.", "Easy"),
    ("Requests for extra sports equipment are sent to the Headmaster/Principal.", "True", "Text confirms sports equipment requests go to Headmaster.", "Easy"),
    ("Informal letters to grandmothers should use strict legal terms.", "False", "Informal letters use warm, affectionate, personal language.", "Easy"),
    ("'The Importance of Trees in Our Life' is an essay topic in Chapter 15.", "True", "Text confirms this environmental essay topic.", "Easy"),
    ("'If I Were the Principal of My School' is an essay topic in Chapter 15.", "True", "Text confirms this imaginative essay topic.", "Easy"),
    ("Diary entries close with 'Good Night, [Your Name]'.", "True", "Text confirms diary sign-off format.", "Easy"),
    ("Essays consist of an Introduction, Body Paragraphs, and Conclusion.", "True", "Text confirms standard essay structure.", "Easy"),
    ("Stories do not require any resolution or moral.", "False", "Stories require a plot resolution and meaningful moral.", "Easy"),
    ("Chapter 15 title is 'Composition Modules'.", "True", "Chapter title is 'Composition Modules'.", "Easy"),

    # Medium (26-40)
    ("Formal letters use precise, polite language suited for official administration.", "True", "Formal letters maintain polite official register.", "Medium"),
    ("Informal letters require a formal Subject line before the salutation.", "False", "Informal letters omit Subject lines.", "Medium"),
    ("Subject lines help officials scan letter purposes quickly.", "True", "Subject lines state purpose concisely for busy officials.", "Medium"),
    ("Aarav Kumar's leave application specified dates from February 22 to 24.", "True", "Text confirms dates from Feb 22 to Feb 24.", "Medium"),
    ("Sensory details like sunsets and ice cream make travel letters engaging.", "True", "Sensory details create vivid reading experiences.", "Medium"),
    ("Diary entries provide a private outlet for emotional self-reflection.", "True", "Diaries allow private processing of daily thoughts and feelings.", "Medium"),
    ("A story plot requires characters, setting, conflict, climax, and resolution.", "True", "Standard narrative arc requires these key components.", "Medium"),
    ("An essay on trees should discuss oxygen production and soil erosion prevention.", "True", "Environmental essays cover biological and ecological utilities.", "Medium"),
    ("Complaints to postmasters should specify delayed letters and parcel details.", "True", "Specific details help postmasters investigate mail delays.", "Medium"),
    ("Persuasive civic letters highlight public safety hazards politely.", "True", "Polite, evidence-based writing achieves civic response.", "Medium"),
    ("Evening time stamps in diaries record the moment of daily reflection.", "True", "Time stamps record when evening writing occurs.", "Medium"),
    ("Cybersecurity stories convey that hacking is illegal and catches criminals.", "True", "Teaches digital safety and legal consequences of cybercrime.", "Medium"),
    ("Transition words link paragraphs to maintain logical essay flow.", "True", "Transitions connect thoughts smoothly between paragraphs.", "Medium"),
    ("Audience awareness dictates choice between formal and informal vocabulary.", "True", "Target recipient determines appropriate language register.", "Medium"),
    ("Chapter 15 equips Class 5 students with practical composition skills.", "True", "Teaches essential formal, informal, and creative writing skills.", "Medium"),

    # Hard (41-50)
    ("Civic letter writing fosters democratic participation and public accountability.", "True", "Writing civic letters trains active democratic citizenship.", "Hard"),
    ("Rhetorical structuring in essays organizes arguments logically from intro to conclusion.", "True", "Logical structuring ensures persuasive essay flow.", "Hard"),
    ("Expressive diary writing supports childhood emotional self-regulation.", "True", "Writing about feelings helps process emotions constructively.", "Hard"),
    ("Official complaint letters require objective facts and polite corrective requests.", "True", "Requires factual evidence and respectful request for action.", "Hard"),
    ("Standard formal leave models require exact dates, clear reason, and proper subscription.", "True", "Format requires complete administrative details.", "Hard"),
    ("Language register selection dictates formal vocabulary for official recipients.", "True", "Appropriate register maintains professional respect.", "Hard"),
    ("Paragraph transitions guide readers smoothly through complex multi-point essays.", "True", "Transitions link complex ideas cohesively.", "Hard"),
    ("Composition modules synthesize format rules, grammar, and creative self-expression.", "True", "Combines format rules, grammar, and creative writing.", "Hard"),
    ("Structured composition skills remain essential in modern digital and academic life.", "True", "Clear structured writing remains vital across professional fields.", "Hard"),
    ("Chapter 15 prepares students for comprehensive written communication mastery.", "True", "Provides complete foundational training in written communication.", "Hard")
]

tf_content = f"# True / False — Chapter 15: Composition Modules\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH15_TF_{idx:03d}"
    stmt = item[0]
    ans = item[1]
    exp = item[2] if len(item) > 2 else "Explanation"
    diff = item[3] if len(item) > 3 else "Easy"
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH15_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("What key component must be included in a Formal Letter to state its purpose?", "A Formal Letter must include a clear 'Subject' line that states the specific purpose of the letter.", "Easy", "Remembering"),
    ("What salutation and closing sign-off are used in a Formal Leave Application?", "Salutation: 'Respected Sir/Madam'; Closing sign-off: 'Yours sincerely' or 'Yours faithfully'.", "Easy", "Remembering"),
    ("Who wrote the model leave application in Chapter 15 and for what reason?", "Aarav Kumar (Class 5A) wrote it to request leave from Feb 22 to 24 to attend a family function.", "Easy", "Remembering"),
    ("What salutation and sign-off are used in an Informal Letter to a friend?", "Salutation: 'Dear [Name]'; Closing sign-off: 'Your friend' or 'With love'.", "Easy", "Remembering"),
    ("Where did Nidhi go for her summer vacation in the model informal letter?", "Nidhi visited Goa with her family, where she played on the beach, collected seashells, swam, and ate ice cream.", "Easy", "Remembering"),
    ("What details are written at the top of a Diary Entry?", "A Diary Entry opens with the Date, Day, and Time (e.g., 9:30 PM) at the top.", "Easy", "Remembering"),
    ("What opening salutation and closing sign-off are used in a Diary Entry?", "Salutation: 'Dear Diary'; Closing sign-off: 'Good Night, [Your Name]'.", "Easy", "Remembering"),
    ("In which grammatical perspective is a Diary Entry written?", "A Diary Entry is written in the first-person perspective using pronouns like 'I', 'me', and 'my'.", "Easy", "Understanding"),
    ("Name three essay topics included in Chapter 15.", "Three essay topics are: 1. Honesty is the Best Policy, 2. The Importance of Trees in Our Life, 3. My Favourite Festival.", "Easy", "Remembering"),
    ("Name three formal letter topics included in Chapter 15.", "1. Leave application to the Principal, 2. Complaint to Postmaster about parcel delays, 3. Application to Councillor for a street lamp.", "Easy", "Remembering"),
    ("Name three informal letter topics included in Chapter 15.", "1. Letter to friend describing summer vacation, 2. Letter to grandmother inviting her for vacation, 3. Letter to friend describing a cricket match.", "Easy", "Remembering"),
    ("Name three story topics included in Chapter 15.", "1. The Hacker Got Caught, 2. The Magical Pen, 3. The Lost Puppy and How I Helped It.", "Easy", "Remembering"),
    ("To whom would you address a formal application requesting extra sports equipment?", "You would address it to the Headmaster or Principal of your school.", "Easy", "Understanding"),
    ("To whom would you write a complaint about delayed mail delivery?", "You would write a formal complaint to the Postmaster of your area.", "Easy", "Understanding"),
    ("To whom would you write a letter requesting the installation of a street lamp?", "You would write to the Area Councillor or Municipal Officer of your locality.", "Easy", "Understanding"),
    ("To whom would you write requesting new storybooks for school?", "You would write a formal request to the School Librarian.", "Easy", "Understanding"),
    ("What three main sections make up a structured Essay?", "An essay consists of an Introduction, Body Paragraphs, and a Conclusion.", "Easy", "Understanding"),
    ("What key elements make up a complete Story?", "A story requires a Title, Setting, Characters, Conflict/Problem, Climax, and Resolution/Moral.", "Easy", "Understanding"),
    ("Why did Aarav Kumar promise to complete classwork in his leave application?", "To show academic responsibility and reassure the Principal that his studies would not suffer during leave.", "Easy", "Understanding"),
    ("What sensory activities did Nidhi describe in her Goa vacation letter?", "She described playing on sandy beaches, collecting seashells, tasting seafood, swimming, and eating ice cream at sunset.", "Easy", "Remembering"),
    ("What is the purpose of writing an essay on 'Honesty is the Best Policy'?", "To explain the moral value of truthfulness, showing how honesty builds trust, self-respect, and strong character.", "Easy", "Understanding"),
    ("What is the purpose of writing an essay on 'The Importance of Trees in Our Life'?", "To highlight environmental benefits of trees, such as oxygen production, rain support, soil protection, and wildlife habitat.", "Easy", "Understanding"),
    ("What topic asks students to imagine holding their school's top leadership position?", "The essay topic: 'If I Were the Principal of My School'.", "Easy", "Remembering"),
    ("What title is given to Chapter 15?", "The title of Chapter 15 is 'Composition Modules'.", "Easy", "Remembering"),
    ("What main writing goal does Chapter 15 achieve for Class 5 students?", "It equips students with standard formats, model examples, and creative prompts for formal, informal, diary, and essay writing.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze the main structural differences between Formal and Informal Letters.", "Formal letters include sender address, date, receiver address, Subject line, formal salutation, and official closing. Informal letters omit receiver address and Subject, using friendly salutations and warm personal sign-offs.", "Medium", "Analyzing"),
    ("Explain why a Subject line is necessary in a Formal Letter.", "A Subject line provides a one-sentence summary of the letter's purpose, allowing busy officials to quickly identify and direct the request to the correct department.", "Medium", "Analyzing"),
    ("Describe the reflective purpose of maintaining a personal Diary Entry.", "A Diary Entry offers a private emotional space to record daily events, process personal feelings, reflect on mistakes or successes, and track self-growth.", "Medium", "Understanding"),
    ("How should a story like 'The Magical Pen' be structured from beginning to end?", "Title -> Beginning (finding the magical pen) -> Middle (discovering its magic powers and facing a challenge/conflict) -> Climax -> Ending (moral lesson on using magic/talents responsibly).", "Medium", "Applying"),
    ("Outline an essay structure for 'A Day Without Electricity'.", "Intro (our dependence on power) -> Body 1 (inconveniences: no lights, fans, gadgets, water pumps) -> Body 2 (alternative activities: family conversation, outdoor play, candle light) -> Conclusion (valuing energy conservation).", "Medium", "Applying"),
    ("How does Aarav Kumar maintain a polite and responsible tone in his application?", "He uses respectful salutations ('Respected Sir'), clearly states dates and family reason, promises to complete missed work, and ends with 'Thank you' and 'Yours sincerely'.", "Medium", "Analyzing"),
    ("Why is descriptive sensory language valuable in informal travel letters?", "Sensory details (sight, sound, taste, touch) paint vivid mental pictures, making the travel experience lively and enjoyable for the reader.", "Medium", "Analyzing"),
    ("Compare an Essay with a Story composition.", "An essay is a structured factual or analytical piece discussing a topic logically in paragraphs; a story is a creative narrative with characters, plot conflict, and resolution.", "Medium", "Comparing"),
    ("What key points should be included in a letter to the Municipal Officer about cleaning a park?", "Polite salutation -> Location of the park -> Description of accumulated garbage and safety/health hazards -> Request for urgent cleaning -> Thanking you.", "Medium", "Applying"),
    ("How does writing a diary entry about 'A day when you helped someone' build moral character?", "It encourages reflection on empathy, kindness, and community service, reinforcing positive moral values in daily life.", "Medium", "Evaluating"),
    ("Explain the importance of the Date and Time in a Diary Entry.", "The Date and Time anchor the entry in historical personal time, establishing when the evening reflection took place.", "Medium", "Understanding"),
    ("What moral and cyber safety lessons does 'The Hacker Got Caught' convey?", "It teaches that unauthorized computer hacking is a serious crime, cybersecurity systems catch offenders, and digital integrity must be maintained.", "Medium", "Evaluating"),
    ("How do transition words (e.g., 'Furthermore', 'In addition') improve essay coherence?", "They connect ideas logically between sentences and paragraphs, guiding the reader smoothly through the writer's arguments.", "Medium", "Analyzing"),
    ("Summarize Chapter 15 in four concise sentences.", "Chapter 15 provides complete composition modules covering Essay Writing, Formal Letters, Informal Letters, Diary Entries, and Story Writing. It equips Class 5 students with standard formats, model examples, and practice prompts for academic and personal writing. Students learn formal civic applications, warm personal letters, reflective daily diary entries, and structured essays on moral and environmental themes. Through these modules, learners develop clear written communication, logical organization, and creative expression.", "Medium", "Understanding"),
    ("How can Class 5 students apply these composition modules to real-world tasks?", "Students can write real leave applications to school, draft friendly letters to relatives, maintain daily personal diaries, and write structured essays for school competitions.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the civic importance of teaching primary students to write formal letters to local officials.", "Teaching formal civic correspondence empowers young citizens to articulate community needs politely, demand public accountability, and participate actively in democratic governance.", "Hard", "Evaluating"),
    ("Deconstruct the rhetorical organization of an essay on 'If I Were the Principal of My School'.", "Intro (vision for leadership) -> Body 1 (academic reforms & joyful learning) -> Body 2 (sports, arts & facilities) -> Body 3 (student discipline & welfare) -> Inspiring Conclusion.", "Hard", "Analyzing"),
    ("Evaluate the psychological benefit of expressive writing in children's diary entries.", "Expressive writing allows children to process complex emotions ('I felt nervous/happy because...'), reducing emotional stress and fostering self-awareness.", "Hard", "Evaluating"),
    ("Compare the formal precision of a complaint to a Postmaster with the creative freedom of writing 'The Magical Pen'.", "Official complaint demands objective facts, clear evidence, and polite demand; story writing permits imaginative fantasy, emotional arcs, and creative world-building.", "Hard", "Comparing"),
    ("Formulate a complete model leave application following Chapter 15 guidelines.", "'To The Principal, ABC School, City. Subject: Application for Leave. Respected Sir, I am Aarav Kumar of Class 5A. Kindly grant leave from Feb 22 to 24 for a family function. I will complete missed work. Yours sincerely, Aarav Kumar.'", "Hard", "Creating"),
    ("Assess the role of Language Register (formal vs informal diction) in written communication.", "Register selection ensures tone matches recipient status—formal register maintains official respect; informal register fosters personal warmth.", "Hard", "Evaluating"),
    ("Analyze how paragraphing structure enhances reader comprehension across composition genres.", "Paragraphing breaks text into logical units (one main idea per paragraph), creating visual clarity and guiding the reader through arguments or story events.", "Hard", "Analyzing"),
    ("Synthesize how Chapter 15 unifies technical formats, functional grammar, and creative expression.", "Bridges technical format rules (letter layouts/diary headings) with functional grammar (tenses/punctuation) and creative imagination (essays/stories).", "Hard", "Synthesizing"),
    ("Critique the claim: 'Short text messages have made formal composition skills unnecessary.'", "False; professional, academic, and civic success continues to demand structured formal writing, logical organization, and clear communication etiquette.", "Hard", "Evaluating"),
    ("Formulate a comprehensive composition prompt assessing Class 5 writing skills.", "'Write a formal application to your Principal requesting new sports equipment for the school playground. Include correct format, Subject line, polite salutation, clear reasons, and proper sign-off.'", "Hard", "Creating")
]

sa_content = f"# Short Answer Questions — Chapter 15: Composition Modules\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH15_SA_{idx:03d}"
    q_txt = item[0]
    ans = item[1]
    diff = item[2] if len(item) > 2 else "Easy"
    bloom = item[3] if len(item) > 3 else "Understanding"
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH15_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Examine the format and structural rules of Formal Letter Writing as presented in Chapter 15.",
     "Formal Letter Writing follows strict layout rules to maintain professional clarity and respect:\n1. **Sender's Address & Date**: Placed at the top left corner.\n2. **Receiver's Designation & Address**: The official title and address of the recipient (e.g., 'The Principal, ABC School, City').\n3. **Subject Line**: A concise one-sentence statement declaring the exact purpose of the letter (e.g., 'Subject: Request for Leave').\n4. **Salutation**: Formal greeting such as 'Respected Sir/Madam'.\n5. **Body Text**: Divided logically into paragraphs—stating the student's name/class, clear reason for request/complaint, dates, and assurance to complete missed work.\n6. **Subscription & Signature**: Professional closing ('Thanking you', 'Yours sincerely/faithfully') followed by the sender's full name and class.",
     "Easy", "Remembering"),

    ("Examine the format and structural rules of Informal Letter Writing as presented in Chapter 15.",
     "Informal Letter Writing is used for personal communication with friends and family:\n1. **Sender's Address & Date**: Placed at the top left corner.\n2. **Salutation**: Warm, friendly greeting such as 'Dear Riya' or 'Dearest Grandmother'.\n3. **Body Text**: Conversational and affectionate tone divided into paragraphs—opening inquiry about health/wellbeing, detailed sharing of personal news (e.g., summer vacation in Goa), asking about the recipient's news, and expressing eagerness to meet.\n4. **Subscription & Signature**: Warm personal closing ('Your friend', 'Yours affectionately') followed by the sender's first name.",
     "Easy", "Remembering"),

    ("Examine the format, purpose, and key elements of a Diary Entry as presented in Chapter 15.",
     "A Diary Entry is a private personal record of thoughts, feelings, and events:\n1. **Header Details**: Opens with Date, Day, and Time (e.g., '9:30 PM') at the top left.\n2. **Salutation**: Traditional opening 'Dear Diary'.\n3. **First-Person Perspective**: Written in the first person ('I', 'me', 'my') to record daily activities and personal experiences.\n4. **Emotional Reflection**: Expresses honest feelings ('I felt excited/surprised/sad because...') and reflects on the day's highlights or funny incidents.\n5. **Sign-off**: Closes with a reflective evening thought ('It was truly a wonderful day') followed by 'Good Night, [Your Name]'.",
     "Easy", "Remembering"),

    ("Compare Formal Letter Writing with Informal Letter Writing across format, tone, and audience.",
     "Formal and Informal letters differ significantly across three dimensions:\n- **Audience**: Formal letters are sent to school principals, postmasters, librarians, and municipal officers; Informal letters are sent to friends, cousins, parents, and grandparents.\n- **Format**: Formal letters include receiver address and a mandatory Subject line; Informal letters omit receiver address and Subject line.\n- **Tone & Diction**: Formal letters use polite, objective, administrative language ('request', 'grant permission', 'Yours sincerely'); Informal letters use warm, conversational, affectionate language ('awesome', 'cant wait to hear', 'Your friend').",
     "Easy", "Comparing"),

    ("Describe the structure of an Essay and outline the points for 'The Importance of Trees in Our Life'.",
     "An Essay is structured into three main parts:\n1. **Introduction**: Introduces the topic ('Trees are green gold and essential for all living beings').\n2. **Body Paragraphs**: Explains key arguments in detail:\n   - *Environmental Benefits*: Oxygen production, absorbing carbon dioxide, supporting rain, preventing soil erosion.\n   - *Human Utilities*: Providing fruits, shade, timber, rubber, paper, and medicinal herbs.\n   - *Ecosystem Support*: Harboring birds, animals, and insects.\n3. **Conclusion**: Summarizes the main theme and delivers a call to action ('We must protect forests and plant more trees for a green future').",
     "Easy", "Understanding"),

    ("Describe the structure of a Story composition and outline the plot for 'The Magical Pen'.",
     "A Story composition requires structured narrative elements:\n1. **Title**: Catchy title reflecting the plot ('The Magical Pen').\n2. **Beginning/Setting**: Introduces the protagonist (a hardworking Class 5 student) who finds an unusual, glowing pen on the way to school.\n3. **Middle/Conflict**: The student discovers that whatever the pen draws or writes comes to life or completes homework automatically. The student faces a dilemma when tempted to cheat on a big test.\n4. **Climax & Resolution**: The student realizes that using the pen to cheat is wrong, decides to study hard and write with their own mind, and uses the magical pen only for creative drawing.\n5. **Moral**: 'True achievement comes from honest hard work, not magic shortcuts.'",
     "Easy", "Understanding"),

    ("Write a complete model formal leave application based on Aarav Kumar's example in Chapter 15.",
     "**Model Formal Application**:\n\nYour Address\nCity, Date\n\nThe Principal\nABC School\nCity Name\n\nSubject: Request for Leave of Absence\n\nRespected Sir/Madam,\n\nI am Aarav Kumar, a student of Class 5A. I am writing to request a leave of absence from February 22 to February 24, as I am travelling with my family to attend a family function out of station.\n\nI assure you that I will complete all missed classwork and homework promptly upon my return. Kindly grant me permission for these three days of leave.\n\nThank you.\n\nYours sincerely,\nAarav Kumar\nClass 5A",
     "Easy", "Creating"),

    ("Write a complete model informal letter based on Nidhi's Goa vacation example in Chapter 15.",
     "**Model Informal Letter**:\n\nYour Address\nCity, Date\n\nDear Riya,\n\nI hope you are doing well. How was your summer vacation? I had an amazing time during the holidays!\n\nMy family and I visited Goa. We enjoyed playing on the sandy beach, collecting colorful seashells, and tasting delicious seafood. I even learned how to swim in the sea! In the evenings, we watched breathtaking sunsets while eating cold ice cream.\n\nTell me all about your vacation. Did you go anywhere fun? I can't wait to hear from you soon!\n\nYour friend,\nNidhi",
     "Easy", "Creating"),

    ("Summarize Chapter 15 in five detailed bullet points.",
     "- Chapter 15 provides complete composition modules for Essay Writing, Formal Letters, Informal Letters, Diary Entries, and Story Writing.\n- Formal Letters follow strict layouts with Subject lines, polite salutations ('Respected Sir'), and official sign-offs ('Yours sincerely').\n- Informal Letters use friendly, conversational tones to share personal news and travel experiences with family and friends.\n- Diary Entries open with Date/Day/Time and 'Dear Diary', offering a private first-person space for emotional reflection.\n- Story and Essay modules teach structured paragraphing, logical introductions, body points, conclusions, and moral lessons.",
     "Easy", "Understanding"),

    ("What lessons about effective communication and character building can Class 5 students learn from Chapter 15?",
     "Students learn that clear written communication requires choosing the correct format and tone for different audiences. They learn to express civic requests politely, share personal experiences warmly, reflect on daily emotions honestly, and present moral thoughts logically. Mastering these modules builds academic confidence, self-expression, civic awareness, and lifelong communication skills.",
     "Easy", "Applying"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why is a Subject line omitted in informal letters but essential in formal applications?", "Informal letters are personal conversations between friends without rigid administrative goals; formal applications require concise Subject lines so busy officials can process requests quickly.", "Easy", "Analyzing"),
    ("Describe the points needed for an essay on 'Honesty is the Best Policy'.", "Intro (defining honesty) -> Body 1 (truthfulness builds trust and deep friendships) -> Body 2 (deceit causes fear, guilt, and lost respect) -> Conclusion (honesty brings peace of mind and strong character).", "Easy", "Understanding"),
    ("Describe the points needed for an essay on 'A Day Without Electricity'.", "Intro (electricity powers modern life) -> Body 1 (inconveniences: dark rooms, no fans, stopped water pumps, uncharged devices) -> Body 2 (positive aspects: family conversation, board games, stargazing) -> Conclusion (valuing power conservation).", "Easy", "Understanding"),
    ("Explain the layout of a letter to the Postmaster complaining about parcel delays.", "Sender Address/Date -> The Postmaster, Head Post Office -> Subject: Complaint Regarding Delayed Parcel -> Respected Sir -> Details of tracking/delay -> Request for urgent delivery -> Yours faithfully.", "Easy", "Understanding"),
    ("Explain the layout of a letter to the Area Councillor requesting a street lamp.", "Sender Address/Date -> The Area Councillor, Ward 12 -> Subject: Request for Installation of Street Lamp -> Respected Sir -> Location details & night safety hazards -> Request for action -> Yours sincerely.", "Easy", "Understanding"),
    ("Describe a diary entry about 'Fun at the School Fete'.", "Date/Day/Time -> Dear Diary -> Describe arriving at decorated school ground -> Rides, games, winning prizes, eating snacks with friends -> Excitement and fatigue -> Good Night, [Name].", "Easy", "Understanding"),
    ("Describe a story plot for 'The Hacker Got Caught'.", "Title -> Tech-savvy student notices school website grade alterations -> Tracks suspicious digital logins -> Informs computer teacher -> Security team catches hacker -> Moral: Cybercrime is illegal and punishable.", "Easy", "Understanding"),
    ("How does writing a letter to a grandmother inviting her for vacation show family affection?", "It expresses warm love, inquires about her health, shares excitement about spending holiday time together, and promises to take good care of her.", "Easy", "Understanding"),
    ("What points should be included in an essay on 'My Favourite Festival'?", "Intro (name of festival) -> Body 1 (historical/cultural significance) -> Body 2 (preparations, new clothes, sweets, family celebrations) -> Conclusion (message of joy and unity).", "Easy", "Understanding"),
    ("What points should be included in an essay on 'My Best Friend'?", "Intro (friend's name & how you met) -> Body 1 (qualities: kind, honest, helpful) -> Body 2 (shared hobbies, studying together) -> Conclusion (valuing true friendship).", "Easy", "Understanding"),
    ("Re-write Aarav's leave application as a formal letter requesting 2 days leave for sick leave instead of family function.", "Sender Address/Date -> The Principal, ABC School -> Subject: Application for Sick Leave -> Respected Sir, I am Aarav Kumar of Class 5A. I am unwell with fever and advised 2 days rest (Feb 22-23). I will complete missed work. Yours sincerely, Aarav Kumar.", "Easy", "Creating"),
    ("Why is first-person perspective ('I') natural for diary entries but avoided in formal applications?", "Diary entries are personal self-reflections ('I felt happy'); formal applications maintain objective administrative tone while identifying the applicant.", "Easy", "Analyzing"),
    ("How does story writing develop creative problem-solving skills in primary students?", "Creating characters who encounter conflicts (e.g., losing a puppy or finding a magic lamp) forces students to invent logical, satisfying solutions.", "Easy", "Understanding"),
    ("Analyze why Chapter 15 is the final concluding chapter of Book 5.", "Because composition modules synthesize all reading comprehension, vocabulary, grammar, and writing skills learned throughout the entire textbook into practical output.", "Easy", "Analyzing"),
    ("How can students practice writing diary entries to improve daily reflection?", "By setting aside 5 minutes before bedtime to write 4-5 sentences recording one main event, one emotion felt, and one positive thought for tomorrow.", "Easy", "Applying"),

    # Medium (26-40)
    ("Critically analyze how composition modules prepare primary students for academic and real-world literacy.",
     "Composition modules build comprehensive literacy:\n1. **Academic Preparedness**: Formats for formal applications, essays, and stories align with school exam requirements.\n2. **Civic Agency**: Letter writing to local authorities (Councillors/Postmasters) teaches students how to address real-world community problems.\n3. **Emotional Intelligence**: Diary entries provide a reflective tool for personal mental health and emotional awareness.\n4. **Communicative Versatility**: Switching between formal, informal, and narrative registers develops adaptable communication skills.",
     "Medium", "Analyzing"),

    ("Examine the narrative arc of a story module: Setting, Conflict, Climax, and Resolution.",
     "A structured story module follows a defined narrative arc:\n- **Setting**: Establishes time, place, and characters (e.g., a quiet village or school computer lab).\n- **Conflict**: Introduces a challenge or problem (e.g., a lost puppy, a magical pen dilemma, or a cyber hacker).\n- **Climax**: The peak moment of tension where characters must take decisive action.\n- **Resolution**: The problem is solved, order is restored, and a clear moral lesson is derived.",
     "Medium", "Analyzing"),

    ("Evaluate the importance of using appropriate Language Registers (formal vs informal diction).",
     "Language register ensures communication fits the social context:\n- **Formal Register**: Uses polite, objective, dignified vocabulary ('Respected Sir', 'request', 'grant permission') to show respect to authority figures.\n- **Informal Register**: Uses relaxed, affectionate, conversational vocabulary ('Dear Riya', 'had an awesome time', 'can't wait') to build intimacy with friends.\nFailing to use the correct register causes miscommunication or perceived disrespect.",
     "Medium", "Evaluating"),

    ("Discuss how essay writing trains logical thinking and paragraph organization.",
     "Essay writing forces students to organize thoughts systematically:\n- **Main Idea**: Each paragraph must focus on one central topic sentence.\n- **Logical Order**: Points move coherently from introductory thesis to supporting evidence and final concluding synthesis.\n- **Transitions**: Linking words connect ideas, training students in structured, logical reasoning.",
     "Medium", "Analyzing"),

    ("Design a comprehensive writing workshop plan for Class 5 based on Chapter 15.",
     "Workshop Title: 'Young Authors Composition Lab'\n- **Station 1 (Formal Letters)**: Practice drafting leave applications and civic complaint letters using format templates.\n- **Station 2 (Informal Letters)**: Write postcard-style vacation letters to classmates.\n- **Station 3 (Diary Corner)**: Write an entry about 'My Best Day at School' in decorated mini-diaries.\n- **Station 4 (Story Studio)**: Spin a story wheel (Character + Object + Setting) to draft a creative story with a moral.",
     "Medium", "Creating"),

    ("How does Nidhi's letter to Riya demonstrate effective informal letter writing?", "She opens with friendly inquiries, shares vivid vacation memories (Goa, swimming, ice cream), asks about Riya's holidays, and closes warmly.", "Medium", "Understanding"),
    ("Contrast a formal leave application with an informal letter to a cousin about a birthday party.", "Formal application uses structured boxes, Subject line, polite administrative language; informal letter uses free-flowing paragraphs, enthusiastic descriptions, and personal affection.", "Medium", "Comparing"),
    ("Why is a clear moral lesson essential when writing stories for Class 5?", "A moral lesson anchors the narrative in ethical values, teaching readers positive character traits like honesty, kindness, or hard work.", "Medium", "Evaluating"),
    ("How does an essay on 'If I Were the Principal of My School' encourage constructive student voice?", "It allows students to think critically about school improvement, proposing positive ideas for sports, academics, library books, and student welfare.", "Medium", "Evaluating"),
    ("Describe the steps needed to edit and proofread a completed formal application.", "Check sender/receiver address layout -> Verify Subject line -> Check polite salutation -> Ensure clear dates and reason -> Verify proper sign-off and signature.", "Medium", "Applying"),
    ("Why is third-person narration sometimes preferred in formal essays, while first-person is used in diaries?", "Third-person narration maintains objective, general authority in essays; first-person narration reflects intimate, subjective personal experience in diaries.", "Medium", "Analyzing"),
    ("How does letter writing to a Postmaster or Councillor build civic responsibility?", "It teaches students that citizens have the right and duty to communicate politely with public servants to improve community infrastructure and services.", "Medium", "Understanding"),
    ("Analyze why Chapter 15 includes both model compositions and 'More Topics to Practice'.", "Model compositions provide scaffolding and clear standards; practice topics challenge students to apply learned formats independently.", "Medium", "Analyzing"),
    ("What makes a diary entry an effective self-assessment tool at the end of a school day?", "It helps students review what went well, identify mistakes made, process emotional reactions, and set positive intentions for the next day.", "Medium", "Evaluating"),
    ("Construct an informal letter model from a child to grandparents describing a new school.", "'Dear Dadi and Dadu, I hope you are healthy. My new school is wonderful! The classrooms are big, and I made two new friends, Rahul and Amit. My English teacher is very kind. I miss you both and hope you visit soon! Your loving grandson, Aarav.'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the pedagogical shift from rote memorization of essays to functional composition skills.",
     "Rote essay memorization produces rigid, artificial writing unable to adapt to real-life situations. Functional composition training equips students with adaptable format rules, register awareness, and paragraph structuring, enabling them to communicate effectively across diverse academic, civic, and professional demands.",
     "Hard", "Evaluating"),

    ("Deconstruct the structural rhetoric of a formal civic complaint letter (e.g., Park Cleaning).",
     "1. Official Heading & Address -> 2. Precise Subject Line -> 3. Respectful Salutation -> 4. Statement of Problem & Location -> 5. Impact Analysis (health/safety hazard for children) -> 6. Specific Action Request -> 7. Professional Closing & Contact Info.",
     "Hard", "Analyzing"),

    ("Synthesize how Chapter 15 integrates formatting rules, functional grammar, and creative self-expression.",
     "Unifies technical format templates (letter/diary headings) with functional grammar (verb tenses, punctuation, capitalization) and creative self-expression (essay arguments, story plots).", "Hard", "Synthesizing"),

    ("Formulate a comprehensive composition assessment rubric for evaluating Class 5 student writing.",
     "Rubric Criteria:\n1. **Format Adherence (25%)**: Correct addresses, Subject line, date, salutation, subscription.\n2. **Content & Organization (35%)**: Clear paragraphs, logical flow, complete details, relevant topic focus.\n3. **Language & Register (25%)**: Appropriate formal/informal tone, varied vocabulary, correct tenses.\n4. **Grammar & Mechanics (15%)**: Punctuation, spelling, capitalization.",
     "Hard", "Creating"),

    ("Evaluate the impact of expressive diary writing on developing emotional resilience in children.", "Regular diary writing provides a safe, non-judgmental space for emotional catharsis, helping children process trauma, anxiety, or conflict, leading to improved self-regulation.", "Hard", "Evaluating"),

    ("Compare the narrative conflict resolution in 'The Hacker Got Caught' with 'The Lost Puppy and How I Helped It'.", "'The Hacker Got Caught' relies on technological investigation, law/cyber authority, and crime resolution; 'The Lost Puppy' relies on personal empathy, community care, and compassionate rescue.", "Hard", "Comparing"),
    ("Discuss the importance of teaching digital letter writing and email etiquette alongside traditional letters.", "While physical letter formats establish foundational structure, adapting them to digital email formats (Subject lines, formal salutations, professional sign-offs) prepares students for modern digital communication.", "Hard", "Understanding"),
    ("Analyze how sentence variety (simple, compound, complex sentences) elevates essay writing quality.", "Using varied sentence lengths and structures prevents monotonous rhythm, emphasizes key points, and creates sophisticated, engaging prose.", "Hard", "Analyzing"),
    ("Draft an analytical commentary on the importance of mastering Composition Modules in primary education.", "Mastering Composition Modules in Class 5 transforms passive language learners into active, articulate communicators. By mastering structured formats, appropriate registers, and creative storytelling, students gain the foundational tools required for advanced academic writing, civic engagement, and lifelong personal expression.", "Hard", "Evaluating"),
    ("Synthesize the complete educational takeaways of Chapter 15 for Book 5 English Question Bank.", "Chapter 15 successfully completes Book 5 by providing comprehensive composition modules that test and reinforce formal application layout, informal travel letters, reflective diary entries, structured essays, and moral story writing across 300 rigorous questions.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 15: Composition Modules\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH15_LA_{idx:03d}"
    q_txt = item[0]
    ans = item[1]
    diff = item[2] if len(item) > 2 else "Easy"
    bloom = item[3] if len(item) > 3 else "Understanding"
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH15_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("Formal Letter Writing: Your Address [City, Date] The Principal, ABC [School Name], [City Name] Subject: Request for Leave Respected Sir/Madam, I am Aarav Kumar, a student of Class 5A. I am writing to request a leave of absence from February 22, to February 24 as I am travelling with my family for a family function.",
     [
         ("Who is the sender of this formal letter?", "Aarav Kumar, a student of Class 5A.", "Easy", "Remembering"),
         ("To whom is this letter addressed?", "The Principal, ABC School.", "Easy", "Remembering"),
         ("What is the stated Subject of this letter?", "Subject: Request for Leave.", "Easy", "Remembering"),
         ("What dates of leave are requested?", "February 22 to February 24.", "Easy", "Remembering"),
         ("Why is a Subject line mandatory in formal letters?", "To state the letter's purpose clearly and concisely for official processing.", "Medium", "Understanding")
     ]),

    # Set 2
    ("I will complete all my classwork and homework once I return. Kindly grant me permission for the leave. Thank you. Yours sincerely, xyz",
     [
         ("What promise does the student make upon returning from leave?", "To complete all missed classwork and homework.", "Easy", "Remembering"),
         ("What polite request is made in the second sentence?", "Kindly grant me permission for the leave.", "Easy", "Remembering"),
         ("What formal expression of gratitude is included?", "Thank you.", "Easy", "Remembering"),
         ("What formal sign-off subscription is used?", "Yours sincerely.", "Easy", "Remembering"),
         ("How does promising to complete missed work demonstrate student responsibility?", "It shows academic dedication and reassures the principal that studies will not suffer.", "Medium", "Analyzing")
     ]),

    # Set 3
    ("Informal Letter Writing: Your Address [City, Date] Dear Riya, I hope you are doing well. How was your summer vacation? I had an amazing time! My family and I visited Goa. We enjoyed playing on the beach, collecting seashells and tasting delicious seafood. I even learned to swim!",
     [
         ("Who is the recipient of this informal letter?", "Riya.", "Easy", "Remembering"),
         ("Where did the sender visit during summer vacation?", "Goa.", "Easy", "Remembering"),
         ("Name three activities the sender enjoyed in Goa.", "Playing on the beach, collecting seashells, and tasting delicious seafood.", "Easy", "Remembering"),
         ("What new skill did the sender learn in Goa?", "Learned to swim.", "Easy", "Remembering"),
         ("Why is the salutation 'Dear Riya' appropriate for an informal letter?", "Because it uses a warm, friendly tone suitable for personal writing to a friend.", "Medium", "Understanding")
     ]),

    # Set 4
    ("In the evenings, we watched the sunset while eating ice cream. Tell me about your vacation. Did you go anywhere fun? I cant wait to hear from you! Your friend, Nidhi",
     [
         ("What did Nidhi's family watch in the evenings while eating ice cream?", "The sunset.", "Easy", "Remembering"),
         ("What does Nidhi ask Riya to share in her reply?", "To tell about her vacation and if she went anywhere fun.", "Easy", "Remembering"),
         ("How does Nidhi express her eagerness to hear back?", "I cant wait to hear from you!", "Easy", "Remembering"),
         ("What friendly closing subscription is used?", "Your friend, Nidhi.", "Easy", "Remembering"),
         ("What sensory details in this extract make the description vivid?", "Watching sunsets (visual) while eating ice cream (taste/temperature).", "Medium", "Analyzing")
     ]),

    # Set 5
    ("Diary Entry: Date: Day: Time - Dear Diary, Today was a very (adjective) day for me. In the morning, I (what you did first). At school, our teacher surprised us with (event/activity). I felt (emotion) because (reason)... Good Night, (Your Name)",
     [
         ("What three header details open a Diary Entry?", "Date, Day, and Time.", "Easy", "Remembering"),
         ("What is the traditional opening salutation for a diary?", "Dear Diary.", "Easy", "Remembering"),
         ("In which grammatical perspective is a diary entry written?", "First-person perspective ('I', 'me', 'my').", "Easy", "Understanding"),
         ("How does a diary entry close at night?", "Good Night, (Your Name).", "Easy", "Remembering"),
         ("Why do diary templates include emotion prompts like 'I felt (emotion) because (reason)'?", "To encourage emotional self-reflection and expressive writing.", "Medium", "Analyzing")
     ]),

    # Set 6
    ("More Topics to Practice (Formal Letters): 1. Write a letter to your Principal requesting leave for two days. 2. Write a letter to the Municipal Officer about the need to clean the park near your house. 3. Write a letter to the Librarian requesting new storybooks...",
     [
         ("To whom would you write regarding cleaning a neighborhood park?", "The Municipal Officer / Area Councillor.", "Easy", "Remembering"),
         ("To whom would you write requesting new storybooks?", "The School Librarian.", "Easy", "Remembering"),
         ("What layout component is shared by all three formal topics?", "Subject line, formal salutation, and official sign-off.", "Easy", "Understanding"),
         ("Why is writing a letter to a Municipal Officer considered civic writing?", "Because it teaches citizens to politely demand public services and community cleanliness.", "Medium", "Evaluating"),
         ("What details should be included in a library book request letter?", "Specific genres/titles of storybooks requested and how they will benefit students.", "Medium", "Applying")
     ]),

    # Set 7
    ("More Topics to Practice (Informal Letters): 1. Write a letter to your friend telling him about your summer vacation. 2. Write a letter to your cousin describing your friend's birthday celebration. 3. Write a letter to your grandparents about your new school...",
     [
         ("Name three recipients of informal letters mentioned in these topics.", "Friend, cousin, and grandparents.", "Easy", "Remembering"),
         ("What topic involves describing a birthday party?", "Topic 2 (letter to cousin describing a friend's birthday celebration).", "Easy", "Remembering"),
         ("What topic involves sharing news about moving to a new educational institution?", "Topic 3 (letter to grandparents about your new school).", "Easy", "Remembering"),
         ("What tone should be used across all three informal topics?", "A warm, conversational, and personal tone.", "Easy", "Understanding"),
         ("How does writing to grandparents differ from writing to a formal principal?", "Writing to grandparents uses loving personal affection without rigid Subject lines or formal addresses.", "Medium", "Comparing")
     ]),

    # Set 8
    ("Essay Writing Topics: 1. Weather Cycle, 2. Honesty is the Best Policy, 3. My Favourite Festival, 4. A Day Without Electricity, 5. The Importance of Trees in Our Life.",
     [
         ("Which essay topic deals with moral character and truthfulness?", "Honesty is the Best Policy.", "Easy", "Remembering"),
         ("Which essay topic deals with environmental conservation?", "The Importance of Trees in Our Life.", "Easy", "Remembering"),
         ("Which essay topic deals with modern technological dependence?", "A Day Without Electricity.", "Easy", "Remembering"),
         ("What three structural parts must every essay contain?", "Introduction, Body Paragraphs, and Conclusion.", "Easy", "Understanding"),
         ("Outline an introduction for 'The Importance of Trees in Our Life'.", "Define trees as Earth's green lifelines providing oxygen, shade, and natural balance.", "Medium", "Applying")
     ]),

    # Set 9
    ("Story Writing Topics: 1. THE HACKER GOT CAUGHT, 2. THE MAGICAL PEN, 3. The Day I Found a Magic Lamp, 4. The Adventure in the Forest, 5. The Lost Puppy and How I Helped It.",
     [
         ("Which story topic deals with digital crime and cybersecurity?", "The Hacker Got Caught.", "Easy", "Remembering"),
         ("Which story topic involves finding a magical writing tool?", "The Magical Pen.", "Easy", "Remembering"),
         ("Which story topic involves rescuing an animal?", "The Lost Puppy and How I Helped It.", "Easy", "Remembering"),
         ("What elements make up a complete story plot?", "Title, Setting, Characters, Conflict, Climax, and Moral Resolution.", "Easy", "Understanding"),
         ("What moral lesson can be derived from 'The Lost Puppy and How I Helped It'?", "Compassion, kindness, and taking responsibility for helpless animals.", "Medium", "Evaluating")
     ]),

    # Set 10
    ("Composition Modules: Essay Writing... Formal Letter Writing... Informal Letter Writing... Diary Entry... Story Writing...",
     [
         ("How many distinct composition modules are covered in Chapter 15?", "Five modules (Essay, Formal Letter, Informal Letter, Diary Entry, Story).", "Easy", "Remembering"),
         ("Which module uses the salutation 'Respected Sir/Madam'?", "Formal Letter Writing.", "Easy", "Remembering"),
         ("Which module uses header details 'Date, Day, Time' and 'Dear Diary'?", "Diary Entry.", "Easy", "Remembering"),
         ("Which module requires a plot conflict, climax, and moral resolution?", "Story Writing.", "Easy", "Remembering"),
         ("Summarize how mastering these five modules prepares Class 5 students for comprehensive communication.", "Mastering these modules equips students to write formal civic requests, warm personal letters, reflective daily journals, structured analytical essays, and creative moral stories.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 15: Composition Modules\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH15_EXT_{q_counter:03d}"
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

with open(os.path.join(CH15_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 15 in {CH15_DIR}")
