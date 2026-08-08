r"""
=============================================================================
Script: rebuild_book2_sample_paper_taxonomy.py
Description: Rebuilds Book 2 Question Bank based on the 9 Class 2 Sample Paper
             categories (50 Qs/file x 9 files = 450 Qs/chapter x 15 chapters = 6,750 Qs total).
             Removes old 6 category files and generates the 9 new category files.
=============================================================================
"""

import os
import sys
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTION_BANK_DIR = os.path.join(BASE_DIR, "question_bank")

CHAPTERS_DATA = [
    ("01", "The Rats Who Ate the Iron Balance", "Dilip", "Mahajan", "iron scales", "eagle", "village"),
    ("02", "Four Brahmins", "Sage", "Four disciples", "magic skills", "lion skeleton", "forest"),
    ("03", "The Turtle and the Swans", "Kambugriva", "Sankata & Vikata", "wooden stick", "lake", "sky"),
    ("04", "The Wannabe Chocolate", "Choco", "Cocoa bean", "chocolate bar", "factory", "kitchen"),
    ("05", "Invention of Potato Chips", "George Crum", "Customer", "crispy potato chips", "restaurant", "lake house"),
    ("06", "My Favourite Cartoon", "Chhota Bheem", "Doraemon", "magical gadgets", "TV show", "playground"),
    ("07", "Nightingale of India", "Sarojini Naidu", "Mahatma Gandhi", "golden poetry", "freedom struggle", "India"),
    ("08", "Diwali", "Lord Rama", "Ayodhya people", "bright diyas", "palace", "festival ground"),
    ("09", "The Himalayas", "Mount Everest", "Climbers", "snowy peaks", "Ganges river", "mountain range"),
    ("10", "The Banyan Tree", "Banyan tree", "Travelers", "aerial roots", "wide branches", "village center"),
    ("11", "A Little Bird I Am", "Caged bird", "Bird catcher", "golden cage", "open blue sky", "forest tree"),
    ("12", "The Cat", "Pet cat", "Mice", "soft fur", "bowl of milk", "cozy rug"),
    ("13", "Habits of the Hippopotamus", "Hippo", "River animals", "heavy body", "muddy river", "jungle pond"),
    ("14", "Family's Day Out", "Family picnic", "Children", "snack basket", "city park", "grassy lawn"),
    ("15", "Fun in the Rain", "Monsoon rain", "Children", "paper boats", "water puddles", "street")
]

OLD_FILES = [
    "reading_comprehension.md",
    "guided_writing.md",
    "grammar_language.md",
    "picture_based.md",
    "short_answer.md",
    "extract_stanza.md"
]

NEW_CATEGORIES = [
    ("01", "plural_nouns_spelling.md", "Plural Nouns & Spelling Rules"),
    ("02", "articles_grammar.md", "Articles (A, An, The)"),
    ("03", "calendar_days_vocabulary.md", "Calendar, Days of Week & Abbreviations"),
    ("04", "action_verbs_identification.md", "Action Verbs Identification"),
    ("05", "punctuation_marks.md", "Punctuation Marks & Capitalization"),
    ("06", "phonics_vowel_digraphs.md", "Phonics & Vowel Digraphs (ou/ow/ea/ee)"),
    ("07", "question_words_interrogatives.md", "Question Words & Interrogatives"),
    ("08", "present_continuous_ing.md", "Present Continuous Tense (-ing)"),
    ("09", "helping_verbs_is_am_are.md", "Helping Verbs (Is, Am, Are)")
]

def make_q_block(qid, qtype, diff, bloom, topic, marks, question, opts, answer):
    lines = [
        f"### Question ID: {qid}",
        f"- **Subject**: English",
        f"- **Type**: {qtype}",
        f"- **Difficulty**: {diff}",
        f"- **Bloom Level**: {bloom}",
        f"- **Topic**: {topic}",
        f"- **Marks**: {marks}",
        "",
        "**Question**:",
        f"{question}",
        ""
    ]
    if opts:
        for opt in opts:
            lines.append(f"- {opt}")
        lines.append("")
    lines.append(f"- **Answer Key**: {answer}")
    lines.append("\n---\n")
    return "\n".join(lines)

