Touch

The touch command updates the access and modification timestamps of a file. By default, if the specified file does not exist, touch will create an empty file with the given filename. Because of this side-effect, you’ll often see this command used to quickly create new empty files.

touch new_file.txt

You can also create multiple files at once by listing them:

touch some_file.txt some_other_file.txt

touch can be very handy when writing scripts because it ensures files exist without altering existing ones, creating new files only if necessary.
Assignment

You discovered a discrepancy with the credit card files. WorldBanc is supposed to be keeping credit history records, but they aren't there!

    Change into the worldbanc/public/products/credit_cards directory
    Create a new file named credithistory.txt so they can keep track of that information
    Use ls to verify that the file has been created successfully.

Paste the contents of the credit_cards directory into the text field and submit it.


codemaster@Money:~/worldbanc/public/products$ ls
accounts  cds  credit_cards  loans
codemaster@Money:~/worldbanc/public/products$ pwd
/home/codemaster/worldbanc/public/products
codemaster@Money:~/worldbanc/public/products$ ls
accounts  cds  credit_cards  loans
codemaster@Money:~/worldbanc/public/products$ cd credit_cards
codemaster@Money:~/worldbanc/public/products/credit_cards$ ls
creditplus.txt        tbills.txt
economypoints.txt     travelrewards.txt
freedomunited.txt     worldbanccard.txt
jointrewardsplux.txt
codemaster@Money:~/worldbanc/public/products/credit_cards$ touch credithistory.txt
codemaster@Money:~/worldbanc/public/products/credit_cards$ ls
credithistory.txt  jointrewardsplux.txt
creditplus.txt     tbills.txt
economypoints.txt  travelrewards.txt
codemaster@Money:~/worldbanc/public/products/credit_cards$