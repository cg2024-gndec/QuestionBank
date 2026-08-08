r"""
=============================================================================
Script: rebuild_chapter_06.py
Description: Generates 50 rich, non-duplicate, multi-tiered (Easy, Medium, Hard)
             questions for each of the 9 category files in Chapter 06:
             "My Favourite Cartoon" (450 Qs total).
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH06_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_06")
os.makedirs(CH06_DIR, exist_ok=True)

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
    header = "# Category 1: Plural Nouns & Spelling Rules — Chapter 06: My Favourite Cartoon\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("cartoon", "cartoons", "cartoonies", "cartoonses", "cartoonz", "A", "Regular noun adding -s."),
        ("gadget", "gadgets", "gadgetes", "gadgeties", "gadgetz", "A", "Regular noun adding -s."),
        ("pocket", "pockets", "pocketes", "pocketies", "pocketz", "A", "Regular noun adding -s."),
        ("lesson", "lessons", "lessones", "lessonies", "lessonz", "A", "Regular noun adding -s."),
        ("trouble", "troubles", "troublies", "troublees", "troublez", "A", "Regular noun ending in -e adds -s."),
        ("situation", "situations", "situationes", "situationies", "situationz", "A", "Regular noun adding -s."),
        ("picture", "pictures", "picturies", "picturees", "picturez", "A", "Regular noun ending in -e adds -s."),
        ("century", "centuries", "centurys", "centuryes", "centuriz", "A", "Consonant + y changes to -ies."),
        ("story", "stories", "storys", "storyes", "storiez", "A", "Consonant + y changes to -ies."),
        ("boy", "boys", "boies", "boyes", "boiy", "A", "Vowel + y adds -s."),
        ("cat", "cats", "cates", "caties", "catz", "A", "Regular noun adding -s."),
        ("friend", "friends", "friendes", "friendies", "friendz", "A", "Regular noun adding -s."),
        ("year", "years", "yeares", "yearies", "yearz", "A", "Regular noun adding -s."),
        ("day", "days", "daies", "dayes", "dayz", "A", "Vowel + y adds -s."),
        ("show", "shows", "showes", "showies", "showz", "A", "Regular noun adding -s."),
        ("episode", "episodes", "episodies", "episodees", "episodez", "A", "Regular noun ending in -e adds -s."),
        ("child", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("person", "people", "persons", "peoples", "persones", "A", "Irregular plural: person becomes people.")
    ]
    
    for idx, (word, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH06_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{word}'** from or related to Chapter 06 (*My Favourite Cartoon*)?"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Plural Noun Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Doraemon fetches futuristic (gadget / gadgets) from his pocket.", "gadgets", "gadget", "gadgetes", "gadgeties", "A", "Plural noun 'gadgets'."),
        ("Doraemon has saved Nobita from many (trouble / troubles).", "troubles", "trouble", "troublies", "troublees", "A", "'many' requires plural noun 'troubles'."),
        ("The cartoon series spans over two (century / centuries).", "centuries", "century", "centurys", "centuryes", "A", "Consonant + y changes to -ies (centuries)."),
        ("Identify the INCORRECT plural spelling in this list: lessons, pockets, storys, friends.", "storys", "lessons", "pockets", "friends", "A", "Plural of story is 'stories', not 'storys'."),
        ("Choose the sentence with the correct plural noun form:", "Doraemon teaches valuable life lessons.", "Doraemon teaches valuable life lessones.", "Doraemon teaches valuable life lessonies.", "Doraemon teaches valuable life lessonz.", "A", "lessons is the correct plural of lesson."),
        ("Which noun forms its plural by changing consonant + y to -ies?", "century -> centuries", "boy -> boys", "pocket -> pockets", "gadget -> gadgets", "A", "Century ends in consonant + y, so plural is centuries."),
        ("Change the singular noun in brackets to plural: 'The children watched five ____ (episode) of Doraemon.'", "episodes", "episodies", "episodees", "episodez", "A", "Regular noun ending in -e adds -s (episodes)."),
        ("Select the sentence where ALL plural nouns are spelt correctly:", "The boys learned lessons from the cartoons.", "The boies learned lessones from the cartoons.", "The boys learned lessonies from the cartoones.", "The boyes learned lessons from the cartoons.", "A", "boys, lessons, cartoons are all correctly spelt plurals."),
        ("What is the correct plural of 'robotic cat'?", "robotic cats", "robotic cates", "robotic caties", "robotic catz", "A", "Regular noun adding -s."),
        ("Doraemon has been popular for many (year / years).", "years", "yeares", "yearies", "yearz", "A", "Regular noun adding -s (years)."),
        ("The show teaches children about true (friendship / friendships).", "friendships", "friendshipes", "friendshipies", "friendshipz", "A", "Plural of friendship is friendships."),
        ("Millions of (child / children) watch Doraemon every day.", "children", "childs", "childes", "childrens", "A", "Irregular plural of child is children."),
        ("How many (situation / situations) did Doraemon solve?", "situations", "situation", "situationes", "situationies", "A", "Plural noun 'situations'."),
        ("The two (creator / creators) worked together on the series.", "creators", "creatores", "creator", "creatories", "A", "Plural of creator is creators."),
        ("Which plural noun rule applies to the word **'boxes'**?", "Add -es to nouns ending in -x", "Add -s to vowel + y", "Change -f to -ves", "Change -y to -ies", "A", "Box ends in -x, so it adds -es."),
        ("Doraemon pulls tools from his magic (pocket / pockets).", "pockets", "pocketes", "pocket", "pocketies", "A", "Plural noun 'pockets'."),
        ("Identify the correct plural form of 'person':", "people", "persons", "peoples", "persones", "A", "Irregular plural: person becomes people."),
        ("Nobita faced many difficult (task / tasks).", "tasks", "taskes", "task", "taskies", "A", "Regular noun adding -s.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH06_CAT01_Q{idx:02d}"
        qtxt = f"Contextual Plural Rule Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Plural Noun Application", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Rewrite the sentence in PLURAL form: 'The boy used a gadget to solve a problem.'", "The boys used gadgets to solve problems.", "The boies used gadgetes to solve problemes.", "The boys used gadget to solve problems.", "The boyes used gadgets to solve problemz.", "A", "Plural of boy->boys, gadget->gadgets, problem->problems."),
        ("Analyze the error: 'Doraemon gave Nobita much advices.' Why is 'advices' inappropriate here?", "'advice' is an uncountable noun, so 'advice' (or 'pieces of advice') should be used.", "'advices' should be 'adviceses'.", "'advices' should be 'advicies'.", "No error.", "A", "Abstract uncountable nouns like advice do not normally take plural form."),
        ("Complete the paragraph with correct plurals: 'The two ____ (friend) experienced many ____ (adventure) in different ____ (century).'", "friends, adventures, centuries", "friendes, adventuries, centurys", "friends, adventure, centuriz", "friendes, adventures, centuries", "A", "friends (-s), adventures (-e + s), centuries (-y -> -ies)."),
        ("Identify the sentence where ALL three underlined nouns are correctly pluralized:", "The **children** pulled **gadgets** from their **pockets**.", "The **childs** pulled **gadgetes** from their **pockets**.", "The **childrens** pulled **gadgeties** from their **pocketes**.", "The **childes** pulled **gadgets** from their **pockets**.", "A", "children (irregular), gadgets (-s), pockets (-s)."),
        ("Which group contains ONLY irregular plural nouns?", "children, people, men, feet", "cartoons, gadgets, pockets, lessons", "stories, centuries, cities, armies", "leaves, thieves, wolves, knives", "A", "children, people, men, feet change forms without standard -s/-es."),
        ("Why does 'boy' become 'boys' but 'story' becomes 'stories'?", "Because 'boy' has a vowel before y (o+y -> -s), while 'story' has a consonant before y (r+y -> -ies).", "Because 'boy' is short and 'story' is long.", "Because 'boy' is a person and 'story' is a text.", "Both follow the exact same rule.", "A", "Vowel+y adds -s; Consonant+y changes y to -ies."),
        ("Find the TWO grammatical mistakes in: 'The two boies watched many mouses on television.'", "'boies' should be 'boys' and 'mouses' should be 'mice'.", "'boies' should be 'boy' and 'mouses' should be 'mices'.", "'television' should be 'televisions' only.", "There are no mistakes in the sentence.", "A", "boys (vowel + y) and mice (irregular plural)."),
        ("Replace the singular words in brackets: 'Doraemon raised his ____ (hand) and moved his ____ (foot).'", "hands, feet", "handes, foots", "hands, feets", "handies, foots", "A", "Plural of hand is hands, plural of foot is feet."),
        ("Analyze this sentence: 'Doraemon gives good advice.' Can 'advice' be pluralized as 'advices'?", "No, 'advice' is an uncountable noun; we say 'pieces of advice' for plural.", "Yes, 'advices' is correct.", "No, it becomes 'advicess'.", "Yes, 'an advice' is correct.", "A", "Advice is an uncountable noun."),
        ("Fill in the blanks: 'The two ____ (boy) faced many ____ (trouble) in school.'", "boys, troubles", "boies, troublies", "boys, troublees", "boies, troubles", "A", "boy -> boys; trouble -> troubles."),
        ("Select the option that shows correct plural transformation for ALL three words: 'hero', 'city', 'box'", "heroes, cities, boxes", "heros, citys, boxs", "heroes, cityes, boxies", "heroes, cities, foxen", "A", "hero -> heroes (-o + es); city -> cities; box -> boxes."),
        ("HOTS Reasoning: Why do we say 'magic is fun' rather than 'magics are fun'?", "Because 'magic' is an uncountable abstract noun that stays singular.", "Because magic comes from pockets.", "Because Doraemon is blue.", "Because Nobita sleeps.", "A", "Uncountable abstract nouns take singular verbs."),
        ("Transform into singular: 'The robotic cats fetched the gadgets from the pockets.'", "The robotic cat fetched the gadget from the pocket.", "The robotic cats fetched the gadget from the pocket.", "The robotic cat fetch the gadget from the pocket.", "The robotic cat fetched the gadgets from the pocket.", "A", "Singular forms: cat, gadget, pocket."),
        ("Identify the correct rule for forming the plural of **'gadget'**:", "Add -s because it is a regular noun ending in a consonant (gadgets).", "Add -es (gadgetes).", "Change -t to -ves (gadgevs).", "Change vowel sound.", "A", "Regular noun adding -s.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH06_CAT01_Q{idx:02d}"
        qtxt = f"Higher Order Thinking Skills (HOTS) & Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Plural & Spelling Analysis", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 2. Articles Grammar (50 Qs)
# ---------------------------------------------------------------------------
def build_articles_grammar():
    header = "# Category 2: Articles (A, An, The) — Chapter 06: My Favourite Cartoon\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("Doraemon is ___ robotic cat from the 22nd century.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'robotic'."),
        ("Doraemon is ___ earless cat.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'earless'."),
        ("He was created by ___ Japanese artist.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'Japanese'."),
        ("Doraemon has ___ fourth-dimensional pocket.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'fourth-dimensional'."),
        ("Nobita is ___ lazy boy.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'lazy'."),
        ("___ Panchatantra/Animation story teaches moral values.", "An / A", "An", "A", "No article", "C", "Use 'A' before consonant sound 'Panchatantra/Animation'."),
        ("Doraemon pulls ___ futuristic gadget from his pouch.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'futuristic'."),
        ("Doraemon is ___ honest friend to Nobita.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' sound in 'honest'."),
        ("___ series teaches responsibility and friendship.", "The", "A", "An", "No article", "A", "Use 'The' for specific series in context."),
        ("Nobita often gets into ___ unusual trouble.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'unusual'."),
        ("It is ___ popular anime series worldwide.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'popular'."),
        ("Doraemon came from ___ 22nd century.", "the", "a", "an", "no article", "A", "Use 'the' for ordinal century 'the 22nd century'."),
        ("___ blue robotic cat helps Nobita every day.", "The", "A", "An", "No article", "A", "Use 'The' for specific cat Doraemon."),
        ("Doraemon has ___ charming personality.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'charming'."),
        ("Nobita is ___ schoolboy in Japan.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'schoolboy'."),
        ("Doraemon is ___ iconic cartoon character.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'iconic'."),
        ("The cartoon brings ___ happiness to children.", "no article", "a", "an", "the", "A", "Abstract noun 'happiness' takes no indefinite article here."),
        ("___ sun set while Nobita did his homework.", "The", "A", "An", "No article", "A", "Use 'The' for unique celestial object 'sun'.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH06_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article (a / an / the / no article):\n\n\"{q_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Basic Article Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Doraemon helps ___ boy named Nobita and uses ___ gadget to solve problems.", "a, a", "the, an", "an, a", "a, the", "A", "'a boy' (first mention), 'a gadget' (consonant sound)."),
        ("Why do we say '**a** robotic cat' but '**an** earless cat'?", "Because 'robotic' begins with a consonant sound (r) and 'earless' with a vowel sound (e).", "Because Doraemon flies.", "Because Nobita is lazy.", "Because 22nd century is future.", "A", "Article selection depends on initial vowel/consonant sound."),
        ("Select the sentence with CORRECT article usage:", "Doraemon is a robotic cat with a 4D pocket.", "Doraemon is an robotic cat with an 4D pocket.", "Doraemon is the a robotic cat.", "Doraemon is a an robotic cat.", "A", "'a robotic' (/r/) and 'a 4D' (/f/) both take 'a'."),
        ("Fill in the blanks: 'Doraemon came from ___ future to help ___ lazy boy.'", "the, a", "a, a", "an, an", "a, the", "A", "'the future' (unique concept), 'a lazy boy' (consonant sound)."),
        ("Identify the INCORRECT article in: 'Doraemon gave Nobita **a** unusual gadget.'", "'a' should be 'an'", "'a' should be 'the'", "'unusual' should be 'a unusual'", "No mistake", "A", "'unusual' starts with vowel sound /u/, so it takes 'an'."),
        ("Which article completes the sentence? 'Time travel requires ___ active imagination.'", "an", "a", "the", "no article", "A", "'active' starts with vowel sound /a/, requiring 'an'."),
        ("Choose the correct pair of articles: '___ cat fetched ___ magic tool.'", "The, a", "A, a", "An, an", "The, the", "A", "'The cat' (specific Doraemon), 'a magic tool' (consonant sound)."),
        ("Why do we use 'a' before 'futuristic gadget' in 'He has **a** futuristic gadget'?", "Because 'futuristic' begins with the consonant sound /f/.", "Because gadget is a noun.", "Because 22nd century is far.", "Because Nobita is young.", "A", "'futuristic' starts with consonant sound /f/."),
        ("Complete the dialogue: Nobita: 'Give me ___ gadget!' Doraemon: 'I have ___ special tool!'", "a, a", "a, an", "an, the", "the, the", "A", "'a gadget' (consonant sound), 'a special tool' (consonant sound)."),
        ("Select the correct sentence:", "A cartoon is an entertaining show.", "An cartoon is an entertaining show.", "The cartoon is a entertaining show.", "An cartoon is a entertaining show.", "A", "'A cartoon' (consonant sound), 'an entertaining show' (vowel sound)."),
        ("Fill in the blank: 'Nobita slept for ___ long time before doing homework.'", "a", "an", "the", "no article", "A", "Idiomatic phrase 'for a long time'."),
        ("Identify where NO article is needed:", "The series teaches **___ responsibility** and friendship.", "Doraemon pulled out ___ gadget.", "He helped ___ boy.", "He lived in ___ house.", "A", "Abstract noun 'responsibility' takes no indefinite article here."),
        ("Choose the correct sentence for story summary:", "Friendship and hard work lead to success.", "A friendship and an hard work lead to success.", "An friendship and a hard work lead to success.", "The friendship a leads to success.", "A", "Abstract concepts take no indefinite articles in general sense."),
        ("Fill in the blanks: 'Doraemon spent ___ hour fixing ___ broken gadget.'", "an, a", "a, a", "an, an", "the, an", "A", "'an hour' (silent h), 'a broken gadget' (consonant b)."),
        ("Which sentence uses 'the' correctly for ordinal numbers?", "Doraemon came from the 22nd century.", "Doraemon came from a 22nd century.", "Doraemon came from an 22nd century.", "Doraemon came from 22nd century.", "A", "Ordinal number 'the 22nd' takes 'the'."),
        ("Identify the article error: 'Doraemon gave **a** explanation after **an** short delay.'", "'an short' should be 'a short' and 'a explanation' should be 'an explanation'", "'a explanation' should be 'an explanation'", "'an short' should be 'a short'", "No error", "A", "'an explanation' (vowel /e/) and 'a short delay' (consonant /s/)."),
        ("Complete: 'It was ___ unexpected adventure in ___ 22nd century.'", "an, the", "a, an", "the, the", "an, an", "A", "an unexpected (/u/), the 22nd century (ordinal)."),
        ("Choose the correct option: '___ sun shone over Japan.'", "The", "A", "An", "No article", "A", "'The sun' (unique celestial body).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH06_CAT02_Q{idx:02d}"
        qtxt = f"Contextual Article Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Article Usage in Context", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze article usage in: 'Doraemon pulls **a** magic from **the** pocket.' Correct the error:", "'pulls a magic' -> 'pulls magic' (uncountable abstract noun magic takes no article 'a').", "'the pocket' -> 'an pocket'.", "'pulls a magic' -> 'pulls an magic'.", "No error present.", "A", "'magic' is uncountable and takes no article 'a'."),
        ("Fill in all three blanks: '___ robotic cat told ___ boy that ___ hard work is necessary.'", "The, the, no article", "A, an, a", "An, a, the", "The, a, a", "A", "'The robotic cat' (specific), 'the boy' (specific), 'hard work' (general abstract)."),
        ("Identify why 'the' is used in: 'Nobita opened **the** fourth-dimensional pocket.'", "Because 'the fourth-dimensional pocket' refers to the specific pocket on Doraemon's belly.", "Because pocket is a proper noun.", "Because Nobita is lazy.", "Because 22nd century is far.", "A", "'The' specifies the definite unique pocket."),
        ("Spot the TWO article errors: 'It took **a** hour for **a** eagle to fly past Japan.'", "'a hour' should be 'an hour' and 'a eagle' should be 'an eagle'.", "'a hour' should be 'the hour' and 'a eagle' should be 'a eagle'.", "No errors.", "Only 'a hour' is wrong.", "A", "Both 'hour' (silent h) and 'eagle' (vowel e) require 'an'."),
        ("Choose the paragraph with PERFECT article usage throughout:", "A robotic cat came from the future. He met a lazy boy. The cat helped the boy with gadgets.", "An robotic cat came from a future. He met an lazy boy. A cat helped a boy.", "The robotic cat came from an future.", "A robotic cat came from a future. The cat was an honest.", "A", "A robotic cat (first mention), the future (unique), a lazy boy (consonant), The cat / the boy (second mention)."),
        ("Why is it correct to write 'a unique gadget' but 'an unusual gadget'?", "Because 'unique' begins with consonant sound /j/ (yoo), while 'unusual' begins with vowel sound /u/.", "Because unique is longer.", "Because gadget is noun.", "Both take 'an'.", "A", "Sound determines article: /yoo/ is a consonant sound."),
        ("Select the option that correctly completes the story moral: '___ good friend helps in ___ time of trouble and teaches ___ valuable lesson.'", "A, a, a", "An, a, an", "The, the, the", "A, an, a", "A", "A good friend, a time of trouble, a valuable lesson."),
        ("Analyze this sentence: 'Doraemon went back to **the** past.' Why is 'the' appropriate?", "Because it refers to the specific historical time period of Nobita's childhood.", "Because past is in Japan.", "Because past is plural.", "Because Doraemon is cat.", "A", "'the' specifies the definite time period."),
        ("Correct the sentence: 'An robotic cat gave a gadget to a boy.'", "A robotic cat gave a gadget to the boy.", "The robotic cat gave an gadget to a boy.", "An robotic cat gave the gadget to the boy.", "A robotic cat gave a gadget to a boy.", "A", "'A robotic cat' (/r/ sound), 'a gadget' (/g/ sound), 'the boy' (specific)."),
        ("Fill in the blanks: '___ gadgets in ___ pocket were created in ___ 22nd century.'", "The, the, the", "A, a, a", "No article, a, an", "An, the, a", "A", "'The gadgets' (specific), 'the pocket' (specific), 'the 22nd century' (ordinal)."),
        ("Spot the missing article: 'Doraemon pulled out gadget and handed it to Nobita.'", "Missing 'a' before 'gadget' -> 'pulled out a gadget...'", "Missing 'an' before 'handed'", "Missing 'the' before 'out'", "No article is missing", "A", "Indefinite singular noun 'a gadget' needs 'a'."),
        ("HOTS Reasoning: Which sentence uses 'a', 'an', and 'the' correctly in a single rule demonstration?", "An earless cat gave a gadget to the boy.", "A earless cat gave an gadget to a boy.", "The earless cat gave an gadget to an boy.", "An earless cat gave an gadget to the boy.", "A", "An earless (vowel), a gadget (consonant), the boy (specific)."),
        ("Rewrite correctly: 'Doraemon was a honest cat who had an 4D pocket.'", "Doraemon was an honest cat who had a 4D pocket.", "Doraemon was a honest cat who had a 4D pocket.", "Doraemon was an honest cat who had an 4D pocket.", "Doraemon was the honest cat who had an 4D pocket.", "A", "'an honest' (silent h), 'a 4D' (consonant sound /f/)."),
        ("Identify the correct rule for using 'the' with ordinal numbers (first, 21st, 22nd):", "Ordinal numbers take 'the' because they indicate a specific position in a sequence.", "Ordinal numbers take 'an'.", "Ordinal numbers never take articles.", "Ordinal numbers take 'a' only.", "A", "'The first', 'the 22nd century' take 'the'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH06_CAT02_Q{idx:02d}"
        qtxt = f"Higher Order Article Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Article Analysis & Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 3. Calendar & Days Vocabulary (50 Qs)
# ---------------------------------------------------------------------------
def build_calendar_days():
    header = "# Category 3: Calendar, Days & Abbreviations — Chapter 06: My Favourite Cartoon\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    days_easy = [
        ("Doraemon was first introduced in the year **1969**. How many years are in 1 decade?", "10 years", "100 years", "5 years", "50 years", "A", "1 decade = 10 years."),
        ("What is the standard abbreviation for **Sunday**?", "Sun.", "Snd.", "Su.", "Sn.", "A", "Sun. is standard abbreviation."),
        ("Which day comes right after Friday?", "Saturday", "Sunday", "Thursday", "Monday", "A", "Saturday follows Friday."),
        ("What is the abbreviation for **Saturday**?", "Sat.", "Satur.", "Sa.", "St.", "A", "Sat. is standard abbreviation."),
        ("If Nobita watches cartoons 7 days a week, how many weekend days does he watch (Sat-Sun)?", "2 weekend days", "5 weekend days", "1 weekend day", "0 weekend days", "A", "Saturday and Sunday are 2 weekend days."),
        ("Which month comes right before December?", "November", "October", "January", "September", "A", "November comes before December."),
        ("What is the short abbreviation for **December**?", "Dec.", "Dece.", "Dc.", "Dcm.", "A", "Dec. is standard abbreviation."),
        ("Nobita watches cartoons in the **afternoon** after school. What time of day is 12:00 PM?", "Noon / Midday", "Midnight", "Dawn", "Twilight", "A", "Noon/midday is 12:00 PM."),
        ("What is the abbreviation for **Wednesday**?", "Wed.", "Weds.", "We.", "W.", "A", "Wed. is standard abbreviation."),
        ("How many years are in 1 century?", "100 years", "10 years", "1000 years", "50 years", "A", "1 century = 100 years."),
        ("Which month comes right after August?", "September", "October", "July", "June", "A", "September comes after August."),
        ("What is the short abbreviation for **September**?", "Sept. or Sep.", "Spt.", "Septe.", "St.", "A", "Sept. or Sep. is standard abbreviation."),
        ("If today is Wednesday, what day was yesterday?", "Tuesday", "Thursday", "Monday", "Friday", "A", "Yesterday was Tuesday."),
        ("If today is Thursday, what day will tomorrow be?", "Friday", "Wednesday", "Saturday", "Sunday", "A", "Tomorrow will be Friday."),
        ("What is the abbreviation for **Thursday**?", "Thu. / Thurs.", "Thr.", "Ths.", "Tu.", "A", "Thu. is standard abbreviation."),
        ("Which day comes between Monday and Wednesday?", "Tuesday", "Thursday", "Friday", "Sunday", "A", "Tuesday is between Monday and Wednesday."),
        ("What is the abbreviation for **January**?", "Jan.", "Jny.", "Ja.", "Jn.", "A", "Jan. is standard abbreviation."),
        ("Which month comes right before March?", "February", "January", "April", "May", "A", "February comes before March.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(days_easy, start=1):
        qid = f"BK02_CH06_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Vocabulary & Time Concepts:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Days & Calendar Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Nobita got a futuristic gadget on **Monday**. He used it for 3 days before returning it. On which day did he return it?", "Thursday", "Wednesday", "Friday", "Saturday", "A", "Monday + 3 days = Tuesday(1), Wednesday(2), Thursday(3)."),
        ("Nobita watched cartoons from **4:00 PM to 5:30 PM**. How many minutes did he watch?", "90 minutes (1.5 hours)", "60 minutes", "120 minutes", "45 minutes", "A", "1 hour 30 minutes = 90 minutes."),
        ("Match the day with its abbreviation: **Friday**", "Fri.", "Frid.", "Fr.", "F.", "A", "Fri. is standard."),
        ("If Doraemon spent 22 centuries in time travel, how many years is 1 century?", "100 years", "10 years", "1000 years", "50 years", "A", "1 century = 100 years (22nd century = year 2101-2200)."),
        ("Identify the correctly spelt month name:", "February", "Febuary", "Februery", "Febraury", "A", "February is the correct spelling."),
        ("Identify the INCORRECT pair of day and abbreviation:", "Monday - Mon.", "Tuesday - Tue.", "Wednesday - Wed.", "Friday - Frd.", "D", "Friday abbreviation is Fri., not Frd."),
        ("Doraemon was created in **1969**. How many years from 1969 to 1979?", "10 years (1 decade)", "5 years", "20 years", "100 years", "A", "1979 - 1969 = 10 years."),
        ("Which month has 31 days and comes right after May?", "July (has 31) / June (has 30)", "July", "June", "August", "A", "July has 31 days and follows June."),
        ("Rearrange in correct chronological order: Mon, Wed, Tue, Thu", "Mon, Tue, Wed, Thu", "Mon, Wed, Tue, Thu", "Tue, Mon, Wed, Thu", "Thu, Wed, Tue, Mon", "A", "Monday -> Tuesday -> Wednesday -> Thursday."),
        ("What day is 4 days before Sunday?", "Wednesday", "Thursday", "Tuesday", "Friday", "A", "Sunday - 4 days = Saturday(1), Friday(2), Thursday(3), Wednesday(4)."),
        ("If an episode lasts 20 minutes, how many episodes can Nobita watch in 1 hour?", "3 episodes", "2 episodes", "4 episodes", "5 episodes", "A", "1 hour = 60 minutes. 60 / 20 = 3 episodes."),
        ("Select the month that has 30 days:", "April", "May", "July", "August", "A", "April has 30 days."),
        ("Which abbreviation stands for **February**?", "Feb.", "Febr.", "Fe.", "Fb.", "A", "Feb. is standard abbreviation."),
        ("If today is **Mon.**, what day will it be after 7 days?", "Monday", "Tuesday", "Sunday", "Friday", "A", "7 days is a full week cycle, landing on Monday again."),
        ("Nobita did homework from **6:00 PM to 7:00 PM**. How many minutes did he study?", "60 minutes (1 hour)", "30 minutes", "90 minutes", "45 minutes", "A", "1 hour = 60 minutes."),
        ("Identify the word that means 'occurring once every week':", "Weekly", "Daily", "Monthly", "Yearly", "A", "Weekly means once a week."),
        ("Which of the following is a weekend day?", "Sunday", "Monday", "Tuesday", "Wednesday", "A", "Sunday is a weekend day."),
        ("Choose the correct abbreviation for **November**:", "Nov.", "Nove.", "Nv.", "Nm.", "A", "Nov. is standard.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH06_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Application & Story Timeline:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Calendar & Time Reasoning", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Nobita used a time machine from **Mon., 1st Dec.** to **Fri., 5th Dec.**. How many days did he travel?", "5 days", "4 days", "3 days", "7 days", "A", "1st to 5th Dec inclusive is 5 days."),
        ("Doraemon helped Nobita with homework from **4:15 PM to 5:15 PM**. For how many minutes did they study?", "60 minutes (1 hour)", "45 minutes", "90 minutes", "30 minutes", "A", "1 hour = 60 minutes."),
        ("Solve the calendar puzzle: If 1st December 1969 was a Monday, what day of the week was 8th December 1969?", "Monday", "Tuesday", "Sunday", "Friday", "A", "1 + 7 = 8th December, landing on Monday."),
        ("Analyze this schedule: Nobita watches cartoons on Mon, Wed, Fri; Doraemon rests on Tue, Thu, Sat. On which day do BOTH rest?", "Sunday", "Monday", "Saturday", "Wednesday", "A", "Sunday is not listed in schedule."),
        ("Complete the full series of day abbreviations: Mon., Tue., Wed., Thu., Fri., Sat., ____.", "Sun.", "Sund.", "Su.", "Sn.", "A", "Sun. completes the 7 days of the week."),
        ("If a cartoon series aired for a fortnight, how many days did it air?", "14 days (2 weeks)", "7 days", "30 days", "3 days", "A", "A fortnight is 14 days."),
        ("Spot the error in the calendar sequence: 'Jan, Feb, Apr, Mar, May'", "April and March are in wrong order.", "February is in wrong position.", "May should be first.", "No error.", "A", "March comes before April (Jan, Feb, Mar, Apr, May)."),
        ("The cartoon festival ended on **31st December**. What date was the next day?", "1st January", "32nd December", "30th December", "1st February", "A", "December has 31 days, so next day is 1st January."),
        ("If yesterday was two days before Tuesday, what day is tomorrow?", "Tuesday", "Monday", "Wednesday", "Sunday", "A", "Two days before Tuesday = Sunday (yesterday). Today = Monday. Tomorrow = Tuesday."),
        ("Calculate: How many days are there in total during **December** and **January** combined?", "62 days (31 + 31)", "60 days", "61 days", "59 days", "A", "Both December (31) and January (31) have 31 days. 31 + 31 = 62 days."),
        ("HOTS Reasoning: What is the mathematical difference between 22nd century and 21st century?", "100 years (1 century)", "10 years", "1000 years", "50 years", "A", "22nd century - 21st century = 1 century = 100 years."),
        ("Identify the correct statement about a leap year:", "A leap year has 366 days and February has 29 days.", "A leap year has 365 days.", "February has 28 days in leap year.", "A leap year occurs every 3 years.", "A", "Leap year has 366 days (Feb = 29 days)."),
        ("Doraemon gave Nobita 60 gadgets over 3 months. How many gadgets per month did Nobita get?", "20 gadgets per month", "10 gadgets", "30 gadgets", "15 gadgets", "A", "60 / 3 = 20 gadgets per month."),
        ("Which month pair both have 31 days and come right after each other at the end of the year and start of next year?", "December and January", "November and December", "October and November", "January and February", "A", "December (31) and January (31) are consecutive 31-day months across new year.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH06_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Logic & Mathematical Time Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Calendar & Time Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 4. Action Verbs Identification (50 Qs)
# ---------------------------------------------------------------------------
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification — Chapter 06: My Favourite Cartoon\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_verbs = [
        ("Fujiko F. Fujio **created** Doraemon in 1969.", "created", "Fujiko", "Doraemon", "in", "A", "'created' is the action verb."),
        ("Doraemon **travels** back in time.", "travels", "Doraemon", "back", "time", "A", "'travels' is the action verb."),
        ("Doraemon **helps** Nobita in trouble.", "helps", "Doraemon", "Nobita", "trouble", "A", "'helps' is the action verb."),
        ("Doraemon **fetches** gadgets from his pocket.", "fetches", "Doraemon", "gadgets", "pocket", "A", "'fetches' is the physical action verb."),
        ("The gadgets **lead** to adventurous situations.", "lead", "gadgets", "adventurous", "situations", "A", "'lead' is the action verb."),
        ("The series **teaches** valuable life lessons.", "teaches", "series", "valuable", "lessons", "A", "'teaches' is the action verb."),
        ("Nobita **gets** into trouble at school.", "gets", "Nobita", "trouble", "school", "A", "'gets' is the action verb."),
        ("Children **watch** Doraemon on TV.", "watch", "children", "Doraemon", "TV", "A", "'watch' is the action verb."),
        ("Doraemon **opens** his 4D pocket.", "opens", "Doraemon", "his", "pocket", "A", "'opens' is the physical action verb."),
        ("Nobita **cries** when he loses his homework.", "cries", "Nobita", "when", "homework", "A", "'cries' is the action verb."),
        ("Doraemon **gives** Nobita a flying gadget.", "gives", "Doraemon", "Nobita", "gadget", "A", "'gives' is the action verb."),
        ("Nobita **flies** over the city.", "flies", "Nobita", "over", "city", "A", "'flies' is the action verb."),
        ("Doraemon **warns** Nobita to be responsible.", "warns", "Doraemon", "Nobita", "responsible", "A", "'warns' is the action verb."),
        ("Nobita **learns** the value of hard work.", "learns", "Nobita", "value", "work", "A", "'learns' is the mental action verb."),
        ("Doraemon **smiles** at his best friend.", "smiles", "Doraemon", "his", "friend", "A", "'smiles' is the action verb."),
        ("The friends **play** together in the park.", "play", "friends", "together", "park", "A", "'play' is the action verb."),
        ("Doraemon **saves** Nobita from giant bullies.", "saves", "Doraemon", "Nobita", "bullies", "A", "'saves' is the action verb."),
        ("Children **love** watching the animated show.", "love", "children", "watching", "show", "A", "'love' is the emotional action verb.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_verbs, start=1):
        qid = f"BK02_CH06_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in this sentence from or related to Chapter 06:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Action Verb Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Which word from the sentence is an **action verb**? 'Doraemon **quickly** **pulled** a **magic** **gadget**.'", "pulled", "quickly", "magic", "gadget", "A", "'pulled' shows physical action; 'quickly' is adverb, 'magic' is adjective, 'gadget' is noun."),
        ("Identify BOTH action verbs in: 'Doraemon **opened** his pouch and **pulled** out a tool.'", "opened, pulled", "Doraemon, pouch", "tool, opened", "pulled, pouch", "A", "'opened' and 'pulled' are both action verbs."),
        ("What is the past tense action verb of 'teach' as used in story ('teaches life lessons')?", "taught", "teached", "teaching", "teaches", "A", "Past tense of teach is taught."),
        ("Choose the sentence where the underlined word is used as an ACTION VERB:", "Nobita will **fly** using the bamboo copter.", "The bird has a high **fly**.", "Look at the **fly** on the wall.", "There is a **fly** in the room.", "A", "In (A), 'fly' acts as the main action verb."),
        ("Find the action verb in: 'Doraemon brought hope to Nobita.'", "brought", "Doraemon", "hope", "Nobita", "A", "'brought' is the action verb."),
        ("Which sentence contains NO physical action verb?", "Doraemon is a robotic cat.", "He pulled out a gadget.", "He flew over the town.", "He helped his friend.", "A", "'Doraemon is a robotic cat' contains linking verb 'is', but no physical action verb."),
        ("Change the action verb 'fly' to past tense: 'Nobita (fly) above the trees.'", "flew", "flyed", "flying", "flies", "A", "Past tense of fly is flew."),
        ("Identify the action verb: 'Doraemon saved Nobita and warned him about greed.'", "saved, warned", "Doraemon, Nobita", "greed, saved", "warned, Nobita", "A", "'saved' and 'warned' are action verbs."),
        ("Select the action verb that completes the sentence: 'The show ____ children around the world.'", "entertains / inspires", "robotic", "blue", "cartoon", "A", "'entertains' / 'inspires' is an action verb."),
        ("Which word is an action verb? (gadgets, pocket, fetched, robotic)", "fetched", "gadgets", "pocket", "robotic", "A", "'fetched' is an action verb; others are nouns/adjectives."),
        ("What action did Doraemon perform to help Nobita?", "fetched", "robotic", "earless", "blue", "A", "Doraemon fetched gadgets (action verb)."),
        ("Identify the action verb in: 'Nobita thought about his mistakes.'", "thought", "Nobita", "about", "mistakes", "A", "'thought' is a mental action verb."),
        ("Choose the correct action verb: 'Doraemon ____ time to arrive in 20th century.'", "traveled", "time", "century", "future", "A", "'traveled' is the action verb."),
        ("Identify the action verb in: 'The cartoon teaches important lessons.'", "teaches", "cartoon", "important", "lessons", "A", "'teaches' is the action verb."),
        ("Which of these words is NOT an action verb? (help, fetch, blue, teach)", "blue", "help", "fetch", "teach", "A", "'blue' is an adjective; others are action verbs."),
        ("Identify the action verb in: 'Nobita smiled at Doraemon.'", "smiled", "Nobita", "at", "Doraemon", "A", "'smiled' is the action verb."),
        ("Fill in the blank with an appropriate action verb: 'Doraemon ____ the magic pocket.'", "unzipped / opened", "blue", "futuristic", "cat", "A", "'unzipped' / 'opened' is an action verb."),
        ("What action verb completes the sentence? 'Doraemon ____ Nobita's life.'", "improves / transforms", "robotic", "lazy", "pocket", "A", "'improves' / 'transforms' is an action verb.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH06_CAT04_Q{idx:02d}"
        qtxt = f"Action Verb Grammar Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Action Verb Context & Tense", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence: 'The helpful robotic cat quickly fetched a gadget and saved his friend.' How many total ACTION VERBS are present?", "2 action verbs ('fetched', 'saved')", "1 action verb", "3 action verbs", "0 action verbs", "A", "'fetched' and 'saved' are action verbs; 'helpful', 'robotic', 'quickly' are adjectives/adverbs."),
        ("Categorize the verbs: In 'Doraemon **was** helpful, so he **gave** Nobita a gadget', classify 'was' and 'gave'.", "'was' is a linking verb; 'gave' is an action verb.", "Both are action verbs.", "Both are linking verbs.", "'was' is action; 'gave' is linking.", "A", "'was' links state of being; 'gave' shows physical action."),
        ("Replace the weak verb with a strong action verb: 'Doraemon **went fast** to help Nobita.'", "Doraemon **rushed** to help Nobita.", "Doraemon **was near** Nobita.", "Doraemon **walked slow**.", "Doraemon **looked at** Nobita.", "A", "'rushed' is a much stronger, vivid action verb."),
        ("Identify the sentence with THREE distinct action verbs:", "Doraemon **traveled** in time, **fetched** gadgets, and **helped** Nobita.", "Doraemon was blue, earless, and robotic.", "The gadgets were futuristic and funny.", "The show was created in 1969.", "A", "traveled, fetched, helped are 3 distinct action verbs."),
        ("Differentiate verb types: Which underlined word is an ACTION verb?", "Doraemon **rescued** Nobita from trouble.", "Doraemon was **friendly**.", "Nobita was **lazy**.", "The pocket was **magic**.", "A", "'rescued' is an action verb."),
        ("Spot the incorrect verb tense: 'Doraemon **fetch** a gadget yesterday.' Correct it:", "'fetch' should be 'fetched' (past action verb).", "'fetch' should be 'fetching'.", "'fetch' should be 'fetches'.", "'fetch' should be 'will fetch'.", "A", "Past time indicator 'yesterday' requires past tense action verb 'fetched'."),
        ("Form an action chain: Rearrange the story action verbs in correct order of occurrence: (traveled, arrived, fetched, saved)", "traveled -> arrived -> fetched -> saved", "saved -> fetched -> arrived -> traveled", "arrived -> traveled -> saved -> fetched", "fetched -> arrived -> traveled -> saved", "A", "First traveled in time, arrived in past, fetched gadget, saved Nobita."),
        ("Identify the verb error in dialogue: Nobita said, 'I have **learn** a valuable lesson!'", "'learn' is incorrect; the past participle form is 'learned' or 'learnt' ('have learned').", "'learn' should be 'learning'.", "'learn' should be 'learns'.", "No error.", "A", "Perfect tense requires past participle 'learned' / 'learnt'."),
        ("Analyze this sentence: 'Doraemon **encouraged** Nobita to work hard.' What type of action verb is 'encouraged'?", "Supportive speech/mental action verb", "Physical movement verb", "Linking verb", "State of being verb", "A", "'encouraged' is an action verb of speech/support."),
        ("Which sentence uses action verbs to show cause and effect?", "Doraemon **brought** gadgets, so Nobita **solved** his problems.", "Doraemon is blue and Nobita is lazy.", "The pocket is fourth-dimensional.", "Japan is an island nation.", "A", "'brought' (cause action) -> 'solved' (effect action)."),
        ("Spot the missing action verb: 'Doraemon ____ into his 4D pocket and ____ a propeller.'", "reached, pulled", "blue, fast", "was, was", "quick, slow", "A", "'reached' and 'pulled' complete sentence with vivid actions."),
        ("HOTS Reasoning: Why is 'improves' in 'He improves Nobita's life' considered a TRANSFORMATIVE action verb?", "Because it describes actively elevating the quality and outcome of someone's life.", "Because improving requires gadgets.", "Because Doraemon is robotic.", "Because it is a noun.", "A", "Descriptive action verb conveying positive transformation."),
        ("Transform the action verb to future tense: 'Doraemon **helps** Nobita tomorrow.'", "Doraemon **will help** Nobita tomorrow.", "Doraemon **helped** Nobita tomorrow.", "Doraemon **is helping** Nobita tomorrow.", "Doraemon **help** Nobita tomorrow.", "A", "'will help' expresses future action."),
        ("Identify the sentence where the action verb matches the plural subject:", "The gadgets **solve** Nobita's problems.", "The gadgets **solves** Nobita's problems.", "A gadget **solve** Nobita's problems.", "The gadgets **is solving** Nobita's problems.", "A", "Plural subject 'gadgets' takes base verb 'solve' in simple present.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH06_CAT04_Q{idx:02d}"
        qtxt = f"Higher Order Action Verb Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Action Verb Classification & Tense Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 5. Punctuation Marks (50 Qs)
# ---------------------------------------------------------------------------
def build_punctuation_marks():
    header = "# Category 5: Punctuation Marks & Capitalization — Chapter 06: My Favourite Cartoon\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_punct = [
        ("What punctuation mark should be placed at the end of: 'Doraemon is a robotic cat__'", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "Comma (,)", "A", "A statement ends with a full stop."),
        ("Which mark is used at the end of an asking sentence: 'What gadget did Doraemon use__'", "Question mark (?)", "Full stop (.)", "Comma (,)", "Exclamation mark (!)", "A", "A question ends with a question mark."),
        ("Which letter should ALWAYS be capitalized in a proper name like 'Nobita Nobi'?", "First letter of each name (e.g., Nobita Nobi)", "The last letter", "All letters", "No letters", "A", "Proper names require capitalized initial letters."),
        ("Identify the punctuation mark used to separate items in a list: 'The show teaches responsibility__ friendship__ and hard work.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Hyphen (-)", "A", "Commas separate items in a list."),
        ("Which punctuation mark shows sudden excitement: 'Look! It is a flying gadget__'", "Exclamation mark (!)", "Full stop (.)", "Comma (,)", "Question mark (?)", "A", "Exclamation marks express intense excitement."),
        ("Select the proper noun that MUST start with a capital letter:", "Doraemon", "cat", "pocket", "gadget", "A", "'Doraemon' as a proper name starts with capital 'D'."),
        ("Which of the following is the symbol for a **full stop**?", ".", "?", "!", ",", "A", "Period/full stop is '.'"),
        ("Which of the following is the symbol for a **question mark**?", "?", ".", "!", ",", "A", "Question mark is '?'"),
        ("Which of the following is the symbol for an **exclamation mark**?", "!", "?", ".", ",", "A", "Exclamation mark is '!'"),
        ("Which word in this sentence should start with a CAPITAL letter? 'fujiko F. Fujio created Doraemon.'", "fujiko -> Fujiko", "created -> Created", "robotic -> Robotic", "cat -> Cat", "A", "First name 'Fujiko' must start with a capital letter."),
        ("What punctuation mark goes in the box? 'Doraemon comes from the 22nd century [ ]'", "Full stop (.)", "Question mark (?)", "Comma (,)", "Exclamation mark (!)", "A", "Full stop ends the statement."),
        ("Which creator name is capitalized correctly?", "Fujiko F. Fujio", "fujiko f. fujio", "Fujiko f. Fujio", "FUJIKO F. FUJIO", "A", "Capital letters for proper artist name."),
        ("What mark goes after a speaker tag: 'Doraemon said__ \"I will help you, Nobita!\"'", "Comma (,)", "Question mark (?)", "Full stop (.)", "Exclamation mark (!)", "A", "Comma follows dialogue speaker tags."),
        ("Identify the correct capital letter for the pronoun 'I': 'nobita said, \"i will study hard.\"'", "I", "i", "i'm", "I'm", "A", "Standalone pronoun 'I' is always capitalized."),
        ("Which option shows a sentence ending correctly?", "The show is very popular in Japan.", "The show is very popular in Japan?", "The show is very popular in Japan,", "The show is very popular in Japan;", "A", "Full stop at end of simple statement."),
        ("What mark is used in possessives like 'the **cat's** pocket'?", "Apostrophe (')", "Comma (,)", "Full stop (.)", "Hyphen (-)", "A", "Apostrophe indicates possession."),
        ("Which book chapter title is capitalized correctly?", "My Favourite Cartoon", "my favourite cartoon", "My Favourite cartoon", "MY FAVOURITE CARTOON", "A", "Major words in titles are capitalized."),
        ("What punctuation mark is used around spoken dialogue: '___Here is a gadget for you!___'", "Quotation marks / Speech marks ( \" \" )", "Parentheses ( )", "Full stops ( . . )", "Commas ( , , )", "A", "Speech marks enclose spoken dialogue.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_punct, start=1):
        qid = f"BK02_CH06_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Punctuation & Capitalization Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Identify the sentence with CORRECT capitalization and punctuation:", "Doraemon helps Nobita Nobi in Japan on Monday.", "doraemon helps nobita nobi in japan on monday.", "Doraemon helps nobita nobi in Japan on monday?", "doraemon Helps Nobita Nobi In Japan On Monday.", "A", "Doraemon, Nobita Nobi (names), Japan (country), Monday (day) capitalized; period at end."),
        ("Which sentence is punctuated as a CORRECT question?", "Why did Doraemon travel back in time?", "Why did Doraemon travel back in time.", "Why did Doraemon travel back in time!", "Why did Doraemon travel back in time,", "A", "Question starting with 'Why' ends with question mark ?"),
        ("Spot the capitalization mistake in: 'doraemon lived with Nobita in a small Town.'", "'doraemon' should be capitalized ('Doraemon'); 'Town' should be lowercase.", "'Town' should be capitalized only.", "'nobita' should be lowercase.", "No mistake.", "A", "Name 'Doraemon' capitalized; common noun town lowercase here."),
        ("Choose the correctly punctuated dialogue sentence:", "\"Don't worry, Nobita,\" said Doraemon.", "don't worry Nobita said Doraemon.", "\"Don't worry, Nobita\" said Doraemon", "Don't worry, Nobita, said Doraemon.", "A", "Quotation marks around dialogue, comma inside quote, capital D."),
        ("Identify where a COMMA is missing: 'The show teaches responsibility friendship and hard work.'", "Between 'responsibility' and 'friendship' ('responsibility, friendship')", "After 'The'", "After 'work'", "No comma needed", "A", "Commas separate items in list: 'responsibility, friendship and hard work'."),
        ("Which sentence uses the apostrophe correctly for possession?", "This is Doraemon's magic pocket.", "This is Doraemons' magic pocket.", "This is Doraemons magic pocket.", "This is Doraemon's' magic pocket.", "A", "Doraemon's indicates possession by Doraemon."),
        ("Select the sentence with CORRECT punctuation for an exclamatory statement:", "What an amazing robotic cat Doraemon is!", "What an amazing robotic cat Doraemon is?", "What an amazing robotic cat Doraemon is.", "What an amazing robotic cat Doraemon is,", "A", "Exclamatory statement ends with exclamation mark !"),
        ("Which contraction is written correctly for 'does not'?", "doesn't", "does'nt", "doesnt'", "d'oesnt", "A", "doesn't is standard contraction."),
        ("Find the sentence with NO capitalization errors:", "Fujiko F. Fujio created Doraemon in 1969 in Japan.", "fujiko f. fujio created doraemon in 1969 in japan.", "Fujiko F. Fujio Created Doraemon In 1969 In Japan.", "fujiko F. Fujio created Doraemon in 1969 in Japan.", "A", "'Fujiko F. Fujio', 'Doraemon', and 'Japan' capitalized as proper names."),
        ("What punctuation mark belongs in the blank? 'Nobita shouted, \"Hooray__ Doraemon brought a new gadget!\"'", "!", ".", "?", ",", "A", "Exclamation mark ! expresses excitement."),
        ("Choose the correct form for 'is not'?", "isn't", "is'nt", "isnt'", "i'snt", "A", "isn't is standard contraction."),
        ("Identify the punctuation error: 'Doraemon opened his pocket, he pulled out a propellor.'", "Comma splice between two independent clauses (should be full stop or 'and').", "Missing question mark.", "Missing capital letters.", "No error.", "A", "Two complete sentences separated only by comma."),
        ("Select the sentence with proper use of capital letters for names and places:", "Doraemon lives with Nobita Nobi in Japan.", "doraemon lives with nobita nobi in japan.", "Doraemon lives with Nobita nobi in Japan.", "doraemon Lives with Nobita Nobi in japan.", "A", "Names 'Doraemon', 'Nobita Nobi', 'Japan' all capitalized."),
        ("Which sentence correctly uses an apostrophe for possessive noun?", "Nobita's test marks were low.", "Nobitas' test marks were low.", "Nobitas test marks were low.", "Nobita's' test marks were low.", "A", "Nobita's indicates singular possession."),
        ("Identify the correct punctuation for a list of items: 'The pocket contains ____'", "gadgets, tools, and toys.", "gadgets tools and toys.", "gadgets; tools; and toys.", "gadgets: tools: and toys.", "A", "Commas separate items in list."),
        ("Choose the sentence that correctly asks a question about the story:", "Why does Doraemon help Nobita?", "Why does Doraemon help Nobita.", "Why does Doraemon help Nobita!", "why does Doraemon help Nobita.", "A", "Capital W, ends with question mark ?"),
        ("Fix the sentence: 'where is doraemons pouch'", "Where is Doraemon's pouch?", "Where is doraemons pouch.", "where is Doraemon's pouch!", "Where is Doraemons' pouch?", "A", "Capital W, possessive Doraemon's, ends with ?"),
        ("Which of these sentences is punctuated PERFECTLY?", "Doraemon said, \"I will help you solve this!\"", "Doraemon said \"i will help you solve this!\"", "doraemon said, \"I will help you solve this!\"", "Doraemon said, \"I will help you solve this.\"", "A", "Capital D, comma after said, speech marks around dialogue with ! inside.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH06_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Context Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Punctuation Application & Dialogue Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze and count ALL capitalization and punctuation errors in: 'on monday doraemon said to nobita nobi, lets use a gadget'", "5 errors (on->On, monday->Monday, doraemon->Doraemon, nobita nobi->Nobita Nobi, lets->let's, capital L in Let's, period)", "2 errors", "3 errors", "7 errors", "A", "Starts sentence, day name, person names, contraction let's, capital L, period."),
        ("Correct the entire dialogue paragraph: 'nobita asked can you help me with this problem doraemon replied yes i have the right tool'", "\"Can you help me with this problem?\" asked Nobita. Doraemon replied, \"Yes, I have the right tool.\"", "nobita asked \"can you help me with this problem\" doraemon replied \"yes i have the right tool.\"", "Nobita asked, Can you help me with this problem. Doraemon replied, Yes I have the right tool.", "\"Can you help me with this problem?\" Asked Nobita. Doraemon replied \"Yes I have the right tool?\"", "A", "Full proper quotation, dialogue tags, capitalization, and terminal punctuation."),
        ("Distinguish between singular possessive and contraction: 'Doraemon**'**s pocket is 4D, and he**'**s helpful.'", "First 's is possessive (pocket belonging to Doraemon); second 's is contraction (he is).", "Both are possessive.", "Both are contractions.", "First is contraction; second is possessive.", "A", "Doraemon's pocket = pocket of Doraemon; he's = he is."),
        ("Spot the subtle punctuation flaw in this dialogue: '\"Here is a gadget,\" Said Doraemon.'", "'Said' should be lowercase 'said' because it continues the dialogue tag outside quotation marks.", "'Here' should be lowercase.", "Commas should be outside quotes.", "No flaw.", "A", "Dialogue tags following quotes start with lowercase unless proper nouns."),
        ("Which sentence correctly uses punctuation to show contrast?", "Nobita is lazy, but Doraemon is helpful.", "Nobita is lazy but, Doraemon is helpful.", "Nobita is lazy but Doraemon is helpful!", "Nobita is lazy; but Doraemon is helpful?", "A", "Comma before coordinating conjunction 'but' joining two independent clauses."),
        ("Reconstruct with perfect punctuation: 'doraemon arrived in japan on monday 15th december 1969'", "Doraemon arrived in Japan on Monday, 15th December 1969.", "doraemon arrived in japan on monday, 15th december 1969.", "Doraemon arrived in Japan on Monday 15th December 1969", "Doraemon arrived in japan on monday 15th december 1969.", "A", "Doraemon, Japan, Monday, 15th December 1969, period."),
        ("Identify why exclamation mark is necessary here: '\"Wow! Look at this futuristic gadget!\"'", "Because Nobita is expressing intense awe and excitement.", "Because Doraemon is blue.", "Because pocket is small.", "Because sentence is long.", "A", "Exclamation mark communicates intense excitement."),
        ("Choose the correctly punctuated sentence containing an appositive phrase:", "Doraemon, a robotic cat from the future, helps Nobita.", "Doraemon a robotic cat from the future helps Nobita.", "Doraemon, a robotic cat from the future helps Nobita.", "Doraemon a robotic cat from the future, helps Nobita.", "A", "Appositive phrase 'a robotic cat from the future' is set off by commas."),
        ("Analyze the use of hyphen in: 'The earless robotic-cat has a fourth-dimensional pocket.'", "Hyphen joins compound adjective (fourth-dimensional).", "Hyphen replaces comma.", "Hyphen indicates question.", "Hyphen is an apostrophe.", "A", "Compound adjectives modifying nouns take hyphens."),
        ("Identify the correct sentence with direct speech quote within text:", "Doraemon stated, \"I am here to help you,\" and Nobita smiled.", "Doraemon stated \"I am here to help you\" and Nobita smiled.", "Doraemon stated, 'I am here to help you,' and Nobita smiled.", "Doraemon stated: \"I am here to help you\" and Nobita smiled.", "A", "Comma before quote, double quotation marks around direct speech, comma inside quote."),
        ("Spot the missing apostrophe: 'Nobitas homework was finished with Doraemons help.'", "Missing apostrophes in both 'Nobita's' and 'Doraemon's' -> 'Nobita's homework was finished with Doraemon's help.'", "Missing apostrophe in 'homework''", "Missing apostrophe in 'was''", "No apostrophe needed", "A", "Both 'Nobita's' and 'Doraemon's' require possessive apostrophes."),
        ("HOTS Reasoning: Why does putting a comma in different places change meaning? Compare: 'Nobita, said Doraemon, is lazy.' vs 'Nobita said, \"Doraemon is lazy.\"'", "In the first, Doraemon says Nobita is lazy; in the second, Nobita says Doraemon is lazy.", "Both mean the exact same thing.", "The first is a question.", "Commas do not affect meaning.", "A", "Punctuation alters who speaks and who is described."),
        ("Correct all 4 errors in: 'whats the robotic cats name asked nobita'", "\"What's the robotic cat's name?\" asked Nobita.", "whats the robotic cats name? asked nobita.", "\"What's the robotic cats name.\" asked Nobita.", "\"whats the robotic cats name?\" Asked Nobita.", "A", "Quotation marks, capital W, possessive cat's, question mark, capital N."),
        ("Identify the rule for capitalizing artist and character names like 'Fujiko F. Fujio' and 'Doraemon':", "Proper names of real people and fictional characters take initial capital letters.", "Character names are never capitalized.", "Character names are capitalized only at end of sentence.", "Names must be written in ALL CAPS.", "A", "Proper names take initial capitals.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH06_CAT05_Q{idx:02d}"
        qtxt = f"Higher Order Punctuation Analysis & Dialogue Formatting:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Punctuation & Dialogue Editing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 6. Phonics & Vowel Digraphs (50 Qs)
# ---------------------------------------------------------------------------
def build_phonics_digraphs():
    header = "# Category 6: Phonics & Vowel Digraphs — Chapter 06: My Favourite Cartoon\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_phonics = [
        ("Which vowel digraph is present in the word **'blue'** (sound /oo/)?", "ue", "ee", "ai", "ou", "A", "'ue' forms the vowel sound in blue."),
        ("Identify the vowel digraph in the word **'free'**:", "ee", "ea", "oa", "ui", "A", "'ee' forms the long /e/ vowel sound in free."),
        ("Which word from the story contains the **'ou'** vowel digraph?", "trouble", "cat", "time", "boy", "A", "'trouble' contains the 'ou' digraph."),
        ("Identify the vowel digraph in the word **'reach'**:", "ea", "ee", "ow", "oo", "A", "'ea' forms long /e/ sound in reach."),
        ("Which vowel digraph appears in the word **'paid'**?", "ai", "ay", "ea", "oa", "A", "'ai' makes long /a/ sound in paid."),
        ("Find the word with the **'oo'** vowel digraph: 'Doraemon has a cool gadget.'", "cool", "Doraemon", "has", "gadget", "A", "'cool' contains 'oo' digraph."),
        ("Which word from the story rhymes with **'cat'**?", "hat", "cot", "cut", "cheat", "A", "'hat' rhymes with 'cat'."),
        ("Which word from the story rhymes with **'boy'**?", "toy", "bay", "buy", "bow", "A", "'toy' rhymes with 'boy'."),
        ("Identify the vowel digraph in the word **'boasted'**:", "oa", "ou", "ow", "oo", "A", "'oa' makes long /o/ sound in boasted."),
        ("Which word from the story rhymes with **'time'**?", "lime", "tame", "team", "tomb", "A", "'lime' rhymes with 'time'."),
        ("Identify the vowel digraph in **'voice'**:", "oi", "ea", "ee", "ia", "A", "'oi' is the vowel digraph in voice."),
        ("Which word from Chapter 06 has the **'ea'** digraph making a long /e/ sound?", "teaches", "head", "heavy", "dead", "A", "'teaches' has 'ea' making long /e/ sound."),
        ("Which word rhymes with **'day'**?", "away", "die", "due", "door", "A", "'away' rhymes with 'day'."),
        ("Identify the silent letter in **'know'** (as in 'Doraemon knows everything'):", "k", "n", "o", "w", "A", "Initial 'k' before 'n' is silent."),
        ("Which word from the story has long /i/ sound spelled with **'igh'**?", "bright", "bought", "blue", "boy", "A", "'igh' in bright makes long /i/ sound."),
        ("Find the word with **'ou'** digraph: 'They found a 4D pocket.'", "found", "pocket", "they", "4D", "A", "'found' contains 'ou' digraph."),
        ("Which word rhymes with **'show'**?", "know", "shoe", "shut", "shop", "A", "'know' rhymes with 'show'."),
        ("Identify the silent letter in the word **'wrist'** (as in 'wrist watch'):", "w", "r", "i", "s", "A", "Initial 'w' before 'r' is silent.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_phonics, start=1):
        qid = f"BK02_CH06_CAT06_Q{idx:02d}"
        qtxt = f"Phonics & Vowel Digraph Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Vowel Digraphs & Rhyming Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Compare the **'ea'** digraph sound in **'teaches'** and **'bread'**. What is the difference?", "'teaches' has long /e/ sound; 'bread' has short /e/ sound.", "Both have short /e/ sound.", "Both have long /a/ sound.", "'teaches' has short /e/; 'bread' has long /e/.", "A", "'ea' can make long /e/ (teaches) or short /e/ (bread)."),
        ("Select the word pair from Chapter 06 that has the SAME vowel digraph sound:", "cool - tool", "fries - bread", "teaches - roar", "cat - sweet", "A", "'cool' and 'tool' both have 'oo' long /oo/ sound."),
        ("Which word contains a SILENT letter? (know, cat, boy, blue)", "know", "cat", "boy", "blue", "A", "'know' has silent initial 'k'."),
        ("Identify the odd one out based on vowel sound: (teach, reach, beach, bread)", "bread", "teach", "reach", "beach", "A", "'bread' has short /e/ sound; others have long /e/ sound."),
        ("Which digraph completes the word for time travel tool? 'gadg__t'", "e", "ea", "ee", "ou", "A", "'gadget' uses vowel 'e'."),
        ("Group these story words by digraph: **found**, **out**, **shouted**. What digraph do they all share?", "ou", "ow", "oo", "oi", "A", "All share 'ou' making /ow/ diphthong sound."),
        ("Find the word with consonant digraph **'th'** from the story: 'Doraemon is from **the** 22nd century.'", "the", "century", "from", "robotic", "A", "'the' contains voiced 'th' consonant digraph."),
        ("Which of these words has the **'ow'** vowel digraph making long /o/ sound? (show, grow, blow, all of these)", "all of these", "show", "grow", "blow", "A", "show, grow, blow all share 'ow' long /o/ sound."),
        ("Identify the vowel digraph in **'favourite'**:", "ou", "ae", "ur", "or", "A", "'ou' is the digraph in favourite."),
        ("Which word from the story has a silent **'k'**? (know, knee, knife, all of these)", "all of these", "know", "knee", "knife", "A", "know, knee, knife all have silent initial 'k'."),
        ("Select the word that rhymes with **'cat'** and fits sentence: 'Doraemon is a robotic ____.'", "cat", "bat", "rat", "hat", "A", "'cat' fits the sentence."),
        ("Identify the digraph in **'charming'**:", "ch", "ar", "ing", "ch and ar", "D", "'ch' consonant digraph and 'ar' vowel blend."),
        ("Which word has the short /u/ sound made by **'ou'**? (trouble, house, out, shout)", "trouble", "house", "out", "shout", "A", "'trouble' has short /u/ sound with 'ou'."),
        ("Find the R-controlled vowel sound in: 'Doraemon is a **star** of animation.'", "ar sound", "ea", "ou", "ai", "A", "R-controlled vowel in star."),
        ("Which word contains the **'oi'** diphthong/digraph? (choice, voice, point, all of these)", "all of these", "choice", "voice", "point", "A", "choice, voice, point all contain 'oi'."),
        ("Identify the soft **'c'** sound in Chapter 06 vocabulary: (century, cat, pocket, cool)", "century", "cat", "pocket", "cool", "A", "'century' has soft /s/ sound for 'c' before 'e'; others have hard /k/ sound."),
        ("Which word has a soft **'g'** sound? (gadget, magic, danger, all of these)", "all of these", "gadget", "magic", "danger", "A", "gadget (second g), magic, danger all have soft /j/ sound for 'g'."),
        ("Choose the correct spelling with **'ea'** digraph for instructing:", "teaches", "teachies", "teachees", "techs", "A", "teaches is standard spelling.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH06_CAT06_Q{idx:02d}"
        qtxt = f"Phonics Analysis & Sound Pattern Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Phonic Rules & Sound Discrimination", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the phonics rule: Why does 'c' in **'century'** sound like /s/, but 'c' in **'cat'** sounds like /k/?", "Because 'c' followed by 'e', 'i', or 'y' makes soft /s/ sound; before 'a', 'o', 'u' it makes hard /k/ sound.", "Because century is long.", "Because cat is blue.", "There is no rule.", "A", "Soft 'c' rule: c + i, e, y = /s/ sound."),
        ("Categorize the 'ea' digraphs into long /e/ vs short /e/: (teaches, reach, bread, heavy, lead [metal])", "Long /e/: teaches, reach; Short /e/: bread, heavy, lead [metal]", "All are long /e/.", "All are short /e/.", "Long /e/: bread; Short /e/: teaches", "A", "teaches, reach make long /e/; bread, heavy, lead (metal) make short /e/."),
        ("Identify the word pair where SILENT letters exist in BOTH words:", "know - wrist", "cat - boy", "blue - pocket", "gadget - show", "A", "'know' (silent k) and 'wrist' (silent w)."),
        ("Decode the phonics blend: Which word contains a 3-letter consonant blend at the start?", "screamed / scrolled", "cat", "friend", "blue", "A", "'scr' blend type."),
        ("Examine the hard vs soft 'g' rule: Why is 'g' soft in **'magic'** but hard in **'gadget' (first g)**?", "'g' followed by 'e', 'i', or 'y' makes soft /j/ sound (magic); 'g' before 'a', 'o', 'u' makes hard /g/ sound (gadget).", "Because magic is trick.", "Because gadget is tool.", "There is no rule.", "A", "Soft 'g' rule: g + e, i, y = /j/ sound."),
        ("Find the word with BOTH a vowel digraph AND a silent letter:", "teaches", "cat", "boy", "show", "A", "'teaches' has 'ea' digraph."),
        ("Differentiate diphthongs: Which pair produces the /ow/ sound as in **'out'**?", "out - found", "voice - coin", "paid - day", "boat - coat", "A", "'out' and 'found' share /ow/ diphthong sound."),
        ("Analyze homophones: 'Doraemon was sent to the **past** / **passed**.' Which word means former time?", "past", "passed", "parst", "passte", "A", "'past' (former time) and 'passed' (moved by) are homophones/near-homophones."),
        ("Identify the phonic pattern in **'futuristic'**: What vowel sound does the first 'u' make?", "Long /yoo/ sound", "Short /u/ sound", "Silent sound", "Short /o/ sound", "A", "'fu-tur-is-tic' first 'u' makes long /yoo/ sound."),
        ("Sort by ending sound: Which word ends with the /z/ sound? (gadgets, lessons, pockets, cats)", "lessons", "gadgets", "pockets", "cats", "A", "Plurals ending in voiced sounds take /z/ ending sound (lessons)."),
        ("Spot the word where 'k' is SILENT: (know, knee, knife, all of these)", "all of these", "know", "knee", "knife", "A", "'k' is silent before 'n' in know, knee, knife."),
        ("HOTS Reasoning: Why do 'blue' and 'blew' sound identical but have different spellings and meanings?", "They are homophones (same sound, different spelling/meaning).", "They are synonyms.", "They are antonyms.", "They are plurals.", "A", "Homophones share pronunciation but differ in spelling/meaning."),
        ("Identify the compound word from story concepts containing two simple words:", "homework / schoolboy", "Doraemon", "Fujiko", "animation", "A", "homework = home + work; schoolboy = school + boy."),
        ("Determine the syllable count and stress: How many syllables are in **'responsibility'**?", "6 syllables (re-spon-si-bil-i-ty)", "4 syllables", "5 syllables", "3 syllables", "A", "re-spon-si-bil-i-ty has 6 syllables.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH06_CAT06_Q{idx:02d}"
        qtxt = f"Higher Order Phonics & Orthographic Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Phonetic Rules & Homophone Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 7. Question Words & Interrogatives (50 Qs)
# ---------------------------------------------------------------------------
def build_question_words():
    header = "# Category 7: Question Words & Interrogatives — Chapter 06: My Favourite Cartoon\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_qwords = [
        ("___ created Doraemon?", "Who", "What", "Where", "Why", "A", "'Who' asks about a person (Fujiko F. Fujio)."),
        ("___ is Doraemon?", "What", "Who", "Where", "When", "A", "'What' asks about identity/description (a blue robotic cat)."),
        ("___ was Doraemon sent from?", "Where / From what century", "Who", "Why", "When", "A", "'Where' / 'From what century' asks about origin (22nd century)."),
        ("___ was Doraemon sent back in time to help?", "Whom / Who", "What", "Where", "Why", "A", "'Whom' asks about target person (Nobita Nobi)."),
        ("___ does Doraemon fetch his futuristic gadgets from?", "Where", "Who", "Why", "When", "A", "'Where' asks about location (his 4D pocket)."),
        ("___ year was Doraemon first introduced?", "Which / In what year", "Who", "Where", "Why", "A", "'Which' asks about specific year (1969)."),
        ("___ did Doraemon come to live with Nobita?", "Why", "Who", "Where", "What", "A", "'Why' asks for reason (to help him improve his life)."),
        ("___ does Doraemon react when Nobita gets into trouble?", "How", "Who", "Where", "What", "A", "'How' asks about method/reaction (uses futuristic gadgets)."),
        ("___ color is Doraemon?", "What", "Who", "Where", "Why", "A", "'What' asks about color (blue)."),
        ("___ pocket does Doraemon have on his belly?", "What kind of", "Who", "Where", "Why", "A", "'What kind of' asks about type (fourth-dimensional pocket)."),
        ("___ lessons does the series teach children?", "What", "Who", "Where", "Why", "A", "'What' asks about lessons (responsibility, friendship, hard work)."),
        ("___ character is lazy but good-hearted?", "Which", "Who", "Why", "When", "A", "'Which' asks about character (Nobita Nobi)."),
        ("___ country does the Doraemon series originate from?", "Which", "Who", "Why", "When", "A", "'Which' asks about country (Japan)."),
        ("___ moral lesson is emphasized in the show?", "What", "Who", "Where", "Why", "A", "'What' asks about lesson."),
        ("___ gadgets does Doraemon have in his pocket?", "How many", "Who", "Where", "Why", "A", "'How many' asks about quantity (countless)."),
        ("___ creator wrote the Doraemon manga?", "Who", "What", "Where", "Why", "A", "'Who' asks about author (Fujiko F. Fujio)."),
        ("___ does Nobita need Doraemon's help?", "Why", "Who", "Where", "What", "A", "'Why' asks for reason (he is lazy and gets into trouble)."),
        ("___ did Doraemon first appear on television?", "When", "Who", "Where", "Why", "A", "'When' asks about time (1969).")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_qwords, start=1):
        qid = f"BK02_CH06_CAT07_Q{idx:02d}"
        qtxt = f"Choose the correct **question word** (Who, What, Where, Why, How, When):\n\n\"{q_blank} _____?\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Question Word Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Match question to answer: Question: '___ was Doraemon sent to the past?' Answer: 'Because Nobita needed help to improve his life.'", "Why", "What", "Where", "Who", "A", "'Why' asks for reasons ('Because...')."),
        ("Match question to answer: Question: '___ is Doraemon from?' Answer: 'The 22nd century in Japan.'", "Where", "Who", "Why", "When", "A", "'Where' asks for location/origin."),
        ("Choose the correct question word for TIME: '___ was Doraemon first created?'", "When", "Where", "Who", "Why", "A", "'When' inquires about time (in 1969)."),
        ("Form an asking sentence: 'Doraemon fetches gadgets.' -> '____ does Doraemon fetch?'", "What", "Who", "Why", "Where", "A", "'What' inquires about object."),
        ("Identify the INCORRECT question word usage: '**Why** is Nobita's best friend?'", "'Why' should be 'Who'", "'Why' should be 'Where'", "'Why' should be 'When'", "No error", "A", "'Who is Nobita's best friend?' asks for identity."),
        ("Select the proper interrogative sentence:", "Why did Doraemon travel back in time?", "Why Doraemon traveled back in time?", "Why did Doraemon traveled back in time?", "Why Doraemon travel back time?", "A", "Interrogative word + auxiliary 'did' + base verb 'travel'."),
        ("Which question word asks about MANNER or METHOD? '___ does Doraemon solve Nobita's problems?'", "How", "Who", "What", "Where", "A", "'How' inquires about method/manner (by using gadgets)."),
        ("Complete the question: '___ of the two characters is from the future?'", "Which", "What", "Where", "Why", "A", "'Which' chooses between specific options."),
        ("Change statement to question: 'Doraemon helps Nobita.' -> '____ helps Nobita?'", "Who", "What", "Where", "Why", "A", "'Who' asks for subject (Doraemon)."),
        ("Fill in the blank: '___ famous is the Doraemon series?'", "How", "What", "Where", "Why", "A", "'How famous' measures degree."),
        ("Identify the question word in: 'Whom did Fujiko F. Fujio create in 1969?'", "Whom", "did", "Fujiko", "create", "A", "'Whom' is the interrogative pronoun asking about object character."),
        ("Choose the question that matches this answer: 'He was sent back because Nobita's future was full of hardship.'", "Why was Doraemon sent back in time?", "Where did he go?", "Who sent him?", "What did he bring?", "A", "'Why...' matches answer starting with 'because...'."),
        ("Fill in the blank: '___ gadget helped Nobita fly?'", "Which", "Who", "Why", "Where", "A", "'Which gadget' asks for identification (bamboo copter)."),
        ("Complete: '___ gadgets does Doraemon carry?'", "How many", "How much", "Who", "Where", "A", "'How many' asks about countable quantity (gadgets)."),
        ("Select the correct question for: 'Doraemon fetches gadgets from his 4D pocket.'", "What does Doraemon do?", "Where was Doraemon?", "Why is Doraemon blue?", "Who was Nobita?", "A", "'What does Doraemon do?' asks for action."),
        ("Which question word inquires about POSSESSION? '___ pocket contains futuristic tools?'", "Whose", "Who", "Where", "Why", "A", "'Whose' asks about ownership."),
        ("Form question: 'Nobita has many troubles.' -> '____ troubles does Nobita have?'", "How many", "How much", "Why", "Where", "A", "'How many' asks for countable number."),
        ("Identify the question mark error: 'Why did Doraemon help Nobita.' Correct it:", "Why did Doraemon help Nobita?", "Why did Doraemon help Nobita!", "Why did Doraemon help Nobita,", "Why did Doraemon help Nobita;", "A", "Questions must end with question mark ?")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH06_CAT07_Q{idx:02d}"
        qtxt = f"Question Formation & Context Alignment:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Interrogative Sentence Formation", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence structure: 'Why did Doraemon come from the 22nd century?' What is the syntax pattern?", "Question Word + Helping Verb (did) + Subject (Doraemon) + Main Verb (come) + Prepositional Phrase", "Question Word + Main Verb + Subject", "Subject + Question Word + Verb", "Helping Verb + Question Word + Subject", "A", "Standard English question syntax."),
        ("Differentiate between 'How many' vs 'How much': '___ gadgets' vs '___ trouble'", "'How many' for countable gadgets; 'How much' for uncountable trouble.", "Both use 'How many'.", "Both use 'How much'.", "'How much' for gadgets; 'How many' for trouble.", "A", "Countable nouns take 'How many'; uncountable nouns take 'How much'."),
        ("Spot the syntax error in question: 'Where Doraemon came from?' Correct it:", "Where **did** Doraemon come from?", "Where Doraemon come from?", "Where came Doraemon from?", "Where does Doraemon came from?", "A", "Past simple questions require auxiliary 'did' before subject and base verb 'come'."),
        ("Framing multi-question interview: What sequence of question words logically reveals the story plot?", "Who -> Where is he from -> Why was he sent -> What lessons does he teach", "How -> Who -> Why -> What", "Where -> Where -> Where -> Where", "Why -> Why -> Why -> Why", "A", "Reveals character, origin, purpose, and educational value."),
        ("Transform the statement into a formal question: 'True friendship involves guiding someone to work hard.'", "How does Doraemon's friendship teach Nobita the value of hard work?", "Where is Japan?", "Who is Doraemon?", "What is a cat?", "A", "Directly targets the moral lesson."),
        ("Analyze this ambiguous question: 'What did Doraemon do?' How can it be made precise?", "Add specific context: 'What gadget did Doraemon pull out of his pocket to solve Nobita's homework problem?'", "Make it shorter: 'What cat?'", "Change to: 'Where cat?'", "Remove 'What'.", "A", "Adding specific context clarifies which action."),
        ("Choose the correct question pair for dialogue: Nobita: '___ can I finish this homework?' Doraemon: '___ don't you try doing it yourself first?'", "How, Why", "Who, Where", "Where, How", "When, Whose", "A", "How (method of finishing), Why don't you (suggestion)."),
        ("Spot the DOUBLE auxiliary error: 'Why did Doraemon brought the gadget?'", "'did' requires base verb 'bring', not past tense 'brought'.", "'did' should be 'was'.", "'Why' should be 'How'.", "No error.", "A", "Auxiliary 'did' must be followed by base form of verb ('bring')."),
        ("Reconstruct question from answer: Answer: 'Doraemon has a fourth-dimensional pocket on his belly.'", "Question: 'Where does Doraemon store his futuristic gadgets?'", "Question: 'Where did Doraemon fly?'", "Question: 'Who is Nobita?'", "Question: 'Why is Doraemon blue?'", "A", "Targets storage location of gadgets."),
        ("Form indirect question: 'Nobita asked where Doraemon got the new gadget.' What is the sentence type?", "Assertive statement containing an embedded indirect question.", "Direct question requiring question mark.", "Exclamatory sentence.", "Command.", "A", "Indirect questions are statements ending with full stop."),
        ("Identify the correct question word for moral reasoning: '___ should we rely on hard work rather than magical shortcuts?'", "Why", "What", "Who", "Where", "A", "'Why' inquires into the moral reason for personal effort."),
        ("HOTS Reasoning: Why is 'Who' used for people/characters but 'Which' used when selecting from a specific group of cartoons?", "'Who' is general; 'Which' is used when choosing from a defined limited set.", "'Who' is for inanimate objects.", "'Which' is only for numbers.", "Both are identical.", "A", "'Which of the cartoons...' selects from a defined group."),
        ("Correct all errors in: 'who created doraemon in 1969'", "Who created Doraemon in 1969?", "Who created Doraemon in 1969.", "Whom created Doraemon?", "Who does created Doraemon in 1969?", "A", "Capital W, capital D, question mark at end."),
        ("Select the question that evaluates Higher Order Thinking (HOTS) about Chapter 06:", "How does Doraemon's insistence on Nobita making an effort teach that tools cannot replace personal responsibility?", "What color is Doraemon?", "Where is Japan?", "Does Doraemon have ears?", "A", "Asks student to evaluate moral theme and cause-and-effect.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH06_CAT07_Q{idx:02d}"
        qtxt = f"Higher Order Interrogative Analysis & Syntax:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Question Syntax & Analytical Framing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 8. Present Continuous Tense (-ing) (50 Qs)
# ---------------------------------------------------------------------------
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense (-ing) — Chapter 06: My Favourite Cartoon\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_ing = [
        ("Doraemon is **helping** Nobita with his homework.", "helping", "Doraemon", "is", "homework", "A", "'helping' is verb + -ing form."),
        ("Doraemon is **fetching** a gadget from his pocket.", "fetching", "Doraemon", "is", "pocket", "A", "'fetching' is verb + -ing form."),
        ("Nobita is **crying** about his bad test score.", "crying", "Nobita", "is", "score", "A", "'crying' is verb + -ing form."),
        ("The gadgets are **solving** Nobita's daily problems.", "solving", "gadgets", "are", "problems", "A", "'solving' is verb + -ing form."),
        ("Children are **watching** Doraemon on television.", "watching", "children", "are", "television", "A", "'watching' is verb + -ing form."),
        ("Doraemon is **flying** with the bamboo copter.", "flying", "Doraemon", "is", "copter", "A", "'flying' is verb + -ing form."),
        ("The cartoon is **teaching** valuable life lessons.", "teaching", "cartoon", "is", "lessons", "A", "'teaching' is verb + -ing form."),
        ("Nobita is **learning** to be responsible.", "learning", "Nobita", "is", "responsible", "A", "'learning' is verb + -ing form."),
        ("Doraemon is **traveling** through time.", "traveling", "Doraemon", "is", "time", "A", "'traveling' is verb + -ing form."),
        ("The friends are **playing** together happily.", "playing", "friends", "are", "happily", "A", "'playing' is verb + -ing form."),
        ("Doraemon is **warning** Nobita not to be lazy.", "warning", "Doraemon", "is", "lazy", "A", "'warning' is verb + -ing form."),
        ("Nobita is **trying** his best to improve.", "trying", "Nobita", "is", "best", "A", "'trying' is verb + -ing form."),
        ("Doraemon is **smiling** warmly at Nobita.", "smiling", "Doraemon", "is", "Nobita", "A", "'smiling' is verb + -ing form."),
        ("The show is **entertaining** millions of viewers.", "entertaining", "show", "is", "viewers", "A", "'entertaining' is verb + -ing form."),
        ("Nobita is **running** away from bullies.", "running", "Nobita", "is", "bullies", "A", "'running' is verb + -ing form."),
        ("Doraemon is **searching** his 4D pocket.", "searching", "Doraemon", "is", "pocket", "A", "'searching' is verb + -ing form."),
        ("The children are **laughing** at the funny scene.", "laughing", "children", "are", "scene", "A", "'laughing' is verb + -ing form."),
        ("Doraemon is **protecting** Nobita from harm.", "protecting", "Doraemon", "is", "harm", "A", "'protecting' is verb + -ing form.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_ing, start=1):
        qid = f"BK02_CH06_CAT08_Q{idx:02d}"
        qtxt = f"Identify the **present continuous (-ing) verb** in this sentence:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the present continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Present Continuous Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("What is the correct -ing spelling rule for **'help'**? (Doraemon is ____ Nobita.)", "helping (add -ing)", "helpping", "helpeing", "helpng", "A", "Regular verb adding -ing (helping)."),
        ("What is the correct -ing spelling rule for **'smile'**? (Doraemon is ____.)", "smiling (drop final silent e)", "smileing", "smilling", "smilng", "A", "Drop final silent 'e' before adding -ing (smiling)."),
        ("What is the correct -ing spelling rule for **'run'**? (Nobita is ____ home.)", "running (double final consonant)", "runing", "runnning", "runeing", "A", "CVC rule: double final consonant before -ing (running)."),
        ("Fill in the blank with present continuous form: 'Doraemon (fetch) ____ a gadget from his pocket.'", "is fetching", "was fetch", "are fetch", "is fetched", "A", "Singular subject takes 'is fetching'."),
        ("Choose the sentence in PRESENT CONTINUOUS tense:", "Doraemon is helping Nobita today.", "Doraemon helped Nobita yesterday.", "Doraemon will help Nobita tomorrow.", "Doraemon helped last week.", "A", "'is helping' is present continuous."),
        ("Fill in the blanks: 'The friends ____ (play) in the park, and Doraemon ____ (watch) them.'", "are playing, is watching", "is playing, are watching", "are play, is watch", "was playing, were watching", "A", "Plural 'friends' takes 'are playing'; singular 'Doraemon' takes 'is watching'."),
        ("Identify the spelling mistake in: 'Doraemon is **giveing** Nobita a tool.'", "'giveing' should be 'giving'", "'giveing' should be 'giving'", "'is' should be 'are'", "No mistake", "A", "Give drops silent e before -ing (giving)."),
        ("Select the correct -ing form for **'create'**:", "creating", "createing", "creatting", "creatng", "A", "Drop silent 'e': create -> creating."),
        ("Which sentence describes an action HAPPENING RIGHT NOW?", "Doraemon is unzipping his magic pocket.", "Doraemon unzipped his pocket yesterday.", "Doraemon unzips his pocket every day.", "Doraemon will unzip his pocket tomorrow.", "A", "Present continuous ('is unzipping') describes ongoing action right now."),
        ("Fill in the blank: 'I ____ (watch) my favourite cartoon Doraemon.'", "am watching", "is watching", "are watching", "am watcheing", "A", "Subject 'I' takes 'am watching'."),
        ("Choose the correct form: 'The children ____ (learn) valuable life lessons.'", "are learning", "is learning", "am learning", "are learn", "A", "Plural subject 'children' takes 'are learning'."),
        ("Identify the verb in: 'Why are you crying, Nobita?'", "are crying", "Why", "you", "Nobita", "A", "Helping verb 'are' + main verb 'crying' form present continuous."),
        ("What is the -ing form of **'fly'**?", "flying", "flyying", "flieing", "flyng", "A", "Vowel + y verb adding -ing (flying)."),
        ("What is the -ing form of **'solve'**?", "solving", "solveing", "solvving", "solvng", "A", "Drop silent e: solve -> solving."),
        ("Change simple present to continuous: 'Doraemon helps Nobita.' -> 'Doraemon ____ Nobita.'", "is helping", "helped", "was helping", "will help", "A", "is helping."),
        ("Fill in the blank: 'The popularity of the show ____ (increasing) globally.'", "is increasing", "are increasing", "am increasing", "increased", "A", "is increasing."),
        ("Identify the correct present continuous sentence:", "Look! Doraemon is pulling out a new gadget.", "Look! Doraemon pull out a new gadget.", "Look! Doraemon pulled out a new gadget.", "Look! Doraemon pulling out a new gadget.", "A", "Exclamation 'Look!' introduces action happening now ('is pulling')."),
        ("Select the correct -ing form for **'save'**:", "saving", "saveing", "savving", "savng", "A", "Drop silent e: save -> saving.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH06_CAT08_Q{idx:02d}"
        qtxt = f"Present Continuous Grammar & Spelling Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Present Continuous Formation & Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze spelling rules for adding -ing to verbs: Group them correctly: (run, smile, fly)", "run -> running (double consonant), smile -> smiling (drop e), fly -> flying (add -ing)", "All just add -ing.", "All double the last letter.", "run -> runing, smile -> smileing, fly -> flieing", "A", "3 distinct orthographic rules for -ing derivation."),
        ("Convert past tense narrative to present continuous picture scene: 'Doraemon fetched a gadget while Nobita watched.'", "Doraemon is fetching a gadget while Nobita is watching.", "Doraemon fetching while Nobita watching.", "Doraemon was fetching while Nobita watched.", "Doraemon will fetch while Nobita watches.", "A", "Both verbs transformed to present continuous (is fetching, is watching)."),
        ("Spot the missing auxiliary verb in: 'Doraemon helping Nobita and children watching TV.' Correct it:", "'Doraemon **is** helping Nobita and children **are** watching TV.'", "'Doraemon helping Nobita and children watching TV.'", "'Doraemon **are** helping and children **is** watching TV.'", "No error.", "A", "Present continuous requires auxiliary (is/am/are) before -ing verb."),
        ("Differentiate state vs action: Why don't we usually say 'Nobita is **knowing** the answer'?", "Because 'know' is a stative verb expressing state of knowledge, not an ongoing physical action.", "Because 'knowing' is hard to spell.", "Because Doraemon helped.", "Because Nobita is lazy.", "A", "Stative verbs (know, love, believe) do not usually take continuous form."),
        ("Identify the sentence with CORRECT present continuous subject-verb agreement:", "The children are enjoying the Doraemon episode.", "The children is enjoying the Doraemon episode.", "The children am enjoying the Doraemon episode.", "The children enjoying the Doraemon episode.", "A", "Plural subject ('children') takes plural auxiliary 'are'."),
        ("Form negative present continuous: 'Doraemon is giving up on Nobita.' -> Negative:", "Doraemon is **not** giving up on Nobita.", "Doraemon not giving up on Nobita.", "Doraemon is no giving up on Nobita.", "Doraemon isn't give up on Nobita.", "A", "Add 'not' between auxiliary 'is' and main verb 'giving'."),
        ("Spot all THREE spelling errors: 'He is **smileing** warmly, **runing** fast, and **dieing** of laughter.'", "'smileing' -> 'smiling'; 'runing' -> 'running'; 'dieing' -> 'dying'", "'smileing' -> 'smilling'; 'runing' -> 'runing'; 'dieing' -> 'dieing'", "No errors.", "Only 'runing' is wrong.", "A", "smiling (drop e), running (double n), dying (-ie to -y)."),
        ("Rewrite as interrogative present continuous: 'Doraemon is fetching a new gadget.'", "**Is** Doraemon fetching a new gadget?", "Are Doraemon fetching a new gadget?", "Doraemon fetching a new gadget?", "Why Doraemon is fetching gadget?", "A", "Move auxiliary 'Is' to beginning of sentence."),
        ("Analyze action timeline: 'The TV channel **is broadcasting** a new Doraemon special tomorrow.' What does present continuous express here?", "A fixed future arrangement / planned action.", "Past completed action.", "Action that happened long ago.", "Uncertain rumor.", "A", "Present continuous can express planned future actions."),
        ("Choose the sentence showing PARALLEL present continuous actions:", "While Doraemon is guiding, Nobita is trying his best.", "While Doraemon guided, Nobita is trying.", "Doraemon is guiding while Nobita tried.", "Doraemon guide while Nobita try.", "A", "Both parallel ongoing actions use present continuous."),
        ("Correct the error: 'Doraemon is flyying across the sky.'", "'flyying' should be 'flying' (single 'y').", "'is' should be 'are'.", "'sky' should be capitalized.", "No error.", "A", "Fly + ing = flying."),
        ("HOTS Reasoning: Compare 'Doraemon helped Nobita' (Past Simple) vs 'Doraemon is helping Nobita' (Present Continuous). How does the meaning change?", "Past simple states a completed past event; present continuous describes an action currently in progress.", "Both mean the exact same thing.", "Past simple is for future; continuous is for past.", "Continuous means Doraemon left.", "A", "Tense changes temporal aspect (completed vs ongoing)."),
        ("Form question: 'Why ____ the children ____ (watching) Doraemon?'", "are, watching", "is, watching", "am, watching", "do, watching", "A", "Plural subject children takes 'are ... watching'."),
        ("Identify the correct present continuous sentence describing show impact:", "The entire audience is enjoying the Doraemon movie.", "The entire audience is enjoy the Doraemon movie.", "The entire audience are enjoying the Doraemon movie.", "The entire audience enjoying the Doraemon movie.", "A", "Collective singular subject 'audience' + is + enjoying.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH06_CAT08_Q{idx:02d}"
        qtxt = f"Higher Order Present Continuous Analysis & Editing:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Continuous Tense Aspect & Error Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 9. Helping Verbs (Is, Am, Are) (50 Qs)
# ---------------------------------------------------------------------------
def build_helping_verbs():
    header = "# Category 9: Helping Verbs (Is, Am, Are) — Chapter 06: My Favourite Cartoon\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_hv = [
        ("Doraemon ___ a blue robotic cat.", "is", "are", "am", "be", "A", "Singular subject 'Doraemon' takes 'is'."),
        ("I ___ a big fan of the Doraemon cartoon.", "am", "is", "are", "be", "A", "Pronoun 'I' takes 'am'."),
        ("The gadgets ___ stored in his 4D pocket.", "are", "is", "am", "be", "A", "Plural subject 'gadgets' takes 'are'."),
        ("Nobita ___ a lazy but good-hearted boy.", "is", "are", "am", "be", "A", "Singular subject 'Nobita' takes 'is'."),
        ("The episodes ___ full of fun and adventure.", "are", "is", "am", "be", "A", "Plural subject 'episodes' takes 'are'."),
        ("Fujiko F. Fujio ___ the creator of Doraemon.", "is", "are", "am", "be", "A", "Singular subject takes 'is'."),
        ("The children ___ watching their favourite show.", "are", "is", "am", "be", "A", "Plural subject 'children' takes 'are'."),
        ("Doraemon and Nobita ___ best friends.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("I ___ sure that friendship is important.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The cartoon series ___ popular around the world.", "is", "are", "am", "be", "A", "Singular 'series' in this context takes 'is'."),
        ("The life lessons ___ valuable for everyone.", "are", "is", "am", "be", "A", "Plural 'lessons' takes 'are'."),
        ("The 4D pocket ___ located on Doraemon's belly.", "is", "are", "am", "be", "A", "Singular 'pocket' takes 'is'."),
        ("You ___ watching an episode of Doraemon.", "are", "is", "am", "be", "A", "Pronoun 'You' always takes 'are'."),
        ("Doraemon ___ fetching a futuristic tool.", "is", "are", "am", "be", "A", "Singular 'Doraemon' takes 'is'."),
        ("The gadgets ___ very helpful to Nobita.", "are", "is", "am", "be", "A", "Plural 'gadgets' takes 'are'."),
        ("I ___ happy when Nobita succeeds.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("Nobita ___ learning to be hard-working.", "is", "are", "am", "be", "A", "Singular 'Nobita' takes 'is'."),
        ("The viewers ___ enjoying the new episode.", "are", "is", "am", "be", "A", "Plural 'viewers' takes 'are'.")
    ]
    
    for idx, (sent_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_hv, start=1):
        qid = f"BK02_CH06_CAT09_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct helping verb (is / am / are):\n\n\"{sent_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Helping Verb Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Choose the correct helping verb: 'Doraemon and Nobita Nobi ____ facing a new challenge.'", "are", "is", "am", "be", "A", "Compound subject ('Doraemon and Nobita') is plural, taking 'are'."),
        ("Select the sentence with CORRECT helping verb agreement:", "Doraemon is fetching a bamboo copter.", "Doraemon are fetching a bamboo copter.", "Doraemon am fetching a bamboo copter.", "Doraemon be fetching a bamboo copter.", "A", "Singular noun 'Doraemon' requires 'is'."),
        ("Fill in the blanks: 'I ____ watching Doraemon, and my brothers ____ watching cartoons.'", "am, are", "is, are", "are, is", "am, is", "A", "'I am', 'brothers are'."),
        ("Identify the mistake in: 'The gadgets in the pocket **is** amazing.'", "'is' should be 'are' because 'gadgets' is a plural noun.", "'is' should be 'am'", "'is' should be 'was'", "No mistake", "A", "'gadgets' is plural, requiring 'are'."),
        ("Which helping verb completes the question? '____ you a fan of Doraemon?'", "Are", "Is", "Am", "Be", "A", "Subject 'you' takes 'Are'."),
        ("Fill in the blank: 'Neither laziness nor excuses ____ helpful in the long run.'", "are", "is", "am", "be", "A", "'Neither...nor' with plural second subject 'excuses' takes 'are'."),
        ("Select the correct sentence for story moral:", "Responsibility and friendship are essential life values.", "Responsibility and friendship is essential life values.", "Responsibility and friendship am essential life values.", "Responsibility and friendship be essential life values.", "A", "Compound subject 'Responsibility and friendship' takes 'are'."),
        ("Complete the conversation: Nobita: 'Where ____ my gadgets?' Doraemon: 'They ____ in my pocket!'", "are, are", "is, is", "is, are", "are, is", "A", "Plural 'my gadgets' -> are; plural 'They' -> are."),
        ("Identify where 'is' is used incorrectly:", "The gadgets **is** helpful.", "Doraemon is blue.", "Nobita is young.", "The show is funny.", "A", "'The gadgets is' should be 'The gadgets are'."),
        ("Choose the correct helping verb for collective noun used as a single unit: 'The audience ____ cheering for Doraemon.'", "is", "are", "am", "be", "A", "Collective noun 'audience' treated as singular unit takes 'is'."),
        ("Fill in the blank: 'Nobita ____ not always lazy when he tries hard.'", "is", "are", "am", "be", "A", "Singular 'Nobita' takes 'is'."),
        ("Select the sentence with correct helping verb for 'I':", "I am drawing a picture of Doraemon.", "I is drawing a picture of Doraemon.", "I are drawing a picture of Doraemon.", "I be drawing a picture of Doraemon.", "A", "Subject 'I' takes 'am'."),
        ("Fill in the blank: 'There ____ many gadgets in Doraemon's pouch.'", "are", "is", "am", "be", "A", "'There are' before plural noun 'many gadgets'."),
        ("Fill in the blank: 'There ____ a 4D pocket on his belly.'", "is", "are", "am", "be", "A", "'There is' before singular noun 'a 4D pocket'."),
        ("Choose the correct sentence:", "What are the children learning from the cartoon?", "What is the children learning from the cartoon?", "What am the children learning from the cartoon?", "What be the children learning from the cartoon?", "A", "Plural subject 'the children' takes 'are'."),
        ("Identify the correct form: 'Doraemon, as well as his friends, ____ going on an adventure.'", "is", "are", "am", "be", "A", "Subject is singular 'Doraemon' ('as well as...' does not change subject number), taking 'is'."),
        ("Fill in the blank: 'Both Doraemon and Nobita ____ happy at the end of the episode.'", "are", "is", "am", "be", "A", "'Both ... and ...' takes plural verb 'are'."),
        ("Select the option with correct helping verbs: 'Nobita ____ lazy, but Doraemon ____ helpful.'", "is, is", "are, is", "am, are", "is, are", "A", "'Nobita is', 'Doraemon is'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH06_CAT09_Q{idx:02d}"
        qtxt = f"Helping Verb Subject-Verb Agreement Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Subject-Verb Agreement Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze subject-verb agreement: 'Each of the futuristic gadgets **____** stored in the pocket.' Choose the correct verb and reason:", "is — because 'Each' is a singular indefinite pronoun requiring singular verb 'is'.", "are — because 'futuristic gadgets' is plural.", "am — because it refers to speaker.", "be — because gadgets are magic.", "A", "'Each' is singular indefinite pronoun taking singular verb 'is'."),
        ("Spot the subtle agreement error in: 'A set of magic gadgets **are** lying on the floor.'", "'are' should be 'is' because the subject is singular noun 'set'.", "'are' should be 'am'.", "'gadgets' should be 'gadget'.", "No error.", "A", "'A set' is singular, so it requires 'is lying'."),
        ("Compare: (1) 'Doraemon and Nobita **are** flying.' vs (2) 'Doraemon, together with Nobita, **is** flying.' Why are the verbs different?", "In (1), 'and' creates a plural subject (are); in (2), 'together with' is a prepositional phrase, leaving 'Doraemon' as sole singular subject (is).", "They mean different things.", "Sentence (2) is grammatically wrong.", "Both should use 'are'.", "A", "Prepositional phrases like 'together with' do not change subject number."),
        ("Identify the correct agreement for indefinite pronouns: 'Everyone in the family **____** watching the cartoon.'", "is", "are", "am", "be", "A", "'Everyone' is a singular indefinite pronoun requiring 'is'."),
        ("Spot all THREE subject-verb errors in: 'The gadgets **is** magic, I **is** watching, and Doraemon **are** blue.'", "'gadgets is' -> 'gadgets are'; 'I is' -> 'I am'; 'Doraemon are' -> 'Doraemon is'", "'gadgets is' -> 'gadgets am'; 'I is' -> 'I are'; 'Doraemon are' -> 'Doraemon am'", "Only 'I is' is wrong.", "No errors present.", "A", "gadgets are (plural), I am (1st person), Doraemon is (3rd person singular)."),
        ("Fill in the blanks in this complex sentence: 'Not only Nobita but also his friends **____** watching, while Doraemon **____** helping.'", "are, is", "is, are", "is, is", "are, are", "A", "'Not only...but also' agrees with closer subject ('friends' -> are); 'Doraemon' -> is."),
        ("Transform to negative: 'Doraemon and Nobita are in the room.'", "Doraemon and Nobita **are not** in the room.", "Doraemon and Nobita is not in the room.", "Doraemon and Nobita am not in the room.", "Doraemon and Nobita not in room.", "A", "Add 'not' after plural helping verb 'are'."),
        ("Analyze inverted subject position: 'Inside the 4D pocket **____** stored many futuristic gadgets.'", "are", "is", "am", "be", "A", "Subject is plural 'many futuristic gadgets', appearing after verb, requiring 'are'."),
        ("Determine agreement with uncountable nouns: 'The information stored in the gadget **____** useful.'", "is", "are", "am", "be", "A", "Uncountable noun 'information' is treated as singular, taking 'is'."),
        ("Correct the sentence: 'Here **is** the gadgets you requested.'", "Here **are** the gadgets you requested.", "Here am the gadgets you requested.", "Here be the gadgets you requested.", "No error.", "A", "Plural subject 'gadgets' requires 'Here are...''"),
        ("Identify the sentence where 'is' acts as a MAIN linking verb rather than a helping verb:", "Doraemon **is** a robotic cat.", "Doraemon **is** helping Nobita.", "Doraemon **is** fetching a gadget.", "Doraemon **is** flying in the air.", "A", "In 'Doraemon is a robotic cat', 'is' is the main linking verb connecting subject to predicate noun."),
        ("HOTS Reasoning: Why does English use 'am' ONLY with the subject pronoun 'I'?", "Because 'am' is the unique 1st person singular present indicative form of the verb 'to be'.", "Because 'I' is capitalized.", "Because Doraemon commanded it.", "There is no reason.", "A", "'am' is exclusively reserved for 1st person singular 'I'."),
        ("Fill in the blanks: 'Neither Nobita nor his classmates **____** working hard, because the lesson **____** difficult.'", "are, is", "is, are", "is, is", "are, are", "A", "'classmates' is closer plural subject -> are; 'lesson' -> is."),
        ("Select the option with PERFECT helping verb agreement throughout:", "Doraemon is blue, I am watching, and the gadgets are magic.", "Doraemon are blue, I is watching, and the gadgets is magic.", "Doraemon am blue, I are watching, and the gadgets am magic.", "Doraemon is blue, I is watching, and the gadgets is magic.", "A", "Doraemon is (singular), I am (1st person), gadgets are (plural).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH06_CAT09_Q{idx:02d}"
        qtxt = f"Higher Order Helping Verb Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Subject-Verb Agreement & Syntax", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# MAIN EXECUTION FOR REBUILDING CHAPTER 06
# ---------------------------------------------------------------------------
def rebuild_chapter_06():
    print("Rebuilding Chapter 06 category files with high-quality, multi-tiered (Easy/Medium/Hard) non-duplicate questions...")

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
        filepath = os.path.join(CH06_DIR, fname)
        print(f"  Generating {fname}...")
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {fname} created successfully.")

    print("\n[SUCCESS] Completed rebuilding all 9 category files for Chapter 06 (450 total high-quality questions)!")

if __name__ == "__main__":
    rebuild_chapter_06()
