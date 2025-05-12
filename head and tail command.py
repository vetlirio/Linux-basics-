head and tail

Sometimes you don't want to print everything in a file. Files can be really big after all.
The head Command

The head command prints the first n lines of a file, where n is a number you specify.

head -n 10 file1.txt

If you don't specify a number, it will default to 10.
The tail Command

The tail command prints the last n lines of a file, where n is a number you specify.

tail -n 10 file1.txt



codemaster@Money:~/worldbanc/private/transactions$ head -n 6 2023.csv
amount,from_user_id,to_user_id,from_name,to_name,created_at
80.16,18,14,Steve,Oscar,2023-07-05 08:43:55
962.70,5,10,Frank,Kyle,2023-01-07 18:39:14
407.51,4,4,Eva,Eva,2023-05-31 15:26:04
827.96,4,1,Eva,Bob,2023-06-03 16:53:02
472.91,5,13,Frank,Nora,2023-02-05 06:47:19
codemaster@Money:~/worldbanc/private/transactions$ tail -n 5 2023.csv
393.56,14,4,Oscar,Eva,2023-09-04 14:04:54
861.65,11,6,Lily,Grace,2023-08-10 01:28:46
210.75,5,5,Frank,Frank,2023-04-20 03:23:14
737.84,18,4,Steve,Eva,2023-11-18 16:21:57
683.91,10,8,Kyle,Ivan,2023-11-11 18:57:27