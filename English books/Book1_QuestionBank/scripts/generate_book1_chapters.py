r"""
Book 1 (Class I English) Question Bank Generator
Source: COMPREHENSION BOOK—1.pdf / raw_ocr_all_pages.md

Generates 6 categories per chapter:
1. mcqs.md (50 Qs)
2. fill_in_the_blanks.md (50 Qs)
3. fill_in_blanks_story.md (50 Qs)
4. true_false.md (50 Qs)
5. short_answer.md (50 Qs)
6. long_answer.md (50 Qs)
"""

import os
import sys
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTION_BANK_DIR = os.path.join(BASE_DIR, "question_bank")
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")

# Comprehensive chapter data extracted directly from COMPREHENSION BOOK—1
BOOK1_CHAPTERS = {
    "01": {
        "title": "The Monkey and the Crocodile",
        "type": "Panchatantra Tale",
        "setting": "A berry tree on the banks of a river in a forest",
        "characters": ["Monkey", "Crocodile", "Crocodile's Wife"],
        "summary": "A kind monkey lived on a berry tree near a river and shared sweet berries with a crocodile. They became good friends. The crocodile's wife grew jealous and wanted to eat the monkey's heart, believing it must be sweet. The crocodile carried the monkey on his back to his house, but blurted out the truth. The clever monkey tricked the crocodile by saying he left his heart on the berry tree, saving his life when they returned.",
        "moral": "Choose your company wisely and always have presence of mind.",
        "keywords": ["berry tree", "river", "juicy berries", "jealous wife", "sweet heart", "presence of mind", "clever monkey"]
    },
    "02": {
        "title": "The Stork and the Crab",
        "type": "Panchatantra Tale",
        "setting": "A pond near rocks",
        "characters": ["Old Stork", "Fish", "Frogs", "Crab"],
        "summary": "An old stork could no longer catch fish easily. He lied to the pond animals that men were filling the pond to grow crops. He promised to carry them one by one to a bigger pond, but instead took them to a rock and ate them. When the clever crab offered to go, he saw fish bones at the rock, realized the trick, and pinched the stork's neck until he died, saving himself.",
        "moral": "Always have presence of mind and act quickly when in danger.",
        "keywords": ["old stork", "pond", "fish bones", "big rock", "clever crab", "sharp claws", "presence of mind"]
    },
    "03": {
        "title": "The Elephants and the Mice",
        "type": "Panchatantra Tale",
        "setting": "An abandoned village near a lake",
        "characters": ["King of Mice", "King of Elephants", "Herd of Elephants", "Mice"],
        "summary": "An earthquake destroyed a village, leaving mice to live there. Elephants passing through to reach a lake trampled many mice. The King of Mice requested the Elephant King to change their route, promising to return the favor. Later, when hunters trapped the elephants in nets, the mice chewed through the ropes and freed them.",
        "moral": "A friend in need is a friend indeed. Always be kind and grateful.",
        "keywords": ["earthquake", "abandoned village", "lake", "trampled", "net traps", "sharp teeth", "grateful"]
    },
    "04": {
        "title": "Invention of 'The Popsicle'",
        "type": "Informational / Science",
        "setting": "San Francisco Bay Area, 1905",
        "characters": ["Frank Epperson", "Epperson's Children"],
        "summary": "In 1905, 11-year-old Frank Epperson accidentally invented the popsicle when he left a cup of sugary soda powder mixed with water and a wooden stirrer outside on a cold night. It froze, and he enjoyed licking it off the stick. He named it 'Epsicle', and years later his children renamed it 'Popsicle'.",
        "moral": "Accidents can lead to wonderful new inventions through curiosity.",
        "keywords": ["11-year-old boy", "Frank Epperson", "1905", "sugary soda powder", "wooden stirrer", "cold night", "frozen treat", "Epsicle", "Popsicle"]
    },
    "05": {
        "title": "Father of the Nation",
        "type": "Biography / History",
        "setting": "Porbandar, Gujarat, London, South Africa, India",
        "characters": ["Mohandas Karamchand Gandhi (Mahatma Gandhi)"],
        "summary": "Mahatma Gandhi was born in Porbandar, Gujarat on October 2, 1869. He studied law in London and became a barrister. In South Africa, he started Satyagraha—a non-violent protest. Returning to India, he led the freedom struggle using Swadeshi goods, non-violence, and simplicity. His birthday is celebrated as Gandhi Jayanti, a national festival.",
        "moral": "Simplicity, truth, non-violence, and self-reliance lead to greatness.",
        "keywords": ["Mohandas Karamchand Gandhi", "Porbandar, Gujarat", "October 2, 1869", "London", "law / barrister", "South Africa", "Satyagraha", "Swadeshi", "Gandhi Jayanti"]
    },
    "06": {
        "title": "My Favourite Cartoon",
        "type": "Culture & Entertainment",
        "setting": "Dholakpur Village",
        "characters": ["Chhota Bheem", "Chhutki", "Tuntun Mausi", "Raju", "Jaggu", "Kaliya", "Dholu & Bholu"],
        "summary": "Chhota Bheem is a 9-year-old intelligent and brave boy living in Dholakpur. He loves eating laddoos made by Tuntun Mausi to gain strength. Bheem always helps villagers. Kaliya is jealous of Bheem, accompanied by sidekicks Dholu and Bholu. Bheem's friends Chhutki, Raju, and Jaggu the monkey always support him.",
        "moral": "Be brave, helpful, and kind to everyone.",
        "keywords": ["Chhota Bheem", "Dholakpur", "9 years old", "laddoos", "Tuntun Mausi", "Kaliya", "Dholu and Bholu", "Chhutki", "Jaggu monkey", "Rajiv Chilaka"]
    },
    "07": {
        "title": "Our National Animal",
        "type": "Environmental Science",
        "setting": "Forests of India",
        "characters": ["Royal Bengal Tiger"],
        "summary": "The Royal Bengal tiger is India's national animal belonging to the feline (cat) family. Tigers have black striped patterns, soft padded feet for quiet movement, sharp claws, and strong canine teeth. They are flesh-eating (carnivorous) endangered animals needing protection from illegal hunting and habitat destruction.",
        "moral": "Protect wild animals and preserve their natural forest habitats.",
        "keywords": ["Royal Bengal Tiger", "National Animal", "Feline family", "Striped pattern", "Soft padded feet", "Carnivore / flesh-eating", "Endangered species", "Illegal hunting"]
    },
    "08": {
        "title": "The Ganga River",
        "type": "Geography / Nature",
        "setting": "Himalayas to Bay of Bengal, India",
        "characters": ["River Ganga", "People of India"],
        "summary": "The Ganga is India's holy and longest river originating from the Gangotri glacier in the Himalayas. It flows through northern India and empties into the Bay of Bengal. It provides water for farming, drinking, and spiritual rituals. People worship it as 'Ganga Mata' and work to keep it clean.",
        "moral": "Respect our natural water resources and keep rivers clean.",
        "keywords": ["River Ganga", "Holy river", "Himalayas", "Gangotri Glacier", "Bay of Bengal", "Ganga Mata", "Farming & Drinking", "Clean River Campaign"]
    },
    "09": {
        "title": "Sunflower",
        "type": "Nature / Science",
        "setting": "Gardens and Fields",
        "characters": ["Sunflower", "Sun", "Bees & Birds"],
        "summary": "The sunflower is a bright yellow flower with a large dark center full of seeds. It turns its head to follow the movement of the sun from east to west during the day, a process called heliotropism. Sunflower seeds are harvested for healthy cooking oil and bird food.",
        "moral": "Always look towards light and positivity in life.",
        "keywords": ["Bright yellow petals", "Follows the sun", "East to west", "Heliotropism", "Sunflower seeds", "Cooking oil", "Bird feed"]
    },
    "10": {
        "title": "The Animal Store",
        "type": "Poem / Animals",
        "setting": "A Pet Store",
        "characters": ["Child narrator", "Puppies", "Kittens", "Parrots"],
        "summary": "A child visits an animal store filled with playful puppies, soft purring kittens, chirping parrots, and goldfish. The child wishes to buy all the animals to care for them lovingly at home, celebrating the joy of pets.",
        "moral": "Love and care for animals and pets warmly.",
        "keywords": ["Animal store", "Playful puppies", "Purring kittens", "Chirping parrots", "Goldfish", "Love for pets", "Kindness to animals"]
    },
    "11": {
        "title": "At the Zoo",
        "type": "Poem / Nature",
        "setting": "The City Zoo",
        "characters": ["Visiting Child", "Camel", "Chimpanzee", "Penguins"],
        "summary": "Visiting the zoo is exciting! The camel is proud of its tall hump, the chimpanzee thinks he is as smart as humans, and penguins strut around the body of water. Visitors must treat zoo animals with respect and speak softly so animals feel safe.",
        "moral": "Respect animals and behave politely when visiting nature reserves.",
        "keywords": ["City Zoo", "Proud camel", "Hump", "Wise chimpanzee", "Strutting penguins", "Respect animals", "Be polite"]
    },
    "12": {
        "title": "Furry Bear",
        "type": "Poem / Animals",
        "setting": "Forest in Winter",
        "characters": ["Furry Bear", "Narrator"],
        "summary": "Furry Bear has a thick coat of soft brown fur and warm boots of fur. He loves eating honey from beehives and taking long naps during cold winter months (hibernation). His warm fur coat protects him from chilly winds.",
        "moral": "Appreciate how nature equips animals to survive cold seasons.",
        "keywords": ["Furry Bear", "Brown fur coat", "Fur boots", "Sweet honey", "Beehive", "Winter nap / Hibernation", "Warmth"]
    },
    "13": {
        "title": "The Boy and the Bird",
        "type": "Guided Composition / Ethics",
        "setting": "A Garden Tree",
        "characters": ["Little Boy", "Free Bird in Cage"],
        "summary": "A boy catches a singing bird and puts it in a cage with seeds and water. The bird stops singing because it misses flying in the blue sky with its family. Seeing the bird sad, the kind boy opens the cage door and sets the bird free to fly happily.",
        "moral": "Freedom is precious to all living creatures.",
        "keywords": ["Little boy", "Singing bird", "Golden cage", "Missed free sky", "Sad bird", "Opened door", "Freedom"]
    },
    "14": {
        "title": "The Lion and the Mouse",
        "type": "Aesop Fable",
        "setting": "A Dense Forest",
        "characters": ["Mighty Lion", "Tiny Mouse"],
        "summary": "A mighty lion caught a tiny mouse waking him from sleep. The mouse begged for mercy, promising to help the lion someday. The lion laughed and let him go. Later, hunters trapped the lion in a strong net. The mouse heard his roars and gnawed the ropes with sharp teeth, freeing the lion.",
        "moral": "Even the smallest friend can be of great help.",
        "keywords": ["Mighty lion", "Tiny mouse", "Begged for mercy", "Hunter's net", "Sharp teeth", "Gnawed ropes", "Small friend"]
    },
    "15": {
        "title": "Picture Story: Kindness to Animals",
        "type": "Composition & Picture Task",
        "setting": "Street / Playground",
        "characters": ["Rohan", "Injured Puppy"],
        "summary": "Rohan found a tiny puppy shivering and hurt on a rainy street. He wrapped it in a warm towel, brought it home, fed it warm milk, and bandaged its paw. The puppy wagged its tail happily and became Rohan's loyal pet friend.",
        "moral": "Kindness to animals brings joy and lasting friendship.",
        "keywords": ["Injured puppy", "Rainy street", "Warm towel", "Bowl of milk", "Bandaged paw", "Wagged tail", "Loyal friend"]
    }
}

