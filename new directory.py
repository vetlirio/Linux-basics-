Directories

As we mentioned before, a directory is just a location in a filesystem that can contain files and other directories. On some systems, directories are called "folders", but it's the same thing.
The mkdir Command

The "make directory" command creates a new directory inside the current directory.

mkdir my_directory

Assignment

During your digging, you find that a file appears to be out of place!

    Make sure you're in the worldbanc/public/products/credit_cards directory
    Run ls from there. You should see a file called tbills.txt. Treasury Bills (T-Bills) are a type of investment, not a credit card!
    Go back to the products directory and create a new directory called "investments".
    List the contents of the products directory again to confirm that the new directory was created.

Paste the contents of the products directory into the input field and submit it.

codemaster@Money:/$ cd worldbanc/public/products/credit_cards
-bash: cd: worldbanc/public/products/credit_cards: No such file or directory
codemaster@Money:/$ cd /home/codemaster/worldbanc/public/products/credit_cards
codemaster@Money:~/worldbanc/public/products/credit_cards$ ls
credithistory.txt  creditplus.txt  economypoints.txt  freedomunited.txt  jointrewardsplux.txt  tbills.txt  travelrewards.txt  worldbanccard.txt
codemaster@Money:~/worldbanc/public/products/credit_cards$ cd ..
codemaster@Money:~/worldbanc/public/products$ mkdir investments
codemaster@Money:~/worldbanc/public/products$ ls
accounts  cds  credit_cards  investments  loans
codemaster@Money:~/worldbanc/public/products$
