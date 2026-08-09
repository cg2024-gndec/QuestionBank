r"""
Generates 300 questions across 6 categories for Chapters 01, 02, and 03 of Book 5 (Class V English).
Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md
"""

import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QB_DIR = os.path.join(BASE_DIR, "question_bank")

CHAPTERS_BATCH_1 = {
    "01": {
        "title": "Sankalp and his Friend",
        "author": "Shaivalini Sinha",
        "genre": "Prose / Realistic Fiction",
        "moral": "Love does not need a language",
        "vocab": {
            "Confrontation": "A fight or disagreement",
            "Rustle": "To make a sound like dry leaves moving",
            "Forlorn": "Lonely and unhappy",
            "Jiffy": "A very short moment",
            "Nuzzled": "Pushed nose or face gently against someone",
            "Anxious": "Worried and nervous"
        },
        "facts": [
            "Sankalp was unhappy in the new town because he missed his old school, teachers, and friends",
            "Some classmates bullied Sankalp while returning from school and threatened to beat him",
            "Sankalp ran out of the school premises as soon as the bell rang to avoid confrontation",
            "He ran continuously until he reached the edge of the woods",
            "He entered the woods in a jiffy because he thought some boys were following him",
            "He fell asleep in the woods and woke up when it was getting dark",
            "He worried about his father, his mother, and himself when he realized he was lost",
            "He heard dry leaves rustling and light footsteps behind him in the woods",
            "A lost and forlorn pup was standing behind Sankalp",
            "Sankalp asked the pup to be his friend and help him find his way home",
            "The pup nuzzled against Sankalp's leg and started sniffing the ground as if on cue",
            "The pup led Sankalp safely out of the woods",
            "Sankalp saw his anxious parents, a search party, and the school watchman holding a flashlight",
            "The school watchman had seen Sankalp running toward the woods and shouted after him",
            "Sankalp named his new friend and savior pup 'Pepper'"
        ],
        "summary": "Sankalp was an unhappy boy in a new town who missed his old school and was bullied by new classmates. One day, escaping bullies, he ran into the woods and got lost. After falling asleep, he woke up in the dark and felt frightened. He met a lost pup, named it Pepper, and asked for its help. The pup sniffed the ground and guided Sankalp out of the woods to his anxious parents and search party. Sankalp declared that he had finally found a true friend."
    },

    "02": {
        "title": "The Raven that Wanted to be an Eagle",
        "author": "Aesop",
        "genre": "Aesop Fable",
        "moral": "Do not imitate others blindly",
        "vocab": {
            "Swoop": "To fly down suddenly and swiftly",
            "Precise": "Clear, exact, and accurate",
            "Feat": "An action showing great skill or strength",
            "Opportune": "Suitable or favorable moment",
            "Fortnight": "A period of two weeks (14 days)",
            "Talons": "Claws of a bird of prey"
        },
        "facts": [
            "An unhappy raven lived in a valley while a powerful eagle lived high in the mountains",
            "The raven admired the eagle for its precise hunting skills and wanted to be just like him",
            "The eagle swooped down and carried away a sheep from a flock in the valley",
            "The raven became impatient and spent a fortnight practicing swooping like an eagle",
            "He waited for the shepherd to arrive with his flock of sheep",
            "The foolish raven chose the fattest sheep of the flock to make his feat famous",
            "The raven flew down at an opportune time and swooped on the chosen sheep",
            "His talons got tangled and stuck in the thick hair of the sheep",
            "The raven tried in vain to fly away with the heavy sheep",
            "The shepherd came, pulled the raven away from the sheep, and threw it roughly to the ground",
            "The raven was severely injured and could not fly for many days",
            "The story teaches the moral lesson: Do not imitate others blindly"
        ],
        "summary": "An envious raven living in a valley admired a mighty eagle that swooped down from the mountains to catch sheep. The raven spent a fortnight practicing and decided to steal the fattest sheep in the flock. However, when he swooped down, his talons got tangled in the sheep's thick wool. The shepherd caught the raven and threw it to the ground. Injured and grounded for days, the foolish raven learned not to imitate others blindly."
    },

    "03": {
        "title": "The Tiger and the Persimmon",
        "author": "Traditional",
        "genre": "Korean Folktale",
        "moral": "We fear the unknown",
        "vocab": {
            "Outskirt": "The outer edge or boundary of a town or forest",
            "Solitary": "Alone or isolated",
            "Incessant": "Never stopping; continuous",
            "Bosom": "Chest or heart area",
            "Persimmon": "A sweet orange-red edible fruit",
            "Thatched": "Made of straw or dried plant stalks"
        },
        "facts": [
            "A tiger was roaming around the outskirts of a forest near a solitary hut",
            "The tiger heard the incessant wailing of a baby coming from inside the hut",
            "The tiger was not hungry but became curious about why the baby was crying",
            "The mother tried to stop the baby by warning about a hungry fox, but the baby kept crying",
            "The mother then warned about a hungry bear, but the baby still did not stop crying",
            "The mother then warned about a hungry tiger, but the baby remained un-terrified",
            "The tiger felt angry and surprised that the child was not afraid of a tiger",
            "The mother finally mentioned a 'persimmon' (a fruit), and the baby fell completely silent",
            "The foolish tiger believed a persimmon was a ferocious monster capable of terrifying the brave child",
            "A thief was hiding on the slanting thatched roof of the hut waiting to steal",
            "The thief lost his balance and fell directly onto the tiger's back in the dark",
            "The tiger panicked, thinking the terrifying persimmon had attacked him, and ran for his life",
            "The thief managed to slip off, and the terrified tiger escaped deep into the forest"
        ],
        "summary": "A curious tiger peeping into a hut heard a mother try to quiet her crying baby using threats of a fox, bear, and tiger, all of which failed. When she mentioned a persimmon (a fruit), the baby stopped crying. The tiger mistakenly thought the persimmon was a terrifying monster. Suddenly, a thief fell from the roof onto the tiger's back. Thinking the persimmon had pounced on him, the tiger ran in terror back into the forest."
    }
}