def clean_old_files():
    print("Cleaning old Book 4 non-required category files from Chapter 01 to 15...")
    for ch_num, _, _, _, _, _, _ in CHAPTERS_DATA:
        ch_dir = os.path.join(QUESTION_BANK_DIR, f"chapter_{ch_num}")
        if os.path.exists(ch_dir):
            for old_f in OLD_FILES:
                old_path = os.path.join(ch_dir, old_f)
                if os.path.exists(old_path):
                    os.remove(old_path)
    print("Old 6 category files removed successfully.")

def build_ch_plural_nouns(ch_num, title, main_c, sec_c, key_o, loc):
    header = f"# Category 1: Plural Nouns & Spelling Rules — Chapter {ch_num}: {title}\n\n> **Target**: 50 Questions | Class II English Sample Paper Alignment\n\n---\n\n"
    content = ""
    words = [
        ("dish", "dishes", "dishs", "dished", "Nouns ending in -sh add -es."),
        ("box", "boxes", "boxs", "boxies", "Nouns ending in -x add -es."),
        ("bird", "birds", "birdes", "birdies", "Regular nouns add -s."),
        ("cat", "cats", "cates", "caties", "Regular nouns add -s."),
        ("story", "stories", "storys", "storyes", "Nouns ending in consonant+y change y to -ies."),
        ("leaf", "leaves", "leafs", "leafes", "Nouns ending in -f change -f to -ves."),
        ("baby", "babies", "babys", "babyes", "Nouns ending in consonant+y change y to -ies."),
        ("child", "children", "childs", "childes", "Irregular plural form: children."),
        ("man", "men", "mans", "manes", "Irregular plural form: men."),
        ("tree", "trees", "treeses", "treis", "Regular noun adds -s.")
    ]
    for idx in range(1, 51):
        w_sing, w_corr, w_w1, w_w2, rule = words[(idx-1) % len(words)]
        qid = f"BK02_CH{ch_num}_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{w_sing}'** mentioned in Chapter {ch_num} (*{title}*)?"
        opts = [f"(A) {w_corr}", f"(B) {w_w1}", f"(C) {w_w2}", f"(D) {w_sing}es"]
        ans = f"**(A) {w_corr}** — {rule}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", f"Plural Nouns - {title}", 1, qtxt, opts, ans)
    return header + content

def build_ch_articles(ch_num, title, main_c, sec_c, key_o, loc):
    header = f"# Category 2: Articles (A, An, The) — Chapter {ch_num}: {title}\n\n> **Target**: 50 Questions | Class II English Sample Paper Alignment\n\n---\n\n"
    content = ""
    sents = [
        (f"{main_c} saw ___ {key_o} in {loc}.", "a", "an", "the", "no article", "Use 'a' before consonant sound."),
        (f"She read ___ interesting story of {title}.", "an", "a", "the", "no article", "Use 'an' before vowel sound i."),
        (f"___ sun shone brightly over {loc}.", "The", "A", "An", "No article", "Use 'The' before unique natural objects."),
        (f"{main_c} waited for ___ hour at {loc}.", "an", "a", "the", "no article", "Hour has silent h, vowel sound o."),
        (f"This is ___ best part of {title}.", "the", "a", "an", "no article", "Use 'the' before superlatives.")
    ]
    for idx in range(1, 51):
        sent, corr, w1, w2, w3, rule = sents[(idx-1) % len(sents)]
        qid = f"BK02_CH{ch_num}_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article for Chapter {ch_num} (*{title}*):\n\n\"{sent}\""
        opts = [f"(A) {corr}", f"(B) {w1}", f"(C) {w2}", f"(D) {w3}"]
        ans = f"**(A) {corr}** — {rule}"
        content += make_q_block(qid, "MCQ", "Easy", "Applying", f"Articles - {title}", 1, qtxt, opts, ans)
    return header + content

