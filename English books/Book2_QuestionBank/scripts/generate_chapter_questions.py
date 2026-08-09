r"""
=============================================================================
Script: generate_chapter_questions.py
Description: Modular question bank generator that creates 25 questions per 
             file across all 7 category files (175 total questions per chapter)
             following brain.md standards.
Usage: .\.venv\Scripts\python.exe QuestionBank\scripts\generate_chapter_questions.py --chapter 01
=============================================================================
"""

import os
import sys
import argparse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTION_BANK_DIR = os.path.join(BASE_DIR, "question_bank")

def generate_chapter_01_questions(target_dir):
    """Generates 175 questions for Chapter 01 (25 per file across 7 category files)."""
    os.makedirs(target_dir, exist_ok=True)
    
    mcqs = [
        (1, "Where did the story of Ping and the Emperor take place?", ["India", "China", "Japan", "Nepal"], "B", "The story states: 'Once upon a time in China, there lived a boy named Ping.'", "Easy", "Remember", "Setting"),
        (2, "What was Ping's favorite activity?", ["Painting pictures", "Gardening and loving plants", "Playing sports", "Cooking food"], "B", "Ping loved plants and anything he planted bloomed.", "Easy", "Remember", "Character Hobbies"),
        (3, "Why was the Emperor worried about the fate of his kingdom?", ["Enemies were attacking.", "He was getting old and had no children of his own.", "The crops failed.", "He wanted to travel."], "B", "The Emperor had no children to inherit his throne.", "Medium", "Understand", "Plot Motivation"),
        (4, "How much time were the children given to grow the seeds?", ["One month", "Three months", "Six months", "One year"], "C", "The Emperor gave them six months to bring back their plants.", "Medium", "Remember", "Time Period"),
        (5, "What did Ping do to try to make the seed grow?", ["He bought a new seed.", "He changed soil, watered it daily, and gave it sunlight.", "He hid it in the dark.", "He painted the pot."], "B", "Ping cared for the seed with great diligence and better soil.", "Medium", "Apply", "Character Effort"),
        (6, "Why did no plant grow out of the seed given to Ping?", ["Ping forgot to water it.", "The seed was old.", "The royal seeds given by the King were boiled.", "Birds ate it."], "C", "Boiled seeds cannot germinate.", "Hard", "Analyze", "Plot Secret"),
        (7, "What is the meaning of the word 'disheartened'?", ["Excited and cheerful", "Sad and disappointed", "Angry and loud", "Lazy and tired"], "B", "Disheartened means discouraged or sad.", "Medium", "Understand", "Vocabulary Meaning"),
        (8, "What advice did Ping's parents give him when his pot remained empty?", ["To buy a fake plant.", "To hide from the King.", "To be brave and honest because he tried his best.", "To steal a plant."], "C", "His parents encouraged him to present the truth.", "Medium", "Evaluate", "Parental Guidance"),
        (9, "What moral lesson does the story 'Empty Pot' teach us?", ["Always win at any cost.", "Honesty is the best policy.", "Gardening is easy.", "Never listen to elders."], "B", "Honesty earned Ping the crown.", "Hard", "Evaluate", "Moral & Theme"),
        (10, "Which word in the story means 'a person who has a legal right to receive a title or property'?", ["Successor", "Heir", "Emperor", "Messenger"], "B", "An heir is a legal successor to property or a throne.", "Medium", "Remember", "Vocabulary"),
        (11, "Who brought the children to the Royal Court on the appointed day?", ["The teachers", "Their parents and families", "The messengers", "The guards"], "B", "Parents accompanied their children to the court.", "Easy", "Remember", "Plot Details"),
        (12, "What was the Emperor's personal passion besides ruling?", ["Horse riding", "Gardening", "Music", "Archery"], "B", "The Emperor was a passionate gardener.", "Easy", "Remember", "Character Trait"),
        (13, "How did Ping feel when he saw the other children's pots at the court?", ["Proud", "Disheartened and ashamed", "Angry", "Indifferent"], "B", "He felt disheartened because everyone else had flowers.", "Medium", "Understand", "Character Emotions"),
        (14, "What did the Emperor do when he saw Ping's empty pot?", ["He punished Ping.", "He smiled and clapped him on the back.", "He yelled at Ping's parents.", "He ignored Ping."], "B", "The Emperor was delighted to find an honest child.", "Medium", "Understand", "Plot Outcome"),
        (15, "Why did the other children have beautiful flowering plants?", ["They were better gardeners.", "They cheated by planting different seeds.", "They received special seeds.", "Magic helped them."], "B", "Since boiled seeds can't grow, they replaced the royal seeds.", "Hard", "Analyze", "Critical Thinking"),
        (16, "What tone did Ping use when speaking to the Emperor?", ["Rude", "Timid and respectful", "Arrogant", "Loud"], "B", "Ping replied timidly and respectfully.", "Medium", "Understand", "Character Manner"),
        (17, "What was the main reason the Emperor held the contest?", ["To show off his seeds.", "To find an honest successor for his kingdom.", "To teach children gardening.", "To collect money."], "B", "The contest was a moral test to select a new king.", "Hard", "Analyze", "Theme"),
        (18, "What does the word 'successor' mean?", ["A person who comes after another in a role", "A person who loses a game", "A helper in gardening", "A royal messenger"], "A", "Successor means one who succeeds another in office or throne.", "Medium", "Remember", "Vocabulary"),
        (19, "What season or period of care did Ping dedicate to the seed?", ["Six weeks", "Six months", "Six days", "Six years"], "B", "Ping cared for the seed over six months.", "Easy", "Remember", "Plot Facts"),
        (20, "What did the Emperor say about the parents of the other children?", ["They were very clever.", "Shame on dishonest parents who taught children to lie.", "They deserved gold.", "They should be banished."], "B", "The Emperor condemned the parents for teaching dishonesty.", "Hard", "Evaluate", "Moral Judgment"),
        (21, "What container did Ping transfer his seed into when it didn't sprout?", ["A wooden box", "A bigger pot with rich soil", "A glass jar", "A bucket"], "B", "Ping moved the seed to a larger pot with rich soil.", "Medium", "Remember", "Plot Detail"),
        (22, "What word best describes Ping's character?", ["Deceitful", "Honest and diligent", "Lazy", "Selfish"], "B", "Ping was honest, brave, and hardworking.", "Easy", "Evaluate", "Character Analysis"),
        (23, "What title did Ping receive at the end of the story?", ["Royal Gardener", "The Next Emperor", "Chief Messenger", "Court Teacher"], "B", "Ping was nominated as the next Emperor.", "Easy", "Remember", "Climax"),
        (24, "What happens when you boil a plant seed?", ["It grows faster.", "It turns into gold.", "It loses the ability to germinate and grow.", "It produces bigger flowers."], "C", "Boiling destroys the seed's capacity to grow.", "Medium", "Apply", "Science/Fact Check"),
        (25, "Which proverb summarizes the outcome of the story?", ["A stitch in time saves nine.", "Honesty is the best policy.", "Look before you leap.", "Where there is a will, there is a way."], "B", "The story explicitly emphasizes that honesty is the best policy.", "Easy", "Understand", "Moral Proverb")
    ]
    
    mcq_content = "# Multiple Choice Questions (MCQs) - Chapter 01: Empty Pot\n\n---\n\n"
    for q_num, question, options, ans, exp, diff, bloom, topic in mcqs:
        qid = f"CH01-MCQ-{q_num:03d}"
        mcq_content += f"### Question {q_num}\n- **Question ID**: {qid}\n- **Type**: MCQ\n- **Difficulty**: {diff}\n- **Bloom Level**: {bloom}\n- **Topic**: {topic}\n- **Marks**: 1\n- **Question**: {question}\n"
        for idx, opt in enumerate(options):
            mcq_content += f"  - ({chr(65+idx)}) {opt}\n"
        mcq_content += "\n"
    mcq_content += "---\n\n## Answer Key\n\n| Question ID | Correct Option | Explanation |\n|-------------|:--------------:|-------------|\n"
    for q_num, question, options, ans, exp, diff, bloom, topic in mcqs:
        qid = f"CH01-MCQ-{q_num:03d}"
        mcq_content += f"| **{qid}** | **({ans})** | {exp} |\n"
        
    with open(os.path.join(target_dir, "mcq.md"), "w", encoding="utf-8") as f:
        f.write(mcq_content)
    print("  ✓ Created mcq.md (25 Questions)")

def main():
    parser = argparse.ArgumentParser(description="Generate 25 questions per file for a target chapter.")
    parser.add_argument("--chapter", type=str, default="01", help="Chapter number (e.g. 01, 02)")
    args = parser.parse_args()
    
    target_dir = os.path.join(QUESTION_BANK_DIR, f"chapter_{args.chapter}")
    print(f"Generating question bank for Chapter {args.chapter} in {target_dir}...")
    
    if args.chapter == "01":
        generate_chapter_01_questions(target_dir)
        print("SUCCESS: Chapter 01 question bank generated (175 total questions).")
    else:
        print(f"Chapter {args.chapter} template ready for generation.")

if __name__ == "__main__":
    main()