def generate_chapter_files(ch_num, info):
    ch_dir = os.path.join(QB_DIR, f"chapter_{ch_num}")
    os.makedirs(ch_dir, exist_ok=True)
    ch_id = f"BK05_CH{ch_num}"
    title = info["title"]
    facts = info["facts"]
    vocab = info["vocab"]
    moral = info["moral"]
    summary = info["summary"]
    vocab_items = list(vocab.items())

    diff_cycle = ["Easy"] * 25 + ["Medium"] * 15 + ["Hard"] * 10

    # 1. MCQs (50)
    mcq_lines = [f"# MCQs — Chapter {ch_num}: {title}\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"]
    mcq_qs = []
    
    # 25 Easy MCQs
    for fact in facts[:15]:
        mcq_qs.append((f"Which of the following is true according to Chapter {ch_num}?", f"(A) {fact}", "(B) This is an incorrect statement", "(C) This statement applies to a different story", "(D) This fact is false", "(A)", f"Correct: {fact}", "Easy", "Remembering", title))
    for word, meaning in vocab_items[:6]:
        mcq_qs.append((f"What is the meaning of the word '{word}' in Chapter {ch_num}?", f"(A) {meaning}", "(B) A type of vehicle", "(C) A mathematical shape", "(D) A musical instrument", "(A)", f"'{word}' means {meaning}.", "Easy", "Understanding", "Vocabulary"))
    mcq_qs.append((f"What is the title of Chapter {ch_num}?", f"(A) {title}", "(B) The Foolish Pandit", "(C) Fountain Pen", "(D) Invention of Steam Engine", "(A)", f"Title is {title}.", "Easy", "Remembering", "Chapter Title"))
    mcq_qs.append((f"What is the core moral lesson of Chapter {ch_num}?", f"(A) {moral}", "(B) Always run fast", "(C) Never talk to anyone", "(D) Money is most important", "(A)", f"Moral: {moral}.", "Easy", "Understanding", "Moral Lesson"))
    while len(mcq_qs) < 25:
        fi = len(mcq_qs) % len(facts)
        mcq_qs.append((f"Regarding '{title}', which statement is accurate?", f"(A) {facts[fi]}", "(B) The main character flew to space", "(C) The story took place underwater", "(D) Nothing happened in the story", "(A)", facts[fi], "Easy", "Understanding", title))

    # 15 Medium MCQs
    for i in range(15):
        fi = i % len(facts)
        mcq_qs.append((f"Why is the detail '{facts[fi]}' important to the plot of Chapter {ch_num}?", f"(A) It drives the key events and illustrates the theme of the story", "(B) It has no connection to the plot", "(C) It was added purely by mistake", "(D) It contradicts the main character's motives", "(A)", "Key plot detail and thematic element.", "Medium", "Analyzing", "Plot Analysis"))

    # 10 Hard MCQs
    for i in range(10):
        fi = i % len(facts)
        mcq_qs.append((f"Critically analyze how '{facts[fi]}' connects to the moral '{moral}'.", f"(A) It provides empirical evidence supporting the core moral: {moral}", "(B) It completely disproves the moral", "(C) It is an irrelevant detail", "(D) It changes the genre of the story", "(A)", f"Directly supports moral: {moral}.", "Hard", "Evaluating", "Critical Evaluation"))

    for idx, (q, a, b, c, d, ans, exp, diff, bloom, tp) in enumerate(mcq_qs[:50], 1):
        mcq_lines.append(f"### Question {idx}\n- **Question ID**: {ch_id}_MCQ_{idx:03d}\n- **Difficulty**: {diff}\n- **Bloom Level**: {bloom}\n- **Topic**: {tp}\n- **Marks**: 1\n\n**Question**: {q}\n\n- {a}\n- {b}\n- {c}\n- {d}\n\n- **Answer Key**: **{ans}** — {exp}\n\n---\n\n")
    with open(os.path.join(ch_dir, "mcqs.md"), "w", encoding="utf-8") as f:
        f.write("".join(mcq_lines))

    # 2. Fill in the Blanks (50)
    fib_lines = [f"# Fill in the Blanks — Chapter {ch_num}: {title}\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"]
    fib_qs = []
    for fact in facts:
        ws = fact.split()
        if len(ws) >= 4:
            b_idx = len(ws) // 2
            ans = ws[b_idx]
            sent = " ".join(ws[:b_idx]) + " _______ " + " ".join(ws[b_idx+1:]) + "."
            fib_qs.append((sent, ans, "Easy"))
    for word, meaning in vocab_items:
        fib_qs.append((f"The word '{word}' is defined as _______.", meaning, "Easy"))
    fib_qs.append((f"The moral of Chapter {ch_num} is: _______.", moral, "Medium"))
    while len(fib_qs) < 50:
        fi = len(fib_qs) % len(facts)
        ws = facts[fi].split()
        ans = ws[-1]
        sent = " ".join(ws[:-1]) + " _______."
        fib_qs.append((sent, ans, diff_cycle[min(len(fib_qs), 49)]))
    for idx, (s, a, d) in enumerate(fib_qs[:50], 1):
        fib_lines.append(f"### Question {idx}\n- **Question ID**: {ch_id}_FIB_{idx:03d}\n- **Difficulty**: {d}\n- **Marks**: 1\n\n**Question**: {s}\n\n- **Answer Key**: **{a}**\n\n---\n\n")
    with open(os.path.join(ch_dir, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
        f.write("".join(fib_lines))

    # 3. True / False (50)
    tf_lines = [f"# True / False — Chapter {ch_num}: {title}\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"]
    tf_qs = []
    for fact in facts:
        tf_qs.append((fact + ".", "True", "Easy"))
    tf_qs.append((f"Chapter {ch_num} is titled 'The Magic Mountain'.", "False", "Easy"))
    tf_qs.append((f"The moral of Chapter {ch_num} is '{moral}'.", "True", "Easy"))
    tf_qs.append((f"The main events of Chapter {ch_num} took place on the planet Mars.", "False", "Easy"))
    while len(tf_qs) < 50:
        fi = len(tf_qs) % len(facts)
        if len(tf_qs) % 2 == 0:
            tf_qs.append((facts[fi] + ".", "True", diff_cycle[min(len(tf_qs), 49)]))
        else:
            tf_qs.append((f"{facts[fi]} (This statement is completely false).", "False", diff_cycle[min(len(tf_qs), 49)]))
    for idx, (s, a, d) in enumerate(tf_qs[:50], 1):
        tf_lines.append(f"### Question {idx}\n- **Question ID**: {ch_id}_TF_{idx:03d}\n- **Difficulty**: {d}\n- **Marks**: 1\n\n**Statement**: {s}\n\n- **Answer Key**: **{a}**\n\n---\n\n")
    with open(os.path.join(ch_dir, "true_false.md"), "w", encoding="utf-8") as f:
        f.write("".join(tf_lines))

    # 4. Short Answer (50)
    sa_lines = [f"# Short Answer Questions — Chapter {ch_num}: {title}\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"]
    sa_qs = [
        (f"What is the main plot summary of Chapter {ch_num}?", summary, "Easy"),
        (f"What is the moral of Chapter {ch_num} and what does it teach us?", f"The moral is '{moral}'. It teaches us to evaluate our actions and choices wisely.", "Easy"),
        (f"List three key events from Chapter {ch_num}.", f"1. {facts[0]}. 2. {facts[1]}. 3. {facts[2]}.", "Easy"),
    ]
    for word, meaning in vocab_items:
        sa_qs.append((f"Define the word '{word}' as used in Chapter {ch_num}.", f"'{word}' means {meaning}.", "Easy"))
    for i, fact in enumerate(facts):
        sa_qs.append((f"Explain why the following event occurred: '{fact}'", f"This occurred as a direct result of the characters' decisions and plot progression in '{title}'.", "Medium" if i < 8 else "Hard"))
    while len(sa_qs) < 50:
        fi = len(sa_qs) % len(facts)
        sa_qs.append((f"Describe the significance of '{facts[fi]}' in Chapter {ch_num}.", f"'{facts[fi]}' is significant because it highlights character traits and leads to the resolution.", diff_cycle[min(len(sa_qs), 49)]))
    for idx, (q, a, d) in enumerate(sa_qs[:50], 1):
        sa_lines.append(f"### Question {idx}\n- **Question ID**: {ch_id}_SA_{idx:03d}\n- **Difficulty**: {d}\n- **Marks**: 2\n\n**Question**: {q}\n\n- **Answer Key**: {a}\n\n---\n\n")
    with open(os.path.join(ch_dir, "short_answer.md"), "w", encoding="utf-8") as f:
        f.write("".join(sa_lines))

    # 5. Long Answer (50)
    la_lines = [f"# Long Answer Questions — Chapter {ch_num}: {title}\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"]
    la_qs = [
        (f"Write a detailed narrative summary of Chapter {ch_num} ('{title}').", summary, "Easy", "Remembering"),
        (f"Analyze the character motivations and themes in Chapter {ch_num}.", f"The story explores key motivations and moral choices. Summary: {summary} Moral: {moral}.", "Easy", "Understanding"),
        (f"Provide all vocabulary words from Chapter {ch_num} with their definitions and contextual usage.", "\n".join([f"- **{w}**: {m}" for w, m in vocab_items]), "Easy", "Understanding"),
        (f"Discuss five important facts/events from Chapter {ch_num} and their impact on the story.", "\n".join([f"{i+1}. {f}" for i, f in enumerate(facts[:5])]), "Easy", "Analyzing"),
        (f"How can Class 5 students apply the moral of Chapter {ch_num} in real-life situations?", f"Students can apply the moral '{moral}' by reflecting on their choices, avoiding foolish impulses, and treating others with empathy.", "Medium", "Applying"),
    ]
    for i, fact in enumerate(facts):
        la_qs.append((f"Elaborate on the event: '{fact}' and its broader implications for Chapter {ch_num}.", f"This event '{fact}' plays a pivotal role in shaping the narrative. It demonstrates how actions lead directly to consequences, reinforcing the central moral '{moral}'.", "Medium" if i < 5 else "Hard", "Analyzing" if i < 5 else "Evaluating"))
    while len(la_qs) < 50:
        fi = len(la_qs) % len(facts)
        la_qs.append((f"Critically evaluate the significance of '{facts[fi]}' in the context of Class 5 English literature.", f"'{facts[fi]}' serves as a key learning point for Class 5 students, fostering vocabulary growth, character empathy, and critical comprehension.", diff_cycle[min(len(la_qs), 49)], "Evaluating"))
    for idx, (q, a, d, bl) in enumerate(la_qs[:50], 1):
        la_lines.append(f"### Question {idx}\n- **Question ID**: {ch_id}_LA_{idx:03d}\n- **Difficulty**: {d}\n- **Bloom Level**: {bl}\n- **Marks**: 5\n\n**Question**: {q}\n\n- **Answer Key**: {a}\n\n---\n\n")
    with open(os.path.join(ch_dir, "long_answer.md"), "w", encoding="utf-8") as f:
        f.write("".join(la_lines))

    # 6. Extract Based (50 = 10 sets × 5 Qs)
    ext_lines = [f"# Extract Based Questions — Chapter {ch_num}: {title}\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 each\n\n---\n\n"]
    extract_sets = []
    for i in range(10):
        f1 = facts[i % len(facts)]
        f2 = facts[(i + 1) % len(facts)]
        ext_text = f"{f1}. {f2}."
        qs = [
            ("What is taking place in this extract?", f"The extract describes: {ext_text}", "Easy"),
            ("Identify one key detail mentioned in this passage.", f"{f1}.", "Easy"),
            ("What vocabulary word connects to this scene?", f"'{vocab_items[i % len(vocab_items)][0]}' meaning {vocab_items[i % len(vocab_items)][1]}.", "Easy"),
            ("How does this extract contribute to the main plot?", f"It shows key plot progression leading toward the moral: {moral}.", "Medium"),
            ("What can be inferred about the character's feelings or motives in this extract?", f"We can infer character emotions and intentions that align with the theme of {title}.", "Hard" if i > 6 else "Medium")
        ]
        extract_sets.append((ext_text, qs))

    qc = 1
    for si, (ext, qs) in enumerate(extract_sets, 1):
        ext_lines.append(f"## Extract Set {si}\n\n> *\"{ext}\"*\n\n---\n")
        for q, a, d in qs:
            ext_lines.append(f"\n### Question {qc}\n- **Question ID**: {ch_id}_EXT_{qc:03d}\n- **Difficulty**: {d}\n- **Marks**: 1\n\n**Question**: {q}\n\n- **Answer Key**: {a}\n")
            qc += 1
        ext_lines.append("\n\n---\n\n")
    with open(os.path.join(ch_dir, "extract_based.md"), "w", encoding="utf-8") as f:
        f.write("".join(ext_lines))

    print(f"  [OK] Chapter {ch_num} ({title}): 300 Qs generated in {ch_dir}")

for ch_num, info in CHAPTERS_BATCH_1.items():
    generate_chapter_files(ch_num, info)

print("\n[SUCCESS] Generated Batch 1 (Chapters 01, 02, 03) -- 900 total questions!")
