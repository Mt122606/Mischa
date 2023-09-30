{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44be6b2a-78f5-42c8-8969-3578ec1c7e32",
   "metadata": {},
   "outputs": [],
   "source": [
    "Guests = [\n",
    "    {'name' : 'Jon Doe', 'Great Work?' : False},\n",
    "    {'name' : 'Jane Doe', 'Great Work?' : False},\n",
    "    {'name' : 'Elvis Presley', 'Great Work?' : True}\n",
    "]\n",
    "\n",
    "def list_Guests():\n",
    "    for index, Guest in enumerate(Guests):\n",
    "        print(str.format('{}: {} (Great Work?: {})', index, Guest['name'], Guest['Great Work?']))\n",
    "\n",
    "\n",
    "def add_Guest():\n",
    "    Guest_text = input('Thank you for Visiting. \\n \\tPlease enter your name: ')\n",
    "    new_Guest ={'name':Guest_text,'Great Work?':False}\n",
    "    # Using the above task_text variable, create a dictionary named new_task and set completed to False\n",
    "    Guests.append(new_Guest)\n",
    "    # Then, add new_task to the tasks list\n",
    "\n",
    "def remove_Guest():\n",
    "# You will need a function to handle removing a task.\n",
    "    # When this function is run, list out the tasks. Hint! There is already a function that handles this\n",
    "    list_Guests()\n",
    "    # Here, create a variable that uses input. The user should be able to input the index number of the task to be removed. Hint! You will need to wrap the input() function within the int() function so the user's input is read as a number.\n",
    "    remove = int(input('which Guest would like to delete? :'))\n",
    "    # Here, delete the task in the tasks list based on the above variable\n",
    "    Guests.remove(Guests[remove])\n",
    "\n",
    "def Guest_Review():\n",
    "# You will need a function to handle marking a task complete.\n",
    "    # When this function is run, list out the tasks. Hint! There is a function that already does this for you.\n",
    "    list_Guests()\n",
    "    # Here, create a variable that uses input. The user should be able to input the index number of the task to be marked complete. Hint! You will need to wrap the input() function within the int() function so the user's input is read as a number.\n",
    "    Guest_Review = int(input('Which number guest are you in the above list? :'))\n",
    "    # Mark the task complete in the tasks list based on the variable you created above. Hint! you will need to use two sets of square brackets to find the index and set the appropriate key to True \n",
    "    Guests[Guest_Review]['Great Work?'] = True\n",
    "    \n",
    "\n",
    "menu_text = \"\"\"\n",
    "====================\n",
    "1. List the Guests\n",
    "2. Add your name to the guest list\n",
    "3. Remove a Guest\n",
    "4. Tell me that my work is great?\n",
    "5. Quit\n",
    "\n",
    "What would you like to do? \"\"\"\n",
    "\n",
    "program_is_running = True\n",
    "\n",
    "while program_is_running:\n",
    "    decision = input(menu_text)\n",
    "    if decision == '1':\n",
    "        list_Guests()\n",
    "    # Add elif statements for inputs 2, 3, and 4\n",
    "    elif decision == '2':\n",
    "        add_Guest()\n",
    "    elif decision == '3':\n",
    "        remove_Guest()\n",
    "    elif decision == '4':\n",
    "        Guest_Review()\n",
    "    elif decision == '5':\n",
    "        program_is_running = False\n",
    "    else: \n",
    "        print('please choose a valid option')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f24ecfab-3956-4f8f-8a4e-47ddf7733f08",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
