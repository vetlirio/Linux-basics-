More and Less

The more and less commands let you view the contents of a file, one page (or line) at a time.

As the adage goes, less is more.

In the context of these commands, less is literally more. The less command does everything that the more command does but also has more features. As a general rule, you should use less instead of more.

You would only use more if you're on a system that doesn't have less installed.
Assignment

You found nothing suspicious in the first and last transactions of 2023, but you're not done yet! It's time to dig through the middle of the file as well.

    Run less and pass in the path to the 2023.csv file, located at the root in the worldbanc/private/transactions directory.

less 2023.csv

Notice that you're now in an interactive mode and you've lost your shell prompt! That's because less has taken over your terminal window.

    Press "enter" a few times to scroll down a few lines, just to see how that works. Press "q" to exit the less program and return to your shell prompt.
    Re-run the less command, but this time, pass in the -N flag to show line numbers:

less -N 2023.csv

You can use the spacebar to scroll down a page at a time, and you can go back up by pressing "b".

    Find line 153. Copy and paste the contents of that line into the text field and submit it.

You can use "q" to exit less at any time.


    153 876.65,12,2,Mia,Charlie,2023-07-30 03:44:00
