r"""
=============================================================================
Script: rebuild_chapter_02.py
Description: Generates 50 rich, non-duplicate, multi-tiered (Easy, Medium, Hard)
             questions for each of the 9 category files in Chapter 02:
             "Four Brahmins" (450 Qs total).
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH02_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_02")
os.makedirs(CH02_DIR, exist_ok=True)

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
    header = "# Category 1: Plural Nouns & Spelling Rules — Chapter 02: Four Brahmins\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("Brahmin", "Brahmins", "Brahmines", "Brahminz", "Brahminies", "A", "Regular noun adding -s."),
        ("disciple", "disciples", "disciplies", "disciplex", "disciplez", "A", "Regular noun adding -s."),
        ("sage", "sages", "sagies", "sagees", "sagez", "A", "Regular noun ending in -e adds -s."),
        ("skill", "skills", "skilles", "skillies", "skillz", "A", "Regular noun adding -s."),
        ("bone", "bones", "bonies", "bonees", "bonez", "A", "Regular noun ending in -e adds -s."),
        ("lion", "lions", "liones", "lionies", "lionz", "A", "Regular noun adding -s."),
        ("tree", "trees", "treess", "treies", "treez", "A", "Regular noun adding -s."),
        ("body", "bodies", "bodys", "bodyes", "bodiez", "A", "Consonant + y changes to -ies."),
        ("friend", "friends", "friendes", "friendies", "friendz", "A", "Regular noun adding -s."),
        ("organ", "organs", "organes", "organies", "organz", "A", "Regular noun adding -s."),
        ("muscle", "muscles", "musclies", "musclees", "musclez", "A", "Regular noun ending in -e adds -s."),
        ("ashram", "ashrams", "ashrames", "ashramies", "ashramz", "A", "Regular noun adding -s."),
        ("town", "towns", "townes", "townies", "townz", "A", "Regular noun adding -s."),
        ("life", "lives", "lifes", "lifees", "livs", "A", "Nouns ending in -fe change -fe to -ves."),
        ("leaf", "leaves", "leafs", "leafes", "leavs", "A", "Nouns ending in -f change -f to -ves."),
        ("man", "men", "mans", "manes", "mens", "A", "Irregular plural: man becomes men."),
        ("tooth", "teeth", "tooths", "toothes", "teethes", "A", "Irregular plural: tooth becomes teeth."),
        ("foot", "feet", "foots", "feets", "footes", "A", "Irregular plural: foot becomes feet.")
    ]
    
    for idx, (word, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH02_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{word}'** from or related to Chapter 02 (*Four Brahmins*)?"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Plural Noun Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The sage was surrounded by four (disciple / disciples).", "disciples", "disciple", "disciplies", "disciplex", "A", "'four' requires plural noun 'disciples'."),
        ("The first Brahmin assembled all the (bone / bones) of the lion.", "bones", "bone", "bonies", "boness", "A", "'all the' with countable noun requires plural 'bones'."),
        ("The second Brahmin restored the (organ / organs) and skin.", "organs", "organ", "organes", "organies", "A", "'organs' is the plural form."),
        ("Identify the INCORRECT plural spelling in this list: trees, lions, bodis, ashrams.", "bodis", "trees", "lions", "ashrams", "A", "Plural of body is 'bodies', not 'bodis'."),
        ("Choose the sentence with the correct plural noun form:", "Three Brahmins brought the lion to life.", "Three Brahmines brought the lion to life.", "Three Brahmins brought the lion to lifes.", "Three Brahmin brought the lion to lives.", "A", "Brahmins (plural), life (singular concept/plural lives)."),
        ("Which noun forms its plural by changing -fe to -ves?", "life -> lives", "lion -> lions", "tree -> trees", "sage -> sages", "A", "Life ends in -fe, so plural is lives."),
        ("Change the singular noun in brackets to plural: 'The lion had sharp ____ (tooth).'", "teeth", "tooths", "toothes", "teethes", "A", "Irregular plural of tooth is teeth."),
        ("Select the sentence where ALL plural nouns are spelt correctly:", "The disciples saw the bones under the trees.", "The disciplex saw the bones under the trees.", "The disciples saw the bonies under the treess.", "The disciplees saw the bones under the trees.", "A", "disciples, bones, trees are all correctly spelt plurals."),
        ("What is the correct plural of 'simpleton'?", "simpletons", "simpletones", "simpletonies", "simpletonz", "A", "Regular noun adding -s."),
        ("The Brahmins spent many (day / days) studying at the ashram.", "days", "daies", "day", "dayes", "A", "Vowel + y adds -s (days)."),
        ("The fourth Brahmin climbed up among the green (leaf / leaves).", "leaves", "leafs", "leafes", "leavs", "A", "Nouns ending in -f change to -ves (leaves)."),
        ("The third Brahmin showed his magical (power / powers).", "powers", "power", "poweres", "poweries", "A", "Plural noun 'powers'."),
        ("How many (skeleton / skeletons) were lying near the tree?", "skeletons", "skeleton", "skeletones", "skeletonies", "A", "Plural noun 'skeletons'."),
        ("The lion attacked the three (man / men).", "men", "mans", "manes", "mens", "A", "Irregular plural of man is men."),
        ("Which plural noun rule applies to the word **'bodies'**?", "Consonant + y changes to -ies", "Add -es to -x", "Add -s to vowel + y", "Change -f to -ves", "A", "Body ends in consonant + y, so y becomes -ies."),
        ("The sage taught many (lesson / lessons) to his disciples.", "lessons", "lessones", "lessonies", "lessonz", "A", "Regular noun adding -s."),
        ("Identify the correct plural form of 'child' (like the young disciple):", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("The fourth Brahmin heard the heavy (step / steps) of the lion.", "steps", "stepes", "step", "stepies", "A", "Regular noun adding -s.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH02_CAT01_Q{idx:02d}"
        qtxt = f"Contextual Plural Rule Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Plural Noun Application", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Rewrite the sentence in PLURAL form: 'The Brahmin saw a lion near the tree.'", "The Brahmins saw lions near the trees.", "The Brahmines saw lions near the treess.", "The Brahmins saw lion near the trees.", "The Brahmin saw lions near the treez.", "A", "Plural of Brahmin->Brahmins, lion->lions, tree->trees."),
        ("Analyze the error: 'The third Brahmin said that books give knowledge but not wisdoms.' Why is 'wisdoms' wrong here?", "'wisdom' is an uncountable abstract noun and does not normally take a plural -s.", "'wisdoms' should be 'wisdomes'.", "'wisdoms' should be 'wisdome'.", "'wisdoms' should be 'wizdoms'.", "A", "Abstract uncountable nouns like wisdom do not take plural forms."),
        ("Complete the paragraph with correct plurals: 'The three ____ (man) used their magical ____ (skill) to assemble the ____ (bone).'", "men, skills, bones", "mans, skilles, bonies", "mens, skills, bone", "men, skilles, bones", "A", "men (irregular), skills (regular), bones (-e + s)."),
        ("Identify the sentence where ALL three underlined nouns are correctly pluralized:", "The **disciples** lost their **lives** because of their **mistakes**.", "The **disciplex** lost their **lifes** because of their **mistakes**.", "The **disciples** lost their **lifes** because of their **mistakies**.", "The **disciplees** lost their **lives** because of their **mistakes**.", "A", "disciples (-s), lives (-fe to -ves), mistakes (-s)."),
        ("Which group contains ONLY irregular plural nouns?", "men, teeth, feet, children", "lions, trees, bones, sages", "bodies, cities, stories, armies", "leaves, thieves, wolves, knives", "A", "men, teeth, feet, children change internal vowels/endings without -s/-es."),
        ("Why does 'day' become 'days' but 'body' becomes 'bodies'?", "Because 'day' has a vowel before y (a+y -> -s), while 'body' has a consonant before y (d+y -> -ies).", "Because 'day' is short and 'body' is long.", "Because 'day' is time and 'body' is physical.", "Both follow the exact same rule.", "A", "Vowel+y adds -s; Consonant+y changes y to -ies."),
        ("Find the TWO grammatical mistakes in: 'The three Brahmines saw many mouses near the forest.'", "'Brahmines' should be 'Brahmins' and 'mouses' should be 'mice'.", "'Brahmines' should be 'Brahmin' and 'mouses' should be 'mices'.", "'forest' should be 'forests' only.", "There are no mistakes in the sentence.", "A", "Brahmins (regular -s) and mice (irregular plural)."),
        ("Replace the singular words in brackets: 'The lion had sharp ____ (claw) and heavy ____ (foot).'", "claws, feet", "clawes, foots", "claws, feets", "clawies, foots", "A", "Plural of claw is claws, plural of foot is feet."),
        ("Analyze this sentence: 'The sage gave advice to his disciples.' Can 'advice' be pluralized as 'advices'?", "No, 'advice' is uncountable; we say 'pieces of advice' for plural.", "Yes, 'advices' is correct.", "No, it becomes 'advicess'.", "Yes, 'an advice' is correct.", "A", "Advice is an uncountable noun."),
        ("Fill in the blanks: 'The lion ate the three ____ (Brahmin) and left their ____ (body) on the ground.'", "Brahmins, bodies", "Brahmines, bodys", "Brahmins, bodyes", "Brahmines, bodies", "A", "Brahmin -> Brahmins; body -> bodies."),
        ("Select the option that shows correct plural transformation for ALL three words: 'shelf', 'story', 'fox'", "shelves, stories, foxes", "shelfs, storys, foxs", "shelves, storyes, foxies", "shelfes, stories, foxen", "A", "shelf -> shelves; story -> stories; fox -> foxes."),
        ("HOTS Reasoning: Why do we say 'knowledge is power' rather than 'knowledges are powers'?", "Because 'knowledge' is an uncountable concept that stays singular.", "Because knowledge comes from books.", "Because power is plural.", "Because sage said so.", "A", "Uncountable abstract nouns take singular verbs."),
        ("Transform into singular: 'The sages taught the simpletons under the banyan trees.'", "The sage taught the simpleton under the banyan tree.", "The sages taught the simpleton under the banyan tree.", "The sage teach the simpleton under the banyan tree.", "The sage taught the simpletons under the banyan tree.", "A", "Singular forms: sage, simpleton, tree."),
        ("Identify the correct rule for forming the plural of **'ashram'**:", "Add -s because it is a regular noun ending in a consonant (ashrams).", "Add -es (ashrames).", "Change -m to -ves (ashravs).", "Change vowel sound.", "A", "Regular noun adding -s.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH02_CAT01_Q{idx:02d}"
        qtxt = f"Higher Order Thinking Skills (HOTS) & Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Plural & Spelling Analysis", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 2. Articles Grammar (50 Qs)
# ---------------------------------------------------------------------------
def build_articles_grammar():
    header = "# Category 2: Articles (A, An, The) — Chapter 02: Four Brahmins\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("A wise sage lived in ___ ashram.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'ashram'."),
        ("The fourth disciple was ___ simpleton.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'simpleton'."),
        ("The first Brahmin saw ___ skeleton of a lion.", "the", "a", "an", "no article", "A", "Use 'the' for specific skeleton mentioned."),
        ("Three disciples wanted to go to ___ town.", "the", "a", "an", "no article", "A", "Use 'the' for specific destination town."),
        ("The second Brahmin created ___ organ for the lion.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'organ'."),
        ("___ Panchatantra story teaches common sense.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'Panchatantra'."),
        ("The fourth Brahmin climbed ___ tree quickly.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'tree'."),
        ("The third Brahmin chanted ___ spell to revive the lion.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'spell'."),
        ("___ lion attacked the three clever friends.", "The", "A", "An", "No article", "A", "Use 'The' for specific lion revived in story."),
        ("The fourth Brahmin was ___ honest person.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' sound in 'honest'."),
        ("It was ___ evening when they stopped to rest.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'evening'."),
        ("The lion was ___ ferocious animal.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'ferocious'."),
        ("___ fourth Brahmin survived the incident.", "The", "A", "An", "No article", "A", "Use 'The' for ordinal number 'fourth'."),
        ("They found the bones under ___ old banyan tree.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'old'."),
        ("The sage was ___ wise teacher.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'wise'."),
        ("The third Brahmin made ___ big mistake.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'big'."),
        ("The lion had ___ appetite after coming back to life.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'appetite'."),
        ("Dilip returned to ___ ashram of his guru.", "the", "a", "an", "no article", "A", "Use 'the' for specific ashram of his guru.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH02_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article (a / an / the):\n\n\"{q_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Basic Article Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The fourth Brahmin warned ___ third Brahmin, but ___ warning was ignored.", "the, the", "a, an", "an, a", "a, the", "A", "Both third Brahmin and warning are specific in this context."),
        ("Why do we say '**an** ashram' but '**a** simpleton'?", "Because 'ashram' begins with a vowel sound (a) and 'simpleton' with a consonant sound (s).", "Because ashrams are big.", "Because simpletons are poor.", "Because sage lived there.", "A", "Article selection depends on initial vowel/consonant sound."),
        ("Select the sentence with CORRECT article usage:", "The sage had a wise disciple and a simpleton.", "The sage had an wise disciple and an simpleton.", "The sage had the a wise disciple.", "The sage had a an wise disciple.", "A", "'a wise' (/w/) and 'a simpleton' (/s/) both take 'a'."),
        ("Fill in the blanks: 'The second Brahmin restored ___ skin on ___ skeleton.'", "the, the", "a, a", "an, an", "a, the", "A", "Both skin and skeleton are specific items of the lion in the story."),
        ("Identify the INCORRECT article in: 'The fourth Brahmin climbed **an** tree.'", "'an' should be 'a'", "'an' should be 'the'", "'tree' should be 'an tree'", "No mistake", "A", "'tree' starts with consonant sound /t/, so it takes 'a'."),
        ("Which article completes the sentence? 'Learning magic requires ___ active mind.'", "an", "a", "the", "no article", "A", "'active' starts with vowel sound /a/, requiring 'an'."),
        ("Choose the correct pair of articles: '___ lion roared in ___ forest.'", "The, the", "A, a", "An, an", "The, a", "A", "'The lion' (specific lion revived in story), 'the forest' (specific location)."),
        ("Why do we use 'a' before 'majestic lion' in 'They saw **a** majestic lion'?", "Because 'majestic' begins with the consonant sound /m/.", "Because lion is wild.", "Because majestic is a noun.", "Because the Brahmin was clever.", "A", "'majestic' starts with consonant sound /m/."),
        ("Complete the dialogue: Fourth Brahmin: 'Do not revive ___ lion!' Third Brahmin: 'I have ___ magic spell!'", "the, a", "a, an", "an, the", "the, the", "A", "'the lion' (specific dead lion), 'a magic spell' (consonant sound)."),
        ("Select the correct sentence:", "A lion is a dangerous animal.", "An lion is a dangerous animal.", "The lion is an dangerous animal.", "An lion is an dangerous animal.", "A", "'A lion' (consonant sound), 'a dangerous animal' (consonant sound)."),
        ("Fill in the blank: 'The fourth Brahmin waited for ___ long time on the tree branch.'", "a", "an", "the", "no article", "A", "Idiomatic phrase 'for a long time'."),
        ("Identify where NO article is needed:", "The story shows that **___ wisdom** is better than bookish knowledge.", "They saw ___ lion.", "He climbed ___ tree.", "He had ___ spell.", "A", "Abstract nouns like 'wisdom' generally do not take articles in general context."),
        ("Choose the correct sentence for story summary:", "Bookish knowledge without common sense is useless.", "A bookish knowledge without common sense is useless.", "An bookish knowledge without common sense is useless.", "The bookish a knowledge is useless.", "A", "Abstract concept 'Bookish knowledge' takes no indefinite article."),
        ("Fill in the blanks: 'The fourth Brahmin spent ___ hour waiting on ___ branch.'", "an, a", "a, a", "an, an", "the, an", "A", "'an hour' (silent h), 'a branch' (consonant b)."),
        ("Which sentence uses 'the' correctly for ordinal numbers?", "The fourth Brahmin was the wisest of them all.", "The fourth Brahmin was a wisest of them all.", "The fourth Brahmin was an wisest of them all.", "Fourth Brahmin was wisest of them all.", "A", "Ordinal 'The fourth' and superlative 'the wisest' take 'the'."),
        ("Identify the article error: 'The third Brahmin chanted **a** spell with **an** great confidence.'", "'an great' should be 'great' or 'a great'", "'a spell' should be 'an spell'", "'third' needs 'a'", "No error", "A", "'great' starts with consonant sound /g/, so it takes 'a great' or no article with uncountable noun."),
        ("Complete: 'It was ___ unexpected attack by ___ hungry lion.'", "an, a", "a, an", "the, the", "an, an", "A", "an unexpected (/u/), a hungry (/h/)."),
        ("Choose the correct option: '___ sun set while the Brahmins rested.'", "The", "A", "An", "No article", "A", "'The sun' (unique celestial body).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH02_CAT02_Q{idx:02d}"
        qtxt = f"Contextual Article Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Article Usage in Context", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze article usage in: 'The three Brahmins lacked **a** common sense.' Correct the error:", "'a common sense' -> 'common sense' (uncountable abstract noun takes no indefinite article).", "'a common sense' -> 'an common sense'.", "'a common sense' -> 'the a common sense'.", "No error present.", "A", "'common sense' is uncountable and takes no article 'a'."),
        ("Fill in all three blanks: '___ sage told ___ disciples that ___ life must be respected.'", "The, the, no article", "A, an, a", "An, a, the", "The, a, a", "A", "'The sage' (specific), 'the disciples' (specific), 'life' (general abstract)."),
        ("Identify why 'the' is used in: 'The fourth Brahmin climbed **the** tree.'", "Because 'the tree' refers to the specific tree under which they were resting in the story.", "Because tree is a proper noun.", "Because lion climbed it.", "Because sage was rich.", "A", "'The' specifies the definite tree mentioned in the narrative."),
        ("Spot the TWO article errors: 'It took **a** hour for **a** eagle to fly past.'", "'a hour' should be 'an hour' and 'a eagle' should be 'an eagle'.", "'a hour' should be 'the hour' and 'a eagle' should be 'a eagle'.", "No errors.", "Only 'a hour' is wrong.", "A", "Both 'hour' (silent h) and 'eagle' (vowel e) require 'an'."),
        ("Choose the paragraph with PERFECT article usage throughout:", "A sage had four disciples. Three disciples were clever. The fourth disciple was a simpleton.", "An sage had four disciples. A three disciples were clever. A fourth disciple was an simpleton.", "The sage had four a disciples. Three disciples were a clever.", "A sage had an four disciples. The three disciples were an clever.", "A", "A sage (first mention), Three disciples, The fourth (ordinal), a simpleton."),
        ("Why is it correct to write 'a universe of knowledge' but 'an understanding of life'?", "Because 'universe' begins with consonant sound /j/ (yoo), while 'understanding' begins with vowel sound /u/.", "Because universe is big.", "Because understanding is free.", "Both take 'an'.", "A", "Sound determines article: /yoo/ is a consonant sound."),
        ("Select the option that correctly completes the story moral: '___ clever mind without ___ wisdom is ___ dangerous combination.'", "A, no article, a", "An, a, an", "The, the, the", "A, a, a", "A", "A clever mind, wisdom (no article), a dangerous combination."),
        ("Analyze this sentence: 'The fourth Brahmin returned to **the** ashram.' Why is 'the' appropriate?", "Because it refers to the specific ashram of the sage where they lived.", "Because ashram is in a town.", "Because ashram is plural.", "Because four is a number.", "A", "'the' specifies the known home ashram."),
        ("Correct the sentence: 'An lion ate a three Brahmins.'", "A lion ate the three Brahmins.", "The lion ate an three Brahmins.", "An lion ate the three Brahmins.", "A lion ate a three Brahmins.", "A", "'A lion' (/l/ sound), 'the three Brahmins' (specific group)."),
        ("Fill in the blanks: '___ magic is ___ fascinating subject, but ___ magic used by the third Brahmin caused harm.'", "No article, a, the", "A, a, a", "The, an, the", "An, a, a", "A", "'Magic' (abstract general, no article); 'a fascinating subject'; 'the magic' (specific magic used by third Brahmin)."),
        ("Spot the missing article: 'Fourth Brahmin stayed on branch until lion walked away.'", "Missing 'The' before 'Fourth' -> 'The fourth Brahmin stayed on a branch...'", "Missing 'a' before 'lion'", "Missing 'an' before 'stayed'", "No article is missing", "A", "Ordinal 'Fourth' needs 'The fourth'; branch needs 'a branch'."),
        ("HOTS Reasoning: Which sentence uses 'a', 'an', and 'the' correctly in a single rule demonstration?", "An eagle flew over a tree in the forest.", "A eagle flew over an tree in a forest.", "The eagle flew over an tree in an forest.", "An eagle flew over an tree in the forest.", "A", "An eagle (vowel), a tree (consonant), the forest (specific)."),
        ("Rewrite correctly: 'The third Brahmin was a arrogant man who made an big mistake.'", "The third Brahmin was an arrogant man who made a big mistake.", "The third Brahmin was a arrogant man who made a big mistake.", "The third Brahmin was an arrogant man who made an big mistake.", "The third Brahmin was the arrogant man who made an big mistake.", "A", "'an arrogant' (vowel /a/), 'a big mistake' (consonant /b/)."),
        ("Identify the correct rule for using 'the' with ordinal numbers (first, second, third, fourth):", "Ordinal numbers take 'the' when identifying specific items in a series.", "Ordinal numbers always take 'an'.", "Ordinal numbers never take articles.", "Ordinal numbers take 'a' only.", "A", "Ordinal numbers specify definite positions (the first, the second, the fourth).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH02_CAT02_Q{idx:02d}"
        qtxt = f"Higher Order Article Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Article Analysis & Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 3. Calendar & Days Vocabulary (50 Qs)
# ---------------------------------------------------------------------------
def build_calendar_days():
    header = "# Category 3: Calendar, Days & Abbreviations — Chapter 02: Four Brahmins\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    days_easy = [
        ("The four Brahmins started their journey in the **morning**. What word means the end of the day before night?", "Evening", "Afternoon", "Midnight", "Dawn", "A", "Evening is the time before night."),
        ("What is the standard abbreviation for **Tuesday**?", "Tue.", "Tues.", "Tu.", "Ts.", "A", "Tue. is standard abbreviation."),
        ("Which day comes right after Wednesday?", "Thursday", "Friday", "Tuesday", "Saturday", "A", "Thursday follows Wednesday."),
        ("What is the abbreviation for **Thursday**?", "Thu. / Thurs.", "Thr.", "Ths.", "Tu.", "A", "Thu. is standard abbreviation."),
        ("If the Brahmins walked for 1 full week, how many days did they walk?", "7 days", "5 days", "10 days", "30 days", "A", "1 week = 7 days."),
        ("Which month comes right before April?", "March", "May", "February", "January", "A", "March comes before April."),
        ("What is the short abbreviation for **March**?", "Mar.", "Mch.", "Ma.", "Mr.", "A", "Mar. is standard abbreviation."),
        ("The Brahmins rested under the tree in the evening. What word means the middle of the day?", "Noon / Midday", "Midnight", "Dawn", "Twilight", "A", "Noon/midday is 12:00 PM."),
        ("What is the abbreviation for **Friday**?", "Fri.", "Frid.", "Fr.", "F.", "A", "Fri. is standard abbreviation."),
        ("How many months are in a half year?", "6 months", "12 months", "3 months", "4 months", "A", "Half of 12 months = 6 months."),
        ("Which month comes after May?", "June", "July", "April", "August", "A", "June comes after May."),
        ("What is the short abbreviation for **June**?", "Jun. / June", "Jn.", "Ju.", "Jne.", "A", "Jun. or June is standard abbreviation."),
        ("If today is Wednesday, what day was yesterday?", "Tuesday", "Thursday", "Monday", "Friday", "A", "Yesterday was Tuesday."),
        ("If today is Friday, what day will tomorrow be?", "Saturday", "Thursday", "Sunday", "Monday", "A", "Tomorrow will be Saturday."),
        ("What is the abbreviation for **Saturday**?", "Sat.", "Satur.", "Sa.", "St.", "A", "Sat. is standard abbreviation."),
        ("Which day comes between Monday and Wednesday?", "Tuesday", "Thursday", "Sunday", "Friday", "A", "Tuesday is between Monday and Wednesday."),
        ("What is the abbreviation for **November**?", "Nov.", "Nove.", "Nv.", "Nvm.", "A", "Nov. is standard abbreviation."),
        ("Which month comes right before December?", "November", "October", "January", "September", "A", "November comes before December.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(days_easy, start=1):
        qid = f"BK02_CH02_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Vocabulary & Time Concepts:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Days & Calendar Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The Brahmins left the ashram on **Tuesday morning**. They walked for 2 full days before finding the bones. On which day did they find the bones?", "Thursday", "Wednesday", "Friday", "Saturday", "A", "Tuesday + 2 days = Wednesday(1), Thursday(2)."),
        ("The third Brahmin took 3 minutes to chant his spell. If he started at **4:00 PM**, at what time did the lion come alive?", "4:03 PM", "4:30 PM", "5:00 PM", "4:15 PM", "A", "4:00 PM + 3 minutes = 4:03 PM."),
        ("Match the day with its abbreviation: **Sunday**", "Sun.", "Snd.", "Su.", "Sn.", "A", "Sun. is standard."),
        ("If the fourth Brahmin stayed in the tree from **6:00 PM** to **6:00 AM**, how many hours was he in the tree?", "12 hours", "6 hours", "24 hours", "10 hours", "A", "6:00 PM to 6:00 AM is 12 hours (overnight)."),
        ("Identify the correctly spelt month name:", "October", "Octobre", "Octoberr", "October", "A", "October is the correct spelling."),
        ("Identify the INCORRECT pair of day and abbreviation:", "Monday - Mon.", "Tuesday - Tue.", "Wednesday - Wed.", "Thursday - Thr.", "D", "Thursday abbreviation is Thu. / Thurs., not Thr."),
        ("The disciples spent **3 years** learning at the ashram. How many months is 3 years?", "36 months", "24 months", "12 months", "30 months", "A", "3 years x 12 months = 36 months."),
        ("Which month has 31 days and comes right after June?", "July", "August", "May", "September", "A", "July has 31 days and follows June."),
        ("Rearrange in correct chronological order: Thu, Tue, Wed, Fri", "Tue, Wed, Thu, Fri", "Wed, Tue, Thu, Fri", "Tue, Thu, Wed, Fri", "Fri, Thu, Wed, Tue", "A", "Tuesday -> Wednesday -> Thursday -> Friday."),
        ("What day is 3 days before Friday?", "Tuesday", "Wednesday", "Monday", "Thursday", "A", "Friday - 3 days = Thursday(1), Wednesday(2), Tuesday(3)."),
        ("If the lion went away after 1 hour, how many minutes did the fourth Brahmin wait?", "60 minutes", "30 minutes", "100 minutes", "12 minutes", "A", "1 hour = 60 minutes."),
        ("Select the month that has exactly 30 days:", "September", "October", "December", "August", "A", "September has 30 days."),
        ("Which abbreviation stands for **February**?", "Feb.", "Febr.", "Fe.", "Fb.", "A", "Feb. is standard abbreviation."),
        ("If today is **Wed.**, what day will it be after 14 days?", "Wednesday", "Thursday", "Tuesday", "Sunday", "A", "14 days is exactly 2 full weeks (7x2), so it lands on Wednesday again."),
        ("The Brahmins' journey began in **Oct.** and ended in **Nov.**. How many months are mentioned?", "2 months", "1 month", "3 months", "4 months", "A", "October and November = 2 months."),
        ("Identify the word that means 'occurring once every week':", "Weekly", "Daily", "Monthly", "Yearly", "A", "Weekly means once a week."),
        ("Which of the following is a weekday (school working day)?", "Monday", "Sunday", "Saturday", "Weekend", "A", "Monday is a standard weekday."),
        ("Choose the correct abbreviation for **August**:", "Aug.", "Augu.", "Au.", "Ag.", "A", "Aug. is standard.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH02_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Application & Story Timeline:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Calendar & Time Reasoning", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("The Brahmins left the ashram on **Mon., 1st March** and reached the forest on **Fri., 5th March**. How many days did they travel?", "5 days", "4 days", "3 days", "7 days", "A", "1st to 5th March inclusive is 5 days (Mon, Tue, Wed, Thu, Fri)."),
        ("The fourth Brahmin was in the tree for 12 hours. If he climbed up at **6:00 PM on Friday**, at what time and day did he get down?", "6:00 AM on Saturday", "6:00 PM on Saturday", "12:00 PM on Friday", "6:00 AM on Sunday", "A", "6:00 PM Friday + 12 hours = 6:00 AM Saturday."),
        ("Solve the calendar puzzle: If 1st November is a Thursday, what day of the week will 15th November be?", "Thursday", "Friday", "Wednesday", "Saturday", "A", "1 + 14 (2 weeks) = 15th November, so it falls on Thursday."),
        ("Analyze this schedule: 1st Brahmin studied Mon & Thu; 2nd Brahmin studied Tue & Fri; 3rd Brahmin studied Wed & Sat. On which day did ALL THREE rest together?", "Sunday", "Monday", "Saturday", "Wednesday", "A", "Sunday is not listed in any study schedule."),
        ("Complete the full series of day abbreviations: Mon., Tue., Wed., ____, Fri., Sat., ____.", "Thu., Sun.", "Thurs., Sun.", "Th., Su.", "Thu., Sn.", "A", "Thu. and Sun. complete the sequence."),
        ("If the 3 clever Brahmins spent a fortnight boasting about their skills, how many days did they boast?", "14 days (2 weeks)", "7 days", "30 days", "3 days", "A", "A fortnight is 14 days."),
        ("Spot the error in the calendar sequence: 'Aug, Sep, Nov, Oct, Dec'", "November and October are in wrong order.", "September is in wrong position.", "December should be first.", "No error.", "A", "October comes before November (Aug, Sep, Oct, Nov, Dec)."),
        ("The fourth Brahmin returned to ashram on **31st October**. What date was the next day?", "1st November", "32nd October", "30th October", "1st December", "A", "October has 31 days, so the next day is 1st November."),
        ("If yesterday was two days before Tuesday, what day is tomorrow?", "Tuesday", "Monday", "Wednesday", "Sunday", "A", "Two days before Tuesday = Sunday (yesterday). Today = Monday. Tomorrow = Tuesday."),
        ("Calculate: How many days are there in total during **July** and **August** combined?", "62 days (31 + 31)", "60 days", "61 days", "59 days", "A", "Both July (31) and August (31) have 31 days. 31 + 31 = 62 days."),
        ("HOTS Reasoning: Why do we write 'a.m.' for morning hours and 'p.m.' for afternoon/evening hours?", "'a.m.' stands for Ante Meridiem (before noon); 'p.m.' stands for Post Meridiem (after noon).", "Because a.m. means after morning.", "Because p.m. means past midnight.", "Because sage created it.", "A", "a.m. = Ante Meridiem; p.m. = Post Meridiem."),
        ("Identify the correct statement about leap year in relation to months:", "Leap year adds 1 extra day to February, making it 29 days.", "Leap year adds 1 day to March.", "Leap year removes 1 day from December.", "Leap year occurs every 3 years.", "A", "February has 29 days in a leap year."),
        ("The three Brahmins rested for 3 hours. How many minutes is 3 hours?", "180 minutes", "120 minutes", "300 minutes", "60 minutes", "A", "3 hours x 60 minutes = 180 minutes."),
        ("Which month pair both have 30 days and are separated by July and August?", "June and September", "April and May", "September and October", "January and February", "A", "June (30 days) and September (30 days) are separated by July and August (31 days each).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH02_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Logic & Mathematical Time Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Calendar & Time Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 4. Action Verbs Identification (50 Qs)
# ---------------------------------------------------------------------------
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification — Chapter 02: Four Brahmins\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_verbs = [
        ("The first Brahmin **reconstructed** the skeleton.", "reconstructed", "first", "Brahmin", "skeleton", "A", "'reconstructed' is the action verb."),
        ("The second Brahmin **restored** organs and skin.", "restored", "second", "organs", "skin", "A", "'restored' is the action verb."),
        ("The third Brahmin **chanted** a magic spell.", "chanted", "third", "magic", "spell", "A", "'chanted' is the action verb."),
        ("The fourth Brahmin **climbed** up a tree.", "climbed", "fourth", "up", "tree", "A", "'climbed' is the physical action verb."),
        ("The hungry lion **killed** the three friends.", "killed", "hungry", "lion", "three", "A", "'killed' is the action verb."),
        ("The lion **ate** all three Brahmins.", "ate", "lion", "all", "Brahmins", "A", "'ate' is the action verb."),
        ("The fourth Brahmin **warned** his companions.", "warned", "fourth", "his", "companions", "A", "'warned' is the action verb."),
        ("The disciples **learned** magic from the sage.", "learned", "disciples", "magic", "sage", "A", "'learned' is the mental action verb."),
        ("The Brahmins **walked** through the forest all day.", "walked", "Brahmins", "forest", "day", "A", "'walked' is the action verb."),
        ("They **rested** under a shady banyan tree.", "rested", "they", "under", "banyan", "A", "'rested' is the action verb."),
        ("The simpleton **offered** to cook and clean.", "offered", "simpleton", "cook", "clean", "A", "'offered' is the action verb."),
        ("The three friends **ignored** the fourth Brahmin.", "ignored", "three", "friends", "fourth", "A", "'ignored' is the action verb."),
        ("The fourth Brahmin **pleaded** with his friends.", "pleaded", "fourth", "friends", "with", "A", "'pleaded' is the action verb."),
        ("The lion **roared** loudly in the forest.", "roared", "lion", "loudly", "forest", "A", "'roared' is the action verb."),
        ("The fourth Brahmin **got** down from the tree.", "got", "fourth", "down", "tree", "A", "'got' (got down) is the action verb."),
        ("The surviving Brahmin **returned** to the ashram.", "returned", "surviving", "Brahmin", "ashram", "A", "'returned' is the action verb."),
        ("He **grieved** for his lost friends.", "grieved", "he", "for", "friends", "A", "'grieved' is the emotional action verb."),
        ("The sage **taught** valuable lessons to all.", "taught", "sage", "valuable", "lessons", "A", "'taught' is the action verb.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_verbs, start=1):
        qid = f"BK02_CH02_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in this sentence from or related to Chapter 02:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Action Verb Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Which word from the sentence is an **action verb**? 'The fourth Brahmin **silently** **climbed** a **tall** **tree**.'", "climbed", "silently", "tall", "tree", "A", "'climbed' shows physical action; 'silently' is adverb, 'tall' is adjective, 'tree' is noun."),
        ("Identify BOTH action verbs in: 'The lion **woke** up and **attacked** the Brahmins.'", "woke, attacked", "lion, up", "Brahmins, attacked", "woke, Brahmins", "A", "'woke' and 'attacked' are both action verbs."),
        ("What is the past tense action verb of 'bring' as used in the story ('bring back to life')?", "brought", "bringed", "bringing", "brings", "A", "Past tense of bring is brought."),
        ("Choose the sentence where the underlined word is used as an ACTION VERB:", "The lion will **leap** upon them.", "The lion made a huge **leap**.", "That was a high **leap**.", "The **leap** was dangerous.", "A", "In (A), 'leap' acts as the main action verb."),
        ("Find the action verb in: 'The first Brahmin put the bones together.'", "put", "first", "bones", "together", "A", "'put' is the action verb."),
        ("Which sentence contains NO physical action verb?", "The three Brahmins were arrogant.", "The fourth Brahmin climbed a tree.", "The lion devoured the men.", "They walked to the town.", "A", "'The three Brahmins were arrogant' contains linking verb 'were', but no physical action verb."),
        ("Change the action verb 'sing' to past tense: 'The birds (sing) in the morning.'", "sang", "singed", "singing", "sings", "A", "Past tense of sing is sang."),
        ("Identify the action verb: 'The fourth Brahmin warned his friends but they ignored him.'", "warned, ignored", "fourth, friends", "they, warned", "ignored, friends", "A", "'warned' and 'ignored' are action verbs."),
        ("Select the action verb that completes the sentence: 'The sage ____ his disciples in the ashram.'", "instructed", "wise", "ashram", "clever", "A", "'instructed' is an action verb."),
        ("Which word is an action verb? (bones, lion, revived, skeleton)", "revived", "bones", "lion", "skeleton", "A", "'revived' is an action verb; others are nouns."),
        ("What action did the fourth Brahmin perform to stay safe?", "climbed", "simpleton", "bones", "lion", "A", "He climbed a tree (action verb)."),
        ("Identify the action verb in: 'Dilip thought about the consequences.'", "thought", "Dilip", "about", "consequences", "A", "'thought' is a mental action verb."),
        ("Choose the correct action verb: 'The starving lion ____ the three men.'", "devoured", "devourable", "devouring", "teeth", "A", "'devoured' is the action verb."),
        ("Identify the action verb in: 'The sage wept for the dead disciples.'", "wept", "sage", "dead", "disciples", "A", "'wept' is the action verb."),
        ("Which of these words is NOT an action verb? (run, shout, golden, chant)", "golden", "run", "shout", "chant", "A", "'golden' is an adjective; others are action verbs."),
        ("Identify the action verb in: 'The third Brahmin spoke a powerful spell.'", "spoke", "third", "powerful", "spell", "A", "'spoke' is the action verb."),
        ("Fill in the blank with an appropriate action verb: 'The lion ____ out of the bushes.'", "pounced", "big", "yellow", "tree", "A", "'pounced' is an action verb."),
        ("What action verb completes the sentence? 'The fourth Brahmin ____ his life through wisdom.'", "saved", "wise", "tree", "lion", "A", "'saved' is an action verb.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH02_CAT04_Q{idx:02d}"
        qtxt = f"Action Verb Grammar Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Action Verb Context & Tense", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence: 'The arrogant third Brahmin foolishly chanted a spell to revive the dead lion.' How many total ACTION VERBS are present?", "2 action verbs ('chanted', 'revive')", "1 action verb", "3 action verbs", "0 action verbs", "A", "'chanted' and 'revive' are action verbs; 'arrogant', 'foolishly', 'dead' are adjectives/adverbs."),
        ("Categorize the verbs: In 'The fourth Brahmin **was** sensible, so he **climbed** the tree', classify 'was' and 'climbed'.", "'was' is a linking verb; 'climbed' is an action verb.", "Both are action verbs.", "Both are linking verbs.", "'was' is action; 'climbed' is linking.", "A", "'was' links state of being; 'climbed' shows physical action."),
        ("Replace the weak verb with a strong action verb: 'The lion **went fast** towards the Brahmins.'", "The lion **charged** towards the Brahmins.", "The lion **was near** the Brahmins.", "The lion **walked slow**.", "The lion **looked at** the Brahmins.", "A", "'charged' is a much stronger, vivid action verb."),
        ("Identify the sentence with THREE distinct action verbs:", "The fourth Brahmin **warned** his friends, **climbed** a tree, and **watched** in fear.", "The three Brahmins were clever, proud, and foolish.", "The lion devoured the three Brahmins.", "The sage lived in a quiet ashram.", "A", "warned, climbed, watched are 3 distinct action verbs."),
        ("Differentiate verb types: Which underlined word is an ACTION verb?", "The fourth Brahmin **objected** to the spell.", "The fourth Brahmin was **smart**.", "The lion was **hungry**.", "The sage was **wise**.", "A", "'objected' is an action verb."),
        ("Spot the incorrect verb tense: 'The third Brahmin **bring** the lion to life yesterday.' Correct it:", "'bring' should be 'brought' (past action verb).", "'bring' should be 'bringing'.", "'bring' should be 'brings'.", "'bring' should be 'will bring'.", "A", "Past time indicator 'yesterday' requires past tense action verb 'brought'."),
        ("Form an action chain: Rearrange the story action verbs in correct order of occurrence: (chanted, assembled, climbed, devoured)", "assembled -> chanted -> climbed -> devoured", "devoured -> climbed -> chanted -> assembled", "climbed -> assembled -> chanted -> devoured", "chanted -> assembled -> devoured -> climbed", "A", "First assembled bones, then chanted spell, fourth Brahmin climbed tree, lion devoured them."),
        ("Identify the verb error in dialogue: Third Brahmin said, 'I have **make** a living lion!'", "'make' is incorrect; the past participle form is 'made' ('have made').", "'make' should be 'making'.", "'make' should be 'makes'.", "No error.", "A", "Perfect tense requires past participle 'made'."),
        ("Analyze this sentence: 'The fourth Brahmin **pleaded** with his friends to stop.' What type of action verb is 'pleaded'?", "Vocal/Speech action verb", "Physical movement verb", "Linking verb", "State of being verb", "A", "'pleaded' is an action verb of speech/feeling."),
        ("Which sentence uses action verbs to show cause and effect?", "The third Brahmin **revived** the lion, and it **devoured** them.", "The three Brahmins were clever and proud.", "The lion had sharp teeth and claws.", "The ashram was far from the town.", "A", "'revived' (cause action) -> 'devoured' (effect action)."),
        ("Spot the missing action verb: 'The lion ____ from its sleep and ____ the men.'", "awoke, attacked", "big, hungry", "was, was", "quick, slow", "A", "'awoke' and 'attacked' complete sentence with vivid actions."),
        ("HOTS Reasoning: Why is 'warned' in 'He warned his friends' considered a COMMUNICATIVE action verb?", "Because it describes the active transmission of a cautionary message.", "Because warning requires a tree.", "Because lion was hungry.", "Because it is a noun.", "A", "Descriptive speech action verb conveying caution."),
        ("Transform the action verb to future tense: 'The lion **attacks** the disciples.'", "The lion **will attack** the disciples.", "The lion **attacked** the disciples.", "The lion **is attacking** the disciples.", "The lion **attack** the disciples.", "A", "'will attack' expresses future action."),
        ("Identify the sentence where the action verb matches the plural subject:", "The disciples **learn** magic.", "The disciples **learns** magic.", "The disciple **learn** magic.", "The disciples **is learning** magic.", "A", "Plural subject 'disciples' takes base verb 'learn' in simple present.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH02_CAT04_Q{idx:02d}"
        qtxt = f"Higher Order Action Verb Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Action Verb Classification & Tense Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 5. Punctuation Marks (50 Qs)
# ---------------------------------------------------------------------------
def build_punctuation_marks():
    header = "# Category 5: Punctuation Marks & Capitalization — Chapter 02: Four Brahmins\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_punct = [
        ("What punctuation mark should be placed at the end of: 'The sage had four disciples__'", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "Comma (,)", "A", "A statement ends with a full stop."),
        ("Which mark is used at the end of an asking sentence: 'Why are you bringing the lion back to life__'", "Question mark (?)", "Full stop (.)", "Comma (,)", "Exclamation mark (!)", "A", "A question ends with a question mark."),
        ("Which letter should ALWAYS be capitalized in a title or proper noun like 'Panchatantra'?", "The first letter (e.g., Panchatantra)", "The last letter", "All letters", "No letters", "A", "First letter of proper nouns must be capitalized."),
        ("Identify the punctuation mark used to separate items in a list: 'The lion had bones__ skin__ and organs.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Hyphen (-)", "A", "Commas separate items in a list."),
        ("Which punctuation mark shows sudden danger or warning: 'Stop! The lion will eat us__'", "Exclamation mark (!)", "Full stop (.)", "Comma (,)", "Question mark (?)", "A", "Exclamation marks express intense warning."),
        ("Select the proper noun that MUST start with a capital letter:", "Brahmin", "lion", "tree", "bones", "A", "'Brahmin' as a caste/group title starts with capital 'B'."),
        ("Which of the following is the symbol for a **full stop**?", ".", "?", "!", ",", "A", "Period/full stop is '.'"),
        ("Which of the following is the symbol for a **question mark**?", "?", ".", "!", ",", "A", "Question mark is '?'"),
        ("Which of the following is the symbol for an **exclamation mark**?", "!", "?", ".", ",", "A", "Exclamation mark is '!'"),
        ("Which word in this sentence should start with a CAPITAL letter? 'the fourth Brahmin climbed a tree.'", "the -> The", "fourth -> Fourth", "tree -> Tree", "climbed -> Climbed", "A", "The first word of a sentence must start with a capital letter."),
        ("What punctuation mark goes in the box? 'The lion attacked the three Brahmins [ ]'", "Full stop (.)", "Question mark (?)", "Comma (,)", "Exclamation mark (!)", "A", "Full stop ends the statement."),
        ("Which name is capitalized correctly?", "Panchatantra", "panchatantra", "pAnchaTantra", "panchatantrA", "A", "Capital 'P' for proper name Panchatantra."),
        ("What mark goes after a speaker tag: 'The fourth Brahmin said__ \"Do not revive the lion.\"'", "Comma (,)", "Question mark (?)", "Full stop (.)", "Exclamation mark (!)", "A", "Comma follows dialogue speaker tags."),
        ("Identify the correct capital letter for the pronoun 'I': 'he said, \"i will bring it to life.\"'", "I", "i", "i'm", "I'm", "A", "Standalone pronoun 'I' is always capitalized."),
        ("Which option shows a sentence ending correctly?", "The lion devoured them all.", "The lion devoured them all?", "The lion devoured them all,", "The lion devoured them all;", "A", "Full stop at end of simple statement."),
        ("What mark is used in possessives like 'the **sage's** ashram'?", "Apostrophe (')", "Comma (,)", "Full stop (.)", "Hyphen (-)", "A", "Apostrophe indicates possession."),
        ("Which book title is capitalized correctly?", "Four Brahmins", "four brahmins", "Four brahmins", "FOUR BRAHMINS", "A", "Major words in titles are capitalized."),
        ("What punctuation mark is used around spoken dialogue: '___Leave the bones alone!___'", "Quotation marks / Speech marks ( \" \" )", "Parentheses ( )", "Full stops ( . . )", "Commas ( , , )", "A", "Speech marks enclose spoken dialogue.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_punct, start=1):
        qid = f"BK02_CH02_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Punctuation & Capitalization Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Identify the sentence with CORRECT capitalization and punctuation:", "The four Brahmins walked towards the town on Tuesday.", "the four brahmins walked towards the town on tuesday.", "The four brahmins walked towards the town on tuesday?", "the Four Brahmins Walked Towards The Town On Tuesday.", "A", "The (start), Brahmins (proper), Tuesday (day) capitalized; ends with period."),
        ("Which sentence is punctuated as a CORRECT question?", "Why did the third Brahmin revive the lion?", "Why did the third Brahmin revive the lion.", "Why did the third Brahmin revive the lion!", "Why did the third Brahmin revive the lion,", "A", "Question starting with 'Why' ends with question mark ?"),
        ("Spot the capitalization mistake in: 'the sage lived in an Ashram near the Forest.'", "'the' should be capitalized ('The'); 'Ashram' and 'Forest' should be lowercase.", "'Forest' should be capitalized only.", "'Ashram' should be capitalized.", "No mistake.", "A", "Sentence start 'The' capitalized; common nouns ashram and forest lowercase here."),
        ("Choose the correctly punctuated dialogue sentence:", "\"Leave the dead alone,\" warned the fourth Brahmin.", "leave the dead alone warned the fourth Brahmin.", "\"Leave the dead alone\" warned the fourth Brahmin", "Leave the dead alone, warned the fourth Brahmin.", "A", "Quotation marks around dialogue, comma inside quote, capital L."),
        ("Identify where a COMMA is missing: 'The lion had skeleton flesh and skin.'", "Between 'skeleton' and 'flesh' ('skeleton, flesh')", "After 'The'", "After 'skin'", "No comma needed", "A", "Commas separate items in list: 'skeleton, flesh and skin'."),
        ("Which sentence uses the apostrophe correctly for possession?", "This is the sage's ashram.", "This is the sages' ashram.", "This is the sages ashram.", "This is the sage's' ashram.", "A", "sage's indicates possession by the sage."),
        ("Select the sentence with CORRECT punctuation for an exclamatory warning:", "Beware! The lion is coming to life!", "Beware? The lion is coming to life?", "Beware. The lion is coming to life.", "Beware, The lion is coming to life,", "A", "Exclamatory warning uses exclamation mark !"),
        ("Which contraction is written correctly for 'cannot'?", "can't", "ca'nt", "cant'", "c'ant", "A", "can't is standard contraction."),
        ("Find the sentence with NO capitalization errors:", "The Panchatantra is an ancient Indian book of fables.", "the panchatantra is an ancient indian book of fables.", "The Panchatantra Is An Ancient Indian Book Of Fables.", "the Panchatantra is an Ancient Indian book of Fables.", "A", "'Panchatantra' and 'Indian' capitalized as proper nouns/adjectives."),
        ("What punctuation mark belongs in the blank? 'The fourth Brahmin shouted, \"Look out__ The lion is awake!\"'", "!", ".", "?", ",", "A", "Exclamation mark ! expresses urgent warning."),
        ("Choose the correct form for 'would not':", "wouldn't", "would'nt", "wouldnt'", "w'ouldnt", "A", "wouldn't is the standard contraction."),
        ("Identify the punctuation error: 'The third Brahmin sang a spell, the lion woke up.'", "Comma splice between two independent clauses (should be full stop or 'and').", "Missing question mark.", "Missing capital letters.", "No error.", "A", "Two complete sentences separated only by comma."),
        ("Select the sentence with proper use of capital letters for names and titles:", "Sage Vasishta taught the four Brahmins.", "sage vasishta taught the four brahmins.", "Sage vasishta taught the Four brahmins.", "sage Vasishta taught the four Brahmins.", "A", "Title 'Sage' and name 'Vasishta' both capitalized."),
        ("Which sentence correctly uses an apostrophe for possessive plural?", "The three Brahmins' foolishness led to their death.", "The three Brahmin's foolishness led to their death.", "The three Brahmins foolishness led to their death.", "The three Brahmins's foolishness led to their death.", "A", "Plural ending in -s takes apostrophe after the s (Brahmins')."),
        ("Identify the correct punctuation for a list of items: 'The lion possessed ____'", "sharp teeth, long claws, and strong muscles.", "sharp teeth long claws and strong muscles.", "sharp teeth; long claws; and strong muscles.", "sharp teeth: long claws: and strong muscles.", "A", "Commas separate items in list."),
        ("Choose the sentence that correctly asks a question about the story:", "How did the fourth Brahmin save his life?", "How did the fourth Brahmin save his life.", "How did the fourth Brahmin save his life!", "how did the fourth Brahmin save his life.", "A", "Capital H, ends with question mark ?"),
        ("Fix the sentence: 'where is the lions skeleton'", "Where is the lion's skeleton?", "Where is the lions skeleton.", "where is the Lion's skeleton!", "Where is the Lions' skeleton?", "A", "Capital W, possessive lion's, ends with ?"),
        ("Which of these sentences is punctuated PERFECTLY?", "The fourth Brahmin pleaded, \"Please stop!\"", "The fourth Brahmin pleaded \"please stop!\"", "the fourth Brahmin pleaded, \"Please stop!\"", "The fourth Brahmin pleaded, \"Please stop.\"", "A", "Capital T, comma after pleaded, speech marks around warning with ! inside.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH02_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Context Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Punctuation Application & Dialogue Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze and count ALL capitalization and punctuation errors in: 'on wednesday the 3 brahmins went to town and said, we have magic powers'", "5 errors (on->On, wednesday->Wednesday, 3->three, missing quotes & period)", "2 errors", "3 errors", "7 errors", "A", "Starts sentence, day name, spelling out numbers in text, quotation marks & period."),
        ("Correct the entire dialogue paragraph: 'the fourth brahmin warned don't revive the lion the third brahmin replied only fools fear knowledge'", "\"Don't revive the lion!\" warned the fourth Brahmin. The third Brahmin replied, \"Only fools fear knowledge.\"", "the fourth brahmin warned \"don't revive the lion\" the third brahmin replied \"only fools fear knowledge.\"", "The fourth Brahmin warned, Don't revive the lion. The third Brahmin replied, Only fools fear knowledge.", "\"Don't revive the lion?\" Warned the fourth Brahmin. The third Brahmin replied \"Only fools fear knowledge?\"", "A", "Full proper quotation, dialogue tags, capitalization, and terminal punctuation."),
        ("Distinguish between singular possessive and plural possessive: 'the **Brahmin's** book' vs 'the **Brahmins'** book'", "First refers to one Brahmin's book; second refers to the book of multiple Brahmins.", "Both refer to one Brahmin.", "Both refer to multiple Brahmins.", "First is plural; second is singular.", "A", "Brahmin's = singular; Brahmins' = plural possessive."),
        ("Spot the subtle punctuation flaw in this dialogue: '\"I will restore its skin,\" Said the second Brahmin.'", "'Said' should be lowercase 'said' because it continues the dialogue tag outside quotation marks.", "'I' should be lowercase.", "Commas should be outside quotes.", "No flaw.", "A", "Dialogue tags following quotes start with lowercase unless proper nouns."),
        ("Which sentence correctly uses punctuation to show contrast?", "They had knowledge, but they lacked common sense.", "They had knowledge but, they lacked common sense.", "They had knowledge but they lacked common sense!", "They had knowledge; but they lacked common sense?", "A", "Comma before coordinating conjunction 'but' joining two independent clauses."),
        ("Reconstruct with perfect punctuation: 'the sage warned his disciples on monday 12th march at the ashram'", "The sage warned his disciples on Monday, 12th March, at the ashram.", "the sage warned his disciples on monday, 12th march at the ashram.", "The sage warned his disciples on Monday 12th March at the ashram", "The sage warned his disciples on monday 12th march at ashram.", "A", "The, Monday, 12th March set off by commas, ends with period."),
        ("Identify why exclamation mark is necessary here: '\"Stop! It will devour us all!\"'", "Because the fourth Brahmin is shouting in extreme panic and terror.", "Because lion is sleeping.", "Because tree is tall.", "Because sentence is long.", "A", "Exclamation mark communicates intense urgency and terror."),
        ("Choose the correctly punctuated sentence containing an appositive phrase:", "The fourth Brahmin, a simpleton with common sense, saved his own life.", "The fourth Brahmin a simpleton with common sense saved his own life.", "The fourth Brahmin, a simpleton with common sense saved his own life.", "The fourth Brahmin a simpleton with common sense, saved his own life.", "A", "Appositive phrase 'a simpleton with common sense' is set off by commas."),
        ("Analyze the use of hyphen in: 'The twenty-four year old disciple was foolish.'", "Hyphen joins compound numbers (twenty-four).", "Hyphen replaces comma.", "Hyphen indicates question.", "Hyphen is an apostrophe.", "A", "Compound numbers from twenty-one to ninety-nine take hyphens."),
        ("Identify the correct sentence with direct speech quote within text:", "The third Brahmin boasted, \"I will bring it to life,\" which was a fatal mistake.", "The third Brahmin boasted \"I will bring it to life\" which was a fatal mistake.", "The third Brahmin boasted, 'I will bring it to life,' which was a fatal mistake.", "The third Brahmin boasted: \"I will bring it to life\" which was a fatal mistake.", "A", "Comma before quote, double quotation marks around direct speech, comma inside quote."),
        ("Spot the missing apostrophe: 'The lions roaring scared the three friends.'", "Missing apostrophe in 'lion's' -> 'The lion's roaring'", "Missing apostrophe in 'friends''", "Missing apostrophe in 'scared''", "No apostrophe needed", "A", "'lion's roaring' requires possessive apostrophe."),
        ("HOTS Reasoning: Why does putting a comma in different places change meaning? Compare: 'The sage said the Brahmin was foolish.' vs '\"The sage,\" said the Brahmin, \"was foolish.\"'", "In the first, speaker says sage called Brahmin foolish; in the second, Brahmin says sage was foolish.", "Both mean the exact same thing.", "The first is a question.", "Commas do not affect meaning.", "A", "Punctuation alters who speaks and who is being described."),
        ("Correct all 4 errors in: 'what have you done asked the sage'", "\"What have you done?\" asked the sage.", "what have you done? asked the sage.", "\"What have you done.\" asked the sage.", "\"what have you done?\" Asked the sage.", "A", "Quotation marks, capital W, question mark inside quote, period at end."),
        ("Identify the rule for capitalizing titles of respect like 'Sage' or 'Guru':", "Titles used before proper names or as proper names are capitalized.", "Titles are never capitalized.", "Titles are capitalized only at end of sentence.", "Titles must be written in ALL CAPS.", "A", "Titles used before proper names take capital initial.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH02_CAT05_Q{idx:02d}"
        qtxt = f"Higher Order Punctuation Analysis & Dialogue Formatting:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Punctuation & Dialogue Editing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 6. Phonics & Vowel Digraphs (50 Qs)
# ---------------------------------------------------------------------------
def build_phonics_digraphs():
    header = "# Category 6: Phonics & Vowel Digraphs — Chapter 02: Four Brahmins\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_phonics = [
        ("Which vowel digraph is present in the word **'learnt'** (in Chapter 02)?", "ea", "ee", "ai", "ou", "A", "'ea' is the vowel digraph in learnt."),
        ("Identify the vowel digraph in the word **'tree'**:", "ee", "ea", "oa", "ui", "A", "'ee' forms the long /e/ vowel sound in tree."),
        ("Which word from the story contains the **'ou'** vowel digraph?", "four", "sage", "lion", "bone", "A", "'four' contains the 'ou' digraph."),
        ("Identify the vowel digraph in the word **'dead'**:", "ea", "ee", "ow", "oo", "A", "'ea' forms short /e/ sound in dead."),
        ("Which vowel digraph appears in the word **'paid'**?", "ai", "ay", "ea", "oa", "A", "'ai' makes long /a/ sound in paid."),
        ("Find the word with the **'oo'** vowel digraph: 'The lion was a fool to attack.'", "fool", "lion", "was", "attack", "A", "'fool' contains 'oo' digraph."),
        ("Which word from the story rhymes with **'tree'**?", "free", "try", "true", "tray", "A", "'free' rhymes with 'tree'."),
        ("Which word from the story rhymes with **'bone'**?", "stone", "ban", "bound", "burn", "A", "'stone' rhymes with 'bone'."),
        ("Identify the vowel digraph in the word **'roared'**:", "oa", "ou", "ow", "oo", "A", "'oa' makes long /o/ sound in roared."),
        ("Which word from the story rhymes with **'life'**?", "wife", "lift", "live", "leaf", "A", "'wife' rhymes with 'life'."),
        ("Identify the vowel digraph in **'grieving'**:", "ie", "ea", "ee", "ia", "A", "'ie' is the vowel digraph in grieving."),
        ("Which word from Chapter 02 has the **'ea'** digraph making a long /e/ sound?", "eaten", "dead", "head", "read (past)", "A", "'eaten' has 'ea' making long /e/ sound."),
        ("Which word rhymes with **'day'**?", "away", "die", "due", "door", "A", "'away' rhymes with 'day'."),
        ("Identify the silent letter in **'climb'** (as in 'climbed a tree'):", "b", "m", "c", "l", "A", "Final 'b' after 'm' is silent in climb."),
        ("Which word from the story has long /i/ sound spelled with **'igh'**?", "brightest", "bought", "bones", "body", "A", "'igh' in brightest makes long /i/ sound."),
        ("Find the word with **'ou'** digraph: 'They found the lion's skeleton.'", "found", "skeleton", "lion", "they", "A", "'found' contains 'ou' digraph."),
        ("Which word rhymes with **'sage'**?", "page", "sag", "song", "see", "A", "'page' rhymes with 'sage'."),
        ("Identify the silent letter in the word **'know'** (as in 'bookish knowledge'):", "k", "n", "o", "w", "A", "Initial 'k' before 'n' is silent.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_phonics, start=1):
        qid = f"BK02_CH02_CAT06_Q{idx:02d}"
        qtxt = f"Phonics & Vowel Digraph Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Vowel Digraphs & Rhyming Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Compare the **'ea'** digraph sound in **'eaten'** and **'dead'**. What is the difference?", "'eaten' has long /e/ sound; 'dead' has short /e/ sound.", "Both have short /e/ sound.", "Both have long /a/ sound.", "'eaten' has short /e/; 'dead' has long /e/.", "A", "'ea' can make long /e/ (eaten) or short /e/ (dead)."),
        ("Select the word pair from Chapter 02 that has the SAME vowel digraph sound:", "tree - see", "four - dead", "learnt - roar", "bone - tree", "A", "'tree' and 'see' both have 'ee' long /e/ sound."),
        ("Which word contains a SILENT letter? (climb, lion, tree, bone)", "climb", "lion", "tree", "bone", "A", "'climb' has silent 'b' at the end."),
        ("Identify the odd one out based on vowel sound: (tree, free, see, dead)", "dead", "tree", "free", "see", "A", "'dead' has short /e/ sound; others have long /e/ sound."),
        ("Which digraph completes the word for disciple's feeling? 'gr__ving'", "ie", "ea", "ee", "ou", "A", "'grieving' uses 'ie' digraph."),
        ("Group these story words by digraph: **found**, **out**, **shouted**. What digraph do they all share?", "ou", "ow", "oo", "oi", "A", "All share 'ou' making /ow/ diphthong sound."),
        ("Find the word with consonant digraph **'th'** from the story: 'The **fourth** Brahmin was smart.'", "fourth", "was", "smart", "Brahmin", "A", "'fourth' contains unvoiced 'th' consonant digraph."),
        ("Which of these words has the **'oa'** vowel digraph? (roared, boasted, coat, all of these)", "all of these", "roared", "boasted", "coat", "A", "roared, boasted, coat all share 'oa' long /o/ sound."),
        ("Identify the vowel digraph in **'beauty'** (related to majestic lion):", "eau", "ea", "au", "ty", "A", "'eau' is the trigraph/digraph forming /yoo/ sound."),
        ("Which word from the story has a silent **'k'**? (knowledge, knee, knock, all of these)", "all of these", "knowledge", "knee", "knock", "A", "knowledge, knee, knock all have silent initial 'k'."),
        ("Select the word that rhymes with **'bone'** and fits sentence: 'The lion turned into ____.'", "stone", "cone", "zone", "lone", "A", "'stone' rhymes with 'bone'."),
        ("Identify the digraph in **'bleeding'**:", "ee", "ea", "ai", "oa", "A", "'ee' makes long /e/ sound."),
        ("Which word has the short /u/ sound made by **'ou'**? (touch, house, out, shout)", "touch", "house", "out", "shout", "A", "'touch' has short /u/ sound with 'ou'."),
        ("Find the R-controlled vowel sound in: 'The Brahmins lived in an **ashram**.'", "ar sound", "ea", "ou", "ai", "A", "R-controlled vowel in ashram."),
        ("Which word contains the **'oi'** diphthong/digraph? (voice, point, choice, all of these)", "all of these", "voice", "point", "choice", "A", "voice, point, choice all contain 'oi'."),
        ("Identify the soft **'c'** sound in Chapter 02 vocabulary: (disciple, skeleton, cook, clean)", "disciple", "skeleton", "cook", "clean", "A", "'disciple' has soft /s/ sound for 'c'; others have hard /k/ sound."),
        ("Which word has a soft **'g'** sound? (sage, magic, danger, all of these)", "all of these", "sage", "magic", "danger", "A", "sage, magic, danger all have soft /j/ sound for 'g'."),
        ("Choose the correct spelling with **'ea'** digraph for gaining knowledge:", "learned / learnt", "learnd", "learnted", "lerned", "A", "learned / learnt is standard spelling.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH02_CAT06_Q{idx:02d}"
        qtxt = f"Phonics Analysis & Sound Pattern Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Phonic Rules & Sound Discrimination", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the phonics rule: Why does 'g' in **'sage'** sound like /j/, but 'g' in **'good'** sounds like /g/?", "Because 'g' followed by 'e', 'i', or 'y' makes soft /j/ sound; before 'o', 'a', 'u' it makes hard /g/ sound.", "Because sage is a person.", "Because good is an adjective.", "There is no rule.", "A", "Soft 'g' rule: g + e, i, y = /j/ sound."),
        ("Categorize the 'ea' digraphs into long /e/ vs short /e/: (eaten, dead, head, lead [metal], read [present])", "Long /e/: eaten, read [present]; Short /e/: dead, head, lead [metal]", "All are long /e/.", "All are short /e/.", "Long /e/: dead; Short /e/: eaten", "A", "eaten, read (present) make long /e/; dead, head, lead (metal) make short /e/."),
        ("Identify the word pair where SILENT letters exist in BOTH words:", "climb - knowledge", "bone - lion", "tree - sage", "forest - river", "A", "'climb' (silent b) and 'knowledge' (silent k)."),
        ("Decode the phonics blend: Which word contains a 3-letter consonant blend at the start?", "skeleton", "tree", "flew", "climbed", "A", "'sk' / 'skl' / 'str' / 'scr' blend types."),
        ("Examine the hard vs soft 'c' rule: Why is 'c' soft in **'disciple'** but hard in **'clever'**?", "'c' followed by 'i', 'e', 'y' makes soft /s/ sound (disciple); 'c' before 'l' or 'a','o','u' makes hard /k/ sound (clever).", "Because disciple is young.", "Because clever describes 3 Brahmins.", "There is no rule.", "A", "Soft 'c' rule: c + i, e, y = /s/ sound."),
        ("Find the word with BOTH a vowel digraph AND a silent letter:", "roared", "bone", "lion", "tree", "A", "'roared' has 'oa' digraph and silent 'e' in -ed."),
        ("Differentiate diphthongs: Which pair produces the /ow/ sound as in **'out'**?", "out - found", "voice - coin", "paid - day", "boat - coat", "A", "'out' and 'found' share /ow/ diphthong sound."),
        ("Analyze homophones: 'The lion ate the **whole** / **hole** animal.' Which word means entire?", "whole", "hole", "hoal", "whoal", "A", "'whole' means entire/complete; 'hole' is an opening."),
        ("Identify the phonic pattern in **'skeleton'**: What vowel sound does the first 'e' make?", "Short /e/ sound", "Long /e/ sound", "Silent sound", "Long /a/ sound", "A", "'skel-' makes short /e/ sound."),
        ("Sort by ending sound: Which word ends with the /z/ sound? (bones, trees, disciples, all of these)", "all of these", "bones", "trees", "disciples", "A", "Plurals ending in voiced consonants/vowels take /z/ ending sound."),
        ("Spot the word where 'b' is SILENT: (climb, thumb, lamb, all of these)", "all of these", "climb", "thumb", "lamb", "A", "'b' is silent after 'm' at the end of root words."),
        ("HOTS Reasoning: Why do 'know' and 'no' sound identical but have different spellings and meanings?", "They are homophones (same sound, different spelling/meaning).", "They are synonyms.", "They are antonyms.", "They are plurals.", "A", "Homophones share pronunciation but differ in origin/spelling/meaning."),
        ("Identify the compound word from story concepts containing two simple words:", "simpleton / bonesetter", "Brahmin", "Panchatantra", "ashram", "A", "bonesetter = bone + setter."),
        ("Determine the syllable count and stress: How many syllables are in **'consequences'**?", "4 syllables (con-se-quen-ces)", "2 syllables", "3 syllables", "5 syllables", "A", "con-se-quen-ces has 4 distinct syllables.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH02_CAT06_Q{idx:02d}"
        qtxt = f"Higher Order Phonics & Orthographic Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Phonetic Rules & Homophone Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 7. Question Words & Interrogatives (50 Qs)
# ---------------------------------------------------------------------------
def build_question_words():
    header = "# Category 7: Question Words & Interrogatives — Chapter 02: Four Brahmins\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_qwords = [
        ("___ had four disciples living at his ashram?", "Who", "What", "Where", "Why", "A", "'Who' asks about a person (the sage)."),
        ("___ did the three clever Brahmins learn at the ashram?", "What", "Who", "Where", "When", "A", "'What' asks about a thing/subject (magical skills)."),
        ("___ did the three Brahmins decide to go to earn money?", "Where", "Who", "What", "Why", "A", "'Where' asks about location (to town)."),
        ("___ was considered a simpleton among the four disciples?", "Who", "What", "Where", "Why", "A", "'Who' asks about identity (fourth Brahmin)."),
        ("___ did the fourth Brahmin offer to do if he joined them?", "What", "Where", "Why", "When", "A", "'What' asks about action (cook and clean)."),
        ("___ did the Brahmins find under the tree?", "What", "Who", "Where", "Why", "A", "'What' asks about object (bones of a lion)."),
        ("___ reconstructed the skeleton of the lion?", "Which Brahmin / Who", "What", "Where", "Why", "A", "'Who' asks about subject person (first Brahmin)."),
        ("___ added organs, flesh, and skin to the skeleton?", "Who", "What", "Where", "When", "A", "'Who' asks about person (second Brahmin)."),
        ("___ brought the dead lion back to life?", "Who", "What", "Where", "Why", "A", "'Who' asks about person (third Brahmin)."),
        ("___ did the fourth Brahmin climb a tree?", "Why", "Who", "Where", "What", "A", "'Why' asks for reason (to save his life)."),
        ("___ did the fourth Brahmin do when he saw the lion waking up?", "What", "Who", "Where", "Why", "A", "'What' asks about action."),
        ("___ animal was brought back to life by magic?", "Which", "Who", "Why", "When", "A", "'Which' asks about specific animal (lion)."),
        ("___ did the lion do to the three clever Brahmins?", "What", "Who", "Where", "Why", "A", "'What' asks about action (killed and ate them)."),
        ("___ did the fourth Brahmin go after the lion left?", "Where", "Who", "Why", "What", "A", "'Where' asks about destination (back to ashram)."),
        ("___ lesson/moral does the story teach us?", "What", "Who", "Where", "Why", "A", "'What' asks about moral lesson."),
        ("___ disciples survived the attack by the lion?", "How many", "Who", "Where", "Why", "A", "'How many' asks about number (only one)."),
        ("___ failed to save the three Brahmins despite their magical powers?", "What", "Who", "Where", "Why", "A", "'What' asks about cause (lack of common sense)."),
        ("___ did the fourth Brahmin warn his friends?", "How many times / Why", "Who", "Where", "What", "A", "'Why' / 'How' asks about warning.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_qwords, start=1):
        qid = f"BK02_CH02_CAT07_Q{idx:02d}"
        qtxt = f"Choose the correct **question word** (Who, What, Where, Why, How, When):\n\n\"{q_blank} _____?\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Question Word Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Match question to answer: Question: '___ did the lion kill the three Brahmins?' Answer: 'Because it was hungry.'", "Why", "What", "Where", "Who", "A", "'Why' asks for reasons ('Because...')."),
        ("Match question to answer: Question: '___ was the sage's ashram located?' Answer: 'In the quiet forest.'", "Where", "Who", "Why", "When", "A", "'Where' asks for location."),
        ("Choose the correct question word for TIME: '___ did the Brahmins rest under the tree?'", "When", "Where", "Who", "Why", "A", "'When' inquires about time (in the evening)."),
        ("Form an asking sentence: 'The fourth Brahmin climbed a tree.' -> '____ did the fourth Brahmin climb?'", "What / Which tree", "Who", "Why", "Where", "A", "'What' or 'Which tree' inquires about object."),
        ("Identify the INCORRECT question word usage: '**Why** is the fourth Brahmin's name?'", "'Why' should be 'What'", "'Why' should be 'Where'", "'Why' should be 'When'", "No error", "A", "'What is the fourth Brahmin's name?' asks for identity."),
        ("Select the proper interrogative sentence:", "Why did the third Brahmin chant the spell?", "Why the third Brahmin chanted the spell?", "Why did the third Brahmin chanted the spell?", "Why third Brahmin chant spell?", "A", "Interrogative word + auxiliary 'did' + base verb 'chant'."),
        ("Which question word asks about MANNER or METHOD? '___ did the fourth Brahmin escape the lion?'", "How", "Who", "What", "Where", "A", "'How' inquires about method/manner (by climbing a tree)."),
        ("Complete the question: '___ of the four disciples possessed common sense?'", "Which", "What", "Where", "Why", "A", "'Which' chooses between specific options."),
        ("Change statement to question: 'The lion devoured three Brahmins.' -> '____ devoured three Brahmins?'", "What animal / Who", "Where", "Why", "When", "A", "'What animal' or 'Who' asks for subject."),
        ("Fill in the blank: '___ clever were the three disciples in magic?'", "How", "What", "Where", "Why", "A", "'How clever' measures degree."),
        ("Identify the question word in: 'Whom did the sage instruct in his ashram?'", "Whom", "did", "sage", "ashram", "A", "'Whom' is the interrogative pronoun asking about object person."),
        ("Choose the question that matches this answer: 'He climbed a tree because he saw the lion waking up.'", "Why did the fourth Brahmin climb the tree?", "Where did he climb?", "Who climbed the tree?", "What did he climb?", "A", "'Why...' matches answer starting with 'because...'."),
        ("Fill in the blank: '___ Brahmin possessed true wisdom?'", "Which", "Who", "Why", "Where", "A", "'Which Brahmin' asks for identification among group."),
        ("Complete: '___ time did they spend walking through the forest?'", "How much", "How many", "Who", "Where", "A", "'How much' asks about uncountable quantity (time)."),
        ("Select the correct question for: 'The third Brahmin brought the lion back to life.'", "What did the third Brahmin do?", "Where was the third Brahmin?", "Why is the third Brahmin poor?", "Who was the lion?", "A", "'What did third Brahmin do?' asks for action."),
        ("Which question word inquires about POSSESSION? '___ skeleton was restored by the Brahmins?'", "Whose", "Who", "Where", "Why", "A", "'Whose' asks about ownership/origin."),
        ("Form question: 'The sage had four disciples.' -> '____ disciples did the sage have?'", "How many", "How much", "Why", "Where", "A", "'How many' asks for countable number."),
        ("Identify the question mark error: 'Why did the lion attack them.' Correct it:", "Why did the lion attack them?", "Why did the lion attack them!", "Why did the lion attack them,", "Why did the lion attack them;", "A", "Questions must end with question mark ?")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH02_CAT07_Q{idx:02d}"
        qtxt = f"Question Formation & Context Alignment:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Interrogative Sentence Formation", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence structure: 'Why did the third Brahmin revive the lion?' What is the syntax pattern?", "Question Word + Helping Verb (did) + Subject (third Brahmin) + Main Verb (revive) + Object", "Question Word + Main Verb + Subject", "Subject + Question Word + Verb", "Helping Verb + Question Word + Subject", "A", "Standard English question syntax."),
        ("Differentiate between 'How many' vs 'How much': '___ bones' vs '___ wisdom'", "'How many' for countable bones; 'How much' for uncountable wisdom.", "Both use 'How many'.", "Both use 'How much'.", "'How much' for bones; 'How many' for wisdom.", "A", "Countable nouns take 'How many'; uncountable nouns take 'How much'."),
        ("Spot the syntax error in question: 'Where the fourth Brahmin went after the attack?' Correct it:", "Where **did** the fourth Brahmin go after the attack?", "Where the fourth Brahmin go?", "Where went the fourth Brahmin?", "Where does the fourth Brahmin went?", "A", "Past simple questions require auxiliary 'did' before subject and base verb 'go'."),
        ("Framing multi-question interview: What sequence of question words logically reveals the story plot?", "Who -> What did they find -> What foolish act was committed -> How did the wise Brahmin survive", "How -> Who -> Why -> What", "Where -> Where -> Where -> Where", "Why -> Why -> Why -> Why", "A", "Reveals character, incident, conflict, and resolution."),
        ("Transform the statement into a formal question: 'Bookish knowledge without common sense is useless.'", "Why is bookish knowledge without common sense useless?", "Where is bookish knowledge useless?", "Who has bookish knowledge?", "What is a book?", "A", "Directly targets the moral lesson."),
        ("Analyze this ambiguous question: 'What did the Brahmin do?' How can it be made precise?", "Add specific context: 'What magic step did the third Brahmin perform on the lion's body?'", "Make it shorter: 'What Brahmin?'", "Change to: 'Where Brahmin?'", "Remove 'What'.", "A", "Adding specific context clarifies which Brahmin and which action."),
        ("Choose the correct question pair for dialogue: Fourth Brahmin: '___ are you reviving the lion?' Third Brahmin: '___ is your problem? I am showing my skill!'", "Why, What", "Who, Where", "Where, How", "When, Whose", "A", "Why (reason for reviving), What (expression of annoyance)."),
        ("Spot the DOUBLE auxiliary error: 'Why did the third Brahmin brought the lion back to life?'", "'did' requires base verb 'bring', not past tense 'brought'.", "'did' should be 'was'.", "'Why' should be 'How'.", "No error.", "A", "Auxiliary 'did' must be followed by base form of verb ('bring')."),
        ("Reconstruct question from answer: Answer: 'Common sense is far superior to mere bookish knowledge.'", "Question: 'What is the main moral lesson taught by the story of the Four Brahmins?'", "Question: 'Where did Brahmins go?'", "Question: 'Who is lion?'", "Question: 'Why lion eat?'", "A", "Targets the moral theme."),
        ("Form indirect question: 'The sage asked where his three disciples had gone.' What is the sentence type?", "Assertive statement containing an embedded indirect question.", "Direct question requiring question mark.", "Exclamatory sentence.", "Command.", "A", "Indirect questions are statements ending with full stop."),
        ("Identify the correct question word for moral reasoning: '___ did the three clever Brahmins fail despite their magic?'", "Why", "What", "Who", "Where", "A", "'Why' inquires into the moral reason for failure (lack of wisdom)."),
        ("HOTS Reasoning: Why is 'Who' used for people but 'Which' used when selecting from a specific group of people?", "'Who' is general; 'Which' is used when choosing from a defined limited set.", "'Who' is for animals.", "'Which' is only for things.", "Both are identical.", "A", "'Which of the four Brahmins...' selects from a defined group."),
        ("Correct all errors in: 'who revived the dead lion'", "Who revived the dead lion?", "Who revived the dead lion.", "Whom revived dead lion?", "Who does revived the dead lion?", "A", "Capital W, question mark at end."),
        ("Select the question that evaluates Higher Order Thinking (HOTS) about Chapter 02:", "How does the story demonstrate that practical wisdom is superior to book learning?", "What animal was made of bones?", "Where did the sage live?", "Did the lion eat them?", "A", "Asks student to evaluate moral theme and cause-and-effect.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH02_CAT07_Q{idx:02d}"
        qtxt = f"Higher Order Interrogative Analysis & Syntax:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Question Syntax & Analytical Framing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 8. Present Continuous Tense (-ing) (50 Qs)
# ---------------------------------------------------------------------------
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense (-ing) — Chapter 02: Four Brahmins\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_ing = [
        ("The fourth Brahmin is **climbing** up the tree.", "climbing", "fourth", "is", "tree", "A", "'climbing' is verb + -ing form."),
        ("The third Brahmin is **chanting** a spell.", "chanting", "third", "is", "spell", "A", "'chanting' is verb + -ing form."),
        ("The lion is **waking** up from the dead.", "waking", "lion", "is", "dead", "A", "'waking' is verb + -ing form."),
        ("The disciples are **walking** through the forest.", "walking", "disciples", "are", "forest", "A", "'walking' is verb + -ing form."),
        ("The second Brahmin is **restoring** the organs.", "restoring", "second", "is", "organs", "A", "'restoring' is verb + -ing form."),
        ("The first Brahmin is **assembling** the skeleton.", "assembling", "first", "is", "skeleton", "A", "'assembling' is verb + -ing form."),
        ("The hungry lion is **devouring** the three friends.", "devouring", "lion", "is", "friends", "A", "'devouring' is verb + -ing form."),
        ("The fourth Brahmin is **warning** his companions.", "warning", "fourth", "is", "companions", "A", "'warning' is verb + -ing form."),
        ("The fourth Brahmin is **grieving** for his lost friends.", "grieving", "fourth", "is", "friends", "A", "'grieving' is verb + -ing form."),
        ("The simpleton is **preparing** dinner under the tree.", "preparing", "simpleton", "is", "dinner", "A", "'preparing' is verb + -ing form."),
        ("The sage is **teaching** lessons at the ashram.", "teaching", "sage", "is", "ashram", "A", "'teaching' is verb + -ing form."),
        ("The lion is **roaring** loudly.", "roaring", "lion", "is", "loudly", "A", "'roaring' is verb + -ing form."),
        ("The fourth Brahmin is **returning** to the ashram.", "returning", "fourth", "is", "ashram", "A", "'returning' is verb + -ing form."),
        ("The three Brahmins are **showing** off their magic.", "showing", "three", "are", "magic", "A", "'showing' is verb + -ing form."),
        ("The birds are **flying** above the trees.", "flying", "birds", "are", "trees", "A", "'flying' is verb + -ing form."),
        ("The sun is **setting** in the evening.", "setting", "sun", "is", "evening", "A", "'setting' is verb + -ing form."),
        ("The fourth Brahmin is **watching** from the tree branch.", "watching", "fourth", "is", "branch", "A", "'watching' is verb + -ing form."),
        ("The disciples are **traveling** to the town.", "traveling", "disciples", "are", "town", "A", "'traveling' is verb + -ing form.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_ing, start=1):
        qid = f"BK02_CH02_CAT08_Q{idx:02d}"
        qtxt = f"Identify the **present continuous (-ing) verb** in this sentence:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the present continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Present Continuous Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("What is the correct -ing spelling rule for **'climb'**? (The Brahmin is ____ the tree.)", "climbing (add -ing)", "climbbing", "climeing", "climbbng", "A", "Regular verb adding -ing (climbing)."),
        ("What is the correct -ing spelling rule for **'prepare'**? (He is ____ dinner.)", "preparing (drop final silent e)", "prepareing", "preparring", "prepareing", "A", "Drop final silent 'e' before adding -ing (preparing)."),
        ("What is the correct -ing spelling rule for **'run'**? (The lion is ____ after them.)", "running (double the last consonant)", "runing", "runnning", "runeing", "A", "CVC rule: double final consonant before -ing (running)."),
        ("Fill in the blank with present continuous form: 'The third Brahmin (chant) ____ a spell.'", "is chanting", "was chant", "are chant", "is chanted", "A", "Singular subject takes 'is chanting'."),
        ("Choose the sentence in PRESENT CONTINUOUS tense:", "The lion is roaring in the forest.", "The lion roared in the forest.", "The lion will roar in the forest.", "The lion roared yesterday.", "A", "'is roaring' is present continuous."),
        ("Fill in the blanks: 'The Brahmins ____ (rest) under the tree, and the lion ____ (wake) up.'", "are resting, is waking", "is resting, are waking", "are rest, is wake", "was resting, were waking", "A", "Plural 'Brahmins' takes 'are resting'; singular 'lion' takes 'is waking'."),
        ("Identify the spelling mistake in: 'The Brahmin is **chantting** a spell.'", "'chantting' should be 'chanting'", "'chantting' should be 'chanting'", "'is' should be 'are'", "No mistake", "A", "Chant does not double 't' (chanting)."),
        ("Select the correct -ing form for **'restore'**:", "restoring", "restoreing", "restorring", "restorng", "A", "Drop silent 'e': restore -> restoring."),
        ("Which sentence describes an action HAPPENING RIGHT NOW?", "The fourth Brahmin is looking down from the tree.", "The fourth Brahmin looked down yesterday.", "The fourth Brahmin looks down every day.", "The fourth Brahmin will look down tomorrow.", "A", "Present continuous ('is looking') describes ongoing action right now."),
        ("Fill in the blank: 'I ____ (warn) you not to revive the lion!'", "am warning", "is warning", "are warning", "am warneing", "A", "Subject 'I' takes 'am warning'."),
        ("Choose the correct form: 'The three friends ____ (ignore) the wise advice.'", "are ignoring", "is ignoring", "am ignoring", "are ignore", "A", "Plural subject 'three friends' takes 'are ignoring'."),
        ("Identify the verb in: 'Why are you reviving the dead lion?'", "are reviving", "Why", "you", "dead lion", "A", "Helping verb 'are' + main verb 'reviving' form present continuous."),
        ("What is the -ing form of **'sit'**?", "sitting", "siting", "sittting", "siteing", "A", "CVC rule: sit -> sitting."),
        ("What is the -ing form of **'hide'**?", "hiding", "hideing", "hidding", "hideing", "A", "Drop silent e: hide -> hiding."),
        ("Change simple present to continuous: 'The lion roars.' -> 'The lion ____.'", "is roaring", "roared", "was roaring", "will roar", "A", "is roaring."),
        ("Fill in the blank: 'The Brahmin ____ (plead) with his companions to stop.'", "is pleading", "are pleading", "am pleading", "pleaded", "A", "is pleading."),
        ("Identify the correct present continuous sentence:", "Look! The lion is opening its eyes.", "Look! The lion open its eyes.", "Look! The lion opened its eyes.", "Look! The lion opening its eyes.", "A", "Exclamation 'Look!' introduces action happening now ('is opening')."),
        ("Select the correct -ing form for **'assemble'**:", "assembling", "assembleing", "assemblling", "assemblng", "A", "Drop silent e: assemble -> assembling.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH02_CAT08_Q{idx:02d}"
        qtxt = f"Present Continuous Grammar & Spelling Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Present Continuous Formation & Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze spelling rules for adding -ing to verbs: Group them correctly: (stop, create, lie)", "stop -> stopping (double consonant), create -> creating (drop e), lie -> lying (change -ie to -y)", "All just add -ing.", "All double the last letter.", "stop -> stoping, create -> createing, lie -> lieing", "A", "3 distinct orthographic rules for -ing derivation."),
        ("Convert past tense narrative to present continuous picture scene: 'The third Brahmin chanted while the lion woke up.'", "The third Brahmin is chanting while the lion is waking up.", "The third Brahmin chanting while lion waking up.", "The third Brahmin was chanting while lion woke up.", "The third Brahmin will chant while lion wakes up.", "A", "Both verbs transformed to present continuous (is chanting, is waking)."),
        ("Spot the missing auxiliary verb in: 'The fourth Brahmin climbing the tree and the lion roaring.' Correct it:", "'The fourth Brahmin **is** climbing the tree and the lion **is** roaring.'", "'The fourth Brahmin climbing tree and lion roaring.'", "'The fourth Brahmin **are** climbing and lion **are** roaring.'", "No error.", "A", "Present continuous requires auxiliary (is/am/are) before -ing verb."),
        ("Differentiate state vs action: Why don't we usually say 'The sage is **believing** in wisdom'?", "Because 'believe' is a stative verb expressing a state of mind, not an ongoing physical action.", "Because 'believing' is hard to spell.", "Because sage is old.", "Because lion ate them.", "A", "Stative verbs (believe, know, want) do not usually take continuous form."),
        ("Identify the sentence with CORRECT present continuous subject-verb agreement:", "The three clever Brahmins are boasting about their powers.", "The three clever Brahmins is boasting about their powers.", "The three clever Brahmins am boasting about their powers.", "The three clever Brahmins boasting about their powers.", "A", "Plural subject ('three clever Brahmins') takes plural auxiliary 'are'."),
        ("Form negative present continuous: 'The lion is sleeping peacefully.' -> Negative:", "The lion is **not** sleeping peacefully.", "The lion not sleeping peacefully.", "The lion is no sleeping peacefully.", "The lion isn't sleep peacefully.", "A", "Add 'not' between auxiliary 'is' and main verb 'sleeping'."),
        ("Spot all THREE spelling errors: 'He is **prepareing** dinner, **runing** fast, and **dieing** of fear.'", "'prepareing' -> 'preparing'; 'runing' -> 'running'; 'dieing' -> 'dying'", "'prepareing' -> 'preparring'; 'runing' -> 'runing'; 'dieing' -> 'dieing'", "No errors.", "Only 'runing' is wrong.", "A", "preparing (drop e), running (double n), dying (-ie to -y)."),
        ("Rewrite as interrogative present continuous: 'The third Brahmin is chanting a spell.'", "**Is** the third Brahmin chanting a spell?", "Are the third Brahmin chanting a spell?", "The third Brahmin chanting a spell?", "Why the third Brahmin is chanting spell?", "A", "Move auxiliary 'Is' to beginning of sentence."),
        ("Analyze action timeline: 'The Brahmins **are starting** their journey tomorrow.' What does present continuous express here?", "A fixed future arrangement / planned action.", "Past completed action.", "Action that happened long ago.", "Uncertain rumor.", "A", "Present continuous can express planned future actions."),
        ("Choose the sentence showing PARALLEL present continuous actions:", "While the third Brahmin is chanting, the fourth Brahmin is climbing a tree.", "While third Brahmin chanted, fourth Brahmin is climbing.", "Third Brahmin is chanting while fourth Brahmin climbed.", "Third Brahmin chant while fourth Brahmin climb.", "A", "Both parallel ongoing actions use present continuous."),
        ("Correct the error: 'The lion is attackking the Brahmins.'", "'attackking' should be 'attacking' (single 'k').", "'is' should be 'are'.", "'lion' should be capitalized.", "No error.", "A", "Attack ends in consonant blend -ck, just add -ing (attacking)."),
        ("HOTS Reasoning: Compare 'The lion killed them' (Past Simple) vs 'The lion is killing them' (Present Continuous). How does the meaning change?", "Past simple states a completed past event; present continuous describes an action currently in progress.", "Both mean the exact same thing.", "Past simple is for future; continuous is for past.", "Continuous means lion was friendly.", "A", "Tense changes temporal aspect (completed vs ongoing)."),
        ("Form question: 'Why ____ the Brahmins ____ (arguing)?'", "are, arguing", "is, arguing", "am, arguing", "do, arguing", "A", "Plural subject Brahmins takes 'are ... arguing'."),
        ("Identify the correct present continuous sentence describing animal action:", "The starved lion is devouring its prey under the tree.", "The starved lion is devour its prey under the tree.", "The starved lion are devouring its prey under the tree.", "The starved lion devouring its prey under the tree.", "A", "Singular lion + is + devouring.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH02_CAT08_Q{idx:02d}"
        qtxt = f"Higher Order Present Continuous Analysis & Editing:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Continuous Tense Aspect & Error Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 9. Helping Verbs (Is, Am, Are) (50 Qs)
# ---------------------------------------------------------------------------
def build_helping_verbs():
    header = "# Category 9: Helping Verbs (Is, Am, Are) — Chapter 02: Four Brahmins\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_hv = [
        ("The fourth Brahmin ___ wise and sensible.", "is", "are", "am", "be", "A", "Singular subject 'The fourth Brahmin' takes 'is'."),
        ("I ___ learning the story of the Four Brahmins.", "am", "is", "are", "be", "A", "Pronoun 'I' takes 'am'."),
        ("The three Brahmins ___ clever but foolish.", "are", "is", "am", "be", "A", "Plural subject 'three Brahmins' takes 'are'."),
        ("The sage ___ respected by all his disciples.", "is", "are", "am", "be", "A", "Singular subject 'sage' takes 'is'."),
        ("The lion's bones ___ scattered under the tree.", "are", "is", "am", "be", "A", "Plural subject 'bones' takes 'are'."),
        ("The third Brahmin ___ arrogant about his skill.", "is", "are", "am", "be", "A", "Singular subject 'third Brahmin' takes 'is'."),
        ("The disciples ___ walking towards the town.", "are", "is", "am", "be", "A", "Plural subject 'disciples' takes 'are'."),
        ("The fourth Brahmin and the sage ___ at the ashram.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("I ___ sure that common sense is essential.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The Panchatantra fable ___ moral and educational.", "is", "are", "am", "be", "A", "Singular 'fable' takes 'is'."),
        ("The lion's teeth ___ sharp and dangerous.", "are", "is", "am", "be", "A", "Plural 'teeth' takes 'are'."),
        ("The tree ___ tall and leafy.", "is", "are", "am", "be", "A", "Singular 'tree' takes 'is'."),
        ("You ___ reading Chapter 02.", "are", "is", "am", "be", "A", "Pronoun 'You' always takes 'are'."),
        ("The lion ___ waking up now.", "is", "are", "am", "be", "A", "Singular 'lion' takes 'is'."),
        ("The magic spells ___ dangerous without wisdom.", "are", "is", "am", "be", "A", "Plural 'spells' takes 'are'."),
        ("I ___ glad the fourth Brahmin survived.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The fourth Brahmin ___ safe on the tree branch.", "is", "are", "am", "be", "A", "Singular 'fourth Brahmin' takes 'is'."),
        ("The three friends ___ dead after the lion's attack.", "are", "is", "am", "be", "A", "Plural 'three friends' takes 'are'.")
    ]
    
    for idx, (sent_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_hv, start=1):
        qid = f"BK02_CH02_CAT09_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct helping verb (is / am / are):\n\n\"{sent_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Helping Verb Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Choose the correct helping verb: 'The first Brahmin and the second Brahmin ____ working on the skeleton.'", "are", "is", "am", "be", "A", "Compound subject ('first Brahmin and second Brahmin') is plural, so it takes 'are'."),
        ("Select the sentence with CORRECT helping verb agreement:", "The fourth Brahmin is resting on the tree branch.", "The fourth Brahmin are resting on the tree branch.", "The fourth Brahmin am resting on the tree branch.", "The fourth Brahmin be resting on the tree branch.", "A", "Singular noun 'fourth Brahmin' requires 'is'."),
        ("Fill in the blanks: 'I ____ writing the answer, and my classmates ____ listening.'", "am, are", "is, are", "are, is", "am, is", "A", "'I am', 'classmates are'."),
        ("Identify the mistake in: 'The lion's claws **is** very sharp.'", "'is' should be 'are' because 'claws' is a plural noun.", "'is' should be 'am'", "'is' should be 'was'", "No mistake", "A", "'claws' is plural, requiring 'are'."),
        ("Which helping verb completes the question? '____ you aware of the danger, my friends?'", "Are", "Is", "Am", "Be", "A", "Subject 'you' takes 'Are'."),
        ("Fill in the blank: 'Neither knowledge nor magic ____ useful without common sense.'", "is", "are", "am", "be", "A", "'Neither...nor' with singular second subject takes 'is'."),
        ("Select the correct sentence for story moral:", "Wisdom and common sense are superior to mere knowledge.", "Wisdom and common sense is superior to mere knowledge.", "Wisdom and common sense am superior to mere knowledge.", "Wisdom and common sense be superior to mere knowledge.", "A", "Compound subject 'Wisdom and common sense' takes 'are'."),
        ("Complete the conversation: Sage: 'Where ____ the three disciples?' Fourth Brahmin: 'They ____ no more!'", "are, are", "is, is", "is, are", "are, is", "A", "Plural 'three disciples' -> are; plural 'They' -> are."),
        ("Identify where 'is' is used incorrectly:", "The bones **is** lying on the ground.", "The lion is wild.", "The sage is wise.", "The tree is tall.", "A", "'The bones is' should be 'The bones are'."),
        ("Choose the correct helping verb for collective noun used as a single unit: 'The group of disciples ____ studying.'", "is", "are", "am", "be", "A", "Collective noun 'group' treated as singular unit takes 'is'."),
        ("Fill in the blank: 'The simpleton ____ not interested in showing off magic.'", "is", "are", "am", "be", "A", "Singular 'simpleton' takes 'is'."),
        ("Select the sentence with correct helping verb for 'I':", "I am sitting on a high tree branch.", "I is sitting on a high tree branch.", "I are sitting on a high tree branch.", "I be sitting on a high tree branch.", "A", "Subject 'I' takes 'am'."),
        ("Fill in the blank: 'There ____ three dead Brahmins on the forest floor.'", "are", "is", "am", "be", "A", "'There are' before plural noun 'three dead Brahmins'."),
        ("Fill in the blank: 'There ____ a dangerous lion nearby.'", "is", "are", "am", "be", "A", "'There is' before singular noun 'a dangerous lion'."),
        ("Choose the correct sentence:", "What are the disciples doing with the bones?", "What is the disciples doing with the bones?", "What am the disciples doing with the bones?", "What be the disciples doing with the bones?", "A", "Plural subject 'the disciples' takes 'are'."),
        ("Identify the correct form: 'The lion, as well as its cubs, ____ hungry.'", "is", "are", "am", "be", "A", "Subject is singular 'The lion' ('as well as...' does not change subject number), taking 'is'."),
        ("Fill in the blank: 'Both the first Brahmin and the second Brahmin ____ guilty of foolishness.'", "are", "is", "am", "be", "A", "'Both ... and ...' takes plural verb 'are'."),
        ("Select the option with correct helping verbs: 'The third Brahmin ____ foolish, but I ____ sensible.'", "is, am", "are, is", "am, are", "is, are", "A", "'third Brahmin is', 'I am'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH02_CAT09_Q{idx:02d}"
        qtxt = f"Helping Verb Subject-Verb Agreement Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Subject-Verb Agreement Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze subject-verb agreement: 'Each of the three Brahmins **____** proud of his skill.' Choose the correct verb and reason:", "is — because 'Each' is a singular indefinite pronoun requiring singular verb 'is'.", "are — because 'three Brahmins' is plural.", "am — because it refers to speaker.", "be — because Brahmins are clever.", "A", "'Each' is singular indefinite pronoun taking singular verb 'is'."),
        ("Spot the subtle agreement error in: 'A set of magic spells **are** written in the book.'", "'are' should be 'is' because the subject is singular noun 'set'.", "'are' should be 'am'.", "'spells' should be 'spell'.", "No error.", "A", "'A set' is singular, so it requires 'is written'."),
        ("Compare: (1) 'The 1st Brahmin and 2nd Brahmin **are** working.' vs (2) 'The 1st Brahmin, along with the 2nd Brahmin, **is** working.' Why are the verbs different?", "In (1), 'and' creates a plural subject (are); in (2), 'along with' is a prepositional phrase, leaving '1st Brahmin' as sole singular subject (is).", "They mean different things.", "Sentence (2) is grammatically wrong.", "Both should use 'are'.", "A", "Prepositional phrases like 'along with' do not change subject number."),
        ("Identify the correct agreement for indefinite pronouns: 'Everyone in the ashram **____** listening to the sage.'", "is", "are", "am", "be", "A", "'Everyone' is a singular indefinite pronoun requiring 'is'."),
        ("Spot all THREE subject-verb errors in: 'The disciples **is** clever, I **is** safe, and the lion **are** dangerous.'", "'disciples is' -> 'disciples are'; 'I is' -> 'I am'; 'lion are' -> 'lion is'", "'disciples is' -> 'disciples am'; 'I is' -> 'I are'; 'lion are' -> 'lion am'", "Only 'I is' is wrong.", "No errors present.", "A", "disciples are (plural), I am (1st person), lion is (3rd person singular)."),
        ("Fill in the blanks in this complex sentence: 'Not only the 1st Brahmin but also his companions **____** foolish, while the 4th Brahmin **____** wise.'", "are, is", "is, are", "is, is", "are, are", "A", "'Not only...but also' agrees with closer subject ('companions' -> are); '4th Brahmin' -> is."),
        ("Transform to negative: 'The lion and the Brahmins are under the tree.'", "The lion and the Brahmins **are not** under the tree.", "The lion and the Brahmins is not under the tree.", "The lion and the Brahmins am not under the tree.", "The lion and the Brahmins not under tree.", "A", "Add 'not' after plural helping verb 'are'."),
        ("Analyze inverted subject position: 'Beside the banyan tree **____** sitting a wise sage.'", "is", "are", "am", "be", "A", "Subject is singular 'a wise sage', appearing after verb, requiring 'is'."),
        ("Determine agreement with uncountable nouns: 'The knowledge gained by the disciples **____** impressive.'", "is", "are", "am", "be", "A", "Uncountable noun 'knowledge' is treated as singular, taking 'is'."),
        ("Correct the sentence: 'Here **is** the bones of the lion.'", "Here **are** the bones of the lion.", "Here am the bones of the lion.", "Here be the bones of the lion.", "No error.", "A", "Plural subject 'bones' requires 'Here are...''"),
        ("Identify the sentence where 'is' acts as a MAIN linking verb rather than a helping verb:", "The fourth Brahmin **is** a simpleton.", "The fourth Brahmin **is** climbing the tree.", "The fourth Brahmin **is** warning his friends.", "The fourth Brahmin **is** running away.", "A", "In 'The fourth Brahmin is a simpleton', 'is' is the main linking verb connecting subject to predicate noun."),
        ("HOTS Reasoning: Why does English use 'am' ONLY with the subject pronoun 'I'?", "Because 'am' is the unique 1st person singular present indicative form of the verb 'to be'.", "Because 'I' is capitalized.", "Because sage commanded it.", "There is no reason.", "A", "'am' is exclusively reserved for 1st person singular 'I'."),
        ("Fill in the blanks: 'Neither the 1st Brahmin nor the other disciples **____** listening, because they **____** proud.'", "are, are", "is, is", "is, are", "are, is", "A", "'other disciples' is closer plural subject -> are; 'they' -> are."),
        ("Select the option with PERFECT helping verb agreement throughout:", "The sage is wise, I am sensible, and the three friends are foolish.", "The sage are wise, I is sensible, and the three friends is foolish.", "The sage am wise, I are sensible, and the three friends am foolish.", "The sage is wise, I is sensible, and the three friends is foolish.", "A", "sage is (singular), I am (1st person), three friends are (plural).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH02_CAT09_Q{idx:02d}"
        qtxt = f"Higher Order Helping Verb Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Subject-Verb Agreement & Syntax", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# MAIN EXECUTION FOR REBUILDING CHAPTER 02
# ---------------------------------------------------------------------------
def rebuild_chapter_02():
    print("Rebuilding Chapter 02 category files with high-quality, multi-tiered (Easy/Medium/Hard) non-duplicate questions...")

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
        filepath = os.path.join(CH02_DIR, fname)
        print(f"  Generating {fname}...")
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {fname} created successfully.")

    print("\n[SUCCESS] Completed rebuilding all 9 category files for Chapter 02 (450 total high-quality questions)!")

if __name__ == "__main__":
    rebuild_chapter_02()
