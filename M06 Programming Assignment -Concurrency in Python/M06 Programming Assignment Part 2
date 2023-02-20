# M06 Programming Assignment - Concurrency in Python
# Author: Xander Jewell
# Created: 2022-02-20
# Doing the Programming Assingments in our class book: 
# 15.1

# Importing Multiprocessing
import multiprocessing
# Importing datetime from datetime
from datetime import datetime 
# Importing Sleep from time
from time import sleep
# Importing Random
import random

# Creating a function to print the information
def current_time(second):
    # Making sure that function sleeps at each second
    sleep(second)
    # Printing the information
    print(f'Waiting {second} seconds / The time is {datetime.utcnow()}')

if __name__ == '__main__':
    # Creating a for loop to do the multiprocessing
    for n in range(3):
        # Creating a random second
        second = random.random()
        # defining the process
        process = multiprocessing.Process(target=current_time, args=(second,))
        # Starting the process
        process.start()
