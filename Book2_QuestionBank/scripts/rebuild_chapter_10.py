r"""
=============================================================================
Script: rebuild_chapter_10.py
Description: Generates 50 rich, non-duplicate, multi-tiered (Easy, Medium, Hard)
             questions for each of the 9 category files in Chapter 10:
             "The Banyan Tree" (450 Qs total).
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH10_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_10")
os.makedirs(CH10_DIR, exist_ok=True)

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
    header = "# Category 1: Plural Nouns & Spelling Rules — Chapter 10: The Banyan Tree\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("tree", "trees", "treeses", "treies", "treez", "A", "Regular noun adding -s."),
        ("root", "roots", "rootes", "rooties", "rootz", "A", "Regular noun adding -s."),
        ("branch", "branches", "branchs", "branchies", "branchz", "A", "Nouns ending in -ch add -es."),
        ("place", "places", "plaies", "placees", "placez", "A", "Regular noun ending in -e adds -s."),
        ("year", "years", "yeares", "yearies", "yearz", "A", "Regular noun adding -s."),
        ("fruit", "fruits", "fruites", "fruities", "fruitz", "A", "Regular noun adding -s."),
        ("religion", "religions", "religiones", "religionies", "religionz", "A", "Regular noun adding -s."),
        ("bird", "birds", "birdes", "birdies", "birdz", "A", "Regular noun adding -s."),
        ("animal", "animals", "animales", "animalies", "animalz", "A", "Regular noun adding -s."),
        ("leaf", "leaves", "leafs", "leafes", "leavies", "A", "Nouns ending in -f change -f to -ves."),
        ("seed", "seeds", "seedes", "seedies", "seedz", "A", "Regular noun adding -s."),
        ("wood", "woods", "woodes", "woodies", "woodz", "A", "Regular noun adding -s."),
        ("century", "centuries", "centurys", "centuryes", "centuriz", "A", "Consonant + y changes to -ies."),
        ("trunk", "trunks", "trunkes", "trunkies", "trunkz", "A", "Regular noun adding -s."),
        ("forest", "forests", "forestes", "foresties", "forestz", "A", "Regular noun adding -s."),
        ("shadow", "shadows", "shadowes", "shadowies", "shadowz", "A", "Regular noun adding -s."),
        ("child", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("person", "people", "persons", "peoples", "persones", "A", "Irregular plural: person becomes people.")
    ]
    
    for idx, (word, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH10_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{word}'** from or related to Chapter 10 (*The Banyan Tree*)?"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Plural Noun Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The Banyan Tree has aerial roots that grow from its (branch / branches).", "branches", "branch", "branchs", "branchies", "A", "Nouns ending in -ch add -es (branches)."),
        ("The tree spreads across many (place / places) in India.", "places", "place", "plaies", "placees", "A", "Regular noun adding -s (places)."),
        ("Banyan trees live for hundreds of (year / years).", "years", "year", "yeares", "yearies", "A", "Regular noun adding -s (years)."),
        ("Identify the INCORRECT plural spelling in this list: trees, roots, branchs, fruits.", "branchs", "trees", "roots", "fruits", "A", "Plural of branch is 'branches', not 'branchs'."),
        ("Choose the sentence with the correct plural noun form:", "Green leaves cover the long branches.", "Green leafs cover the long branchs.", "Green leavies cover the long branchies.", "Green leafes cover the long branchz.", "A", "leaves (-f -> -ves) and branches (-ch -> -es) are correct."),
        ("Which noun forms its plural by changing consonant + y to -ies?", "century -> centuries", "day -> days", "tree -> trees", "root -> roots", "A", "Century ends in consonant + y, so plural is centuries."),
        ("Change the singular noun in brackets to plural: 'The Banyan tree dropped green ____ (leaf) on the ground.'", "leaves", "leafs", "leafes", "leavies", "A", "Nouns ending in -f change to -ves (leaves)."),
        ("Select the sentence where ALL plural nouns are spelt correctly:", "Birds build nests on the branches of banyan trees.", "Birdes build nestes on the branchs of banyan trees.", "Birds build nesties on the branchies of banyan treez.", "Birdz build nests on the branches of banyan trees.", "A", "birds, nests, branches, trees are all correctly spelt plurals."),
        ("What is the correct plural of 'aerial root'?", "aerial roots", "aerial rootes", "aerial rooties", "aerial rootz", "A", "Regular noun adding -s."),
        ("The banyan tree has survived for several (century / centuries).", "centuries", "centurys", "centuryes", "centuriz", "A", "Consonant + y changes to -ies (centuries)."),
        ("Many (bird / birds) rest under the shade of the banyan tree.", "birds", "birdes", "birdies", "birdz", "A", "Plural of bird is birds."),
        ("Many (person / people) worship the banyan tree as sacred.", "people", "persons", "peoples", "persones", "A", "Irregular plural of person is people."),
        ("How many (branch / branches) did the huge banyan tree have?", "branches", "branchs", "branchies", "branchz", "A", "Nouns ending in -ch add -es (branches)."),
        ("The fruits of the banyan tree are eaten by many (animal / animals).", "animals", "animales", "animalies", "animalz", "A", "Plural of animal is animals."),
        ("Which plural noun rule applies to the word **'branches'**?", "Add -es to nouns ending in -ch", "Add -s to vowel + y", "Change -f to -ves", "Change -y to -ies", "A", "Branch ends in -ch, so it adds -es."),
        ("Paper is made from the (wood / woods) of banyan trees.", "wood / woods", "woodes", "woodies", "woodz", "A", "Plural of wood is woods."),
        ("Identify the correct plural form of 'child':", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("Banyan trees provide shelter for small (creature / creatures).", "creatures", "creaturees", "creaturies", "creaturez", "A", "Regular noun adding -s (creatures).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH10_CAT01_Q{idx:02d}"
        qtxt = f"Contextual Plural Rule Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Plural Noun Application", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Rewrite the sentence in PLURAL form: 'The bird sat on a branch and ate a leaf.'", "The birds sat on branches and ate leaves.", "The birdes sat on branchs and ate leafs.", "The birds sat on branchies and ate leafes.", "The birdz sat on branches and ate leavies.", "A", "Plural of bird->birds, branch->branches (-ch+es), leaf->leaves (-f->-ves)."),
        ("Analyze the error: 'The banyan tree has much leaves.' Why is 'much' inappropriate here?", "'leaves' is a plural countable noun, so 'many leaves' should be used.", "'leaves' should be 'leafs'.", "'leaves' should be 'leafes'.", "No error.", "A", "Countable plural nouns take 'many', not 'much'."),
        ("Complete the paragraph with correct plurals: 'The two ____ (banyan tree) grew many ____ (aerial root) and dropped thousands of ____ (leaf).'", "banyan trees, aerial roots, leaves", "banyan treies, aerial rootes, leafs", "banyan treez, aerial rooties, leafes", "banyan treees, aerial roots, leavies", "A", "banyan trees (-s), aerial roots (-s), leaves (-f -> -ves)."),
        ("Identify the sentence where ALL three underlined nouns are correctly pluralized:", "The **children** rested on the **branches** among the **leaves**.", "The **childs** rested on the **branchs** among the **leafs**.", "The **childrens** rested on the **branchies** among the **leafes**.", "The **childes** rested on the **branches** among the **leavies**.", "A", "children (irregular), branches (-ch+es), leaves (-f->-ves)."),
        ("Which group contains ONLY irregular plural nouns?", "children, people, men, teeth", "trees, roots, branches, leaves", "centuries, places, fruits, religions", "leaves, thieves, wolves, knives", "A", "children, people, men, teeth change forms without standard -s/-es."),
        ("Why does 'day' become 'days' but 'century' becomes 'centuries'?", "Because 'day' has a vowel before y (a+y -> -s), while 'century' has a consonant before y (r+y -> -ies).", "Because 'day' is short and 'century' is long.", "Because 'day' is time and 'century' is 100 years.", "Both follow the exact same rule.", "A", "Vowel+y adds -s; Consonant+y changes y to -ies."),
        ("Find the TWO grammatical mistakes in: 'The two familys rested under the banyan tree and saw many mouses.'", "'familys' should be 'families' and 'mouses' should be 'mice'.", "'familys' should be 'family' and 'mouses' should be 'mices'.", "'tree' should be 'trees' only.", "There are no mistakes in the sentence.", "A", "families (consonant + y) and mice (irregular plural)."),
        ("Replace the singular words in brackets: 'The monkeys swung by their ____ (foot) and clapped their ____ (hand).'", "feet, hands", "foots, handes", "feets, hands", "foots, handies", "A", "Plural of foot is feet, plural of hand is hands."),
        ("Analyze this sentence: 'Paper is made from the wood of this tree.' Can 'wood' be pluralized as 'woods' here?", "Yes, 'woods' can refer to forests, but as raw material substance 'wood' is uncountable singular.", "Yes, 'woods' is the only correct form.", "No, it becomes 'woodss'.", "Yes, 'a wood' is correct.", "A", "Wood as substance material is uncountable mass noun."),
        ("Fill in the blanks: 'The two ____ (child) climbed two ____ (branch) of the tree.'", "children, branches", "childs, branchs", "childrens, branchies", "childes, branches", "A", "child -> children; branch -> branches (-ch + es)."),
        ("Select the option that shows correct plural transformation for ALL three words: 'leaf', 'century', 'branch'", "leaves, centuries, branches", "leafs, centurys, branchs", "leaves, centuryes, branchies", "leafes, centuries, foxen", "A", "leaf -> leaves; century -> centuries; branch -> branches."),
        ("HOTS Reasoning: Why do we say 'the banyan tree provides shade' rather than 'shades'?", "Because 'shade' in the sense of cool shelter is an uncountable mass noun.", "Because shade is dark.", "Because trees are tall.", "Because India is warm.", "A", "Uncountable mass noun takes singular verb."),
        ("Transform into singular: 'The children rested under the banyan trees.'", "The child rested under the banyan tree.", "The children rested under the banyan tree.", "The child rest under the banyan tree.", "The child rested under the banyan trees.", "A", "Singular forms: child, banyan tree."),
        ("Identify the correct rule for forming the plural of **'branch'**:", "Add -es because it is a regular noun ending in -ch (branches).", "Add -s (branchs).", "Change -ch to -ves (branves).", "Change vowel sound.", "A", "Nouns ending in -ch add -es.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH10_CAT01_Q{idx:02d}"
        qtxt = f"Higher Order Thinking Skills (HOTS) & Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Plural & Spelling Analysis", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 2. Articles Grammar (50 Qs)
# ---------------------------------------------------------------------------
def build_articles_grammar():
    header = "# Category 2: Articles (A, An, The) — Chapter 10: The Banyan Tree\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("The Banyan Tree is ___ huge tree.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'huge'."),
        ("It has ___ aerial root growing from its branches.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'aerial'."),
        ("The Banyan Tree is ___ national tree of India.", "the", "a", "an", "no article", "A", "Use 'the' for unique national symbol 'the national tree'."),
        ("The tree has ___ long life-span of 200-500 years.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'long'."),
        ("In Ayurveda, its fruit is used as ___ medicine.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'medicine'."),
        ("___ Panchatantra/Nature story describes the banyan tree.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'Panchatantra/Nature'."),
        ("Paper is made from ___ wood of this tree.", "the", "a", "an", "no article", "A", "Use 'the' for specific wood of the banyan tree."),
        ("The banyan tree is ___ sacred tree in Hinduism.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'sacred'."),
        ("___ banyan tree spreads over a vast area.", "The", "A", "An", "No article", "A", "Definite article 'The' specifies the banyan tree species."),
        ("It is ___ important medicinal plant in Ayurveda.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'important'."),
        ("___ roots descend to the ground to support the branches.", "The", "A", "An", "No article", "A", "Use 'The' for specific roots of the banyan tree."),
        ("It is ___ ancient tree with deep cultural roots.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'ancient'."),
        ("___ fruit of the banyan tree is eaten by birds.", "The", "A", "An", "No article", "A", "Use 'The' for specific fruit of banyan tree."),
        ("India chose the Banyan as ___ symbol of longevity.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'symbol'."),
        ("They created ___ peaceful shelter under the tree.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'peaceful'."),
        ("It is ___ unusual feature for roots to grow from branches.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'unusual'."),
        ("The banyan tree provides ___ shade to travelers.", "no article", "a", "an", "the", "A", "Abstract/uncountable mass noun 'shade' takes no indefinite article here."),
        ("___ sun shines through the dense leaves of the banyan tree.", "The", "A", "An", "No article", "A", "Use 'The' for unique celestial object 'sun'.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH10_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article (a / an / the / no article):\n\n\"{q_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Basic Article Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The Banyan Tree is ___ huge tree with ___ long life-span.", "a, a", "an, a", "a, an", "the, a", "A", "'a huge tree' (consonant sound), 'a long life-span' (consonant sound)."),
        ("Why do we say '**a** banyan tree' but '**an** aerial root'?", "Because 'banyan' begins with a consonant sound (b) and 'aerial' with a vowel sound (a).", "Because banyan trees are huge.", "Because aerial roots are high.", "Because India is warm.", "A", "Article selection depends on initial vowel/consonant sound."),
        ("Select the sentence with CORRECT article usage:", "The Banyan Tree is the national tree of India.", "A Banyan Tree is a national tree of the India.", "An Banyan Tree is the national tree of India.", "The Banyan Tree is a national tree of an India.", "A", "'The Banyan Tree' (species/title), 'the national tree' (unique national symbol), 'India' (country name takes no article)."),
        ("Fill in the blanks: 'They rested under ___ tree and saw ___ bird on a branch.'", "a, a", "an, an", "a, an", "an, a", "A", "'a tree' (consonant /t/), 'a bird' (consonant /b/)."),
        ("Identify the INCORRECT article in: 'It has **a** aerial root.'", "'a' should be 'an'", "'a' should be 'the'", "'aerial' should be 'a aerial'", "No mistake", "A", "'aerial' starts with vowel sound /air/, so it takes 'an'."),
        ("Which article completes the sentence? 'The fruit is ___ effective remedy in Ayurveda.'", "an", "a", "the", "no article", "A", "'effective' starts with vowel sound /e/, requiring 'an'."),
        ("Choose the correct pair of articles: '___ root descended to ___ ground.'", "The, the", "A, a", "An, an", "The, a", "A", "'The root' (specific root), 'the ground' (specific ground surface)."),
        ("Why do we use 'an' before 'aerial root' in 'It has **an** aerial root'?", "Because 'aerial' begins with the vowel sound /air/.", "Because root is a noun.", "Because banyan is a tree.", "Because ground is below.", "A", "'aerial' starts with vowel sound /air/."),
        ("Complete the dialogue: Student: 'Is that ___ banyan tree?' Teacher: 'Yes, it is ___ national tree of India!'", "a, the", "a, an", "an, the", "the, the", "A", "'a banyan tree' (consonant sound), 'the national tree' (unique national symbol)."),
        ("Select the correct sentence:", "A banyan tree is a sacred tree.", "An banyan tree is a sacred tree.", "The banyan tree is an sacred tree.", "An banyan tree is an sacred tree.", "A", "'A banyan tree' (consonant sound), 'a sacred tree' (consonant sound)."),
        ("Fill in the blank: 'Banyan trees live for ___ long time.'", "a", "an", "the", "no article", "A", "Idiomatic phrase 'for a long time'."),
        ("Identify where NO article is needed:", "The banyan tree provides **___ medicine** for skin irritation.", "He planted ___ tree.", "She saw ___ root.", "They visited ___ place.", "A", "Uncountable mass noun 'medicine' takes no indefinite article here."),
        ("Choose the correct sentence for story summary:", "Nature gives us shadow and shelter under trees.", "A nature gives us a shadow and a shelter.", "An nature gives us an shadow.", "The nature a gives shadow.", "A", "Abstract concepts take no indefinite articles in general moral sense."),
        ("Fill in the blanks: 'The scientist spent ___ hour studying ___ aerial root.'", "an, an", "a, a", "an, a", "the, a", "A", "'an hour' (silent h), 'an aerial root' (vowel sound /air/)."),
        ("Which sentence uses 'the' correctly for national symbols?", "The banyan tree is the national tree of India.", "A banyan tree is a national tree of India.", "An banyan tree is an national tree of India.", "Banyan tree is national tree of India.", "A", "Unique national symbol takes 'the national tree'."),
        ("Identify the article error: 'The banyan is **a** sacred tree with **an** long life-span.'", "'an long' should be 'a long'", "'a sacred' should be 'an sacred'", "'an long' should be 'the long'", "No error", "A", "'a long life-span' (consonant sound /l/)."),
        ("Complete: 'It was ___ unexpected cure for ___ skin irritation.'", "an, no article", "a, an", "the, the", "an, a", "A", "an unexpected (/u/), skin irritation (uncountable, no article)."),
        ("Choose the correct option: '___ sun shone on the banyan tree.'", "The", "A", "An", "No article", "A", "'The sun' (unique celestial body).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH10_CAT02_Q{idx:02d}"
        qtxt = f"Contextual Article Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Article Usage in Context", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze article usage in: 'The banyan tree is **the** national tree of **the** India.' Correct the error:", "'the India' -> 'India' (proper names of countries do not take 'the' unless compound like the USA/UK).", "'the national tree' -> 'a national tree'.", "'The banyan tree' -> 'An banyan tree'.", "No error.", "A", "Country names like India do not take 'the'."),
        ("Fill in all three blanks: '___ tree has ___ aerial root that touches ___ ground.'", "The, an, the", "A, a, a", "An, a, the", "The, a, a", "A", "'The tree' (specific), 'an aerial root' (vowel sound), 'the ground' (surface)."),
        ("Identify why 'the' is used in: 'The Banyan Tree is **the** national tree of India.'", "Because 'national tree' is a unique, definite national designation for India.", "Because banyan is a proper noun.", "Because roots are long.", "Because India is big.", "A", "'the' specifies the singular national symbol designation."),
        ("Spot the TWO article errors: 'It took **a** hour to inspect **a** aerial root of the tree.'", "'a hour' should be 'an hour' and 'a aerial' should be 'an aerial'.", "'a hour' should be 'the hour' and 'a aerial' should be 'a aerial'.", "No errors.", "Only 'a hour' is wrong.", "A", "Both 'hour' (silent h) and 'aerial' (vowel a) require 'an'."),
        ("Choose the paragraph with PERFECT article usage throughout:", "The Banyan Tree is a huge tree. It has an aerial root. The root grows down to the ground.", "An Banyan Tree is an huge tree. It has a aerial root. A root grows down to a ground.", "The Banyan Tree is an huge tree.", "A Banyan Tree is a huge tree. The aerial root was an honest.", "A", "The Banyan Tree (species), a huge tree (consonant), an aerial root (vowel), The root (second mention), the ground (surface)."),
        ("Why is it correct to write 'a unique tree' but 'an unusual tree'?", "Because 'unique' begins with consonant sound /j/ (yoo), while 'unusual' begins with vowel sound /u/.", "Because unique is longer.", "Because tree is noun.", "Both take 'an'.", "A", "Sound determines article: /yoo/ is a consonant sound."),
        ("Select the option that correctly completes the story moral: '___ ancient tree provides ___ shade to ___ weary traveler.'", "An, no article, a", "A, a, an", "The, the, the", "An, a, a", "A", "An ancient tree, shade (uncountable mass noun, no article), a weary traveler."),
        ("Analyze this sentence: 'Ayurveda uses **the** fruit of the banyan tree.' Why is 'the' appropriate?", "Because it refers to the specific fruit of the banyan tree.", "Because fruit is in Ayurveda.", "Because fruit is plural.", "Because banyan is national tree.", "A", "'the' specifies the definite fruit of the tree."),
        ("Correct the sentence: 'An banyan tree has a aerial root in the forest.'", "A banyan tree has an aerial root in the forest.", "The banyan tree has an aerial root in an forest.", "An banyan tree has the aerial root in a forest.", "A banyan tree has a aerial root in a forest.", "A", "'A banyan' (/b/ sound), 'an aerial' (vowel /air/), 'the forest' (specific area)."),
        ("Fill in the blanks: '___ fruits of ___ banyan tree are useful in ___ Ayurveda.'", "The, the, no article", "A, a, a", "No article, a, an", "An, the, a", "A", "'The fruits' (specific), 'the banyan tree' (specific), Ayurveda (proper name, no article)."),
        ("Spot the missing article: 'Banyan tree is national tree of India.'", "Missing 'The' at start and 'the' before 'national tree' -> 'The Banyan tree is the national tree...'", "Missing 'an' before 'India'", "Missing 'a' before 'of'", "No article is missing", "A", "Both subject and national symbol require articles."),
        ("HOTS Reasoning: Which sentence uses 'a', 'an', and 'the' correctly in a single rule demonstration?", "An aerial root of a banyan tree reached the ground.", "A aerial root of an banyan tree reached a ground.", "The aerial root of an banyan tree reached an ground.", "An aerial root of an banyan tree reached the ground.", "A", "An aerial (vowel), a banyan (consonant), the ground (specific)."),
        ("Rewrite correctly: 'The banyan is a honest symbol of nature with an wide canopy.'", "The banyan is an honest symbol of nature with a wide canopy.", "The banyan is a honest symbol of nature with a wide canopy.", "The banyan is an honest symbol of nature with an wide canopy.", "The banyan is the honest symbol of nature with an wide canopy.", "A", "'an honest' (silent h), 'a wide canopy' (consonant /w/)."),
        ("Identify the correct rule for using 'the' with unique national symbols (the national tree, the national flower, the national anthem):", "Official unique national symbols take the definite article 'the'.", "National symbols take 'an'.", "National symbols never take articles.", "National symbols take 'a' only.", "A", "National symbols take 'the'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH10_CAT02_Q{idx:02d}"
        qtxt = f"Higher Order Article Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Article Analysis & Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 3. Calendar & Days Vocabulary (50 Qs)
# ---------------------------------------------------------------------------
def build_calendar_days():
    header = "# Category 3: Calendar, Days & Abbreviations — Chapter 10: The Banyan Tree\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    days_easy = [
        ("The average life-span of a banyan tree is **200-500 years**. How many years make up **1 century**?", "100 years", "10 years", "50 years", "1000 years", "A", "1 century = 100 years."),
        ("How many centuries are in **500 years**?", "5 centuries", "50 centuries", "2 centuries", "10 centuries", "A", "500 / 100 = 5 centuries."),
        ("What is the standard abbreviation for **Wednesday**?", "Wed.", "Weds.", "We.", "W.", "A", "Wed. is standard abbreviation."),
        ("Which day comes right after Tuesday?", "Wednesday", "Thursday", "Monday", "Friday", "A", "Wednesday follows Tuesday."),
        ("What is the abbreviation for **Tuesday**?", "Tue.", "Tues.", "Tu.", "Ts.", "A", "Tue. is standard abbreviation."),
        ("How many years make up **1 decade**?", "10 years", "100 years", "5 years", "50 years", "A", "1 decade = 10 years."),
        ("How many decades are in **200 years**?", "20 decades", "2 decades", "200 decades", "50 decades", "A", "200 / 10 = 20 decades."),
        ("If a tree planting event occurs on **Sunday morning**, what time of day comes right after morning?", "Afternoon", "Night", "Evening", "Midnight", "A", "Afternoon follows morning."),
        ("What is the abbreviation for **Sunday**?", "Sun.", "Snd.", "Su.", "Sn.", "A", "Sun. is standard abbreviation."),
        ("Which month comes right before July?", "June", "May", "August", "September", "A", "June comes before July."),
        ("What is the short abbreviation for **July**?", "Jul.", "Jly.", "Ju.", "Jl.", "A", "Jul. is standard abbreviation."),
        ("Which month comes right after July?", "August", "September", "June", "May", "A", "August comes after July."),
        ("What is the short abbreviation for **August**?", "Aug.", "Augu.", "Au.", "Ag.", "A", "Aug. is standard abbreviation."),
        ("If today is Wednesday, what day was yesterday?", "Tuesday", "Thursday", "Monday", "Sunday", "A", "Yesterday was Tuesday."),
        ("If today is Wednesday, what day will tomorrow be?", "Thursday", "Tuesday", "Friday", "Saturday", "A", "Tomorrow will be Thursday."),
        ("What is the abbreviation for **Thursday**?", "Thu.", "Thur.", "Th.", "Ts.", "A", "Thu. is standard abbreviation."),
        ("Which day comes between Friday and Sunday?", "Saturday", "Thursday", "Monday", "Tuesday", "A", "Saturday is between Friday and Sunday."),
        ("Which month comes right before August?", "July", "June", "September", "October", "A", "July comes before August.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(days_easy, start=1):
        qid = f"BK02_CH10_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Vocabulary & Time Concepts:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Days & Calendar Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("A banyan tree planting drive started on **Monday** and lasted for 4 days. On which day did it end?", "Thursday", "Wednesday", "Friday", "Saturday", "A", "Monday + 4 days = Tuesday(1), Wednesday(2), Thursday(3), Friday(end day 4 inclusive / Thursday 4th day)."),
        ("Students observed the banyan tree roots from **10:00 AM to 1:00 PM**. How many hours did they observe?", "3 hours", "2 hours", "4 hours", "5 hours", "A", "1:00 PM - 10:00 AM = 3 hours."),
        ("Match the day with its abbreviation: **Thursday**", "Thu.", "Thur.", "Th.", "Ts.", "A", "Thu. is standard."),
        ("The banyan tree has lived for **3 centuries**. How many years is that?", "300 years", "30 years", "3,000 years", "150 years", "A", "3 x 100 = 300 years."),
        ("Identify the correctly spelt month name:", "August", "Agust", "Auguste", "Augustt", "A", "August is the correct spelling."),
        ("Identify the INCORRECT pair of day and abbreviation:", "Monday - Mon.", "Tuesday - Tue.", "Wednesday - Wed.", "Thursday - Thr.", "D", "Thursday abbreviation is Thu., not Thr."),
        ("Calculate: How many days are in **July**?", "31 days", "30 days", "28 days", "29 days", "A", "July has 31 days."),
        ("Which month has 31 days and comes right after June?", "July", "August", "May", "September", "A", "July has 31 days and follows June."),
        ("Rearrange in correct chronological order: Wed, Mon, Tue, Thu", "Mon, Tue, Wed, Thu", "Tue, Mon, Wed, Thu", "Mon, Wed, Tue, Thu", "Thu, Wed, Tue, Mon", "A", "Monday -> Tuesday -> Wednesday -> Thursday."),
        ("What day is 3 days before Saturday?", "Wednesday", "Thursday", "Tuesday", "Friday", "A", "Saturday - 3 days = Friday(1), Thursday(2), Wednesday(3)."),
        ("If a banyan tree study project lasts for 4 weeks, how many days is that?", "28 days (4 x 7)", "20 days", "30 days", "14 days", "A", "4 weeks x 7 days = 28 days."),
        ("Select the month that has 31 days:", "August", "June", "April", "September", "A", "August has 31 days."),
        ("Which abbreviation stands for **September**?", "Sept. or Sep.", "Spt.", "Septe.", "St.", "A", "Sept. or Sep. is standard abbreviation."),
        ("If today is **Wed.**, what day will it be after 7 days?", "Wednesday", "Thursday", "Tuesday", "Friday", "A", "7 days is a full week cycle, landing on Wednesday again."),
        ("The nature walk under banyan trees lasted from **8:30 AM to 10:30 AM**. How many hours did it last?", "2 hours", "1 hour", "3 hours", "1.5 hours", "A", "10:30 AM - 8:30 AM = 2 hours."),
        ("Identify the word that means 'living for more than two years' or 'continuing for a long time':", "Perennial / Long-lived", "Daily", "Weekly", "Monthly", "A", "Perennial means lasting a very long time."),
        ("Which of the following is a weekend day?", "Sunday", "Monday", "Tuesday", "Wednesday", "A", "Sunday is a weekend day."),
        ("Choose the correct abbreviation for **July**:", "Jul.", "Jly.", "Ju.", "Jl.", "A", "Jul. is standard.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH10_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Application & Story Timeline:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Calendar & Time Reasoning", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("A famous banyan tree in Howrah, India has been growing since **1787**. How many years old was it in **1987**?", "200 years (2 centuries)", "100 years", "300 years", "50 years", "A", "1987 - 1787 = 200 years."),
        ("If a banyan tree's average life span is **200 to 500 years**, what is the difference between maximum and minimum average life span?", "300 years (3 centuries)", "200 years", "500 years", "100 years", "A", "500 - 200 = 300 years."),
        ("Solve the calendar puzzle: If 15th August (India's Independence Day) was a Friday, what day of the week was 22nd August?", "Friday", "Saturday", "Thursday", "Monday", "A", "15 + 7 = 22nd August, landing on Friday."),
        ("Analyze this schedule: Tree watering on Mon, Wed, Fri; Pruning on Tue, Thu, Sat. On which day do BOTH rest?", "Sunday", "Monday", "Saturday", "Wednesday", "A", "Sunday is not listed in schedule."),
        ("Complete the full series of day abbreviations: Mon., Tue., Wed., Thu., Fri., Sat., ____.", "Sun.", "Sund.", "Su.", "Sn.", "A", "Sun. completes the 7 days of the week."),
        ("If a nature camp under banyan trees lasted a fortnight, how many days did it cover?", "14 days (2 weeks)", "7 days", "30 days", "3 days", "A", "A fortnight is 14 days."),
        ("Spot the error in the calendar sequence: 'May, Jun, Aug, Jul, Sep'", "August and July are in wrong order.", "June is in wrong position.", "September should be first.", "No error.", "A", "July comes before August (May, Jun, Jul, Aug, Sep)."),
        ("July has **31 days**. What date was the day right after 31st July?", "1st August", "32nd July", "30th July", "1st September", "A", "July has 31 days, so next day is 1st August."),
        ("If yesterday was two days before Friday, what day is tomorrow?", "Friday", "Thursday", "Saturday", "Wednesday", "A", "Two days before Friday = Wednesday (yesterday). Today = Thursday. Tomorrow = Friday."),
        ("Calculate: How many days are there in total during **July** and **August** combined?", "62 days (31 + 31)", "60 days", "61 days", "59 days", "A", "July (31) + August (31) = 62 days."),
        ("HOTS Reasoning: Why is the Banyan Tree called a living witness of centuries of history?", "Because its average life span of 200-500 years allows a single tree to survive across multiple human generations and historical eras.", "Because its leaves are green.", "Because paper is made from it.", "Because birds nest in it.", "A", "Extremely long lifespan spanning 2-5 centuries."),
        ("Identify the correct statement about a leap year:", "A leap year has 366 days and February has 29 days.", "A leap year has 365 days.", "February has 28 days in leap year.", "A leap year occurs every 10 years.", "A", "Leap year has 366 days (Feb = 29 days)."),
        ("An aerial root grows 10 centimeters per month. How many centimeters does it grow in 1 year (12 months)?", "120 centimeters (1.2 meters)", "100 centimeters", "60 centimeters", "200 centimeters", "A", "10 x 12 = 120 centimeters."),
        ("Which month pair both have 31 days and come right after each other in late summer?", "July and August", "June and July", "August and September", "May and June", "A", "July (31) and August (31) are consecutive 31-day months.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH10_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Logic & Mathematical Time Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Calendar & Time Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 4. Action Verbs Identification (50 Qs)
# ---------------------------------------------------------------------------
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification — Chapter 10: The Banyan Tree\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_verbs = [
        ("The Banyan Tree **grows** in many places in India.", "grows", "Banyan Tree", "many", "places", "A", "'grows' is the action verb."),
        ("Aerial roots **descend** to the ground.", "descend", "aerial", "roots", "ground", "A", "'descend' is the physical action verb."),
        ("The tree **spreads** further across the land.", "spreads", "tree", "further", "land", "A", "'spreads' is the action verb."),
        ("Ayurveda **uses** the fruit to treat inflammation.", "uses", "Ayurveda", "fruit", "inflammation", "A", "'uses' is the action verb."),
        ("Paper is **made** from the wood of this tree.", "made", "paper", "wood", "tree", "A", "'made' is the action verb."),
        ("People **consider** the Banyan Tree sacred.", "consider", "people", "Banyan Tree", "sacred", "A", "'consider' is the mental action verb."),
        ("Birds **build** nests in the branches.", "build", "birds", "nests", "branches", "A", "'build' is the physical action verb."),
        ("The banyan tree **provides** shade for travelers.", "provides", "banyan tree", "shade", "travelers", "A", "'provides' is the action verb."),
        ("Roots **anchor** the massive tree in the soil.", "anchor", "roots", "massive", "soil", "A", "'anchor' is the physical action verb."),
        ("Animals **eat** the fruits of the banyan tree.", "eat", "animals", "fruits", "tree", "A", "'eat' is the physical action verb."),
        ("Children **play** under the huge canopy.", "play", "children", "huge", "canopy", "A", "'play' is the physical action verb."),
        ("The banyan tree **stands** tall for centuries.", "stands", "banyan tree", "tall", "centuries", "A", "'stands' is the action verb."),
        ("Leaves **absorb** sunlight for energy.", "absorb", "leaves", "sunlight", "energy", "A", "'absorb' is the action verb."),
        ("The roots **reach** deep into the earth.", "reach", "roots", "deep", "earth", "A", "'reach' is the physical action verb."),
        ("People **worship** under the sacred tree.", "worship", "people", "sacred", "tree", "A", "'worship' is the action verb."),
        ("The tree **protects** soil from erosion.", "protects", "tree", "soil", "erosion", "A", "'protects' is the action verb."),
        ("Branches **extend** wide in all directions.", "extend", "branches", "wide", "directions", "A", "'extend' is the action verb."),
        ("Travelers **rest** beneath its cool shade.", "rest", "travelers", "beneath", "shade", "A", "'rest' is the action verb.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_verbs, start=1):
        qid = f"BK02_CH10_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in this sentence from or related to Chapter 10:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Action Verb Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Which word from the sentence is an **action verb**? 'The aerial roots **gradually** **descend** to the **hard** **ground**.'", "descend", "gradually", "hard", "ground", "A", "'descend' shows physical action; 'gradually' is adverb, 'hard' is adjective, 'ground' is noun."),
        ("Identify BOTH action verbs in: 'The roots **grow** from branches and **descend** to the earth.'", "grow, descend", "roots, branches", "earth, grow", "descend, branches", "A", "'grow' and 'descend' are both action verbs."),
        ("What is the past tense action verb of 'grow' as used in sentence ('the roots grew long')?", "grew", "growed", "growing", "grows", "A", "Past tense of grow is grew."),
        ("Choose the sentence where the underlined word is used as an ACTION VERB:", "Aerial roots **descend** from high branches.", "The slope had a steep **descend**.", "We watched the plane's **descend**.", "I noticed their **descend**.", "A", "In (A), 'descend' acts as the main action verb."),
        ("Find the action verb in: 'The banyan tree treats skin irritation in Ayurveda.'", "treats", "banyan tree", "skin", "Ayurveda", "A", "'treats' is the action verb."),
        ("Which sentence contains NO physical action verb?", "The Banyan Tree is the national tree of India.", "Roots grow from branches.", "Animals eat the fruits.", "The tree spreads across the ground.", "A", "'The Banyan Tree is the national tree of India' contains linking verb 'is', but no physical action verb."),
        ("Change the action verb 'spread' to past tense: 'The tree (spread) over a wide area last century.'", "spread", "spreaded", "spreading", "spreads", "A", "Past tense of spread remains spread."),
        ("Identify the action verb: 'The banyan tree provides shade and shelters birds.'", "provides, shelters", "banyan tree, shade", "birds, shade", "shelters, shade", "A", "'provides' and 'shelters' are action verbs."),
        ("Select the action verb that completes the sentence: 'The aerial roots ____ the heavy branches of the banyan tree.'", "support / hold", "strong", "long", "tree", "A", "'support' / 'hold' is an action verb."),
        ("Which word is an action verb? (aerial, descend, sacred, inflammation)", "descend", "aerial", "sacred", "inflammation", "A", "'descend' is an action verb; others are adjectives/nouns."),
        ("What action do aerial roots perform to help the tree expand?", "descend / grow", "sacred", "abode", "inflammation", "A", "Roots descend and grow to the ground (action verb)."),
        ("Identify the action verb in: 'Hindus consider the banyan tree sacred.'", "consider", "Hindus", "banyan tree", "sacred", "A", "'consider' is a mental action verb."),
        ("Choose the correct action verb: 'Workers ____ paper from banyan tree wood.'", "make / manufacture", "strong", "huge", "paper", "A", "'make' / 'manufacture' is the action verb."),
        ("Identify the action verb in: 'The fruit treats inflammation effectively.'", "treats", "fruit", "inflammation", "effectively", "A", "'treats' is the action verb."),
        ("Which of these words is NOT an action verb? (descend, spread, sacred, treat)", "sacred", "descend", "spread", "treat", "A", "'sacred' is an adjective; others are action verbs."),
        ("Identify the action verb in: 'Monkeys swing from the aerial roots.'", "swing", "monkeys", "from", "roots", "A", "'swing' is the action verb."),
        ("Fill in the blank with an appropriate action verb: 'The banyan tree ____ for over 300 years.'", "survives / lives", "huge", "green", "wood", "A", "'survives' / 'lives' is an action verb."),
        ("What action verb completes the sentence? 'The dense canopy ____ sunlight from reaching the ground.'", "blocks / prevents", "dark", "shade", "tree", "A", "'blocks' / 'prevents' is an action verb.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH10_CAT04_Q{idx:02d}"
        qtxt = f"Action Verb Grammar Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Action Verb Context & Tense", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence: 'The aerial roots gracefully grow down from branches and anchor the banyan tree.' How many total ACTION VERBS are present?", "2 action verbs ('grow', 'anchor')", "1 action verb", "3 action verbs", "0 action verbs", "A", "'grow' and 'anchor' are action verbs; 'gracefully', 'aerial' are adverbs/adjectives."),
        ("Categorize the verbs: In 'The banyan tree **is** sacred, so people **worship** beneath it', classify 'is' and 'worship'.", "'is' is a linking verb; 'worship' is an action verb.", "Both are action verbs.", "Both are linking verbs.", "'is' is action; 'worship' is linking.", "A", "'is' links state of being; 'worship' shows action."),
        ("Replace the weak verb with a strong action verb: 'The aerial roots **go** down to the soil.'", "The aerial roots **descend** to the soil.", "The aerial roots **were near** the soil.", "The aerial roots **saw** the soil.", "The aerial roots **looked at** the ground.", "A", "'descend' is a much stronger, precise action verb."),
        ("Identify the sentence with THREE distinct action verbs:", "The aerial roots **grow** from branches, **descend** to the ground, and **support** the tree.", "The banyan tree is huge, old, and sacred.", "The banyan tree is the national tree of India.", "It is found in many places.", "A", "grow, descend, support are 3 distinct action verbs."),
        ("Differentiate verb types: Which underlined word is an ACTION verb?", "Ayurveda **uses** banyan fruit as medicine.", "The banyan tree was **huge**.", "The wood was **strong**.", "The fruit was **red**.", "A", "'uses' is an action verb."),
        ("Spot the incorrect verb tense: 'The aerial roots **descends** to the ground yesterday.' Correct it for past simple:", "'descended' is the past action verb form.", "'descends' should be 'descending'.", "'descends' should be 'descend'.", "'descends' should be 'will descend'.", "A", "Past simple of descend is descended."),
        ("Form an action chain: Rearrange the story action verbs in correct order of occurrence: (roots sprout from branch, descend to ground, take root in soil, form new trunks)", "roots sprout from branch -> descend to ground -> take root in soil -> form new trunks", "form new trunks -> take root in soil -> descend to ground -> roots sprout", "descend to ground -> roots sprout -> form new trunks -> take root in soil", "take root -> form trunks -> descend -> sprout", "A", "Chrono order: sprout, descend, take root, form new trunks."),
        ("Identify the verb error in dialogue: Student said, 'We have **observe** the banyan tree's roots!'", "'observe' is incorrect; the past participle form is 'observed' ('have observed').", "'observe' should be 'observing'.", "'observe' should be 'observes'.", "No error.", "A", "Perfect tense requires past participle 'observed'."),
        ("Analyze this sentence: 'The banyan tree **symbolizes** eternal life.' What type of action verb is 'symbolizes'?", "Representational/symbolic action verb", "Physical movement verb", "Linking verb", "State of being verb", "A", "'symbolizes' is an action verb describing symbolic representation."),
        ("Which sentence uses action verbs to show cause and effect?", "Roots **descend** into the soil, so the tree **expands** into a massive grove.", "The banyan tree is huge and paper is made from wood.", "The tree is sacred in Hinduism and Buddhism.", "Average life span is 200-500 years.", "A", "'descend' (cause action) -> 'expands' (effect action)."),
        ("Spot the missing action verb: 'The aerial roots ____ down and ____ additional support to the heavy branches.'", "grow, provide", "huge, green", "was, was", "quick, slow", "A", "'grow' and 'provide' complete sentence with vivid actions."),
        ("HOTS Reasoning: Why is 'sustains' in 'The banyan tree sustains a rich ecosystem' considered an ESSENTIAL action verb?", "Because it describes actively supporting, feeding, and sheltering numerous living organisms.", "Because sustaining requires climbing.", "Because banyan is a tree.", "Because it is a noun.", "A", "Descriptive action verb conveying ecological support."),
        ("Transform the action verb to future tense: 'The banyan tree **spreads** further next year.'", "The banyan tree **will spread** further next year.", "The banyan tree **spreaded** further next year.", "The banyan tree **is spreading** further next year.", "The banyan tree **spreads** further next year.", "A", "'will spread' expresses future action."),
        ("Identify the sentence where the action verb matches the plural subject:", "The aerial roots **descend** to the ground.", "The aerial roots **descends** to the ground.", "An aerial root **descend** to the ground.", "The aerial roots **is descending** to the ground.", "A", "Plural subject 'aerial roots' takes base verb 'descend' in simple present.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH10_CAT04_Q{idx:02d}"
        qtxt = f"Higher Order Action Verb Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Action Verb Classification & Tense Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 5. Punctuation Marks (50 Qs)
# ---------------------------------------------------------------------------
def build_punctuation_marks():
    header = "# Category 5: Punctuation Marks & Capitalization — Chapter 10: The Banyan Tree\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_punct = [
        ("What punctuation mark should be placed at the end of: 'The Banyan Tree is the national tree of India__'", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "Comma (,)", "A", "A statement ends with a full stop."),
        ("Which mark is used at the end of an asking sentence: 'What is special about the roots of the Banyan Tree__'", "Question mark (?)", "Full stop (.)", "Comma (,)", "Exclamation mark (!)", "A", "A question ends with a question mark."),
        ("Which letter should ALWAYS be capitalized in a country name like 'India'?", "First letter (India)", "The last letter", "All letters", "No letters", "A", "Country names require capitalized initial letters."),
        ("Identify the punctuation mark used to separate items in a list: 'The banyan tree provides shade__ wood__ and fruit.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Hyphen (-)", "A", "Commas separate items in a list."),
        ("Which punctuation mark shows sudden wonder: 'What an enormous banyan tree this is__'", "Exclamation mark (!)", "Full stop (.)", "Comma (,)", "Question mark (?)", "A", "Exclamation marks express intense wonder."),
        ("Select the proper noun that MUST start with a capital letter:", "Hinduism", "tree", "branch", "root", "A", "'Hinduism' as a religion name starts with capital 'H'."),
        ("Which of the following is the symbol for a **full stop**?", ".", "?", "!", ",", "A", "Period/full stop is '.'"),
        ("Which of the following is the symbol for a **question mark**?", "?", ".", "!", ",", "A", "Question mark is '?'"),
        ("Which of the following is the symbol for an **exclamation mark**?", "!", "?", ".", ",", "A", "Exclamation mark is '!'"),
        ("Which word in this sentence should start with a CAPITAL letter? 'buddhism considers the banyan tree sacred.'", "buddhism -> Buddhism", "considers -> Considers", "sacred -> Sacred", "the -> The", "A", "Religion name 'Buddhism' must start with a capital letter."),
        ("What punctuation mark goes in the box? 'The average life span of a banyan tree is 200-500 years [ ]'", "Full stop (.)", "Question mark (?)", "Comma (,)", "Exclamation mark (!)", "A", "Full stop ends the statement."),
        ("Which title is capitalized correctly?", "Ayurveda", "ayurveda", "AyurVeda", "AYURVEDA", "A", "Capital letter for proper traditional medicine system name."),
        ("What mark goes after a speaker tag: 'Teacher said__ \"The banyan tree is sacred in India.\"'", "Comma (,)", "Question mark (?)", "Full stop (.)", "Exclamation mark (!)", "A", "Comma follows dialogue speaker tags."),
        ("Identify the correct capital letter for the pronoun 'I': 'he said, \"i love sitting under the banyan tree.\"'", "I", "i", "i'm", "I'm", "A", "Standalone pronoun 'I' is always capitalized."),
        ("Which option shows a sentence ending correctly?", "Paper is made from the wood of this tree.", "Paper is made from the wood of this tree?", "Paper is made from the wood of this tree,", "Paper is made from the wood of this tree;", "A", "Full stop at end of simple statement."),
        ("What mark is used in compound words like '**life-span**'?", "Hyphen (-)", "Comma (,)", "Full stop (.)", "Apostrophe (')", "A", "Hyphen joins compound words like life-span."),
        ("Which tree name title is capitalized correctly?", "The Banyan Tree", "the banyan tree", "The banyan Tree", "THE BANYAN TREE", "A", "Title capitalization."),
        ("What punctuation mark is used around exact dictionary definitions: 'Aerial means ___from or in the air___.'", "Double or single quotation marks ( \" \" or ' ' )", "Parentheses ( )", "Full stops ( . . )", "Commas ( , , )", "A", "Quotation marks enclose exact defined meanings.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_punct, start=1):
        qid = f"BK02_CH10_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Punctuation & Capitalization Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Identify the sentence with CORRECT capitalization and punctuation:", "The Banyan Tree is sacred in Hinduism and Buddhism in India.", "the banyan tree is sacred in hinduism and buddhism in india.", "The Banyan Tree is sacred in hinduism and Buddhism in india?", "the Banyan Tree Is Sacred In Hinduism And Buddhism In India.", "A", "Banyan Tree, Hinduism, Buddhism, India (proper names) capitalized; period at end."),
        ("Which sentence is punctuated as a CORRECT question?", "Where can the Banyan Tree be commonly found?", "Where can the Banyan Tree be commonly found.", "Where can the Banyan Tree be commonly found!", "Where can the Banyan Tree be commonly found,", "A", "Question starting with 'Where' ends with question mark ?"),
        ("Spot the capitalization mistake in: 'ayurveda uses banyan fruit to treat skin irritation.'", "'ayurveda' should be capitalized ('Ayurveda'); 'banyan fruit' is correct.", "'banyan' should be uppercase.", "'Ayurveda' should be lowercase.", "No mistake.", "A", "Traditional medical system 'Ayurveda' must be capitalized."),
        ("Choose the correctly punctuated dialogue sentence:", "\"The banyan tree lives for centuries,\" said Father.", "the banyan tree lives for centuries said Father.", "\"The banyan tree lives for centuries\" said Father", "The banyan tree lives for centuries, said Father.", "A", "Quotation marks around dialogue, comma inside quote, capital T."),
        ("Identify where a COMMA is missing: 'The tree has roots branches and green leaves.'", "Between 'roots' and 'branches' ('roots, branches')", "After 'The'", "After 'leaves'", "No comma needed", "A", "Commas separate items in list: 'roots, branches and green leaves'."),
        ("Which sentence uses the apostrophe correctly for possession?", "This is the banyan tree's fruit.", "This is the banyan trees' fruit.", "This is the banyan trees fruit.", "This is the banyan tree's' fruit.", "A", "banyan tree's indicates singular possession."),
        ("Select the sentence with CORRECT punctuation for an exclamatory statement:", "What a giant banyan tree this is!", "What a giant banyan tree this is?", "What a giant banyan tree this is.", "What a giant banyan tree this is,", "A", "Exclamatory statement ends with exclamation mark !"),
        ("Which contraction is written correctly for 'it is'?", "it's", "its'", "it'es", "i'ts", "A", "it's is standard contraction."),
        ("Find the sentence with NO capitalization errors:", "The Banyan Tree is the national tree of India.", "the banyan tree is the national tree of india.", "The Banyan Tree Is The National Tree Of India.", "the Banyan Tree is the national tree of India.", "A", "'Banyan Tree', 'India' capitalized as proper nouns."),
        ("What punctuation mark belongs in the blank? 'The child exclaimed, \"Look at those massive aerial roots__\"'", "!", ".", "?", ",", "A", "Exclamation mark ! expresses wonder."),
        ("Choose the correct form for 'does not':", "doesn't", "does'nt", "doesnt'", "d'oesnt", "A", "doesn't is standard contraction."),
        ("Identify the punctuation error: 'The roots are long, the branches are wide.'", "Comma splice between two independent clauses (should be full stop or 'and').", "Missing question mark.", "Missing capital letters.", "No error.", "A", "Two complete sentences separated only by comma."),
        ("Select the sentence with proper use of capital letters for religions and nations:", "The banyan tree is sacred in Hinduism in India.", "the banyan tree is sacred in hinduism in india.", "The banyan tree is sacred in hinduism in India.", "the Banyan tree is sacred in Hinduism in india.", "A", "Names 'Hinduism', 'India' all capitalized."),
        ("Which sentence correctly uses an apostrophe for possessive noun?", "The tree's canopy provides shade.", "The trees' canopy provides shade.", "The trees canopy provides shade.", "The tree's' canopy provides shade.", "A", "tree's indicates singular possession."),
        ("Identify the correct punctuation for a list of items: 'The banyan tree is found in ____'", "India, Nepal, and Bangladesh.", "India Nepal and Bangladesh.", "India; Nepal; and Bangladesh.", "India: Nepal: and Bangladesh.", "A", "Commas separate items in list."),
        ("Choose the sentence that correctly asks a question about the story:", "How long does a Banyan Tree live?", "How long does a Banyan Tree live.", "How long does a Banyan Tree live!", "how long does a Banyan Tree live.", "A", "Capital H, ends with question mark ?"),
        ("Fix the sentence: 'what is the national tree of india'", "What is the national tree of India?", "What is the national tree of India.", "what is the national tree of India!", "Where is India's tree?", "A", "Capital W, capital I, ends with ?"),
        ("Which of these sentences is punctuated PERFECTLY?", "Mother said, \"The Banyan Tree is the national tree of India!\"", "Mother said \"the Banyan Tree is the national tree of India!\"", "mother said, \"The Banyan Tree is the national tree of India!\"", "Mother said, \"The Banyan Tree is the national tree of India.\"", "A", "Capital M, comma after said, speech marks around dialogue with ! inside.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH10_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Context Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Punctuation Application & Dialogue Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze and count ALL capitalization and punctuation errors in: 'on monday teacher said in india, the banyan tree is sacred in hinduism and buddhism'", "5 errors (on->On, monday->Monday, india->India, banyan tree capitalization, hinduism->Hinduism, buddhism->Buddhism, period)", "2 errors", "3 errors", "7 errors", "A", "Starts sentence, day name, country name, religion names, period."),
        ("Correct the entire dialogue paragraph: 'the guide asked do you see the aerial roots the child replied yes they grow down from the branches'", "\"Do you see the aerial roots?\" asked the guide. The child replied, \"Yes, they grow down from the branches.\"", "the guide asked \"do you see the aerial roots\" the child replied \"yes they grow down from the branches.\"", "The guide asked, Do you see the aerial roots. The child replied, Yes they grow down from the branches.", "\"Do you see the aerial roots?\" Asked the guide. The child replied \"Yes they grow down from the branches?\"", "A", "Full proper quotation, dialogue tags, capitalization, and terminal punctuation."),
        ("Distinguish between singular possessive and contraction: 'The banyan tree**'**s life is long, and it**'**s the national tree of India.'", "First 's is possessive (life of banyan tree); second 's is contraction (it is).", "Both are possessive.", "Both are contractions.", "First is contraction; second is possessive.", "A", "banyan tree's life = life of banyan tree; it's = it is."),
        ("Spot the subtle punctuation flaw in this dialogue: '\"The banyan tree is huge,\" Said the guide.'", "'Said' should be lowercase 'said' because it continues the dialogue tag outside quotation marks.", "'The' should be lowercase.", "Commas should be outside quotes.", "No flaw.", "A", "Dialogue tags following quotes start with lowercase unless proper nouns."),
        ("Which sentence correctly uses punctuation to show contrast?", "The banyan tree is ancient, but its leaves remain green.", "The banyan tree is ancient but, its leaves remain green.", "The banyan tree is ancient but its leaves remain green!", "The banyan tree is ancient; but its leaves remain green?", "A", "Comma before coordinating conjunction 'but' joining two independent clauses."),
        ("Reconstruct with perfect punctuation: 'the banyan tree lives for 200-500 years in india'", "The Banyan Tree lives for 200-500 years in India.", "the banyan tree lives for 200-500 years in india.", "The Banyan Tree lives for 200-500 years in India", "The banyan tree lives for 200 500 years in india.", "A", "The Banyan Tree, hyphen in 200-500, India, period."),
        ("Identify why exclamation mark is necessary here: '\"Look at the massive banyan tree! It covers an entire acre!\"'", "Because the speaker is expressing intense awe at the tree's immense size.", "Because banyan is green.", "Because wood is hard.", "Because sentence is long.", "A", "Exclamation mark communicates intense awe at immense scale."),
        ("Choose the correctly punctuated sentence containing an appositive phrase:", "The Banyan Tree, the national tree of India, is considered sacred.", "The Banyan Tree the national tree of India is considered sacred.", "The Banyan Tree, the national tree of India is considered sacred.", "The Banyan Tree the national tree of India, is considered sacred.", "A", "Appositive phrase 'the national tree of India' is set off by commas."),
        ("Analyze the use of hyphen in: 'The banyan tree has a long life-span.'", "Hyphen joins compound noun (life-span).", "Hyphen replaces comma.", "Hyphen indicates question.", "Hyphen is an apostrophe.", "A", "Compound nouns take hyphens."),
        ("Identify the correct sentence with direct speech quote within text:", "Teacher explained, \"Ayurveda uses banyan fruit,\" and students took notes.", "Teacher explained \"Ayurveda uses banyan fruit\" and students took notes.", "Teacher explained, 'Ayurveda uses banyan fruit,' and students took notes.", "Teacher explained: \"Ayurveda uses banyan fruit\" and students took notes.", "A", "Comma before quote, double quotation marks around direct speech, comma inside quote."),
        ("Spot the missing apostrophe: 'The banyan trees branches drop aerial roots.'", "Missing apostrophe in 'tree's' -> 'The banyan tree's branches...'", "Missing apostrophe in 'roots''", "Missing apostrophe in 'drop''", "No apostrophe needed", "A", "'The banyan tree's branches' requires possessive apostrophe."),
        ("HOTS Reasoning: Why does putting a comma in different places change meaning? Compare: 'Children, said teacher, should respect ancient banyan trees.' vs 'Children said, \"Teacher should respect ancient banyan trees.\"'", "In the first, teacher instructs children; in the second, children instruct teacher.", "Both mean the exact same thing.", "The first is a question.", "Commas do not affect meaning.", "A", "Punctuation alters who speaks and who is instructed."),
        ("Correct all 4 errors in: 'whats the banyan trees lifespan asked the student'", "\"What's the banyan tree's life-span?\" asked the student.", "whats the banyan trees lifespan? asked the student.", "\"What's the banyan trees lifespan.\" asked the student.", "\"whats the banyan trees lifespan?\" Asked the student.", "A", "Quotation marks, capital W, possessive tree's, hyphenated life-span, question mark, period at end."),
        ("Identify the rule for capitalizing names of religions like 'Hinduism' and 'Buddhism':", "Names of religions and religious traditions always take initial capital letters.", "Religion names are never capitalized.", "Religion names are capitalized only at end of sentence.", "Religion names must be written in ALL CAPS.", "A", "Proper names of religions take initial capitals.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH10_CAT05_Q{idx:02d}"
        qtxt = f"Higher Order Punctuation Analysis & Dialogue Formatting:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Punctuation & Dialogue Editing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 6. Phonics & Vowel Digraphs (50 Qs)
# ---------------------------------------------------------------------------
def build_phonics_digraphs():
    header = "# Category 6: Phonics & Vowel Digraphs — Chapter 10: The Banyan Tree\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_phonics = [
        ("Which vowel digraph is present in the word **'tree'** (in Chapter 10)?", "ee", "ea", "ai", "ou", "A", "'ee' is the vowel digraph in tree."),
        ("Identify the vowel digraph in the word **'root'**:", "oo", "ee", "oa", "ui", "A", "'oo' forms the vowel sound in root."),
        ("Which word from the story contains the **'ou'** vowel digraph?", "ground", "tree", "root", "leaf", "A", "'ground' contains the 'ou' digraph."),
        ("Identify the vowel digraph in the word **'leaf'**:", "ea", "ee", "ow", "oo", "A", "'ea' forms long /e/ sound in leaf."),
        ("Which vowel digraph appears in the word **'treat'**?", "ea", "ay", "ee", "oa", "A", "'ea' makes long /e/ sound in treat."),
        ("Find the word with the **'oo'** vowel digraph: 'Paper is made from the wood of this tree.'", "wood", "paper", "made", "tree", "A", "'wood' contains 'oo' vowel sound pattern."),
        ("Which word from the story rhymes with **'tree'**?", "see", "try", "tray", "tie", "A", "'see' rhymes with 'tree'."),
        ("Which word from the story rhymes with **'root'**?", "boot", "rate", "rot", "road", "A", "'boot' rhymes with 'root'."),
        ("Identify the vowel digraph in the word **'boasted'**:", "oa", "ou", "ow", "oo", "A", "'oa' makes long /o/ sound in boasted."),
        ("Which word from the story rhymes with **'ground'**?", "found", "grand", "gold", "gone", "A", "'found' rhymes with 'ground'."),
        ("Identify the vowel digraph in **'aerial'**:", "ae", "ur", "or", "oo", "A", "'ae' vowel letter combination in aerial."),
        ("Which word from Chapter 10 has the **'ea'** digraph making a long /e/ sound?", "treat", "head", "heavy", "dead", "A", "'treat' has 'ea' making long /e/ sound."),
        ("Which word rhymes with **'day'**?", "away", "die", "due", "door", "A", "'away' rhymes with 'day'."),
        ("Identify the silent letter in **'grow'** (as in 'roots grow from branches'):", "w (in some phonetic contexts / silent w)", "g", "r", "o", "A", "'ow' forms vowel sound, 'w' acts as silent glide letter."),
        ("Which word from the story has long /i/ sound spelled with **'igh'**?", "high", "bought", "bowl", "baker", "A", "'igh' in high makes long /i/ sound."),
        ("Find the word with **'ou'** digraph: 'They sat around the banyan tree.'", "around", "banyan", "they", "tree", "A", "'around' contains 'ou' digraph."),
        ("Which word rhymes with **'shade'**?", "made", "sat", "so", "seat", "A", "'made' rhymes with 'shade'."),
        ("Identify the silent letter in the word **'know'** (as in 'did not know'):", "k", "n", "o", "w", "A", "Initial 'k' before 'n' is silent.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_phonics, start=1):
        qid = f"BK02_CH10_CAT06_Q{idx:02d}"
        qtxt = f"Phonics & Vowel Digraph Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Vowel Digraphs & Rhyming Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Compare the **'ea'** digraph sound in **'treat'** and **'bread'**. What is the difference?", "'treat' has long /e/ sound; 'bread' has short /e/ sound.", "Both have short /e/ sound.", "Both have long /a/ sound.", "'treat' has short /e/; 'bread' has long /e/.", "A", "'ea' can make long /e/ (treat) or short /e/ (bread)."),
        ("Select the word pair from Chapter 10 that has the SAME vowel digraph sound:", "tree - leaf", "high - bread", "abode - roar", "ground - sweet", "A", "'tree' (ee) and 'leaf' (ea) both make long /e/ sound."),
        ("Which word contains SILENT letters? (high, tree, root, branch)", "high", "tree", "root", "branch", "A", "'high' has silent 'gh'."),
        ("Identify the odd one out based on vowel sound: (tree, leaf, treat, bread)", "bread", "tree", "leaf", "treat", "A", "'bread' has short /e/ sound; others have long /e/ sound."),
        ("Which digraph completes the word for plant part? 'r__t'", "oo", "ee", "ai", "ou", "A", "'root' uses 'oo' digraph."),
        ("Group these story words by digraph: **ground**, **out**, **around**. What digraph do they all share?", "ou", "ow", "oo", "oi", "A", "All share 'ou' making /ow/ diphthong sound."),
        ("Find the word with consonant digraph **'th'** from the story: 'The banyan tree has a long **life-span**.'", "the", "banyan", "has", "tree", "A", "'the' contains voiced 'th' consonant digraph."),
        ("Which of these words has the **'ow'** vowel digraph making long /o/ sound? (grow, show, blow, all of these)", "all of these", "grow", "show", "blow", "A", "grow, show, blow all share 'ow' long /o/ sound."),
        ("Identify the vowel digraph in **'fruit'**:", "ui", "ai", "ea", "oo", "A", "'ui' forms /oo/ sound in fruit."),
        ("Which word from the story has silent **'k'**? (know, knee, knife, all of these)", "all of these", "know", "knee", "knife", "A", "know, knee, knife all have silent initial 'k' before 'n'."),
        ("Select the word that rhymes with **'root'** and fits sentence: 'The aerial root took ____.'", "root", "boot", "hoot", "suit", "A", "'root' fits the sentence."),
        ("Identify the digraph in **'reached'**:", "ea", "ee", "ai", "oa", "A", "'ea' makes long /e/ sound."),
        ("Which word has the short /u/ sound made by **'ou'**? (touch, ground, out, shout)", "touch", "ground", "out", "shout", "A", "'touch' has short /u/ sound with 'ou'."),
        ("Find the R-controlled vowel sound in: 'Paper is made from **wood** / **part**.'", "ar sound in part", "ea", "ou", "ai", "A", "R-controlled vowel in part."),
        ("Which word contains the **'oi'** diphthong/digraph? (choice, voice, point, all of these)", "all of these", "choice", "voice", "point", "A", "choice, voice, point all contain 'oi'."),
        ("Identify the soft **'c'** sound in Chapter 10 vocabulary: (place, sacred, descend, place and descend)", "place and descend", "sacred", "wood", "root", "D", "place (/s/ sound) and descend (/s/ sound) have soft 'c' before 'e' or 'i'."),
        ("Which word has a soft **'g'** sound? (germ, magic, region, all of these)", "all of these", "germ", "magic", "region", "A", "germ, magic, region all have soft /j/ sound for 'g'."),
        ("Choose the correct spelling with **'ee'** digraph for plant structure:", "tree", "tre", "trea", "trie", "A", "tree is standard spelling with 'ee'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH10_CAT06_Q{idx:02d}"
        qtxt = f"Phonics Analysis & Sound Pattern Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Phonic Rules & Sound Discrimination", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the phonics rule: Why does 'c' in **'place'** sound like /s/, but 'c' in **'sacred'** sounds like /k/?", "Because 'c' followed by 'e', 'i', or 'y' makes soft /s/ sound (place); before 'r', 'a', 'o', 'u' it makes hard /k/ sound (sacred).", "Because place is wide.", "Because sacred is holy.", "There is no rule.", "A", "Soft 'c' rule: c + e, i, y = /s/ sound."),
        ("Categorize the 'ea' digraphs into long /e/ vs short /e/: (treat, leaf, bread, heavy, lead [metal])", "Long /e/: treat, leaf; Short /e/: bread, heavy, lead [metal]", "All are long /e/.", "All are short /e/.", "Long /e/: bread; Short /e/: treat", "A", "treat, leaf make long /e/; bread, heavy, lead (metal) make short /e/."),
        ("Identify the word pair where SILENT letters exist in BOTH words:", "high - know", "tree - root", "ground - leaf", "branch - fruit", "A", "'high' (silent gh) and 'know' (silent k)."),
        ("Decode the phonics blend: Which word contains a 3-letter consonant blend at the start?", "spreads / sprout", "tree", "root", "leaf", "A", "'spr' blend type."),
        ("Examine the hard vs soft 'g' rule: Why is 'g' soft in **'germ'** but hard in **'ground'**?", "'g' followed by 'e', 'i', or 'y' makes soft /j/ sound (germ); 'g' before 'r' or 'a','o','u' makes hard /g/ sound (ground).", "Because germ is tiny.", "Because ground is hard.", "There is no rule.", "A", "Soft 'g' rule: g + e, i, y = /j/ sound."),
        ("Find the word with BOTH a vowel digraph AND a silent letter:", "highest", "tree", "root", "leaf", "A", "'highest' has 'igh' trigraph with silent 'gh'."),
        ("Differentiate diphthongs: Which pair produces the /ow/ sound as in **'ground'**?", "ground - out", "voice - coin", "paid - day", "boat - coat", "A", "'ground' and 'out' share /ow/ diphthong sound."),
        ("Analyze homophones: 'The **root** / **route** of the tree reached the soil.' Which word means plant part?", "root", "route", "rute", "roote", "A", "'root' (part of plant) and 'route' (pathway) are homophones."),
        ("Identify the phonic pattern in **'inflammation'**: What vowel sound does the first 'a' make?", "Short /a/ sound", "Long /a/ sound", "Silent sound", "Short /u/ sound", "A", "'in-flam-ma-tion' 'a' in 'flam' makes short /a/ sound."),
        ("Sort by ending sound: Which word ends with the /z/ sound? (trees, roots, fruits, branches)", "trees", "roots", "fruits", "branches", "A", "Plurals ending in voiced vowels take /z/ ending sound (trees)."),
        ("Spot the word where 'k' is SILENT: (know, knee, knife, all of these)", "all of these", "know", "knee", "knife", "A", "'k' is silent before 'n' in know, knee, knife."),
        ("HOTS Reasoning: Why do 'root' and 'route' sound identical but have different spellings and meanings?", "They are homophones (same sound, different spelling/meaning).", "They are synonyms.", "They are antonyms.", "They are plurals.", "A", "Homophones share pronunciation but differ in spelling/meaning."),
        ("Identify the compound word from story concepts containing two simple words:", "life-span / doorstep", "banyan", "Ayurveda", "aerial", "A", "life-span = life + span."),
        ("Determine the syllable count and stress: How many syllables are in **'inflammation'**?", "4 syllables (in-flam-ma-tion)", "3 syllables", "5 syllables", "2 syllables", "A", "in-flam-ma-tion has 4 syllables.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH10_CAT06_Q{idx:02d}"
        qtxt = f"Higher Order Phonics & Orthographic Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Phonetic Rules & Homophone Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 7. Question Words & Interrogatives (50 Qs)
# ---------------------------------------------------------------------------
def build_question_words():
    header = "# Category 7: Question Words & Interrogatives — Chapter 10: The Banyan Tree\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_qwords = [
        ("___ can the Banyan Tree be commonly found?", "Where", "Who", "What", "Why", "A", "'Where' asks about location (in many places in India)."),
        ("___ is special about the roots of the Banyan Tree?", "What", "Who", "Where", "Why", "A", "'What' asks about feature (aerial roots grow from branches and descend to the ground)."),
        ("___ long does a Banyan Tree usually live?", "How", "Who", "Where", "Why", "A", "'How long' asks about lifespan duration (200-500 years)."),
        ("___ is the banyan fruit used for in Ayurveda?", "What", "Who", "Where", "Why", "A", "'What' asks about purpose (to treat inflammation and skin irritation)."),
        ("___ material is made from the wood of the banyan tree?", "What", "Who", "Where", "Why", "A", "'What material' asks about product (paper)."),
        ("___ religions consider the Banyan Tree sacred?", "Which", "Who", "Where", "Why", "A", "'Which religions' asks for identification (Hinduism and Buddhism)."),
        ("___ country has chosen the Banyan Tree as its national tree?", "Which", "Who", "Where", "Why", "A", "'Which country' asks about nation (India)."),
        ("___ do aerial roots grow from?", "Where / What", "Who", "Why", "When", "A", "'Where' asks about origin part (from the branches)."),
        ("___ do aerial roots descend to?", "Where", "Who", "What", "Why", "A", "'Where' asks about destination (to the ground)."),
        ("___ allows the banyan tree to spread so far?", "What", "Who", "Where", "Why", "A", "'What' asks about mechanism (aerial roots forming new prop trunks)."),
        ("___ is the average life-span of a banyan tree?", "What", "Who", "Where", "Why", "A", "'What' asks about figure (200-500 years)."),
        ("___ medical system uses banyan fruit to treat skin irritation?", "Which", "Who", "Where", "Why", "A", "'Which' asks about tradition (Ayurveda)."),
        ("___ part of the tree is used to make paper?", "Which", "Who", "Where", "Why", "A", "'Which part' asks for component (the wood)."),
        ("___ animal or bird species live in the banyan tree?", "Which / What", "Who", "Where", "Why", "A", "'Which' asks about animal species."),
        ("___ condition is treated using banyan fruit?", "Which / What", "Who", "Where", "Why", "A", "'Which condition' asks about ailments (inflammation and skin irritation)."),
        ("___ does the banyan tree provide for travelers?", "What", "Who", "Where", "Why", "A", "'What' asks about benefits (shade and shelter)."),
        ("___ is the Banyan Tree considered sacred?", "Why", "Who", "Where", "What", "A", "'Why' asks for cultural/religious reasons (symbol of longevity, eternal life)."),
        ("___ creates new prop trunks for the banyan tree?", "What", "Who", "Where", "Why", "A", "'What' asks about mechanism (aerial roots reaching the soil).")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_qwords, start=1):
        qid = f"BK02_CH10_CAT07_Q{idx:02d}"
        qtxt = f"Choose the correct **question word** (Who, What, Where, Why, How, When):\n\n\"{q_blank} _____?\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Question Word Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Match question to answer: Question: '___ are aerial roots important?' Answer: 'Because they descend to the ground and allow the tree to spread further.'", "Why", "What", "Where", "Who", "A", "'Why' asks for reasons ('Because...')."),
        ("Match question to answer: Question: '___ is the banyan tree found?' Answer: 'In many places across India.'", "Where", "Who", "Why", "When", "A", "'Where' asks for location."),
        ("Choose the correct question word for DURATION: '___ many years can a banyan tree live?'", "How", "Where", "Who", "Why", "A", "'How many' inquires about number of years (200-500 years)."),
        ("Form an asking sentence: 'Paper is made from wood.' -> '____ is paper made from?'", "What", "Who", "Why", "Where", "A", "'What' inquires about raw material."),
        ("Identify the INCORRECT question word usage: '**Why** is the national tree of India?'", "'Why' should be 'What'", "'Why' should be 'Where'", "'Why' should be 'When'", "No error", "A", "'What is the national tree of India?' asks for identity."),
        ("Select the proper interrogative sentence:", "Why is the banyan tree considered sacred?", "Why the banyan tree is considered sacred?", "Why does the banyan tree is considered sacred?", "Why banyan tree sacred?", "A", "Interrogative word + auxiliary 'is' + subject + predicate."),
        ("Which question word asks about MANNER or METHOD? '___ does the banyan tree spread across acres of land?'", "How", "Who", "What", "Where", "A", "'How' inquires about method/manner (by growing aerial roots from branches)."),
        ("Complete the question: '___ of the two religions consider the banyan tree sacred?'", "Which", "What", "Where", "Why", "A", "'Which' chooses between specific options (Hinduism and Buddhism)."),
        ("Change statement to question: 'The banyan tree is India's national tree.' -> '____ is India's national tree?'", "Which / What", "Who", "Where", "Why", "A", "'Which' asks for specific tree."),
        ("Fill in the blank: '___ old can a banyan tree get?'", "How", "What", "Where", "Why", "A", "'How old' measures age."),
        ("Identify the question word in: 'Whom does the banyan tree provide shade to?'", "Whom", "does", "banyan", "shade", "A", "'Whom' is the interrogative pronoun asking about recipient travelers/people."),
        ("Choose the question that matches this answer: 'In Ayurveda, it is used to treat inflammation and skin irritation.'", "What is banyan fruit used for?", "Where does the banyan tree grow?", "Who planted the tree?", "What is paper made from?", "A", "'What is banyan fruit used for?' matches answer about medical uses."),
        ("Fill in the blank: '___ part of the banyan tree grows downward into the soil?'", "Which", "Who", "Why", "Where", "A", "'Which part' asks for identification (aerial roots)."),
        ("Complete: '___ years is the average lifespan of a banyan tree?'", "How many", "How much", "Who", "Where", "A", "'How many' asks about countable quantity (years)."),
        ("Select the correct question for: 'Paper is made from the wood of the banyan tree.'", "What is made from the wood of the banyan tree?", "Where is paper made?", "Why do birds eat fruit?", "Who is the national tree?", "A", "'What is made from...' asks for product."),
        ("Which question word inquires about POSSESSION? '___ fruit is used in Ayurveda?'", "Whose", "Who", "Where", "Why", "A", "'Whose' / 'Which tree's' asks about ownership/source."),
        ("Form question: 'Many birds nest in the banyan tree.' -> '____ birds nest in the banyan tree?'", "How many", "How much", "Why", "Where", "A", "'How many' asks for countable number."),
        ("Identify the question mark error: 'Why is the banyan tree important.' Correct it:", "Why is the banyan tree important?", "Why is the banyan tree important!", "Why is the banyan tree important,", "Why is the banyan tree important;", "A", "Questions must end with question mark ?")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH10_CAT07_Q{idx:02d}"
        qtxt = f"Question Formation & Context Alignment:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Interrogative Sentence Formation", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence structure: 'Why do aerial roots descend to the ground?' What is the syntax pattern?", "Question Word + Helping Verb (do) + Subject (aerial roots) + Main Verb (descend) + Prepositional Phrase", "Question Word + Main Verb + Subject", "Subject + Question Word + Verb", "Helping Verb + Question Word + Subject", "A", "Standard English question syntax."),
        ("Differentiate between 'How many' vs 'How much': '___ years' vs '___ shade'", "'How many' for countable years; 'How much' for uncountable shade.", "Both use 'How many'.", "Both use 'How much'.", "'How much' for years; 'How many' for shade.", "A", "Countable nouns take 'How many'; uncountable nouns take 'How much'."),
        ("Spot the syntax error in question: 'Where aerial roots grow on the banyan tree?' Correct it:", "Where **do** aerial roots grow on the banyan tree?", "Where aerial roots grow banyan tree?", "Where grew aerial roots banyan tree?", "Where does aerial roots grow on banyan tree?", "A", "Present simple questions require auxiliary 'do' before plural subject 'aerial roots' and base verb 'grow'."),
        ("Framing multi-question interview: What sequence of question words logically reveals the banyan tree characteristics?", "What is the Banyan Tree -> Where does it grow -> How do aerial roots function -> Why is it the national tree", "How -> Who -> Why -> What", "Where -> Where -> Where -> Where", "Why -> Why -> Why -> Why", "A", "Reveals identity, habitat, botanical structure, and national significance."),
        ("Transform the statement into a formal question: 'The banyan tree's wide canopy provides a sanctuary for biodiversity.'", "How does the banyan tree's expansive canopy function as a ecological sanctuary for local wildlife?", "Where is India?", "Who is Buddha?", "What is a leaf?", "A", "Directly targets ecological sanctuary function."),
        ("Analyze this ambiguous question: 'What does it treat?' How can it be made precise?", "Add specific context: 'What medical conditions are treated using banyan fruit in Ayurveda?'", "Make it shorter: 'What treat?'", "Change to: 'Where treat?'", "Remove 'What'.", "A", "Adding specific context clarifies which medical treatment."),
        ("Choose the correct question pair for dialogue: Student: '___ are these roots growing from branches?' Teacher: '___ about observing how they reach the soil below?'", "Why, How", "Who, Where", "Where, How", "When, Whose", "A", "Why (reason for branch roots), How about (suggestion)."),
        ("Spot the DOUBLE auxiliary error: 'Why do aerial roots descended to the ground?'", "'do' requires base verb 'descend', not past tense 'descended'.", "'do' should be 'is'.", "'Why' should be 'How'.", "No error.", "A", "Auxiliary 'do' must be followed by base form of verb ('descend')."),
        ("Reconstruct question from answer: Answer: 'The banyan tree has an average life-span of 200 to 500 years.'", "Question: 'What is the average life-span of a banyan tree?'", "Question: 'Where did they go?'", "Question: 'Who ate banyan fruit?'", "Question: 'Why is paper white?'", "A", "Targets lifespan duration."),
        ("Form indirect question: 'The child asked why the banyan tree was chosen as the national tree.' What is the sentence type?", "Assertive statement containing an embedded indirect question.", "Direct question requiring question mark.", "Exclamatory sentence.", "Command.", "A", "Indirect questions are statements ending with full stop."),
        ("Identify the correct question word for moral reasoning: '___ is conserving ancient banyan trees essential for environmental balance?'", "Why", "What", "Who", "Where", "A", "'Why' inquires into the ecological reason for conservation."),
        ("HOTS Reasoning: Why is 'Who' used for people but 'Which' used when selecting from a specific group of trees?", "'Who' is general for humans; 'Which' is used when choosing from a defined limited set of trees/objects.", "'Who' is for inanimate objects.", "'Which' is only for numbers.", "Both are identical.", "A", "'Which of the trees...' selects from a defined group."),
        ("Correct all errors in: 'why is the banyan tree the national tree of india'", "Why is the Banyan Tree the national tree of India?", "Why is the banyan tree the national tree of india.", "Whom is the banyan tree national tree?", "Why does the banyan tree national tree of India?", "A", "Capital W, capital B, T, I, question mark at end."),
        ("Select the question that evaluates Higher Order Thinking (HOTS) about Chapter 10:", "How does the unique growth mechanism of aerial roots enable a single banyan tree to expand into a self-supporting forest ecosystem over centuries?", "How long does a banyan tree live?", "Where is India?", "Is the fruit eaten by birds?", "A", "Asks student to evaluate botanical self-propagation and ecosystem formation.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH10_CAT07_Q{idx:02d}"
        qtxt = f"Higher Order Interrogative Analysis & Syntax:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Question Syntax & Analytical Framing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 8. Present Continuous Tense (-ing) (50 Qs)
# ---------------------------------------------------------------------------
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense (-ing) — Chapter 10: The Banyan Tree\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_ing = [
        ("The banyan tree is **growing** rapidly in the warm climate.", "growing", "banyan tree", "is", "climate", "A", "'growing' is verb + -ing form."),
        ("Aerial roots are **descending** to the ground.", "descending", "roots", "are", "ground", "A", "'descending' is verb + -ing form."),
        ("The tree is **spreading** its branches over a wide area.", "spreading", "tree", "is", "area", "A", "'spreading' is verb + -ing form."),
        ("Doctors are **using** banyan fruit to treat skin irritation.", "using", "doctors", "are", "irritation", "A", "'using' is verb + -ing form."),
        ("Workers are **making** paper from banyan wood.", "making", "workers", "are", "wood", "A", "'making' is verb + -ing form."),
        ("Birds are **building** nests in the dense branches.", "building", "birds", "are", "branches", "A", "'building' is verb + -ing form."),
        ("The tree is **providing** cool shade for travelers.", "providing", "tree", "is", "travelers", "A", "'providing' is verb + -ing form."),
        ("Children are **playing** under the banyan tree.", "playing", "children", "are", "tree", "A", "'playing' is verb + -ing form."),
        ("The roots are **anchoring** the tree firmly in soil.", "anchoring", "roots", "are", "soil", "A", "'anchoring' is verb + -ing form."),
        ("Animals are **eating** the ripe banyan fruits.", "eating", "animals", "are", "fruits", "A", "'eating' is verb + -ing form."),
        ("People are **worshiping** under the sacred banyan tree.", "worshiping", "people", "are", "tree", "A", "'worshiping' is verb + -ing form."),
        ("Monkeys are **swinging** from the aerial roots.", "swinging", "monkeys", "are", "roots", "A", "'swinging' is verb + -ing form."),
        ("The sun is **shining** through the banyan leaves.", "shining", "sun", "is", "leaves", "A", "'shining' is verb + -ing form."),
        ("Botanists are **studying** the ancient banyan tree.", "studying", "botanists", "are", "tree", "A", "'studying' is verb + -ing form."),
        ("Raindrops are **falling** on the broad banyan leaves.", "falling", "raindrops", "are", "leaves", "A", "'falling' is verb + -ing form."),
        ("The tree is **absorbing** water from the deep ground.", "absorbing", "tree", "is", "ground", "A", "'absorbing' is verb + -ing form."),
        ("Visitors are **admiring** the national tree of India.", "admiring", "visitors", "are", "India", "A", "'admiring' is verb + -ing form."),
        ("The canopy is **expanding** every year.", "expanding", "canopy", "is", "year", "A", "'expanding' is verb + -ing form.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_ing, start=1):
        qid = f"BK02_CH10_CAT08_Q{idx:02d}"
        qtxt = f"Identify the **present continuous (-ing) verb** in this sentence:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the present continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Present Continuous Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("What is the correct -ing spelling rule for **'descend'**? (The roots are ____.)", "descending (add -ing)", "descendding", "descendeing", "descendng", "A", "Regular verb adding -ing (descending)."),
        ("What is the correct -ing spelling rule for **'make'**? (They are ____ paper.)", "making (drop final silent e)", "makeing", "makking", "makng", "A", "Drop final silent 'e' before adding -ing (making)."),
        ("What is the correct -ing spelling rule for **'spread'**? (The tree is ____.)", "spreading (add -ing)", "spreadding", "spreadeing", "spreadng", "A", "Regular verb adding -ing (spreading)."),
        ("Fill in the blank with present continuous form: 'The banyan tree (grow) ____ near the village.'", "is growing", "was grow", "are grow", "is growed", "A", "Singular subject takes 'is growing'."),
        ("Choose the sentence in PRESENT CONTINUOUS tense:", "The aerial roots are growing down right now.", "The aerial roots grew down last year.", "The aerial roots will grow down next month.", "The aerial roots grew yesterday.", "A", "'are growing' is present continuous."),
        ("Fill in the blanks: 'The roots ____ (descend), and the leaves ____ (absorb) sunlight.' ", "are descending, are absorbing", "is descending, is absorbing", "are descend, is absorb", "was descending, were absorbing", "A", "Plural 'roots' takes 'are descending'; plural 'leaves' takes 'are absorbing'."),
        ("Identify the spelling mistake in: 'Workers are **makeing** paper from wood.'", "'makeing' should be 'making'", "'makeing' should be 'making'", "'are' should be 'is'", "No mistake", "A", "Make drops silent e before -ing (making)."),
        ("Select the correct -ing form for **'provide'**:", "providing", "provideing", "providring", "providng", "A", "Drop silent 'e': provide -> providing."),
        ("Which sentence describes an action HAPPENING RIGHT NOW?", "The children are swinging from the aerial roots.", "The children swung from the roots yesterday.", "The children swing from the roots every day.", "The children will swing tomorrow.", "A", "Present continuous ('are swinging') describes ongoing action right now."),
        ("Fill in the blank: 'I ____ (examine) a leaf from the banyan tree.'", "am examining", "is examining", "are examining", "am examineing", "A", "Subject 'I' takes 'am examining'."),
        ("Choose the correct form: 'The birds ____ (nest) in the banyan branches.'", "are nesting", "is nesting", "am nesting", "are nest", "A", "Plural subject 'birds' takes 'are nesting'."),
        ("Identify the verb in: 'Why are you climbing the banyan tree?'", "are climbing", "Why", "you", "tree", "A", "Helping verb 'are' + main verb 'climbing' form present continuous."),
        ("What is the -ing form of **'swing'**?", "swinging", "swingging", "swingeing", "swingng", "A", "Regular verb adding -ing (swinging)."),
        ("What is the -ing form of **'shade'**?", "shading", "shadeing", "shadding", "shadng", "A", "Drop silent e: shade -> shading."),
        ("Change simple present to continuous: 'Roots reach the ground.' -> 'Roots ____ the ground.'", "are reaching", "reached", "were reaching", "will reach", "A", "are reaching."),
        ("Fill in the blank: 'The banyan tree ____ (expanding) across the field.'", "is expanding", "are expanding", "am expanding", "expanded", "A", "is expanding."),
        ("Identify the correct present continuous sentence:", "Look! The aerial root is touching the ground.", "Look! The aerial root touches the ground.", "Look! The aerial root touched the ground.", "Look! The aerial root touching the ground.", "A", "Exclamation 'Look!' introduces action happening now ('is touching')."),
        ("Select the correct -ing form for **'descend'**:", "descending", "descendding", "descendeing", "descendng", "A", "Regular verb adding -ing (descending).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH10_CAT08_Q{idx:02d}"
        qtxt = f"Present Continuous Grammar & Spelling Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Present Continuous Formation & Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze spelling rules for adding -ing to verbs: Group them correctly: (run, make, descend)", "run -> running (double consonant), make -> making (drop e), descend -> descending (add -ing)", "All just add -ing.", "All double the last letter.", "run -> runing, make -> makeing, descend -> descendding", "A", "3 distinct orthographic rules for -ing derivation."),
        ("Convert past tense narrative to present continuous picture scene: 'Roots grew while birds nested.'", "Roots are growing while birds are nesting.", "Roots growing while birds nesting.", "Roots were growing while birds nested.", "Roots will grow while birds nest.", "A", "Both verbs transformed to present continuous (are growing, are nesting)."),
        ("Spot the missing auxiliary verb in: 'Aerial roots descending and tree spreading wide.' Correct it:", "'Aerial roots **are** descending and tree **is** spreading wide.'", "'Aerial roots descending and tree spreading wide.'", "'Aerial roots **is** descending and tree **are** spreading.'", "No error.", "A", "Present continuous requires auxiliary (is/am/are) before -ing verb."),
        ("Differentiate state vs action: Why don't we usually say 'The banyan tree is **having** aerial roots'?", "Because 'have' expressing possession is a stative verb, not an active process.", "Because 'having' is hard to spell.", "Because roots are brown.", "Because India is warm.", "A", "Stative verbs (have, own, belong) expressing possession take simple present."),
        ("Identify the sentence with CORRECT present continuous subject-verb agreement:", "The aerial roots of the banyan tree are descending.", "The aerial roots of the banyan tree is descending.", "The aerial roots of the banyan tree am descending.", "The aerial roots of the banyan tree descending.", "A", "Plural subject ('roots') takes plural auxiliary 'are'."),
        ("Form negative present continuous: 'The banyan tree is losing its leaves.' -> Negative:", "The banyan tree is **not** losing its leaves.", "The banyan tree not losing its leaves.", "The banyan tree are no losing its leaves.", "The banyan tree isn't lose its leaves.", "A", "Add 'not' between auxiliary 'is' and main verb 'losing'."),
        ("Spot all THREE spelling errors: 'She is **makeing** tea, **runing** near tree, and **dieing** to see it.'", "'makeing' -> 'making'; 'runing' -> 'running'; 'dieing' -> 'dying'", "'makeing' -> 'makking'; 'runing' -> 'runing'; 'dieing' -> 'dieing'", "No errors.", "Only 'runing' is wrong.", "A", "making (drop e), running (double n), dying (-ie to -y)."),
        ("Rewrite as interrogative present continuous: 'The banyan tree is spreading rapidly.'", "**Is** the banyan tree spreading rapidly?", "Are the banyan tree spreading rapidly?", "The banyan tree spreading rapidly?", "Why the banyan tree is spreading rapidly?", "A", "Move auxiliary 'Is' to beginning of sentence."),
        ("Analyze action timeline: 'The school **is planting** a banyan tree tomorrow.' What does present continuous express here?", "A fixed future arrangement / planned action.", "Past completed action.", "Action that happened long ago.", "Uncertain rumor.", "A", "Present continuous can express planned future actions."),
        ("Choose the sentence showing PARALLEL present continuous actions:", "While aerial roots are descending, the main trunk is thickening.", "While roots descended, trunk is thickening.", "Roots are descending while trunk thickened.", "Roots descend while trunk thickens.", "A", "Both parallel ongoing actions use present continuous."),
        ("Correct the error: 'The roots are growwing down.'", "'growwing' should be 'growing' (single 'w').", "'are' should be 'is'.", "'down' should be capitalized.", "No error.", "A", "Grow + ing = growing."),
        ("HOTS Reasoning: Compare 'Roots grew down' (Past Simple) vs 'Roots are growing down' (Present Continuous). How does the meaning change?", "Past simple states a completed past event; present continuous describes an action currently in progress.", "Both mean the exact same thing.", "Past simple is for future; continuous is for past.", "Continuous means roots stopped.", "A", "Tense changes temporal aspect (completed vs ongoing)."),
        ("Form question: 'Why ____ the banyan tree ____ (spreading) so far?'", "is, spreading", "are, spreading", "am, spreading", "do, spreading", "A", "Singular subject banyan tree takes 'is ... spreading'."),
        ("Identify the correct present continuous sentence describing botanical growth:", "The aerial root system is transforming into secondary trunks.", "The aerial root system is transform into secondary trunks.", "The aerial root system are transforming into secondary trunks.", "The aerial root system transforming into secondary trunks.", "A", "Collective singular subject 'aerial root system' + is + transforming.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH10_CAT08_Q{idx:02d}"
        qtxt = f"Higher Order Present Continuous Analysis & Editing:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Continuous Tense Aspect & Error Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 9. Helping Verbs (Is, Am, Are) (50 Qs)
# ---------------------------------------------------------------------------
def build_helping_verbs():
    header = "# Category 9: Helping Verbs (Is, Am, Are) — Chapter 10: The Banyan Tree\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_hv = [
        ("The Banyan Tree ___ a huge tree found in India.", "is", "are", "am", "be", "A", "Singular subject 'The Banyan Tree' takes 'is'."),
        ("Aerial roots ___ growing from the high branches.", "are", "is", "am", "be", "A", "Plural subject 'Aerial roots' takes 'are'."),
        ("I ___ sitting under the shade of the banyan tree.", "am", "is", "are", "be", "A", "Pronoun 'I' takes 'am'."),
        ("The banyan fruit ___ used in Ayurveda to treat inflammation.", "is", "are", "am", "be", "A", "Singular subject 'banyan fruit' takes 'is'."),
        ("Paper ___ made from the wood of this tree.", "is", "are", "am", "be", "A", "Uncountable subject 'Paper' takes 'is'."),
        ("Hinduism and Buddhism ___ religions that consider it sacred.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("The Banyan Tree ___ the national tree of India.", "is", "are", "am", "be", "A", "Singular subject takes 'is'."),
        ("Birds and monkeys ___ living in the banyan branches.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("I ___ fascinated by aerial roots.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The lifespan of a banyan tree ___ 200 to 500 years.", "is", "are", "am", "be", "A", "Singular 'lifespan' takes 'is'."),
        ("The branches ___ wide and full of leaves.", "are", "is", "am", "be", "A", "Plural 'branches' takes 'are'."),
        ("India ___ home to many ancient banyan trees.", "is", "are", "am", "be", "A", "Singular 'India' takes 'is'."),
        ("You ___ studying Chapter 10.", "are", "is", "am", "be", "A", "Pronoun 'You' always takes 'are'."),
        ("The scientist ___ examining the banyan tree.", "is", "are", "am", "be", "A", "Singular 'scientist' takes 'is'."),
        ("The medicinal fruits ___ useful for skin irritation.", "are", "is", "am", "be", "A", "Plural 'medicinal fruits' takes 'are'."),
        ("I ___ proud of our national tree.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The canopy ___ dense and protective.", "is", "are", "am", "be", "A", "Singular 'canopy' takes 'is'."),
        ("The roots ___ reaching deep into the earth.", "are", "is", "am", "be", "A", "Plural 'roots' takes 'are'.")
    ]
    
    for idx, (sent_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_hv, start=1):
        qid = f"BK02_CH10_CAT09_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct helping verb (is / am / are):\n\n\"{sent_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Helping Verb Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Choose the correct helping verb: 'The banyan tree and the neem tree ____ both useful in Ayurveda.'", "are", "is", "am", "be", "A", "Compound subject ('The banyan tree and the neem tree') is plural, taking 'are'."),
        ("Select the sentence with CORRECT helping verb agreement:", "The Banyan Tree is the national tree of India.", "The Banyan Tree are the national tree of India.", "The Banyan Tree am the national tree of India.", "The Banyan Tree be the national tree of India.", "A", "Singular noun 'The Banyan Tree' requires 'is'."),
        ("Fill in the blanks: 'I ____ drawing a banyan tree, and my friends ____ gathering leaves.'", "am, are", "is, are", "are, is", "am, is", "A", "'I am', 'friends are'."),
        ("Identify the mistake in: 'The aerial roots on the banyan tree **is** long.'", "'is' should be 'are' because 'roots' is a plural noun.", "'is' should be 'am'", "'is' should be 'was'", "No mistake", "A", "'roots' is plural, requiring 'are'."),
        ("Which helping verb completes the question? '____ you aware of the banyan tree's medicinal uses?'", "Are", "Is", "Am", "Be", "A", "Subject 'you' takes 'Are'."),
        ("Fill in the blank: 'Neither cold nor heat ____ harming the ancient banyan tree.'", "is", "are", "am", "be", "A", "'Neither...nor' with singular second subject 'heat' takes 'is'."),
        ("Select the correct sentence for story moral:", "Trees and forests are vital for our survival.", "Trees and forests is vital for our survival.", "Trees and forests am vital for our survival.", "Trees and forests be vital for our survival.", "A", "Compound subject 'Trees and forests' takes 'are'."),
        ("Complete the conversation: Student: 'Where ____ the banyan fruit?' Teacher: 'It ____ on the high branch!'", "is, is", "are, are", "is, are", "are, is", "A", "Singular 'the banyan fruit' -> is; singular 'It' -> is."),
        ("Identify where 'is' is used incorrectly:", "The roots **is** descending.", "The tree is tall.", "India is vast.", "The paper is smooth.", "A", "'The roots is' should be 'The roots are'."),
        ("Choose the correct helping verb for collective noun used as a single unit: 'The flock of birds ____ resting in the banyan tree.'", "is", "are", "am", "be", "A", "Collective noun 'flock' treated as singular unit takes 'is'."),
        ("Fill in the blank: 'The fruit of the banyan tree ____ harvested for Ayurvedic medicine.'", "is", "are", "am", "be", "A", "Singular 'fruit' takes 'is'."),
        ("Select the sentence with correct helping verb for 'I':", "I am studying the banyan tree's lifecycle.", "I is studying the banyan tree's lifecycle.", "I are studying the banyan tree's lifecycle.", "I be studying the banyan tree's lifecycle.", "A", "Subject 'I' takes 'am'."),
        ("Fill in the blank: 'There ____ many banyan trees in Indian villages.'", "are", "is", "am", "be", "A", "'There are' before plural noun 'many banyan trees'."),
        ("Fill in the blank: 'There ____ a massive banyan tree in the center of the park.'", "is", "are", "am", "be", "A", "'There is' before singular noun 'a massive banyan tree'."),
        ("Choose the correct sentence:", "What are the birds doing in the banyan tree?", "What is the birds doing in the banyan tree?", "What am the birds doing in the banyan tree?", "What be the birds doing in the banyan tree?", "A", "Plural subject 'the birds' takes 'are'."),
        ("Identify the correct form: 'The banyan tree, as well as its roots, ____ admired by visitors.'", "is", "are", "am", "be", "A", "Subject is singular 'The banyan tree' ('as well as...' does not change subject number), taking 'is'."),
        ("Fill in the blank: 'Both Hinduism and Buddhism ____ considering the banyan tree sacred.'", "are", "is", "am", "be", "A", "'Both ... and ...' takes plural verb 'are'."),
        ("Select the option with correct helping verbs: 'The tree ____ huge, but its fruits ____ small.'", "is, are", "are, is", "am, are", "is, is", "A", "'tree is', 'fruits are'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH10_CAT09_Q{idx:02d}"
        qtxt = f"Helping Verb Subject-Verb Agreement Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Subject-Verb Agreement Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze subject-verb agreement: 'Each of the banyan tree's branches **____** growing aerial roots.' Choose the correct verb and reason:", "is — because 'Each' is a singular indefinite pronoun requiring singular verb 'is'.", "are — because 'branches' is plural.", "am — because it refers to speaker.", "be — because roots are long.", "A", "'Each' is singular indefinite pronoun taking singular verb 'is'."),
        ("Spot the subtle agreement error in: 'A cluster of aerial roots **are** reaching the ground.'", "'are' should be 'is' because the subject is singular noun 'cluster'.", "'are' should be 'am'.", "'roots' should be 'root'.", "No error.", "A", "'A cluster' is singular, so it requires 'is reaching'."),
        ("Compare: (1) 'The banyan tree and the peepal tree **are** sacred.' vs (2) 'The banyan tree, along with the peepal tree, **is** sacred.' Why are the verbs different?", "In (1), 'and' creates a plural subject (are); in (2), 'along with' is a prepositional phrase, leaving 'The banyan tree' as sole singular subject (is).", "They mean different things.", "Sentence (2) is grammatically wrong.", "Both should use 'are'.", "A", "Prepositional phrases like 'along with' do not change subject number."),
        ("Identify the correct agreement for indefinite pronouns: 'Everyone in the village **____** gathering under the banyan tree.'", "is", "are", "am", "be", "A", "'Everyone' is a singular indefinite pronoun requiring 'is'."),
        ("Spot all THREE subject-verb errors in: 'The roots **is** long, I **is** watching, and the leaves **is** green.'", "'roots is' -> 'roots are'; 'I is' -> 'I am'; 'leaves is' -> 'leaves are'", "'roots is' -> 'roots am'; 'I is' -> 'I are'; 'leaves is' -> 'leaves am'", "Only 'I is' is wrong.", "No errors present.", "A", "roots are (plural), I am (1st person), leaves are (plural)."),
        ("Fill in the blanks in this complex sentence: 'Not only the trunk but also the roots **____** descending, while the child **____** playing.'", "are, is", "is, are", "is, is", "are, are", "A", "'Not only...but also' agrees with closer plural subject ('roots' -> are); 'child' -> is."),
        ("Transform to negative: 'The Banyan Tree is the national tree of India.'", "The Banyan Tree **is not** the national tree of India.", "The Banyan Tree are not the national tree of India.", "The Banyan Tree am not the national tree of India.", "The Banyan Tree not national tree.", "A", "Add 'not' after singular helping verb 'is'."),
        ("Analyze inverted subject position: 'Under the spreading branches **____** resting several travelers.'", "are", "is", "am", "be", "A", "Subject is plural 'several travelers', appearing after verb, requiring 'are'."),
        ("Determine agreement with uncountable nouns: 'The wood of the banyan tree **____** used to make paper.'", "is", "are", "am", "be", "A", "Uncountable noun 'wood' is treated as singular, taking 'is'."),
        ("Correct the sentence: 'Here **is** the banyan fruits you asked for.'", "Here **are** the banyan fruits you asked for.", "Here am the banyan fruits you asked for.", "Here be the banyan fruits you asked for.", "No error.", "A", "Plural subject 'banyan fruits' requires 'Here are...''"),
        ("Identify the sentence where 'is' acts as a MAIN linking verb rather than a helping verb:", "The Banyan Tree **is** the national tree of India.", "The banyan tree **is** expanding across the field.", "The botanist **is** measuring the roots.", "The paper **is** coming from wood.", "A", "In 'The Banyan Tree is the national tree of India', 'is' is the main linking verb connecting subject to predicate noun."),
        ("HOTS Reasoning: Why does English use 'am' ONLY with the subject pronoun 'I'?", "Because 'am' is the unique 1st person singular present indicative form of the verb 'to be'.", "Because 'I' is capitalized.", "Because banyan is a tree.", "There is no reason.", "A", "'am' is exclusively reserved for 1st person singular 'I'."),
        ("Fill in the blanks: 'Neither inflammation nor skin irritation **____** untreated, because banyan fruit **____** effective.'", "is, is", "are, is", "is, are", "are, are", "A", "'skin irritation' is singular closer subject -> is; 'banyan fruit' -> is."),
        ("Select the option with PERFECT helping verb agreement throughout:", "The Banyan Tree is huge, I am sitting under it, and its roots are long.", "The Banyan Tree are huge, I is sitting under it, and its roots is long.", "The Banyan Tree am huge, I are sitting under it, and its roots am long.", "The Banyan Tree is huge, I is sitting under it, and its roots is long.", "A", "The Banyan Tree is (singular), I am (1st person), roots are (plural).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH10_CAT09_Q{idx:02d}"
        qtxt = f"Higher Order Helping Verb Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Subject-Verb Agreement & Syntax", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# MAIN EXECUTION FOR REBUILDING CHAPTER 10
# ---------------------------------------------------------------------------
def rebuild_chapter_10():
    print("Rebuilding Chapter 10 category files with high-quality, multi-tiered (Easy/Medium/Hard) non-duplicate questions...")

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
        filepath = os.path.join(CH10_DIR, fname)
        print(f"  Generating {fname}...")
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {fname} created successfully.")

    print("\n[SUCCESS] Completed rebuilding all 9 category files for Chapter 10 (450 total high-quality questions)!")

if __name__ == "__main__":
    rebuild_chapter_10()
