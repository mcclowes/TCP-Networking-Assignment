import pickle

# Save a dictionary into a pickle file.

moviedb = [['Moneyball', 'www.moneyball.com', 'Not a movie about the lottery, surprisingly'],\
           ['Casino', 'www.casino.com', 'Bit of a gamble really'],\
           ['Avatar','www.avatar.com','Smurfs + Pocahantas'],\
           ['The Hobbit','www.thehobbit.com','Dragons and dwarves'],\
           ['Rush','www.rush.co.uk','Fast cars, fast lives'],\
           ['Taken','www.taken.org','Are you Taken the piss'],\
           ['Spirited Away','www.spiritedaway.jp','That music'],\
           ['Bridge over the River Kawaiiii','www.bridge.com','A documentary about bridge making'],\
           ['Benjamin Button','www.bb.com','A film charting Brad Pitts plastic surgery'],\
           ['Noddy','www.noddy.com','Racist'],\
           ['Lock Stock and Two Smoking Barrels','www.lsatsb.com','Guv'],\
           ['Drive','www.drivefast.com','Maurice Drive has gotta go fast!'],\
           ['The Room','www.tommywiseau.com','Oh hai Mark'],\
           ['Month Python and the Holy Grail','www.monty.co.uk','Python']]

pickle.dump( moviedb, open( "moviedb.p", "wb" ) )

serverdb = [['localhost',11000],['localhost',11001],['localhost',11002]]

pickle.dump( serverdb, open( "serverdb.p", "wb" ) )

portdb = [['localhost',11000],['localhost',11001],['localhost',11002],['localhost',11003],['localhost',11004],['localhost',12000],['locahost',12001]]

pickle.dump( portdb, open( "portdb.p", "wb" ) )
