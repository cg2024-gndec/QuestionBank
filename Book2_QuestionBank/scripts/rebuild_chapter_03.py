r"""
=============================================================================
Script: rebuild_chapter_03.py
Description: Generates 50 rich, non-duplicate, multi-tiered (Easy, Medium, Hard)
             questions for each of the 9 category files in Chapter 03:
             "The Turtle and the Swans" (450 Qs total).
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH03_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_03")
os.makedirs(CH03_DIR, exist_ok=True)

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
    header = "# Category 1: Plural Nouns & Spelling Rules — Chapter 03: The Turtle and the Swans\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("turtle", "turtles", "turtlies", "turtlese", "turtlez", "A", "Regular noun adding -s."),
        ("swan", "swans", "swanes", "swanies", "swanz", "A", "Regular noun adding -s."),
        ("lake", "lakes", "lakies", "lakees", "lakez", "A", "Regular noun ending in -e adds -s."),
        ("friend", "friends", "friendes", "friendies", "friendz", "A", "Regular noun adding -s."),
        ("stick", "sticks", "stickes", "stickies", "stickz", "A", "Regular noun adding -s."),
        ("beak", "beaks", "beakes", "beakies", "beakz", "A", "Regular noun adding -s."),
        ("mouth", "mouths", "mouthes", "mouthies", "mouthz", "A", "Regular noun adding -s."),
        ("voice", "voices", "voicies", "voicees", "voicez", "A", "Regular noun ending in -e adds -s."),
        ("town", "towns", "townes", "townies", "townz", "A", "Regular noun adding -s."),
        ("village", "villages", "villagies", "villagese", "villagz", "A", "Regular noun ending in -e adds -s."),
        ("bird", "birds", "birdes", "birdies", "birdz", "A", "Regular noun adding -s."),
        ("sound", "sounds", "soundes", "soundies", "soundz", "A", "Regular noun adding -s."),
        ("place", "places", "placies", "placees", "placez", "A", "Regular noun ending in -e adds -s."),
        ("feather", "feathers", "featheres", "featheries", "featherz", "A", "Regular noun adding -s."),
        ("wing", "wings", "winges", "wingies", "wingz", "A", "Regular noun adding -s."),
        ("person", "people", "persons", "peoples", "persones", "A", "Irregular plural: person becomes people."),
        ("foot", "feet", "foots", "feets", "footes", "A", "Irregular plural: foot becomes feet."),
        ("leaf", "leaves", "leafs", "leafes", "leavs", "A", "Nouns ending in -f change to -ves.")
    ]
    
    for idx, (word, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH03_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{word}'** from or related to Chapter 03 (*The Turtle and the Swans*)?"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Plural Noun Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The turtle had two (swan / swans) as his best friends.", "swans", "swan", "swanes", "swanies", "A", "'two' requires plural noun 'swans'."),
        ("The swans held both (end / ends) of the stick.", "ends", "end", "endes", "endies", "A", "'both' requires plural 'ends'."),
        ("The swans opened their (beak / beaks) to hold the stick.", "beaks", "beak", "beakes", "beakies", "A", "'beaks' is the plural form."),
        ("Identify the INCORRECT plural spelling in this list: lakes, turtles, villagies, towns.", "villagies", "lakes", "turtles", "towns", "A", "Plural of village is 'villages', not 'villagies'."),
        ("Choose the sentence with the correct plural noun form:", "Many people watched the swans flying.", "Many persons watched the swans flying.", "Many peoples watched the swans flying.", "Many person watched the swans flying.", "A", "Plural of person in standard context is 'people'."),
        ("Which noun forms its plural by changing -f to -ves?", "leaf -> leaves", "turtle -> turtles", "lake -> lakes", "swan -> swans", "A", "Leaf ends in -f, so plural is leaves."),
        ("Change the singular noun in brackets to plural: 'The swans spread their ____ (wing).'", "wings", "winges", "wingies", "wingz", "A", "Plural of wing is wings."),
        ("Select the sentence where ALL plural nouns are spelt correctly:", "The turtles lived near the lakes.", "The turtlex lived near the lakes.", "The turtles lived near the lakies.", "The turtlees lived near the lakes.", "A", "turtles, lakes are both correctly spelt plurals."),
        ("What is the correct plural of 'voice'?", "voices", "voicies", "voicees", "voicez", "A", "Regular noun adding -s."),
        ("The turtle spent many (day / days) talking near the lake.", "days", "daies", "day", "dayes", "A", "Vowel + y adds -s (days)."),
        ("The swans flew over many green (tree / trees).", "trees", "treess", "treies", "treez", "A", "Plural of tree is trees."),
        ("The villagers looked up with their (eye / eyes) wide open.", "eyes", "eyess", "eyies", "eyez", "A", "Plural of eye is eyes."),
        ("How many (problem / problems) did the friends face during summer?", "problems", "problem", "problemes", "problemies", "A", "Plural noun 'problems'."),
        ("The two swans were good (friend / friends).", "friends", "friendes", "friend", "friendies", "A", "Plural of friend is friends."),
        ("Which plural noun rule applies to the word **'cities'**?", "Consonant + y changes to -ies", "Add -es to -x", "Add -s to vowel + y", "Change -f to -ves", "A", "City ends in consonant + y, so y becomes -ies."),
        ("The turtle ignored many (advice / pieces of advice).", "pieces of advice", "advices", "advicess", "advicies", "A", "'advice' is uncountable; plural expression is 'pieces of advice'."),
        ("Identify the correct plural form of 'child':", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("The swans carried two short (stick / sticks).", "sticks", "stickes", "stick", "stickies", "A", "Regular noun adding -s.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH03_CAT01_Q{idx:02d}"
        qtxt = f"Contextual Plural Rule Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Plural Noun Application", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Rewrite the sentence in PLURAL form: 'The swan held a stick near the lake.'", "The swans held sticks near the lakes.", "The swanes held stickes near the lakies.", "The swans held stick near the lakes.", "The swan held sticks near the lakez.", "A", "Plural of swan->swans, stick->sticks, lake->lakes."),
        ("Analyze the error: 'The turtle loved to listen to his own voices.' Why is 'voices' wrong here?", "'voice' refers to the turtle's single voice, so singular 'voice' should be used.", "'voices' should be 'voicies'.", "'voices' should be 'voicees'.", "No error.", "A", "An individual person/animal has one single voice."),
        ("Complete the paragraph with correct plurals: 'The two ____ (swan) flew over three ____ (village) carrying two wooden ____ (stick).'", "swans, villages, sticks", "swanes, villagies, stickes", "swans, village, stick", "swanes, villages, sticks", "A", "swans (-s), villages (-e + s), sticks (-s)."),
        ("Identify the sentence where ALL three underlined nouns are correctly pluralized:", "The **swans** carried the **turtles** over the **towns**.", "The **swanes** carried the **turtlex** over the **towns**.", "The **swans** carried the **turtles** over the **townies**.", "The **swanees** carried the **turtles** over the **towns**.", "A", "swans (-s), turtles (-s), towns (-s)."),
        ("Which group contains ONLY irregular plural nouns?", "people, feet, teeth, children", "turtles, swans, lakes, sticks", "cities, bodies, stories, armies", "leaves, thieves, wolves, knives", "A", "people, feet, teeth, children change forms without standard -s/-es."),
        ("Why does 'day' become 'days' but 'story' becomes 'stories'?", "Because 'day' has a vowel before y (a+y -> -s), while 'story' has a consonant before y (r+y -> -ies).", "Because 'day' is short and 'story' is long.", "Because 'day' is time and 'story' is text.", "Both follow the exact same rule.", "A", "Vowel+y adds -s; Consonant+y changes y to -ies."),
        ("Find the TWO grammatical mistakes in: 'The two swanes saw many mouses near the lake.'", "'swanes' should be 'swans' and 'mouses' should be 'mice'.", "'swanes' should be 'swan' and 'mouses' should be 'mices'.", "'lake' should be 'lakes' only.", "There are no mistakes in the sentence.", "A", "swans (regular -s) and mice (irregular plural)."),
        ("Replace the singular words in brackets: 'The swan had white ____ (feather) and black ____ (foot).'", "feathers, feet", "featheres, foots", "feathers, feets", "featheries, foots", "A", "Plural of feather is feathers, plural of foot is feet."),
        ("Analyze this sentence: 'The swans gave good advice.' Can 'advice' be pluralized as 'advices'?", "No, 'advice' is an uncountable noun; we say 'pieces of advice' for plural.", "Yes, 'advices' is correct.", "No, it becomes 'advicess'.", "Yes, 'an advice' is correct.", "A", "Advice is an uncountable noun."),
        ("Fill in the blanks: 'The two ____ (swan) held the ____ (end) of the stick.'", "swans, ends", "swanes, endes", "swans, endies", "swanes, ends", "A", "swan -> swans; end -> ends."),
        ("Select the option that shows correct plural transformation for ALL three words: 'goose', 'city', 'fox'", "geese, cities, foxes", "gooses, citys, foxs", "geese, cityes, foxies", "gooses, cities, foxen", "A", "goose -> geese; city -> cities; fox -> foxes."),
        ("HOTS Reasoning: Why do we say 'water is essential' rather than 'waters are essential'?", "Because 'water' is an uncountable material noun that stays singular.", "Because water is in the lake.", "Because swans fly.", "Because turtle drowned.", "A", "Uncountable material nouns take singular verbs."),
        ("Transform into singular: 'The swans flew over the lakes with the sticks.'", "The swan flew over the lake with the stick.", "The swans flew over the lake with the stick.", "The swan fly over the lake with the stick.", "The swan flew over the lakes with the stick.", "A", "Singular forms: swan, lake, stick."),
        ("Identify the correct rule for forming the plural of **'beak'**:", "Add -s because it is a regular noun ending in a consonant (beaks).", "Add -es (beakes).", "Change -k to -ves (beavs).", "Change vowel sound.", "A", "Regular noun adding -s.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH03_CAT01_Q{idx:02d}"
        qtxt = f"Higher Order Thinking Skills (HOTS) & Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Plural & Spelling Analysis", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 2. Articles Grammar (50 Qs)
# ---------------------------------------------------------------------------
def build_articles_grammar():
    header = "# Category 2: Articles (A, An, The) — Chapter 03: The Turtle and the Swans\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("Once upon a time, there lived ___ turtle near a lake.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'turtle'."),
        ("The turtle had ___ pair of swans as best friends.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'pair'."),
        ("During summer, ___ lake started drying up.", "the", "a", "an", "no article", "A", "Use 'the' for specific lake mentioned in story."),
        ("The swans found ___ bigger lake far away.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'bigger'."),
        ("The swans held ___ stick in their beaks.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'stick'."),
        ("___ Panchatantra story teaches us to think before speaking.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'Panchatantra'."),
        ("The turtle was ___ talkative animal.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'talkative'."),
        ("The swans gave ___ important warning to the turtle.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'important'."),
        ("___ turtle fell to his death because he spoke.", "The", "A", "An", "No article", "A", "Use 'The' for specific turtle in story."),
        ("The villagers saw ___ amazing sight in the sky.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'amazing'."),
        ("It was ___ hot cloudless summer.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'hot'."),
        ("The turtle held the middle of ___ stick.", "the", "a", "an", "no article", "A", "Use 'the' for specific stick."),
        ("___ sun shone brightly over the lake.", "The", "A", "An", "No article", "A", "Use 'The' for unique celestial object 'sun'."),
        ("The turtle gave ___ foolish response.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'foolish'."),
        ("The swans came up with ___ clever idea.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'clever'."),
        ("The turtle was ___ honest friend but too talkative.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' sound in 'honest'."),
        ("The villagers looked up in ___ awe.", "no article", "a", "an", "the", "A", "Abstract noun 'awe' in prepositional phrase takes no article ('in awe')."),
        ("___ swans flew smoothly in the air.", "The", "A", "An", "No article", "A", "Use 'The' for specific pair of swans.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH03_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article (a / an / the / no article):\n\n\"{q_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Basic Article Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The swans warned ___ turtle not to open his mouth, but ___ turtle forgot.", "the, the", "a, an", "an, a", "a, the", "A", "Both turtle mentions refer to the specific turtle in the story."),
        ("Why do we say '**a** turtle' but '**an** eagle'?", "Because 'turtle' begins with a consonant sound (t) and 'eagle' with a vowel sound (e).", "Because turtles swim.", "Because eagles fly higher.", "Because swans live in lakes.", "A", "Article selection depends on initial vowel/consonant sound."),
        ("Select the sentence with CORRECT article usage:", "The swans found a new lake and a wooden stick.", "The swans found an new lake and an wooden stick.", "The swans found the a new lake.", "The swans found a an wooden stick.", "A", "'a new' (/n/) and 'a wooden' (/w/) both take 'a'."),
        ("Fill in the blanks: 'The turtle grabbed ___ middle of ___ stick.'", "the, the", "a, a", "an, an", "a, the", "A", "Both 'middle' and 'stick' are specific in this context."),
        ("Identify the INCORRECT article in: 'The turtle was **an** talkative animal.'", "'an' should be 'a'", "'an' should be 'the'", "'talkative' should be 'an talkative'", "No mistake", "A", "'talkative' starts with consonant sound /t/, so it takes 'a'."),
        ("Which article completes the sentence? 'Flying requires ___ open sky.'", "an", "a", "the", "no article", "A", "'open' starts with vowel sound /o/, requiring 'an'."),
        ("Choose the correct pair of articles: '___ turtle fell from ___ sky.'", "The, the", "A, a", "An, an", "The, a", "A", "'The turtle' (specific turtle in story), 'the sky' (unique environment)."),
        ("Why do we use 'a' before 'bigger lake' in 'They found **a** bigger lake'?", "Because 'bigger' begins with the consonant sound /b/.", "Because lake is large.", "Because bigger is a noun.", "Because swans flew.", "A", "'bigger' starts with consonant sound /b/."),
        ("Complete the dialogue: Swans: 'Hold ___ stick tightly!' Turtle: 'I will not say ___ word!'", "the, a", "a, an", "an, the", "the, the", "A", "'the stick' (specific stick), 'a word' (consonant sound)."),
        ("Select the correct sentence:", "A swan is a graceful bird.", "An swan is a graceful bird.", "The swan is an graceful bird.", "An swan is an graceful bird.", "A", "'A swan' (consonant sound), 'a graceful bird' (consonant sound)."),
        ("Fill in the blank: 'The friends searched for ___ long time before finding the lake.'", "a", "an", "the", "no article", "A", "Idiomatic phrase 'for a long time'."),
        ("Identify where NO article is needed:", "The turtle did not pay **___ attention** to advice.", "They found ___ stick.", "He held ___ stick.", "He saw ___ town.", "A", "Uncountable noun 'attention' in 'pay attention' takes no article."),
        ("Choose the correct sentence for story summary:", "Foolish talkativeness leads to a tragic end.", "A foolish talkativeness leads to an tragic end.", "An foolish talkativeness leads to a tragic end.", "The foolish a talkativeness is bad.", "A", "Abstract concept 'Foolish talkativeness' takes no indefinite article."),
        ("Fill in the blanks: 'The swans spent ___ hour searching for ___ lake.'", "an, a", "a, a", "an, an", "the, an", "A", "'an hour' (silent h), 'a lake' (consonant l)."),
        ("Which sentence uses 'the' correctly for specific environmental features?", "The lake started drying up during the hot summer.", "A lake started drying up during a hot summer.", "An lake started drying up during an hot summer.", "Lake started drying up during summer.", "A", "Specific lake and specific summer season mentioned in narrative take 'the'."),
        ("Identify the article error: 'The turtle gave **a** explanation after **an** long delay.'", "'an long' should be 'a long'", "'a explanation' should be 'an explanation'", "both 'a explanation' -> 'an explanation' and 'an long' -> 'a long'", "No error", "C", "'an explanation' (vowel /e/) and 'a long delay' (consonant /l/)."),
        ("Complete: 'It was ___ unusual flight over ___ small village.'", "an, a", "a, an", "the, the", "an, an", "A", "an unusual (/u/), a small (/s/)."),
        ("Choose the correct option: '___ sun dried up the small lake.'", "The", "A", "An", "No article", "A", "'The sun' (unique celestial body).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH03_CAT02_Q{idx:02d}"
        qtxt = f"Contextual Article Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Article Usage in Context", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze article usage in: 'The turtle paid **a** no attention to **the** advice.' Correct the error:", "'paid a no attention' -> 'paid no attention' (uncountable noun attention takes no article 'a').", "'the advice' -> 'an advice'.", "'paid a no attention' -> 'paid an attention'.", "No error present.", "A", "'attention' is uncountable and takes no article 'a'."),
        ("Fill in all three blanks: '___ swans told ___ turtle that ___ silence was necessary.'", "The, the, no article", "A, an, a", "An, a, the", "The, a, a", "A", "'The swans' (specific), 'the turtle' (specific), 'silence' (general abstract)."),
        ("Identify why 'the' is used in: 'The turtle bit **the** middle of the stick.'", "Because 'the middle' refers to the specific central point of the stick.", "Because middle is a proper noun.", "Because swans flew.", "Because lake was dry.", "A", "'The' specifies the definite part of the stick."),
        ("Spot the TWO article errors: 'It took **a** hour for **a** eagle to fly past the lake.'", "'a hour' should be 'an hour' and 'a eagle' should be 'an eagle'.", "'a hour' should be 'the hour' and 'a eagle' should be 'a eagle'.", "No errors.", "Only 'a hour' is wrong.", "A", "Both 'hour' (silent h) and 'eagle' (vowel e) require 'an'."),
        ("Choose the paragraph with PERFECT article usage throughout:", "A turtle lived near a lake. He had two swans as friends. The lake began to dry in the summer.", "An turtle lived near an lake. He had two swans as friends. A lake began to dry in a summer.", "The turtle lived near an lake. He had two a swans.", "A turtle lived near an lake. The two swans were a friends.", "A", "A turtle (first mention), a lake (first mention), The lake (second mention), the summer."),
        ("Why is it correct to write 'a unique view' but 'an unusual view'?", "Because 'unique' begins with consonant sound /j/ (yoo), while 'unusual' begins with vowel sound /u/.", "Because unique is longer.", "Because view is noun.", "Both take 'an'.", "A", "Sound determines article: /yoo/ is a consonant sound."),
        ("Select the option that correctly completes the story moral: '___ wise person thinks before ___ speech, but ___ foolish person speaks without thinking.'", "A, no article, a", "An, a, an", "The, the, the", "A, a, a", "A", "A wise person, speech (uncountable concept), a foolish person."),
        ("Analyze this sentence: 'The swans flew to **the** new lake.' Why is 'the' appropriate?", "Because it refers to the specific new lake discovered by the swans.", "Because lake is in a town.", "Because lake is plural.", "Because swans fly.", "A", "'the' specifies the definite destination lake."),
        ("Correct the sentence: 'An turtle fell from a sky.'", "A turtle fell from the sky.", "The turtle fell from an sky.", "An turtle fell from the sky.", "A turtle fell from a sky.", "A", "'A turtle' (/t/ sound), 'the sky' (unique environment)."),
        ("Fill in the blanks: '___ water in ___ lake dried up during ___ summer.'", "The, the, the", "A, a, a", "No article, a, an", "An, the, a", "A", "'The water' (specific water), 'the lake' (specific lake), 'the summer' (specific season)."),
        ("Spot the missing article: 'Turtle opened his mouth and fell to ground.'", "Missing 'The' before 'Turtle' -> 'The turtle opened his mouth and fell to the ground.'", "Missing 'a' before 'mouth'", "Missing 'an' before 'opened'", "No article is missing", "A", "Specific subject 'The turtle' and specific surface 'the ground' need 'the'."),
        ("HOTS Reasoning: Which sentence uses 'a', 'an', and 'the' correctly in a single rule demonstration?", "An eagle flew over a tree near the lake.", "A eagle flew over an tree near a lake.", "The eagle flew over an tree near an lake.", "An eagle flew over an tree near the lake.", "A", "An eagle (vowel), a tree (consonant), the lake (specific)."),
        ("Rewrite correctly: 'The turtle was a arrogant creature who made an fatal error.'", "The turtle was an arrogant creature who made a fatal error.", "The turtle was a arrogant creature who made a fatal error.", "The turtle was an arrogant creature who made an fatal error.", "The turtle was the arrogant creature who made an fatal error.", "A", "'an arrogant' (vowel /a/), 'a fatal error' (consonant /f/)."),
        ("Identify the correct rule for using 'the' with unique natural objects (sun, sky, earth):", "Unique natural objects take 'the' because there is only one in context.", "Unique objects take 'an'.", "Unique objects never take articles.", "Unique objects take 'a' only.", "A", "'The sun', 'the sky', 'the earth' take 'the'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH03_CAT02_Q{idx:02d}"
        qtxt = f"Higher Order Article Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Article Analysis & Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 3. Calendar & Days Vocabulary (50 Qs)
# ---------------------------------------------------------------------------
def build_calendar_days():
    header = "# Category 3: Calendar, Days & Abbreviations — Chapter 03: The Turtle and the Swans\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    days_easy = [
        ("The lake dried up during the hot **summer**. Which season comes right after summer?", "Autumn / Fall", "Winter", "Spring", "Monsoon", "A", "Autumn follows summer."),
        ("What is the standard abbreviation for **Wednesday**?", "Wed.", "Weds.", "We.", "W.", "A", "Wed. is standard abbreviation."),
        ("Which day comes right after Thursday?", "Friday", "Saturday", "Wednesday", "Sunday", "A", "Friday follows Thursday."),
        ("What is the abbreviation for **Friday**?", "Fri.", "Frid.", "Fr.", "F.", "A", "Fri. is standard abbreviation."),
        ("If the swans flew for 2 days, how many hours did they travel in total?", "48 hours", "24 hours", "12 hours", "36 hours", "A", "2 days x 24 hours = 48 hours."),
        ("Which month comes right before May?", "April", "March", "June", "July", "A", "April comes before May."),
        ("What is the short abbreviation for **April**?", "Apr.", "Ap.", "Apl.", "Aprl.", "A", "Apr. is standard abbreviation."),
        ("The sun was bright during the **afternoon**. What time of day is 12:00 PM?", "Noon / Midday", "Midnight", "Dawn", "Twilight", "A", "Noon/midday is 12:00 PM."),
        ("What is the abbreviation for **Saturday**?", "Sat.", "Satur.", "Sa.", "St.", "A", "Sat. is standard abbreviation."),
        ("How many months are in a full year?", "12 months", "6 months", "10 months", "14 months", "A", "1 year = 12 months."),
        ("Which hot month comes right after June?", "July", "August", "May", "September", "A", "July comes after June."),
        ("What is the short abbreviation for **July**?", "Jul. / July", "Jl.", "Jy.", "Jly.", "A", "Jul. or July is standard abbreviation."),
        ("If today is Thursday, what day was yesterday?", "Wednesday", "Friday", "Tuesday", "Saturday", "A", "Yesterday was Wednesday."),
        ("If today is Saturday, what day will tomorrow be?", "Sunday", "Friday", "Monday", "Tuesday", "A", "Tomorrow will be Sunday."),
        ("What is the abbreviation for **Sunday**?", "Sun.", "Snd.", "Su.", "Sn.", "A", "Sun. is standard abbreviation."),
        ("Which day comes between Tuesday and Thursday?", "Wednesday", "Friday", "Monday", "Sunday", "A", "Wednesday is between Tuesday and Thursday."),
        ("What is the abbreviation for **May**?", "May", "My.", "Ma.", "M.", "A", "May is short enough to not need truncation (May)."),
        ("Which month comes right before June?", "May", "April", "July", "March", "A", "May comes before June.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(days_easy, start=1):
        qid = f"BK02_CH03_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Vocabulary & Time Concepts:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Days & Calendar Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The lake started drying up in **May**. By **August**, it was completely dry. How many months did the drying process take?", "3 months (May to Aug)", "1 month", "5 months", "2 months", "A", "May to August is 3 months (May-Jun, Jun-Jul, Jul-Aug)."),
        ("The swans flew out to search for a lake at **7:00 AM** and returned at **11:00 AM**. How many hours were they searching?", "4 hours", "2 hours", "5 hours", "3 hours", "A", "11:00 AM - 7:00 AM = 4 hours."),
        ("Match the day with its abbreviation: **Monday**", "Mon.", "Mnd.", "Mo.", "Mn.", "A", "Mon. is standard."),
        ("If the swans and turtle started flying on **Friday morning** and arrived on **Saturday morning**, how many days did the flight take?", "1 full day (24 hours)", "2 days", "3 days", "half a day", "A", "Friday morning to Saturday morning is 1 full day."),
        ("Identify the correctly spelt month name:", "August", "Auguest", "Auguste", "Augustt", "A", "August is the correct spelling."),
        ("Identify the INCORRECT pair of day and abbreviation:", "Monday - Mon.", "Tuesday - Tue.", "Wednesday - Wed.", "Friday - Frd.", "D", "Friday abbreviation is Fri., not Frd."),
        ("The summer lasted for **12 weeks**. How many months is approximately 12 weeks?", "3 months", "6 months", "1 month", "12 months", "A", "4 weeks per month -> 12 / 4 = 3 months."),
        ("Which month has 30 days and comes right before June?", "May (has 31) / April (has 30)", "April", "March", "July", "B", "April has 30 days and comes before May/June."),
        ("Rearrange in correct chronological order: Fri, Wed, Thu, Sat", "Wed, Thu, Fri, Sat", "Thu, Wed, Fri, Sat", "Wed, Fri, Thu, Sat", "Sat, Fri, Thu, Wed", "A", "Wednesday -> Thursday -> Friday -> Saturday."),
        ("What day is 2 days before Sunday?", "Friday", "Saturday", "Thursday", "Monday", "A", "Sunday - 2 days = Saturday(1), Friday(2)."),
        ("If the turtle talked after 30 minutes of flying, how many half-hours did he stay quiet?", "1 half-hour", "2 half-hours", "3 half-hours", "4 half-hours", "A", "30 minutes = 1 half-hour."),
        ("Select the month that has 31 days:", "May", "June", "April", "September", "A", "May has 31 days."),
        ("Which abbreviation stands for **March**?", "Mar.", "Mch.", "Ma.", "Mr.", "A", "Mar. is standard abbreviation."),
        ("If today is **Fri.**, what day will it be after 7 days?", "Friday", "Saturday", "Thursday", "Monday", "A", "7 days is a full week cycle, landing on Friday again."),
        ("The flight passed over villages from **9:00 AM** to **10:00 AM**. How many minutes were they in the air before the turtle fell?", "60 minutes", "30 minutes", "90 minutes", "45 minutes", "A", "1 hour = 60 minutes."),
        ("Identify the word that means 'occurring once every year':", "Yearly / Annual", "Daily", "Weekly", "Monthly", "A", "Yearly or Annual means once a year."),
        ("Which of the following is a weekend day?", "Saturday", "Monday", "Tuesday", "Wednesday", "A", "Saturday is a weekend day."),
        ("Choose the correct abbreviation for **September**:", "Sept. or Sep.", "Spt.", "Septe.", "St.", "A", "Sept. or Sep. is standard.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH03_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Application & Story Timeline:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Calendar & Time Reasoning", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("The swans searched for a new lake from **Mon., 1st June** to **Wed., 3rd June**. How many days did they search?", "3 days", "2 days", "1 day", "4 days", "A", "1st, 2nd, 3rd June inclusive is 3 days."),
        ("The turtle stayed quiet from **10:00 AM to 10:45 AM**. For how many minutes did he obey the warning?", "45 minutes", "30 minutes", "60 minutes", "15 minutes", "A", "10:45 - 10:00 = 45 minutes."),
        ("Solve the calendar puzzle: If 1st June is a Monday, what day of the week will 8th June be?", "Monday", "Tuesday", "Sunday", "Friday", "A", "1 + 7 = 8th June, landing on Monday."),
        ("Analyze this schedule: Swans flew on Mon, Wed, Fri; Turtle rested Tue, Thu, Sat. On which day did NONE of them travel?", "Sunday", "Monday", "Saturday", "Wednesday", "A", "Sunday is not listed in travel schedule."),
        ("Complete the full series of day abbreviations: Mon., Tue., Wed., Thu., ____, Sat., ____.", "Fri., Sun.", "Frid., Sun.", "Fr., Su.", "Fri., Sn.", "A", "Fri. and Sun. complete the sequence."),
        ("If the lake was dry for a fortnight, how many days was it dry?", "14 days (2 weeks)", "7 days", "30 days", "3 days", "A", "A fortnight is 14 days."),
        ("Spot the error in the calendar sequence: 'May, Jun, Aug, Jul, Sep'", "August and July are in wrong order.", "June is in wrong position.", "September should be first.", "No error.", "A", "July comes before August (May, Jun, Jul, Aug, Sep)."),
        ("The swans arrived at the new lake on **30th June**. What date was the next day?", "1st July", "31st June", "29th June", "1st August", "A", "June has 30 days, so the next day is 1st July."),
        ("If yesterday was two days before Thursday, what day is tomorrow?", "Thursday", "Wednesday", "Friday", "Tuesday", "A", "Two days before Thursday = Tuesday (yesterday). Today = Wednesday. Tomorrow = Thursday."),
        ("Calculate: How many days are there in total during **June** and **July** combined?", "61 days (30 + 31)", "60 days", "62 days", "59 days", "A", "June has 30 days, July has 31 days. 30 + 31 = 61 days."),
        ("HOTS Reasoning: Why do summer months (May, June, July) cause lakes to dry up faster?", "High temperatures increase evaporation rate of water.", "Swans drink all the water.", "Turtles eat the water.", "Lakes sleep in summer.", "A", "Heat causes rapid evaporation."),
        ("Identify the correct statement about a leap year:", "Leap year adds 1 day to February, making it 29 days.", "Leap year adds 1 day to June.", "Leap year removes 1 day from July.", "Leap year occurs every 5 years.", "A", "February has 29 days in a leap year."),
        ("The turtle fell from a height of 100 meters in 5 seconds. How many seconds did his fall take?", "5 seconds", "10 seconds", "1 second", "60 seconds", "A", "Directly stated as 5 seconds."),
        ("Which month pair both have 31 days and come right after each other in summer?", "July and August", "June and July", "August and September", "May and June", "A", "July (31 days) and August (31 days) are consecutive months with 31 days.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH03_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Logic & Mathematical Time Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Calendar & Time Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 4. Action Verbs Identification (50 Qs)
# ---------------------------------------------------------------------------
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification — Chapter 03: The Turtle and the Swans\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_verbs = [
        ("The swans **flew** to find a new lake.", "flew", "swans", "new", "lake", "A", "'flew' is the action verb."),
        ("The turtle **held** the stick with his mouth.", "held", "turtle", "stick", "mouth", "A", "'held' is the physical action verb."),
        ("The lake **started** drying up in summer.", "started", "lake", "up", "summer", "A", "'started' is the action verb."),
        ("The swans **warned** the turtle not to talk.", "warned", "swans", "turtle", "talk", "A", "'warned' is the action verb."),
        ("The turtle **opened** his mouth to speak.", "opened", "turtle", "mouth", "speak", "A", "'opened' is the action verb."),
        ("The turtle **fell** down from the sky.", "fell", "turtle", "down", "sky", "A", "'fell' is the action verb."),
        ("The villagers **watched** the unique view.", "watched", "villagers", "unique", "view", "A", "'watched' is the action verb."),
        ("The turtle **loved** the sound of his voice.", "loved", "turtle", "sound", "voice", "A", "'loved' is the emotional action/state verb."),
        ("The friends **decided** to move away.", "decided", "friends", "away", "move", "A", "'decided' is the mental action verb."),
        ("The swans **brought** a wooden stick.", "brought", "swans", "wooden", "stick", "A", "'brought' is the action verb."),
        ("The turtle **ignored** the good advice.", "ignored", "turtle", "good", "advice", "A", "'ignored' is the action verb."),
        ("The turtle **agreed** to keep quiet.", "agreed", "turtle", "quiet", "keep", "A", "'agreed' is the action verb."),
        ("The turtle **talked** all day long.", "talked", "turtle", "long", "day", "A", "'talked' is the action verb."),
        ("The swans **carried** the turtle high up.", "carried", "swans", "turtle", "high", "A", "'carried' is the action verb."),
        ("The lake **dried** under the hot sun.", "dried", "lake", "under", "sun", "A", "'dried' is the action verb."),
        ("The turtle **blurted** out loud words.", "blurted", "turtle", "out", "words", "A", "'blurted' is the vocal action verb."),
        ("The turtle **died** when he hit the ground.", "died", "turtle", "hit", "ground", "A", "'died' is the action/event verb."),
        ("We must **think** before we speak.", "think", "we", "must", "before", "A", "'think' is the mental action verb.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_verbs, start=1):
        qid = f"BK02_CH03_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in this sentence from or related to Chapter 03:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Action Verb Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Which word from the sentence is an **action verb**? 'The turtle **foolishly** **opened** his **big** **mouth**.'", "opened", "foolishly", "big", "mouth", "A", "'opened' shows physical action; 'foolishly' is adverb, 'big' is adjective, 'mouth' is noun."),
        ("Identify BOTH action verbs in: 'The swans **flew** high and **held** the stick.'", "flew, held", "swans, high", "stick, held", "flew, stick", "A", "'flew' and 'held' are both action verbs."),
        ("What is the past tense action verb of 'fall' as used in the story ('fell to his death')?", "fell", "fall", "fallen", "falling", "A", "Past tense of fall is fell."),
        ("Choose the sentence where the underlined word is used as an ACTION VERB:", "The swans will **fly** to the new lake.", "The bird has a graceful **fly**.", "Look at that **fly** on the stick.", "There is a **fly** in the water.", "A", "In (A), 'fly' acts as the main action verb."),
        ("Find the action verb in: 'The swans found a bigger lake.'", "found", "swans", "bigger", "lake", "A", "'found' is the action verb."),
        ("Which sentence contains NO physical action verb?", "The turtle was talkative.", "The swans flew away.", "The turtle dropped the stick.", "They found a new lake.", "A", "'The turtle was talkative' contains linking verb 'was', but no physical action verb."),
        ("Change the action verb 'speak' to past tense: 'The turtle (speak) without thinking.'", "spoke", "speaked", "speaking", "speaks", "A", "Past tense of speak is spoke."),
        ("Identify the action verb: 'The swans warned the turtle but he forgot.'", "warned, forgot", "swans, turtle", "he, warned", "forgot, turtle", "A", "'warned' and 'forgot' are action verbs."),
        ("Select the action verb that completes the sentence: 'The lake ____ during the hot summer.'", "evaporated / dried", "dry", "hot", "water", "A", "'evaporated' / 'dried' is an action verb."),
        ("Which word is an action verb? (lake, turtle, carried, stick)", "carried", "lake", "turtle", "stick", "A", "'carried' is an action verb; others are nouns."),
        ("What action did the turtle perform that caused his fall?", "opened", "talkative", "stick", "lake", "A", "He opened his mouth (action verb)."),
        ("Identify the action verb in: 'The turtle thought about speaking.'", "thought", "turtle", "about", "speaking", "A", "'thought' is a mental action verb."),
        ("Choose the correct action verb: 'The villagers ____ in amazement.'", "marveled / watched", "amazing", "awe", "eyes", "A", "'marveled' / 'watched' is the action verb."),
        ("Identify the action verb in: 'The swans gripped the wooden stick.'", "gripped", "swans", "wooden", "stick", "A", "'gripped' is the action verb."),
        ("Which of these words is NOT an action verb? (fly, hold, blue, fall)", "blue", "fly", "hold", "fall", "A", "'blue' is an adjective; others are action verbs."),
        ("Identify the action verb in: 'The turtle shouted at the villagers.'", "shouted", "turtle", "at", "villagers", "A", "'shouted' is the action verb."),
        ("Fill in the blank with an appropriate action verb: 'The swans ____ through the blue sky.'", "glided / flew", "high", "blue", "clouds", "A", "'glided' / 'flew' is an action verb."),
        ("What action verb completes the sentence? 'The swans ____ a solution to the problem.'", "devised / found", "wise", "stick", "lake", "A", "'devised' / 'found' is an action verb.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH03_CAT04_Q{idx:02d}"
        qtxt = f"Action Verb Grammar Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Action Verb Context & Tense", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence: 'The talkative turtle foolishly opened his mouth and fell to his death.' How many total ACTION VERBS are present?", "2 action verbs ('opened', 'fell')", "1 action verb", "3 action verbs", "0 action verbs", "A", "'opened' and 'fell' are action verbs; 'talkative', 'foolishly', 'death' are adjectives/adverbs/nouns."),
        ("Categorize the verbs: In 'The turtle **was** talkative, so he **opened** his mouth', classify 'was' and 'opened'.", "'was' is a linking verb; 'opened' is an action verb.", "Both are action verbs.", "Both are linking verbs.", "'was' is action; 'opened' is linking.", "A", "'was' links state of being; 'opened' shows physical action."),
        ("Replace the weak verb with a strong action verb: 'The turtle **fell down fast** from the sky.'", "The turtle **plummeted** from the sky.", "The turtle **was below** the sky.", "The turtle **went down**.", "The turtle **looked at** the ground.", "A", "'plummeted' is a much stronger, vivid action verb."),
        ("Identify the sentence with THREE distinct action verbs:", "The swans **flew** abroad, **found** a lake, and **carried** the turtle.", "The turtle was slow, talkative, and foolish.", "The lake dried up in the summer.", "The people watched in awe.", "A", "flew, found, carried are 3 distinct action verbs."),
        ("Differentiate verb types: Which underlined word is an ACTION verb?", "The turtle **disobeyed** the warning.", "The turtle was **foolish**.", "The lake was **dry**.", "The swans were **helpful**.", "A", "'disobeyed' is an action verb."),
        ("Spot the incorrect verb tense: 'The turtle **fall** from the sky yesterday.' Correct it:", "'fall' should be 'fell' (past action verb).", "'fall' should be 'falling'.", "'fall' should be 'falls'.", "'fall' should be 'will fall'.", "A", "Past time indicator 'yesterday' requires past tense action verb 'fell'."),
        ("Form an action chain: Rearrange the story action verbs in correct order of occurrence: (warned, held, opened, fell)", "warned -> held -> opened -> fell", "fell -> opened -> held -> warned", "held -> warned -> fell -> opened", "opened -> warned -> held -> fell", "A", "First swans warned, turtle held stick, turtle opened mouth, turtle fell."),
        ("Identify the verb error in dialogue: Turtle said, 'I have **speak** without thinking!'", "'speak' is incorrect; the past participle form is 'spoken' ('have spoken').", "'speak' should be 'speaking'.", "'speak' should be 'speaks'.", "No error.", "A", "Perfect tense requires past participle 'spoken'."),
        ("Analyze this sentence: 'The turtle **blurted** out a foolish remark.' What type of action verb is 'blurted'?", "Vocal/Speech action verb", "Physical movement verb", "Linking verb", "State of being verb", "A", "'blurted' is an action verb of speech."),
        ("Which sentence uses action verbs to show cause and effect?", "The turtle **opened** his mouth, so he **fell** down.", "The turtle was slow and the swans were fast.", "The lake had fresh water.", "The sky was blue.", "A", "'opened' (cause action) -> 'fell' (effect action)."),
        ("Spot the missing action verb: 'The swans ____ the stick in their beaks and ____ into the air.'", "clutched, soared", "big, blue", "was, was", "quick, slow", "A", "'clutched' and 'soared' complete sentence with vivid actions."),
        ("HOTS Reasoning: Why is 'warned' in 'The swans warned him' considered a PREVENTATIVE action verb?", "Because it describes an active effort to prevent a future disaster.", "Because warning requires a stick.", "Because lake was dry.", "Because it is a noun.", "A", "Descriptive speech action verb aimed at prevention."),
        ("Transform the action verb to future tense: 'The turtle **falls** to the ground.'", "The turtle **will fall** to the ground.", "The turtle **fell** to the ground.", "The turtle **is falling** to the ground.", "The turtle **fall** to the ground.", "A", "'will fall' expresses future action."),
        ("Identify the sentence where the action verb matches the plural subject:", "The swans **fly** across the sky.", "The swans **flies** across the sky.", "The swan **fly** across the sky.", "The swans **is flying** across the sky.", "A", "Plural subject 'swans' takes base verb 'fly' in simple present.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH03_CAT04_Q{idx:02d}"
        qtxt = f"Higher Order Action Verb Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Action Verb Classification & Tense Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 5. Punctuation Marks (50 Qs)
# ---------------------------------------------------------------------------
def build_punctuation_marks():
    header = "# Category 5: Punctuation Marks & Capitalization — Chapter 03: The Turtle and the Swans\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_punct = [
        ("What punctuation mark should be placed at the end of: 'The turtle lived near a lake__'", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "Comma (,)", "A", "A statement ends with a full stop."),
        ("Which mark is used at the end of an asking sentence: 'Why did the lake dry up__'", "Question mark (?)", "Full stop (.)", "Comma (,)", "Exclamation mark (!)", "A", "A question ends with a question mark."),
        ("Which letter should ALWAYS be capitalized in a proper title like 'Panchatantra'?", "The first letter (e.g., Panchatantra)", "The last letter", "All letters", "No letters", "A", "First letter of proper nouns must be capitalized."),
        ("Identify the punctuation mark used to separate items in a list: 'The swans saw houses__ trees__ and people.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Hyphen (-)", "A", "Commas separate items in a list."),
        ("Which punctuation mark shows sudden amazement or warning: 'Look at that flying turtle__'", "Exclamation mark (!)", "Full stop (.)", "Comma (,)", "Question mark (?)", "A", "Exclamation marks express amazement/surprise."),
        ("Select the word that MUST start with a capital letter at sentence beginning:", "Once", "turtle", "lake", "stick", "A", "First word of a sentence MUST be capitalized."),
        ("Which of the following is the symbol for a **full stop**?", ".", "?", "!", ",", "A", "Period/full stop is '.'"),
        ("Which of the following is the symbol for a **question mark**?", "?", ".", "!", ",", "A", "Question mark is '?'"),
        ("Which of the following is the symbol for an **exclamation mark**?", "!", "?", ".", ",", "A", "Exclamation mark is '!'"),
        ("Which word in this sentence should start with a CAPITAL letter? 'the swans flew high in the sky.'", "the -> The", "swans -> Swans", "sky -> Sky", "flew -> Flew", "A", "The first word of a sentence must start with a capital letter."),
        ("What punctuation mark goes in the box? 'The turtle opened his mouth [ ]'", "Full stop (.)", "Question mark (?)", "Comma (,)", "Exclamation mark (!)", "A", "Full stop ends the statement."),
        ("Which name is capitalized correctly?", "Panchatantra", "panchatantra", "pAnchaTantra", "panchatantrA", "A", "Capital 'P' for proper name Panchatantra."),
        ("What mark goes after a speaker tag: 'The turtle blurted out__ \"Look at all the people!\"'", "Comma (,)", "Question mark (?)", "Full stop (.)", "Exclamation mark (!)", "A", "Comma follows dialogue speaker tags."),
        ("Identify the correct capital letter for the pronoun 'I': 'the turtle said, \"i am flying!\"'", "I", "i", "i'm", "I'm", "A", "Standalone pronoun 'I' is always capitalized."),
        ("Which option shows a sentence ending correctly?", "The turtle fell to his death.", "The turtle fell to his death?", "The turtle fell to his death,", "The turtle fell to his death;", "A", "Full stop at end of simple statement."),
        ("What mark is used in possessives like 'the **turtle's** shell'?", "Apostrophe (')", "Comma (,)", "Full stop (.)", "Hyphen (-)", "A", "Apostrophe indicates possession."),
        ("Which book title is capitalized correctly?", "The Turtle and the Swans", "the turtle and the swans", "The turtle And The swans", "THE TURTLE AND THE SWANS", "A", "Major words in titles are capitalized."),
        ("What punctuation mark is used around spoken dialogue: '___Do not talk while flying!___'", "Quotation marks / Speech marks ( \" \" )", "Parentheses ( )", "Full stops ( . . )", "Commas ( , , )", "A", "Speech marks enclose spoken dialogue.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_punct, start=1):
        qid = f"BK02_CH03_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Punctuation & Capitalization Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Identify the sentence with CORRECT capitalization and punctuation:", "The turtle lived near a lake in June.", "the turtle lived near a lake in june.", "The turtle lived near a lake in june?", "the Turtle Lived Near A Lake In June.", "A", "The (start), June (month) capitalized; ends with period."),
        ("Which sentence is punctuated as a CORRECT question?", "Why did the turtle open his mouth?", "Why did the turtle open his mouth.", "Why did the turtle open his mouth!", "Why did the turtle open his mouth,", "A", "Question starting with 'Why' ends with question mark ?"),
        ("Spot the capitalization mistake in: 'the turtle lived near a Lake with two Swans.'", "'the' should be capitalized ('The'); 'Lake' and 'Swans' should be lowercase.", "'Swans' should be capitalized only.", "'Lake' should be capitalized.", "No mistake.", "A", "Sentence start 'The' capitalized; common nouns lake and swans lowercase here."),
        ("Choose the correctly punctuated dialogue sentence:", "\"Hold the stick tightly,\" warned the swans.", "hold the stick tightly warned the swans.", "\"Hold the stick tightly\" warned the swans", "Hold the stick tightly, warned the swans.", "A", "Quotation marks around dialogue, comma inside quote, capital H."),
        ("Identify where a COMMA is missing: 'The turtle saw houses towns and lakes.'", "Between 'houses' and 'towns' ('houses, towns')", "After 'The'", "After 'lakes'", "No comma needed", "A", "Commas separate items in list: 'houses, towns and lakes'."),
        ("Which sentence uses the apostrophe correctly for possession?", "This is the turtle's shell.", "This is the turtles' shell.", "This is the turtles shell.", "This is the turtle's' shell.", "A", "turtle's indicates possession by one turtle."),
        ("Select the sentence with CORRECT punctuation for an exclamatory statement:", "Look at the flying turtle!", "Look at the flying turtle?", "Look at the flying turtle.", "Look at the flying turtle,", "A", "Exclamatory statement ends with exclamation mark !"),
        ("Which contraction is written correctly for 'could not'?", "couldn't", "could'nt", "couldnt'", "c'ouldnt", "A", "couldn't is standard contraction."),
        ("Find the sentence with NO capitalization errors:", "The Panchatantra is a famous collection of Indian fables.", "the panchatantra is a famous collection of indian fables.", "The Panchatantra Is A Famous Collection Of Indian Fables.", "the Panchatantra is a famous collection of Indian fables.", "A", "'Panchatantra' and 'Indian' capitalized as proper nouns/adjectives."),
        ("What punctuation mark belongs in the blank? 'The villagers shouted, \"Oh dear__ The turtle is falling!\"'", "!", ".", "?", ",", "A", "Exclamation mark ! expresses distress/shock."),
        ("Choose the correct form for 'did not':", "didn't", "did'nt", "didnt'", "d'idnt", "A", "didn't is the standard contraction."),
        ("Identify the punctuation error: 'The lake dried up, the swans flew away.'", "Comma splice between two independent clauses (should be full stop or 'and').", "Missing question mark.", "Missing capital letters.", "No error.", "A", "Two complete sentences separated only by comma."),
        ("Select the sentence with proper use of capital letters for months and days:", "The lake dried up in June on Monday.", "The lake dried up in june on monday.", "The lake dried up in June on monday.", "The lake dried up in june on Monday.", "A", "Both June (month) and Monday (day) must be capitalized."),
        ("Which sentence correctly uses an apostrophe for possessive plural?", "The two swans' beaks held the wooden stick.", "The two swan's beaks held the wooden stick.", "The two swans beaks held the wooden stick.", "The two swans's beaks held the wooden stick.", "A", "Plural ending in -s takes apostrophe after the s (swans')."),
        ("Identify the correct punctuation for a list of items: 'The turtle saw ____'", "villages, rivers, and green fields.", "villages rivers and green fields.", "villages; rivers; and green fields.", "villages: rivers: and green fields.", "A", "Commas separate items in list."),
        ("Choose the sentence that correctly asks a question about the story:", "How did the swans carry the turtle?", "How did the swans carry the turtle.", "How did the swans carry the turtle!", "how did the swans carry the turtle.", "A", "Capital H, ends with question mark ?"),
        ("Fix the sentence: 'where is the turtles lake'", "Where is the turtle's lake?", "Where is the turtles lake.", "where is the Turtle's lake!", "Where is the Turtles' lake?", "A", "Capital W, possessive turtle's, ends with ?"),
        ("Which of these sentences is punctuated PERFECTLY?", "The swans warned, \"Do not open your mouth!\"", "The swans warned \"do not open your mouth!\"", "the swans warned, \"Do not open your mouth!\"", "The swans warned, \"Do not open your mouth.\"", "A", "Capital T, comma after warned, speech marks around warning with ! inside.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH03_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Context Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Punctuation Application & Dialogue Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze and count ALL capitalization and punctuation errors in: 'on monday the turtle asked the swans, can i fly with you'", "5 errors (on->On, monday->Monday, missing quotes, capital C in Can, question mark)", "2 errors", "3 errors", "7 errors", "A", "Starts sentence, day name, quotation marks, capital Can, question mark."),
        ("Correct the entire dialogue paragraph: 'the swans warned don't speak a word the turtle shouted look at the people'", "\"Don't speak a word!\" warned the swans. The turtle shouted, \"Look at the people!\"", "the swans warned \"don't speak a word\" the turtle shouted \"look at the people.\"", "The swans warned, Don't speak a word. The turtle shouted, Look at the people.", "\"Don't speak a word?\" Warned the swans. The turtle shouted \"Look at the people?\"", "A", "Full proper quotation, dialogue tags, capitalization, and terminal punctuation."),
        ("Distinguish between singular possessive and plural possessive: 'the **turtle's** shell' vs 'the **swans'** wings'", "First refers to one turtle's shell; second refers to the wings of two swans.", "Both refer to one animal.", "Both refer to multiple animals.", "First is plural; second is singular.", "A", "turtle's = singular; swans' = plural possessive."),
        ("Spot the subtle punctuation flaw in this dialogue: '\"Hold the stick,\" Said the swan.'", "'Said' should be lowercase 'said' because it continues the dialogue tag outside quotation marks.", "'Hold' should be lowercase.", "Commas should be outside quotes.", "No flaw.", "A", "Dialogue tags following quotes start with lowercase unless proper nouns."),
        ("Which sentence correctly uses punctuation to show contrast?", "The turtle was warned, but he could not stay quiet.", "The turtle was warned but, he could not stay quiet.", "The turtle was warned but he could not stay quiet!", "The turtle was warned; but he could not stay quiet?", "A", "Comma before coordinating conjunction 'but' joining two independent clauses."),
        ("Reconstruct with perfect punctuation: 'the swans flew over towns on tuesday 14th july at noon'", "The swans flew over towns on Tuesday, 14th July, at noon.", "the swans flew over towns on tuesday, 14th july at noon.", "The swans flew over towns on Tuesday 14th July at noon", "The swans flew over towns on tuesday 14th july at noon.", "A", "The, Tuesday, 14th July set off by commas, ends with period."),
        ("Identify why exclamation mark is necessary here: '\"Look at all the people!\"'", "Because the turtle is shouting out loud in sudden excitement.", "Because swans are flying.", "Because stick is short.", "Because sentence is long.", "A", "Exclamation mark communicates sudden excitement/outburst."),
        ("Choose the correctly punctuated sentence containing an appositive phrase:", "The turtle, a talkative creature, fell to his death.", "The turtle a talkative creature fell to his death.", "The turtle, a talkative creature fell to his death.", "The turtle a talkative creature, fell to his death.", "A", "Appositive phrase 'a talkative creature' is set off by commas."),
        ("Analyze the use of hyphen in: 'The thirty-two villagers watched the turtle in awe.'", "Hyphen joins compound numbers (thirty-two).", "Hyphen replaces comma.", "Hyphen indicates question.", "Hyphen is an apostrophe.", "A", "Compound numbers from twenty-one to ninety-nine take hyphens."),
        ("Identify the correct sentence with direct speech quote within text:", "The turtle foolishly shouted, \"Look at them,\" and lost his grip.", "The turtle foolishly shouted \"Look at them\" and lost his grip.", "The turtle foolishly shouted, 'Look at them,' and lost his grip.", "The turtle foolishly shouted: \"Look at them\" and lost his grip.", "A", "Comma before quote, double quotation marks around direct speech, comma inside quote."),
        ("Spot the missing apostrophe: 'The turtles shell was hard and heavy.'", "Missing apostrophe in 'turtle's' -> 'The turtle's shell'", "Missing apostrophe in 'was''", "Missing apostrophe in 'heavy''", "No apostrophe needed", "A", "'turtle's shell' requires possessive apostrophe."),
        ("HOTS Reasoning: Why does putting a comma in different places change meaning? Compare: 'The swans, said the turtle, are fast.' vs 'The swans said, \"The turtle is fast.\"'", "In the first, turtle says swans are fast; in the second, swans say turtle is fast.", "Both mean the exact same thing.", "The first is a question.", "Commas do not affect meaning.", "A", "Punctuation alters who speaks and who is described."),
        ("Correct all 4 errors in: 'why are you talking asked the swans'", "\"Why are you talking?\" asked the swans.", "why are you talking? asked the swans.", "\"Why are you talking.\" asked the swans.", "\"why are you talking?\" Asked the swans.", "A", "Quotation marks, capital W, question mark inside quote, period at end."),
        ("Identify the rule for capitalizing titles of respect or proper names:", "Proper names of people, places, and book titles require initial capital letters.", "Proper names are never capitalized.", "Proper names are capitalized only at end of sentence.", "Proper names must be written in ALL CAPS.", "A", "Proper names take capital initials.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH03_CAT05_Q{idx:02d}"
        qtxt = f"Higher Order Punctuation Analysis & Dialogue Formatting:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Punctuation & Dialogue Editing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 6. Phonics & Vowel Digraphs (50 Qs)
# ---------------------------------------------------------------------------
def build_phonics_digraphs():
    header = "# Category 6: Phonics & Vowel Digraphs — Chapter 03: The Turtle and the Swans\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_phonics = [
        ("Which vowel digraph is present in the word **'beak'** (in Chapter 03)?", "ea", "ee", "ai", "ou", "A", "'ea' is the vowel digraph in beak."),
        ("Identify the vowel digraph in the word **'heed'**:", "ee", "ea", "oa", "ui", "A", "'ee' forms the long /e/ vowel sound in heed."),
        ("Which word from the story contains the **'ou'** vowel digraph?", "sound", "lake", "swan", "stick", "A", "'sound' contains the 'ou' digraph."),
        ("Identify the vowel digraph in the word **'speak'**:", "ea", "ee", "ow", "oo", "A", "'ea' forms long /e/ sound in speak."),
        ("Which vowel digraph appears in the word **'paid'**?", "ai", "ay", "ea", "oa", "A", "'ai' makes long /a/ sound in paid."),
        ("Find the word with the **'oo'** vowel digraph: 'The turtle was a fool to talk.'", "fool", "turtle", "was", "talk", "A", "'fool' contains 'oo' digraph."),
        ("Which word from the story rhymes with **'lake'**?", "make", "look", "like", "leak", "A", "'make' rhymes with 'lake'."),
        ("Which word from the story rhymes with **'town'**?", "down", "than", "to", "ton", "A", "'down' rhymes with 'town'."),
        ("Identify the vowel digraph in the word **'roared'**:", "oa", "ou", "ow", "oo", "A", "'oa' makes long /o/ sound in roared."),
        ("Which word from the story rhymes with **'slow'**?", "crow", "slap", "slot", "saw", "A", "'crow' rhymes with 'slow'."),
        ("Identify the vowel digraph in **'voice'**:", "oi", "ea", "ee", "ia", "A", "'oi' is the vowel digraph in voice."),
        ("Which word from Chapter 03 has the **'ea'** digraph making a long /e/ sound?", "beak", "head", "heavy", "dead", "A", "'beak' has 'ea' making long /e/ sound."),
        ("Which word rhymes with **'day'**?", "away", "die", "due", "door", "A", "'away' rhymes with 'day'."),
        ("Identify the silent letter in **'talk'** (as in 'turtle loved to talk'):", "l", "t", "a", "k", "A", "Silent 'l' in talk."),
        ("Which word from the story has long /i/ sound spelled with **'igh'**?", "high", "brought", "beak", "body", "A", "'igh' in high makes long /i/ sound."),
        ("Find the word with **'ou'** digraph: 'They found a new lake.'", "found", "lake", "new", "they", "A", "'found' contains 'ou' digraph."),
        ("Which word rhymes with **'flight'**?", "sight", "fly", "flat", "flew", "A", "'sight' rhymes with 'flight'."),
        ("Identify the silent letter in the word **'know'** (as in 'did not know'):", "k", "n", "o", "w", "A", "Initial 'k' before 'n' is silent.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_phonics, start=1):
        qid = f"BK02_CH03_CAT06_Q{idx:02d}"
        qtxt = f"Phonics & Vowel Digraph Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Vowel Digraphs & Rhyming Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Compare the **'ea'** digraph sound in **'beak'** and **'dead'**. What is the difference?", "'beak' has long /e/ sound; 'dead' has short /e/ sound.", "Both have short /e/ sound.", "Both have long /a/ sound.", "'beak' has short /e/; 'dead' has long /e/.", "A", "'ea' can make long /e/ (beak) or short /e/ (dead)."),
        ("Select the word pair from Chapter 03 that has the SAME vowel digraph sound:", "heed - see", "four - dead", "beak - roar", "lake - tree", "A", "'heed' and 'see' both have 'ee' long /e/ sound."),
        ("Which word contains a SILENT letter? (talk, swan, lake, stick)", "talk", "swan", "lake", "stick", "A", "'talk' has silent 'l'."),
        ("Identify the odd one out based on vowel sound: (beak, speak, reach, dead)", "dead", "beak", "speak", "reach", "A", "'dead' has short /e/ sound; others have long /e/ sound."),
        ("Which digraph completes the word for sound? 'v__ce'", "oi", "ea", "ee", "ou", "A", "'voice' uses 'oi' digraph."),
        ("Group these story words by digraph: **sound**, **mouth**, **out**. What digraph do they all share?", "ou", "ow", "oo", "oi", "A", "All share 'ou' making /ow/ diphthong sound."),
        ("Find the word with consonant digraph **'th'** from the story: 'The **turtle** held **the** stick.'", "the", "turtle", "held", "stick", "A", "'the' contains voiced 'th' consonant digraph."),
        ("Which of these words has the **'ow'** vowel digraph making long /o/ sound? (slow, grow, blow, all of these)", "all of these", "slow", "grow", "blow", "A", "slow, grow, blow all share 'ow' long /o/ sound."),
        ("Identify the vowel digraph in **'awe'** (as in 'watched in awe'):", "aw", "ae", "we", "ew", "A", "'aw' is the digraph making /aw/ sound."),
        ("Which word from the story has a silent **'l'**? (talk, walk, half, all of these)", "all of these", "talk", "walk", "half", "A", "talk, walk, half all have silent 'l'."),
        ("Select the word that rhymes with **'lake'** and fits sentence: 'The turtle made a ____.'", "mistake", "lake", "take", "brake", "A", "'mistake' rhymes with 'lake'."),
        ("Identify the digraph in **'bleeding'**:", "ee", "ea", "ai", "oa", "A", "'ee' makes long /e/ sound."),
        ("Which word has the short /u/ sound made by **'ou'**? (touch, mouth, out, shout)", "touch", "mouth", "out", "shout", "A", "'touch' has short /u/ sound with 'ou'."),
        ("Find the R-controlled vowel sound in: 'The lake dried during **summer**.'", "er sound", "ea", "ou", "ai", "A", "R-controlled vowel in summer."),
        ("Which word contains the **'oi'** diphthong/digraph? (choice, voice, point, all of these)", "all of these", "choice", "voice", "point", "A", "choice, voice, point all contain 'oi'."),
        ("Identify the soft **'c'** sound in Chapter 03 vocabulary: (voice, lake, beak, stick)", "voice", "lake", "beak", "stick", "A", "'voice' has soft /s/ sound for 'c'; others have hard /k/ sound."),
        ("Which word has a soft **'g'** sound? (village, magic, danger, all of these)", "all of these", "village", "magic", "danger", "A", "village, magic, danger all have soft /j/ sound for 'g'."),
        ("Choose the correct spelling with **'ea'** digraph for bird's bill:", "beak", "beake", "beakk", "beck", "A", "beak is standard spelling.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH03_CAT06_Q{idx:02d}"
        qtxt = f"Phonics Analysis & Sound Pattern Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Phonic Rules & Sound Discrimination", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the phonics rule: Why does 'c' in **'voice'** sound like /s/, but 'c' in **'can'** sounds like /k/?", "Because 'c' followed by 'e', 'i', or 'y' makes soft /s/ sound; before 'a', 'o', 'u' it makes hard /k/ sound.", "Because voice is human.", "Because can is a verb.", "There is no rule.", "A", "Soft 'c' rule: c + i, e, y = /s/ sound."),
        ("Categorize the 'ea' digraphs into long /e/ vs short /e/: (beak, speak, dead, heavy, lead [metal])", "Long /e/: beak, speak; Short /e/: dead, heavy, lead [metal]", "All are long /e/.", "All are short /e/.", "Long /e/: dead; Short /e/: beak", "A", "beak, speak make long /e/; dead, heavy, lead (metal) make short /e/."),
        ("Identify the word pair where SILENT letters exist in BOTH words:", "talk - know", "beak - lake", "swan - tree", "fly - high", "A", "'talk' (silent l) and 'know' (silent k)."),
        ("Decode the phonics blend: Which word contains a 3-letter consonant blend at the start?", "squeaked / screamed", "turtle", "flew", "stick", "A", "'squ' / 'scr' blend types."),
        ("Examine the hard vs soft 'g' rule: Why is 'g' soft in **'village'** but hard in **'ground'**?", "'g' followed by 'e', 'i', or 'y' makes soft /j/ sound (village); 'g' before 'r' or 'a','o','u' makes hard /g/ sound (ground).", "Because village is quiet.", "Because ground is hard.", "There is no rule.", "A", "Soft 'g' rule: g + e, i, y = /j/ sound."),
        ("Find the word with BOTH a vowel digraph AND a silent letter:", "beaks", "talk", "lake", "swan", "A", "'beaks' has 'ea' digraph."),
        ("Differentiate diphthongs: Which pair produces the /ow/ sound as in **'mouth'**?", "mouth - sound", "voice - coin", "paid - day", "boat - coat", "A", "'mouth' and 'sound' share /ow/ diphthong sound."),
        ("Analyze homophones: 'The turtle saw a **sea** / **see**.' Which word means ocean?", "sea", "see", "si", "seey", "A", "'sea' (ocean) and 'see' (look) are homophones; 'sea' means ocean."),
        ("Identify the phonic pattern in **'height'**: What letters make the long /i/ sound?", "eigh", "ei", "gh", "ht", "A", "'eigh' makes long /i/ sound in height."),
        ("Sort by ending sound: Which word ends with the /z/ sound? (swans, lakes, sticks, beaks)", "swans", "lakes", "sticks", "beaks", "A", "Plurals ending in voiced sounds take /z/ ending sound (swans)."),
        ("Spot the word where 'l' is SILENT: (talk, walk, chalk, all of these)", "all of these", "talk", "walk", "chalk", "A", "'l' is silent in talk, walk, chalk."),
        ("HOTS Reasoning: Why do 'beak' and 'peek' sound identical at the end but have different spellings?", "They use different vowel digraphs ('ea' vs 'ee') to produce the long /e/ sound.", "They are synonyms.", "They are antonyms.", "They are plurals.", "A", "Both 'ea' and 'ee' can produce long /e/ sound."),
        ("Identify the compound word from story concepts containing two simple words:", "cloudless / dragonfly", "Panchatantra", "village", "turtle", "A", "cloudless = cloud + less; dragonfly = dragon + fly."),
        ("Determine the syllable count and stress: How many syllables are in **'unfortunate'**?", "4 syllables (un-for-tu-nate)", "2 syllables", "3 syllables", "5 syllables", "A", "un-for-tu-nate has 4 distinct syllables.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH03_CAT06_Q{idx:02d}"
        qtxt = f"Higher Order Phonics & Orthographic Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Phonetic Rules & Homophone Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 7. Question Words & Interrogatives (50 Qs)
# ---------------------------------------------------------------------------
def build_question_words():
    header = "# Category 7: Question Words & Interrogatives — Chapter 03: The Turtle and the Swans\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_qwords = [
        ("___ lived near the lake with a pair of swans?", "Who", "What", "Where", "Why", "A", "'Who' asks about a person/animal (the turtle)."),
        ("___ did the swans find when the lake dried up?", "What", "Who", "Where", "When", "A", "'What' asks about a thing (a bigger lake)."),
        ("___ did the friends decide to go when the lake dried up?", "Where", "Who", "What", "Why", "A", "'Where' asks about location (to a new bigger lake)."),
        ("___ was very talkative and loved his own voice?", "Who", "What", "Where", "Why", "A", "'Who' asks about identity (the turtle)."),
        ("___ did the swans carry the turtle in the air?", "How", "Where", "Why", "When", "A", "'How' asks about method (using a stick)."),
        ("___ warning did the swans give to the turtle?", "What", "Who", "Where", "Why", "A", "'What' asks about content of warning (not to talk)."),
        ("___ did the turtle fall down from the sky?", "Why", "Who", "Where", "What", "A", "'Why' asks for reason (he opened his mouth to talk)."),
        ("___ did the villagers react when they saw the flying turtle?", "How", "Who", "Where", "What", "A", "'How' asks about manner/reaction (watched in awe)."),
        ("___ held the two ends of the stick?", "Who", "What", "Where", "Why", "A", "'Who' asks about subject (the pair of swans)."),
        ("___ held the middle of the stick?", "Who", "What", "Where", "Why", "A", "'Who' asks about subject (the turtle)."),
        ("___ did the turtle open his mouth?", "Why / What happened", "Who", "Where", "When", "A", "'Why' / 'What' asks about action and motive."),
        ("___ season caused the lake to dry up?", "Which", "Who", "Why", "When", "A", "'Which' asks about specific season (summer)."),
        ("___ did the turtle fall to his death?", "Where", "Who", "Why", "What", "A", "'Where' / 'How' asks about destination/manner (to the ground)."),
        ("___ lesson does the story teach us?", "What", "Who", "Where", "Why", "A", "'What' asks about moral lesson."),
        ("___ swans were friends with the turtle?", "How many", "Who", "Where", "Why", "A", "'How many' asks about number (two / a pair)."),
        ("___ failed to follow the advice of his friends?", "Who", "What", "Where", "Why", "A", "'Who' asks about character (the turtle)."),
        ("___ did the swans search for water?", "Where", "Who", "Why", "What", "A", "'Where' asks about location."),
        ("___ did the turtle realize his mistake?", "When", "Who", "Where", "Why", "A", "'When' asks about time (as he fell).")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_qwords, start=1):
        qid = f"BK02_CH03_CAT07_Q{idx:02d}"
        qtxt = f"Choose the correct **question word** (Who, What, Where, Why, How, When):\n\n\"{q_blank} _____?\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Question Word Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Match question to answer: Question: '___ did the turtle fall?' Answer: 'Because he opened his mouth.'", "Why", "What", "Where", "Who", "A", "'Why' asks for reasons ('Because...')."),
        ("Match question to answer: Question: '___ was the new lake located?' Answer: 'Some distance away.'", "Where", "Who", "Why", "When", "A", "'Where' asks for location."),
        ("Choose the correct question word for TIME: '___ did the lake start drying up?'", "When", "Where", "Who", "Why", "A", "'When' inquires about time (during hot summer)."),
        ("Form an asking sentence: 'The swans carried a stick.' -> '____ did the swans carry?'", "What", "Who", "Why", "Where", "A", "'What' inquires about object."),
        ("Identify the INCORRECT question word usage: '**Why** is the turtle's name?'", "'Why' should be 'What'", "'Why' should be 'Where'", "'Why' should be 'When'", "No error", "A", "'What is the turtle's name?' asks for identity."),
        ("Select the proper interrogative sentence:", "Why did the turtle open his mouth?", "Why the turtle opened his mouth?", "Why did the turtle opened his mouth?", "Why turtle open mouth?", "A", "Interrogative word + auxiliary 'did' + base verb 'open'."),
        ("Which question word asks about MANNER or METHOD? '___ did the swans transport the turtle?'", "How", "Who", "What", "Where", "A", "'How' inquires about method/manner (by holding a stick)."),
        ("Complete the question: '___ of the three animals was talkative?'", "Which", "What", "Where", "Why", "A", "'Which' chooses between specific options."),
        ("Change statement to question: 'The villagers watched the sky.' -> '____ watched the sky?'", "Who", "What", "Where", "Why", "A", "'Who' asks for subject (the villagers)."),
        ("Fill in the blank: '___ fast did the lake dry up?'", "How", "What", "Where", "Why", "A", "'How fast' measures speed/degree."),
        ("Identify the question word in: 'Whom did the swans warn before flying?'", "Whom", "did", "swans", "flying", "A", "'Whom' is the interrogative pronoun asking about object person/animal."),
        ("Choose the question that matches this answer: 'He fell because he could not stay quiet.'", "Why did the turtle fall?", "Where did he fall?", "Who fell down?", "What did he fall on?", "A", "'Why...' matches answer starting with 'because...'."),
        ("Fill in the blank: '___ bird carried the stick?'", "Which", "Who", "Why", "Where", "A", "'Which bird' asks for identification."),
        ("Complete: '___ water was left in the lake?'", "How much", "How many", "Who", "Where", "A", "'How much' asks about uncountable quantity (water)."),
        ("Select the correct question for: 'The turtle opened his mouth to speak.'", "What did the turtle do?", "Where was the turtle?", "Why is the turtle fast?", "Who was the swan?", "A", "'What did turtle do?' asks for action."),
        ("Which question word inquires about POSSESSION? '___ advice was ignored by the turtle?'", "Whose", "Who", "Where", "Why", "A", "'Whose' asks about origin/ownership."),
        ("Form question: 'The turtle had two friends.' -> '____ friends did the turtle have?'", "How many", "How much", "Why", "Where", "A", "'How many' asks for countable number."),
        ("Identify the question mark error: 'Why did the turtle talk.' Correct it:", "Why did the turtle talk?", "Why did the turtle talk!", "Why did the turtle talk,", "Why did the turtle talk;", "A", "Questions must end with question mark ?")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH03_CAT07_Q{idx:02d}"
        qtxt = f"Question Formation & Context Alignment:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Interrogative Sentence Formation", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence structure: 'Why did the turtle disobey the swans' warning?' What is the syntax pattern?", "Question Word + Helping Verb (did) + Subject (the turtle) + Main Verb (disobey) + Object", "Question Word + Main Verb + Subject", "Subject + Question Word + Verb", "Helping Verb + Question Word + Subject", "A", "Standard English question syntax."),
        ("Differentiate between 'How many' vs 'How much': '___ swans' vs '___ water'", "'How many' for countable swans; 'How much' for uncountable water.", "Both use 'How many'.", "Both use 'How much'.", "'How much' for swans; 'How many' for water.", "A", "Countable nouns take 'How many'; uncountable nouns take 'How much'."),
        ("Spot the syntax error in question: 'Where the swans carried the turtle?' Correct it:", "Where **did** the swans carry the turtle?", "Where the swans carry the turtle?", "Where carried the swans the turtle?", "Where does the swans carried the turtle?", "A", "Past simple questions require auxiliary 'did' before subject and base verb 'carry'."),
        ("Framing multi-question interview: What sequence of question words logically reveals the story plot?", "Who -> What problem occurred -> How was a solution made -> Why did it end tragically", "How -> Who -> Why -> What", "Where -> Where -> Where -> Where", "Why -> Why -> Why -> Why", "A", "Reveals character, problem, solution, and tragic resolution."),
        ("Transform the statement into a formal question: 'Think before speaking.'", "Why is it important to think before speaking?", "Where do we speak?", "Who speaks?", "What is speaking?", "A", "Directly targets the moral lesson."),
        ("Analyze this ambiguous question: 'What did the turtle do?' How can it be made precise?", "Add specific context: 'What mistake did the turtle commit while flying in the air?'", "Make it shorter: 'What turtle?'", "Change to: 'Where turtle?'", "Remove 'What'.", "A", "Adding specific context clarifies which action and mistake."),
        ("Choose the correct question pair for dialogue: Swans: '___ will you keep your mouth closed?' Turtle: '___ would I open it when I am flying?'", "How / When, Why", "Who, Where", "Where, How", "When, Whose", "A", "How/When (condition of keeping quiet), Why (reason for opening)."),
        ("Spot the DOUBLE auxiliary error: 'Why did the turtle opened his mouth?'", "'did' requires base verb 'open', not past tense 'opened'.", "'did' should be 'was'.", "'Why' should be 'How'.", "No error.", "A", "Auxiliary 'did' must be followed by base form of verb ('open')."),
        ("Reconstruct question from answer: Answer: 'The turtle fell because he could not control his tongue.'", "Question: 'What caused the fatal fall of the talkative turtle?'", "Question: 'Where did turtle fly?'", "Question: 'Who is swan?'", "Question: 'Why swans fly?'", "A", "Targets cause of the fall."),
        ("Form indirect question: 'The villagers asked how the turtle was flying.' What is the sentence type?", "Assertive statement containing an embedded indirect question.", "Direct question requiring question mark.", "Exclamatory sentence.", "Command.", "A", "Indirect questions are statements ending with full stop."),
        ("Identify the correct question word for moral reasoning: '___ should we assess the situation before blurting out words?'", "Why", "What", "Who", "Where", "A", "'Why' inquires into the moral reason for self-control."),
        ("HOTS Reasoning: Why is 'Who' used for people/characters but 'Which' used when selecting from a specific group of animals?", "'Who' is general; 'Which' is used when choosing from a defined limited set.", "'Who' is for inanimate objects.", "'Which' is only for numbers.", "Both are identical.", "A", "'Which of the three friends...' selects from a defined group."),
        ("Correct all errors in: 'who carried the stick in their beaks'", "Who carried the stick in their beaks?", "Who carried the stick in their beaks.", "Whom carried stick in beaks?", "Who does carried the stick in their beaks?", "A", "Capital W, question mark at end."),
        ("Select the question that evaluates Higher Order Thinking (HOTS) about Chapter 03:", "How does the turtle's tragic fate prove that foolish talkativeness leads to downfall?", "What were the names of the swans?", "Where was the lake?", "Did the turtle fly?", "A", "Asks student to evaluate moral theme and cause-and-effect.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH03_CAT07_Q{idx:02d}"
        qtxt = f"Higher Order Interrogative Analysis & Syntax:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Question Syntax & Analytical Framing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 8. Present Continuous Tense (-ing) (50 Qs)
# ---------------------------------------------------------------------------
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense (-ing) — Chapter 03: The Turtle and the Swans\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_ing = [
        ("The swans are **flying** in the sky.", "flying", "swans", "are", "sky", "A", "'flying' is verb + -ing form."),
        ("The turtle is **holding** the stick tightly.", "holding", "turtle", "is", "stick", "A", "'holding' is verb + -ing form."),
        ("The lake is **drying** up in the summer.", "drying", "lake", "is", "summer", "A", "'drying' is verb + -ing form."),
        ("The swans are **carrying** the turtle.", "carrying", "swans", "are", "turtle", "A", "'carrying' is verb + -ing form."),
        ("The turtle is **falling** to the ground.", "falling", "turtle", "is", "ground", "A", "'falling' is verb + -ing form."),
        ("The villagers are **watching** the flying scene.", "watching", "villagers", "are", "scene", "A", "'watching' is verb + -ing form."),
        ("The swans are **searching** for a new lake.", "searching", "swans", "are", "lake", "A", "'searching' is verb + -ing form."),
        ("The turtle is **opening** his mouth.", "opening", "turtle", "is", "mouth", "A", "'opening' is verb + -ing form."),
        ("The birds are **soaring** over the hills.", "soaring", "birds", "are", "hills", "A", "'soaring' is verb + -ing form."),
        ("The turtle is **talking** without thinking.", "talking", "turtle", "is", "thinking", "A", "'talking' is verb + -ing form."),
        ("The sun is **shining** hot in May.", "shining", "sun", "is", "hot", "A", "'shining' is verb + -ing form."),
        ("The swans are **warning** the talkative turtle.", "warning", "swans", "are", "turtle", "A", "'warning' is verb + -ing form."),
        ("The water is **evaporating** from the pond.", "evaporating", "water", "is", "pond", "A", "'evaporating' is verb + -ing form."),
        ("The turtle is **disobeying** the advice.", "disobeying", "turtle", "is", "advice", "A", "'disobeying' is verb + -ing form."),
        ("The villagers are **pointing** at the sky.", "pointing", "villagers", "are", "sky", "A", "'pointing' is verb + -ing form."),
        ("The swans are **holding** the stick beaks.", "holding", "swans", "are", "beaks", "A", "'holding' is verb + -ing form."),
        ("The turtle is **losing** his grip on the stick.", "losing", "turtle", "is", "grip", "A", "'losing' is verb + -ing form."),
        ("The story is **teaching** us self-control.", "teaching", "story", "is", "self-control", "A", "'teaching' is verb + -ing form.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_ing, start=1):
        qid = f"BK02_CH03_CAT08_Q{idx:02d}"
        qtxt = f"Identify the **present continuous (-ing) verb** in this sentence:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the present continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Present Continuous Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("What is the correct -ing spelling rule for **'fly'**? (The swans are ____.)", "flying (add -ing)", "flyying", "flieing", "flyng", "A", "Vowel + y verb adding -ing (flying)."),
        ("What is the correct -ing spelling rule for **'hold'**? (The turtle is ____ the stick.)", "holding (add -ing)", "holdding", "holdeing", "holdng", "A", "Regular verb adding -ing (holding)."),
        ("What is the correct -ing spelling rule for **'shine'**? (The sun is ____.)", "shining (drop final silent e)", "shineing", "shinning", "shinng", "A", "Drop final silent 'e' before adding -ing (shining)."),
        ("Fill in the blank with present continuous form: 'The lake (dry) ____ up.'", "is drying", "was dry", "are dry", "is dried", "A", "Singular subject takes 'is drying'."),
        ("Choose the sentence in PRESENT CONTINUOUS tense:", "The swans are flying to the lake.", "The swans flew to the lake.", "The swans will fly to the lake.", "The swans flew yesterday.", "A", "'are flying' is present continuous."),
        ("Fill in the blanks: 'The swans ____ (carry) the stick, and the turtle ____ (hang) in the middle.'", "are carrying, is hanging", "is carrying, are hanging", "are carry, is hang", "was carrying, were hanging", "A", "Plural 'swans' takes 'are carrying'; singular 'turtle' takes 'is hanging'."),
        ("Identify the spelling mistake in: 'The turtle is **openning** his mouth.'", "'openning' should be 'opening'", "'openning' should be 'opening'", "'is' should be 'are'", "No mistake", "A", "Open does not double 'n' (opening)."),
        ("Select the correct -ing form for **'move'**:", "moving", "moveing", "movving", "movng", "A", "Drop silent 'e': move -> moving."),
        ("Which sentence describes an action HAPPENING RIGHT NOW?", "The turtle is falling through the air.", "The turtle fell yesterday.", "The turtle falls every time.", "The turtle will fall tomorrow.", "A", "Present continuous ('is falling') describes ongoing action right now."),
        ("Fill in the blank: 'I ____ (hold) the stick with my teeth!'", "am holding", "is holding", "are holding", "am holdeing", "A", "Subject 'I' takes 'am holding'."),
        ("Choose the correct form: 'The villagers ____ (shout) with surprise.'", "are shouting", "is shouting", "am shouting", "are shout", "A", "Plural subject 'villagers' takes 'are shouting'."),
        ("Identify the verb in: 'Why are you opening your mouth?'", "are opening", "Why", "you", "mouth", "A", "Helping verb 'are' + main verb 'opening' form present continuous."),
        ("What is the -ing form of **'drop'**?", "dropping", "droping", "droppping", "dropeing", "A", "CVC rule: drop -> dropping."),
        ("What is the -ing form of **'bite'**?", "biting", "biteing", "bitting", "biteing", "A", "Drop silent e: bite -> biting."),
        ("Change simple present to continuous: 'The turtle talks.' -> 'The turtle ____.'", "is talking", "talked", "was talking", "will talk", "A", "is talking."),
        ("Fill in the blank: 'The turtle ____ (fall) to the ground.'", "is falling", "are falling", "am falling", "fell", "A", "is falling."),
        ("Identify the correct present continuous sentence:", "Look! The turtle is loosening his grip.", "Look! The turtle loosen his grip.", "Look! The turtle loosened his grip.", "Look! The turtle loosening his grip.", "A", "Exclamation 'Look!' introduces action happening now ('is loosening')."),
        ("Select the correct -ing form for **'create'**:", "creating", "createing", "creatting", "creatng", "A", "Drop silent e: create -> creating.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH03_CAT08_Q{idx:02d}"
        qtxt = f"Present Continuous Grammar & Spelling Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Present Continuous Formation & Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze spelling rules for adding -ing to verbs: Group them correctly: (stop, save, lie)", "stop -> stopping (double consonant), save -> saving (drop e), lie -> lying (change -ie to -y)", "All just add -ing.", "All double the last letter.", "stop -> stoping, save -> saveing, lie -> lieing", "A", "3 distinct orthographic rules for -ing derivation."),
        ("Convert past tense narrative to present continuous picture scene: 'The swans flew while the turtle held the stick.'", "The swans are flying while the turtle is holding the stick.", "The swans flying while turtle holding stick.", "The swans were flying while turtle held stick.", "The swans will fly while turtle holds stick.", "A", "Both verbs transformed to present continuous (are flying, is holding)."),
        ("Spot the missing auxiliary verb in: 'The turtle falling and the swans flying.' Correct it:", "'The turtle **is** falling and the swans **are** flying.'", "'The turtle falling and swans flying.'", "'The turtle **are** falling and swans **is** flying.'", "No error.", "A", "Present continuous requires auxiliary (is/am/are) before -ing verb."),
        ("Differentiate state vs action: Why don't we usually say 'The turtle is **liking** the voice'?", "Because 'like' is a stative verb expressing a feeling/preference, not an ongoing physical action.", "Because 'liking' is hard to spell.", "Because turtle fell.", "Because swans flew.", "A", "Stative verbs (like, love, want) do not usually take continuous form."),
        ("Identify the sentence with CORRECT present continuous subject-verb agreement:", "The two swans are carrying the heavy turtle.", "The two swans is carrying the heavy turtle.", "The two swans am carrying the heavy turtle.", "The two swans carrying the heavy turtle.", "A", "Plural subject ('two swans') takes plural auxiliary 'are'."),
        ("Form negative present continuous: 'The turtle is listening to advice.' -> Negative:", "The turtle is **not** listening to advice.", "The turtle not listening to advice.", "The turtle is no listening to advice.", "The turtle isn't listen to advice.", "A", "Add 'not' between auxiliary 'is' and main verb 'listening'."),
        ("Spot all THREE spelling errors: 'He is **holdingg** the stick, **runing** fast, and **dieing**.'", "'holdingg' -> 'holding'; 'runing' -> 'running'; 'dieing' -> 'dying'", "'holdingg' -> 'holdng'; 'runing' -> 'runing'; 'dieing' -> 'dieing'", "No errors.", "Only 'runing' is wrong.", "A", "holding (single g), running (double n), dying (-ie to -y)."),
        ("Rewrite as interrogative present continuous: 'The turtle is opening his mouth.'", "**Is** the turtle opening his mouth?", "Are the turtle opening his mouth?", "The turtle opening his mouth?", "Why the turtle is opening mouth?", "A", "Move auxiliary 'Is' to beginning of sentence."),
        ("Analyze action timeline: 'The swans **are migrating** to the new lake tomorrow.' What does present continuous express here?", "A fixed future arrangement / planned action.", "Past completed action.", "Action that happened long ago.", "Uncertain rumor.", "A", "Present continuous can express planned future actions."),
        ("Choose the sentence showing PARALLEL present continuous actions:", "While the swans are flying, the villagers are watching.", "While swans flew, villagers are watching.", "Swans are flying while villagers watched.", "Swans fly while villagers watch.", "A", "Both parallel ongoing actions use present continuous."),
        ("Correct the error: 'The swans are flyying over the town.'", "'flyying' should be 'flying' (single 'y').", "'are' should be 'is'.", "'town' should be capitalized.", "No error.", "A", "Fly + ing = flying."),
        ("HOTS Reasoning: Compare 'The turtle fell' (Past Simple) vs 'The turtle is falling' (Present Continuous). How does the meaning change?", "Past simple states a completed past event; present continuous describes an action currently in progress.", "Both mean the exact same thing.", "Past simple is for future; continuous is for past.", "Continuous means turtle stayed on stick.", "A", "Tense changes temporal aspect (completed vs ongoing)."),
        ("Form question: 'Why ____ the turtle ____ (talking)?'", "is, talking", "are, talking", "am, talking", "do, talking", "A", "Singular subject turtle takes 'is ... talking'."),
        ("Identify the correct present continuous sentence describing animal flight:", "The pair of swans is soaring high above the clouds.", "The pair of swans is soar high above the clouds.", "The pair of swans are soaring high above the clouds.", "The pair of swans soaring high above the clouds.", "A", "Collective singular subject 'pair of swans' + is + soaring.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH03_CAT08_Q{idx:02d}"
        qtxt = f"Higher Order Present Continuous Analysis & Editing:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Continuous Tense Aspect & Error Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 9. Helping Verbs (Is, Am, Are) (50 Qs)
# ---------------------------------------------------------------------------
def build_helping_verbs():
    header = "# Category 9: Helping Verbs (Is, Am, Are) — Chapter 03: The Turtle and the Swans\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_hv = [
        ("The turtle ___ very talkative.", "is", "are", "am", "be", "A", "Singular subject 'The turtle' takes 'is'."),
        ("I ___ reading the fable of the Turtle and Swans.", "am", "is", "are", "be", "A", "Pronoun 'I' takes 'am'."),
        ("The two swans ___ good friends.", "are", "is", "am", "be", "A", "Plural subject 'two swans' takes 'are'."),
        ("The lake ___ drying up during summer.", "is", "are", "am", "be", "A", "Singular subject 'lake' takes 'is'."),
        ("The stick's ends ___ held by the swans.", "are", "is", "am", "be", "A", "Plural subject 'ends' takes 'are'."),
        ("The middle of the stick ___ held by the turtle.", "is", "are", "am", "be", "A", "Singular subject 'middle' takes 'is'."),
        ("The villagers ___ watching in awe.", "are", "is", "am", "be", "A", "Plural subject 'villagers' takes 'are'."),
        ("The turtle and the swans ___ flying together.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("I ___ sure that foolish talk leads to trouble.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The Panchatantra tale ___ short and wise.", "is", "are", "am", "be", "A", "Singular 'tale' takes 'is'."),
        ("The swans' wings ___ strong and wide.", "are", "is", "am", "be", "A", "Plural 'wings' takes 'are'."),
        ("The sky ___ clear and blue.", "is", "are", "am", "be", "A", "Singular 'sky' takes 'is'."),
        ("You ___ reading Chapter 03.", "are", "is", "am", "be", "A", "Pronoun 'You' always takes 'are'."),
        ("The turtle ___ falling down.", "is", "are", "am", "be", "A", "Singular 'turtle' takes 'is'."),
        ("The swans ___ flying to a new lake.", "are", "is", "am", "be", "A", "Plural 'swans' takes 'are'."),
        ("I ___ sad about the turtle's end.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The turtle ___ holding the stick with his mouth.", "is", "are", "am", "be", "A", "Singular 'turtle' takes 'is'."),
        ("The people ___ amazed by the sight.", "are", "is", "am", "be", "A", "Plural 'people' takes 'are'.")
    ]
    
    for idx, (sent_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_hv, start=1):
        qid = f"BK02_CH03_CAT09_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct helping verb (is / am / are):\n\n\"{sent_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Helping Verb Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Choose the correct helping verb: 'The first swan and the second swan ____ holding the stick.'", "are", "is", "am", "be", "A", "Compound subject ('first swan and second swan') is plural, taking 'are'."),
        ("Select the sentence with CORRECT helping verb agreement:", "The turtle is flying through the sky.", "The turtle are flying through the sky.", "The turtle am flying through the sky.", "The turtle be flying through the sky.", "A", "Singular noun 'turtle' requires 'is'."),
        ("Fill in the blanks: 'I ____ watching the swans, and the turtle ____ holding the stick.'", "am, is", "is, are", "are, is", "am, are", "A", "'I am', 'turtle is'."),
        ("Identify the mistake in: 'The swans' wings **is** very wide.'", "'is' should be 'are' because 'wings' is a plural noun.", "'is' should be 'am'", "'is' should be 'was'", "No mistake", "A", "'wings' is plural, requiring 'are'."),
        ("Which helping verb completes the question? '____ you ready to learn the moral of the story?'", "Are", "Is", "Am", "Be", "A", "Subject 'you' takes 'Are'."),
        ("Fill in the blank: 'Neither advice nor warning ____ effective on a foolish person.'", "is", "are", "am", "be", "A", "'Neither...nor' with singular second subject takes 'is'."),
        ("Select the correct sentence for story moral:", "Patience and self-control are valuable qualities.", "Patience and self-control is valuable qualities.", "Patience and self-control am valuable qualities.", "Patience and self-control be valuable qualities.", "A", "Compound subject 'Patience and self-control' takes 'are'."),
        ("Complete the conversation: Swans: 'Where ____ we flying?' Turtle: 'We ____ going to the new lake!'", "are, are", "is, is", "is, are", "are, is", "A", "Plural 'we' -> are; plural 'We' -> are."),
        ("Identify where 'is' is used incorrectly:", "The swans **is** flying high.", "The turtle is talkative.", "The lake is dry.", "The stick is strong.", "A", "'The swans is' should be 'The swans are'."),
        ("Choose the correct helping verb for collective noun used as a single unit: 'The flock of birds ____ flying together.'", "is", "are", "am", "be", "A", "Collective noun 'flock' treated as singular unit takes 'is'."),
        ("Fill in the blank: 'The turtle ____ not able to control his tongue.'", "is", "are", "am", "be", "A", "Singular 'turtle' takes 'is'."),
        ("Select the sentence with correct helping verb for 'I':", "I am looking at the flying turtle.", "I is looking at the flying turtle.", "I are looking at the flying turtle.", "I be looking at the flying turtle.", "A", "Subject 'I' takes 'am'."),
        ("Fill in the blank: 'There ____ two swans in the sky.'", "are", "is", "am", "be", "A", "'There are' before plural noun 'two swans'."),
        ("Fill in the blank: 'There ____ a talkative turtle in the lake.'", "is", "are", "am", "be", "A", "'There is' before singular noun 'a talkative turtle'."),
        ("Choose the correct sentence:", "What are the villagers doing near the field?", "What is the villagers doing near the field?", "What am the villagers doing near the field?", "What be the villagers doing near the field?", "A", "Plural subject 'the villagers' takes 'are'."),
        ("Identify the correct form: 'The turtle, as well as the swans, ____ leaving the dry lake.'", "is", "are", "am", "be", "A", "Subject is singular 'The turtle' ('as well as...' does not change subject number), taking 'is'."),
        ("Fill in the blank: 'Both the turtle and the swans ____ in danger.'", "are", "is", "am", "be", "A", "'Both ... and ...' takes plural verb 'are'."),
        ("Select the option with correct helping verbs: 'The turtle ____ slow, but the swans ____ fast.'", "is, are", "are, is", "am, are", "is, is", "A", "'turtle is', 'swans are'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH03_CAT09_Q{idx:02d}"
        qtxt = f"Helping Verb Subject-Verb Agreement Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Subject-Verb Agreement Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze subject-verb agreement: 'Each of the two swans **____** holding one end of the stick.' Choose the correct verb and reason:", "is — because 'Each' is a singular indefinite pronoun requiring singular verb 'is'.", "are — because 'two swans' is plural.", "am — because it refers to speaker.", "be — because swans fly.", "A", "'Each' is singular indefinite pronoun taking singular verb 'is'."),
        ("Spot the subtle agreement error in: 'A pair of white swans **are** flying above the lake.'", "'are' should be 'is' because the subject is singular noun 'pair'.", "'are' should be 'am'.", "'swans' should be 'swan'.", "No error.", "A", "'A pair' is singular, so it requires 'is flying'."),
        ("Compare: (1) 'The turtle and the swans **are** flying.' vs (2) 'The turtle, together with the swans, **is** flying.' Why are the verbs different?", "In (1), 'and' creates a plural subject (are); in (2), 'together with' is a prepositional phrase, leaving 'turtle' as sole singular subject (is).", "They mean different things.", "Sentence (2) is grammatically wrong.", "Both should use 'are'.", "A", "Prepositional phrases like 'together with' do not change subject number."),
        ("Identify the correct agreement for indefinite pronouns: 'Everyone in the town **____** looking up at the sky.'", "is", "are", "am", "be", "A", "'Everyone' is a singular indefinite pronoun requiring 'is'."),
        ("Spot all THREE subject-verb errors in: 'The swans **is** fast, I **is** watching, and the turtle **are** foolish.'", "'swans is' -> 'swans are'; 'I is' -> 'I am'; 'turtle are' -> 'turtle is'", "'swans is' -> 'swans am'; 'I is' -> 'I are'; 'turtle are' -> 'turtle am'", "Only 'I is' is wrong.", "No errors present.", "A", "swans are (plural), I am (1st person), turtle is (3rd person singular)."),
        ("Fill in the blanks in this complex sentence: 'Not only the turtle but also the swans **____** flying, while the villagers **____** shouting.'", "are, are", "is, are", "is, is", "are, is", "A", "'Not only...but also' agrees with closer subject ('swans' -> are); 'villagers' -> are."),
        ("Transform to negative: 'The turtle and the stick are on the ground.'", "The turtle and the stick **are not** on the ground.", "The turtle and the stick is not on the ground.", "The turtle and the stick am not on the ground.", "The turtle and the stick not on ground.", "A", "Add 'not' after plural helping verb 'are'."),
        ("Analyze inverted subject position: 'Above the cloudless sky **____** flying two graceful swans.'", "are", "is", "am", "be", "A", "Subject is plural 'two graceful swans', appearing after verb, requiring 'are'."),
        ("Determine agreement with uncountable nouns: 'The water in the old lake **____** completely gone.'", "is", "are", "am", "be", "A", "Uncountable noun 'water' is treated as singular, taking 'is'."),
        ("Correct the sentence: 'Here **is** the two swans coming to help.'", "Here **are** the two swans coming to help.", "Here am the two swans coming to help.", "Here be the two swans coming to help.", "No error.", "A", "Plural subject 'two swans' requires 'Here are...''"),
        ("Identify the sentence where 'is' acts as a MAIN linking verb rather than a helping verb:", "The turtle **is** a talkative creature.", "The turtle **is** flying in the air.", "The turtle **is** opening his mouth.", "The turtle **is** falling down.", "A", "In 'The turtle is a talkative creature', 'is' is the main linking verb connecting subject to predicate noun."),
        ("HOTS Reasoning: Why does English use 'am' ONLY with the subject pronoun 'I'?", "Because 'am' is the unique 1st person singular present indicative form of the verb 'to be'.", "Because 'I' is capitalized.", "Because swans commanded it.", "There is no reason.", "A", "'am' is exclusively reserved for 1st person singular 'I'."),
        ("Fill in the blanks: 'Neither the turtle nor his friends **____** happy about the drought, because the lake **____** dry.'", "are, is", "is, are", "is, is", "are, are", "A", "'friends' is closer plural subject -> are; 'lake' -> is."),
        ("Select the option with PERFECT helping verb agreement throughout:", "The lake is dry, I am amazed, and the swans are flying.", "The lake are dry, I is amazed, and the swans is flying.", "The lake am dry, I are amazed, and the swans am flying.", "The lake is dry, I is amazed, and the swans is flying.", "A", "lake is (singular), I am (1st person), swans are (plural).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH03_CAT09_Q{idx:02d}"
        qtxt = f"Higher Order Helping Verb Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Subject-Verb Agreement & Syntax", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# MAIN EXECUTION FOR REBUILDING CHAPTER 03
# ---------------------------------------------------------------------------
def rebuild_chapter_03():
    print("Rebuilding Chapter 03 category files with high-quality, multi-tiered (Easy/Medium/Hard) non-duplicate questions...")

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
        filepath = os.path.join(CH03_DIR, fname)
        print(f"  Generating {fname}...")
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {fname} created successfully.")

    print("\n[SUCCESS] Completed rebuilding all 9 category files for Chapter 03 (450 total high-quality questions)!")

if __name__ == "__main__":
    rebuild_chapter_03()
