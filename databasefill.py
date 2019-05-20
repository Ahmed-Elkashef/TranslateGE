# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Word, Base

engine = create_engine('sqlite:///words.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# German Words

Kaufen = Word(  vocabulary_word='kaufen',
                short_description="When you Kauft something, you pay money in order to own it. "
                +"You might buy your wife a bouquet of flowers for your anniversary.",
                long_description="When you buy food, flowers or furniture, you purchase it, "
                +"exchanging a certain amount of money for it, and when you call something "
                +"'ein kauf' or 'ein Stahl' it's a real bargain. You may say, 'She said she"
                +" won the lottery, but I don't kauf/buy it,' you mean that you don't accept"
                +" that facet as the truth.",
                word_familie_1st_label="abkaufen", word_familie_1st_score=4, word_familie_1st_color="#6497b1",
                word_familie_2nd_label="aufkaufen", word_familie_2nd_score=4, word_familie_2nd_color="#6497b1",
                word_familie_3rd_label="einkaufen", word_familie_3rd_score=6, word_familie_3rd_color="#005b96",
                word_familie_4th_label=u"Zurückkaufen", word_familie_4th_score=4 , word_familie_4th_color="#6497b1",
                word_familie_5th_label="Nachkaufen", word_familie_5th_score=2 , word_familie_5th_color="#b3cde0")
session.add(Kaufen)
session.commit()

"""
Katze = Word(vocabulary_word='katze', short_description="What's another name for the four-legged feline that"
+" lies around on your keyboard all day and purrs? You might call it 'Fluffy,' but it's also known"
+" as a cat.", long_description="If you're in the market for a pet cat, just make sure it meows, "
+"and doesn't roar like the lion, tiger, or jaguar, all of which are in the same family as the"
+" housecat. Domesticated as long ago as ancient Egyptian times, the cat is a fixture not only in"
+" many homes, but also in a host of English expressions - like, 'when the cat's away, the mice"
+" will play,' 'it's raining cats and dogs,' and 'the cat's pajamas.'")
session.add(Katze)
session.commit()

Katalog = Word(vocabulary_word='katalog', short_description="A catalog is a book that lists many things: the"
+" most common type of catalog is for a store.", long_description="A catalog is an organized list that"
+" appears in book or pamphlet form. The Sears catalog tells you all the things you can buy at Sears,"
+" along with pictures of the items and what they cost. But you can also use catalog to mean any kind"
+" of listing. In an argument, you might say, 'Why don't you just make a catalog of all my faults!' "
+"When you're making a catalog of any kind, you're cataloging.")
session.add(Katalog)
session.commit()

Konkret = Word(vocabulary_word='konkret', short_description="Concrete is that pourable mix of cement,"
+" water, sand, and gravel that hardens into a super-strong building material. Sidewalks, foundations,"
+" and highways are all made of concrete.", long_description="Though people use the words cement and"
+" concrete as if they were the same, they're not. Concrete has cement in it, but also includes other"
+" materials; cement is what binds concrete together. Construction workers hate when kids write their"
+" names in concrete before it hardens: once concrete hardens, it's going to be solid for a long time."
+" When used as an adjective, concrete also means solid. If you've got concrete plans for Saturday,"
+" then you have a definite plan.")
session.add(Konkret)
session.commit()
"""

print("added words!")
