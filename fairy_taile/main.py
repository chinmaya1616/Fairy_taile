def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input


noun1 = get_input("charcter name (boy)")
noun2 = get_input("character name (girl)")

story = f"""

**Once upon a time**, in a prosperous kingdom, there lived a wise and noble king named {noun1} and his beautiful queen, {noun2}. They ruled their land with kindness and justice, and the people adored them.

{noun1} was known for his bravery and strategic mind, while {noun2} was celebrated for her wisdom and compassion. Together, they made a formidable pair, bringing peace and prosperity to their kingdom. However, as the years passed, their harmonious relationship began to face challenges.

One day, as they sat in the royal garden, an argument erupted between them.

"We must allocate more resources to fortify our army," {noun1} declared. "Our neighboring kingdoms are growing stronger, and we need to be prepared for any threat."

{noun2} shook her head, her voice calm but firm. "Our people need better schools and hospitals, {noun1}. If we invest in their education and health, our kingdom will be stronger from within."

Their disagreement grew, with neither willing to compromise. Days turned into weeks, and the palace, once filled with laughter and love, now echoed with their arguments.

"Why can't you see the importance of security?" {noun1} demanded during one particularly heated debate. "Without a strong defense, everything else is meaningless!"

"And why can't you understand that our people's well-being is paramount?" {noun2} retorted. "A strong, educated, and healthy populace is the foundation of any great kingdom!"

Their once unbreakable bond was now strained, and the royal court began to feel the tension. The kingdom, too, felt the impact of their discord, as the people became divided in their loyalties.

Finally, after many sleepless nights and countless arguments, {noun1} and {noun2} made a painful decision.

"We can't go on like this," {noun1} said quietly, his voice heavy with sorrow. "Our differences are too great."

{noun2} nodded, tears glistening in her eyes. "For the sake of the kingdom and ourselves, it is best that we part ways."

With heavy hearts, they announced their decision to divorce. The kingdom mourned the end of an era, as their beloved king and queen went their separate ways.

Though their love story did not have the fairy tale ending many had hoped for, {noun1} and {noun2} each found peace and fulfillment in their new lives. They continued to rule the kingdom, but from different palaces, and over time, the realm regained its balance.

**The end.**
"""
print(story)