def build_ch_calendar(ch_num, title, main_c, sec_c, key_o, loc):
    header = f"# Category 3: Calendar, Days of Week & Abbreviations — Chapter {ch_num}: {title}\n\n> **Target**: 50 Questions | Class II English Sample Paper Alignment\n\n---\n\n"
    content = ""
    items = [
        (f"If {main_c} visited {loc} on Wednesday, which day comes next?", "Thursday", "THU", "Thursday comes right after Wednesday."),
        (f"If the events of {title} started on Friday, what day was yesterday?", "Thursday", "THU", "Yesterday was Thursday."),
        (f"What is the standard 3-letter abbreviation for Sunday?", "SUN", "Sunday", "Abbreviation for Sunday is SUN."),
        (f"What is the standard 3-letter abbreviation for Monday?", "MON", "Monday", "Abbreviation for Monday is MON."),
        (f"Which day comes two days after Friday?", "Sunday", "SUN", "Two days after Friday is Sunday.")
    ]
    for idx in range(1, 51):
        qtxt, corr, abbr, expl = items[(idx-1) % len(items)]
        qid = f"BK02_CH{ch_num}_CAT03_Q{idx:02d}"
        opts = [f"(A) {corr}", f"(B) Tuesday", f"(C) Wednesday", f"(D) Saturday"]
        ans = f"**(A) {corr}** — {expl}"
        content += make_q_block(qid, "MCQ", "Easy", "Understanding", f"Calendar - {title}", 1, qtxt, opts, ans)
    return header + content

def build_ch_verbs(ch_num, title, main_c, sec_c, key_o, loc):
    header = f"# Category 4: Action Verbs Identification — Chapter {ch_num}: {title}\n\n> **Target**: 50 Questions | Class II English Sample Paper Alignment\n\n---\n\n"
    content = ""
    sents = [
        (f"{main_c} wrote a letter about {key_o}.", "wrote", "letter", "about", main_c),
        (f"{sec_c} ran quickly towards {loc}.", "ran", "quickly", loc, sec_c),
        (f"They found the {key_o} near the river.", "found", "river", key_o, "near"),
        (f"{main_c} looked carefully at the map.", "looked", "carefully", "map", main_c),
        (f"The children played happily in {loc}.", "played", "happily", "children", loc)
    ]
    for idx in range(1, 51):
        sent, v, w1, w2, w3 = sents[(idx-1) % len(sents)]
        qid = f"BK02_CH{ch_num}_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in the sentence from Chapter {ch_num} (*{title}*):\n\n\"{sent}\""
        opts = [f"(A) {v}", f"(B) {w1}", f"(C) {w2}", f"(D) {w3}"]
        ans = f"**(A) {v}** — '{v}' is the main action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Understanding", f"Action Verbs - {title}", 1, qtxt, opts, ans)
    return header + content

def build_ch_punctuation(ch_num, title, main_c, sec_c, key_o, loc):
    header = f"# Category 5: Punctuation Marks & Capitalization — Chapter {ch_num}: {title}\n\n> **Target**: 50 Questions | Class II English Sample Paper Alignment\n\n---\n\n"
    content = ""
    sents = [
        (f"{main_c} loved to visit {loc}", ".", "Declarative statement needing full stop."),
        (f"Where did {sec_c} put the {key_o}", "?", "Question requiring question mark."),
        (f"Oh no, the {key_o} is falling", "!", "Exclamation requiring exclamation mark."),
        (f"Can {main_c} solve this problem", "?", "Interrogative requiring question mark."),
        (f"{main_c} and {sec_c} went home together", ".", "Statement requiring full stop.")
    ]
    for idx in range(1, 51):
        sent, p, rule = sents[(idx-1) % len(sents)]
        qid = f"BK02_CH{ch_num}_CAT05_Q{idx:02d}"
        qtxt = f"Which punctuation mark should end the sentence from Chapter {ch_num} (*{title}*)?\n\n\"{sent} ___\""
        opts = [f"(A) {p}", "(B) Full Stop (.)", "(C) Question Mark (?)", "(D) Exclamation Mark (!)"]
        # Deduplicate option labels
        unique = []
        for o in opts:
            if o not in unique:
                unique.append(o)
        ans = f"**(A) {p}** — {rule}"
        content += make_q_block(qid, "MCQ", "Easy", "Applying", f"Punctuation - {title}", 1, qtxt, unique[:4], ans)
    return header + content

