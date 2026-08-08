r"""
=============================================================================
Script: rebuild_chapter_01.py
Description: Generates 50 rich, non-duplicate, multi-tiered (Easy, Medium, Hard)
             questions for each of the 9 category files in Chapter 01:
             "The Rats Who Ate the Iron Balance" (450 Qs total).
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH01_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_01")
os.makedirs(CH01_DIR, exist_ok=True)

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
    header = "# Category 1: Plural Nouns & Spelling Rules — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("rat", "rats", "rate", "raties", "ratses", "A", "Regular noun adding -s."),
        ("scale", "scales", "scalez", "scalies", "scaleses", "A", "Regular noun adding -s."),
        ("boy", "boys", "boies", "boyes", "boiy", "A", "Vowel + y adds -s."),
        ("mouse", "mice", "mouses", "meece", "mices", "A", "Irregular plural: mouse becomes mice."),
        ("dish", "dishes", "dishs", "dished", "dishies", "A", "Nouns ending in -sh add -es."),
        ("box", "boxes", "boxs", "boxies", "boxen", "A", "Nouns ending in -x add -es."),
        ("leaf", "leaves", "leafs", "leafes", "leavs", "A", "Nouns ending in -f change -f to -ves."),
        ("story", "stories", "storys", "storyes", "storie", "A", "Consonant + y changes to -ies."),
        ("city", "cities", "citys", "cityes", "cites", "A", "Consonant + y changes to -ies."),
        ("child", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("day", "days", "daies", "dayes", "dayz", "A", "Vowel + y adds -s."),
        ("river", "rivers", "riveres", "riveries", "riverz", "A", "Regular noun adding -s."),
        ("father", "fathers", "fatheres", "fatheries", "fatherz", "A", "Regular noun adding -s."),
        ("year", "years", "yeares", "yearies", "yearz", "A", "Regular noun adding -s."),
        ("friend", "friends", "friendes", "friendies", "friendz", "A", "Regular noun adding -s."),
        ("village", "villages", "villagies", "villagese", "villagz", "A", "Regular noun ending in -e adds -s."),
        ("bank", "banks", "bankes", "bankies", "bankz", "A", "Regular noun adding -s."),
        ("tooth", "teeth", "tooths", "toothes", "teethes", "A", "Irregular plural: tooth becomes teeth.")
    ]
    
    for idx, (word, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH01_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{word}'** as seen in or related to Chapter 01 (*The Rats Who Ate the Iron Balance*)?"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Plural Noun Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Dilip bought three (scale / scales) from the market.", "scales", "scale", "scalees", "scalies", "A", "'three' requires plural noun 'scales'."),
        ("The Mahajan claimed that many (mouse / mice) ate the iron balance.", "mice", "mouses", "mouse", "mices", "A", "'many' requires plural 'mice'."),
        ("Dilip saw five (boy / boys) near the river bank.", "boys", "boies", "boy", "boyes", "A", "'five' requires plural 'boys'."),
        ("Identify the word with an INCORRECT plural spelling in this list: rats, scales, boyes, rivers.", "boyes", "rats", "scales", "rivers", "A", "The plural of boy is 'boys', not 'boyes'."),
        ("Choose the sentence with the correct plural noun form:", "Dilip returned after five years.", "Dilip returned after five yeares.", "Dilip returned after five year.", "Dilip returned after five yearies.", "A", "'years' is the correct plural form of year."),
        ("Which of the following nouns forms its plural by changing the vowel sound completely?", "mouse -> mice", "rat -> rats", "boy -> boys", "scale -> scales", "A", "Mouse changes to mice (irregular vowel change)."),
        ("Change the underlined singular noun to plural: 'The eagle flew past the **tree**.'", "trees", "treess", "treies", "treez", "A", "Plural of tree is trees."),
        ("Select the sentence where ALL plural nouns are spelt correctly:", "The rats ate the scales in the houses.", "The meeces ate the scales in the houses.", "The rats ate the scalees in the housen.", "The mouses ate the scales in the house.", "A", "rats, scales, houses are all correctly spelt plurals."),
        ("What is the plural of 'thief' (a person who steals like Mahajan)?", "thieves", "thiefs", "thiefes", "thieveses", "A", "Nouns ending in -f change -f to -ves (thieves)."),
        ("Dilip carried two heavy (box / boxes) across the village.", "boxes", "boxs", "box", "boxies", "A", "Nouns ending in -x add -es."),
        ("The Mahajan hid behind two big (bush / bushes).", "bushes", "bushs", "bush", "bushies", "A", "Nouns ending in -sh add -es."),
        ("Dilip heard many (echo / echoes) in the valley.", "echoes", "echos", "echo", "echoies", "A", "Nouns ending in -o usually add -es."),
        ("How many (day / days) did Dilip stay in the foreign land?", "days", "daies", "day", "dayes", "A", "Vowel + y adds -s (days)."),
        ("The Mahajan had two (child / children) living in the house.", "children", "childs", "child", "childrens", "A", "Irregular plural of child is children."),
        ("Which plural noun rule applies to the word **'cities'**?", "Change consonant + y to -ies", "Add -es to -x", "Add -s to vowel + y", "Change -f to -ves", "A", "City ends in consonant + y, so y becomes -ies."),
        ("Dilip placed four (glass / glasses) on the table.", "glasses", "glasss", "glass", "glassies", "A", "Nouns ending in -ss add -es."),
        ("Identify the correct plural form of 'man':", "men", "mans", "manes", "mens", "A", "Irregular plural: man becomes men."),
        ("The eagle flew over three (hill / hills).", "hills", "hilles", "hill", "hillies", "A", "Regular noun adding -s.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH01_CAT01_Q{idx:02d}"
        qtxt = f"Contextual Plural Rule Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Plural Noun Application", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Rewrite the sentence in PLURAL form: 'The rat ate a scale in the house.'", "The rats ate scales in the houses.", "The mouses ate scales in the house.", "The rats ate scalees in the housen.", "The meeces ate scale in the houses.", "A", "Plural of rat->rats, scale->scales, house->houses."),
        ("Analyze the error: 'The Mahajan said that three mouses ate his iron balance.' What is the correct grammar rule?", "'mouses' should be 'mice' because mouse is an irregular noun.", "'mouses' should be 'mices' because -es is added.", "'mouses' should remain singular.", "'mouses' should be 'meece'.", "A", "Mouse is an irregular noun with plural 'mice'."),
        ("Complete the paragraph with correct plurals: 'Dilip spent many ____ (year) abroad to earn ____ (rupee). He brought back two heavy ____ (box).'", "years, rupees, boxes", "yeares, rupee, boxs", "year, rupees, boxies", "years, rupees, box", "A", "years (regular), rupees (regular), boxes (-x + es)."),
        ("Identify the sentence where ALL three underline nouns are correctly pluralized:", "The **men** saw the **birds** carrying the **keys**.", "The **mans** saw the **birdes** carrying the **keies**.", "The **mens** saw the **birds** carrying the **keies**.", "The **men** saw the **birdes** carrying the **keys**.", "A", "men (irregular), birds (-s), keys (vowel+y adds -s)."),
        ("Which group contains ONLY irregular plural nouns?", "mice, men, children, teeth", "rats, boys, scales, rivers", "boxes, bushes, dishes, glasses", "leaves, thieves, wolves, knives", "A", "mice, men, children, teeth change internal vowels/endings without standard -s/-es rules."),
        ("Why does 'boy' become 'boys' but 'story' becomes 'stories'?", "Because 'boy' has a vowel before y, while 'story' has a consonant before y.", "Because 'boy' is short and 'story' is long.", "Because 'boy' is a person and 'story' is a thing.", "Both follow the exact same rule.", "A", "Vowel+y adds -s; Consonant+y changes y to -ies."),
        ("Find the TWO grammatical mistakes in: 'The boyes saw four mouses near the river.'", "'boyes' should be 'boys' and 'mouses' should be 'mice'.", "'boyes' should be 'boies' and 'mouses' should be 'mices'.", "'river' should be 'rivers' only.", "There are no mistakes in the sentence.", "A", "boys (vowel+y) and mice (irregular plural)."),
        ("Replace the singular words in brackets: 'Dilip took the ____ (child) to see the ____ (goose) near the lake.'", "children, geese", "childs, gooses", "childrens, geeses", "childes, gooses", "A", "Plural of child is children, plural of goose is geese."),
        ("Analyze this claim: 'All nouns ending in -f change to -ves in plural.' Is this always true?", "No, some nouns like 'roof' just add -s ('roofs').", "Yes, every single -f noun becomes -ves.", "No, all -f nouns change to -ies.", "Yes, -f nouns take -es.", "A", "Roof->roofs, chief->chiefs are exceptions adding only -s."),
        ("Fill in the blanks for the story scene: 'Two ____ (thief) stole five ____ (donkey) from the market.'", "thieves, donkeys", "thiefs, donkeies", "thieves, donkeies", "thiefes, donkeys", "A", "thief -> thieves (-f to -ves); donkey -> donkeys (vowel+y adds -s)."),
        ("Select the option that shows correct plural transformation for ALL three words: 'calf', 'city', 'fox'", "calves, cities, foxes", "calfs, citys, foxs", "calves, cityes, foxies", "calfes, cities, foxen", "A", "calf -> calves; city -> cities; fox -> foxes."),
        ("HOTS Reasoning: If one iron scale is called 'a scale', why do we usually say 'a pair of scales'?", "Because weighing scales have two balancing pans (plural form).", "Because 'scale' has no singular form.", "Because Mahajan made a spelling mistake.", "Because iron cannot be singular.", "A", "Traditional weighing scales consist of two balancing pans."),
        ("Transform into singular: 'The eagles carried the boys to the mountains.'", "The eagle carried the boy to the mountain.", "The eagless carried the boies to the mountain.", "The eagle carry the boy to the mountain.", "The eagles carry the boy to mountain.", "A", "Singular subject and object: eagle, boy, mountain."),
        ("Identify the correct rule for forming the plural of **'match'**:", "Add -es because it ends in -ch (matches).", "Add -s only (matchs).", "Change -ch to -ies (matchees).", "Change vowel sound (metch).", "A", "Nouns ending in -ch add -es.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH01_CAT01_Q{idx:02d}"
        qtxt = f"Higher Order Thinking Skills (HOTS) & Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Plural & Spelling Analysis", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 2. Articles Grammar (50 Qs)
# ---------------------------------------------------------------------------
def build_articles_grammar():
    header = "# Category 2: Articles (A, An, The) — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("Dilip was ___ poor boy from a small village.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'poor'."),
        ("Mahajan was ___ greedy merchant.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'greedy'."),
        ("Dilip saw ___ eagle in the sky.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'eagle'."),
        ("Dilip gave ___ heavy iron scales as security.", "the", "an", "a", "no article", "A", "Use 'the' for specific scales mentioned in the story."),
        ("Mahajan lived in ___ old house.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'old'."),
        ("___ Panchatantra tale teaches moral values.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'Panchatantra'."),
        ("Dilip wanted to earn ___ honest living.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' sound in 'honest'."),
        ("Mahajan hid behind ___ big tree.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'big'."),
        ("___ sun shines brightly over the village.", "The", "A", "An", "No article", "A", "Use 'The' before unique natural object 'sun'."),
        ("Dilip took Mahajan's son to ___ river.", "the", "a", "an", "no article", "A", "Use 'the' for specific river mentioned in story."),
        ("It took ___ hour for Dilip to reach home.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' sound in 'hour'."),
        ("Dilip was ___ honest boy.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' in 'honest'."),
        ("Mahajan gave ___ fake explanation to Dilip.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'fake'."),
        ("___ rats in the story did not really eat iron.", "The", "A", "An", "No article", "A", "Use 'The' for specific rats referred to in the story."),
        ("Dilip went to ___ foreign land.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'foreign'."),
        ("Mahajan felt like ___ foolish man.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'foolish'."),
        ("___ eagle cannot carry a human boy.", "An", "A", "The", "No article", "A", "Use 'An' before vowel sound 'eagle'."),
        ("Dilip returned ___ scales to their owner.", "the", "a", "an", "no article", "A", "Use 'the' for specific scales.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH01_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article (a / an / the):\n\n\"{q_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Basic Article Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Dilip met ___ Mahajan and asked for ___ iron scales back.", "the, the", "a, an", "an, a", "the, a", "A", "Both subjects (Mahajan and scales) are specific in this context."),
        ("Why do we say '**an** eagle' but '**a** rat'?", "Because 'eagle' begins with a vowel sound (e) and 'rat' with a consonant sound (r).", "Because eagles fly higher than rats.", "Because 'eagle' is bigger than 'rat'.", "Because Mahajan preferred eagles.", "A", "Article selection depends on initial vowel/consonant sound."),
        ("Select the sentence with the CORRECT article usage:", "Dilip borrowed money from a Mahajan.", "Dilip borrowed money from an Mahajan.", "Dilip borrowed money from the an Mahajan.", "Dilip borrowed money from a an Mahajan.", "A", "'a Mahajan' is correct as Mahajan starts with consonant sound /m/."),
        ("Fill in the blanks: 'Dilip sat under ___ banyan tree near ___ river.'", "a, the", "an, a", "the, an", "a, a", "A", "'a banyan tree' (first mention), 'the river' (specific location)."),
        ("Identify the INCORRECT article in: 'Dilip saw **an** boy near **the** river.'", "'an' should be 'a'", "'the' should be 'an'", "'an' should be 'the'", "No mistake", "A", "'boy' starts with consonant sound /b/, so it takes 'a'."),
        ("Which article completes the sentence? 'Mahajan learned ___ important lesson today.'", "an", "a", "the", "no article", "A", "'important' starts with vowel sound /i/, requiring 'an'."),
        ("Choose the correct pair of articles: '___ eagle flew over ___ village.'", "An, the", "A, a", "The, an", "An, an", "A", "'An eagle' (vowel sound), 'the village' (specific village)."),
        ("Why do we use 'a' before 'heavy box' in 'Dilip carried **a** heavy box'?", "Because 'heavy' begins with the consonant sound /h/.", "Because box is iron.", "Because heavy is a noun.", "Because Dilip is poor.", "A", "'heavy' starts with consonant sound /h/."),
        ("Complete the dialogue: Dilip: 'I need ___ scale.' Mahajan: '___ mice ate it!'", "the, The", "a, An", "an, The", "a, A", "A", "'the scale' (specific item borrowed), 'The mice' (specific mice claimed by Mahajan)."),
        ("Select the correct sentence:", "An eagle is a strong bird.", "A eagle is a strong bird.", "The eagle is an strong bird.", "An eagle is an strong bird.", "A", "'An eagle' (vowel sound), 'a strong bird' (consonant sound)."),
        ("Fill in the blank: 'Dilip waited for ___ long time before returning.'", "a", "an", "the", "no article", "A", "Idiomatic expression 'for a long time'."),
        ("Identify where NO article is needed:", "Dilip loved **___ honesty**.", "Dilip saw ___ eagle.", "Dilip carried ___ box.", "Mahajan had ___ son.", "A", "Abstract nouns like 'honesty' generally do not take an article here."),
        ("Choose the correct sentence for story summary:", "Dilip was an honest young boy.", "Dilip was a honest young boy.", "Dilip was the honest a boy.", "Dilip was an honest a boy.", "A", "'an honest' is correct because 'h' is silent."),
        ("Fill in the blanks: 'Dilip spent ___ year in ___ distant land.'", "a, a", "an, an", "the, an", "a, an", "A", "'a year' (/y/ sound), 'a distant land' (/d/ sound)."),
        ("Which sentence uses 'the' correctly for superlative degree?", "Dilip was the smartest boy in the village.", "Dilip was a smartest boy in the village.", "Dilip was an smartest boy in the village.", "Dilip was smartest boy in a village.", "A", "Superlative degree ('smartest') takes 'the'."),
        ("Identify the article error: 'Mahajan gave **a** iron scale to Dilip.'", "'a' should be 'an' or 'the'", "'iron' should be 'a iron'", "'scale' needs 'an'", "No error", "A", "'iron' starts with vowel sound /i/, so it takes 'an' or 'the'."),
        ("Complete: 'It was ___ unusual story about ___ rat and ___ eagle.'", "an, a, an", "a, an, a", "the, the, the", "an, an, an", "A", "an unusual (/u/), a rat (/r/), an eagle (/e/)."),
        ("Choose the correct option: '___ sun set while Dilip reached home.'", "The", "A", "An", "No article", "A", "'The sun' (unique celestial body).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH01_CAT02_Q{idx:02d}"
        qtxt = f"Contextual Article Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Article Usage in Context", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze article usage in: 'Dilip gave **a** iron scale as **a** security.' Correct all errors:", "'a iron' -> 'an iron' (or 'the iron'); 'a security' -> 'security' (uncountable noun).", "'a iron' -> 'a iron'; 'a security' -> 'an security'.", "'a iron' -> 'the iron'; 'a security' -> 'a security'.", "No errors present in the original sentence.", "A", "'iron' begins with vowel sound; 'security' is uncountable here."),
        ("Fill in all three blanks: '___ Mahajan learned that ___ lie cannot hide ___ truth forever.'", "The, a, the", "A, an, a", "An, a, the", "The, the, an", "A", "'The Mahajan' (specific person), 'a lie' (general concept), 'the truth' (abstract specific noun)."),
        ("Identify why 'the' is used in: 'Dilip returned **the** boy to his father.'", "Because 'the boy' refers to the specific boy (Mahajan's son) already introduced in the story.", "Because boy is a proper noun.", "Because eagle carried him.", "Because Mahajan was rich.", "A", "'The' specifies a definite, previously mentioned person."),
        ("Spot the TWO article errors: 'It took **a** hour for **a** eagle to fly away.'", "'a hour' should be 'an hour' and 'a eagle' should be 'an eagle'.", "'a hour' should be 'the hour' and 'a eagle' should be 'a eagle'.", "'a hour' should be 'a hour' and 'a eagle' should be 'the eagle'.", "There are no errors.", "A", "Both 'hour' (silent h) and 'eagle' (vowel e) require 'an'."),
        ("Choose the paragraph with PERFECT article usage throughout:", "Dilip was a poor boy. He had an iron balance. He gave the balance to a Mahajan.", "Dilip was an poor boy. He had a iron balance. He gave a balance to the Mahajan.", "Dilip was the poor boy. He had an iron balance. He gave an balance to a Mahajan.", "Dilip was a poor boy. He had a iron balance. He gave the balance to an Mahajan.", "A", "a poor boy, an iron balance, the balance (second mention), a Mahajan."),
        ("Why is it correct to write 'a European traveler' but 'an eagle'?", "Because 'European' begins with a consonant sound /j/ (yoo), while 'eagle' begins with vowel sound /e/.", "Because Europe is a place.", "Because eagle is an animal.", "Because European has more letters.", "A", "Sound determines article: /yoo/ is a consonant sound."),
        ("Select the option that correctly completes the story moral: '___ honest deed brings ___ good result, while ___ bad action brings regret.'", "An, a, a", "A, an, an", "The, the, the", "An, an, a", "A", "An honest (/o/), a good (/g/), a bad (/b/)."),
        ("Analyze this sentence: 'Dilip went to **the** foreign land.' Why might 'a foreign land' be better here?", "Because it is the first mention of an unspecified foreign country in the story.", "Because foreign land is near the village.", "Because Dilip had already visited it.", "Because land is plural.", "A", "First indefinite mention of an unknown place takes 'a'."),
        ("Correct the sentence: 'An Mahajan wept when an eagle carried his son.'", "A Mahajan wept when an eagle carried his son.", "The Mahajan wept when a eagle carried his son.", "An Mahajan wept when a eagle carried his son.", "A Mahajan wept when a eagle carried his son.", "A", "'Mahajan' starts with consonant /m/, so it takes 'A Mahajan'."),
        ("Fill in the blanks: '___ iron is ___ heavy metal, but ___ scale in this story was made of iron.'", "No article, a, the", "An, a, a", "The, an, the", "A, a, a", "A", "Material noun 'Iron' takes no article in general sense; 'a heavy metal'; 'the scale' (specific scale)."),
        ("Spot the missing article: 'Dilip locked boy in his house until Mahajan apologised.'", "Missing 'the' before 'boy' -> 'locked the boy'", "Missing 'a' before 'house' -> 'in a house'", "Missing 'an' before 'Mahajan'", "No article is missing", "A", "'the boy' is required to specify Mahajan's son."),
        ("HOTS Reasoning: Which sentence uses 'a', 'an', and 'the' correctly in a single rule demonstration?", "An eagle flew over a tree and landed on the roof.", "A eagle flew over an tree and landed on a roof.", "The eagle flew over an tree and landed on an roof.", "An eagle flew over an tree and landed on the roof.", "A", "An eagle (vowel), a tree (consonant), the roof (specific)."),
        ("Rewrite correctly: 'Dilip is a honest boy who told an story to a Mahajan.'", "Dilip is an honest boy who told a story to the Mahajan.", "Dilip is a honest boy who told an story to an Mahajan.", "Dilip is the honest boy who told an story to a Mahajan.", "Dilip is an honest boy who told an story to the Mahajan.", "A", "'an honest', 'a story', 'the Mahajan'."),
        ("Identify the correct rule for using 'the' with body parts or specific objects:", "We use 'the' when referring to specific objects already known to speaker and listener.", "We always use 'an' before objects.", "We never use 'the' with objects.", "We use 'a' for all specific items.", "A", "'The' specifies known/unique items in context.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH01_CAT02_Q{idx:02d}"
        qtxt = f"Higher Order Article Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Article Analysis & Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 3. Calendar & Days Vocabulary (50 Qs)
# ---------------------------------------------------------------------------
def build_calendar_days():
    header = "# Category 3: Calendar, Days & Abbreviations — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    days_months_easy = [
        ("What is the first day of the week?", "Monday", "Sunday", "Saturday", "Friday", "A", "Monday is standard first working day of week."),
        ("What is the correct short abbreviation for **Monday**?", "Mon.", "Mond.", "Mo.", "M.", "A", "Mon. is standard abbreviation."),
        ("Which day comes immediately after Tuesday?", "Wednesday", "Thursday", "Monday", "Friday", "A", "Wednesday comes after Tuesday."),
        ("What is the short abbreviation for **Wednesday**?", "Wed.", "Weds.", "We.", "W.", "A", "Wed. is standard abbreviation."),
        ("How many days are there in a standard week?", "7 days", "5 days", "6 days", "8 days", "A", "A week has 7 days."),
        ("Which month comes first in a calendar year?", "January", "February", "December", "March", "A", "January is the 1st month."),
        ("What is the short abbreviation for **January**?", "Jan.", "Jany.", "Ja.", "Jn.", "A", "Jan. is standard abbreviation."),
        ("Which day comes right before Sunday?", "Saturday", "Friday", "Monday", "Thursday", "A", "Saturday comes before Sunday."),
        ("What is the correct short abbreviation for **August**?", "Aug.", "Augu.", "Au.", "Ag.", "A", "Aug. is standard abbreviation."),
        ("How many months are there in one year?", "12 months", "10 months", "7 months", "14 months", "A", "A year has 12 months."),
        ("Which month comes after October?", "November", "December", "September", "August", "A", "November follows October."),
        ("What is the abbreviation for **December**?", "Dec.", "Dece.", "Dc.", "Dcm.", "A", "Dec. is standard abbreviation."),
        ("If today is Friday, what day was yesterday?", "Thursday", "Saturday", "Wednesday", "Sunday", "A", "Yesterday was Thursday."),
        ("If today is Saturday, what day will tomorrow be?", "Sunday", "Friday", "Monday", "Tuesday", "A", "Tomorrow will be Sunday."),
        ("What is the short abbreviation for **Sunday**?", "Sun.", "Snd.", "Su.", "Sn.", "A", "Sun. is standard abbreviation."),
        ("Which day comes between Wednesday and Friday?", "Thursday", "Tuesday", "Saturday", "Monday", "A", "Thursday is between Wednesday and Friday."),
        ("What is the short abbreviation for **Tuesday**?", "Tue.", "Tues.", "Tu.", "Ts.", "A", "Tue. (or Tues.) is standard abbreviation."),
        ("Which month comes right before July?", "June", "August", "May", "April", "A", "June comes before July.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(days_months_easy, start=1):
        qid = f"BK02_CH01_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Vocabulary & Day Concepts:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Days & Calendar Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Dilip started his journey to the foreign land on **Monday**. He traveled for 4 days. On which day did he arrive?", "Friday", "Thursday", "Saturday", "Wednesday", "A", "Monday + 4 days = Tuesday(1), Wednesday(2), Thursday(3), Friday(4)."),
        ("Dilip returned to his village after 3 years in **March**. Which month comes 2 months after March?", "May", "April", "June", "February", "A", "March + 2 months = April(1), May(2)."),
        ("Match the day with its correct abbreviation: **Thursday**", "Thu. / Thurs.", "Thr.", "Ths.", "Tu.", "A", "Thu. or Thurs. is standard."),
        ("If Dilip met Mahajan on **Wed.** and promised to return 3 days later, what day will that be?", "Saturday", "Friday", "Sunday", "Tuesday", "A", "Wednesday + 3 days = Thursday(1), Friday(2), Saturday(3)."),
        ("Identify the correctly spelt month name:", "February", "Febuary", "Februery", "Febraury", "A", "February is the correct spelling."),
        ("Identify the INCORRECT pair of month and abbreviation:", "September - Sep. / Sept.", "October - Oct.", "November - Nov.", "December - Des.", "D", "December abbreviation is Dec., not Des."),
        ("Dilip locked Mahajan's son on **Friday**. Mahajan returned the scales 2 days later. On which day did Dilip release the boy?", "Sunday", "Saturday", "Monday", "Tuesday", "A", "Friday + 2 days = Saturday(1), Sunday(2)."),
        ("Which month has 28 days (or 29 days in a leap year)?", "February", "January", "March", "April", "A", "February has 28/29 days."),
        ("Rearrange in correct chronological order: Wed, Mon, Tue, Thu", "Mon, Tue, Wed, Thu", "Mon, Wed, Tue, Thu", "Tue, Mon, Wed, Thu", "Thu, Wed, Tue, Mon", "A", "Monday -> Tuesday -> Wednesday -> Thursday."),
        ("What day is 2 days before Tuesday?", "Sunday", "Monday", "Saturday", "Friday", "A", "Tuesday - 2 days = Monday(1), Sunday(2)."),
        ("If Dilip was away for 12 months, how many full years was he away?", "1 year", "2 years", "6 months", "12 years", "A", "12 months = 1 year."),
        ("Select the month that has exactly 30 days:", "April", "January", "March", "May", "A", "April has 30 days (April, June, Sept, Nov)."),
        ("Which abbreviation stands for **Saturday**?", "Sat.", "Satur.", "Sa.", "St.", "A", "Sat. is standard abbreviation."),
        ("If today is **Thu.**, what day will it be after 7 days?", "Thursday", "Friday", "Wednesday", "Sunday", "A", "7 days completes a full week cycle, so it will be Thursday again."),
        ("Dilip's trip lasted from **Jan.** to **Mar.**. How many total months did he travel through?", "3 months (Jan, Feb, Mar)", "2 months", "1 month", "4 months", "A", "January, February, March = 3 months."),
        ("Identify the word that means 'occurring every day':", "Daily", "Weekly", "Monthly", "Yearly", "A", "Daily means every day."),
        ("Which of the following is a weekend day in standard school calendar?", "Sunday", "Monday", "Wednesday", "Thursday", "A", "Sunday is a weekend day."),
        ("Choose the correct abbreviation for **September**:", "Sept. or Sep.", "Spt.", "Septe.", "St.", "A", "Sept. or Sep. is standard.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH01_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Application & Story Timeline:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Calendar & Time Reasoning", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Dilip left his village on **Mon., 1st Jan.** and returned on **Mon., 1st Feb.**. How many days was he away (non-leap year)?", "31 days", "28 days", "30 days", "7 days", "A", "January has 31 days, so 1st Jan to 1st Feb is 31 days."),
        ("Mahajan claimed the mice ate the scales on **Tue.**. Dilip waited 3 days before taking Mahajan's son, and Mahajan apologised 2 days after that. On what day did Mahajan apologise?", "Sunday", "Saturday", "Friday", "Monday", "A", "Tuesday + 3 days = Friday; Friday + 2 days = Sunday."),
        ("Solve the calendar puzzle: If 1st August is a Wednesday, what day of the week will 8th August be?", "Wednesday", "Thursday", "Tuesday", "Friday", "A", "1 + 7 = 8th August, so it falls on the same day (Wednesday)."),
        ("Analyze this schedule: Dilip worked Mon, Wed, Fri. Mahajan worked Tue, Thu, Sat. On which day did NEITHER of them work?", "Sunday", "Monday", "Saturday", "Wednesday", "A", "Sunday is not listed in either work schedule."),
        ("Complete the full series of abbreviations: Mon., Tue., ____, Thu., Fri., ____, Sun.", "Wed., Sat.", "Wed., Sat.", "Weds., Satur.", "We., Sa.", "A", "Wed. and Sat. complete the days of the week abbreviations."),
        ("If Dilip's journey took a fortnight, how many weeks and days did he travel?", "2 weeks (14 days)", "1 week (7 days)", "4 weeks (28 days)", "1 month (30 days)", "A", "A fortnight equals 14 days or 2 weeks."),
        ("Spot the error in the calendar sequence: 'Jan, Feb, Apr, Mar, May, Jun'", "April and March are in wrong order.", "February is in wrong position.", "June should be first.", "No error.", "A", "March comes before April (Jan, Feb, Mar, Apr, May, Jun)."),
        ("Dilip gave security on **30th Nov.** and got it back on **1st Dec.**. How many days later did he get it back?", "1 day later", "30 days later", "2 days later", "7 days later", "A", "November has 30 days, so 1st Dec is the very next day."),
        ("If yesterday was two days before Friday, what day is tomorrow?", "Friday", "Thursday", "Saturday", "Wednesday", "A", "Two days before Friday = Wednesday (yesterday). Today = Thursday. Tomorrow = Friday."),
        ("Calculate: How many days are there in total during the months of **June** and **July** combined?", "61 days (30 + 31)", "60 days", "62 days", "59 days", "A", "June has 30 days, July has 31 days. 30 + 31 = 61 days."),
        ("HOTS Reasoning: Why do we write 'Mon.' with a full stop when abbreviating Monday?", "Because a period/full stop indicates a shortened word abbreviation.", "Because Monday ends with a stop.", "Because it is a question.", "Because Mahajan commanded it.", "A", "Full stop is used to mark standard word abbreviations."),
        ("Identify the correct statement about a leap year:", "A leap year has 366 days and February has 29 days.", "A leap year has 365 days and February has 28 days.", "A leap year has 300 days and March has 20 days.", "A leap year occurs every 2 years.", "A", "Leap year adds 1 day to Feb (29 days total = 366 days)."),
        ("Dilip locked the boy for 48 hours. How many full days is 48 hours?", "2 full days", "1 full day", "3 full days", "4 full days", "A", "24 hours = 1 day. 48 hours = 2 days."),
        ("Which month pair both have 31 days and come right after each other?", "July and August", "June and July", "August and September", "December and January (same year)", "A", "July (31 days) and August (31 days) are consecutive months with 31 days.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH01_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Logic & Mathematical Time Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Calendar & Time Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 4. Action Verbs Identification (50 Qs)
# ---------------------------------------------------------------------------
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_verbs = [
        ("Dilip **wrote** a letter about his iron scales.", "wrote", "Dilip", "letter", "iron", "A", "'wrote' expresses physical/mental action."),
        ("The Mahajan **ran** quickly towards the river.", "ran", "Mahajan", "quickly", "river", "A", "'ran' is the physical action verb."),
        ("An eagle **flew** into the blue sky.", "flew", "eagle", "blue", "sky", "A", "'flew' is the action performed by the eagle."),
        ("The rats **ate** the heavy iron balance.", "ate", "rats", "heavy", "balance", "A", "'ate' is the action verb."),
        ("Dilip **locked** the boy in his house.", "locked", "Dilip", "boy", "house", "A", "'locked' is the action verb."),
        ("The boy **cried** loudly near the river.", "cried", "boy", "loudly", "river", "A", "'cried' is the action verb."),
        ("Dilip **borrowed** money from the Mahajan.", "borrowed", "Dilip", "money", "Mahajan", "A", "'borrowed' is the action verb."),
        ("The Mahajan **apologised** for his lie.", "apologised", "Mahajan", "lie", "for", "A", "'apologised' is the action verb."),
        ("Dilip **returned** to his home village.", "returned", "Dilip", "home", "village", "A", "'returned' is the action verb."),
        ("The boy **followed** Dilip to his house.", "followed", "boy", "Dilip", "house", "A", "'followed' is the action verb."),
        ("Dilip **placed** the scales on the table.", "placed", "Dilip", "scales", "table", "A", "'placed' is the action verb."),
        ("Mahajan **lied** about the iron scales.", "lied", "Mahajan", "about", "scales", "A", "'lied' is the action verb."),
        ("Dilip **carried** a heavy box on his back.", "carried", "Dilip", "heavy", "box", "A", "'carried' is the action verb."),
        ("The birds **sang** in the morning.", "sang", "birds", "morning", "in", "A", "'sang' is the action verb."),
        ("Dilip **earned** money in the foreign land.", "earned", "Dilip", "money", "foreign", "A", "'earned' is the action verb."),
        ("The Mahajan **wept** in sadness.", "wept", "Mahajan", "sadness", "in", "A", "'wept' is the action verb."),
        ("Dilip **asked** the boy to come along.", "asked", "Dilip", "boy", "along", "A", "'asked' is the action verb."),
        ("The boy **walked** slowly to the river.", "walked", "boy", "slowly", "river", "A", "'walked' is the action verb.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_verbs, start=1):
        qid = f"BK02_CH01_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in this sentence from or related to Chapter 01:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Action Verb Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Which of the following words from the sentence is an **action verb**? 'Dilip **quietly** **walked** to the **big** **market**.'", "walked", "quietly", "big", "market", "A", "'walked' shows physical action; 'quietly' is adverb, 'big' is adjective, 'market' is noun."),
        ("Identify BOTH action verbs in: 'Dilip **went** home and **locked** the door.'", "went, locked", "Dilip, home", "door, went", "locked, door", "A", "'went' and 'locked' are both action verbs."),
        ("What is the past tense action verb of 'eat' as used in the story title (*The Rats Who Ate the Iron Balance*)?", "ate", "eaten", "eating", "eats", "A", "'ate' is the past tense action verb."),
        ("Choose the sentence where the underlined word is used as an ACTION VERB:", "Dilip will **fly** to the foreign land.", "The **fly** sat on the iron scale.", "Eagle is a fast **fly**.", "There was a **fly** in the milk.", "A", "In (A), 'fly' acts as the main action verb."),
        ("Find the action verb in: 'Mahajan gave Dilip a small pouch of coins.'", "gave", "Mahajan", "small", "pouch", "A", "'gave' is the action performed by Mahajan."),
        ("Which sentence contains NO action verb?", "Mahajan was greedy.", "Mahajan hid the scales.", "Dilip traveled abroad.", "The eagle carried the boy.", "A", "'Mahajan was greedy' contains linking verb 'was', but no physical action verb."),
        ("Change the action verb 'run' to past tense: 'Dilip (run) to Mahajan's house.'", "ran", "runned", "running", "runs", "A", "Past tense of run is ran."),
        ("Identify the action verb: 'The eagle swooped down and caught the mouse.'", "swooped, caught", "eagle, down", "mouse, swooped", "down, caught", "A", "'swooped' and 'caught' are action verbs."),
        ("Select the action verb that completes the sentence: 'Dilip ____ his scales back from Mahajan.'", "demanded", "honest", "heavy", "greedy", "A", "'demanded' is an action verb."),
        ("Which word is an action verb? (scales, Mahajan, returned, iron)", "returned", "scales", "Mahajan", "iron", "A", "'returned' is an action verb; others are nouns/adjectives."),
        ("What action did Mahajan perform when he realized his mistake?", "apologised", "greedy", "scales", "boy", "A", "Mahajan apologised (action verb)."),
        ("Identify the action verb in: 'Dilip thought of a clever plan.'", "thought", "Dilip", "clever", "plan", "A", "'thought' is a mental action verb."),
        ("Choose the correct action verb: 'The rats ____ through the wooden box.'", "chewed", "chewable", "chewy", "teeth", "A", "'chewed' is the action verb."),
        ("Identify the action verb in: 'The boy smiled at Dilip.'", "smiled", "boy", "at", "Dilip", "A", "'smiled' is the action verb."),
        ("Which of these words is NOT an action verb? (jump, speak, gold, carry)", "gold", "jump", "speak", "carry", "A", "'gold' is a noun/adjective; others are action verbs."),
        ("Identify the action verb in: 'Mahajan searched everywhere for his son.'", "searched", "Mahajan", "everywhere", "son", "A", "'searched' is the action verb."),
        ("Fill in the blank with an appropriate action verb: 'The eagle ____ into the clouds.'", "vanished", "sky", "blue", "high", "A", "'vanished' is an action verb."),
        ("What action verb completes the sentence? 'Dilip ____ money for his travel.'", "saved", "rich", "coin", "road", "A", "'saved' is an action verb.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH01_CAT04_Q{idx:02d}"
        qtxt = f"Action Verb Grammar Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Action Verb Context & Tense", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence: 'The greedy Mahajan lied to Dilip about the heavy scales.' How many total ACTION VERBS are present?", "1 action verb ('lied')", "2 action verbs", "3 action verbs", "0 action verbs", "A", "'lied' is the single action verb. 'greedy' and 'heavy' are adjectives."),
        ("Categorize the verbs: In 'Dilip **was** poor, so he **borrowed** money', classify 'was' and 'borrowed'.", "'was' is a linking verb; 'borrowed' is an action verb.", "Both are action verbs.", "Both are linking verbs.", "'was' is action; 'borrowed' is linking.", "A", "'was' links state of being; 'borrowed' shows action."),
        ("Replace the weak verb with a strong action verb: 'Dilip **went quickly** to Mahajan's house.'", "Dilip **rushed** to Mahajan's house.", "Dilip **was** at Mahajan's house.", "Dilip **walked slow** to house.", "Dilip **saw** Mahajan's house.", "A", "'rushed' is a stronger, vivid action verb than 'went quickly'."),
        ("Identify the sentence with THREE distinct action verbs:", "Dilip **entered** the shop, **bought** scales, and **left** happy.", "Dilip was honest, smart, and poor.", "The Mahajan lied about rats eating iron.", "An eagle flew high in the sky.", "A", "entered, bought, left are 3 distinct action verbs."),
        ("Differentiate verb types: Which underlined word is an ACTION verb?", "Dilip **locked** the door.", "Dilip is **happy**.", "The scales were **heavy**.", "Mahajan was **greedy**.", "A", "'locked' is a physical action verb."),
        ("Spot the incorrect verb tense: 'Dilip **return** from the foreign land yesterday.' Correct it:", "'return' should be 'returned' (past action verb).", "'return' should be 'returning'.", "'return' should be 'returns'.", "'return' should be 'will return'.", "A", "Past time indicator 'yesterday' requires past tense action verb 'returned'."),
        ("Form an action chain: Rearrange the story action verbs in correct order of occurrence: (apologised, borrowed, locked, returned)", "borrowed -> returned -> locked -> apologised", "apologised -> locked -> returned -> borrowed", "returned -> borrowed -> apologised -> locked", "locked -> apologised -> borrowed -> returned", "A", "First Dilip borrowed money, then returned from abroad, locked the boy, and Mahajan apologised."),
        ("Identify the verb error in dialogue: Mahajan said, 'An eagle **eated** my son!'", "'eated' is incorrect; the past tense action verb is 'ate' or 'has taken'.", "'eated' should be 'eaten'.", "'eated' should be 'eats'.", "No error.", "A", "'eat' is irregular; its past tense is 'ate', not 'eated'."),
        ("Analyze this sentence: 'Dilip **whispered** a secret to the boy.' What type of action verb is 'whispered'?", "Vocal/Speech action verb", "Physical movement verb", "Linking verb", "State of being verb", "A", "'whispered' is an action verb of speech/sound."),
        ("Which sentence uses action verbs to show cause and effect?", "Mahajan **lied**, so Dilip **tricked** him.", "Mahajan was rich and Dilip was poor.", "The scales were made of heavy iron.", "An eagle is a big bird.", "A", "'lied' (cause action) -> 'tricked' (effect action)."),
        ("Spot the missing action verb: 'The eagle ____ through the air and ____ the boy.'", "soared, grabbed", "big, heavy", "was, was", "quick, slow", "A", "'soared' and 'grabbed' complete the sentence with vivid actions."),
        ("HOTS Reasoning: Why is 'understood' in 'Dilip understood the lie' considered a MENTAL action verb?", "Because it describes an active thought process in the mind without outer movement.", "Because Dilip spoke out loud.", "Because understanding requires iron.", "Because it is an adjective.", "A", "Mental action verbs describe internal cognitive actions."),
        ("Transform the action verb to future tense: 'Dilip **teaches** Mahajan a lesson.'", "Dilip **will teach** Mahajan a lesson.", "Dilip **taught** Mahajan a lesson.", "Dilip **is teaching** Mahajan a lesson.", "Dilip **teach** Mahajan a lesson.", "A", "'will teach' expresses future action."),
        ("Identify the sentence where the action verb matches the plural subject:", "The rats **eat** the scales.", "The rats **eats** the scales.", "The rat **eat** the scales.", "The rats **is eating** the scales.", "A", "Plural subject 'rats' takes base verb 'eat' in simple present.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH01_CAT04_Q{idx:02d}"
        qtxt = f"Higher Order Action Verb Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Action Verb Classification & Tense Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 5. Punctuation Marks (50 Qs)
# ---------------------------------------------------------------------------
def build_punctuation_marks():
    header = "# Category 5: Punctuation Marks & Capitalization — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_punct = [
        ("What punctuation mark should be placed at the end of a telling sentence like: 'Dilip returned to his village__'", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "Comma (,)", "A", "A telling sentence (statement) ends with a full stop."),
        ("Which mark is used at the end of an asking sentence: 'Where are my iron scales__'", "Question mark (?)", "Full stop (.)", "Comma (,)", "Exclamation mark (!)", "A", "An asking sentence (question) ends with a question mark."),
        ("Which letter should ALWAYS be capitalized in a proper noun like a person's name?", "The first letter (e.g., Dilip)", "The last letter", "All letters", "No letters", "A", "First letter of proper nouns must be capitalized."),
        ("Identify the punctuation mark used to separate items in a list: 'Dilip bought scales__ coins__ and food.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Hyphen (-)", "A", "Commas separate items in a list."),
        ("Which punctuation mark shows sudden strong feeling: 'What a terrible lie__'", "Exclamation mark (!)", "Full stop (.)", "Comma (,)", "Question mark (?)", "A", "Exclamation marks express strong emotion."),
        ("Select the proper noun that MUST start with a capital letter:", "Dilip", "boy", "scales", "village", "A", "'Dilip' is a proper name requiring capital 'D'."),
        ("Which of the following is the symbol for a **full stop**?", ".", "?", "!", ",", "A", "Period/full stop is '.'"),
        ("Which of the following is the symbol for a **question mark**?", "?", ".", "!", ",", "A", "Question mark is '?'"),
        ("Which of the following is the symbol for an **exclamation mark**?", "!", "?", ".", ",", "A", "Exclamation mark is '!'"),
        ("Which word in this sentence should start with a CAPITAL letter? 'the boy went to foreign land.'", "the -> The", "boy -> Boy", "foreign -> Foreign", "land -> Land", "A", "The first word of a sentence must start with a capital letter."),
        ("What punctuation mark goes in the box? 'Mahajan lied to Dilip [ ]'", "Full stop (.)", "Question mark (?)", "Comma (,)", "Exclamation mark (!)", "A", "Full stop ends the statement."),
        ("Which name is capitalized correctly?", "Mahajan", "mahajan", "mAhaJan", "mahajaN", "A", "Capital 'M' for proper name Mahajan."),
        ("What mark goes after a greeting like: 'Dear Father__'", "Comma (,)", "Question mark (?)", "Full stop (.)", "Exclamation mark (!)", "A", "Comma follows letter greetings."),
        ("Identify the correct capital letter for the pronoun 'I': 'dilip said, \"i am honest.\"'", "I", "i", "i'm", "I'm", "A", "The standalone pronoun 'I' is always capitalized."),
        ("Which option shows a sentence ending correctly?", "Dilip locked the boy.", "Dilip locked the boy?", "Dilip locked the boy,", "Dilip locked the boy;", "A", "Full stop at end of simple statement."),
        ("What mark is used in contractions like 'didn**'**t'?", "Apostrophe (')", "Comma (,)", "Full stop (.)", "Hyphen (-)", "A", "Apostrophe replaces omitted letters."),
        ("Which book title is capitalized correctly?", "My Book of English", "my book of english", "My book Of english", "MY BOOK OF english", "A", "Major words in titles are capitalized."),
        ("What punctuation mark is used around spoken words: '___The mice ate it!___'", "Quotation marks / Speech marks ( \" \" )", "Parentheses ( )", "Full stops ( . . )", "Commas ( , , )", "A", "Speech marks enclose spoken dialogue.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_punct, start=1):
        qid = f"BK02_CH01_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Punctuation & Capitalization Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Identify the sentence with CORRECT capitalization and punctuation:", "Dilip went to the Mahajan's house on Monday.", "dilip went to the mahajan's house on monday.", "Dilip went to the mahajan's house on monday?", "dilip Went To The Mahajan's House On Monday.", "A", "Dilip (name), Mahajan's (title), Monday (day of week) capitalized; ends with full stop."),
        ("Which sentence is punctuated as a CORRECT question?", "How can mice eat heavy iron scales?", "How can mice eat heavy iron scales.", "How can mice eat heavy iron scales!", "How can mice eat heavy iron scales,", "A", "Question starting with 'How' ends with question mark ?"),
        ("Spot the capitalization mistake in: 'dilip met mahajan near the River.'", "'dilip' and 'mahajan' should be capitalized ('Dilip', 'Mahajan'), 'River' should be lowercase.", "'River' should be capitalized only.", "'met' should be capitalized.", "No mistake.", "A", "Names of people must be capitalized; common noun river is lowercase here."),
        ("Choose the correctly punctuated dialogue sentence:", "\"An eagle carried away your son,\" said Dilip.", "an eagle carried away your son said dilip.", "\"An eagle carried away your son\" said Dilip", "An eagle carried away your son, said dilip.", "A", "Quotation marks around spoken words, comma inside quote, capital Dilip."),
        ("Identify where a COMMA is missing: 'Dilip took scales money and food.'", "Between 'scales' and 'money' ('scales, money')", "After 'Dilip'", "After 'food'", "No comma needed", "A", "Commas separate items in list: 'scales, money and food'."),
        ("Which sentence uses the apostrophe correctly for possession?", "This is Mahajan's iron balance.", "This is Mahajans' iron balance.", "This is Mahajans iron balance.", "This is Mahajan's' iron balance.", "A", "Mahajan's indicates possession by Mahajan."),
        ("Select the sentence with CORRECT punctuation for an exclamatory statement:", "What a clever trick Dilip played!", "What a clever trick Dilip played?", "What a clever trick Dilip played.", "What a clever trick Dilip played,", "A", "Exclamatory sentence starting with 'What a...' ends with !"),
        ("Which contraction is written correctly for 'did not'?", "didn't", "did'nt", "didnt'", "d'idnt", "A", "Apostrophe replaces the 'o' in not -> didn't."),
        ("Find the sentence with NO capitalization errors:", "Panchatantra stories teach us valuable moral lessons.", "panchatantra stories teach us valuable moral lessons.", "Panchatantra Stories Teach Us Valuable Moral Lessons.", "panchatantra Stories teach us valuable moral Lessons.", "A", "'Panchatantra' capitalized as proper name; rest lower case except start of sentence."),
        ("What punctuation mark belongs in the blank? 'Mahajan cried out, \"Help__ My son is gone!\"'", "!", ".", "?", ",", "A", "Exclamation mark ! expresses urgent distress."),
        ("Choose the correct form for 'cannot':", "can't", "ca'nt", "cant'", "c'ant", "A", "can't is the standard contraction."),
        ("Identify the punctuation error: 'Dilip returned after three years, he paid back the money.'", "Comma splice between two independent clauses (should be a full stop or 'and').", "Missing question mark.", "Missing capital letters.", "No error.", "A", "Two complete sentences separated only by comma."),
        ("Select the sentence with proper use of capital letters for days and months:", "Dilip left on Monday in January.", "Dilip left on monday in january.", "Dilip left on Monday in january.", "Dilip left on monday in January.", "A", "Both Monday (day) and January (month) must be capitalized."),
        ("Which sentence correctly uses an apostrophe for contraction of 'is'?", "Dilip's going to the market.", "Dilips' going to the market.", "Dilips going to the market.", "Dilip'es going to the market.", "A", "Dilip's = Dilip is."),
        ("Identify the correct punctuation for a list of names: 'The characters are ____'", "Dilip, Mahajan, and his son.", "Dilip Mahajan and his son.", "Dilip; Mahajan; and his son.", "Dilip: Mahajan: and his son.", "A", "Commas separate items in list."),
        ("Choose the sentence that correctly asks a question about the story:", "Why did Mahajan tell a lie?", "Why did Mahajan tell a lie.", "Why did Mahajan tell a lie!", "why did Mahajan tell a lie.", "A", "Capital W, question mark at end."),
        ("Fix the sentence: 'where is dilips iron balance'", "Where is Dilip's iron balance?", "Where is dilips iron balance.", "where is Dilip's iron balance!", "Where is Dilips' iron balance?", "A", "Capital W, capital D, apostrophe for Dilip's, ends with ?"),
        ("Which of these sentences is punctuated PERFECTLY?", "Dilip asked, \"Can mice eat iron?\"", "Dilip asked \"can mice eat iron?\"", "dilip asked, \"Can mice eat iron?\"", "Dilip asked, \"Can mice eat iron.\"", "A", "Capital D, comma after asked, speech marks around question with ? inside.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH01_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Context Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Punctuation Application & Dialogue Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze and count ALL capitalization and punctuation errors in: 'on monday dilip went to mahajans house and said, where are my scales'", "5 errors (on->On, monday->Monday, dilip->Dilip, mahajans->Mahajan's, missing quotes & question mark)", "2 errors", "3 errors", "7 errors", "A", "Starts sentence, day name, person name, possessive apostrophe, quotation marks & question mark."),
        ("Correct the entire dialogue paragraph: 'mahajan yelled how can an eagle carry a boy dilip replied the same way mice can eat iron'", "\"How can an eagle carry a boy?\" yelled Mahajan. Dilip replied, \"The same way mice can eat iron.\"", "mahajan yelled \"how can an eagle carry a boy?\" dilip replied \"the same way mice can eat iron.\"", "Mahajan yelled, How can an eagle carry a boy? Dilip replied, The same way mice can eat iron.", "\"How can an eagle carry a boy!\" Yelled Mahajan. Dilip replied \"The same way mice can eat iron?\"", "A", "Full proper quotation, dialogue tags, capitalization, and terminal punctuation."),
        ("Distinguish between possessive 's and contraction 's: 'Dilip**'**s scale is heavy, and he**'**s going home.'", "First 's is possessive (scale belonging to Dilip); second 's is contraction (he is).", "Both are possessive.", "Both are contractions.", "First is contraction; second is possessive.", "A", "Dilip's scale = scale of Dilip (possessive); he's = he is (contraction)."),
        ("Spot the subtle punctuation flaw in this dialogue: '\"The mice ate your scales,\" Lied Mahajan.'", "'Lied' should be lowercase 'lied' because it continues the dialogue tag outside quotation marks.", "'The' should be lowercase.", "Commas should be outside quotes.", "No flaw.", "A", "Dialogue tags following quotes start with lowercase unless proper nouns."),
        ("Which sentence correctly uses punctuation to show contrast?", "Mahajan was rich, but Dilip was honest.", "Mahajan was rich but, Dilip was honest.", "Mahajan was rich but Dilip was honest!", "Mahajan was rich; but Dilip was honest?", "A", "Comma before coordinating conjunction 'but' joining two independent clauses."),
        ("Reconstruct with perfect punctuation: 'dilip took mahajans son to the river on tuesday 5th january'", "Dilip took Mahajan's son to the river on Tuesday, 5th January.", "dilip took mahajans son to the river on tuesday, 5th january.", "Dilip took Mahajans' son to the river on Tuesday 5th January", "Dilip took Mahajan's son to river on tuesday 5th january.", "A", "Dilip, Mahajan's, Tuesday, 5th January, period."),
        ("Identify why exclamation mark is necessary here: '\"Help! An eagle took my son!\"'", "Because Mahajan is shouting in panic and distress.", "Because eagle is flying.", "Because son is heavy.", "Because sentence is long.", "A", "Exclamation mark communicates intense emotion/panic."),
        ("Choose the correctly punctuated sentence containing an appositive phrase:", "Dilip, a poor young man, traveled to a foreign land.", "Dilip a poor young man traveled to a foreign land.", "Dilip, a poor young man traveled to a foreign land.", "Dilip a poor young man, traveled to a foreign land.", "A", "Appositive phrase 'a poor young man' is set off by commas on both sides."),
        ("Analyze the use of hyphen in: 'The twenty-one year old boy travelled far.'", "Hyphen joins compound numbers (twenty-one).", "Hyphen replaces comma.", "Hyphen indicates question.", "Hyphen is an apostrophe.", "A", "Compound numbers from twenty-one to ninety-nine take hyphens."),
        ("Identify the correct sentence with direct speech quote within text:", "Mahajan claimed, \"Mice ate the scales,\" which was a lie.", "Mahajan claimed \"Mice ate the scales\" which was a lie.", "Mahajan claimed, 'Mice ate the scales,' which was a lie.", "Mahajan claimed: \"Mice ate the scales\" which was a lie.", "A", "Comma before quote, double quotation marks around direct speech, comma inside quote."),
        ("Spot the missing apostrophe: 'The eagles nest was high up in the mountains.'", "Missing apostrophe in 'eagle's' -> 'The eagle's nest'", "Missing apostrophe in 'mountains''", "Missing apostrophe in 'was''", "No apostrophe needed", "A", "'eagle's nest' requires possessive apostrophe."),
        ("HOTS Reasoning: Why does putting a comma in different places change meaning? Compare: 'Dilip, said Mahajan, is honest.' vs 'Dilip said, \"Mahajan is honest.\"'", "The first means Mahajan called Dilip honest; the second means Dilip called Mahajan honest.", "Both mean the exact same thing.", "The first is a question; the second is a command.", "Commas do not affect meaning.", "A", "Punctuation changes the speaker and subject of attribution."),
        ("Correct all 4 errors in: 'whats the matter asked mahajan'", "\"What's the matter?\" asked Mahajan.", "whats the matter? asked mahajan.", "\"What's the matter.\" asked Mahajan.", "\"whats the matter?\" Asked Mahajan.", "A", "Quotation marks, capital W, apostrophe in What's, question mark, capital M."),
        ("Identify the rule for capitalizing titles of respect like 'Mahajan' or 'King':", "Titles used as proper names or before proper names are capitalized.", "Titles are never capitalized.", "Titles are capitalized only at end of sentence.", "Titles must be written in ALL CAPS.", "A", "Titles used as proper names or before names take capital initial.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH01_CAT05_Q{idx:02d}"
        qtxt = f"Higher Order Punctuation Analysis & Dialogue Formatting:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Punctuation & Dialogue Editing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 6. Phonics & Vowel Digraphs (50 Qs)
# ---------------------------------------------------------------------------
def build_phonics_digraphs():
    header = "# Category 6: Phonics & Vowel Digraphs — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_phonics = [
        ("Which vowel digraph is present in the story word **'eat'** (in *The Rats Who Ate the Iron Balance*)?", "ea", "ee", "ai", "ou", "A", "'ea' is the vowel digraph in eat."),
        ("Identify the vowel digraph in the word **'heavy'**:", "ea", "ee", "oa", "ui", "A", "'ea' forms the short /e/ vowel sound in heavy."),
        ("Which word from the story contains the **'ee'** vowel digraph?", "greedy", "scale", "iron", "boy", "A", "'greedy' contains the 'ee' digraph."),
        ("Identify the vowel digraph in the word **'house'**:", "ou", "ow", "oi", "oo", "A", "'ou' is the vowel digraph in house."),
        ("Which vowel digraph appears in the word **'rain'**?", "ai", "ay", "ea", "oa", "A", "'ai' makes the long /a/ sound in rain."),
        ("Find the word with the **'oo'** vowel digraph: 'Dilip was a poor boy.'", "poor", "Dilip", "was", "boy", "A", "'poor' contains the 'oo' digraph."),
        ("Which word from the story rhymes with **'scales'**?", "tales", "rats", "boys", "eagles", "A", "'tales' rhymes with 'scales'."),
        ("Which word from the story rhymes with **'boy'**?", "toy", "bay", "buy", "bow", "A", "'toy' rhymes with 'boy'."),
        ("Identify the vowel digraph in the word **'boat'**:", "oa", "ou", "ow", "oo", "A", "'oa' makes the long /o/ sound in boat."),
        ("Which word from the story rhymes with **'rat'**?", "cat", "rot", "run", "red", "A", "'cat' rhymes with 'rat'."),
        ("Identify the vowel digraph in **'paid'**:", "ai", "ay", "ea", "ia", "A", "'ai' is the vowel digraph in paid."),
        ("Which word from Chapter 01 has the **'ea'** digraph making a long /e/ sound?", "scales", "eagle", "balance", "money", "B", "'eagle' has 'ea' making long /e/ sound."),
        ("Which word rhymes with **'lie'**?", "sky", "lay", "low", "lee", "A", "'sky' rhymes with 'lie'."),
        ("Identify the vowel digraph in **'clever'**:", "er (vowel-r blend)", "ea", "ou", "ai", "A", "'er' forms R-controlled vowel sound."),
        ("Which word from the story has the long /i/ sound spelled with **'igh'**?", "high", "huge", "heavy", "house", "A", "'igh' in high makes long /i/ sound."),
        ("Find the word with **'ou'** digraph: 'Dilip found his scales.'", "found", "Dilip", "his", "scales", "A", "'found' contains 'ou' digraph."),
        ("Which word rhymes with **'day'**?", "away", "die", "due", "door", "A", "'away' rhymes with 'day'."),
        ("Identify the silent letter in the word **'know'** (as in 'Dilip did not know'):", "k", "n", "o", "w", "A", "Initial 'k' before 'n' is silent.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_phonics, start=1):
        qid = f"BK02_CH01_CAT06_Q{idx:02d}"
        qtxt = f"Phonics & Vowel Digraph Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Vowel Digraphs & Rhyming Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Compare the **'ea'** digraph sound in **'eagle'** and **'heavy'**. What is the difference?", "'eagle' has long /e/ sound; 'heavy' has short /e/ sound.", "Both have short /e/ sound.", "Both have long /a/ sound.", "'eagle' has short /e/; 'heavy' has long /e/.", "A", "'ea' can make long /e/ (eagle) or short /e/ (heavy)."),
        ("Select the word pair from Chapter 01 that has the SAME vowel digraph sound:", "paid - rain", "house - poor", "heavy - eagle", "boy - rat", "A", "'paid' and 'rain' both have 'ai' long /a/ sound."),
        ("Which word contains a SILENT letter? (scales, honest, rat, boy)", "honest", "scales", "rat", "boy", "A", "'honest' has silent initial 'h'."),
        ("Identify the odd one out based on vowel sound: (eat, seat, heat, head)", "head", "eat", "seat", "heat", "A", "'head' has short /e/ sound; others have long /e/ sound."),
        ("Which digraph completes the word for Mahajan's emotion? 'asham__d'", "e", "ea", "ai", "ou", "A", "'ashamed' ends with -ed."),
        ("Group these story words by digraph: **found**, **out**, **house**. What digraph do they all share?", "ou", "ow", "oo", "oi", "A", "All share 'ou' making /ow/ diphthong sound."),
        ("Find the word with consonant digraph **'th'** from the story: 'Dilip gave **this** heavy balance.'", "this", "heavy", "gave", "balance", "A", "'this' contains voiced 'th' consonant digraph."),
        ("Which of these words has the **'oa'** vowel digraph? (boat, coat, float, all of these)", "all of these", "boat", "coat", "float", "A", "boat, coat, float all share 'oa' long /o/ sound."),
        ("Identify the vowel digraph in **'foreign'**:", "ei", "or", "ig", "gn", "A", "'ei' is the vowel digraph."),
        ("Which word from the story has a silent **'l'**? (talk, walk, scales, half)", "talk / walk / half", "scales", "iron", "boy", "A", "words like walk, talk, half have silent 'l'."),
        ("Select the word that rhymes with **'scales'** and fits the sentence: 'Dilip carried heavy ____.'", "mails", "mice", "boys", "rats", "A", "'mails' rhymes with 'scales'."),
        ("Identify the digraph in **'screamed'**:", "ea", "ee", "ai", "oa", "A", "'ea' makes long /e/ sound."),
        ("Which word has the short /u/ sound made by **'ou'**? (country, house, out, shout)", "country", "house", "out", "shout", "A", "'country' has short /u/ sound with 'ou'."),
        ("Find the R-controlled vowel sound in: 'Dilip went to earn **money**.'", "er / or / ar sound", "ea", "ou", "ai", "A", "vowel sounds modified by r/n."),
        ("Which word contains the **'oi'** diphthong/digraph? (coin, boy, scale, rat)", "coin", "boy", "scale", "rat", "A", "'coin' contains 'oi'."),
        ("Identify the soft **'c'** sound in Chapter 01 vocabulary: (scales, city, cat, carried)", "city", "scales", "cat", "carried", "A", "'city' has soft /s/ sound for 'c'; others have hard /k/ sound."),
        ("Which word has a hard **'g'** sound? (greedy, village, magic, age)", "greedy", "village", "magic", "age", "A", "'greedy' has hard /g/ sound; others have soft /j/ sound."),
        ("Choose the correct spelling with **'ea'** digraph for feeling guilty:", "ashamed", "ashamed", "ashamed", "ashamed", "A", "ashamed contains standard vowel structure.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH01_CAT06_Q{idx:02d}"
        qtxt = f"Phonics Analysis & Sound Pattern Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Phonic Rules & Sound Discrimination", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the phonics rule: Why does 'c' in **'city'** sound like /s/, but 'c' in **'scales'** sounds like /k/?", "Because 'c' followed by 'i', 'e', or 'y' makes soft /s/ sound; before 'a', 'o', 'u', or consonants it makes hard /k/ sound.", "Because city is a place.", "Because scales are iron.", "Because city is capitalized.", "A", "Soft 'c' rule: c + i, e, y = /s/ sound."),
        ("Categorize the 'ea' digraphs into long /e/ vs short /e/: (eagle, heavy, eat, lead [metal], real)", "Long /e/: eagle, eat, real; Short /e/: heavy, lead [metal]", "All are long /e/.", "All are short /e/.", "Long /e/: heavy; Short /e/: eagle", "A", "eagle, eat, real make long /e/; heavy, lead (metal) make short /e/."),
        ("Identify the word pair where SILENT letters exist in BOTH words:", "honest - know", "rat - boy", "scales - eagle", "house - river", "A", "'honest' (silent h) and 'know' (silent k)."),
        ("Decode the phonics blend: Which word contains a 3-letter consonant blend at the start?", "screamed", "scales", "flew", "locked", "A", "'scr' in screamed is a 3-letter initial consonant blend."),
        ("Examine the hard vs soft 'g' rule: Why is 'g' soft in **'village'** but hard in **'greedy'**?", "'g' followed by 'e', 'i', or 'y' usually makes soft /j/ sound (village); 'g' before 'r' or 'a','o','u' makes hard /g/ sound (greedy).", "Because village has two l's.", "Because greedy describes Mahajan.", "There is no rule.", "A", "Soft 'g' rule: g + e, i, y = /j/ sound."),
        ("Find the word with BOTH a vowel digraph AND a silent letter:", "eagle", "rat", "boy", "box", "A", "'eagle' has 'ea' digraph and silent final 'e'."),
        ("Differentiate diphthongs: Which pair produces the /ow/ sound as in **'house'**?", "house - out", "boy - coin", "rain - day", "boat - coat", "A", "'house' and 'out' share /ow/ diphthong sound."),
        ("Analyze homophones: 'Dilip spent one year at **sea** / **see**.' Which word is the correct homophone for the ocean?", "sea", "see", "si", "seey", "A", "'sea' (ocean) and 'see' (look) are homophones; 'sea' means ocean."),
        ("Identify the phonic pattern in **'weight'** (related to scales): What letters make the long /a/ sound?", "eigh", "ei", "gh", "ht", "A", "'eigh' four-letter combination makes long /a/ sound."),
        ("Sort by ending sound: Which word ends with the /iz/ sound? (boxes, rats, boys, scales)", "boxes", "rats", "boys", "scales", "A", "Plurals ending in -x add -es pronounced /iz/ (boxes)."),
        ("Spot the word where 'gh' is SILENT: (night, high, light, all of these)", "all of these", "night", "high", "light", "A", "'gh' is silent in night, high, light."),
        ("HOTS Reasoning: Why do 'fair' and 'fare' sound identical but have different spellings and meanings?", "They are homophones (same sound, different spelling/meaning).", "They are synonyms.", "They are antonyms.", "They are plurals.", "A", "Homophones share pronunciation but differ in origin/spelling/meaning."),
        ("Identify the compound word from story concepts containing two simple words:", "footprint / workshop", "Mahajan", "Panchatantra", "village", "A", "footprint = foot + print; workshop = work + shop."),
        ("Determine the syllable count and stress: How many syllables are in **'Panchatantra'**?", "4 syllables (Pan-cha-tan-tra)", "2 syllables", "3 syllables", "5 syllables", "A", "Pan-cha-tan-tra has 4 distinct syllables.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH01_CAT06_Q{idx:02d}"
        qtxt = f"Higher Order Phonics & Orthographic Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Phonetic Rules & Homophone Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 7. Question Words & Interrogatives (50 Qs)
# ---------------------------------------------------------------------------
def build_question_words():
    header = "# Category 7: Question Words & Interrogatives — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_qwords = [
        ("___ borrowed money to travel to a foreign land?", "Who", "What", "Where", "Why", "A", "'Who' asks about a person (Dilip)."),
        ("___ did Dilip give to the Mahajan as security?", "What", "Who", "Where", "When", "A", "'What' asks about an object (iron scales)."),
        ("___ did Dilip go to earn money?", "Where", "Who", "What", "Why", "A", "'Where' asks about a location (foreign land)."),
        ("___ did the Mahajan refuse to return the scales?", "Why", "Who", "Where", "What", "A", "'Why' asks about a reason (greed)."),
        ("___ did Dilip lock in his house?", "Whom", "Where", "Why", "When", "A", "'Whom' / 'Who' asks about person (Mahajan's son)."),
        ("___ carried away Mahajan's son according to Dilip's story?", "What", "Who", "Where", "Why", "A", "'What' / 'Which bird' asks about eagle."),
        ("___ did the Mahajan feel when he realized his lie?", "How", "Who", "Where", "What", "A", "'How' asks about feeling/condition (ashamed)."),
        ("___ did Dilip return to his village?", "When", "Who", "Where", "What", "A", "'When' asks about time (after a few years)."),
        ("___ scales were stolen according to Mahajan?", "Whose", "Who", "Where", "Why", "A", "'Whose' asks about possession."),
        ("___ mice did Mahajan claim ate the iron scales?", "How many", "Who", "Where", "Why", "A", "'How many' asks about quantity."),
        ("___ reaction did Dilip show when Mahajan lied?", "What", "Who", "Where", "Why", "A", "'What' asks about action/reaction."),
        ("___ path did Dilip take with Mahajan's son?", "Which", "Who", "Why", "When", "A", "'Which' chooses among options."),
        ("___ story is 'The Rats Who Ate the Iron Balance'?", "Which", "Who", "Where", "Why", "A", "'Which' asks about specific story type (Panchatantra)."),
        ("___ did Mahajan apologize to Dilip?", "Why", "Who", "Where", "What", "A", "'Why' asks for moral reason."),
        ("___ did Dilip take the boy?", "Where", "Who", "What", "Why", "A", "'Where' asks about location (to his house)."),
        ("___ was the iron scales?", "How heavy", "Who", "Where", "Why", "A", "'How heavy' asks about weight."),
        ("___ did Dilip do after hearing Mahajan's lie?", "What", "Who", "Where", "Why", "A", "'What' asks about action."),
        ("___ moral did Mahajan learn?", "What", "Who", "Where", "Why", "A", "'What' asks about moral lesson.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_qwords, start=1):
        qid = f"BK02_CH01_CAT07_Q{idx:02d}"
        qtxt = f"Choose the correct **question word** (Who, What, Where, Why, How, When):\n\n\"{q_blank} _____?\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Question Word Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Match question to answer: Question: '___ did Mahajan lie?' Answer: 'Because he was greedy.'", "Why", "What", "Where", "Who", "A", "'Why' asks for reasons ('Because...')."),
        ("Match question to answer: Question: '___ was the iron balance kept?' Answer: 'In Mahajan's house.'", "Where", "Who", "Why", "When", "A", "'Where' asks for location."),
        ("Choose the correct question word for TIME: '___ did Dilip pay back the borrowed money?'", "When", "Where", "Who", "Why", "A", "'When' inquires about time."),
        ("Form an asking sentence: 'Dilip went home.' -> '____ did Dilip go?'", "Where", "Who", "Why", "What", "A", "'Where' inquires about destination."),
        ("Identify the INCORRECT question word usage: '**Why** is the boy's name?'", "'Why' should be 'What'", "'Why' should be 'Where'", "'Why' should be 'When'", "No error", "A", "'What is the boy's name?' asks for identity."),
        ("Select the proper interrogative sentence:", "Why did Mahajan hide the scales?", "Why Mahajan hid the scales?", "Why did Mahajan hid the scales?", "Why Mahajan hide scales?", "A", "Interrogative word + auxiliary 'did' + base verb 'hide'."),
        ("Which question word asks about MANNER or METHOD? '___ did Dilip teach Mahajan a lesson?'", "How", "Who", "What", "Where", "A", "'How' inquires about method or manner."),
        ("Complete the question: '___ of the two characters was honest?'", "Which", "What", "Where", "Why", "A", "'Which' chooses between specific options."),
        ("Change statement to question: 'An eagle flew away with the boy.' -> '____ flew away with the boy?'", "What bird / Who", "Where", "Why", "When", "A", "'What bird' or 'Who' asks for subject."),
        ("Fill in the blank: '___ heavy was the iron scale?'", "How", "What", "Where", "Why", "A", "'How heavy' measures degree of weight."),
        ("Identify the question word in: 'Whom did Dilip meet near the river?'", "Whom", "did", "Dilip", "river", "A", "'Whom' is the interrogative pronoun asking about the object person."),
        ("Choose the question that matches this answer: 'He borrowed money because he was poor.'", "Why did Dilip borrow money?", "Where did Dilip borrow money?", "Who borrowed money?", "What did Dilip borrow?", "A", "'Why...' matches answer starting with 'because...'."),
        ("Fill in the blank: '___ direction did the eagle fly?'", "In which", "Who", "Why", "Where", "A", "'In which' asks for specific direction."),
        ("Complete: '___ money did Dilip earn abroad?'", "How much", "How many", "Who", "Where", "A", "'How much' asks about uncountable quantity (money)."),
        ("Select the correct question for: 'The Mahajan apologised to Dilip.'", "What did the Mahajan do?", "Where was the Mahajan?", "Why is the Mahajan poor?", "Who was the eagle?", "A", "'What did Mahajan do?' asks for action."),
        ("Which question word inquires about POSSESSION? '___ scales were eaten by rats?'", "Whose", "Who", "Where", "Why", "A", "'Whose' asks about ownership/possession."),
        ("Form question: 'Dilip returned after three years.' -> '____ years did Dilip spend abroad?'", "How many", "How much", "Why", "Where", "A", "'How many' asks for countable number of years."),
        ("Identify the question mark error: 'Where did Dilip go.' Correct it:", "Where did Dilip go?", "Where did Dilip go!", "Where did Dilip go,", "Where did Dilip go;", "A", "Questions must end with question mark ?")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH01_CAT07_Q{idx:02d}"
        qtxt = f"Question Formation & Context Alignment:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Interrogative Sentence Formation", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence structure: 'Why did the Mahajan lie to Dilip?' What is the syntax pattern?", "Question Word + Helping Verb (did) + Subject (Mahajan) + Main Verb (lie) + Object/Rest", "Question Word + Main Verb + Subject", "Subject + Question Word + Verb", "Helping Verb + Question Word + Subject", "A", "Standard English question syntax."),
        ("Differentiate between 'How many' vs 'How much': '___ iron scales' vs '___ money'", "'How many' for countable scales; 'How much' for uncountable money.", "Both use 'How many'.", "Both use 'How much'.", "'How much' for scales; 'How many' for money.", "A", "Countable nouns take 'How many'; uncountable nouns take 'How much'."),
        ("Spot the syntax error in question: 'Where Dilip locked the boy?' Correct it:", "Where **did** Dilip lock the boy?", "Where Dilip lock the boy?", "Where locked Dilip the boy?", "Where does Dilip locked the boy?", "A", "Past simple questions require auxiliary 'did' before subject and base verb 'lock'."),
        ("Framing multi-question interview: What sequence of question words logically reveals the story plot?", "Who -> Why -> What happened -> How was it solved", "How -> Who -> Why -> What", "Where -> Where -> Where -> Where", "Why -> Why -> Why -> Why", "A", "Identifies character, motive, event, and resolution."),
        ("Transform the statement into a formal question: 'The Mahajan felt ashamed of his greed.'", "How did the Mahajan feel about his greed?", "Why was Mahajan greedy?", "Who was Mahajan?", "Where did Mahajan feel ashamed?", "A", "'How did Mahajan feel...' directly asks about emotional state."),
        ("Analyze this ambiguous question: 'What did Dilip take?' How can it be made precise?", "Add specific context: 'What object did Dilip give as security to the Mahajan?'", "Make it shorter: 'What take?'", "Change to: 'Where Dilip?'", "Remove 'What'.", "A", "Adding context clarifies the target object."),
        ("Choose the correct question pair for dialogue: Dilip: '___ is my iron balance?' Mahajan: '___ can I say? The mice ate it!'", "Where, What", "Who, Why", "Why, How", "When, Whose", "A", "Where (location of scales), What (expression of regret/excuse)."),
        ("Spot the DOUBLE auxiliary error: 'Why did Dilip carried the boy away?'", "'did' requires base verb 'carry', not past tense 'carried'.", "'did' should be 'was'.", "'Why' should be 'How'.", "No error.", "A", "Auxiliary 'did' must be followed by base form of verb ('carry')."),
        ("Reconstruct question from answer: Answer: 'An eagle carrying a child is impossible!'", "Question: 'What did the Mahajan claim was impossible?'", "Question: 'Where is eagle?'", "Question: 'Who is child?'", "Question: 'Why eagle fly?'", "A", "Targets Mahajan's disbelief."),
        ("Form indirect question: 'I want to know where Dilip went.' What is the sentence type?", "Assertive statement containing an embedded indirect question.", "Direct question requiring question mark.", "Exclamatory sentence.", "Command.", "A", "Indirect questions are statements ending with full stop."),
        ("Identify the correct question word for moral reasoning: '___ should we never tell lies?'", "Why", "What", "Who", "Where", "A", "'Why' inquires into ethical/moral justification."),
        ("HOTS Reasoning: Why is 'Who' used for people but 'Which' used when selecting from a specific group of people?", "'Who' is general; 'Which' is used when choosing from a defined limited set.", "'Who' is for animals.", "'Which' is only for things.", "Both are identical.", "A", "'Which of the boys...' selects from a defined group."),
        ("Correct all errors in: 'who Mahajan saw at the river'", "Who did Mahajan see at the river?", "Who Mahajan see at river?", "Whom Mahajan saw at river?", "Who does Mahajan saw at the river?", "A", "Capital W, auxiliary 'did', base verb 'see', ends with ?"),
        ("Select the question that evaluates Higher Order Thinking (HOTS) about Chapter 01:", "How does Dilip's clever plan prove that dishonesty leads to trouble?", "What was the boy's name?", "Where did Mahajan live?", "Did rats eat iron?", "A", "Asks student to evaluate cause-and-effect and moral reasoning.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH01_CAT07_Q{idx:02d}"
        qtxt = f"Higher Order Interrogative Analysis & Syntax:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Question Syntax & Analytical Framing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 8. Present Continuous Tense (-ing) (50 Qs)
# ---------------------------------------------------------------------------
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense (-ing) — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_ing = [
        ("Dilip is **walking** to the river.", "walking", "Dilip", "is", "river", "A", "'walking' is verb + -ing form."),
        ("The Mahajan is **crying** for his lost son.", "crying", "Mahajan", "is", "son", "A", "'crying' is verb + -ing form."),
        ("An eagle is **flying** high in the sky.", "flying", "eagle", "is", "sky", "A", "'flying' is verb + -ing form."),
        ("The rats are **eating** the food.", "eating", "rats", "are", "food", "A", "'eating' is verb + -ing form."),
        ("Dilip is **carrying** a heavy bag.", "carrying", "Dilip", "is", "bag", "A", "'carrying' is verb + -ing form."),
        ("The boy is **following** Dilip.", "following", "boy", "is", "Dilip", "A", "'following' is verb + -ing form."),
        ("Mahajan is **looking** for his son.", "looking", "Mahajan", "is", "son", "A", "'looking' is verb + -ing form."),
        ("The birds are **singing** in the trees.", "singing", "birds", "are", "trees", "A", "'singing' is verb + -ing form."),
        ("Dilip is **telling** the truth.", "telling", "Dilip", "is", "truth", "A", "'telling' is verb + -ing form."),
        ("Mahajan is **feeling** ashamed.", "feeling", "Mahajan", "is", "ashamed", "A", "'feeling' is verb + -ing form."),
        ("The river is **flowing** fast.", "flowing", "river", "is", "fast", "A", "'flowing' is verb + -ing form."),
        ("Dilip is **planning** a trip.", "planning", "Dilip", "is", "trip", "A", "'planning' is verb + -ing form."),
        ("The children are **playing** near the bank.", "playing", "children", "are", "bank", "A", "'playing' is verb + -ing form."),
        ("Mahajan is **apologising** to Dilip.", "apologising", "Mahajan", "is", "Dilip", "A", "'apologising' is verb + -ing form."),
        ("Dilip is **returning** the boy safely.", "returning", "Dilip", "is", "boy", "A", "'returning' is verb + -ing form."),
        ("The sun is **shining** brightly.", "shining", "sun", "is", "brightly", "A", "'shining' is verb + -ing form."),
        ("Mahajan is **hiding** the scales.", "hiding", "Mahajan", "is", "scales", "A", "'hiding' is verb + -ing form."),
        ("Dilip is **earning** money abroad.", "earning", "Dilip", "is", "money", "A", "'earning' is verb + -ing form.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_ing, start=1):
        qid = f"BK02_CH01_CAT08_Q{idx:02d}"
        qtxt = f"Identify the **present continuous (-ing) verb** in this sentence:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the present continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Present Continuous Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("What is the correct -ing spelling rule for **'run'**? (Dilip is ____ to the market.)", "running (double the last consonant)", "runing", "runnning", "runeing", "A", "CVC rule: double final consonant before -ing (running)."),
        ("What is the correct -ing spelling rule for **'write'**? (Dilip is ____ a letter.)", "writing (drop final silent e)", "writeing", "writting", "writeing", "A", "Drop final silent 'e' before adding -ing (writing)."),
        ("What is the correct -ing spelling rule for **'lie'**? (Mahajan is ____ about the scales.)", "lying (change -ie to -y + ing)", "lieing", "liing", "lyeing", "A", "Verbs ending in -ie change -ie to -y before adding -ing (lying)."),
        ("Fill in the blank with present continuous form: 'Dilip (travel) ____ to a foreign land.'", "is traveling / is travelling", "was travel", "are travel", "is traveled", "A", "Singular subject Dilip takes 'is traveling'."),
        ("Choose the sentence in PRESENT CONTINUOUS tense:", "The eagle is soaring in the sky.", "The eagle soared in the sky.", "The eagle will soar in the sky.", "The eagle soared yesterday.", "A", "'is soaring' is present continuous."),
        ("Fill in the blanks: 'The rats ____ (eat) the cheese, and Mahajan ____ (watch) them.'", "are eating, is watching", "is eating, are watching", "are eat, is watch", "was eating, were watching", "A", "Plural 'rats' takes 'are eating'; singular 'Mahajan' takes 'is watching'."),
        ("Identify the spelling mistake in: 'Dilip is **planing** his travel.'", "'planing' should be 'planning'", "'planing' should be 'planing'", "'is' should be 'are'", "No mistake", "A", "Plan -> planning (double 'n')."),
        ("Select the correct -ing form for **'make'**:", "making", "makeing", "makking", "macking", "A", "Drop silent 'e': make -> making."),
        ("Which sentence describes an action HAPPENING RIGHT NOW?", "Dilip is carrying the heavy iron scales home.", "Dilip carried the scales yesterday.", "Dilip carries scales every year.", "Dilip will carry the scales tomorrow.", "A", "Present continuous ('is carrying') describes ongoing action right now."),
        ("Fill in the blank: 'I ____ (write) a story about Panchatantra.'", "am writing", "is writing", "are writing", "am writeing", "A", "Subject 'I' takes 'am writing'."),
        ("Choose the correct form: 'The boys ____ (play) near the river bank.'", "are playing", "is playing", "am playing", "are play", "A", "Plural subject 'boys' takes 'are playing'."),
        ("Identify the verb in: 'Why are you lying to me?'", "are lying", "Why", "you", "to me", "A", "Helping verb 'are' + main verb 'lying' form present continuous."),
        ("What is the -ing form of **'swim'**?", "swimming", "swiming", "swimnning", "swimeing", "A", "CVC rule: swim -> swimming."),
        ("What is the -ing form of **'hop'**?", "hopping", "hoping", "hopping", "hopeing", "A", "CVC rule: hop -> hopping."),
        ("Change simple present to continuous: 'Dilip walks home.' -> 'Dilip ____ home.'", "is walking", "walked", "was walking", "will walk", "A", "is walking."),
        ("Fill in the blank: 'The Mahajan ____ (weep) because his son is missing.'", "is weeping", "are weeping", "am weeping", "weeped", "A", "is weeping."),
        ("Identify the correct present continuous sentence:", "Look! An eagle is flying away with a lamb.", "Look! An eagle fly away with a lamb.", "Look! An eagle flew away with a lamb.", "Look! An eagle flying away with a lamb.", "A", "Exclamation 'Look!' introduces action happening now ('is flying')."),
        ("Select the correct -ing form for **'dance'**:", "dancing", "danceing", "danccing", "dansing", "A", "Drop silent e: dance -> dancing.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH01_CAT08_Q{idx:02d}"
        qtxt = f"Present Continuous Grammar & Spelling Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Present Continuous Formation & Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze spelling rules for adding -ing to verbs: Group them correctly: (sit, give, tie)", "sit -> sitting (double consonant), give -> giving (drop e), tie -> tying (change -ie to -y)", "All just add -ing.", "All double the last letter.", "sit -> siting, give -> giveing, tie -> tieing", "A", "3 distinct orthographic rules for -ing derivation."),
        ("Convert past tense narrative to present continuous picture scene: 'The eagle carried the boy while Dilip watched.'", "The eagle is carrying the boy while Dilip is watching.", "The eagle carrying the boy while Dilip watching.", "The eagle was carrying the boy while Dilip watched.", "The eagle will carry the boy while Dilip watches.", "A", "Both verbs transformed to present continuous (is carrying, is watching)."),
        ("Spot the missing auxiliary verb in: 'Dilip walking to the village and Mahajan crying.' Correct it:", "'Dilip **is** walking to the village and Mahajan **is** crying.'", "'Dilip walking to village and Mahajan crying.'", "'Dilip **are** walking and Mahajan **are** crying.'", "No error.", "A", "Present continuous requires auxiliary (is/am/are) before -ing verb."),
        ("Differentiate state vs action: Why don't we usually say 'Dilip is **knowing** the answer'?", "Because 'know' is a stative verb that expresses state of mind, not an ongoing physical action.", "Because 'knowing' is difficult to spell.", "Because Dilip did not know.", "Because Mahajan lied.", "A", "Stative verbs (know, love, believe) generally do not take continuous forms in standard grammar."),
        ("Identify the sentence with CORRECT present continuous subject-verb agreement:", "The Mahajan and his son are walking to the river.", "The Mahajan and his son is walking to the river.", "The Mahajan and his son am walking to the river.", "The Mahajan and his son walking to the river.", "A", "Compound subject ('Mahajan and his son') takes plural auxiliary 'are'."),
        ("Form negative present continuous: 'Mahajan is telling the truth.' -> Negative:", "Mahajan is **not** telling the truth.", "Mahajan not telling the truth.", "Mahajan is no telling the truth.", "Mahajan isn't tell the truth.", "A", "Add 'not' between auxiliary 'is' and main verb 'telling'."),
        ("Spot all THREE spelling errors: 'Dilip is **writeing** a letter, **runing** fast, and **lieing** down.'", "'writeing' -> 'writing'; 'runing' -> 'running'; 'lieing' -> 'lying'", "'writeing' -> 'writting'; 'runing' -> 'runing'; 'lieing' -> 'lieing'", "No errors.", "Only 'runing' is wrong.", "A", "writing (drop e), running (double n), lying (-ie to -y)."),
        ("Rewrite as interrogative present continuous: 'The rats are eating the scales.'", "**Are** the rats eating the scales?", "Is the rats eating the scales?", "The rats eating the scales?", "Why the rats are eating scales?", "A", "Move auxiliary 'Are' to beginning of sentence."),
        ("Analyze action timeline: 'Dilip **is leaving** for abroad tomorrow.' What does present continuous express here?", "A fixed future arrangement / planned action.", "Past completed action.", "Action that happened years ago.", "Uncertain rumor.", "A", "Present continuous can express planned future actions."),
        ("Choose the sentence showing PARALLEL present continuous actions:", "While Dilip is walking, the Mahajan is searching for his son.", "While Dilip walked, Mahajan is searching.", "Dilip is walking while Mahajan searched.", "Dilip walk while Mahajan search.", "A", "Both parallel ongoing actions use present continuous."),
        ("Correct the error: 'I am runing towards the river bank.'", "'runing' should be 'running' (double 'n').", "'am' should be 'is'.", "'river' should be capitalized.", "No error.", "A", "Run ends in CVC, so n is doubled."),
        ("HOTS Reasoning: Compare 'The mice ate the iron' (Past Simple) vs 'The mice are eating the iron' (Present Continuous). How does the meaning change?", "Past simple states a completed past event; present continuous describes an action currently in progress.", "Both mean the exact same thing.", "Past simple is for future; continuous is for past.", "Continuous means Mahajan lied.", "A", "Tense changes temporal aspect (completed vs ongoing)."),
        ("Form question: 'Why ____ the Mahajan ____ (weep)?'", "is, weeping", "are, weeping", "am, weeping", "do, weeping", "A", "Singular subject Mahajan takes 'is ... weeping'."),
        ("Identify the correct present continuous sentence describing animal behavior:", "The eagle is soaring gracefully through the clouds.", "The eagle is soar gracefully through clouds.", "The eagle are soaring gracefully through clouds.", "The eagle soaring gracefully through clouds.", "A", "Singular eagle + is + soaring.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH01_CAT08_Q{idx:02d}"
        qtxt = f"Higher Order Present Continuous Analysis & Editing:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Continuous Tense Aspect & Error Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 9. Helping Verbs (Is, Am, Are) (50 Qs)
# ---------------------------------------------------------------------------
def build_helping_verbs():
    header = "# Category 9: Helping Verbs (Is, Am, Are) — Chapter 01: The Rats Who Ate the Iron Balance\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_hv = [
        ("Dilip ___ an honest boy.", "is", "are", "am", "be", "A", "Singular subject 'Dilip' takes 'is'."),
        ("I ___ reading the story of Dilip and Mahajan.", "am", "is", "are", "be", "A", "Pronoun 'I' takes 'am'."),
        ("The rats ___ small animals.", "are", "is", "am", "be", "A", "Plural subject 'rats' takes 'are'."),
        ("The Mahajan ___ very rich and greedy.", "is", "are", "am", "be", "A", "Singular subject 'Mahajan' takes 'is'."),
        ("The iron scales ___ heavy.", "are", "is", "am", "be", "A", "Plural subject 'scales' takes 'are'."),
        ("An eagle ___ a strong bird.", "is", "are", "am", "be", "A", "Singular subject 'An eagle' takes 'is'."),
        ("The boys ___ playing near the river.", "are", "is", "am", "be", "A", "Plural subject 'boys' takes 'are'."),
        ("Dilip and his friend ___ going home.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("I ___ sure that mice cannot eat iron.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The story ___ very interesting.", "is", "are", "am", "be", "A", "Singular 'story' takes 'is'."),
        ("The villagers ___ watching Dilip.", "are", "is", "am", "be", "A", "Plural 'villagers' takes 'are'."),
        ("Mahajan's house ___ big.", "is", "are", "am", "be", "A", "Singular 'house' takes 'is'."),
        ("You ___ a good student.", "are", "is", "am", "be", "A", "Pronoun 'You' always takes 'are'."),
        ("The bird ___ flying away.", "is", "are", "am", "be", "A", "Singular 'bird' takes 'is'."),
        ("The scales ___ made of iron.", "are", "is", "am", "be", "A", "Plural 'scales' takes 'are'."),
        ("I ___ glad Mahajan apologised.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("Dilip ___ returning from abroad.", "is", "are", "am", "be", "A", "Singular 'Dilip' takes 'is'."),
        ("The mice ___ not in the box.", "are", "is", "am", "be", "A", "Plural 'mice' takes 'are'.")
    ]
    
    for idx, (sent_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_hv, start=1):
        qid = f"BK02_CH01_CAT09_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct helping verb (is / am / are):\n\n\"{sent_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Helping Verb Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Choose the correct helping verb: 'Mahajan and his son ____ going to the bank.'", "are", "is", "am", "be", "A", "Compound subject ('Mahajan and his son') is plural, so it takes 'are'."),
        ("Select the sentence with CORRECT helping verb agreement:", "Dilip is carrying the heavy scales.", "Dilip are carrying the heavy scales.", "Dilip am carrying the heavy scales.", "Dilip be carrying the heavy scales.", "A", "Singular noun 'Dilip' requires 'is'."),
        ("Fill in the blanks: 'I ____ going to the market, and my friends ____ coming with me.'", "am, are", "is, are", "are, is", "am, is", "A", "'I am', 'friends are'."),
        ("Identify the mistake in: 'The mice **is** eating the iron balance.'", "'is' should be 'are' because 'mice' is a plural noun.", "'is' should be 'am'", "'is' should be 'was'", "No mistake", "A", "'mice' is plural (plural of mouse), requiring 'are'."),
        ("Which helping verb completes the question? '____ you ready to hear the story of Dilip?'", "Are", "Is", "Am", "Be", "A", "Subject 'you' takes 'Are'."),
        ("Fill in the blank: 'Neither the Mahajan nor his lie ____ going to work.'", "is", "are", "am", "be", "A", "'Neither...nor' with singular second subject takes 'is'."),
        ("Select the correct sentence for story moral:", "Honesty and truth are important virtues.", "Honesty and truth is important virtues.", "Honesty and truth am important virtues.", "Honesty and truth be important virtues.", "A", "Compound subject 'Honesty and truth' takes 'are'."),
        ("Complete the conversation: Dilip: 'Where ____ my scales?' Mahajan: 'They ____ gone!'", "are, are", "is, is", "is, are", "are, is", "A", "Plural 'scales' -> are; plural 'They' -> are."),
        ("Identify where 'is' is used incorrectly:", "The rats **is** hungry.", "Dilip is poor.", "Mahajan is rich.", "The eagle is big.", "A", "'The rats is' should be 'The rats are'."),
        ("Choose the correct helping verb for collective noun used as a single unit: 'The family ____ travelling.'", "is", "are", "am", "be", "A", "Collective noun 'family' treated as singular unit takes 'is'."),
        ("Fill in the blank: 'Dilip ____ not afraid of Mahajan's lies.'", "is", "are", "am", "be", "A", "Singular 'Dilip' takes 'is'."),
        ("Select the sentence with correct helping verb for 'I':", "I am standing near the river.", "I is standing near the river.", "I are standing near the river.", "I be standing near the river.", "A", "Subject 'I' takes 'am'."),
        ("Fill in the blank: 'There ____ many iron scales in the shop.'", "are", "is", "am", "be", "A", "'There are' before plural noun 'many iron scales'."),
        ("Fill in the blank: 'There ____ a bird in the sky.'", "is", "are", "am", "be", "A", "'There is' before singular noun 'a bird'."),
        ("Choose the correct sentence:", "What are the boys doing near the house?", "What is the boys doing near the house?", "What am the boys doing near the house?", "What be the boys doing near the house?", "A", "Plural subject 'the boys' takes 'are'."),
        ("Identify the correct form: 'The scale, as well as the coins, ____ missing.'", "is", "are", "am", "be", "A", "Subject is singular 'The scale' ('as well as...' does not change subject number), taking 'is'."),
        ("Fill in the blank: 'Both Dilip and Mahajan ____ present in court.'", "are", "is", "am", "be", "A", "'Both ... and ...' takes plural verb 'are'."),
        ("Select the option with correct helping verbs: 'He ____ small, but I ____ big.'", "is, am", "are, is", "am, are", "is, are", "A", "'He is', 'I am'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH01_CAT09_Q{idx:02d}"
        qtxt = f"Helping Verb Subject-Verb Agreement Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Subject-Verb Agreement Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze subject-verb agreement: 'Each of the iron scales **____** heavy.' Choose the correct verb and reason:", "is — because 'Each' is a singular indefinite pronoun requiring singular verb 'is'.", "are — because 'scales' is plural.", "am — because it refers to speaker.", "be — because scales are iron.", "A", "'Each' is singular indefinite pronoun taking singular verb 'is'."),
        ("Spot the subtle agreement error in: 'A pair of heavy iron scales **are** lying on the table.'", "'are' should be 'is' because the subject is singular noun 'pair'.", "'are' should be 'am'.", "'scales' should be 'scale'.", "No error.", "A", "'A pair' is singular, so it requires 'is lying'."),
        ("Compare: (1) 'Dilip and Mahajan **are** talking.' vs (2) 'Dilip, together with Mahajan, **is** talking.' Why are the verbs different?", "In (1), 'and' creates a plural subject (are); in (2), 'together with' is a prepositional phrase, leaving 'Dilip' as the sole singular subject (is).", "They mean different things.", "Sentence (2) is grammatically wrong.", "Both should use 'are'.", "A", "Prepositional phrases like 'together with' do not change the number of the subject."),
        ("Identify the correct agreement for indefinite pronouns: 'Everyone in the village **____** watching Dilip.'", "is", "are", "am", "be", "A", "'Everyone' is a singular indefinite pronoun requiring 'is'."),
        ("Spot all THREE subject-verb errors in: 'The rats **is** small, I **is** smart, and Dilip **are** honest.'", "'rats is' -> 'rats are'; 'I is' -> 'I am'; 'Dilip are' -> 'Dilip is'", "'rats is' -> 'rats am'; 'I is' -> 'I are'; 'Dilip are' -> 'Dilip am'", "Only 'I is' is wrong.", "No errors present.", "A", "rats are (plural), I am (1st person), Dilip is (3rd person singular)."),
        ("Fill in the blanks in this complex sentence: 'Not only Mahajan but also his servants **____** lying, while Dilip **____** telling the truth.'", "are, is", "is, are", "is, is", "are, are", "A", "'Not only...but also' agrees with closer subject ('servants' -> are); 'Dilip' -> is."),
        ("Transform to negative: 'The eagle and the boy are in the sky.'", "The eagle and the boy **are not** in the sky.", "The eagle and the boy is not in the sky.", "The eagle and the boy am not in the sky.", "The eagle and the boy not in sky.", "A", "Add 'not' after plural helping verb 'are'."),
        ("Analyze inverted subject position: 'Under the banyan tree **____** sitting three wise men.'", "are", "is", "am", "be", "A", "Subject is plural 'three wise men', appearing after the verb, requiring 'are'."),
        ("Determine agreement with uncountable nouns: 'The money borrowed by Dilip **____** kept in the box.'", "is", "are", "am", "be", "A", "Uncountable noun 'money' is treated as singular, taking 'is'."),
        ("Correct the sentence: 'Here **is** the scales you requested.'", "Here **are** the scales you requested.", "Here am the scales you requested.", "Here be the scales you requested.", "No error.", "A", "Plural subject 'scales' requires 'Here are...''"),
        ("Identify the sentence where 'is' acts as a MAIN linking verb rather than a helping verb:", "Dilip **is** an honest young boy.", "Dilip **is** walking home.", "Dilip **is** carrying scales.", "Dilip **is** leaving today.", "A", "In 'Dilip is an honest boy', 'is' is the main linking verb connecting subject to predicate noun."),
        ("HOTS Reasoning: Why does English use 'am' ONLY with the subject pronoun 'I'?", "Because 'am' is the unique 1st person singular present indicative form of the verb 'to be'.", "Because 'I' is capitalized.", "Because Mahajan commanded it.", "There is no reason.", "A", "'am' is exclusively reserved for 1st person singular 'I'."),
        ("Fill in the blanks: 'Neither Dilip nor the villagers **____** believing Mahajan, because he **____** greedy.'", "are, is", "is, are", "is, is", "are, are", "A", "'villagers' is closer plural subject -> are; 'he' -> is."),
        ("Select the option with PERFECT helping verb agreement throughout:", "Dilip is honest, I am helpful, and the scales are heavy.", "Dilip are honest, I is helpful, and the scales is heavy.", "Dilip am honest, I are helpful, and the scales am heavy.", "Dilip is honest, I is helpful, and the scales is heavy.", "A", "Dilip is (singular), I am (1st person), scales are (plural).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH01_CAT09_Q{idx:02d}"
        qtxt = f"Higher Order Helping Verb Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Subject-Verb Agreement & Syntax", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# MAIN EXECUTION FOR REBUILDING CHAPTER 01
# ---------------------------------------------------------------------------
def rebuild_chapter_01():
    print("Rebuilding Chapter 01 category files with high-quality, multi-tiered (Easy/Medium/Hard) non-duplicate questions...")

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
        filepath = os.path.join(CH01_DIR, fname)
        print(f"  Generating {fname}...")
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {fname} created successfully.")

    print("\n[SUCCESS] Completed rebuilding all 9 category files for Chapter 01 (450 total high-quality questions)!")

if __name__ == "__main__":
    rebuild_chapter_01()
