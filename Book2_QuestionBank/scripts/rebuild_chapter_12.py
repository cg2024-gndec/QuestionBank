r"""
=============================================================================
Script: rebuild_chapter_12.py
Description: Generates 50 rich, non-duplicate, multi-tiered (Easy, Medium, Hard)
             questions for each of the 9 category files in Chapter 12:
             "The Cat" (450 Qs total).
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH12_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_12")
os.makedirs(CH12_DIR, exist_ok=True)

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

# ---------------------------------------------------------------------------
# 1. Plural Nouns & Spelling Rules (50 Qs)
# ---------------------------------------------------------------------------
def build_plural_nouns():
    header = "# Category 1: Plural Nouns & Spelling Rules — Chapter 12: The Cat\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("mouse", "mice", "mouses", "mices", "mousies", "A", "Irregular plural: mouse becomes mice."),
        ("cat", "cats", "cates", "caties", "catz", "A", "Regular noun adding -s."),
        ("kitty", "kitties", "kittys", "kittyes", "kittiz", "A", "Consonant + y changes to -ies."),
        ("house", "houses", "housies", "housees", "housez", "A", "Regular noun ending in -e adds -s."),
        ("wife", "wives", "wifes", "wifees", "wivies", "A", "Nouns ending in -fe change to -ves."),
        ("spouse", "spouses", "spousies", "spousees", "spousez", "A", "Regular noun ending in -e adds -s."),
        ("cot", "cots", "cotes", "coties", "cotz", "A", "Regular noun adding -s."),
        ("word", "words", "wordes", "wordies", "wordz", "A", "Regular noun adding -s."),
        ("night", "nights", "nightes", "nighties", "nightz", "A", "Regular noun adding -s."),
        ("day", "days", "daies", "dayes", "dayz", "A", "Vowel + y adds -s."),
        ("pet", "pets", "petes", "peties", "petz", "A", "Regular noun adding -s."),
        ("home", "homes", "homies", "homees", "homez", "A", "Regular noun ending in -e adds -s."),
        ("wish", "wishes", "wishs", "wishies", "wished", "A", "Nouns ending in -sh add -es."),
        ("box", "boxes", "boxs", "boxies", "boxen", "A", "Nouns ending in -x add -es."),
        ("child", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("person", "people", "persons", "peoples", "persones", "A", "Irregular plural: person becomes people."),
        ("foot", "feet", "foots", "feets", "footies", "A", "Irregular plural: foot becomes feet."),
        ("tooth", "teeth", "tooths", "teeths", "toothies", "A", "Irregular plural: tooth becomes teeth.")
    ]
    
    for idx, (word, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH12_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{word}'** from or related to Chapter 12 (*The Cat*)?"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Plural Noun Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("You get some words regarding (mouse / mice).", "mice", "mouse", "mouses", "mices", "A", "Irregular plural of mouse is 'mice'."),
        ("The owner bought two playful (kitty / kitties).", "kitties", "kitty", "kittys", "kittyes", "A", "Consonant + y changes to -ies (kitties)."),
        ("The two (wife / wives) discussed getting a pet.", "wives", "wife", "wifes", "wifees", "A", "Nouns ending in -fe change to -ves (wives)."),
        ("Identify the INCORRECT plural spelling in this list: cats, houses, mouses, cots.", "mouses", "cats", "houses", "cots", "A", "Plural of mouse is 'mice', not 'mouses'."),
        ("Choose the sentence with the correct plural noun form:", "The house had two mice and three cats.", "The house had two mouses and three cates.", "The house had two mices and three caties.", "The house had two mousies and three catz.", "A", "mice (irregular) and cats (-s) are correct."),
        ("Which noun forms its plural by changing -fe to -ves?", "wife -> wives", "house -> houses", "cat -> cats", "kitty -> kitties", "A", "Wife ends in -fe, so plural is wives."),
        ("Change the singular noun in brackets to plural: 'The cat chased two ____ (mouse) across the room.'", "mice", "mouses", "mices", "mousies", "A", "Irregular plural: mouse becomes mice."),
        ("Select the sentence where ALL plural nouns are spelt correctly:", "The spouses bought kitties for their houses.", "The spousies bought kittys for their housees.", "The spousees bought kitties for their housez.", "The spousz bought kitties for their houses.", "A", "spouses, kitties, houses are all correctly spelt plurals."),
        ("What is the correct plural of 'playful kitty'?", "playful kitties", "playful kittys", "playful kittyes", "playful kittiz", "A", "Consonant + y changes to -ies."),
        ("They spent many restless (night / nights) listening to the cat.", "nights", "nightes", "nighties", "nightz", "A", "Regular noun adding -s (nights)."),
        ("Many (cat / cats) make noise at two a.m.", "cats", "cat", "cates", "caties", "A", "Plural of cat is cats."),
        ("Many (person / people) prefer quiet pets.", "people", "persons", "peoples", "persones", "A", "Irregular plural of person is people."),
        ("How many (house / houses) did they visit?", "houses", "house", "housies", "housees", "A", "Regular noun ending in -e adds -s (houses)."),
        ("The room had two wooden (cot / cots).", "cots", "cot", "cotes", "coties", "A", "Regular noun adding -s (cots)."),
        ("Which plural noun rule applies to the word **'wives'**?", "Change -fe to -ves", "Add -s to vowel + y", "Add -es to -ch", "Change -y to -ies", "A", "Wife ends in -fe, changing to -ves."),
        ("The owner heard many quiet (word / words) from his spouse.", "words", "wordes", "wordies", "wordz", "A", "Plural of word is words."),
        ("Identify the correct plural form of 'child':", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("They saw two quiet (mouse / mice) in the kitchen.", "mice", "mouse", "mouses", "mices", "A", "Irregular plural of mouse is mice.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH12_CAT01_Q{idx:02d}"
        qtxt = f"Contextual Plural Rule Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Plural Noun Application", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Rewrite the sentence in PLURAL form: 'The wife saw a mouse in the house.'", "The wives saw mice in the houses.", "The wifes saw mouses in the housees.", "The wives saw mices in the houses.", "The wivies saw mousies in the cagies.", "A", "Plural of wife->wives (-fe->-ves), mouse->mice (irregular), house->houses."),
        ("Analyze the error: 'He got some words regarding mouses.' Why is 'mouses' inappropriate here?", "'mouse' has an irregular plural form 'mice', not 'mouses'.", "'mouses' should be 'mices'.", "'words' should be 'wordes'.", "No error.", "A", "Mouse becomes mice in plural."),
        ("Complete the paragraph with correct plurals: 'The two ____ (wife) bought three ____ (kitty) to catch four ____ (mouse).'", "wives, kitties, mice", "wifes, kittys, mouses", "wivies, kitties, mices", "wives, kittyes, mouses", "A", "wives (-fe -> -ves), kitties (-y -> -ies), mice (irregular)."),
        ("Identify the sentence where ALL three underlined nouns are correctly pluralized:", "The **spouses** kept **kitties** to chase **mice**.", "The **spousies** kept **kittys** to chase **mouses**.", "The **spousees** kept **kitties** to chase **mices**.", "The **spousz** kept **kitties** to chase **mousies**.", "A", "spouses (-e+s), kitties (-y->-ies), mice (irregular)."),
        ("Which group contains ONLY irregular plural nouns?", "children, people, mice, feet", "cats, houses, cots, words", "kitties, wives, cities, countries", "leaves, thieves, wolves, knives", "A", "children, people, mice, feet change forms without standard -s/-es."),
        ("Why does 'kitty' become 'kitties' but 'day' becomes 'days'?", "Because 'kitty' has a consonant before y (t+y -> -ies), while 'day' has a vowel before y (a+y -> -s).", "Because 'kitty' is short and 'day' is long.", "Because 'kitty' is an animal and 'day' is time.", "Both follow the exact same rule.", "A", "Consonant+y changes y to -ies; Vowel+y adds -s."),
        ("Find the TWO grammatical mistakes in: 'The two wifes saw two mouses in the kitchen.'", "'wifes' should be 'wives' and 'mouses' should be 'mice'.", "'wifes' should be 'wife' and 'mouses' should be 'mices'.", "'kitchen' should be 'kitchens' only.", "There are no mistakes in the sentence.", "A", "wives (-fe -> -ves) and mice (irregular plural)."),
        ("Replace the singular words in brackets: 'The cats flapped their ____ (foot) and sharpened their ____ (tooth).'", "feet, teeth", "foots, tooths", "feets, teeths", "foots, toothies", "A", "Plural of foot is feet, plural of tooth is teeth."),
        ("Analyze this sentence: 'You get some words regarding mice.' Can 'words' be singularized as 'word' in this idiom?", "'words' in 'get words regarding' means speech/advice; singular 'a word' can mean a short message.", "No, 'words' can never be singular.", "Yes, 'a words' is correct.", "No, it becomes 'wordss'.", "A", "'word' can mean message/speech."),
        ("Fill in the blanks: 'The two ____ (child) watched three ____ (kitty) playing.'", "children, kitties", "childs, kittys", "childrens, kittyes", "childes, kitties", "A", "child -> children; kitty -> kitties."),
        ("Select the option that shows correct plural transformation for ALL three words: 'wife', 'kitty', 'mouse'", "wives, kitties, mice", "wifes, kittys, mouses", "wives, kittyes, mices", "wifes, kitties, mousees", "A", "wife -> wives; kitty -> kitties; mouse -> mice."),
        ("HOTS Reasoning: Why do we say 'the mouse is silent' (singular) vs 'mice are silent' (plural)?", "Because singular noun 'mouse' takes singular verb 'is', while irregular plural 'mice' takes plural verb 'are'.", "Because mouse is small.", "Because cat is loud.", "Because spouse spoke.", "A", "Subject-verb agreement: singular mouse is vs plural mice are."),
        ("Transform into singular: 'The wives bought kitties for their houses.'", "The wife bought a kitty for her house.", "The wives bought a kitty for her house.", "The wife buy a kitty for her house.", "The wife bought kitties for her house.", "A", "Singular forms: wife, kitty, house."),
        ("Identify the correct rule for forming the plural of **'mouse'**:", "Irregular plural noun changing internal vowel (mouse -> mice).", "Add -s (mouses).", "Add -es (mousees).", "Change -e to -ves (mouves).", "A", "Irregular plural noun changing internal vowel.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH12_CAT01_Q{idx:02d}"
        qtxt = f"Higher Order Thinking Skills (HOTS) & Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Plural & Spelling Analysis", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 2. Articles Grammar (50 Qs)
# ---------------------------------------------------------------------------
def build_articles_grammar():
    header = "# Category 2: Articles (A, An, The) — Chapter 12: The Cat\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("You get ___ wife, you get a house.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'wife'."),
        ("You get ___ house in the city.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'house'."),
        ("Eventually, you get ___ mouse.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'mouse'."),
        ("You get ___ kitty in a trice.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'kitty'."),
        ("___ mouse is in, the cat is out.", "The", "A", "An", "No article", "A", "Definite article 'The' specifies the mouse in the poem."),
        ("___ Panchatantra/Humorous poem tells a story about a cat.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'Panchatantra/Humorous'."),
        ("___ cat is noisy at two a.m.", "The", "A", "An", "No article", "A", "Definite article 'The' specifies the cat in the poem."),
        ("It dawns upon you in ___ cot.", "your / a", "an", "the", "no article", "A", "Possessive pronoun 'your' or article 'a cot' (consonant sound)."),
        ("The owner hears ___ noisy meow in the night.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'noisy'."),
        ("It was ___ unusual situation at night.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'unusual'."),
        ("The spouse wanted ___ quiet night.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'quiet'."),
        ("It was ___ honest mistake to get a cat.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' sound in 'honest'."),
        ("___ mouse is silent, the cat is not.", "The", "A", "An", "No article", "A", "Use 'The' for specific mouse."),
        ("You should have got another ___ mouse.", "no article", "a", "an", "the", "A", "'another' takes no extra article ('another mouse')."),
        ("They created ___ peaceful bedroom with a cot.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'peaceful'."),
        ("It was ___ early hour when the cat meowed.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'early'."),
        ("The poem brings ___ humor to daily life.", "no article", "a", "an", "the", "A", "Abstract noun 'humor' takes no indefinite article here."),
        ("___ moon shone brightly at two a.m.", "The", "A", "An", "No article", "A", "Use 'The' for unique celestial object 'moon'.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH12_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article (a / an / the / no article):\n\n\"{q_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Basic Article Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("You get ___ wife, you get ___ house.", "a, a", "an, a", "a, an", "the, a", "A", "'a wife' (consonant sound), 'a house' (consonant sound)."),
        ("Why do we say '**a** mouse' but '**an** early hour'?", "Because 'mouse' begins with a consonant sound (m) and 'early' with a vowel sound (e).", "Because mice are small.", "Because cats are noisy.", "Because houses are big.", "A", "Article selection depends on initial vowel/consonant sound."),
        ("Select the sentence with CORRECT article usage:", "You get a kitty in a trice.", "You get an kitty in an trice.", "You get the a kitty in trice.", "You get a kitty in an trice.", "A", "'a kitty' (consonant sound), 'a trice' (consonant sound)."),
        ("Fill in the blanks: '___ mouse is in, ___ cat is out.'", "The, the", "A, a", "An, an", "A, the", "A", "'The mouse' (specific mouse), 'the cat' (specific cat)."),
        ("Identify the INCORRECT article in: 'He bought **a** electric cat toy.'", "'a' should be 'an'", "'a' should be 'the'", "'electric' should be 'a electric'", "No mistake", "A", "'electric' starts with vowel sound /e/, so it takes 'an'."),
        ("Which article completes the sentence? 'The cat made ___ annoying sound at night.'", "an", "a", "the", "no article", "A", "'annoying' starts with vowel sound /a/, requiring 'an'."),
        ("Choose the correct pair of articles: '___ spouse lay in ___ cot.'", "The, the", "A, a", "An, an", "The, a", "A", "'The spouse' (specific spouse), 'the cot' (specific bed cot)."),
        ("Why do we use 'an' before 'early hour' in 'At **an** early hour, the cat meowed'?", "Because 'early' begins with the vowel sound /er/.", "Because hour is a noun.", "Because cat is out.", "Because mouse is silent.", "A", "'early' starts with vowel sound /er/."),
        ("Complete the dialogue: Husband: 'Should we get ___ cat?' Wife: 'No, get ___ mouse!'", "a, a", "a, an", "an, the", "the, the", "A", "'a cat' (consonant sound), 'a mouse' (consonant sound)."),
        ("Select the correct sentence:", "A mouse is a quiet pet.", "An mouse is a quiet pet.", "The mouse is an quiet pet.", "An mouse is an quiet pet.", "A", "'A mouse' (consonant sound), 'a quiet pet' (consonant sound)."),
        ("Fill in the blank: 'The cat remained noisy for ___ long time.'", "a", "an", "the", "no article", "A", "Idiomatic phrase 'for a long time'."),
        ("Identify where NO article is needed:", "The poem contains **___ humor** and ironies.", "He bought ___ cat.", "She saw ___ mouse.", "They built ___ house.", "A", "Abstract noun 'humor' takes no indefinite article here."),
        ("Choose the correct sentence for poem summary:", "Silence and peace are valued at night.", "A silence and a peace are valued.", "An silence and an peace are valued.", "The silence a is valued.", "A", "Abstract concepts take no indefinite articles in general moral sense."),
        ("Fill in the blanks: 'The husband spent ___ hour looking for ___ silent pet.'", "an, a", "a, a", "an, an", "the, an", "A", "'an hour' (silent h), 'a silent pet' (consonant s)."),
        ("Which sentence uses 'the' correctly for specific poem characters?", "The mouse is in, the cat is out.", "A mouse is in, a cat is out.", "An mouse is in, an cat is out.", "Mouse is in, cat is out.", "A", "Specific poem characters take 'the mouse' and 'the cat'."),
        ("Identify the article error: 'He gave **a** explanation of **an** short poem.'", "'an short' should be 'a short' and 'a explanation' should be 'an explanation'", "'a explanation' should be 'an explanation'", "'an short' should be 'a short'", "No error", "A", "'an explanation' (vowel /e/) and 'a short poem' (consonant /s/)."),
        ("Complete: 'It was ___ unexpected event at ___ two a.m.'", "an, no article", "a, an", "the, the", "an, a", "A", "an unexpected (/u/), two a.m. (time expression, no article)."),
        ("Choose the correct option: '___ sun woke them after the noisy night.'", "The", "A", "An", "No article", "A", "'The sun' (unique celestial body).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH12_CAT02_Q{idx:02d}"
        qtxt = f"Contextual Article Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Article Usage in Context", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze article usage in: 'You should have got **a** another mouse.' Correct the error:", "'a another' -> 'another' ('another' already includes the indefinite article 'an' + 'other').", "'another' -> 'an another'.", "'mouse' -> 'mouses'.", "No error.", "A", "'another' cannot be preceded by 'a'."),
        ("Fill in all three blanks: '___ mouse was in ___ house while ___ cat was outside.'", "The, the, the", "A, a, a", "An, a, the", "The, a, a", "A", "'The mouse' (specific), 'the house' (specific), 'the cat' (specific)."),
        ("Identify why 'the' is used in: 'By two a.m., **the** mouse is in, **the** cat is out.'", "Because 'the' specifies the particular mouse and cat in the speaker's household.", "Because cat is a noun.", "Because mouse is silent.", "Because cot is small.", "A", "'the' specifies definite household animals in narrative."),
        ("Spot the TWO article errors: 'It took **a** hour to catch **a** escaped mouse.'", "'a hour' should be 'an hour' and 'a escaped' should be 'an escaped'.", "'a hour' should be 'the hour' and 'a escaped' should be 'a escaped'.", "No errors.", "Only 'a hour' is wrong.", "A", "Both 'hour' (silent h) and 'escaped' (vowel e) require 'an'."),
        ("Choose the paragraph with PERFECT article usage throughout:", "A man bought a house. He got a mouse and a kitty. The cat was noisy at night.", "An man bought an house. He got an mouse.", "The man bought a house. A cat was noisy.", "A man bought a house. The kitty was an honest.", "A", "A man (consonant), a house (consonant), a mouse (consonant), a kitty (consonant), The cat (second mention)."),
        ("Why is it correct to write 'a unique pet' but 'an unusual pet'?", "Because 'unique' begins with consonant sound /j/ (yoo), while 'unusual' begins with vowel sound /u/.", "Because unique is longer.", "Because pet is noun.", "Both take 'an'.", "A", "Sound determines article: /yoo/ is a consonant sound."),
        ("Select the option that correctly completes the poem moral: '___ noisy cat disturbs ___ sleep of ___ weary owner.'", "A, the, a", "An, a, an", "The, the, the", "A, a, a", "A", "A noisy cat, the sleep (specific sleep), a weary owner."),
        ("Analyze this sentence: 'They got words regarding **the** mice.' Why is 'the' appropriate?", "Because 'the' specifies the particular mice disturbing the household.", "Because mice is plural.", "Because house is big.", "Because spouse is awake.", "A", "'the' specifies definite mice in context."),
        ("Correct the sentence: 'An kitty meowed in a quiet house at a early hour.'", "A kitty meowed in a quiet house at an early hour.", "The kitty meowed in an quiet house at a early hour.", "An kitty meowed in the quiet house at an early hour.", "A kitty meowed in a quiet house at a early hour.", "A", "'A kitty' (/k/ sound), 'a quiet' (consonant /q/), 'an early' (vowel /er/)."),
        ("Fill in the blanks: '___ words of ___ spouse made ___ owner reflect.'", "The, the, the", "A, a, a", "No article, a, an", "An, the, a", "A", "'The words' (specific), 'the spouse' (specific), 'the owner' (specific)."),
        ("Spot the missing article: 'Man got mouse and cat in house.'", "Missing 'A' before 'Man', 'a' before 'mouse', 'a' before 'cat', 'a' before 'house' -> 'A man got a mouse...'", "Missing 'an' before 'house'", "Missing 'the' before 'got'", "No article is missing", "A", "Singular countable nouns require articles."),
        ("HOTS Reasoning: Which sentence uses 'a', 'an', and 'the' correctly in a single rule demonstration?", "An hour ago, a cat jumped onto the roof.", "A hour ago, an cat jumped onto a roof.", "The hour ago, an cat jumped onto an roof.", "An hour ago, an cat jumped onto the roof.", "A", "An hour (silent h), a cat (consonant), the roof (specific)."),
        ("Rewrite correctly: 'The spouse gave a honest opinion about an noisy kitty.'", "The spouse gave an honest opinion about a noisy kitty.", "The spouse gave a honest opinion about a noisy kitty.", "The spouse gave an honest opinion about an noisy kitty.", "The spouse gave the honest opinion about an noisy kitty.", "A", "'an honest' (silent h), 'a noisy kitty' (consonant /n/)."),
        ("Identify the correct rule for using articles with time expressions like 'two a.m.' or 'midnight':", "Specific numerical times (two a.m., 3 o'clock, midnight) take no indefinite article before them.", "Times take 'an'.", "Times take 'a'.", "Times take 'the' always.", "A", "Numerical times take no article.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH12_CAT02_Q{idx:02d}"
        qtxt = f"Higher Order Article Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Article Analysis & Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 3. Calendar & Days Vocabulary (50 Qs)
# ---------------------------------------------------------------------------
def build_calendar_days():
    header = "# Category 3: Calendar, Days & Abbreviations — Chapter 12: The Cat\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    days_easy = [
        ("The poem mentions **'two a.m.'**. What does **a.m.** stand for?", "Ante Meridiem (before noon / morning time)", "After Morning", "At Midnight", "All Month", "A", "a.m. stands for ante meridiem (before noon)."),
        ("What does **p.m.** stand for?", "Post Meridiem (after noon / evening time)", "Past Morning", "Plus Minute", "Post Month", "A", "p.m. stands for post meridiem (after noon)."),
        ("What time of day is **2:00 a.m.**?", "Late night / Early morning", "Noon", "Late afternoon", "Evening", "A", "2:00 a.m. is late night / early morning."),
        ("Which day comes right after Monday?", "Tuesday", "Wednesday", "Sunday", "Saturday", "A", "Tuesday follows Monday."),
        ("What is the standard abbreviation for **Tuesday**?", "Tue.", "Tues.", "Tu.", "Ts.", "A", "Tue. is standard abbreviation."),
        ("How many hours are between 12:00 midnight and 2:00 a.m.?", "2 hours", "1 hour", "3 hours", "4 hours", "A", "2:00 a.m. - 12:00 a.m. = 2 hours."),
        ("What is the abbreviation for **Thursday**?", "Thu.", "Thur.", "Th.", "Ts.", "A", "Thu. is standard abbreviation."),
        ("If you go to sleep at 10:00 p.m. and wake up at 6:00 a.m., how many hours do you sleep?", "8 hours", "6 hours", "10 hours", "7 hours", "A", "10 p.m. to 6 a.m. = 8 hours."),
        ("What is the abbreviation for **Friday**?", "Fri.", "Frid.", "Fr.", "F.", "A", "Fri. is standard abbreviation."),
        ("Which month comes right before November?", "October", "September", "December", "August", "A", "October comes before November."),
        ("What is the short abbreviation for **October**?", "Oct.", "Octo.", "Oc.", "Ot.", "A", "Oct. is standard abbreviation."),
        ("Which month comes right after October?", "November", "December", "September", "August", "A", "November comes after October."),
        ("What is the short abbreviation for **November**?", "Nov.", "Nove.", "Nv.", "Nm.", "A", "Nov. is standard abbreviation."),
        ("If today is Monday, what day was yesterday?", "Sunday", "Tuesday", "Saturday", "Friday", "A", "Yesterday was Sunday."),
        ("If today is Tuesday, what day will tomorrow be?", "Wednesday", "Monday", "Thursday", "Friday", "A", "Tomorrow will be Wednesday."),
        ("What is the abbreviation for **Wednesday**?", "Wed.", "Weds.", "We.", "W.", "A", "Wed. is standard abbreviation."),
        ("Which day comes between Monday and Wednesday?", "Tuesday", "Thursday", "Sunday", "Friday", "A", "Tuesday is between Monday and Wednesday."),
        ("Which month comes right before December?", "November", "October", "September", "January", "A", "November comes before December.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(days_easy, start=1):
        qid = f"BK02_CH12_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Vocabulary & Time Concepts:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Days & Calendar Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The cat was noisy every night from **Monday** to **Thursday**. For how many nights was it noisy?", "4 nights", "3 nights", "5 nights", "2 nights", "A", "Monday to Thursday inclusive is 4 nights."),
        ("The cat stayed outside from **2:00 a.m. to 6:00 a.m.**. How many hours was the cat outside?", "4 hours", "3 hours", "5 hours", "2 hours", "A", "6:00 a.m. - 2:00 a.m. = 4 hours."),
        ("Match the day with its abbreviation: **Wednesday**", "Wed.", "Weds.", "We.", "W.", "A", "Wed. is standard."),
        ("Convert to 12-hour clock: **02:00 in the morning**", "2:00 a.m.", "2:00 p.m.", "14:00", "12:02 a.m.", "A", "02:00 in morning is 2:00 a.m."),
        ("Identify the correctly spelt month name:", "November", "Novembre", "Novemberr", "Novembere", "A", "November is the correct spelling."),
        ("Identify the INCORRECT pair of day and abbreviation:", "Monday - Mon.", "Tuesday - Tue.", "Wednesday - Wed.", "Tuesday - Tsd.", "D", "Tuesday abbreviation is Tue., not Tsd."),
        ("Calculate: How many days are in **November**?", "30 days", "31 days", "28 days", "29 days", "A", "November has 30 days."),
        ("Which month has 30 days and comes right after October?", "November", "December", "September", "August", "A", "November has 30 days and follows October."),
        ("Rearrange in correct chronological order: Tue, Sun, Mon, Wed", "Sun, Mon, Tue, Wed", "Mon, Sun, Tue, Wed", "Tue, Mon, Sun, Wed", "Wed, Tue, Mon, Sun", "A", "Sunday -> Monday -> Tuesday -> Wednesday."),
        ("What day is 2 days before Tuesday?", "Sunday", "Monday", "Saturday", "Friday", "A", "Tuesday - 2 days = Monday(1), Sunday(2)."),
        ("If a cat training course lasts for 3 weeks, how many days is that?", "21 days (3 x 7)", "15 days", "30 days", "14 days", "A", "3 weeks x 7 days = 21 days."),
        ("Select the month that has 31 days:", "December", "November", "September", "April", "A", "December has 31 days."),
        ("Which abbreviation stands for **December**?", "Dec.", "Dece.", "Dc.", "Dcm.", "A", "Dec. is standard abbreviation."),
        ("If today is **Tue.**, what day will it be after 7 days?", "Tuesday", "Wednesday", "Monday", "Sunday", "A", "7 days is a full week cycle, landing on Tuesday again."),
        ("The owner was awake from **2:00 a.m. to 4:00 a.m.**. How many hours was he awake?", "2 hours", "1 hour", "3 hours", "4 hours", "A", "4:00 a.m. - 2:00 a.m. = 2 hours."),
        ("Identify the term that means 'occurring at night':", "Nocturnal / Nighttime", "Diurnal", "Weekly", "Yearly", "A", "Nocturnal means active at night."),
        ("Which of the following is a weekday?", "Tuesday", "Sunday", "Saturday", "Weekend", "A", "Tuesday is a weekday."),
        ("Choose the correct abbreviation for **November**:", "Nov.", "Nove.", "Nv.", "Nm.", "A", "Nov. is standard.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH12_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Application & Story Timeline:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Calendar & Time Reasoning", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("The poem says: 'By two a.m. or thereabouts, the mouse is in, the cat is out.' If two a.m. is 2 hours past midnight, what time is midnight?", "12:00 a.m.", "12:00 p.m.", "2:00 p.m.", "10:00 p.m.", "A", "Midnight is 12:00 a.m."),
        ("If the cat meows every **15 minutes** between 2:00 a.m. and 3:00 a.m., how many times does it meow in that 1 hour?", "4 times (60 / 15)", "2 times", "5 times", "3 times", "A", "60 minutes / 15 minutes = 4 times."),
        ("Solve the calendar puzzle: If 2nd November was a Tuesday, what day of the week was 9th November?", "Tuesday", "Wednesday", "Monday", "Thursday", "A", "2 + 7 = 9th November, landing on Tuesday."),
        ("Analyze this schedule: Mouse comes in on Mon, Wed, Fri nights; Cat meows out on Tue, Thu, Sat nights. On which night is it quiet?", "Sunday night", "Monday night", "Saturday night", "Wednesday night", "A", "Sunday night is not listed in schedule."),
        ("Complete the full series of day abbreviations: Mon., Tue., Wed., Thu., Fri., Sat., ____.", "Sun.", "Sund.", "Su.", "Sn.", "A", "Sun. completes the 7 days of the week."),
        ("If a pet care period lasted a fortnight, how many days did it cover?", "14 days (2 weeks)", "7 days", "30 days", "3 days", "A", "A fortnight is 14 days."),
        ("Spot the error in the calendar sequence: 'Sep, Oct, Dec, Nov, Jan'", "December and November are in wrong order.", "October is in wrong position.", "January should be first.", "No error.", "A", "November comes before December (Sep, Oct, Nov, Dec, Jan)."),
        ("November has **30 days**. What date was the day right after 30th November?", "1st December", "31st November", "29th November", "1st January", "A", "November has 30 days, so next day is 1st December."),
        ("If yesterday was two days before Tuesday, what day is tomorrow?", "Tuesday", "Monday", "Wednesday", "Sunday", "A", "Two days before Tuesday = Sunday (yesterday). Today = Monday. Tomorrow = Tuesday."),
        ("Calculate: How many days are there in total during **November** and **December** combined?", "61 days (30 + 31)", "60 days", "62 days", "59 days", "A", "November (30) + December (31) = 61 days."),
        ("HOTS Reasoning: Why does Ogden Nash specify 'two a.m.' rather than 2 p.m. in this poem?", "Because 2 a.m. is late night when humans are sleeping in cots and domestic irony is funniest.", "Because cats eat at 2 p.m.", "Because mice sleep at noon.", "Because houses are locked.", "A", "2 a.m. highlights nocturnal disturbance during sleeping hours."),
        ("Identify the correct statement about a non-leap year:", "A non-leap year has 365 days and February has 28 days.", "A non-leap year has 366 days.", "February has 30 days.", "A non-leap year occurs every 4 years.", "A", "Standard year has 365 days (Feb = 28 days)."),
        ("A cat meowed 30 times in 10 minutes. How many meows per minute on average?", "3 meows per minute", "5 meows", "2 meows", "10 meows", "A", "30 / 10 = 3 meows per minute."),
        ("Which month pair both have 31 days and come right after each other at the end of the year and start of next year?", "December and January", "November and December", "October and November", "January and February", "A", "December (31) and January (31) are consecutive 31-day months.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH12_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Logic & Mathematical Time Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Calendar & Time Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 4. Action Verbs Identification (50 Qs)
# ---------------------------------------------------------------------------
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification — Chapter 12: The Cat\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_verbs = [
        ("You **get** a wife, you get a house.", "get", "wife", "house", "you", "A", "'get' is the main action verb."),
        ("Eventually you **get** a mouse.", "get", "eventually", "mouse", "you", "A", "'get' is the action verb."),
        ("You **get** a kitty in a trice.", "get", "kitty", "trice", "you", "A", "'get' is the action verb."),
        ("It **dawns** upon you in your cot.", "dawns", "upon", "you", "cot", "A", "'dawns' is the mental action verb."),
        ("Instead of kitty, **says** your spouse.", "says", "instead", "kitty", "spouse", "A", "'says' is the speech action verb."),
        ("You **should have got** another mouse.", "got / should have got", "another", "mouse", "you", "A", "'got' is the main action verb."),
        ("The cat **meows** loudly at two a.m.", "meows", "cat", "loudly", "night", "A", "'meows' is the physical action verb."),
        ("The mouse **enters** the house quietly.", "enters", "mouse", "house", "quietly", "A", "'enters' is the physical action verb."),
        ("The cat **goes** outside at night.", "goes", "cat", "outside", "night", "A", "'goes' is the physical action verb."),
        ("The spouse **wakes** up at 2 a.m.", "wakes", "spouse", "up", "cot", "A", "'wakes' is the action verb."),
        ("The cat **chases** the little mouse.", "chases", "cat", "mouse", "little", "A", "'chases' is the physical action verb."),
        ("The owner **lies** in his cot.", "lies", "owner", "his", "cot", "A", "'lies' is the physical action verb."),
        ("The mouse **slips** inside the kitchen.", "slips", "mouse", "inside", "kitchen", "A", "'slips' is the physical action verb."),
        ("The spouse **suggests** getting another mouse.", "suggests", "spouse", "getting", "mouse", "A", "'suggests' is the speech action verb."),
        ("The cat **makes** a loud noise outside.", "makes", "cat", "loud", "noise", "A", "'makes' is the action verb."),
        ("The owner **realizes** the cat is noisy.", "realizes", "owner", "cat", "noisy", "A", "'realizes' is the mental action verb."),
        ("The mouse **remains** quiet in the room.", "remains", "mouse", "quiet", "room", "A", "'remains' is the action verb."),
        ("The spouse **speaks** softly to her husband.", "speaks", "spouse", "softly", "husband", "A", "'speaks' is the action verb.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_verbs, start=1):
        qid = f"BK02_CH12_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in this sentence from or related to Chapter 12:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Action Verb Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Which word from the sentence is an **action verb**? 'The cat **suddenly** **chases** the **small** **mouse**.'", "chases", "suddenly", "small", "mouse", "A", "'chases' shows physical action; 'suddenly' is adverb, 'small' is adjective, 'mouse' is noun."),
        ("Identify BOTH action verbs in: 'The mouse **enters** the house and **remains** silent.'", "enters, remains", "mouse, house", "silent, enters", "remains, house", "A", "'enters' and 'remains' are both action verbs."),
        ("What is the past tense action verb of 'get' as used in poem ('You got a kitty')?", "got", "getted", "getting", "gets", "A", "Past tense of get is got."),
        ("Choose the sentence where the underlined word is used as an ACTION VERB:", "I will **get** a quiet pet tomorrow.", "He gave a quick **get**.", "That was a good **get**.", "I noticed his **get**.", "A", "In (A), 'get' acts as the main action verb."),
        ("Find the action verb in: 'It dawns upon you in your cot.'", "dawns", "upon", "you", "cot", "A", "'dawns' is the action verb meaning realization."),
        ("Which sentence contains NO physical action verb?", "The mouse is silent, the cat is not.", "The mouse enters the house.", "The cat goes outside.", "The spouse speaks to him.", "A", "'The mouse is silent, the cat is not' contains linking verbs 'is', but no physical action verb."),
        ("Change the action verb 'get' to past tense: 'They (get) a kitty yesterday.'", "got", "getted", "getting", "gets", "A", "Past tense of get is got."),
        ("Identify the action verb: 'The cat meows and disturbs sleep.'", "meows, disturbs", "cat, sleep", "meows, cat", "disturbs, sleep", "A", "'meows' and 'disturbs' are action verbs."),
        ("Select the action verb that completes the sentence: 'The spouse ____ another mouse instead of a kitty.'", "recommended / suggested", "quiet", "house", "cat", "A", "'recommended' / 'suggested' is an action verb."),
        ("Which word is an action verb? (spouse, dawns, trice, cot)", "dawns", "spouse", "trice", "cot", "A", "'dawns' is an action verb; others are nouns/adverbs."),
        ("What action does the spouse perform at the end of the poem?", "says / suggests", "kitty", "trice", "cot", "A", "The spouse says/suggests (action verb)."),
        ("Identify the action verb in: 'The owner thinks about getting a quiet pet.'", "thinks", "owner", "quiet", "pet", "A", "'thinks' is a mental action verb."),
        ("Choose the correct action verb: 'The mouse ____ inside while the cat goes outside.'", "slips / enters", "quiet", "silent", "house", "A", "'slips' / 'enters' is the action verb."),
        ("Identify the action verb in: 'The cat meows loudly at night.'", "meows", "cat", "loudly", "night", "A", "'meows' is the action verb."),
        ("Which of these words is NOT an action verb? (get, say, dawn, silent)", "silent", "get", "say", "dawn", "A", "'silent' is an adjective; others are action verbs."),
        ("Identify the action verb in: 'The owner wakes up at two a.m.'", "wakes", "owner", "up", "cot", "A", "'wakes' is the action verb."),
        ("Fill in the blank with an appropriate action verb: 'The cat ____ outside the door.'", "cried / meowed", "quiet", "silent", "house", "A", "'cried' / 'meowed' is an action verb."),
        ("What action verb completes the sentence? 'The spouse ____ getting a cat was a mistake.'", "realizes / believes", "noisy", "cat", "house", "A", "'realizes' / 'believes' is an action verb.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH12_CAT04_Q{idx:02d}"
        qtxt = f"Action Verb Grammar Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Action Verb Context & Tense", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence: 'The spouse humorously suggested and advised getting another mouse.' How many total ACTION VERBS are present?", "2 action verbs ('suggested', 'advised')", "1 action verb", "3 action verbs", "0 action verbs", "A", "'suggested' and 'advised' are action verbs; 'humorously', 'another' are adverbs/adjectives."),
        ("Categorize the verbs: In 'The mouse **is** quiet, but the cat **meows**', classify 'is' and 'meows'.", "'is' is a linking verb; 'meows' is an action verb.", "Both are action verbs.", "Both are linking verbs.", "'is' is action; 'meows' is linking.", "A", "'is' links state of being; 'meows' shows action."),
        ("Replace the weak verb with a strong action verb: 'The mouse **goes** into the house.'", "The mouse **sneaks** into the house.", "The mouse **was near** the house.", "The mouse **saw** the house.", "The mouse **looked at** the kitchen.", "A", "'sneaks' is a much stronger, vivid action verb."),
        ("Identify the sentence with THREE distinct action verbs:", "The cat **leaves** the house, **wanders** outside, and **meows** loudly.", "The cat is noisy, black, and loud.", "The mouse is silent in your cot.", "You get a wife and a house.", "A", "leaves, wanders, meows are 3 distinct action verbs."),
        ("Differentiate verb types: Which underlined word is an ACTION verb?", "The spouse **said** you should get another mouse.", "The cat was **noisy**.", "The mouse was **silent**.", "The night was **dark**.", "A", "'said' is an action verb."),
        ("Spot the incorrect verb tense: 'It **dawned** / **dawns** upon you yesterday.' Correct it for past simple:", "'dawned' is the past action verb form.", "'dawns' should be 'dawning'.", "'dawns' should be 'dawn'.", "'dawns' should be 'will dawn'.", "A", "Past simple of dawn is dawned."),
        ("Form an action chain: Rearrange the story action verbs in correct order of occurrence: (gets wife and house, gets mouse, gets kitty, realizes cat is noisy)", "gets wife and house -> gets mouse -> gets kitty -> realizes cat is noisy", "realizes cat is noisy -> gets kitty -> gets mouse -> gets wife", "gets kitty -> gets mouse -> realizes -> gets wife", "gets mouse -> gets kitty -> gets wife -> realizes", "A", "Chrono order: wife/house, mouse, kitty, realization."),
        ("Identify the verb error in dialogue: Spouse said, 'You should have **get** another mouse!'", "'get' is incorrect; the past participle form is 'got' (or 'gotten') ('should have got').", "'get' should be 'getting'.", "'get' should be 'gets'.", "No error.", "A", "Modal perfect 'should have' requires past participle 'got'/'gotten'."),
        ("Analyze this sentence: 'The poem **satirizes** pet ownership.' What type of action verb is 'satirizes'?", "Literary/humorous action verb", "Physical movement verb", "Linking verb", "State of being verb", "A", "'satirizes' is an action verb describing literary humor."),
        ("Which sentence uses action verbs to show cause and effect?", "The cat **meowed** loudly, so the owner **woke** up at 2 a.m.", "The mouse is silent and the cat is out.", "Ogden Nash wrote the poem.", "You get a wife and house.", "A", "'meowed' (cause action) -> 'woke' (effect action)."),
        ("Spot the missing action verb: 'The cat ____ outside while the mouse ____ the kitchen.'", "meows, explores", "noisy, silent", "was, was", "quick, slow", "A", "'meows' and 'explores' complete sentence with vivid actions."),
        ("HOTS Reasoning: Why is 'regrets' in 'The owner regrets getting a cat' considered a CLEAR mental action verb?", "Because it describes actively feeling sorrow or remorse over a past decision.", "Because regretting requires climbing.", "Because cat is outside.", "Because it is a noun.", "A", "Descriptive action verb conveying emotional realization."),
        ("Transform the action verb to future tense: 'You **get** another mouse tomorrow.'", "You **will get** another mouse tomorrow.", "You **got** another mouse tomorrow.", "You **are getting** another mouse tomorrow.", "You **get** another mouse tomorrow.", "A", "'will get' expresses future action."),
        ("Identify the sentence where the action verb matches the plural subject:", "The cats **meow** outside the window.", "The cats **meows** outside the window.", "A cat **meow** outside the window.", "The cats **is meowing** outside the window.", "A", "Plural subject 'cats' takes base verb 'meow' in simple present.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH12_CAT04_Q{idx:02d}"
        qtxt = f"Higher Order Action Verb Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Action Verb Classification & Tense Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 5. Punctuation Marks (50 Qs)
# ---------------------------------------------------------------------------
def build_punctuation_marks():
    header = "# Category 5: Punctuation Marks & Capitalization — Chapter 12: The Cat\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_punct = [
        ("What punctuation mark should be placed at the end of: 'You get a wife, you get a house__'", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "Comma (,)", "A", "A statement ends with a full stop."),
        ("Which mark is used at the end of an asking sentence: 'What does the spouse suggest instead of a cat__'", "Question mark (?)", "Full stop (.)", "Comma (,)", "Exclamation mark (!)", "A", "A question ends with a question mark."),
        ("Which letter should ALWAYS be capitalized in an author's name like 'Ogden Nash'?", "First letter of each name (Ogden Nash)", "The last letter", "All letters", "No letters", "A", "Author names require capitalized initial letters."),
        ("Identify the punctuation mark used to separate items in a list: 'The house has a cat__ a mouse__ and a cot.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Hyphen (-)", "A", "Commas separate items in a list."),
        ("Which punctuation mark shows sudden surprise: 'You should have got another mouse!__'", "Exclamation mark (!)", "Full stop (.)", "Comma (,)", "Question mark (?)", "A", "Exclamation marks express intense surprise/humor."),
        ("Select the proper noun (poet's name) that MUST start with capital letters:", "Ogden Nash", "kitty", "mouse", "house", "A", "'Ogden Nash' as author's name starts with capital letters."),
        ("Which of the following is the symbol for a **full stop**?", ".", "?", "!", ",", "A", "Period/full stop is '.'"),
        ("Which of the following is the symbol for a **question mark**?", "?", ".", "!", ",", "A", "Question mark is '?'"),
        ("Which of the following is the symbol for an **exclamation mark**?", "!", "?", ".", ",", "A", "Exclamation mark is '!'"),
        ("Which word in this sentence should start with a CAPITAL letter? 'the poem is titled The Cat.'", "the -> The", "titled -> Titled", "poem -> Poem", "is -> Is", "A", "First word of sentence 'The' must start with a capital letter."),
        ("What punctuation mark goes in the box? 'By two a.m. or thereabouts [ ]'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "A", "Comma pauses poetic line."),
        ("Which time abbreviation is punctuated correctly?", "a.m. / p.m.", "am.", "a.m", "A.M..", "A", "Standard lowercase dotted abbreviation 'a.m.'"),
        ("What mark goes after a speaker tag: 'Spouse said__ \"You should have got another mouse!\"'", "Comma (,)", "Question mark (?)", "Full stop (.)", "Exclamation mark (!)", "A", "Comma follows dialogue speaker tags."),
        ("Identify the correct capital letter for the pronoun 'I': 'he said, \"i realized the cat was noisy.\"'", "I", "i", "i'm", "I'm", "A", "Standalone pronoun 'I' is always capitalized."),
        ("Which option shows a sentence ending correctly?", "The mouse is silent, the cat is not.", "The mouse is silent, the cat is not?", "The mouse is silent, the cat is not,", "The mouse is silent, the cat is not;", "A", "Full stop at end of simple statement."),
        ("What mark is used in contractions like '**don't**' or '**it's**'?", "Apostrophe (')", "Comma (,)", "Full stop (.)", "Hyphen (-)", "A", "Apostrophe indicates contraction."),
        ("Which poem title is capitalized correctly?", "The Cat", "the cat", "The cat", "THE CAT", "A", "Title capitalization."),
        ("What punctuation mark is used around spoken lines: '___You should have got another mouse!___'", "Quotation marks / Speech marks ( \" \" )", "Parentheses ( )", "Full stops ( . . )", "Commas ( , , )", "A", "Quotation marks enclose exact spoken words.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_punct, start=1):
        qid = f"BK02_CH12_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Punctuation & Capitalization Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Identify the sentence with CORRECT capitalization and punctuation:", "The poem \"The Cat\" was written by Ogden Nash.", "the poem \"the cat\" was written by ogden nash.", "The poem \"the Cat\" was written by Ogden nash?", "the Poem \"The Cat\" Was Written By Ogden Nash.", "A", "Title \"The Cat\", author Ogden Nash capitalized; period at end."),
        ("Which sentence is punctuated as a CORRECT question?", "Why is the cat noisy at two a.m.?", "Why is the cat noisy at two a.m..", "Why is the cat noisy at two a.m.!", "Why is the cat noisy at two a.m.,", "A", "Question starting with 'Why' ends with question mark ?"),
        ("Spot the capitalization mistake in: 'ogden Nash wrote a funny poem.'", "'ogden' should be capitalized ('Ogden'); 'Nash' is correct.", "'Nash' should be lowercase.", "'poem' should be uppercase.", "No mistake.", "A", "First name 'Ogden' must be capitalized."),
        ("Choose the correctly punctuated dialogue sentence:", "\"You should have got another mouse,\" said the spouse.", "you should have got another mouse said the spouse.", "\"You should have got another mouse\" said the spouse", "You should have got another mouse, said the spouse.", "A", "Quotation marks around dialogue, comma inside quote, capital Y."),
        ("Identify where a COMMA is missing: 'You get a wife you get a house.'", "Between 'wife' and 'you' ('a wife, you get')", "After 'You'", "After 'house'", "No comma needed", "A", "Commas separate clauses in poem: 'You get a wife, you get a house'."),
        ("Which sentence uses the apostrophe correctly for possession?", "This is the cat's meow.", "This is the cats' meow.", "This is the cats meow.", "This is the cat's' meow.", "A", "cat's indicates singular possession."),
        ("Select the sentence with CORRECT punctuation for an exclamatory statement:", "What a noisy cat this is!", "What a noisy cat this is?", "What a noisy cat this is.", "What a noisy cat this is,", "A", "Exclamatory statement ends with exclamation mark !"),
        ("Which contraction is written correctly for 'should not'?", "shouldn't", "should'nt", "shouldnt'", "s'houldnt", "A", "shouldn't is standard contraction."),
        ("Find the sentence with NO capitalization errors:", "Ogden Nash wrote a poem about a mouse and a cat.", "ogden nash wrote a poem about a mouse and a cat.", "Ogden Nash Wrote A Poem About A Mouse And A Cat.", "ogden Nash wrote a poem.", "A", "'Ogden Nash' capitalized as proper name."),
        ("What punctuation mark belongs in the blank? 'The spouse exclaimed, \"Get another mouse!\"'", "!", ".", "?", ",", "A", "Exclamation mark ! expresses humor/exclamation."),
        ("Choose the correct form for 'could not':", "couldn't", "could'nt", "couldnt'", "c'ouldnt", "A", "couldn't is standard contraction."),
        ("Identify the punctuation error: 'The mouse is in, the cat is out.'", "Comma splice between two independent clauses (acceptable in poetic meter, but standard prose requires semicolon/period).", "Missing question mark.", "Missing capital letters.", "No error.", "A", "Poetic parallelism using commas."),
        ("Select the sentence with proper use of capital letters for author and poem title:", "Ogden Nash wrote \"The Cat\" in America.", "ogden nash wrote \"the cat\" in america.", "Ogden nash wrote \"The cat\" in America.", "ogden Nash wrote \"The Cat\" in america.", "A", "Names 'Ogden Nash', 'The Cat', 'America' all capitalized."),
        ("Which sentence correctly uses an apostrophe for possessive noun?", "The mouse's movement was completely silent.", "The mouses' movement was completely silent.", "The mouses movement was completely silent.", "The mouse's' movement was completely silent.", "A", "mouse's indicates singular possession."),
        ("Identify the correct punctuation for a list of items: 'The household has ____'", "a wife, a house, and a cat.", "a wife a house and a cat.", "a wife; a house; and a cat.", "a wife: a house: and a cat.", "A", "Commas separate items in list."),
        ("Choose the sentence that correctly asks a question about the story:", "Why does the cat stay outside at night?", "Why does the cat stay outside at night.", "Why does the cat stay outside at night!", "why does the cat stay outside at night.", "A", "Capital W, ends with question mark ?"),
        ("Fix the sentence: 'who wrote the poem the cat'", "Who wrote the poem \"The Cat\"?", "Who wrote the poem the cat.", "who wrote the poem The Cat!", "Where is Nash?", "A", "Capital W, title quotes, ends with ?"),
        ("Which of these sentences is punctuated PERFECTLY?", "The spouse said, \"You should have got another mouse!\"", "The spouse said \"you should have got another mouse!\"", "the spouse said, \"You should have got another mouse!\"", "The spouse said, \"You should have got another mouse.\"", "A", "Capital T, comma after said, speech marks around dialogue with ! inside.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH12_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Context Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Punctuation Application & Dialogue Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze and count ALL capitalization and punctuation errors in: 'on tuesday ogden nash wrote a poem where spouse said, instead of kitty get another mouse'", "5 errors (on->On, tuesday->Tuesday, ogden nash->Ogden Nash, quotation marks, capital I in Instead, period)", "2 errors", "3 errors", "7 errors", "A", "Starts sentence, day name, author name, quotation marks, capital I, period."),
        ("Correct the entire dialogue paragraph: 'the husband asked is the cat noisy spouse replied yes the cat is not silent'", "\"Is the cat noisy?\" asked the husband. Spouse replied, \"Yes, the cat is not silent.\"", "the husband asked \"is the cat noisy\" spouse replied \"yes the cat is not silent.\"", "The husband asked, Is the cat noisy. Spouse replied, Yes the cat is not silent.", "\"Is the cat noisy?\" Asked the husband. Spouse replied \"Yes the cat is not silent?\"", "A", "Full proper quotation, dialogue tags, capitalization, and terminal punctuation."),
        ("Distinguish between singular possessive and contraction: 'The cat**'**s meow is loud, and it**'**s two a.m.'", "First 's is possessive (meow of the cat); second 's is contraction (it is).", "Both are possessive.", "Both are contractions.", "First is contraction; second is possessive.", "A", "cat's meow = meow of the cat; it's = it is."),
        ("Spot the subtle punctuation flaw in this dialogue: '\"The cat is noisy,\" Said the spouse.'", "'Said' should be lowercase 'said' because it continues the dialogue tag outside quotation marks.", "'The' should be lowercase.", "Commas should be outside quotes.", "No flaw.", "A", "Dialogue tags following quotes start with lowercase unless proper nouns."),
        ("Which sentence correctly uses punctuation to show contrast?", "The mouse is silent, but the cat is not.", "The mouse is silent but, the cat is not.", "The mouse is silent but the cat is not!", "The mouse is silent; but the cat is not?", "A", "Comma before coordinating conjunction 'but' joining two independent clauses."),
        ("Reconstruct with perfect punctuation: 'ogden nash wrote the cat on tuesday 2nd november 1940'", "Ogden Nash wrote \"The Cat\" on Tuesday, 2nd November 1940.", "ogden nash wrote the cat on tuesday, 2nd november 1940.", "Ogden Nash wrote The Cat on Tuesday 2nd November 1940", "Ogden nash wrote The Cat on tuesday 2nd november 1940.", "A", "Author name, title quotes, Tuesday, 2nd November 1940, period."),
        ("Identify why exclamation mark is necessary here: '\"Instead of kitty, get another mouse!\"'", "Because the speaker is expressing humorous exasperation and advice.", "Because cat is outside.", "Because mouse is silent.", "Because sentence is long.", "A", "Exclamation mark communicates humorous exasperation."),
        ("Choose the correctly punctuated sentence containing an appositive phrase:", "Ogden Nash, a famous American poet, wrote this humorous poem.", "Ogden Nash a famous American poet wrote this humorous poem.", "Ogden Nash, a famous American poet wrote this humorous poem.", "Ogden Nash a famous American poet, wrote this humorous poem.", "A", "Appositive phrase 'a famous American poet' is set off by commas."),
        ("Analyze the use of time abbreviation in: 'By two a.m. or thereabouts...'", "'a.m.' is formatted in lowercase with periods for ante meridiem.", "a.m. replaces comma.", "a.m. indicates question.", "a.m. is a proper noun.", "A", "'a.m.' is standard time format."),
        ("Identify the correct sentence with direct speech quote within text:", "The spouse declared, \"You should have got another mouse,\" and laughed.", "The spouse declared \"You should have got another mouse\" and laughed.", "The spouse declared, 'You should have got another mouse,' and laughed.", "The spouse declared: \"You should have got another mouse\" and laughed.", "A", "Comma before quote, double quotation marks around direct speech, comma inside quote."),
        ("Spot the missing apostrophe: 'The cats meow woke everyone at two a.m.'", "Missing apostrophe in 'cat's' -> 'The cat's meow...'", "Missing apostrophe in 'everyone''", "Missing apostrophe in 'woke''", "No apostrophe needed", "A", "'The cat's meow' requires possessive apostrophe."),
        ("HOTS Reasoning: Why does putting a comma in different places change meaning? Compare: 'Spouse, said husband, is right.' vs 'Spouse said, \"Husband is right.\"'", "In the first, husband says spouse is right; in the second, spouse says husband is right.", "Both mean the exact same thing.", "The first is a question.", "Commas do not affect meaning.", "A", "Punctuation alters who speaks and who is praised."),
        ("Correct all 4 errors in: 'whats the cats noise level asked the spouse'", "\"What's the cat's noise level?\" asked the spouse.", "whats the cats noise level? asked the spouse.", "\"What's the cats noise level.\" asked the spouse.", "\"whats the cats noise level?\" Asked the spouse.", "A", "Quotation marks, capital W, possessive cat's, question mark, period at end."),
        ("Identify the rule for capitalizing titles of short poems like \"The Cat\":", "Titles of poems take initial capital letters and are enclosed in quotation marks.", "Poem titles are never capitalized.", "Poem titles are capitalized only at end of line.", "Poem titles must be written in ALL CAPS.", "A", "Short poem titles take initial capitals and quotation marks.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH12_CAT05_Q{idx:02d}"
        qtxt = f"Higher Order Punctuation Analysis & Dialogue Formatting:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Punctuation & Dialogue Editing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 6. Phonics & Vowel Digraphs (50 Qs)
# ---------------------------------------------------------------------------
def build_phonics_digraphs():
    header = "# Category 6: Phonics & Vowel Digraphs — Chapter 12: The Cat\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_phonics = [
        ("Which vowel digraph is present in the word **'house'** (in Chapter 12)?", "ou", "ee", "ai", "ea", "A", "'ou' is the vowel digraph in house."),
        ("Identify the vowel digraph in the word **'mouse'**:", "ou", "ee", "oa", "ui", "A", "'ou' forms the diphthong sound in mouse."),
        ("Which word from the poem contains the **'ou'** vowel digraph?", "spouse", "cat", "cot", "trice", "A", "'spouse' contains the 'ou' digraph."),
        ("Identify the vowel digraph in the word **'clean'**:", "ea", "ee", "ow", "oo", "A", "'ea' forms long /e/ sound in clean."),
        ("Which vowel digraph appears in the word **'paid'**?", "ai", "ay", "ea", "oa", "A", "'ai' makes long /a/ sound in paid."),
        ("Find the word with the **'ou'** vowel digraph: 'By two a.m. or thereabouts...'", "thereabouts", "two", "a.m.", "or", "A", "'thereabouts' contains 'ou' vowel digraph."),
        ("Which word from the poem rhymes with **'house'**?", "mouse", "horse", "hiss", "hose", "A", "'mouse' rhymes with 'house'."),
        ("Which word from the poem rhymes with **'mice'**?", "trice", "mice", "nice", "trice / nice", "D", "'trice' and 'nice' rhyme with 'mice'."),
        ("Identify the vowel digraph in the word **'boasted'**:", "oa", "ou", "ow", "oo", "A", "'oa' makes long /o/ sound in boasted."),
        ("Which word from the poem rhymes with **'cot'**?", "not", "cat", "cut", "coat", "A", "'not' rhymes with 'cot'."),
        ("Identify the vowel digraph in **'sweet'**:", "ee", "ea", "oo", "ui", "A", "'ee' makes long /e/ sound in sweet."),
        ("Which word from Chapter 12 has the **'ou'** digraph making an /ow/ sound?", "spouse", "soup", "group", "soul", "A", "'spouse' has 'ou' making /ow/ sound."),
        ("Which word rhymes with **'day'**?", "away", "die", "due", "door", "A", "'away' rhymes with 'day'."),
        ("Identify the silent letters in **'night'** (as in 'at night'):", "gh", "n", "i", "t", "A", "Silent 'gh' in night."),
        ("Which word from the story has long /i/ sound spelled with **'igh'**?", "night", "bought", "bowl", "baker", "A", "'igh' in night makes long /i/ sound."),
        ("Find the word with **'ou'** digraph: 'They walked around the house.'", "around", "house", "both A and B", "neither", "C", "Both 'around' and 'house' contain 'ou' digraph."),
        ("Which word rhymes with **'cat'**?", "mat", "cot", "cut", "coat", "A", "'mat' rhymes with 'cat'."),
        ("Identify the silent letter in the word **'know'** (as in 'did not know'):", "k", "n", "o", "w", "A", "Initial 'k' before 'n' is silent.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_phonics, start=1):
        qid = f"BK02_CH12_CAT06_Q{idx:02d}"
        qtxt = f"Phonics & Vowel Digraph Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Vowel Digraphs & Rhyming Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Compare the **'ou'** digraph sound in **'house'** and **'soup'**. What is the difference?", "'house' has /ow/ diphthong sound; 'soup' has long /oo/ sound.", "Both have long /oo/ sound.", "Both have short /o/ sound.", "'house' has long /oo/; 'soup' has /ow/.", "A", "'ou' can make /ow/ (house) or long /oo/ (soup)."),
        ("Select the word pair from Chapter 12 that has the SAME vowel digraph sound:", "house - mouse", "night - bread", "cot - roar", "spouse - sweet", "A", "'house' (ou) and 'mouse' (ou) both make /ow/ diphthong sound."),
        ("Which word contains SILENT letters? (night, cat, cot, mouse)", "night", "cat", "cot", "mouse", "A", "'night' has silent 'gh'."),
        ("Identify the odd one out based on vowel sound: (house, mouse, spouse, soup)", "soup", "house", "mouse", "spouse", "A", "'soup' has long /oo/ sound; others have /ow/ diphthong sound."),
        ("Which digraph completes the word for dwelling place? 'h__se'", "ou", "ee", "ai", "ea", "A", "'house' uses 'ou' digraph."),
        ("Group these story words by digraph: **house**, **mouse**, **spouse**. What digraph do they all share?", "ou", "ow", "oo", "oi", "A", "All share 'ou' making /ow/ diphthong sound."),
        ("Find the word with consonant digraph **'th'** from the story: 'By two a.m. or **thereabouts**...'", "thereabouts", "two", "mouse", "cat", "A", "'thereabouts' contains voiced 'th' consonant digraph."),
        ("Which of these words has the **'ow'** vowel digraph making long /o/ sound? (know, show, blow, all of these)", "all of these", "know", "show", "blow", "A", "know, show, blow all share 'ow' long /o/ sound."),
        ("Identify the vowel digraph in **'spouse'**:", "ou", "ae", "ur", "or", "A", "'ou' is the vowel digraph in spouse."),
        ("Which word from the story has silent **'k'**? (know, knee, knife, all of these)", "all of these", "know", "knee", "knife", "A", "know, knee, knife all have silent initial 'k' before 'n'."),
        ("Select the rhyming pair from the poem: 'house' and ____.", "mouse", "cat", "cot", "trice", "A", "'house' rhymes with 'mouse' in the poem."),
        ("Select the rhyming pair from the poem: 'mice' and ____.", "trice", "cat", "house", "cot", "A", "'mice' rhymes with 'trice' in the poem."),
        ("Select the rhyming pair from the poem: 'cot' and ____.", "not", "house", "mice", "trice", "A", "'cot' rhymes with 'not' in the poem."),
        ("Find the R-controlled vowel sound in: 'You should get **another** mouse.'", "er sound in another", "ea", "ou", "ai", "A", "R-controlled vowel in another."),
        ("Which word contains the **'oi'** diphthong/digraph? (choice, voice, point, all of these)", "all of these", "choice", "voice", "point", "A", "choice, voice, point all contain 'oi'."),
        ("Identify the soft **'c'** sound in Chapter 12 vocabulary: (trice, mice, place, all of these)", "all of these", "trice", "mice", "place", "A", "trice, mice, place all have soft /s/ sound for 'c' before 'e'."),
        ("Which word has a soft **'g'** sound? (germ, magic, region, all of these)", "all of these", "germ", "magic", "region", "A", "germ, magic, region all have soft /j/ sound for 'g'."),
        ("Choose the correct spelling with **'ou'** digraph for rodent:", "mouse", "mose", "mowse", "muose", "A", "mouse is standard spelling with 'ou'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH12_CAT06_Q{idx:02d}"
        qtxt = f"Phonics Analysis & Sound Pattern Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Phonic Rules & Sound Discrimination", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the phonics rule: Why does 'c' in **'trice'** sound like /s/, but 'c' in **'cot'** sounds like /k/?", "Because 'c' followed by 'e', 'i', or 'y' makes soft /s/ sound (trice); before 'o', 'a', 'u' it makes hard /k/ sound (cot).", "Because trice is fast.", "Because cot is small.", "There is no rule.", "A", "Soft 'c' rule: c + e, i, y = /s/ sound."),
        ("Categorize the 'ou' digraphs into /ow/ vs /oo/: (house, mouse, spouse, soup, group)", "/ow/: house, mouse, spouse; /oo/: soup, group", "All are /ow/.", "All are /oo/.", "/ow/: soup; /oo/: house", "A", "house, mouse, spouse make /ow/; soup, group make long /oo/."),
        ("Identify the word pair where SILENT letters exist in BOTH words:", "night - know", "cat - cot", "mouse - house", "spouse - trice", "A", "'night' (silent gh) and 'know' (silent k)."),
        ("Decode the phonics blend: Which word contains a 2-letter consonant blend at the start?", "spouse / trice", "cat", "cot", "mouse", "A", "'sp' / 'tr' blend type."),
        ("Examine the soft 'c' rule: Why is 'c' soft in **'mice'** but hard in **'cat'**?", "'c' followed by 'e' makes soft /s/ sound (mice); 'c' before 'a' makes hard /k/ sound (cat).", "Because mice are small.", "Because cat is fast.", "There is no rule.", "A", "Soft 'c' rule: c + e = /s/ sound."),
        ("Find the word with BOTH a vowel digraph AND a silent letter:", "thereabouts", "cat", "cot", "mouse", "A", "'thereabouts' has 'ou' digraph and silent 'e'."),
        ("Differentiate diphthongs: Which pair produces the /ow/ sound as in **'mouse'**?", "mouse - house", "voice - coin", "paid - day", "boat - coat", "A", "'mouse' and 'house' share /ow/ diphthong sound."),
        ("Analyze homophones: 'The cat jumped onto the **cot** / **caught**.' Which word means small bed?", "cot", "caught", "kott", "cote", "A", "'cot' (small bed) and 'caught' (past of catch) are homophones."),
        ("Identify the phonic pattern in **'eventually'**: What vowel sound does the first 'e' make?", "Short /i/ or /e/ sound", "Long /e/ sound", "Silent sound", "Short /u/ sound", "A", "'e-ven-tu-al-ly' first 'e' makes short /e/ sound."),
        ("Sort by ending sound: Which word ends with the /z/ sound? (houses, spouses, cats, cots)", "houses / spouses", "cats", "cots", "mice", "A", "Plurals ending in sibilant + es take /ez/ or /z/ ending sound (houses, spouses)."),
        ("Spot the word where 'k' is SILENT: (know, knee, knife, all of these)", "all of these", "know", "knee", "knife", "A", "'k' is silent before 'n' in know, knee, knife."),
        ("HOTS Reasoning: Why do 'cot' and 'caught' sound similar in some accents but have different spellings and meanings?", "They are near-homophones (different origins, spelling, and meanings).", "They are synonyms.", "They are antonyms.", "They are plurals.", "A", "Near-homophones share similar pronunciation but differ in spelling/meaning."),
        ("Identify the compound word from story concepts containing two simple words:", "thereabouts / doorstep", "eventually", "spouse", "kitty", "A", "thereabouts = there + abouts."),
        ("Determine the syllable count and stress: How many syllables are in **'eventually'**?", "5 syllables (e-ven-tu-al-ly)", "4 syllables", "3 syllables", "2 syllables", "A", "e-ven-tu-al-ly has 5 syllables.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH12_CAT06_Q{idx:02d}"
        qtxt = f"Higher Order Phonics & Orthographic Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Phonetic Rules & Homophone Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 7. Question Words & Interrogatives (50 Qs)
# ---------------------------------------------------------------------------
def build_question_words():
    header = "# Category 7: Question Words & Interrogatives — Chapter 12: The Cat\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_qwords = [
        ("___ happens after you get a wife and a house in the poem?", "What", "Who", "Where", "Why", "A", "'What' asks about event ('Eventually you get a mouse')."),
        ("___ do you get in a trice after words regarding mice?", "What", "Who", "Where", "Why", "A", "'What' asks about item ('a kitty')."),
        ("___ time of night is mentioned in the poem?", "What / When", "Who", "Where", "Why", "A", "'What time' asks about 'two a.m.'"),
        ("___ is inside the house by two a.m.?", "Who / What", "Where", "Why", "When", "A", "'What' asks about 'the mouse'."),
        ("___ is outside the house by two a.m.?", "Who / What", "Where", "Why", "When", "A", "'What' asks about 'the cat'."),
        ("___ is silent by two a.m.?", "Which / What", "Who", "Where", "Why", "A", "'What' asks about 'the mouse'."),
        ("___ is NOT silent by two a.m.?", "Which / What", "Who", "Where", "Why", "A", "'What' asks about 'the cat'."),
        ("___ speaks to you from the cot at night?", "Who", "What", "Where", "Why", "A", "'Who' asks about person ('your spouse')."),
        ("___ does your spouse suggest getting instead of a kitty?", "What", "Who", "Where", "Why", "A", "'What' asks about alternative ('another mouse')."),
        ("___ wrote the poem 'The Cat'?", "Who", "What", "Where", "Why", "A", "'Who' asks about author (Ogden Nash)."),
        ("___ does the word 'eventually' mean in the poem?", "What", "Who", "Where", "Why", "A", "'What' asks about meaning ('finally')."),
        ("___ does the word 'trice' mean in the poem?", "What", "Who", "Where", "Why", "A", "'What' asks about meaning ('very quickly')."),
        ("___ does the word 'spouse' mean in the poem?", "What", "Who", "Where", "Why", "A", "'What' asks about meaning ('husband or wife')."),
        ("___ is the owner lying when he realizes the cat is noisy?", "Where", "Who", "What", "Why", "A", "'Where' asks about location ('in your cot')."),
        ("___ is the cat outside while the mouse is inside?", "Why", "Who", "Where", "What", "A", "'Why' asks for reason (cat wanders out at night)."),
        ("___ pet did the owner get to catch the mouse?", "Which", "Who", "Where", "Why", "A", "'Which pet' asks about 'a kitty')."),
        ("___ pet turned out to be noisy at two a.m.?", "Which", "Who", "Where", "Why", "A", "'Which pet' asks about 'the cat')."),
        ("___ pet was quiet according to the poem?", "Which", "Who", "Where", "Why", "A", "'Which pet' asks about 'the mouse').")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_qwords, start=1):
        qid = f"BK02_CH12_CAT07_Q{idx:02d}"
        qtxt = f"Choose the correct **question word** (Who, What, Where, Why, How, When):\n\n\"{q_blank} _____?\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Question Word Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Match question to answer: Question: '___ is the cat not silent?' Answer: 'Because it meows outside at two a.m.'", "Why", "What", "Where", "Who", "A", "'Why' asks for reasons ('Because...')."),
        ("Match question to answer: Question: '___ is the mouse located by two a.m.?' Answer: 'The mouse is inside the house.'", "Where", "Who", "Why", "When", "A", "'Where' asks for location."),
        ("Choose the correct question word for TIME: '___ does the realization dawn upon you?'", "When", "Where", "Who", "Why", "A", "'When' inquires about time (by two a.m.)."),
        ("Form an asking sentence: 'The cat is noisy.' -> '____ is noisy at two a.m.?'", "What / Which pet", "Who", "Why", "Where", "A", "'What' inquires about subject."),
        ("Identify the INCORRECT question word usage: '**Why** wrote the poem The Cat?'", "'Why' should be 'Who'", "'Why' should be 'Where'", "'Why' should be 'When'", "No error", "A", "'Who wrote the poem...' asks for author identity."),
        ("Select the proper interrogative sentence:", "Why did the spouse suggest getting another mouse?", "Why the spouse suggested getting another mouse?", "Why does the spouse suggested?", "Why spouse suggested?", "A", "Interrogative word + auxiliary 'did' + subject + base verb."),
        ("Which question word asks about MANNER or METHOD? '___ quickly did they get a kitty?'", "How", "Who", "What", "Where", "A", "'How' inquires about speed ('in a trice')."),
        ("Complete the question: '___ of the two animals is quiet at night?'", "Which", "What", "Where", "Why", "A", "'Which' chooses between specific options (the mouse)."),
        ("Change statement to question: 'The cat goes outside.' -> '____ does the cat go?'", "Where", "Who", "Why", "What", "A", "'Where' asks for location."),
        ("Fill in the blank: '___ quiet is the mouse compared to the cat?'", "How", "What", "Where", "Why", "A", "'How quiet' measures degree."),
        ("Identify the question word in: 'Whom does the spouse speak to in the cot?'", "Whom", "does", "spouse", "speak", "A", "'Whom' is the interrogative pronoun asking about the owner/husband."),
        ("Choose the question that matches this answer: 'Instead of kitty, you should have got another mouse.'", "What does the spouse say at night?", "Where does the cat sleep?", "Who caught the mouse?", "What is a cot?", "A", "'What does the spouse say...' matches answer."),
        ("Fill in the blank: '___ word in the poem means very quickly?'", "Which", "Who", "Why", "Where", "A", "'Which word' asks for identification (trice)."),
        ("Complete: '___ pets are mentioned in the poem?'", "How many", "How much", "Who", "Where", "A", "'How many' asks about countable quantity (two: mouse and cat/kitty)."),
        ("Select the correct question for: 'The mouse is in, the cat is out.'", "What happens by two a.m.?", "Where is the kitchen?", "Why do cats like milk?", "Who is Ogden Nash?", "A", "'What happens by two a.m.?' asks for event."),
        ("Which question word inquires about POSSESSION? '___ advice was given by the spouse?'", "Whose", "Who", "Where", "Why", "A", "'Whose advice' asks about source."),
        ("Form question: 'They got two animals.' -> '____ animals did they get?'", "How many", "How much", "Why", "Where", "A", "'How many' asks for countable number."),
        ("Identify the question mark error: 'Why is the cat noisy at night.' Correct it:", "Why is the cat noisy at night?", "Why is the cat noisy at night!", "Why is the cat noisy at night,", "Why is the cat noisy at night;", "A", "Questions must end with question mark ?")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH12_CAT07_Q{idx:02d}"
        qtxt = f"Question Formation & Context Alignment:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Interrogative Sentence Formation", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence structure: 'Why does the spouse suggest getting another mouse instead of a kitty?' What is the syntax pattern?", "Question Word + Helping Verb (does) + Subject (the spouse) + Main Verb (suggest) + Gerund Phrase + Prepositional Phrase", "Question Word + Main Verb + Subject", "Subject + Question Word + Verb", "Helping Verb + Question Word + Subject", "A", "Standard English question syntax."),
        ("Differentiate between 'How many' vs 'How much': '___ mice' vs '___ noise'", "'How many' for countable mice; 'How much' for uncountable noise.", "Both use 'How many'.", "Both use 'How much'.", "'How much' for mice; 'How many' for noise.", "A", "Countable nouns take 'How many'; uncountable nouns take 'How much'."),
        ("Spot the syntax error in question: 'Where the cat goes at two a.m.?' Correct it:", "Where **does** the cat go at two a.m.?", "Where the cat goes at two a.m.?", "Where went the cat at two a.m.?", "Where do the cat go at two a.m.?", "A", "Present simple questions require auxiliary 'does' before singular subject 'the cat' and base verb 'go'."),
        ("Framing multi-question interview: What sequence of question words logically reveals the poem's humorous twist?", "What happens first -> When does the mouse enter -> Why is the cat noisy -> What does the spouse advise", "How -> Who -> Why -> What", "Where -> Where -> Where -> Where", "Why -> Why -> Why -> Why", "A", "Reveals setup, timeline, conflict, and punchline advice."),
        ("Transform the statement into a formal question: 'The irony of pet ownership is humorously exposed at 2 a.m.'", "How does Ogden Nash use the 2 a.m. scenario to highlight the humorous irony of domestic pet choices?", "Where is the cot?", "Who is Nash?", "What is a cat?", "A", "Directly targets humorous irony theme."),
        ("Analyze this ambiguous question: 'What did he get?' How can it be made precise?", "Add specific context: 'What pet did the owner acquire quickly after receiving complaints about mice?'", "Make it shorter: 'What get?'", "Change to: 'Where get?'", "Remove 'What'.", "A", "Adding specific context clarifies which acquisition."),
        ("Choose the correct question pair for dialogue: Owner: '___ is the cat meowing outside?' Spouse: '___ about getting another mouse instead?'", "Why, How", "Who, Where", "Where, How", "When, Whose", "A", "Why (reason for meowing), How about (suggestion)."),
        ("Spot the DOUBLE auxiliary error: 'Why did the spouse suggested another mouse?'", "'did' requires base verb 'suggest', not past tense 'suggested'.", "'did' should be 'was'.", "'Why' should be 'How'.", "No error.", "A", "Auxiliary 'did' must be followed by base form of verb ('suggest')."),
        ("Reconstruct question from answer: Answer: 'At two a.m., the mouse is silent, but the cat is not.'", "Question: 'What contrast is discovered by two a.m.?'", "Question: 'Where did they run?'", "Question: 'Who bought a house?'", "Question: 'Why is day bright?'", "A", "Targets 2 a.m. contrast."),
        ("Form indirect question: 'The owner asked why the cat was making noise.' What is the sentence type?", "Assertive statement containing an embedded indirect question.", "Direct question requiring question mark.", "Exclamatory sentence.", "Command.", "A", "Indirect questions are statements ending with full stop."),
        ("Identify the correct question word for moral reasoning: '___ is humor effective in describing everyday domestic situations?'", "Why", "What", "Who", "Where", "A", "'Why' inquires into the literary effectiveness of humor."),
        ("HOTS Reasoning: Why is 'Who' used for the spouse but 'Which' used when selecting between a cat and a mouse?", "'Who' is used for human spouse; 'Which' is used when choosing between specific animal options.", "'Who' is for inanimate objects.", "'Which' is only for numbers.", "Both are identical.", "A", "'Which of the two animals...' selects from options."),
        ("Correct all errors in: 'why is the cat outside at two am in the poem'", "Why is the cat outside at two a.m. in the poem?", "Why is the cat outside at two am in the poem.", "Whom is the cat outside?", "Why does the cat outside at two am?", "A", "Capital W, lowercase dotted a.m., question mark at end."),
        ("Select the question that evaluates Higher Order Thinking (HOTS) about Chapter 12:", "How does Ogden Nash use reversal of expectations (silent mouse vs noisy cat) to create comedic effect in 'The Cat'?", "What animal meows?", "Where is the cot?", "Who wrote the poem?", "A", "Asks student to evaluate comedic irony and reversal of expectations.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH12_CAT07_Q{idx:02d}"
        qtxt = f"Higher Order Interrogative Analysis & Syntax:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Question Syntax & Analytical Framing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 8. Present Continuous Tense (-ing) (50 Qs)
# ---------------------------------------------------------------------------
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense (-ing) — Chapter 12: The Cat\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_ing = [
        ("The owner is **getting** a new house.", "getting", "owner", "is", "house", "A", "'getting' is verb + -ing form."),
        ("The mouse is **entering** the house quietly.", "entering", "mouse", "is", "house", "A", "'entering' is verb + -ing form."),
        ("The cat is **meowing** outside at 2 a.m.", "meowing", "cat", "is", "night", "A", "'meowing' is verb + -ing form."),
        ("It is **dawning** upon the owner in his cot.", "dawning", "owner", "is", "cot", "A", "'dawning' is verb + -ing form."),
        ("The spouse is **saying** that they need a mouse.", "saying", "spouse", "is", "mouse", "A", "'saying' is verb + -ing form."),
        ("The cat is **staying** outside the house.", "staying", "cat", "is", "house", "A", "'staying' is verb + -ing form."),
        ("The mouse is **staying** silent in the corner.", "staying", "mouse", "is", "corner", "A", "'staying' is verb + -ing form."),
        ("The cat is **making** noise in the middle of the night.", "making", "cat", "is", "night", "A", "'making' is verb + -ing form."),
        ("The owner is **lying** awake in his cot.", "lying", "owner", "is", "cot", "A", "'lying' is verb + -ing form."),
        ("The cat is **chasing** shadows outdoors.", "chasing", "cat", "is", "outdoors", "A", "'chasing' is verb + -ing form."),
        ("The spouse is **suggesting** a different pet.", "suggesting", "spouse", "is", "pet", "A", "'suggesting' is verb + -ing form."),
        ("The mouse is **moving** silently across the floor.", "moving", "mouse", "is", "floor", "A", "'moving' is verb + -ing form."),
        ("The owner is **listening** to the cat's meows.", "listening", "owner", "is", "meows", "A", "'listening' is verb + -ing form."),
        ("The cat is **pacing** back and forth outside.", "pacing", "cat", "is", "outside", "A", "'pacing' is verb + -ing form."),
        ("The mouse is **hiding** under the cabinet.", "hiding", "mouse", "is", "cabinet", "A", "'hiding' is verb + -ing form."),
        ("The clock is **striking** two a.m.", "striking", "clock", "is", "a.m.", "A", "'striking' is verb + -ing form."),
        ("The spouse is **complaining** about the cat.", "complaining", "spouse", "is", "cat", "A", "'complaining' is verb + -ing form."),
        ("The cat is **scratching** at the back door.", "scratching", "cat", "is", "door", "A", "'scratching' is verb + -ing form.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_ing, start=1):
        qid = f"BK02_CH12_CAT08_Q{idx:02d}"
        qtxt = f"Identify the **present continuous (-ing) verb** in this sentence:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the present continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Present Continuous Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("What is the correct -ing spelling rule for **'get'**? (You are ____ a kitty.)", "getting (double final consonant)", "geting", "gettting", "geteing", "A", "CVC rule: double final consonant before -ing (getting)."),
        ("What is the correct -ing spelling rule for **'make'**? (The cat is ____ noise.)", "making (drop final silent e)", "makeing", "makking", "makng", "A", "Drop final silent 'e' before adding -ing (making)."),
        ("What is the correct -ing spelling rule for **'lie'**? (The owner is ____ in his cot.)", "lying (-ie changes to -y + ing)", "lieing", "liying", "ling", "A", "-ie changes to -y before adding -ing (lying)."),
        ("Fill in the blank with present continuous form: 'The cat (meow) ____ outside right now.'", "is meowing", "was meow", "are meow", "is meowed", "A", "Singular subject takes 'is meowing'."),
        ("Choose the sentence in PRESENT CONTINUOUS tense:", "The cat is making noise outside right now.", "The cat made noise outside last night.", "The cat will make noise outside tomorrow.", "The cat made noise yesterday.", "A", "'is making' is present continuous."),
        ("Fill in the blanks: 'The mouse ____ (enter), and the cat ____ (go) out.' ", "is entering, is going", "are entering, are going", "is enter, is go", "was entering, were going", "A", "Singular 'mouse' takes 'is entering'; singular 'cat' takes 'is going'."),
        ("Identify the spelling mistake in: 'The cat is **makeing** noise.'", "'makeing' should be 'making'", "'makeing' should be 'making'", "'is' should be 'are'", "No mistake", "A", "Make drops silent e before -ing (making)."),
        ("Select the correct -ing form for **'chase'**:", "chasing", "chaseing", "chasring", "chasng", "A", "Drop silent 'e': chase -> chasing."),
        ("Which sentence describes an action HAPPENING RIGHT NOW?", "Listen! The cat is meowing outside the window.", "The cat meowed outside yesterday.", "The cat meows every night.", "The cat will meow tomorrow.", "A", "Present continuous ('is meowing') describes ongoing action right now."),
        ("Fill in the blank: 'I ____ (read) Ogden Nash's poem about the cat.'", "am reading", "is reading", "are reading", "am readeing", "A", "Subject 'I' takes 'am reading'."),
        ("Choose the correct form: 'The mouse ____ (remain) completely silent.'", "is remaining", "are remaining", "am remaining", "is remain", "A", "Singular subject 'mouse' takes 'is remaining'."),
        ("Identify the verb in: 'Why are you getting a cat?'", "are getting", "Why", "you", "cat", "A", "Helping verb 'are' + main verb 'getting' form present continuous."),
        ("What is the -ing form of **'dawn'**?", "dawning", "dawnning", "dawneing", "dawnng", "A", "Regular verb adding -ing (dawning)."),
        ("What is the -ing form of **'move'**?", "moving", "moveing", "movving", "movng", "A", "Drop silent e: move -> moving."),
        ("Change simple present to continuous: 'The cat meows.' -> 'The cat ____.'", "is meowing", "meowed", "was meowing", "will meow", "A", "is meowing."),
        ("Fill in the blank: 'The spouse ____ (suggesting) a different pet.'", "is suggesting", "are suggesting", "am suggesting", "suggested", "A", "is suggesting."),
        ("Identify the correct present continuous sentence:", "Look! The cat is jumping over the fence.", "Look! The cat jumps over the fence.", "Look! The cat jumped over the fence.", "Look! The cat jumping over the fence.", "A", "Exclamation 'Look!' introduces action happening now ('is jumping')."),
        ("Select the correct -ing form for **'get'**:", "getting", "geting", "gettting", "geteing", "A", "Double final t: get -> getting.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH12_CAT08_Q{idx:02d}"
        qtxt = f"Present Continuous Grammar & Spelling Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Present Continuous Formation & Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze spelling rules for adding -ing to verbs: Group them correctly: (get, make, lie)", "get -> getting (double consonant), make -> making (drop e), lie -> lying (-ie to -y)", "All just add -ing.", "All double the last letter.", "get -> geting, make -> makeing, lie -> lieing", "A", "3 distinct orthographic rules for -ing derivation."),
        ("Convert past tense narrative to present continuous picture scene: 'The mouse entered while the cat meowed.'", "The mouse is entering while the cat is meowing.", "The mouse entering while the cat meowing.", "The mouse was entering while the cat meowed.", "The mouse will enter while the cat meows.", "A", "Both verbs transformed to present continuous (is entering, is meowing)."),
        ("Spot the missing auxiliary verb in: 'The mouse entering house and cat meowing outside.' Correct it:", "'The mouse **is** entering the house and cat **is** meowing outside.'", "'The mouse entering house and cat meowing outside.'", "'The mouse **are** entering and cat **are** meowing.'", "No error.", "A", "Present continuous requires auxiliary (is/am/are) before -ing verb."),
        ("Differentiate state vs action: Why don't we usually say 'The mouse is **having** silence'?", "Because 'have' expressing state/condition is stative, preferring 'The mouse is silent'.", "Because 'having' is hard to spell.", "Because mouse is small.", "Because cat is outside.", "A", "Stative verbs preferring simple/adjective state."),
        ("Identify the sentence with CORRECT present continuous subject-verb agreement:", "The cats outside the house are meowing loudly.", "The cats outside the house is meowing loudly.", "The cats outside the house am meowing loudly.", "The cats outside the house meowing loudly.", "A", "Plural subject ('cats') takes plural auxiliary 'are'."),
        ("Form negative present continuous: 'The cat is sleeping quietly tonight.' -> Negative:", "The cat is **not** sleeping quietly tonight.", "The cat not sleeping quietly tonight.", "The cat are no sleeping quietly tonight.", "The cat isn't sleep quietly tonight.", "A", "Add 'not' between auxiliary 'is' and main verb 'sleeping'."),
        ("Spot all THREE spelling errors: 'He is **geting** a cat, **makeing** noise, and **lieing** in bed.'", "'geting' -> 'getting'; 'makeing' -> 'making'; 'lieing' -> 'lying'", "'geting' -> 'geting'; 'makeing' -> 'makking'; 'lieing' -> 'lieing'", "No errors.", "Only 'geting' is wrong.", "A", "getting (double t), making (drop e), lying (-ie to -y)."),
        ("Rewrite as interrogative present continuous: 'The spouse is complaining at two a.m.'", "**Is** the spouse complaining at two a.m.?", "Are the spouse complaining at two a.m.?", "The spouse complaining at two a.m.?", "Why the spouse is complaining at two a.m.?", "A", "Move auxiliary 'Is' to beginning of sentence."),
        ("Analyze action timeline: 'We **are adopting** another mouse tomorrow.' What does present continuous express here?", "A fixed future arrangement / planned action.", "Past completed action.", "Action that happened long ago.", "Uncertain rumor.", "A", "Present continuous can express planned future actions."),
        ("Choose the sentence showing PARALLEL present continuous actions:", "While the mouse is entering, the cat is going outside.", "While mouse entered, cat is going.", "Mouse is entering while cat went.", "Mouse enter while cat go.", "A", "Both parallel ongoing actions use present continuous."),
        ("Correct the error: 'The cat is meowwing outside.'", "'meowwing' should be 'meowing' (single 'w').", "'is' should be 'are'.", "'outside' should be capitalized.", "No error.", "A", "Meow + ing = meowing."),
        ("HOTS Reasoning: Compare 'The cat meowed' (Past Simple) vs 'The cat is meowing' (Present Continuous). How does the meaning change?", "Past simple states a completed past event; present continuous describes an action currently in progress.", "Both mean the exact same thing.", "Past simple is for future; continuous is for past.", "Continuous means cat went away.", "A", "Tense changes temporal aspect (completed vs ongoing)."),
        ("Form question: 'Why ____ the cat ____ (making) noise at 2 a.m.?'", "is, making", "are, making", "am, making", "do, making", "A", "Singular subject cat takes 'is ... making'."),
        ("Identify the correct present continuous sentence describing comedic action:", "The cat is creating chaos outside while the mouse is resting inside.", "The cat is create chaos outside while the mouse is rest inside.", "The cat are creating chaos outside while the mouse are resting inside.", "The cat creating chaos outside while the mouse resting inside.", "A", "Singular subjects + is + -ing verbs.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH12_CAT08_Q{idx:02d}"
        qtxt = f"Higher Order Present Continuous Analysis & Editing:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Continuous Tense Aspect & Error Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 9. Helping Verbs (Is, Am, Are) (50 Qs)
# ---------------------------------------------------------------------------
def build_helping_verbs():
    header = "# Category 9: Helping Verbs (Is, Am, Are) — Chapter 12: The Cat\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_hv = [
        ("The mouse ___ in, the cat is out.", "is", "are", "am", "be", "A", "Singular subject 'The mouse' takes 'is'."),
        ("The cat ___ out of the house.", "is", "are", "am", "be", "A", "Singular subject 'The cat' takes 'is'."),
        ("I ___ lying awake in my cot.", "am", "is", "are", "be", "A", "Pronoun 'I' takes 'am'."),
        ("The mouse ___ silent in the room.", "is", "are", "am", "be", "A", "Singular subject 'mouse' takes 'is'."),
        ("The cat ___ not silent at two a.m.", "is", "are", "am", "be", "A", "Singular subject 'cat' takes 'is'."),
        ("The mouse and the cat ___ two animals in the poem.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("The spouse ___ speaking from the cot.", "is", "are", "am", "be", "A", "Singular subject takes 'is'."),
        ("The cats ___ noisy outside at night.", "are", "is", "am", "be", "A", "Plural subject 'cats' takes 'are'."),
        ("I ___ getting another mouse tomorrow.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The owner ___ awake at two a.m.", "is", "are", "am", "be", "A", "Singular 'owner' takes 'is'."),
        ("The pets ___ creating a comedy at night.", "are", "is", "am", "be", "A", "Plural 'pets' takes 'are'."),
        ("Ogden Nash ___ a famous humorous poet.", "is", "are", "am", "be", "A", "Singular subject takes 'is'."),
        ("You ___ reading a funny poem.", "are", "is", "am", "be", "A", "Pronoun 'You' always takes 'are'."),
        ("The husband ___ listening to his wife.", "is", "are", "am", "be", "A", "Singular 'husband' takes 'is'."),
        ("The mice ___ quiet inside the house.", "are", "is", "am", "be", "A", "Irregular plural 'mice' takes 'are'."),
        ("I ___ amused by Ogden Nash's poem.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The house ___ full of surprises.", "is", "are", "am", "be", "A", "Singular 'house' takes 'is'."),
        ("The two a.m. hours ___ noisy with cat meows.", "are", "is", "am", "be", "A", "Plural 'hours' takes 'are'.")
    ]
    
    for idx, (sent_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_hv, start=1):
        qid = f"BK02_CH12_CAT09_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct helping verb (is / am / are):\n\n\"{sent_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Helping Verb Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Choose the correct helping verb: 'The cat and the mouse ____ in different locations at 2 a.m.'", "are", "is", "am", "be", "A", "Compound subject ('The cat and the mouse') is plural, taking 'are'."),
        ("Select the sentence with CORRECT helping verb agreement:", "The mouse is silent, the cat is not.", "The mouse are silent, the cat are not.", "The mouse am silent, the cat am not.", "The mouse be silent, the cat be not.", "A", "Singular subjects 'The mouse' and 'the cat' require 'is'."),
        ("Fill in the blanks: 'I ____ awake in bed, and my cat ____ meowing outside.'", "am, is", "is, is", "are, is", "am, are", "A", "'I am', 'my cat is'."),
        ("Identify the mistake in: 'The mice inside the kitchen **is** silent.'", "'is' should be 'are' because 'mice' is a plural noun.", "'is' should be 'am'", "'is' should be 'was'", "No mistake", "A", "'mice' is plural, requiring 'are'."),
        ("Which helping verb completes the question? '____ you awake at two a.m.?'", "Are", "Is", "Am", "Be", "A", "Subject 'you' takes 'Are'."),
        ("Fill in the blank: 'Neither mouse nor cat ____ staying in the same room.'", "is", "are", "am", "be", "A", "'Neither...nor' with singular second subject 'cat' takes 'is'."),
        ("Select the correct sentence for poem moral:", "Humor and comedy are found in everyday life.", "Humor and comedy is found in everyday life.", "Humor and comedy am found in everyday life.", "Humor and comedy be found in everyday life.", "A", "Compound subject 'Humor and comedy' takes 'are'."),
        ("Complete the conversation: Husband: 'Where ____ the cat?' Wife: 'It ____ outside!'", "is, is", "are, are", "is, are", "are, is", "A", "Singular 'the cat' -> is; singular 'It' -> is."),
        ("Identify where 'is' is used incorrectly:", "The mice **is** silent.", "The cat is noisy.", "The house is quiet.", "The spouse is awake.", "A", "'The mice is' should be 'The mice are'."),
        ("Choose the correct helping verb for collective noun used as a single unit: 'The pair of pets ____ causing confusion.'", "is", "are", "am", "be", "A", "Collective noun 'pair' treated as singular unit takes 'is'."),
        ("Fill in the blank: 'The advice from the spouse ____ clear.'", "is", "are", "am", "be", "A", "Uncountable singular 'advice' takes 'is'."),
        ("Select the sentence with correct helping verb for 'I':", "I am lying in my cot at two a.m.", "I is lying in my cot at two a.m.", "I are lying in my cot at two a.m.", "I be lying in my cot at two a.m.", "A", "Subject 'I' takes 'am'."),
        ("Fill in the blank: 'There ____ two animals in the poem.'", "are", "is", "am", "be", "A", "'There are' before plural noun 'two animals'."),
        ("Fill in the blank: 'There ____ a funny line in the last stanza.'", "is", "are", "am", "be", "A", "'There is' before singular noun 'a funny line'."),
        ("Choose the correct sentence:", "What are the cats doing at two a.m.?", "What is the cats doing at two a.m.?", "What am the cats doing at two a.m.?", "What be the cats doing at two a.m.?", "A", "Plural subject 'the cats' takes 'are'."),
        ("Identify the correct form: 'The cat, as well as the mouse, ____ acting unpredictably.'", "is", "are", "am", "be", "A", "Subject is singular 'The cat' ('as well as...' does not change subject number), taking 'is'."),
        ("Fill in the blank: 'Both the husband and the wife ____ awake.'", "are", "is", "am", "be", "A", "'Both ... and ...' takes plural verb 'are'."),
        ("Select the option with correct helping verbs: 'The mouse ____ inside, but the cat ____ outside.'", "is, is", "are, is", "am, are", "is, are", "A", "'mouse is', 'cat is'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH12_CAT09_Q{idx:02d}"
        qtxt = f"Helping Verb Subject-Verb Agreement Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Subject-Verb Agreement Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze subject-verb agreement: 'Each of the cats **____** meowing at night.' Choose the correct verb and reason:", "is — because 'Each' is a singular indefinite pronoun requiring singular verb 'is'.", "are — because 'cats' is plural.", "am — because it refers to speaker.", "be — because cats are loud.", "A", "'Each' is singular indefinite pronoun taking singular verb 'is'."),
        ("Spot the subtle agreement error in: 'A pair of noisy cats **are** disturbing the peace.'", "'are' should be 'is' because the subject is singular noun 'pair'.", "'are' should be 'am'.", "'cats' should be 'cat'.", "No error.", "A", "'A pair' is singular, so it requires 'is disturbing'."),
        ("Compare: (1) 'The cat and the mouse **are** in the poem.' vs (2) 'The cat, along with the mouse, **is** in the poem.' Why are the verbs different?", "In (1), 'and' creates a plural subject (are); in (2), 'along with' is a prepositional phrase, leaving 'The cat' as sole singular subject (is).", "They mean different things.", "Sentence (2) is grammatically wrong.", "Both should use 'are'.", "A", "Prepositional phrases like 'along with' do not change subject number."),
        ("Identify the correct agreement for indefinite pronouns: 'Everyone in the house **____** awake at two a.m.'", "is", "are", "am", "be", "A", "'Everyone' is a singular indefinite pronoun requiring 'is'."),
        ("Spot all THREE subject-verb errors in: 'The mice **is** silent, I **is** awake, and the cats **is** noisy.'", "'mice is' -> 'mice are'; 'I is' -> 'I am'; 'cats is' -> 'cats are'", "'mice is' -> 'mice am'; 'I is' -> 'I are'; 'cats is' -> 'cats am'", "Only 'I is' is wrong.", "No errors present.", "A", "mice are (plural), I am (1st person), cats are (plural)."),
        ("Fill in the blanks in this complex sentence: 'Not only the mouse but also the cats **____** active, while the spouse **____** speaking.'", "are, is", "is, are", "is, is", "are, are", "A", "'Not only...but also' agrees with closer plural subject ('cats' -> are); 'spouse' -> is."),
        ("Transform to negative: 'The cat is silent.'", "The cat **is not** silent.", "The cat are not silent.", "The cat am not silent.", "The cat no silent.", "A", "Add 'not' after singular helping verb 'is'."),
        ("Analyze inverted subject position: 'In the middle of the night **____** standing a noisy cat.'", "is", "are", "am", "be", "A", "Subject is singular 'a noisy cat', appearing after verb, requiring 'is'."),
        ("Determine agreement with uncountable nouns: 'The noise from the cat **____** disturbing.'", "is", "are", "am", "be", "A", "Uncountable noun 'noise' is treated as singular, taking 'is'."),
        ("Correct the sentence: 'Here **is** the words of the spouse.'", "Here **are** the words of the spouse.", "Here am the words of the spouse.", "Here be the words of the spouse.", "No error.", "A", "Plural subject 'words' requires 'Here are...''"),
        ("Identify the sentence where 'is' acts as a MAIN linking verb rather than a helping verb:", "The mouse **is** silent.", "The cat **is** meowing outside.", "The owner **is** listening to the noise.", "The spouse **is** talking in bed.", "A", "In 'The mouse is silent', 'is' is the main linking verb connecting subject to predicate adjective."),
        ("HOTS Reasoning: Why does English use 'am' ONLY with the subject pronoun 'I'?", "Because 'am' is the unique 1st person singular present indicative form of the verb 'to be'.", "Because 'I' is capitalized.", "Because mouse is small.", "There is no reason.", "A", "'am' is exclusively reserved for 1st person singular 'I'."),
        ("Fill in the blanks: 'Neither cat nor mouse **____** sleeping, because the night **____** noisy.'", "is, is", "are, is", "is, are", "are, are", "A", "'mouse' is singular closer subject -> is; 'night' -> is."),
        ("Select the option with PERFECT helping verb agreement throughout:", "The mouse is silent, I am awake, and the cats are noisy.", "The mouse are silent, I is awake, and the cats is noisy.", "The mouse am silent, I are awake, and the cats am noisy.", "The mouse is silent, I is awake, and the cats is noisy.", "A", "mouse is (singular), I am (1st person), cats are (plural).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH12_CAT09_Q{idx:02d}"
        qtxt = f"Higher Order Helping Verb Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Subject-Verb Agreement & Syntax", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# MAIN EXECUTION FOR REBUILDING CHAPTER 12
# ---------------------------------------------------------------------------
def rebuild_chapter_12():
    print("Rebuilding Chapter 12 category files with high-quality, multi-tiered (Easy/Medium/Hard) non-duplicate questions...")

    files_and_generators = [
        ("plural_nouns_spelling.md", build_plural_nouns),
        ("articles_grammar.md", build_articles_grammar),
        ("calendar_days_vocabulary.md", build_calendar_days),
        ("action_verbs_identification.md", build_action_verbs),
        ("punctuation_marks.md", build_punctuation_marks),
        ("phonics_vowel_digraphs.md", build_phonics_digraphs),
        ("question_words_interrogatives.md", build_question_words),
        ("present_continuous_ing.md", build_present_continuous),
        ("helping_verbs_is_am_are.md", build_helping_verbs)
    ]

    for fname, gen_func in files_and_generators:
        filepath = os.path.join(CH12_DIR, fname)
        print(f"  Generating {fname}...")
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {fname} created successfully.")

    print("\n[SUCCESS] Completed rebuilding all 9 category files for Chapter 12 (450 total high-quality questions)!")

if __name__ == "__main__":
    rebuild_chapter_12()