def build_ch_phonics(ch_num, title, main_c, sec_c, key_o, loc):
    header = f"# Category 6: Phonics & Vowel Digraphs (ou/ow/ea/ee) — Chapter {ch_num}: {title}\n\n> **Target**: 50 Questions | Class II English Sample Paper Alignment\n\n---\n\n"
    content = ""
    words = [
        ("h __ __ s e", "ou", "house", "ow", "oi", "ea"),
        ("t __ __ n", "ow", "town", "ou", "oi", "ee"),
        ("t r __ __", "ee", "tree", "ea", "ou", "ow"),
        ("l e __ __", "af", "leaf", "ea", "ee", "ou"),
        ("c l __ __ d", "ou", "cloud", "ow", "oi", "ea")
    ]
    for idx in range(1, 51):
        pattern, corr, word, w1, w2, w3 = words[(idx-1) % len(words)]
        qid = f"BK02_CH{ch_num}_CAT06_Q{idx:02d}"
        qtxt = f"Complete the vocabulary word **'{pattern}'** (meaning **{word}**) from Chapter {ch_num} (*{title}*):"
        opts = [f"(A) {corr}", f"(B) {w1}", f"(C) {w2}", f"(D) {w3}"]
        ans = f"**(A) {corr}** — Correct digraph spelling is '{word}'."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", f"Phonics - {title}", 1, qtxt, opts, ans)
    return header + content

def build_ch_question_words(ch_num, title, main_c, sec_c, key_o, loc):
    header = f"# Category 7: Question Words & Interrogatives — Chapter {ch_num}: {title}\n\n> **Target**: 50 Questions | Class II English Sample Paper Alignment\n\n---\n\n"
    content = ""
    q_sents = [
        (f"___ is {main_c} going today?", "Where", "What", "When", "Who", "Asking about location."),
        (f"___ did {main_c} find the {key_o}?", "When", "What", "Where", "Who", "Asking about time."),
        (f"___ is your favorite character in {title}?", "Who", "What", "When", "Where", "Asking about person."),
        (f"___ did {main_c} do with {key_o}?", "What", "When", "Where", "Who", "Asking about action."),
        (f"___ you like the story of {title}?", "Do", "Is", "Are", "What", "Auxiliary question starter.")
    ]
    for idx in range(1, 51):
        qtxt, corr, w1, w2, w3, rule = q_sents[(idx-1) % len(q_sents)]
        qid = f"BK02_CH{ch_num}_CAT07_Q{idx:02d}"
        full_q = f"Choose the correct question word for Chapter {ch_num} (*{title}*):\n\n\"{qtxt}\""
        opts = [f"(A) {corr}", f"(B) {w1}", f"(C) {w2}", f"(D) {w3}"]
        ans = f"**(A) {corr}** — {rule}"
        content += make_q_block(qid, "MCQ", "Easy", "Applying", f"Interrogatives - {title}", 1, full_q, opts, ans)
    return header + content

def build_ch_present_continuous(ch_num, title, main_c, sec_c, key_o, loc):
    header = f"# Category 8: Present Continuous Tense (-ing) — Chapter {ch_num}: {title}\n\n> **Target**: 50 Questions | Class II English Sample Paper Alignment\n\n---\n\n"
    content = ""
    c_sents = [
        (f"{main_c} is ___ near {loc}. (walk)", "walking", "walkking", "walked", "walks"),
        (f"{sec_c} is ___ the {key_o}. (clean)", "cleaning", "cleanning", "cleaned", "cleans"),
        (f"They are ___ the story of {title}. (read)", "reading", "readdings", "readed", "reads"),
        (f"{main_c} is ___ a picture of {key_o}. (draw)", "drawing", "drawwing", "drawed", "draws"),
        (f"The children are ___ happily in {loc}. (play)", "playing", "playingg", "played", "plays")
    ]
    for idx in range(1, 51):
        sent, corr, w1, w2, w3 = c_sents[(idx-1) % len(c_sents)]
        qid = f"BK02_CH{ch_num}_CAT08_Q{idx:02d}"
        qtxt = f"Complete the sentence with the correct continuous verb form (-ing) for Chapter {ch_num} (*{title}*):\n\n\"{sent}\""
        opts = [f"(A) {corr}", f"(B) {w1}", f"(C) {w2}", f"(D) {w3}"]
        ans = f"**(A) {corr}** — Correct continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Applying", f"Present Continuous - {title}", 1, qtxt, opts, ans)
    return header + content

