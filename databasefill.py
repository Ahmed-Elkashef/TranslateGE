from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Word, Base

engine = create_engine('sqlite:///words.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# German Words
Katze = Word(word='katze', short_description="What's another name for the four-legged feline that"
+" lies around on your keyboard all day and purrs? You might call it 'Fluffy,' but it's also known"
+" as a cat.", long_description="If you're in the market for a pet cat, just make sure it meows, "
+"and doesn't roar like the lion, tiger, or jaguar, all of which are in the same family as the"
+" housecat. Domesticated as long ago as ancient Egyptian times, the cat is a fixture not only in"
+" many homes, but also in a host of English expressions - like, 'when the cat's away, the mice"
+" will play,' 'it's raining cats and dogs,' and 'the cat's pajamas.'")
session.add(Katze)
session.commit()

print("added words!")
