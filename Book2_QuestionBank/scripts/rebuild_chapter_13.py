r"""
=============================================================================
Script: rebuild_chapter_13.py
Description: Generates 50 rich, non-duplicate, multi-tiered (Easy, Medium, Hard)
             questions for each of the 9 category files in Chapter 13:
             "Habits of the Hippopotamus" (450 Qs total).
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH13_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_13")
os.makedirs(CH13_DIR, exist_ok=True)

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
    header = "# Category 1: Plural Nouns & Spelling Rules — Chapter 13: Habits of the Hippopotamus\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("hippopotamus", "hippopotamuses", "hippopotamuss", "hippopotamusies", "hippopotamusz", "A", "Nouns ending in -s add -es (hippopotamuses)."),
        ("limb", "limbs", "limbes", "limbies", "limbz", "A", "Regular noun adding -s."),
        ("sweet", "sweets", "sweetes", "sweeties", "sweetz", "A", "Regular noun adding -s."),
        ("pie", "pies", "piees", "piies", "piez", "A", "Regular noun ending in -e adds -s."),
        ("truck", "trucks", "truckes", "truckies", "truckz", "A", "Regular noun adding -s."),
        ("tram", "trams", "trames", "tramies", "tramz", "A", "Regular noun adding -s."),
        ("taxicab", "taxicabs", "taxicabes", "taxicabies", "taxicabz", "A", "Regular noun adding -s."),
        ("omnibus", "omnibuses", "omnibuss", "omnibusies", "omnibusz", "A", "Nouns ending in -s add -es (omnibuses)."),
        ("jam", "jams", "james", "jamies", "jamz", "A", "Regular noun adding -s."),
        ("muss", "musses", "musss", "mussies", "mussz", "A", "Nouns ending in -ss add -es (musses)."),
        ("muscle", "muscles", "musclies", "musclees", "musclez", "A", "Regular noun ending in -e adds -s."),
        ("head", "heads", "heades", "headies", "headz", "A", "Regular noun adding -s."),
        ("principle", "principles", "principlies", "principlees", "principlez", "A", "Regular noun ending in -e adds -s."),
        ("thing", "things", "thinges", "thingies", "thingz", "A", "Regular noun adding -s."),
        ("habit", "habits", "habites", "habities", "habitz", "A", "Regular noun adding -s."),
        ("flavor", "flavors", "flavores", "flavories", "flavorz", "A", "Regular noun adding -s."),
        ("child", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("person", "people", "persons", "peoples", "persones", "A", "Irregular plural: person becomes people.")
    ]
    
    for idx, (word, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH13_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{word}'** from or related to Chapter 13 (*Habits of the Hippopotamus*)?"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Plural Noun Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The hippopotamus has strong (limb / limbs).", "limbs", "limb", "limbes", "limbies", "A", "Plural noun 'limbs'."),
        ("He does not care for (sweet / sweets) like ice cream.", "sweets", "sweet", "sweetes", "sweeties", "A", "Plural noun 'sweets'."),
        ("He never rides in (truck / trucks) or (tram / trams).", "trucks, trams", "truckes, trames", "truckies, tramies", "truckz, tramz", "A", "trucks and trams add -s."),
        ("Identify the INCORRECT plural spelling in this list: limbs, sweets, omnibuss, jams.", "omnibuss", "limbs", "sweets", "jams", "A", "Plural of omnibus is 'omnibuses', not 'omnibuss'."),
        ("Choose the sentence with the correct plural noun form:", "He avoids taxicabs and omnibuses.", "He avoids taxicabes and omnibuss.", "He avoids taxicabies and omnibusies.", "He avoids taxicabz and omnibusz.", "A", "taxicabs (-s) and omnibuses (-s + es) are correct."),
        ("Which noun forms its plural by adding -es to a word ending in -s?", "omnibus -> omnibuses", "truck -> trucks", "tram -> trams", "limb -> limbs", "A", "Omnibus ends in -s, so plural is omnibuses."),
        ("Change the singular noun in brackets to plural: 'The street was full of ____ (omnibus).' ", "omnibuses", "omnibuss", "omnibusies", "omnibusz", "A", "Nouns ending in -s add -es (omnibuses)."),
        ("Select the sentence where ALL plural nouns are spelt correctly:", "The hippopotamus stays out of traffic jams and messes.", "The hippopotamus stays out of traffic james and messies.", "The hippopotamus stays out of traffic jamz and messz.", "The hippopotamus stays out of traffic jamies and messes.", "A", "jams, messes are all correctly spelt plurals."),
        ("What is the correct plural of 'apple pie'?", "apple pies", "apple piees", "apple piies", "apple piez", "A", "Regular noun ending in -e adds -s."),
        ("The hippopotamus stays true to his (principle / principles).", "principles", "principle", "principlies", "principlees", "A", "Plural noun 'principles'."),
        ("Many (hippopotamus / hippopotamuses) live near rivers.", "hippopotamuses", "hippopotamuss", "hippopotamusies", "hippopotamusz", "A", "Plural of hippopotamus is hippopotamuses (or hippopotami)."),
        ("Many (person / people) laugh at the funny poem.", "people", "persons", "peoples", "persones", "A", "Irregular plural of person is people."),
        ("How many (truck / trucks) were in the traffic jam?", "trucks", "truck", "truckes", "truckies", "A", "Regular noun adding -s (trucks)."),
        ("The animal avoids all (muss / musses).", "musses", "musss", "mussies", "mussz", "A", "Nouns ending in -ss add -es (musses)."),
        ("Which plural noun rule applies to the word **'omnibuses'**?", "Add -es to nouns ending in -s", "Add -s to vowel + y", "Change -f to -ves", "Change -y to -ies", "A", "Omnibus ends in -s, so it adds -es."),
        ("He eats food with different (flavor / flavors).", "flavors", "flavores", "flavories", "flavorz", "A", "Plural of flavor is flavors."),
        ("Identify the correct plural form of 'child':", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("The hippopotamus rolls along on heavy (limb / limbs).", "limbs", "limb", "limbes", "limbies", "A", "Plural of limb is limbs.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH13_CAT01_Q{idx:02d}"
        qtxt = f"Contextual Plural Rule Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Plural Noun Application", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Rewrite the sentence in PLURAL form: 'The hippopotamus avoids a truck, a tram, and a taxicab.'", "The hippopotamuses avoid trucks, trams, and taxicabs.", "The hippopotamuss avoids truckes, trames, and taxicabes.", "The hippopotamusies avoid truckies, tramies, and taxicabies.", "The hippopotamusz avoids truckz, tramz, and taxicabz.", "A", "Plural of hippopotamus->hippopotamuses (-s+es), truck->trucks, tram->trams, taxicab->taxicabs."),
        ("Analyze the error: 'The hippopotamus ate much sweets.' Why is 'much' inappropriate here?", "'sweets' is a plural countable noun, so 'many sweets' should be used.", "'sweets' should be 'sweetes'.", "'sweets' should be 'sweeties'.", "No error.", "A", "Countable plural nouns take 'many', not 'much'."),
        ("Complete the paragraph with correct plurals: 'The two ____ (hippopotamus) avoided five ____ (truck) and three ____ (omnibus).'", "hippopotamuses, trucks, omnibuses", "hippopotamuss, truckes, omnibuss", "hippopotamusies, truckies, omnibusies", "hippopotamuses, trucks, omnibuss", "A", "hippopotamuses (-s+es), trucks (-s), omnibuses (-s+es)."),
        ("Identify the sentence where ALL three underlined nouns are correctly pluralized:", "The **children** saw **hippopotamuses** avoid **taxicabs**.", "The **childs** saw **hippopotamuss** avoid **taxicabes**.", "The **childrens** saw **hippopotamusies** avoid **taxicabies**.", "The **childes** saw **hippopotamuses** avoid **taxicabz**.", "A", "children (irregular), hippopotamuses (-s+es), taxicabs (-s)."),
        ("Which group contains ONLY irregular plural nouns?", "children, people, men, feet", "limbs, trucks, trams, sweets", "buses, musses, dishes, boxes", "leaves, thieves, wolves, knives", "A", "children, people, men, feet change forms without standard -s/-es."),
        ("Why does 'omnibus' become 'omnibuses' but 'truck' becomes 'trucks'?", "Because 'omnibus' ends in -s (requiring -es), while 'truck' ends in a regular consonant -k (adding -s).", "Because omnibus is big.", "Because truck is fast.", "Both follow the exact same rule.", "A", "Nouns ending in -s add -es; regular consonants add -s."),
        ("Find the TWO grammatical mistakes in: 'The two hippopotamuss saw many mouses near the river.'", "'hippopotamuss' should be 'hippopotamuses' and 'mouses' should be 'mice'.", "'hippopotamuss' should be 'hippopotamus' and 'mouses' should be 'mices'.", "'river' should be 'rivers' only.", "There are no mistakes in the sentence.", "A", "hippopotamuses (-s + es) and mice (irregular plural)."),
        ("Replace the singular words in brackets: 'The hippopotamuses placed their ____ (foot) on the ground.'", "feet", "foots", "feets", "footies", "A", "Plural of foot is feet."),
        ("Analyze this wordplay plural in the poem: 'hippopotomusses' (portmanteau of hippopotamus + musses/messes). What is the base plural rule?", "Nouns ending in -ss or -s add -es to form plural (muss -> musses).", "Add -s only.", "Change -ss to -v.", "Drop -ss.", "A", "Nouns ending in sibilants (-s, -ss) add -es."),
        ("Fill in the blanks: 'The two ____ (child) ate two ____ (apple pie) at the zoo.'", "children, apple pies", "childs, apple piees", "childrens, apple piies", "childes, apple pies", "A", "child -> children; apple pie -> apple pies."),
        ("Select the option that shows correct plural transformation for ALL three words: 'omnibus', 'muss', 'limb'", "omnibuses, musses, limbs", "omnibuss, musss, limbes", "omnibusies, mussies, limbies", "omnibuses, musses, limbes", "A", "omnibus -> omnibuses; muss -> musses; limb -> limbs."),
        ("HOTS Reasoning: Why do we say 'custard' is uncountable but 'pies' are countable?", "Because 'custard' is a liquid mass food (uncountable), while 'pie' refers to individual baked units (countable).", "Because custard is yellow.", "Because pie is sweet.", "Because hippopotamus is big.", "A", "Mass liquids vs discrete baked units."),
        ("Transform into singular: 'The hippopotamuses avoided the omnibuses in the traffic jams.'", "The hippopotamus avoided the omnibus in the traffic jam.", "The hippopotamuses avoided the omnibus in the traffic jam.", "The hippopotamus avoid the omnibus in the traffic jam.", "The hippopotamus avoided the omnibuses in the traffic jam.", "A", "Singular forms: hippopotamus, omnibus, traffic jam."),
        ("Identify the correct rule for forming the plural of **'omnibus'**:", "Add -es because it is a noun ending in -s (omnibuses).", "Add -s (omnibuss).", "Change -s to -v (omnibuvs).", "Change vowel sound.", "A", "Nouns ending in -s add -es.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH13_CAT01_Q{idx:02d}"
        qtxt = f"Higher Order Thinking Skills (HOTS) & Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Plural & Spelling Analysis", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 2. Articles Grammar (50 Qs)
# ---------------------------------------------------------------------------
def build_articles_grammar():
    header = "# Category 2: Articles (A, An, The) — Chapter 13: Habits of the Hippopotamus\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("___ hippopotamus is strong and huge.", "The", "A", "An", "No article", "A", "Use 'The' to specify the generic species subject of poem."),
        ("The hippopotamus has ___ huge head.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'huge'."),
        ("The hippopotamus has ___ broad bustle.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'broad'."),
        ("He takes ___ little hippopotomustard for flavor.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'little'."),
        ("He never rides in ___ omnibus.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'omnibus'."),
        ("___ Panchatantra/Humorous poem describes the hippopotamus.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'Panchatantra/Humorous'."),
        ("He keeps out of ___ traffic jam.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'traffic'."),
        ("He is ___ honest animal true to his principles.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' sound in 'honest'."),
        ("___ hippopotamus does not care for sweets.", "The", "A", "An", "No article", "A", "Definite article 'The' specifies the animal species."),
        ("He faced ___ unusual choice between mustard and custard.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'unusual'."),
        ("He never gets into ___ taxicab.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'taxicab'."),
        ("It is ___ impressive poem by Arthur Guiterman.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'impressive'."),
        ("___ limbs of the hippopotamus are big with muscle.", "The", "A", "An", "No article", "A", "Use 'The' for specific limbs of the hippopotamus."),
        ("He rides neither in ___ truck nor in a tram.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'truck'."),
        ("They created ___ humorous rhyme in the poem.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'humorous'."),
        ("The hippopotamus has ___ open field to walk in.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'open'."),
        ("The poem brings ___ laughter to children.", "no article", "a", "an", "the", "A", "Abstract noun 'laughter' takes no indefinite article here."),
        ("___ sun shines while the hippopotamus rolls along.", "The", "A", "An", "No article", "A", "Use 'The' for unique celestial object 'sun'.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH13_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article (a / an / the / no article):\n\n\"{q_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Basic Article Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The hippopotamus has ___ huge head and ___ broad bustle.", "a, a", "an, a", "a, an", "the, a", "A", "'a huge head' (consonant sound), 'a broad bustle' (consonant sound)."),
        ("Why do we say '**a** taxicab' but '**an** omnibus'?", "Because 'taxicab' begins with a consonant sound (t) and 'omnibus' with a vowel sound (o).", "Because taxicabs are small.", "Because omnibuses are big.", "Because hippos are heavy.", "A", "Article selection depends on initial vowel/consonant sound."),
        ("Select the sentence with CORRECT article usage:", "The hippopotamus is a strong animal.", "An hippopotamus is a strong animal.", "The a hippopotamus is strong animal.", "A hippopotamus is an strong animal.", "A", "'The hippopotamus' (species subject), 'a strong animal' (consonant sound)."),
        ("Fill in the blanks: 'He takes ___ little mustard on ___ dish.'", "a, the", "an, a", "a, an", "the, a", "A", "'a little mustard' (consonant /l/), 'the dish' (specific dish)."),
        ("Identify the INCORRECT article in: 'He never rides in **a** omnibus.'", "'a' should be 'an'", "'a' should be 'the'", "'omnibus' should be 'a omnibus'", "No mistake", "A", "'omnibus' starts with vowel sound /o/, so it takes 'an'."),
        ("Which article completes the sentence? 'The hippo has ___ enormous body.'", "an", "a", "the", "no article", "A", "'enormous' starts with vowel sound /e/, requiring 'an'."),
        ("Choose the correct pair of articles: '___ animal rolls on ___ ground.'", "The, the", "A, a", "An, an", "The, a", "A", "'The animal' (specific hippo), 'the ground' (specific ground)."),
        ("Why do we use 'an' before 'omnibus' in 'He never rides in **an** omnibus'?", "Because 'omnibus' begins with the vowel sound /o/.", "Because omnibus is a bus.", "Because hippo is big.", "Because traffic is heavy.", "A", "'omnibus' starts with vowel sound /o/."),
        ("Complete the dialogue: Child: 'Is a hippopotamus ___ large animal?' Teacher: 'Yes, it is ___ very huge creature!'", "a, a", "a, an", "an, the", "the, the", "A", "'a large animal' (consonant sound), 'a very huge creature' (consonant sound)."),
        ("Select the correct sentence:", "A hippopotamus is a strong animal.", "An hippopotamus is a strong animal.", "The hippopotamus is an strong animal.", "An hippopotamus is an strong animal.", "A", "'A hippopotamus' (consonant sound), 'a strong animal' (consonant sound)."),
        ("Fill in the blank: 'The hippopotamus walked for ___ long distance.'", "a", "an", "the", "no article", "A", "Idiomatic phrase 'for a long distance'."),
        ("Identify where NO article is needed:", "The hippopotamus enjoys **___ mustard** on his food.", "He avoids ___ jam.", "She saw ___ bus.", "They built ___ road.", "A", "Uncountable mass food noun 'mustard' takes no article here."),
        ("Choose the correct sentence for poem summary:", "Honesty and principles guide wise choices.", "A honesty and a principles guide choices.", "An honesty and an principles guide choices.", "The honesty a guides choices.", "A", "Abstract concepts take no indefinite articles in general moral sense."),
        ("Fill in the blanks: 'The poet spent ___ hour writing ___ funny poem.'", "an, a", "a, a", "an, an", "the, an", "A", "'an hour' (silent h), 'a funny poem' (consonant b)."),
        ("Which sentence uses 'the' correctly for species representation?", "The hippopotamus is strong and broad of bustle.", "A hippopotamus is strong and broad of bustle.", "An hippopotamus is strong and broad of bustle.", "Hippopotamus is strong and broad of bustle.", "A", "Definite article 'the' represents entire species in formal description."),
        ("Identify the article error: 'He gave **a** explanation of **an** short rhyme.'", "'an short' should be 'a short' and 'a explanation' should be 'an explanation'", "'a explanation' should be 'an explanation'", "'an short' should be 'a short'", "No error", "A", "'an explanation' (vowel /e/) and 'a short rhyme' (consonant /s/)."),
        ("Complete: 'It was ___ unexpected sight in ___ traffic jam.'", "an, a", "a, an", "the, the", "an, an", "A", "an unexpected (/u/), a traffic jam (consonant sound /t/)."),
        ("Choose the correct option: '___ sun shone on the river bank.'", "The", "A", "An", "No article", "A", "'The sun' (unique celestial body).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH13_CAT02_Q{idx:02d}"
        qtxt = f"Contextual Article Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Article Usage in Context", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze article usage in: 'The hippopotamus is **the** strong animal in **a** river.' Correct the error:", "'the strong animal' -> 'a strong animal' (indefinite classification).", "'a river' -> 'an river'.", "'The hippopotamus' -> 'An hippopotamus'.", "No error.", "A", "Indefinite classification 'a strong animal'."),
        ("Fill in all three blanks: '___ hippopotamus avoids ___ traffic jam by walking on ___ road.'", "The, a, the", "A, a, a", "An, a, the", "The, a, a", "A", "'The hippopotamus' (species), 'a traffic jam' (consonant), 'the road' (surface)."),
        ("Identify why 'the' is used in: '**The** hippopotamus is true to all his principles.'", "Because 'The' is used generically to represent the whole class or species of hippopotamuses.", "Because hippopotamus is a noun.", "Because limbs are big.", "Because mustard is yellow.", "A", "'The' generically represents the entire animal species."),
        ("Spot the TWO article errors: 'It took **a** hour for **a** omnibus to pass.'", "'a hour' should be 'an hour' and 'a omnibus' should be 'an omnibus'.", "'a hour' should be 'the hour' and 'a omnibus' should be 'a omnibus'.", "No errors.", "Only 'a hour' is wrong.", "A", "Both 'hour' (silent h) and 'omnibus' (vowel o) require 'an'."),
        ("Choose the paragraph with PERFECT article usage throughout:", "The hippopotamus is a strong animal. It has a huge head. It avoids an omnibus.", "An hippopotamus is an strong animal. It has an huge head.", "The hippopotamus is the strong animal. It avoids a omnibus.", "A hippopotamus is a strong animal. The head was an honest.", "A", "The hippopotamus (species), a strong animal (consonant), a huge head (consonant), an omnibus (vowel)."),
        ("Why is it correct to write 'a unique habit' but 'an unusual habit'?", "Because 'unique' begins with consonant sound /j/ (yoo), while 'unusual' begins with vowel sound /u/.", "Because unique is longer.", "Because habit is noun.", "Both take 'an'.", "A", "Sound determines article: /yoo/ is a consonant sound."),
        ("Select the option that correctly completes the poem summary: '___ strong animal stays true to ___ principles and avoids ___ traffic jam.'", "A, no article, a", "An, a, an", "The, the, the", "A, a, a", "A", "A strong animal, principles (plural noun, no article), a traffic jam."),
        ("Analyze this sentence: 'He takes to flavor what he eats **a** little hippopotomustard.' Why is 'a' appropriate?", "Because 'a little' is a quantifier phrase modifying the mass noun hippopotomustard.", "Because mustard is a verb.", "Because hippo is in truck.", "Because tram is fast.", "A", "'a little' is an idiomatic quantifier phrase for uncountable mass nouns."),
        ("Correct the sentence: 'An hippopotamus never rides in a omnibus.'", "A hippopotamus never rides in an omnibus.", "The hippopotamus never rides in an omnibus.", "An hippopotamus never rides in the omnibus.", "A hippopotamus never rides in a omnibus.", "A", "'A hippopotamus' (/h/ sound), 'an omnibus' (vowel /o/)."),
        ("Fill in the blanks: '___ habits of ___ hippopotamus are described in ___ poem.'", "The, the, the", "A, a, a", "No article, a, an", "An, the, a", "A", "'The habits' (specific), 'the hippopotamus' (specific), 'the poem' (specific)."),
        ("Spot the missing article: 'Hippopotamus never rides in truck.'", "Missing 'The' at start and 'a' before 'truck' -> 'The hippopotamus never rides in a truck.'", "Missing 'an' before 'rides'", "Missing 'a' before 'never'", "No article is missing", "A", "Singular species subject and countable noun 'truck' require articles."),
        ("HOTS Reasoning: Which sentence uses 'a', 'an', and 'the' correctly in a single rule demonstration?", "An omnibus passed a hippopotamus near the river.", "A omnibus passed an hippopotamus near a river.", "The omnibus passed an hippopotamus near an river.", "An omnibus passed an hippopotamus near the river.", "A", "An omnibus (vowel), a hippopotamus (consonant), the river (specific)."),
        ("Rewrite correctly: 'The hippo is a honest animal with an huge bustle.'", "The hippo is an honest animal with a huge bustle.", "The hippo is a honest animal with a huge bustle.", "The hippo is an honest animal with an huge bustle.", "The hippo is the honest animal with an huge bustle.", "A", "'an honest' (silent h), 'a huge bustle' (consonant /h/)."),
        ("Identify the correct rule for using 'the' with animal species in literary/poetic subjects (the lion, the elephant, the hippopotamus):", "The definite article 'the' is used with a singular countable noun to represent a whole class or species.", "Species take 'an'.", "Species never take articles.", "Species take 'a' only.", "A", "Definite article represents an entire species.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH13_CAT02_Q{idx:02d}"
        qtxt = f"Higher Order Article Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Article Analysis & Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 3. Calendar & Days Vocabulary (50 Qs)
# ---------------------------------------------------------------------------
def build_calendar_days():
    header = "# Category 3: Calendar, Days & Abbreviations — Chapter 13: Habits of the Hippopotamus\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    days_easy = [
        ("The poem says the hippopotamus **'always tries his best'**. What does **'always'** mean?", "At all times / Every day", "Never", "Sometimes", "Once a year", "A", "'Always' means at all times / every day."),
        ("What word is the opposite of **'always'**?", "Never", "Often", "Usually", "Frequently", "A", "'Never' is the antonym of 'always'."),
        ("What is the standard abbreviation for **Friday**?", "Fri.", "Frid.", "Fr.", "F.", "A", "Fri. is standard abbreviation."),
        ("Which day comes right after Thursday?", "Friday", "Saturday", "Wednesday", "Tuesday", "A", "Friday follows Thursday."),
        ("What is the abbreviation for **Thursday**?", "Thu.", "Thur.", "Th.", "Ts.", "A", "Thu. is standard abbreviation."),
        ("The hippopotamus walks in the **morning**, **afternoon**, and **evening**. What time of day comes right before afternoon?", "Morning", "Evening", "Night", "Midnight", "A", "Morning precedes afternoon."),
        ("What is the abbreviation for **Saturday**?", "Sat.", "Satur.", "Sa.", "St.", "A", "Sat. is standard abbreviation."),
        ("What time of day is **12:00 p.m.**?", "Noon / Midday", "Midnight", "Dawn", "Twilight", "A", "Noon/midday is 12:00 p.m."),
        ("What is the abbreviation for **Sunday**?", "Sun.", "Snd.", "Su.", "Sn.", "A", "Sun. is standard abbreviation."),
        ("Which month comes right before December?", "November", "October", "September", "January", "A", "November comes before December."),
        ("What is the short abbreviation for **December**?", "Dec.", "Dece.", "Dc.", "Dcm.", "A", "Dec. is standard abbreviation."),
        ("Which month comes right after December?", "January", "February", "November", "October", "A", "January comes after December."),
        ("What is the short abbreviation for **January**?", "Jan.", "Jany.", "Ja.", "Jn.", "A", "Jan. is standard abbreviation."),
        ("If today is Friday, what day was yesterday?", "Thursday", "Saturday", "Wednesday", "Tuesday", "A", "Yesterday was Thursday."),
        ("If today is Friday, what day will tomorrow be?", "Saturday", "Thursday", "Sunday", "Monday", "A", "Tomorrow will be Saturday."),
        ("What is the abbreviation for **Wednesday**?", "Wed.", "Weds.", "We.", "W.", "A", "Wed. is standard abbreviation."),
        ("Which day comes between Wednesday and Friday?", "Thursday", "Tuesday", "Saturday", "Sunday", "A", "Thursday is between Wednesday and Friday."),
        ("Which month comes right before January?", "December", "November", "October", "February", "A", "December comes before January.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(days_easy, start=1):
        qid = f"BK02_CH13_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Vocabulary & Time Concepts:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Days & Calendar Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The hippopotamus walked along the river from **Monday** to **Friday**. For how many days did it walk?", "5 days", "4 days", "6 days", "7 days", "A", "Monday to Friday inclusive is 5 days."),
        ("The hippopotamus bathed from **9:00 AM to 1:00 PM**. How many hours did it bathe?", "4 hours", "3 hours", "5 hours", "2 hours", "A", "1:00 PM - 9:00 AM = 4 hours."),
        ("Match the day with its abbreviation: **Friday**", "Fri.", "Frid.", "Fr.", "F.", "A", "Fri. is standard."),
        ("The hippopotamus eats **3 meals a day**. How many meals does it eat in 1 week (7 days)?", "21 meals (3 x 7)", "15 meals", "30 meals", "14 meals", "A", "3 x 7 = 21 meals."),
        ("Identify the correctly spelt month name:", "December", "Decembre", "Decemberr", "Decembere", "A", "December is the correct spelling."),
        ("Identify the INCORRECT pair of day and abbreviation:", "Monday - Mon.", "Tuesday - Tue.", "Wednesday - Wed.", "Friday - Frd.", "D", "Friday abbreviation is Fri., not Frd."),
        ("Calculate: How many days are in **December**?", "31 days", "30 days", "28 days", "29 days", "A", "December has 31 days."),
        ("Which month has 31 days and comes right after November?", "December", "January", "October", "September", "A", "December has 31 days and follows November."),
        ("Rearrange in correct chronological order: Fri, Wed, Thu, Sat", "Wed, Thu, Fri, Sat", "Thu, Wed, Fri, Sat", "Fri, Thu, Wed, Sat", "Sat, Fri, Thu, Wed", "A", "Wednesday -> Thursday -> Friday -> Saturday."),
        ("What day is 3 days before Friday?", "Tuesday", "Wednesday", "Monday", "Thursday", "A", "Friday - 3 days = Thursday(1), Wednesday(2), Tuesday(3)."),
        ("If a hippopotamus observation trip lasts for 2 weeks, how many days is that?", "14 days (2 x 7)", "10 days", "20 days", "7 days", "A", "2 weeks x 7 days = 14 days."),
        ("Select the month that has 31 days:", "January", "November", "September", "April", "A", "January has 31 days."),
        ("Which abbreviation stands for **January**?", "Jan.", "Jany.", "Ja.", "Jn.", "A", "Jan. is standard abbreviation."),
        ("If today is **Fri.**, what day will it be after 7 days?", "Friday", "Saturday", "Thursday", "Monday", "A", "7 days is a full week cycle, landing on Friday again."),
        ("The hippopotamus rested from **1:00 PM to 4:00 PM**. How many hours did it rest?", "3 hours", "2 hours", "4 hours", "5 hours", "A", "4:00 PM - 1:00 PM = 3 hours."),
        ("Identify the word that means 'occurring every day without fail':", "Daily / Always", "Weekly", "Monthly", "Yearly", "A", "Daily/always means every day."),
        ("Which of the following is a weekday?", "Friday", "Sunday", "Saturday", "Weekend", "A", "Friday is a weekday."),
        ("Choose the correct abbreviation for **December**:", "Dec.", "Dece.", "Dc.", "Dcm.", "A", "Dec. is standard.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH13_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Application & Story Timeline:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Calendar & Time Reasoning", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("The author Arthur Guiterman wrote poems in the **20th century** (1900s). How many years are in 1 century?", "100 years", "10 years", "50 years", "500 years", "A", "1 century = 100 years."),
        ("If a hippopotamus spends **8 hours a day** swimming for 7 days, how many total hours does it swim in a week?", "56 hours (8 x 7)", "50 hours", "48 hours", "60 hours", "A", "8 x 7 = 56 hours."),
        ("Solve the calendar puzzle: If 1st December was a Wednesday, what day of the week was 8th December?", "Wednesday", "Thursday", "Tuesday", "Friday", "A", "1 + 7 = 8th December, landing on Wednesday."),
        ("Analyze this schedule: Hippo eats in river on Mon, Wed, Fri; Walks on land on Tue, Thu, Sat. On which day does it rest?", "Sunday", "Monday", "Saturday", "Wednesday", "A", "Sunday is not listed in schedule."),
        ("Complete the full series of day abbreviations: Mon., Tue., Wed., Thu., Fri., Sat., ____.", "Sun.", "Sund.", "Su.", "Sn.", "A", "Sun. completes the 7 days of the week."),
        ("If a wildlife survey on hippopotamuses lasted a fortnight, how many days did it cover?", "14 days (2 weeks)", "7 days", "30 days", "3 days", "A", "A fortnight is 14 days."),
        ("Spot the error in the calendar sequence: 'Nov, Dec, Feb, Jan, Mar'", "February and January are in wrong order.", "December is in wrong position.", "March should be first.", "No error.", "A", "January comes before February (Nov, Dec, Jan, Feb, Mar)."),
        ("December has **31 days**. What date was the day right after 31st December?", "1st January (New Year's Day)", "32nd December", "30th December", "1st February", "A", "December has 31 days, so next day is 1st January."),
        ("If yesterday was two days before Friday, what day is tomorrow?", "Friday", "Thursday", "Saturday", "Wednesday", "A", "Two days before Friday = Wednesday (yesterday). Today = Thursday. Tomorrow = Friday."),
        ("Calculate: How many days are there in total during **December** and **January** combined?", "62 days (31 + 31)", "60 days", "61 days", "59 days", "A", "December (31) + January (31) = 62 days."),
        ("HOTS Reasoning: What does the poem imply by 'He always tries his best to do the things one hippopotomust'?", "It humorously suggests that the hippopotamus adheres strictly to its own animal duties every single day.", "It means the hippo drives buses.", "It means the hippo eats candy.", "It means the hippo sleeps all month.", "A", "Humorous reference to daily adherence to duty."),
        ("Identify the correct statement about a non-leap year:", "A non-leap year has 365 days and February has 28 days.", "A non-leap year has 366 days.", "February has 30 days.", "A non-leap year occurs every 4 years.", "A", "Standard year has 365 days (Feb = 28 days)."),
        ("A hippopotamus walked 20 kilometers in 4 hours. How many kilometers per hour on average?", "5 kilometers per hour", "4 km", "10 km", "2 km", "A", "20 / 4 = 5 km per hour."),
        ("Which month pair both have 31 days and come right after each other at the end of the year and start of next year?", "December and January", "November and December", "October and November", "January and February", "A", "December (31) and January (31) are consecutive 31-day months.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH13_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Logic & Mathematical Time Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Calendar & Time Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 4. Action Verbs Identification (50 Qs)
# ---------------------------------------------------------------------------
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification — Chapter 13: Habits of the Hippopotamus\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_verbs = [
        ("The limbs on which he **rolls** along are big.", "rolls", "limbs", "big", "along", "A", "'rolls' is the physical action verb."),
        ("He does not greatly **care** for sweets.", "care", "greatly", "sweets", "he", "A", "'care' is the mental action verb."),
        ("He **takes** a little mustard to flavor food.", "takes", "little", "mustard", "flavor", "A", "'takes' is the action verb."),
        ("He **eats** his food with mustard.", "eats", "food", "mustard", "his", "A", "'eats' is the physical action verb."),
        ("He always **tries** his best.", "tries", "always", "best", "his", "A", "'tries' is the action verb."),
        ("He **does** the things one hippopotomust.", "does", "things", "one", "hippopotomust", "A", "'does' is the action verb."),
        ("He never **rides** in trucks or trams.", "rides", "never", "trucks", "trams", "A", "'rides' is the physical action verb."),
        ("He **keeps** out of traffic jams.", "keeps", "out", "traffic", "jams", "A", "'keeps' is the action verb."),
        ("The hippopotamus **walks** along the river bank.", "walks", "hippopotamus", "along", "river", "A", "'walks' is the physical action verb."),
        ("The hippo **swims** in the cool river.", "swims", "hippo", "cool", "river", "A", "'swims' is the physical action verb."),
        ("He **avoids** crowded vehicles in the city.", "avoids", "crowded", "vehicles", "city", "A", "'avoids' is the action verb."),
        ("The animal **enjoys** eating grass.", "enjoys", "animal", "eating", "grass", "A", "'enjoys' is the mental action verb."),
        ("Children **read** Arthur Guiterman's poem.", "read", "children", "poem", "Guiterman", "A", "'read' is the physical action verb."),
        ("The hippo **refuses** to ride in taxicabs.", "refuses", "hippo", "ride", "taxicabs", "A", "'refuses' is the action verb."),
        ("The heavy animal **moves** slowly.", "moves", "heavy", "animal", "slowly", "A", "'moves' is the physical action verb."),
        ("He **flavors** his meal with mustard.", "flavors", "meal", "mustard", "his", "A", "'flavors' is the action verb."),
        ("The hippo **protects** its territory.", "protects", "hippo", "territory", "its", "A", "'protects' is the action verb."),
        ("People **watch** the hippo at the zoo.", "watch", "people", "hippo", "zoo", "A", "'watch' is the action verb.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_verbs, start=1):
        qid = f"BK02_CH13_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in this sentence from or related to Chapter 13:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Action Verb Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Which word from the sentence is an **action verb**? 'The hippopotamus **slowly** **rolls** on **big** **limbs**.'", "rolls", "slowly", "big", "limbs", "A", "'rolls' shows physical action; 'slowly' is adverb, 'big' is adjective, 'limbs' is noun."),
        ("Identify BOTH action verbs in: 'He **tries** his best and **does** his duty.'", "tries, does", "best, duty", "he, tries", "does, best", "A", "'tries' and 'does' are both action verbs."),
        ("What is the past tense action verb of 'ride' as used in sentence ('He rode a tram')?", "rode", "rided", "riding", "rides", "A", "Past tense of ride is rode."),
        ("Choose the sentence where the underlined word is used as an ACTION VERB:", "He will **flavor** his food with mustard.", "The food has a nice **flavor**.", "I like this **flavor**.", "That is a sweet **flavor**.", "A", "In (A), 'flavor' acts as the main action verb."),
        ("Find the action verb in: 'He never rides in trucks or trams.'", "rides", "never", "trucks", "trams", "A", "'rides' is the physical action verb."),
        ("Which sentence contains NO physical action verb?", "The hippopotamus is strong and broad of bustle.", "He rolls along on big limbs.", "He eats food with mustard.", "He avoids traffic jams.", "A", "'The hippopotamus is strong and broad of bustle' contains linking verb 'is', but no physical action verb."),
        ("Change the action verb 'ride' to past tense: 'He never (ride) in a taxicab.'", "rode", "rided", "riding", "rides", "A", "Past tense of ride is rode."),
        ("Identify the action verb: 'The hippo swims in water and walks on land.'", "swims, walks", "hippo, water", "land, water", "walks, land", "A", "'swims' and 'walks' are action verbs."),
        ("Select the action verb that completes the sentence: 'The hippopotamus ____ traffic jams by walking.'", "avoids / escapes", "strong", "huge", "vehicle", "A", "'avoids' / 'escapes' is an action verb."),
        ("Which word is an action verb? (bustle, muscle, rolls, strong)", "rolls", "bustle", "muscle", "strong", "A", "'rolls' is an action verb; others are nouns/adjectives."),
        ("What action does the hippopotamus avoid according to the poem?", "rides / riding in trucks", "strong", "bustle", "mustard", "A", "He avoids riding in trucks or trams (action verb)."),
        ("Identify the action verb in: 'He cares about his principles.'", "cares", "principles", "about", "his", "A", "'cares' is a mental action verb."),
        ("Choose the correct action verb: 'He ____ his food with hippopotomustard.'", "flavors / seasons", "sweet", "huge", "food", "A", "'flavors' / 'seasons' is the action verb."),
        ("Identify the action verb in: 'He keeps out of traffic jams.'", "keeps", "out", "traffic", "jams", "A", "'keeps' is the action verb."),
        ("Which of these words is NOT an action verb? (roll, ride, eat, strong)", "strong", "roll", "ride", "eat", "A", "'strong' is an adjective; others are action verbs."),
        ("Identify the action verb in: 'The hippo splashes water with its tail.'", "splashes", "hippo", "water", "tail", "A", "'splashes' is the action verb."),
        ("Fill in the blank with an appropriate action verb: 'The hippopotamus ____ on its heavy legs.'", "stomps / rolls", "huge", "broad", "mustard", "A", "'stomps' / 'rolls' is an action verb."),
        ("What action verb completes the sentence? 'He ____ to do what he must.'", "strives / tries", "true", "just", "strong", "A", "'strives' / 'tries' is an action verb.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH13_CAT04_Q{idx:02d}"
        qtxt = f"Action Verb Grammar Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Action Verb Context & Tense", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence: 'The heavy hippopotamus gracefully rolls along and avoids traffic.' How many total ACTION VERBS are present?", "2 action verbs ('rolls', 'avoids')", "1 action verb", "3 action verbs", "0 action verbs", "A", "'rolls' and 'avoids' are action verbs; 'gracefully', 'heavy' are adverbs/adjectives."),
        ("Categorize the verbs: In 'The hippo **is** strong, so it **rolls** easily', classify 'is' and 'rolls'.", "'is' is a linking verb; 'rolls' is an action verb.", "Both are action verbs.", "Both are linking verbs.", "'is' is action; 'rolls' is linking.", "A", "'is' links state of being; 'rolls' shows action."),
        ("Replace the weak verb with a strong action verb: 'The hippo **goes** down the river.'", "The hippo **lumbers** down the river.", "The hippo **was near** the river.", "The hippo **saw** the river.", "The hippo **looked at** the water.", "A", "'lumbers' is a much stronger, descriptive action verb."),
        ("Identify the sentence with THREE distinct action verbs:", "The hippo **rolls** along, **flavors** its food, and **avoids** traffic jams.", "The hippo is strong, huge, and broad.", "He does not care for sweets like ice cream.", "Arthur Guiterman wrote the poem.", "A", "rolls, flavors, avoids are 3 distinct action verbs."),
        ("Differentiate verb types: Which underlined word is an ACTION verb?", "He **eats** food with mustard.", "The hippo was **strong**.", "His head was **huge**.", "The bustle was **broad**.", "A", "'eats' is an action verb."),
        ("Spot the incorrect verb tense: 'He **roll** along on big limbs yesterday.' Correct it for past simple:", "'rolled' is the past action verb form.", "'roll' should be 'rolling'.", "'roll' should be 'rolls'.", "'roll' should be 'will roll'.", "A", "Past simple of roll is rolled."),
        ("Form an action chain: Rearrange the story action verbs in correct order of occurrence: (rolls on limbs, rejects sweets, flavors food with mustard, avoids traffic)", "rolls on limbs -> rejects sweets -> flavors food with mustard -> avoids traffic", "avoids traffic -> flavors food -> rejects sweets -> rolls on limbs", "flavors food -> rolls on limbs -> avoids traffic -> rejects sweets", "rejects sweets -> avoids traffic -> rolls -> flavors", "A", "Chrono stanza order in poem."),
        ("Identify the verb error in dialogue: Child said, 'The hippo has **ride** in a tram!'", "'ride' is incorrect; the past participle form is 'ridden' ('has ridden').", "'ride' should be 'riding'.", "'ride' should be 'rides'.", "No error.", "A", "Perfect tense requires past participle 'ridden'."),
        ("Analyze this sentence: 'The hippopotamus **exemplifies** steadfast adherence to principles.' What type of action verb is 'exemplifies'?", "Demonstrative/representational action verb", "Physical movement verb", "Linking verb", "State of being verb", "A", "'exemplifies' is an action verb describing representation."),
        ("Which sentence uses action verbs to show cause and effect?", "He **walks** on foot, so he **avoids** traffic jams.", "The hippo is strong and broad of bustle.", "Arthur Guiterman wrote a funny poem.", "Ice cream and pie are sweet.", "A", "'walks' (cause action) -> 'avoids' (effect action)."),
        ("Spot the missing action verb: 'The hippo ____ its food and ____ away from noisy buses.'", "flavors, turns", "strong, huge", "was, was", "quick, slow", "A", "'flavors' and 'turns' complete sentence with vivid actions."),
        ("HOTS Reasoning: Why is 'upholds' in 'The hippo upholds its personal principles' considered an HONORABLE action verb?", "Because it describes actively supporting and defending moral standards.", "Because upholding requires climbing.", "Because hippo is big.", "Because it is a noun.", "A", "Descriptive action verb conveying moral support."),
        ("Transform the action verb to future tense: 'The hippopotamus **avoids** traffic tomorrow.'", "The hippopotamus **will avoid** traffic tomorrow.", "The hippopotamus **avoided** traffic tomorrow.", "The hippopotamus **is avoiding** traffic tomorrow.", "The hippopotamus **avoids** traffic tomorrow.", "A", "'will avoid' expresses future action."),
        ("Identify the sentence where the action verb matches the plural subject:", "The hippopotamuses **roll** along the river bank.", "The hippopotamuses **rolls** along the river bank.", "A hippopotamus **roll** along the river bank.", "The hippopotamuses **is rolling** along the river bank.", "A", "Plural subject 'hippopotamuses' takes base verb 'roll' in simple present.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH13_CAT04_Q{idx:02d}"
        qtxt = f"Higher Order Action Verb Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Action Verb Classification & Tense Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 5. Punctuation Marks (50 Qs)
# ---------------------------------------------------------------------------
def build_punctuation_marks():
    header = "# Category 5: Punctuation Marks & Capitalization — Chapter 13: Habits of the Hippopotamus\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_punct = [
        ("What punctuation mark should be placed at the end of: 'The hippopotamus is strong__'", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "Comma (,)", "A", "A statement ends with a full stop."),
        ("Which mark is used at the end of an asking sentence: 'What does the hippopotamus put on his food__'", "Question mark (?)", "Full stop (.)", "Comma (,)", "Exclamation mark (!)", "A", "A question ends with a question mark."),
        ("Which letter should ALWAYS be capitalized in an author's name like 'Arthur Guiterman'?", "First letter of each name (Arthur Guiterman)", "The last letter", "All letters", "No letters", "A", "Author names require capitalized initial letters."),
        ("Identify the punctuation mark used to separate items in a list: 'He avoids trucks__ trams__ and taxicabs.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Hyphen (-)", "A", "Commas separate items in a list."),
        ("Which punctuation mark shows sudden fun in: 'What a funny hippopotamus this is!__'", "Exclamation mark (!)", "Full stop (.)", "Comma (,)", "Question mark (?)", "A", "Exclamation marks express intense humor."),
        ("Select the proper noun (author's name) that MUST start with capital letters:", "Arthur Guiterman", "hippopotamus", "mustard", "tram", "A", "'Arthur Guiterman' as author's name starts with capital letters."),
        ("Which of the following is the symbol for a **full stop**?", ".", "?", "!", ",", "A", "Period/full stop is '.'"),
        ("Which of the following is the symbol for a **question mark**?", "?", ".", "!", ",", "A", "Question mark is '?'"),
        ("Which of the following is the symbol for an **exclamation mark**?", "!", "?", ".", ",", "A", "Exclamation mark is '!'"),
        ("Which word in this sentence should start with a CAPITAL letter? 'the poem is titled Habits of the Hippopotamus.'", "the -> The", "titled -> Titled", "poem -> Poem", "is -> Is", "A", "First word of sentence 'The' must start with a capital letter."),
        ("What punctuation mark goes in the box? 'He never rides in trucks or trams [ ]'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "A", "Comma pauses poetic line."),
        ("Which created portmanteau word is spelled and capitalized correctly in poem?", "hippopotomustard", "Hippopotomustard", "HIPPOPOTOMUSTARD", "hippo-poto-mustard", "A", "Standard lowercase wordplay term in poem text."),
        ("What mark goes after a speaker tag: 'Author said__ \"The hippopotamus is broad of bustle.\"'", "Comma (,)", "Question mark (?)", "Full stop (.)", "Exclamation mark (!)", "A", "Comma follows dialogue speaker tags."),
        ("Identify the correct capital letter for the pronoun 'I': 'he said, \"i like reading Arthur Guiterman's poems.\"'", "I", "i", "i'm", "I'm", "A", "Standalone pronoun 'I' is always capitalized."),
        ("Which option shows a sentence ending correctly?", "The hippopotamus keeps out of traffic jams.", "The hippopotamus keeps out of traffic jams?", "The hippopotamus keeps out of traffic jams,", "The hippopotamus keeps out of traffic jams;", "A", "Full stop at end of simple statement."),
        ("What mark is used in possessives like 'the **hippo's** bustle'?", "Apostrophe (')", "Comma (,)", "Full stop (.)", "Hyphen (-)", "A", "Apostrophe indicates possession."),
        ("Which poem title is capitalized correctly?", "Habits of the Hippopotamus", "habits of the hippopotamus", "Habits Of The Hippopotamus", "HABITS OF THE HIPPOPOTAMUS", "A", "Title capitalization (prepositions/articles lowercase unless first)."),
        ("What punctuation mark is used around poem line quotes: '___The hippopotamus is strong___'", "Quotation marks / Speech marks ( \" \" )", "Parentheses ( )", "Full stops ( . . )", "Commas ( , , )", "A", "Quotation marks enclose exact poem line quotes.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_punct, start=1):
        qid = f"BK02_CH13_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Punctuation & Capitalization Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Identify the sentence with CORRECT capitalization and punctuation:", "The poem \"Habits of the Hippopotamus\" was written by Arthur Guiterman.", "the poem \"habits of the hippopotamus\" was written by arthur guiterman.", "The poem \"habits Of The Hippopotamus\" was written by Arthur guiterman?", "the Poem \"Habits of the Hippopotamus\" Was Written By Arthur Guiterman.", "A", "Title \"Habits of the Hippopotamus\", author Arthur Guiterman capitalized; period at end."),
        ("Which sentence is punctuated as a CORRECT question?", "Why does the hippopotamus avoid traffic jams?", "Why does the hippopotamus avoid traffic jams.", "Why does the hippopotamus avoid traffic jams!", "Why does the hippopotamus avoid traffic jams,", "A", "Question starting with 'Why' ends with question mark ?"),
        ("Spot the capitalization mistake in: 'arthur Guiterman wrote a witty poem.'", "'arthur' should be capitalized ('Arthur'); 'Guiterman' is correct.", "'Guiterman' should be lowercase.", "'poem' should be uppercase.", "No mistake.", "A", "First name 'Arthur' must be capitalized."),
        ("Choose the correctly punctuated dialogue sentence:", "\"The hippo takes hippopotomustard,\" said Arthur Guiterman.", "the hippo takes hippopotomustard said Arthur Guiterman.", "\"The hippo takes hippopotomustard\" said Arthur Guiterman", "The hippo takes hippopotomustard, said Arthur Guiterman.", "A", "Quotation marks around dialogue, comma inside quote, capital T."),
        ("Identify where a COMMA is missing: 'He does not care for ice cream apple pie or custard.'", "Between 'ice cream' and 'apple pie' ('ice cream, apple pie')", "After 'He'", "After 'custard'", "No comma needed", "A", "Commas separate list items: 'ice cream, apple pie or custard'."),
        ("Which sentence uses the apostrophe correctly for possession?", "This is the hippopotamus's tail.", "This is the hippopotamuses' tail.", "This is the hippopotamus tail.", "This is the hippopotamus's' tail.", "A", "hippopotamus's indicates singular possession."),
        ("Select the sentence with CORRECT punctuation for an exclamatory statement:", "What a strong and broad animal the hippopotamus is!", "What a strong and broad animal the hippopotamus is?", "What a strong and broad animal the hippopotamus is.", "What a strong and broad animal the hippopotamus is,", "A", "Exclamatory statement ends with exclamation mark !"),
        ("Which contraction is written correctly for 'does not'?", "doesn't", "does'nt", "doesnt'", "d'oesnt", "A", "doesn't is standard contraction."),
        ("Find the sentence with NO capitalization errors:", "Arthur Guiterman wrote a poem about a hippopotamus.", "arthur guiterman wrote a poem about a hippopotamus.", "Arthur Guiterman Wrote A Poem About A Hippopotamus.", "arthur Guiterman wrote a poem.", "A", "'Arthur Guiterman' capitalized as proper name."),
        ("What punctuation mark belongs in the blank? 'The child laughed, \"He takes hippopotomustard!\"'", "!", ".", "?", ",", "A", "Exclamation mark ! expresses laughter/fun."),
        ("Choose the correct form for 'is not':", "isn't", "is'nt", "isnt'", "i'snt", "A", "isn't is standard contraction."),
        ("Identify the punctuation error: 'The hippo is strong, he is broad of bustle.'", "Comma splice between two independent clauses (should be semicolon or 'and').", "Missing question mark.", "Missing capital letters.", "No error.", "A", "Two complete sentences separated only by comma."),
        ("Select the sentence with proper use of capital letters for author and poem title:", "Arthur Guiterman wrote \"Habits of the Hippopotamus\" in America.", "arthur guiterman wrote \"habits of the hippopotamus\" in america.", "Arthur guiterman wrote \"Habits of the hippopotamus\" in America.", "arthur Guiterman wrote \"Habits of the Hippopotamus\" in america.", "A", "Names 'Arthur Guiterman', 'Habits of the Hippopotamus', 'America' all capitalized."),
        ("Which sentence correctly uses an apostrophe for possessive noun?", "The hippo's limbs are big with muscle.", "The hippos' limbs are big with muscle.", "The hippos limbs are big with muscle.", "The hippo's' limbs are big with muscle.", "A", "hippo's indicates singular possession."),
        ("Identify the correct punctuation for a list of items: 'The hippo rejects ____'", "sweets, ice cream, and custard.", "sweets ice cream and custard.", "sweets; ice cream; and custard.", "sweets: ice cream: and custard.", "A", "Commas separate items in list."),
        ("Choose the sentence that correctly asks a question about the story:", "Why does the hippopotamus avoid riding in omnibuses?", "Why does the hippopotamus avoid riding in omnibuses.", "Why does the hippopotamus avoid riding in omnibuses!", "why does the hippopotamus avoid riding in omnibuses.", "A", "Capital W, ends with question mark ?"),
        ("Fix the sentence: 'who wrote habits of the hippopotamus'", "Who wrote \"Habits of the Hippopotamus\"?", "Who wrote habits of the hippopotamus.", "who wrote Habits of the Hippopotamus!", "Where is Guiterman?", "A", "Capital W, title quotes, ends with ?"),
        ("Which of these sentences is punctuated PERFECTLY?", "Arthur Guiterman wrote, \"He always tries his best!\"", "Arthur Guiterman wrote \"he always tries his best!\"", "arthur Guiterman wrote, \"He always tries his best!\"", "Arthur Guiterman wrote, \"He always tries his best.\"", "A", "Capital A, comma after wrote, speech marks around dialogue with ! inside.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH13_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Context Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Punctuation Application & Dialogue Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze and count ALL capitalization and punctuation errors in: 'on friday arthur guiterman wrote a poem where hippo eats hippopotomustard'", "5 errors (on->On, friday->Friday, arthur guiterman->Arthur Guiterman, quotation marks, capital H in Hippo, period)", "2 errors", "3 errors", "7 errors", "A", "Starts sentence, day name, author name, quotation marks, capital H, period."),
        ("Correct the entire dialogue paragraph: 'the child asked why does he eat mustard the poet replied to flavor his food'", "\"Why does he eat mustard?\" asked the child. The poet replied, \"To flavor his food.\"", "the child asked \"why does he eat mustard\" the poet replied \"to flavor his food.\"", "The child asked, Why does he eat mustard. The poet replied, To flavor his food.", "\"Why does he eat mustard?\" Asked the child. The poet replied \"To flavor his food?\"", "A", "Full proper quotation, dialogue tags, capitalization, and terminal punctuation."),
        ("Distinguish between singular possessive and contraction: 'The hippo**'**s head is huge, and it**'**s a strong animal.'", "First 's is possessive (head of the hippo); second 's is contraction (it is).", "Both are possessive.", "Both are contractions.", "First is contraction; second is possessive.", "A", "hippo's head = head of the hippo; it's = it is."),
        ("Spot the subtle punctuation flaw in this dialogue: '\"He avoids traffic jams,\" Said Arthur Guiterman.'", "'Said' should be lowercase 'said' because it continues the dialogue tag outside quotation marks.", "'He' should be lowercase.", "Commas should be outside quotes.", "No flaw.", "A", "Dialogue tags following quotes start with lowercase unless proper nouns."),
        ("Which sentence correctly uses punctuation to show contrast?", "He does not care for sweets, but he loves mustard.", "He does not care for sweets but, he loves mustard.", "He does not care for sweets but he loves mustard!", "He does not care for sweets; but he loves mustard?", "A", "Comma before coordinating conjunction 'but' joining two independent clauses."),
        ("Reconstruct with perfect punctuation: 'arthur guiterman wrote habits of the hippopotamus on friday 10th december 1930'", "Arthur Guiterman wrote \"Habits of the Hippopotamus\" on Friday, 10th December 1930.", "arthur guiterman wrote habits of the hippopotamus on friday, 10th december 1930.", "Arthur Guiterman wrote Habits of the Hippopotamus on Friday 10th December 1930", "Arthur guiterman wrote Habits of the Hippopotamus on friday 10th december 1930.", "A", "Author name, title quotes, Friday, 10th December 1930, period."),
        ("Identify why exclamation mark is necessary here: '\"He takes a little hippopotomustard!\"'", "Because the speaker is highlighting a humorous and playful portmanteau word.", "Because hippo is big.", "Because mustard is spicy.", "Because sentence is long.", "A", "Exclamation mark communicates humorous delight in wordplay."),
        ("Choose the correctly punctuated sentence containing an appositive phrase:", "Arthur Guiterman, a humorous American poet, wrote this poem.", "Arthur Guiterman a humorous American poet wrote this poem.", "Arthur Guiterman, a humorous American poet wrote this poem.", "Arthur Guiterman a humorous American poet, wrote this poem.", "A", "Appositive phrase 'a humorous American poet' is set off by commas."),
        ("Analyze the use of portmanteau words in poem text: 'hippopotomuscle', 'hippopotomustard', 'hippopotomust'", "Portmanteau words blend 'hippopotamus' with 'muscle', 'mustard', and 'must' for poetic humor.", "They replace commas.", "They indicate questions.", "They are proper names.", "A", "Nonsense wordplay portmanteaus created for comedic rhyme."),
        ("Identify the correct sentence with direct speech quote within text:", "The poet wrote, \"He never rides in trucks or trams,\" and children laughed.", "The poet wrote \"He never rides in trucks or trams\" and children laughed.", "The poet wrote, 'He never rides in trucks or trams,' and children laughed.", "The poet wrote: \"He never rides in trucks or trams\" and children laughed.", "A", "Comma before quote, double quotation marks around direct speech, comma inside quote."),
        ("Spot the missing apostrophe: 'The hippos limbs are big with muscle.'", "Missing apostrophe in 'hippo's' -> 'The hippo's limbs...'", "Missing apostrophe in 'limbs''", "Missing apostrophe in 'muscle''", "No apostrophe needed", "A", "'The hippo's limbs' requires possessive apostrophe."),
        ("HOTS Reasoning: Why does putting a comma in different places change meaning? Compare: 'Hippo, said Arthur, is strong.' vs 'Hippo said, \"Arthur is strong.\"'", "In the first, Arthur says the hippo is strong; in the second, the hippo says Arthur is strong.", "Both mean the exact same thing.", "The first is a question.", "Commas do not affect meaning.", "A", "Punctuation alters who speaks and who is praised."),
        ("Correct all 4 errors in: 'whats the hippos habits asked the student'", "\"What are the hippo's habits?\" asked the student.", "whats the hippos habits? asked the student.", "\"What's the hippos habits.\" asked the student.", "\"whats the hippos habits?\" Asked the student.", "A", "Quotation marks, capital W, possessive hippo's, question mark, period at end."),
        ("Identify the rule for capitalizing titles of short humorous poems like \"Habits of the Hippopotamus\":", "Titles of poems take initial capital letters (except minor prepositions/articles) and are enclosed in quotation marks.", "Poem titles are never capitalized.", "Poem titles are capitalized only at end of line.", "Poem titles must be written in ALL CAPS.", "A", "Short poem titles take initial capitals and quotation marks.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH13_CAT05_Q{idx:02d}"
        qtxt = f"Higher Order Punctuation Analysis & Dialogue Formatting:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Punctuation & Dialogue Editing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 6. Phonics & Vowel Digraphs (50 Qs)
# ---------------------------------------------------------------------------
def build_phonics_digraphs():
    header = "# Category 6: Phonics & Vowel Digraphs — Chapter 13: Habits of the Hippopotamus\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_phonics = [
        ("Which vowel digraph is present in the word **'sweet'** (in Chapter 13)?", "ee", "ea", "ai", "ou", "A", "'ee' is the vowel digraph in sweet."),
        ("Identify the vowel digraph in the word **'pie'** (in apple pie):", "ie", "ee", "oa", "ui", "A", "'ie' forms the long /i/ vowel sound in pie."),
        ("Which word from the poem contains the **'ea'** vowel digraph?", "head", "bustle", "limb", "truck", "A", "'head' contains the 'ea' digraph."),
        ("Identify the vowel digraph in the word **'clean'**:", "ea", "ee", "ow", "oo", "A", "'ea' forms long /e/ sound in clean."),
        ("Which vowel digraph appears in the word **'paid'**?", "ai", "ay", "ea", "oa", "A", "'ai' makes long /a/ sound in paid."),
        ("Find the word with the **'ea'** vowel digraph: 'He eats food with flavor.'", "eats", "food", "flavor", "with", "A", "'eats' contains 'ea' vowel digraph."),
        ("Which word from the poem rhymes with **'bustle'**?", "hippopotomuscle", "battle", "bottle", "beetle", "A", "'hippopotomuscle' rhymes with 'bustle'."),
        ("Which word from the poem rhymes with **'custard'**?", "hippopotomustard", "mustard", "both A and B", "neither", "C", "'hippopotomustard' and 'mustard' rhyme with 'custard'."),
        ("Identify the vowel digraph in the word **'boasted'**:", "oa", "ou", "ow", "oo", "A", "'oa' makes long /o/ sound in boasted."),
        ("Which word from the poem rhymes with **'just'**?", "hippopotomust", "must", "both A and B", "neither", "C", "'hippopotomust' and 'must' rhyme with 'just'."),
        ("Identify the vowel digraph in **'cream'** (as in ice cream):", "ea", "ee", "oo", "ui", "A", "'ea' makes long /e/ sound in cream."),
        ("Which word from Chapter 13 has the **'ea'** digraph making a short /e/ sound?", "head", "eats", "sweet", "pie", "A", "'head' has 'ea' making short /e/ sound."),
        ("Which word rhymes with **'day'**?", "away", "die", "due", "door", "A", "'away' rhymes with 'day'."),
        ("Identify the silent letters in **'high'** (as in 'high peak'):", "gh", "h", "i", "g", "A", "Silent 'gh' in high."),
        ("Which word from the story has long /i/ sound spelled with **'ie'**?", "pie", "bought", "bowl", "baker", "A", "'ie' in pie makes long /i/ sound."),
        ("Find the word with **'ou'** digraph: 'They walked around the hippopotamus.'", "around", "hippopotamus", "walked", "they", "A", "'around' contains 'ou' digraph."),
        ("Which word rhymes with **'jam'**?", "tram", "jim", "job", "gem", "A", "'tram' rhymes with 'jam'."),
        ("Identify the silent letter in the word **'know'** (as in 'did not know'):", "k", "n", "o", "w", "A", "Initial 'k' before 'n' is silent.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_phonics, start=1):
        qid = f"BK02_CH13_CAT06_Q{idx:02d}"
        qtxt = f"Phonics & Vowel Digraph Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Vowel Digraphs & Rhyming Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Compare the **'ea'** digraph sound in **'eats'** and **'head'**. What is the difference?", "'eats' has long /e/ sound; 'head' has short /e/ sound.", "Both have short /e/ sound.", "Both have long /a/ sound.", "'eats' has short /e/; 'head' has long /e/.", "A", "'ea' can make long /e/ (eats) or short /e/ (head)."),
        ("Select the word pair from Chapter 13 that has the SAME vowel sound pattern:", "pie - try", "head - sweet", "bustle - roar", "eats - head", "A", "'pie' (ie) and 'try' (y) both make long /i/ sound."),
        ("Which word contains SILENT letters? (high, limb, pie, tram)", "high / limb", "pie", "tram", "bustle", "A", "'high' (silent gh) and 'limb' (silent b)."),
        ("Identify the odd one out based on vowel sound: (sweet, cream, eats, head)", "head", "sweet", "cream", "eats", "A", "'head' has short /e/ sound; others have long /e/ sound."),
        ("Which digraph completes the word for dessert? 'p__'", "ie", "ee", "ai", "ou", "A", "'pie' uses 'ie' digraph."),
        ("Group these story words by rhyming sound: **bustle**, **hippopotomuscle**. What sound do they share?", "le / uscle ending rhyme", "ow", "oo", "oi", "A", "Both share -uscle / -ustle ending rhyme."),
        ("Find the word with consonant digraph **'th'** from the story: 'The limbs on **which** / **with** he rolls...'", "with", "limbs", "rolls", "big", "A", "'with' contains unvoiced 'th' consonant digraph."),
        ("Which of these words has the **'ow'** vowel digraph making long /o/ sound? (know, show, blow, all of these)", "all of these", "know", "show", "blow", "A", "know, show, blow all share 'ow' long /o/ sound."),
        ("Identify the vowel digraph in **'sweet'**:", "ee", "ae", "ur", "or", "A", "'ee' is the vowel digraph in sweet."),
        ("Which word from the story has silent **'b'**? (limb, thumb, lamb, all of these)", "all of these", "limb", "thumb", "lamb", "A", "limb, thumb, lamb all have silent final 'b' after 'm'."),
        ("Select the rhyming pair from the poem: 'bustle' and ____.", "hippopotomuscle", "custard", "mustard", "trams", "A", "'bustle' rhymes with 'hippopotomuscle' in the poem."),
        ("Select the rhyming pair from the poem: 'custard' and ____.", "hippopotomustard", "bustle", "just", "trams", "A", "'custard' rhymes with 'hippopotomustard' in the poem."),
        ("Select the rhyming pair from the poem: 'just' and ____.", "hippopotomust", "custard", "trams", "jams", "A", "'just' rhymes with 'hippopotomust' in the poem."),
        ("Select the rhyming pair from the poem: 'omnibuses' and ____.", "hippopotomusses", "trams", "jams", "bustle", "A", "'omnibuses' rhymes with 'hippopotomusses' in the poem."),
        ("Which word contains the **'oi'** diphthong/digraph? (choice, voice, point, all of these)", "all of these", "choice", "voice", "point", "A", "choice, voice, point all contain 'oi'."),
        ("Identify the soft **'c'** sound in Chapter 13 vocabulary: (ice, space, center, all of these)", "all of these", "ice", "space", "center", "A", "ice, space, center all have soft /s/ sound for 'c' before 'e' or 'i'."),
        ("Which word has a soft **'g'** sound? (germ, magic, region, all of these)", "all of these", "germ", "magic", "region", "A", "germ, magic, region all have soft /j/ sound for 'g'."),
        ("Choose the correct spelling with **'ea'** digraph for body part:", "head", "hed", "heade", "hied", "A", "head is standard spelling with 'ea'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH13_CAT06_Q{idx:02d}"
        qtxt = f"Phonics Analysis & Sound Pattern Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Phonic Rules & Sound Discrimination", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the phonics rule: Why does 'c' in **'ice'** sound like /s/, but 'c' in **'custard'** sounds like /k/?", "Because 'c' followed by 'e', 'i', or 'y' makes soft /s/ sound (ice); before 'u', 'a', 'o' it makes hard /k/ sound (custard).", "Because ice is cold.", "Because custard is yellow.", "There is no rule.", "A", "Soft 'c' rule: c + e, i, y = /s/ sound."),
        ("Categorize the 'ea' digraphs into long /e/ vs short /e/: (eats, cream, head, heavy, lead [metal])", "Long /e/: eats, cream; Short /e/: head, heavy, lead [metal]", "All are long /e/.", "All are short /e/.", "Long /e/: head; Short /e/: eats", "A", "eats, cream make long /e/; head, heavy, lead (metal) make short /e/."),
        ("Identify the word pair where SILENT letters exist in BOTH words:", "limb - know", "pie - sweet", "head - bustle", "truck - tram", "A", "'limb' (silent b) and 'know' (silent k)."),
        ("Decode the phonics blend: Which word contains a 2-letter consonant blend at the start?", "sweet / tram / truck", "limb", "pie", "head", "A", "'sw' / 'tr' blend type."),
        ("Examine the soft 'c' rule: Why is 'c' soft in **'taxicab (c before a is hard, but c in taxicab)'** vs soft 'c' in **'ice'**?", "'c' followed by 'e' makes soft /s/ sound (ice); 'c' before 'a' makes hard /k/ sound (taxicab).", "Because taxicab is a car.", "Because ice is cold.", "There is no rule.", "A", "Soft 'c' rule: c + e = /s/ sound."),
        ("Find the word with BOTH a vowel digraph AND a silent letter:", "highest", "sweet", "pie", "head", "A", "'highest' has 'igh' trigraph with silent 'gh'."),
        ("Differentiate diphthongs: Which pair produces the /ow/ sound as in **'around'**?", "around - house", "voice - coin", "paid - day", "boat - coat", "A", "'around' and 'house' share /ow/ diphthong sound."),
        ("Analyze homophones: 'The hippo has big **limbs** / **limms**.' Which word means legs/arms?", "limbs", "limms", "lims", "lymphes", "A", "'limbs' (body parts with silent b) is standard spelling."),
        ("Identify the phonic pattern in **'hippopotamus'**: How many syllables are in this word?", "5 syllables (hip-po-pot-a-mus)", "4 syllables", "6 syllables", "3 syllables", "A", "hip-po-pot-a-mus has 5 syllables."),
        ("Sort by ending sound: Which word ends with the /z/ sound? (trams, jams, limbs, cabs)", "trams / jams / limbs / cabs", "sweets", "trucks", "musses", "A", "Plurals ending in voiced consonants take /z/ ending sound (trams, jams, limbs)."),
        ("Spot the word where 'b' is SILENT: (limb, thumb, lamb, all of these)", "all of these", "limb", "thumb", "lamb", "A", "'b' is silent after 'm' in limb, thumb, lamb."),
        ("HOTS Reasoning: Why did Arthur Guiterman invent portmanteau words like 'hippopotomustard'?", "To create humorous perfect rhymes that match the multi-syllable word 'hippopotamus'.", "Because he forgot real words.", "Because hippos eat mustard.", "Because trucks are noisy.", "A", "Comedic portmanteau creation for multi-syllabic rhyming."),
        ("Identify the compound word from story concepts containing two simple words:", "taxicab / ice-cream", "hippopotamus", "Guiterman", "omnibus", "A", "taxicab = taxi + cab; ice-cream = ice + cream."),
        ("Determine the syllable count and stress: How many syllables are in **'hippopotomustard'**?", "6 syllables (hip-po-po-to-mus-tard)", "5 syllables", "7 syllables", "4 syllables", "A", "hip-po-po-to-mus-tard has 6 syllables.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH13_CAT06_Q{idx:02d}"
        qtxt = f"Higher Order Phonics & Orthographic Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Phonetic Rules & Homophone Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 7. Question Words & Interrogatives (50 Qs)
# ---------------------------------------------------------------------------
def build_question_words():
    header = "# Category 7: Question Words & Interrogatives — Chapter 13: Habits of the Hippopotamus\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_qwords = [
        ("___ is described as strong and huge of head in the poem?", "What / Which animal", "Who", "Where", "Why", "A", "'What animal' asks about 'The hippopotamus'."),
        ("___ are the limbs of the hippopotamus described?", "How", "Who", "Where", "Why", "A", "'How' asks about description ('big with hippopotomuscle')."),
        ("___ does the hippopotamus NOT greatly care for?", "What", "Who", "Where", "Why", "A", "'What' asks about food ('sweets like ice cream, apple pie or custard')."),
        ("___ does the hippopotamus take to flavor what he eats?", "What", "Who", "Where", "Why", "A", "'What' asks about condiment ('A little hippopotomustard')."),
        ("___ is the hippopotamus true to?", "What", "Who", "Where", "Why", "A", "'What' asks about values ('all his principles')."),
        ("___ does the hippopotamus always try his best to do?", "What", "Who", "Where", "Why", "A", "'What' asks about actions ('The things one hippopotomust')."),
        ("___ vehicles does the hippopotamus NEVER ride in?", "Which", "Who", "Where", "Why", "A", "'Which vehicles' asks about 'trucks, trams, taxicabs, or omnibuses'."),
        ("___ does the hippopotamus keep out of by avoiding vehicles?", "What", "Who", "Where", "Why", "A", "'What' asks about situations ('traffic jams and other hippopotomusses')."),
        ("___ wrote the poem 'Habits of the Hippopotamus'?", "Who", "What", "Where", "Why", "A", "'Who' asks about author (Arthur Guiterman)."),
        ("___ does the word 'bustle' mean in the poem?", "What", "Who", "Where", "Why", "A", "'What' asks about meaning ('rear part of body')."),
        ("___ does the hippopotamus roll along?", "Where / How", "Who", "Why", "When", "A", "'How' or 'Where' asks about locomotion ('on his big limbs')."),
        ("___ sweet treats are mentioned in stanza 2?", "Which", "Who", "Where", "Why", "A", "'Which sweet treats' asks for 'ice cream, apple pie or custard'."),
        ("___ kind of head does the hippopotamus have?", "What kind of", "Who", "Where", "Why", "A", "'What kind of' asks about physical feature ('huge of head')."),
        ("___ kind of bustle does the hippopotamus have?", "What kind of", "Who", "Where", "Why", "A", "'What kind of' asks about physical feature ('broad of bustle')."),
        ("___ is the hippopotamus always trying to be?", "What", "Who", "Where", "Why", "A", "'What' asks about disposition ('just and true to principles')."),
        ("___ wordplay term means hippo muscles in the poem?", "Which", "Who", "Where", "Why", "A", "'Which wordplay term' asks for 'hippopotomuscle'."),
        ("___ wordplay term means hippo mustard in the poem?", "Which", "Who", "Where", "Why", "A", "'Which wordplay term' asks for 'hippopotomustard'."),
        ("___ wordplay term means hippo duty in the poem?", "Which", "Who", "Where", "Why", "A", "'Which wordplay term' asks for 'hippopotomust'.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_qwords, start=1):
        qid = f"BK02_CH13_CAT07_Q{idx:02d}"
        qtxt = f"Choose the correct **question word** (Who, What, Where, Why, How, When):\n\n\"{q_blank} _____?\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Question Word Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Match question to answer: Question: '___ does the hippo avoid trucks and trams?' Answer: 'To keep out of traffic jams.'", "Why", "What", "Where", "Who", "A", "'Why' asks for reasons ('To keep out of...')."),
        ("Match question to answer: Question: '___ does the hippopotamus live?' Answer: 'Near river banks and open plains.'", "Where", "Who", "Why", "When", "A", "'Where' asks for location."),
        ("Choose the correct question word for MANNER: '___ does the hippopotamus move on its limbs?'", "How", "Where", "Who", "Why", "A", "'How' inquires about manner ('rolls along')."),
        ("Form an asking sentence: 'The hippo eats mustard.' -> '____ does the hippo put on his food?'", "What", "Who", "Why", "Where", "A", "'What' inquires about item."),
        ("Identify the INCORRECT question word usage: '**Why** wrote Habits of the Hippopotamus?'", "'Why' should be 'Who'", "'Why' should be 'Where'", "'Why' should be 'When'", "No error", "A", "'Who wrote...' asks for author identity."),
        ("Select the proper interrogative sentence:", "Why does the hippopotamus refuse to ride in taxicabs?", "Why the hippopotamus refuses to ride in taxicabs?", "Why does the hippopotamus refused?", "Why hippo refuses?", "A", "Interrogative word + auxiliary 'does' + subject + base verb."),
        ("Which question word asks about DEGREE or SIZE? '___ huge is the head of the hippopotamus?'", "How", "Who", "What", "Where", "A", "'How huge' measures degree/size."),
        ("Complete the question: '___ of the sweet treats is NOT a pie?'", "Which", "What", "Where", "Why", "A", "'Which' chooses between specific options (ice cream / custard)."),
        ("Change statement to question: 'The hippo avoids traffic jams.' -> '____ does the hippo avoid?'", "What", "Who", "Why", "Where", "A", "'What' asks for object."),
        ("Fill in the blank: '___ strong is the hippopotamus?'", "How", "What", "Where", "Why", "A", "'How strong' measures degree."),
        ("Identify the question word in: 'Whom does the hippo try to be true to?'", "Whom", "does", "hippo", "try", "A", "'Whom' / 'What' asks about principles/self."),
        ("Choose the question that matches this answer: 'A little hippopotomustard.'", "What does the hippo add for flavor?", "Where does the hippo ride?", "Who wrote the poem?", "What is a bustle?", "A", "'What does the hippo add for flavor?' matches answer."),
        ("Fill in the blank: '___ created wordplay term means messes in the poem?'", "Which", "Who", "Why", "Where", "A", "'Which word' asks for identification (hippopotomusses)."),
        ("Complete: '___ vehicles are listed in stanza 4?'", "How many", "How much", "Who", "Where", "A", "'How many' asks about countable quantity (4: trucks, trams, taxicabs, omnibuses)."),
        ("Select the correct question for: 'The limbs on which he rolls along are big with hippopotomuscle.'", "Why are the hippo's limbs so big?", "Where is the taxicab?", "Why does he eat pie?", "Who is Arthur Guiterman?", "A", "'Why are the hippo's limbs so big?' asks for description."),
        ("Which question word inquires about POSSESSION? '___ bustle is broad?'", "Whose", "Who", "Where", "Why", "A", "'Whose bustle' asks about subject."),
        ("Form question: 'The poem has 4 stanzas.' -> '____ stanzas does the poem have?'", "How many", "How much", "Why", "Where", "A", "'How many' asks for countable number."),
        ("Identify the question mark error: 'Why does the hippo avoid omnibuses.' Correct it:", "Why does the hippo avoid omnibuses?", "Why does the hippo avoid omnibuses!", "Why does the hippo avoid omnibuses,", "Why does the hippo avoid omnibuses;", "A", "Questions must end with question mark ?")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH13_CAT07_Q{idx:02d}"
        qtxt = f"Question Formation & Context Alignment:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Interrogative Sentence Formation", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence structure: 'Why does the hippopotamus avoid riding in trucks, trams, taxicabs, and omnibuses?' What is the syntax pattern?", "Question Word + Helping Verb (does) + Subject (the hippopotamus) + Main Verb (avoid) + Gerund Phrase + List of Nouns", "Question Word + Main Verb + Subject", "Subject + Question Word + Verb", "Helping Verb + Question Word + Subject", "A", "Standard English question syntax."),
        ("Differentiate between 'How many' vs 'How much': '___ vehicles' vs '___ mustard'", "'How many' for countable vehicles; 'How much' for uncountable mustard.", "Both use 'How many'.", "Both use 'How much'.", "'How much' for vehicles; 'How many' for mustard.", "A", "Countable nouns take 'How many'; uncountable nouns take 'How much'."),
        ("Spot the syntax error in question: 'Where the hippopotamus rolls along?' Correct it:", "Where **does** the hippopotamus roll along?", "Where the hippopotamus rolls along?", "Where rolled the hippopotamus?", "Where do the hippopotamus roll along?", "A", "Present simple questions require auxiliary 'does' before singular subject 'the hippopotamus' and base verb 'roll'."),
        ("Framing multi-question interview: What sequence of question words logically reveals the poem's humor?", "What does the hippo look like -> What does he eat -> What does he avoid -> Why does he use funny wordplay", "How -> Who -> Why -> What", "Where -> Where -> Where -> Where", "Why -> Why -> Why -> Why", "A", "Reveals physical appearance, food preferences, habits, and poetic wordplay."),
        ("Transform the statement into a formal question: 'Arthur Guiterman uses portmanteau wordplay to create humorous poetry.'", "How does Arthur Guiterman construct portmanteau words to achieve humorous poetic effects?", "Where is the hippo?", "Who is Guiterman?", "What is a bus?", "A", "Directly targets poetic technique."),
        ("Analyze this ambiguous question: 'What does he eat?' How can it be made precise?", "Add specific context: 'What savory condiment does the hippopotamus add to his food instead of sweet treats?'", "Make it shorter: 'What eat?'", "Change to: 'Where eat?'", "Remove 'What'.", "A", "Adding specific context clarifies which food preference."),
        ("Choose the correct question pair for dialogue: Child: '___ does the hippo not ride in trams?' Author: '___ about keeping out of traffic jams?'", "Why, How", "Who, Where", "Where, How", "When, Whose", "A", "Why (reason for avoiding trams), How about (explanation)."),
        ("Spot the DOUBLE auxiliary error: 'Why does the hippo avoided traffic jams?'", "'does' requires base verb 'avoid', not past tense 'avoided'.", "'does' should be 'is'.", "'Why' should be 'How'.", "No error.", "A", "Auxiliary 'does' must be followed by base form of verb ('avoid')."),
        ("Reconstruct question from answer: Answer: 'The hippopotamus adds a little hippopotomustard to flavor his food.'", "Question: 'What does the hippopotamus add to flavor his food?'", "Question: 'Where did they run?'", "Question: 'Who bought a bus?'", "Question: 'Why is mustard yellow?'", "A", "Targets condiment addition."),
        ("Form indirect question: 'The student asked why the hippo did not like sweets.' What is the sentence type?", "Assertive statement containing an embedded indirect question.", "Direct question requiring question mark.", "Exclamatory sentence.", "Command.", "A", "Indirect questions are statements ending with full stop."),
        ("Identify the correct question word for moral reasoning: '___ is staying true to one's principles an important virtue emphasized in stanza 3?'", "Why", "What", "Who", "Where", "A", "'Why' inquires into the moral reason."),
        ("HOTS Reasoning: Why is 'Who' used for the poet but 'Which' used when selecting from invented portmanteau words?", "'Who' is used for human poet Arthur Guiterman; 'Which' is used when selecting from defined linguistic options.", "'Who' is for inanimate objects.", "'Which' is only for numbers.", "Both are identical.", "A", "'Which of the words...' selects from defined wordplay options."),
        ("Correct all errors in: 'why does the hippo avoid traffic jams in the poem'", "Why does the hippo avoid traffic jams in the poem?", "Why does the hippo avoid traffic jams in the poem.", "Whom does the hippo avoid traffic jams?", "Why do the hippo avoid traffic jams?", "A", "Capital W, question mark at end."),
        ("Select the question that evaluates Higher Order Thinking (HOTS) about Chapter 13:", "How does Arthur Guiterman's invention of words like 'hippopotomustard' and 'hippopotomust' enhance both the rhythm and comedic tone of the poem?", "What does the hippo eat?", "Where are traffic jams?", "Who wrote the poem?", "A", "Asks student to evaluate linguistic invention, poetic rhythm, and comedic tone.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH13_CAT07_Q{idx:02d}"
        qtxt = f"Higher Order Interrogative Analysis & Syntax:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Question Syntax & Analytical Framing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 8. Present Continuous Tense (-ing) (50 Qs)
# ---------------------------------------------------------------------------
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense (-ing) — Chapter 13: Habits of the Hippopotamus\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_ing = [
        ("The hippopotamus is **rolling** along on big limbs.", "rolling", "hippopotamus", "is", "limbs", "A", "'rolling' is verb + -ing form."),
        ("The hippo is **eating** food with mustard.", "eating", "hippo", "is", "mustard", "A", "'eating' is verb + -ing form."),
        ("The hippo is **trying** his best to do his duty.", "trying", "hippo", "is", "duty", "A", "'trying' is verb + -ing form."),
        ("The hippo is **avoiding** traffic jams.", "avoiding", "hippo", "is", "jams", "A", "'avoiding' is verb + -ing form."),
        ("The animal is **walking** near the river bank.", "walking", "animal", "is", "bank", "A", "'walking' is verb + -ing form."),
        ("The hippo is **swimming** in the deep water.", "swimming", "hippo", "is", "water", "A", "'swimming' is verb + -ing form."),
        ("The poet is **inventing** funny words like hippopotomustard.", "inventing", "poet", "is", "words", "A", "'inventing' is verb + -ing form."),
        ("The sun is **shining** on the river.", "shining", "sun", "is", "river", "A", "'shining' is verb + -ing form."),
        ("The hippo is **flavoring** his food with mustard.", "flavoring", "hippo", "is", "food", "A", "'flavoring' is verb + -ing form."),
        ("Children are **laughing** at the poem.", "laughing", "children", "are", "poem", "A", "'laughing' is verb + -ing form."),
        ("The hippo is **staying** out of buses and trams.", "staying", "hippo", "is", "buses", "A", "'staying' is verb + -ing form."),
        ("The big limbs are **moving** smoothly.", "moving", "limbs", "are", "smoothly", "A", "'moving' is verb + -ing form."),
        ("The hippo is **following** his principles.", "following", "hippo", "is", "principles", "A", "'following' is verb + -ing form."),
        ("Vehicles are **causing** traffic jams in the city.", "causing", "vehicles", "are", "city", "A", "'causing' is verb + -ing form."),
        ("The hippo is **enjoying** a peaceful day.", "enjoying", "hippo", "is", "day", "A", "'enjoying' is verb + -ing form."),
        ("The poet is **rhyming** bustle with hippopotomuscle.", "rhyming", "poet", "is", "bustle", "A", "'rhyming' is verb + -ing form."),
        ("The animal is **splashing** water on its back.", "splashing", "animal", "is", "back", "A", "'splashing' is verb + -ing form."),
        ("The hippo is **living** happily in nature.", "living", "hippo", "is", "nature", "A", "'living' is verb + -ing form.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_ing, start=1):
        qid = f"BK02_CH13_CAT08_Q{idx:02d}"
        qtxt = f"Identify the **present continuous (-ing) verb** in this sentence:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the present continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Present Continuous Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("What is the correct -ing spelling rule for **'roll'**? (The hippo is ____ along.)", "rolling (add -ing)", "rollling", "roleing", "rollng", "A", "Regular verb adding -ing (rolling)."),
        ("What is the correct -ing spelling rule for **'swim'**? (The hippo is ____.)", "swimming (double final consonant)", "swiming", "swimmeging", "swimng", "A", "CVC rule: double final consonant before -ing (swimming)."),
        ("What is the correct -ing spelling rule for **'ride'**? (He is not ____ in trams.)", "riding (drop final silent e)", "rideing", "ridding", "ridng", "A", "Drop final silent 'e' before adding -ing (riding)."),
        ("Fill in the blank with present continuous form: 'The hippopotamus (roll) ____ along the river.'", "is rolling", "was roll", "are roll", "is rolled", "A", "Singular subject takes 'is rolling'."),
        ("Choose the sentence in PRESENT CONTINUOUS tense:", "The hippopotamus is rolling along on big limbs right now.", "The hippopotamus rolled along yesterday.", "The hippopotamus will roll along tomorrow.", "The hippopotamus rolled yesterday.", "A", "'is rolling' is present continuous."),
        ("Fill in the blanks: 'The hippo ____ (eat) food and ____ (flavor) it with mustard.' ", "is eating, is flavoring", "are eating, are flavoring", "is eat, is flavor", "was eating, were flavoring", "A", "Singular 'hippo' takes 'is eating' and 'is flavoring'."),
        ("Identify the spelling mistake in: 'The hippo is **swiming** in the river.'", "'swiming' should be 'swimming'", "'swiming' should be 'swimming'", "'is' should be 'are'", "No mistake", "A", "Swim doubles final m before -ing (swimming)."),
        ("Select the correct -ing form for **'taste'**:", "tasting", "tasteing", "tastting", "tastng", "A", "Drop silent 'e': taste -> tasting."),
        ("Which sentence describes an action HAPPENING RIGHT NOW?", "Look! The hippopotamus is rolling into the water.", "The hippopotamus rolled into the water yesterday.", "The hippopotamus rolls into the water every day.", "The hippopotamus will roll tomorrow.", "A", "Present continuous ('is rolling') describes ongoing action right now."),
        ("Fill in the blank: 'I ____ (read) Arthur Guiterman's poem.'", "am reading", "is reading", "are reading", "am readeing", "A", "Subject 'I' takes 'am reading'."),
        ("Choose the correct form: 'The hippo ____ (try) his best to do his duty.'", "is trying", "are trying", "am trying", "is try", "A", "Singular subject 'hippo' takes 'is trying'."),
        ("Identify the verb in: 'Why are you riding in a tram?'", "are riding", "Why", "you", "tram", "A", "Helping verb 'are' + main verb 'riding' form present continuous."),
        ("What is the -ing form of **'try'**?", "trying", "tryying", "trieing", "tryng", "A", "Vowel+y verb adding -ing (trying)."),
        ("What is the -ing form of **'move'**?", "moving", "moveing", "movving", "movng", "A", "Drop silent e: move -> moving."),
        ("Change simple present to continuous: 'The hippo eats mustard.' -> 'The hippo ____ mustard.'", "is eating", "ate", "was eating", "will eat", "A", "is eating."),
        ("Fill in the blank: 'Traffic ____ (jamming) up the city streets.'", "is jamming", "are jamming", "am jamming", "jammed", "A", "Singular subject 'Traffic' takes 'is jamming'."),
        ("Identify the correct present continuous sentence:", "Look! The hippopotamus is avoiding the traffic jam.", "Look! The hippopotamus avoids the traffic jam.", "Look! The hippopotamus avoided the traffic jam.", "Look! The hippopotamus avoiding the traffic jam.", "A", "Exclamation 'Look!' introduces action happening now ('is avoiding')."),
        ("Select the correct -ing form for **'flavor'**:", "flavoring", "flavoreing", "flavorring", "flavorng", "A", "Regular verb adding -ing (flavoring).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH13_CAT08_Q{idx:02d}"
        qtxt = f"Present Continuous Grammar & Spelling Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Present Continuous Formation & Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze spelling rules for adding -ing to verbs: Group them correctly: (swim, ride, roll)", "swim -> swimming (double consonant), ride -> riding (drop e), roll -> rolling (add -ing)", "All just add -ing.", "All double the last letter.", "swim -> swiming, ride -> rideing, roll -> rollling", "A", "3 distinct orthographic rules for -ing derivation."),
        ("Convert past tense narrative to present continuous picture scene: 'The hippo rolled along while traffic jammed.'", "The hippo is rolling along while traffic is jamming.", "The hippo rolling along while traffic jamming.", "The hippo was rolling while traffic jammed.", "The hippo will roll while traffic jams.", "A", "Both verbs transformed to present continuous (is rolling, is jamming)."),
        ("Spot the missing auxiliary verb in: 'The hippo rolling on big limbs and eating mustard.' Correct it:", "'The hippo **is** rolling on big limbs and **is** eating mustard.'", "'The hippo rolling on big limbs and eating mustard.'", "'The hippo **are** rolling and **are** eating.'", "No error.", "A", "Present continuous requires auxiliary (is/am/are) before -ing verb."),
        ("Differentiate state vs action: Why don't we usually say 'The hippo is **caring** for sweets'?", "Because 'care' in the sense of liking/preferring is a stative verb, preferring simple present 'does not care'.", "Because 'caring' is hard to spell.", "Because hippo is big.", "Because mustard is yellow.", "A", "Stative preference verbs prefer simple present."),
        ("Identify the sentence with CORRECT present continuous subject-verb agreement:", "The hippopotamuses in the river are swimming peacefully.", "The hippopotamuses in the river is swimming peacefully.", "The hippopotamuses in the river am swimming peacefully.", "The hippopotamuses in the river swimming peacefully.", "A", "Plural subject ('hippopotamuses') takes plural auxiliary 'are'."),
        ("Form negative present continuous: 'The hippo is riding in a taxicab.' -> Negative:", "The hippo is **not** riding in a taxicab.", "The hippo not riding in a taxicab.", "The hippo are no riding in a taxicab.", "The hippo isn't ride in a taxicab.", "A", "Add 'not' between auxiliary 'is' and main verb 'riding'."),
        ("Spot all THREE spelling errors: 'He is **swiming** fast, **rideing** a bus, and **dieing** of hunger.'", "'swiming' -> 'swimming'; 'rideing' -> 'riding'; 'dieing' -> 'dying'", "'swiming' -> 'swiming'; 'rideing' -> 'riddding'; 'dieing' -> 'dieing'", "No errors.", "Only 'swiming' is wrong.", "A", "swimming (double m), riding (drop e), dying (-ie to -y)."),
        ("Rewrite as interrogative present continuous: 'The hippopotamus is flavoring its meal.'", "**Is** the hippopotamus flavoring its meal?", "Are the hippopotamus flavoring its meal?", "The hippopotamus flavoring its meal?", "Why the hippopotamus is flavoring its meal?", "A", "Move auxiliary 'Is' to beginning of sentence."),
        ("Analyze action timeline: 'The zoo **is welcoming** a new hippopotamus tomorrow.' What does present continuous express here?", "A fixed future arrangement / planned action.", "Past completed action.", "Action that happened long ago.", "Uncertain rumor.", "A", "Present continuous can express planned future actions."),
        ("Choose the sentence showing PARALLEL present continuous actions:", "While the hippo is rolling along, the cars are jamming up.", "While hippo rolled, cars are jamming.", "Hippo is rolling while cars jammed.", "Hippo roll while cars jam.", "A", "Both parallel ongoing actions use present continuous."),
        ("Correct the error: 'The hippo is rollling along.'", "'rollling' should be 'rolling' (double 'l', not triple).", "'is' should be 'are'.", "'along' should be capitalized.", "No error.", "A", "Roll + ing = rolling."),
        ("HOTS Reasoning: Compare 'The hippo rolled along' (Past Simple) vs 'The hippo is rolling along' (Present Continuous). How does the meaning change?", "Past simple states a completed past event; present continuous describes an action currently in progress.", "Both mean the exact same thing.", "Past simple is for future; continuous is for past.", "Continuous means hippo stopped.", "A", "Tense changes temporal aspect (completed vs ongoing)."),
        ("Form question: 'Why ____ the hippopotamus ____ (avoiding) trucks and trams?'", "is, avoiding", "are, avoiding", "am, avoiding", "do, avoiding", "A", "Singular subject hippopotamus takes 'is ... avoiding'."),
        ("Identify the correct present continuous sentence describing humorous animal motion:", "The heavy hippopotamus is rolling along on its muscular limbs.", "The heavy hippopotamus is roll along on its muscular limbs.", "The heavy hippopotamus are rolling along on its muscular limbs.", "The heavy hippopotamus rolling along on its muscular limbs.", "A", "Singular subject + is + rolling.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH13_CAT08_Q{idx:02d}"
        qtxt = f"Higher Order Present Continuous Analysis & Editing:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Continuous Tense Aspect & Error Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 9. Helping Verbs (Is, Am, Are) (50 Qs)
# ---------------------------------------------------------------------------
def build_helping_verbs():
    header = "# Category 9: Helping Verbs (Is, Am, Are) — Chapter 13: Habits of the Hippopotamus\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_hv = [
        ("The hippopotamus ___ strong and huge of head.", "is", "are", "am", "be", "A", "Singular subject 'The hippopotamus' takes 'is'."),
        ("The limbs on which he rolls along ___ big.", "are", "is", "am", "be", "A", "Plural subject 'limbs' takes 'are'."),
        ("I ___ amused by Arthur Guiterman's poem.", "am", "is", "are", "be", "A", "Pronoun 'I' takes 'am'."),
        ("The hippopotamus ___ true to all his principles.", "is", "are", "am", "be", "A", "Singular subject takes 'is'."),
        ("Trucks and trams ___ vehicles the hippo avoids.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("Mustard ___ a savory condiment.", "is", "are", "am", "be", "A", "Uncountable singular 'Mustard' takes 'is'."),
        ("The poem ___ funny and rhythmic.", "is", "are", "am", "be", "A", "Singular subject takes 'is'."),
        ("Sweety treats ___ not preferred by the hippo.", "are", "is", "am", "be", "A", "Plural subject 'Sweety treats' takes 'are'."),
        ("I ___ learning about funny wordplay.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The head of the hippopotamus ___ huge.", "is", "are", "am", "be", "A", "Singular 'head' takes 'is'."),
        ("Traffic jams ___ annoying to commuters.", "are", "is", "am", "be", "A", "Plural 'Traffic jams' takes 'are'."),
        ("Arthur Guiterman ___ a famous poet.", "is", "are", "am", "be", "A", "Singular subject takes 'is'."),
        ("You ___ reading Chapter 13.", "are", "is", "am", "be", "A", "Pronoun 'You' always takes 'are'."),
        ("The hippo ___ rolling along the river.", "is", "are", "am", "be", "A", "Singular 'hippo' takes 'is'."),
        ("Taxicabs and omnibuses ___ avoided by the hippo.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("I ___ enjoying the portmanteau words.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The bustle of the hippo ___ broad.", "is", "are", "am", "be", "A", "Singular 'bustle' takes 'is'."),
        ("The words in the poem ___ creative and fun.", "are", "is", "am", "be", "A", "Plural 'words' takes 'are'.")
    ]
    
    for idx, (sent_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_hv, start=1):
        qid = f"BK02_CH13_CAT09_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct helping verb (is / am / are):\n\n\"{sent_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Helping Verb Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Choose the correct helping verb: 'The hippo's head and bustle ____ both very large.'", "are", "is", "am", "be", "A", "Compound subject ('head and bustle') is plural, taking 'are'."),
        ("Select the sentence with CORRECT helping verb agreement:", "The hippopotamus is strong and broad of bustle.", "The hippopotamus are strong and broad of bustle.", "The hippopotamus am strong and broad of bustle.", "The hippopotamus be strong and broad of bustle.", "A", "Singular noun 'The hippopotamus' requires 'is'."),
        ("Fill in the blanks: 'I ____ reading the poem, and my friends ____ laughing.'", "am, are", "is, are", "are, is", "am, is", "A", "'I am', 'friends are'."),
        ("Identify the mistake in: 'The limbs of the hippopotamus **is** big with muscle.'", "'is' should be 'are' because 'limbs' is a plural noun.", "'is' should be 'am'", "'is' should be 'was'", "No mistake", "A", "'limbs' is plural, requiring 'are'."),
        ("Which helping verb completes the question? '____ you familiar with the word hippopotomustard?'", "Are", "Is", "Am", "Be", "A", "Subject 'you' takes 'Are'."),
        ("Fill in the blank: 'Neither ice cream nor custard ____ preferred by the hippo.'", "is", "are", "am", "be", "A", "'Neither...nor' with singular second subject 'custard' takes 'is'."),
        ("Select the correct sentence for story moral:", "Principles and duty are important to live by.", "Principles and duty is important to live by.", "Principles and duty am important to live by.", "Principles and duty be important to live by.", "A", "Compound subject 'Principles and duty' takes 'are'."),
        ("Complete the conversation: Student: 'Where ____ the hippo?' Teacher: 'He ____ in the river!'", "is, is", "are, are", "is, are", "are, is", "A", "Singular 'the hippo' -> is; singular 'He' -> is."),
        ("Identify where 'is' is used incorrectly:", "The limbs **is** big.", "The hippo is strong.", "The poem is funny.", "The mustard is yellow.", "A", "'The limbs is' should be 'The limbs are'."),
        ("Choose the correct helping verb for collective noun used as a single unit: 'The group of hippos ____ swimming together.'", "is", "are", "am", "be", "A", "Collective noun 'group' treated as singular unit takes 'is'."),
        ("Fill in the blank: 'The mustard on his food ____ adding flavor.'", "is", "are", "am", "be", "A", "Uncountable singular 'mustard' takes 'is'."),
        ("Select the sentence with correct helping verb for 'I':", "I am reading Arthur Guiterman's poem.", "I is reading Arthur Guiterman's poem.", "I are reading Arthur Guiterman's poem.", "I be reading Arthur Guiterman's poem.", "A", "Subject 'I' takes 'am'."),
        ("Fill in the blank: 'There ____ many created words in this poem.'", "are", "is", "am", "be", "A", "'There are' before plural noun 'many created words'."),
        ("Fill in the blank: 'There ____ a funny line in stanza 2.'", "is", "are", "am", "be", "A", "'There is' before singular noun 'a funny line'."),
        ("Choose the correct sentence:", "What are the hippopotamuses doing near the river?", "What is the hippopotamuses doing near the river?", "What am the hippopotamuses doing near the river?", "What be the hippopotamuses doing near the river?", "A", "Plural subject 'the hippopotamuses' takes 'are'."),
        ("Identify the correct form: 'The hippo, as well as its limbs, ____ impressive.'", "is", "are", "am", "be", "A", "Subject is singular 'The hippo' ('as well as...' does not change subject number), taking 'is'."),
        ("Fill in the blank: 'Both trucks and trams ____ avoided by the hippo.'", "are", "is", "am", "be", "A", "'Both ... and ...' takes plural verb 'are'."),
        ("Select the option with correct helping verbs: 'The head ____ huge, but the limbs ____ strong.'", "is, are", "are, is", "am, are", "is, is", "A", "'head is', 'limbs are'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH13_CAT09_Q{idx:02d}"
        qtxt = f"Helping Verb Subject-Verb Agreement Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Subject-Verb Agreement Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze subject-verb agreement: 'Each of the hippo's limbs **____** big with muscle.' Choose the correct verb and reason:", "is — because 'Each' is a singular indefinite pronoun requiring singular verb 'is'.", "are — because 'limbs' is plural.", "am — because it refers to speaker.", "be — because limbs are big.", "A", "'Each' is singular indefinite pronoun taking singular verb 'is'."),
        ("Spot the subtle agreement error in: 'A herd of hippopotamuses **are** resting near the river.'", "'are' should be 'is' because the subject is singular noun 'herd'.", "'are' should be 'am'.", "'hippopotamuses' should be 'hippopotamus'.", "No error.", "A", "'A herd' is singular, so it requires 'is resting'."),
        ("Compare: (1) 'The head and bustle **are** large.' vs (2) 'The head, along with the bustle, **is** large.' Why are the verbs different?", "In (1), 'and' creates a plural subject (are); in (2), 'along with' is a prepositional phrase, leaving 'The head' as sole singular subject (is).", "They mean different things.", "Sentence (2) is grammatically wrong.", "Both should use 'are'.", "A", "Prepositional phrases like 'along with' do not change subject number."),
        ("Identify the correct agreement for indefinite pronouns: 'Everyone who reads the poem **____** amused by the wordplay.'", "is", "are", "am", "be", "A", "'Everyone' is a singular indefinite pronoun requiring 'is'."),
        ("Spot all THREE subject-verb errors in: 'The limbs **is** big, I **is** reading, and the trams **is** noisy.'", "'limbs is' -> 'limbs are'; 'I is' -> 'I am'; 'trams is' -> 'trams are'", "'limbs is' -> 'limbs am'; 'I is' -> 'I are'; 'trams is' -> 'trams am'", "Only 'I is' is wrong.", "No errors present.", "A", "limbs are (plural), I am (1st person), trams are (plural)."),
        ("Fill in the blanks in this complex sentence: 'Not only the head but also the limbs **____** large, while the hippo **____** rolling.'", "are, is", "is, are", "is, is", "are, are", "A", "'Not only...but also' agrees with closer plural subject ('limbs' -> are); 'hippo' -> is."),
        ("Transform to negative: 'The hippopotamus is riding in a tram.'", "The hippopotamus **is not** riding in a tram.", "The hippopotamus are not riding in a tram.", "The hippopotamus am not riding in a tram.", "The hippopotamus no riding in a tram.", "A", "Add 'not' after singular helping verb 'is'."),
        ("Analyze inverted subject position: 'Along the river bank **____** rolling a huge hippopotamus.'", "is", "are", "am", "be", "A", "Subject is singular 'a huge hippopotamus', appearing after verb, requiring 'is'."),
        ("Determine agreement with uncountable nouns: 'The mustard on his food **____** spicy.'", "is", "are", "am", "be", "A", "Uncountable noun 'mustard' is treated as singular, taking 'is'."),
        ("Correct the sentence: 'Here **is** the rhyming lines of the poem.'", "Here **are** the rhyming lines of the poem.", "Here am the rhyming lines of the poem.", "Here be the rhyming lines of the poem.", "No error.", "A", "Plural subject 'rhyming lines' requires 'Here are...''"),
        ("Identify the sentence where 'is' acts as a MAIN linking verb rather than a helping verb:", "The hippopotamus **is** strong and broad of bustle.", "The hippo **is** rolling along the bank.", "Arthur Guiterman **is** writing a funny poem.", "The hippo **is** avoiding traffic jams.", "A", "In 'The hippopotamus is strong and broad of bustle', 'is' is the main linking verb connecting subject to predicate adjectives."),
        ("HOTS Reasoning: Why does English use 'am' ONLY with the subject pronoun 'I'?", "Because 'am' is the unique 1st person singular present indicative form of the verb 'to be'.", "Because 'I' is capitalized.", "Because hippo is big.", "There is no reason.", "A", "'am' is exclusively reserved for 1st person singular 'I'."),
        ("Fill in the blanks: 'Neither trucks nor trams **____** used, because walking **____** better.'", "are, is", "is, are", "is, is", "are, are", "A", "'trams' is closer plural subject -> are; 'walking' -> is."),
        ("Select the option with PERFECT helping verb agreement throughout:", "The hippopotamus is strong, I am reading, and the limbs are big.", "The hippopotamus are strong, I is reading, and the limbs is big.", "The hippopotamus am strong, I are reading, and the limbs am big.", "The hippopotamus is strong, I is reading, and the limbs is big.", "A", "hippopotamus is (singular), I am (1st person), limbs are (plural).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH13_CAT09_Q{idx:02d}"
        qtxt = f"Higher Order Helping Verb Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Subject-Verb Agreement & Syntax", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# MAIN EXECUTION FOR REBUILDING CHAPTER 13
# ---------------------------------------------------------------------------
def rebuild_chapter_13():
    print("Rebuilding Chapter 13 category files with high-quality, multi-tiered (Easy/Medium/Hard) non-duplicate questions...")

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
        filepath = os.path.join(CH13_DIR, fname)
        print(f"  Generating {fname}...")
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {fname} created successfully.")

    print("\n[SUCCESS] Completed rebuilding all 9 category files for Chapter 13 (450 total high-quality questions)!")

if __name__ == "__main__":
    rebuild_chapter_13()