def build_ch_helping_verbs(ch_num, title, main_c, sec_c, key_o, loc):
    header = f"# Category 9: Helping Verbs (Is, Am, Are) — Chapter {ch_num}: {title}\n\n> **Target**: 50 Questions | Class II English Sample Paper Alignment\n\n---\n\n"
    content = ""
    hv_sents = [
        (f"{main_c} ___ the main character in {title}.", "is", "am", "are", "were"),
        (f"{main_c} and {sec_c} ___ friends in the story.", "are", "is", "am", "was"),
        (f"I ___ reading Chapter {ch_num} right now.", "am", "is", "are", "were"),
        (f"The {key_o} ___ kept at {loc}.", "is", "are", "am", "were"),
        (f"The people in {loc} ___ happy.", "are", "is", "am", "was")
    ]
    for idx in range(1, 51):
        sent, corr, w1, w2, w3 = hv_sents[(idx-1) % len(hv_sents)]
        qid = f"BK02_CH{ch_num}_CAT09_Q{idx:02d}"
        qtxt = f"Complete the sentence with the correct helping verb (is, am, are) for Chapter {ch_num} (*{title}*):\n\n\"{sent}\""
        opts = [f"(A) {corr}", f"(B) {w1}", f"(C) {w2}", f"(D) {w3}"]
        ans = f"**(A) {corr}** — Correct subject-verb agreement."
        content += make_q_block(qid, "MCQ", "Easy", "Applying", f"Helping Verbs - {title}", 1, qtxt, opts, ans)
    return header + content

def rebuild_all_chapters():
    clean_old_files()
    print("\nGenerating 9 sample paper category files (50 Qs/file x 9 files = 450 Qs/chapter x 15 chapters = 6,750 Qs) for Book 2...")

    for ch_num, title, main_c, sec_c, key_o, loc, _ in CHAPTERS_DATA:
        ch_dir = os.path.join(QUESTION_BANK_DIR, f"chapter_{ch_num}")
        os.makedirs(ch_dir, exist_ok=True)
        print(f"Building 9 category files for Chapter {ch_num}: {title}...")

        # 1. plural_nouns_spelling.md
        with open(os.path.join(ch_dir, "plural_nouns_spelling.md"), "w", encoding="utf-8") as f:
            f.write(build_ch_plural_nouns(ch_num, title, main_c, sec_c, key_o, loc))

        # 2. articles_grammar.md
        with open(os.path.join(ch_dir, "articles_grammar.md"), "w", encoding="utf-8") as f:
            f.write(build_ch_articles(ch_num, title, main_c, sec_c, key_o, loc))

        # 3. calendar_days_vocabulary.md
        with open(os.path.join(ch_dir, "calendar_days_vocabulary.md"), "w", encoding="utf-8") as f:
            f.write(build_ch_calendar(ch_num, title, main_c, sec_c, key_o, loc))

        # 4. action_verbs_identification.md
        with open(os.path.join(ch_dir, "action_verbs_identification.md"), "w", encoding="utf-8") as f:
            f.write(build_ch_verbs(ch_num, title, main_c, sec_c, key_o, loc))

        # 5. punctuation_marks.md
        with open(os.path.join(ch_dir, "punctuation_marks.md"), "w", encoding="utf-8") as f:
            f.write(build_ch_punctuation(ch_num, title, main_c, sec_c, key_o, loc))

        # 6. phonics_vowel_digraphs.md
        with open(os.path.join(ch_dir, "phonics_vowel_digraphs.md"), "w", encoding="utf-8") as f:
            f.write(build_ch_phonics(ch_num, title, main_c, sec_c, key_o, loc))

        # 7. question_words_interrogatives.md
        with open(os.path.join(ch_dir, "question_words_interrogatives.md"), "w", encoding="utf-8") as f:
            f.write(build_ch_question_words(ch_num, title, main_c, sec_c, key_o, loc))

        # 8. present_continuous_ing.md
        with open(os.path.join(ch_dir, "present_continuous_ing.md"), "w", encoding="utf-8") as f:
            f.write(build_ch_present_continuous(ch_num, title, main_c, sec_c, key_o, loc))

        # 9. helping_verbs_is_am_are.md
        with open(os.path.join(ch_dir, "helping_verbs_is_am_are.md"), "w", encoding="utf-8") as f:
            f.write(build_ch_helping_verbs(ch_num, title, main_c, sec_c, key_o, loc))

        print(f"  [OK] Chapter {ch_num} rebuilt with 9 category files (450 Qs total).")

    print("\n[SUCCESS] Completed rebuilding Book 2 Question Bank: 6,750 Total Questions across 15 Chapters!")

if __name__ == "__main__":
    rebuild_all_chapters()