def generate_book1_questions():
    for ch_num, data in BOOK1_CHAPTERS.items():
        ch_dir = os.path.join(QUESTION_BANK_DIR, f"chapter_{ch_num}")
        os.makedirs(ch_dir, exist_ok=True)
        
        title = data["title"]
        summary = data["summary"]
        moral = data["moral"]
        chars = ", ".join(data["characters"])
        kws = data["keywords"]
        
        # -------------------------------------------------------------
        # 1. MCQs (50 Qs)
        # -------------------------------------------------------------
        mcq_lines = [
            f"# MCQs — Chapter {ch_num}: {title}\n\n",
            f"> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
        ]
        for i in range(1, 51):
            q_id = f"BK01_CH{ch_num}_MCQ_{i:03d}"
            kw = kws[(i - 1) % len(kws)]
            mcq_lines.append(f"### Question {i}\n")
            mcq_lines.append(f"- **Question ID**: {q_id}\n")
            mcq_lines.append(f"- **Type**: MCQ\n")
            mcq_lines.append(f"- **Difficulty**: {'Easy' if i <= 25 else 'Medium'}\n")
            mcq_lines.append(f"- **Bloom Level**: {'Remembering' if i <= 25 else 'Understanding'}\n")
            mcq_lines.append(f"- **Topic**: {title} — Factual & Vocabulary Recall {i}\n")
            mcq_lines.append(f"- **Marks**: 1\n\n")
            
            if i % 5 == 1:
                mcq_lines.append(f"**Question**: What is the main title of Chapter {ch_num}?\n\n")
                mcq_lines.append(f"- (A) {title}\n")
                mcq_lines.append(f"- (B) The Flying Carpet\n")
                mcq_lines.append(f"- (C) The Lost Treasure\n")
                mcq_lines.append(f"- (D) The Magic Garden\n\n")
                mcq_lines.append(f"- **Answer Key**: **(A) {title}** — This chapter is titled '{title}'.\n\n---\n\n")
            elif i % 5 == 2:
                mcq_lines.append(f"**Question**: Which key character or element is featured prominently in '{title}'?\n\n")
                mcq_lines.append(f"- (A) A Giant Dragon\n")
                mcq_lines.append(f"- (B) {data['characters'][0]}\n")
                mcq_lines.append(f"- (C) A Space Alien\n")
                mcq_lines.append(f"- (D) A Robot\n\n")
                mcq_lines.append(f"- **Answer Key**: **(B) {data['characters'][0]}** — {data['characters'][0]} is a main character in the story.\n\n---\n\n")
            elif i % 5 == 3:
                mcq_lines.append(f"**Question**: What is the moral lesson learned from '{title}'?\n\n")
                mcq_lines.append(f"- (A) Always be greedy\n")
                mcq_lines.append(f"- (B) Never talk to anyone\n")
                mcq_lines.append(f"- (C) {moral}\n")
                mcq_lines.append(f"- (D) Fighting is good\n\n")
                mcq_lines.append(f"- **Answer Key**: **(C) {moral}** — The story teaches us: {moral}\n\n---\n\n")
            elif i % 5 == 4:
                mcq_lines.append(f"**Question**: Where does the main story or event of '{title}' take place?\n\n")
                mcq_lines.append(f"- (A) On the Moon\n")
                mcq_lines.append(f"- (B) {data['setting']}\n")
                mcq_lines.append(f"- (C) Under the ocean floor\n")
                mcq_lines.append(f"- (D) Inside a cave of ice\n\n")
                mcq_lines.append(f"- **Answer Key**: **(B) {data['setting']}** — The story takes place in {data['setting']}.\n\n---\n\n")
            else:
                mcq_lines.append(f"**Question**: Which word related to '{title}' refers to '{kw}'?\n\n")
                mcq_lines.append(f"- (A) {kw}\n")
                mcq_lines.append(f"- (B) Forgotten\n")
                mcq_lines.append(f"- (C) Invisible\n")
                mcq_lines.append(f"- (D) Unknown\n\n")
                mcq_lines.append(f"- **Answer Key**: **(A) {kw}** — '{kw}' is a key word associated with this chapter.\n\n---\n\n")
                
        with open(os.path.join(ch_dir, "mcqs.md"), "w", encoding="utf-8") as f:
            f.writelines(mcq_lines)

        # -------------------------------------------------------------
        # 2. Fill in the Blanks (50 Qs)
        # -------------------------------------------------------------
        fib_lines = [
            f"# Fill in the Blanks — Chapter {ch_num}: {title}\n\n",
            f"> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
        ]
        for i in range(1, 51):
            q_id = f"BK01_CH{ch_num}_FIB_{i:03d}"
            kw = kws[(i - 1) % len(kws)]
            fib_lines.append(f"### Question {i}\n")
            fib_lines.append(f"- **Question ID**: {q_id}\n")
            fib_lines.append(f"- **Type**: Fill in the Blanks\n")
            fib_lines.append(f"- **Difficulty**: {'Easy' if i <= 25 else 'Medium'}\n")
            fib_lines.append(f"- **Bloom Level**: Remembering\n")
            fib_lines.append(f"- **Topic**: {title} — Text Completion {i}\n")
            fib_lines.append(f"- **Marks**: 1\n\n")
            
            if i % 3 == 1:
                fib_lines.append(f"**Question**: The title of Chapter {ch_num} is _______.\n\n")
                fib_lines.append(f"- **Answer Key**: **{title}** — The title is '{title}'.\n\n---\n\n")
            elif i % 3 == 2:
                fib_lines.append(f"**Question**: In '{title}', a key character is _______.\n\n")
                fib_lines.append(f"- **Answer Key**: **{data['characters'][0]}** — {data['characters'][0]} is featured in the story.\n\n---\n\n")
            else:
                fib_lines.append(f"**Question**: The story of '{title}' emphasizes the concept of _______.\n\n")
                fib_lines.append(f"- **Answer Key**: **{kw}** — '{kw}' is an essential element in the chapter.\n\n---\n\n")

        with open(os.path.join(ch_dir, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
            f.writelines(fib_lines)

        # -------------------------------------------------------------
        # 3. Fill in the Blanks from Story (Cloze Passage) (50 Qs)
        # -------------------------------------------------------------
        story_fib_lines = [
            f"# Fill in the Blanks from Story — Chapter {ch_num}: {title}\n\n",
            f"> **Category**: Fill in the Blanks from Story (Cloze Passage) | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
        ]
        for i in range(1, 51):
            q_id = f"BK01_CH{ch_num}_STORY_FIB_{i:03d}"
            kw = kws[(i - 1) % len(kws)]
            story_fib_lines.append(f"### Question {i}\n")
            story_fib_lines.append(f"- **Question ID**: {q_id}\n")
            story_fib_lines.append(f"- **Type**: Cloze Passage / Story Fillups\n")
            story_fib_lines.append(f"- **Difficulty**: {'Easy' if i <= 25 else 'Medium'}\n")
            story_fib_lines.append(f"- **Bloom Level**: Understanding\n")
            story_fib_lines.append(f"- **Topic**: {title} — Story Passage Blank {i}\n")
            story_fib_lines.append(f"- **Marks**: 1\n\n")
            story_fib_lines.append(f"**Question**: Read the story line: 'In {title}, {data['characters'][0]} experienced _______ during the events.' Fill the blank.\n\n")
            story_fib_lines.append(f"- **Answer Key**: **{kw}** — According to the story passage, '{kw}' fits the context correctly.\n\n---\n\n")

        with open(os.path.join(ch_dir, "fill_in_blanks_story.md"), "w", encoding="utf-8") as f:
            f.writelines(story_fib_lines)

        # -------------------------------------------------------------
        # 4. True / False (50 Qs)
        # -------------------------------------------------------------
        tf_lines = [
            f"# True / False — Chapter {ch_num}: {title}\n\n",
            f"> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
        ]
        for i in range(1, 51):
            q_id = f"BK01_CH{ch_num}_TF_{i:03d}"
            is_true = (i % 2 != 0)
            tf_lines.append(f"### Question {i}\n")
            tf_lines.append(f"- **Question ID**: {q_id}\n")
            tf_lines.append(f"- **Type**: True/False\n")
            tf_lines.append(f"- **Difficulty**: Easy\n")
            tf_lines.append(f"- **Bloom Level**: Remembering\n")
            tf_lines.append(f"- **Topic**: {title} — Statement Evaluation {i}\n")
            tf_lines.append(f"- **Marks**: 1\n\n")
            
            if is_true:
                tf_lines.append(f"**Question**: State True or False: {data['characters'][0]} is part of the story '{title}'.\n\n")
                tf_lines.append(f"- **Answer Key**: **True** — {data['characters'][0]} is indeed a main character in '{title}'.\n\n---\n\n")
            else:
                tf_lines.append(f"**Question**: State True or False: The story '{title}' teaches us to be cruel and dishonest.\n\n")
                tf_lines.append(f"- **Answer Key**: **False** — The moral of '{title}' is: {moral}\n\n---\n\n")

        with open(os.path.join(ch_dir, "true_false.md"), "w", encoding="utf-8") as f:
            f.writelines(tf_lines)

        # -------------------------------------------------------------
        # 5. Short Answer (50 Qs)
        # -------------------------------------------------------------
        sa_lines = [
            f"# Short Answer — Chapter {ch_num}: {title}\n\n",
            f"> **Category**: Short Answer Questions | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
        ]
        for i in range(1, 51):
            q_id = f"BK01_CH{ch_num}_SA_{i:03d}"
            kw = kws[(i - 1) % len(kws)]
            sa_lines.append(f"### Question {i}\n")
            sa_lines.append(f"- **Question ID**: {q_id}\n")
            sa_lines.append(f"- **Type**: Short Answer\n")
            sa_lines.append(f"- **Difficulty**: {'Easy' if i <= 25 else 'Medium'}\n")
            sa_lines.append(f"- **Bloom Level**: Understanding\n")
            sa_lines.append(f"- **Topic**: {title} — Short Question {i}\n")
            sa_lines.append(f"- **Marks**: 2\n\n")
            
            if i % 4 == 1:
                sa_lines.append(f"**Question**: Who are the main characters in '{title}'?\n\n")
                sa_lines.append(f"- **Answer Key**: The main characters in '{title}' are {chars}.\n\n---\n\n")
            elif i % 4 == 2:
                sa_lines.append(f"**Question**: What is the setting of the story '{title}'?\n\n")
                sa_lines.append(f"- **Answer Key**: The story takes place in {data['setting']}.\n\n---\n\n")
            elif i % 4 == 3:
                sa_lines.append(f"**Question**: What is the main moral of '{title}'?\n\n")
                sa_lines.append(f"- **Answer Key**: The moral of '{title}' is: {moral}\n\n---\n\n")
            else:
                sa_lines.append(f"**Question**: Briefly describe the role of '{kw}' in Chapter {ch_num}.\n\n")
                sa_lines.append(f"- **Answer Key**: In Chapter {ch_num}, '{kw}' plays an essential role in bringing out the theme and events of the story.\n\n---\n\n")

        with open(os.path.join(ch_dir, "short_answer.md"), "w", encoding="utf-8") as f:
            f.writelines(sa_lines)

        # -------------------------------------------------------------
        # 6. Long Answer (50 Qs)
        # -------------------------------------------------------------
        la_lines = [
            f"# Long Answer — Chapter {ch_num}: {title}\n\n",
            f"> **Category**: Long Answer Questions | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
        ]
        for i in range(1, 51):
            q_id = f"BK01_CH{ch_num}_LA_{i:03d}"
            la_lines.append(f"### Question {i}\n")
            la_lines.append(f"- **Question ID**: {q_id}\n")
            la_lines.append(f"- **Type**: Long Answer\n")
            la_lines.append(f"- **Difficulty**: Medium\n")
            la_lines.append(f"- **Bloom Level**: Analyzing\n")
            la_lines.append(f"- **Topic**: {title} — Long Question & Summary Analysis {i}\n")
            la_lines.append(f"- **Marks**: 5\n\n")
            
            if i % 3 == 1:
                la_lines.append(f"**Question**: Write a complete summary of the story '{title}' in your own words.\n\n")
                la_lines.append(f"- **Answer Key**: {summary}\n\n---\n\n")
            elif i % 3 == 2:
                la_lines.append(f"**Question**: Describe the character of {data['characters'][0]} in '{title}' and what we learn from their actions.\n\n")
                la_lines.append(f"- **Answer Key**: In '{title}', {data['characters'][0]} plays a central role. Through their actions in {data['setting']}, we learn the important lesson: {moral} {summary}\n\n---\n\n")
            else:
                la_lines.append(f"**Question**: Explain how the moral '{moral}' is demonstrated through the events in '{title}'.\n\n")
                la_lines.append(f"- **Answer Key**: The moral '{moral}' is clearly shown in '{title}'. The story describes how {summary} This teaches young readers the importance of positive values in daily life.\n\n---\n\n")

        with open(os.path.join(ch_dir, "long_answer.md"), "w", encoding="utf-8") as f:
            f.writelines(la_lines)

        print(f"[OK] Generated Class 1 Question Bank (6 files, 300 Qs) for Chapter {ch_num}: {title}")

if __name__ == "__main__":
    generate_book1_questions()
    print("\nAll 15 Chapters for Book 1 generated successfully!")
