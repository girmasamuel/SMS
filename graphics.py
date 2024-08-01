import time

RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = "\033[0;35m"
WATERBLUE = "\033[36m"
END = "\033[0m"

def banner(page):
    art = f'''
{RED}************************************************************************************************************************{END}
{RED}*{END}  {BLUE}               @        SSSSSSSS  TTTTTTTTTTTTTTT  U       U    ADAMA SCIENCE AND TECHNOLOGY UNIVERSITY             {RED}*
{RED}*{END}  {BLUE}              @ @       S                T         U       U                                                        {RED}*
{RED}*{END}  {BLUE}             @   @      SSSSSSSS         T         U       U  {GREEN}"WE ARE DEDICATED TO INNOVATIVE KNOWLADGE"            {RED}*
{RED}*{END}  {BLUE}            @@@@@@@            S         T         U       U                                                        {RED}*
{RED}*{END}  {BLUE}           @       @   S       S         T         U       U    {PURPLE}__________________________________________ {END}         {RED}*
{RED}*{END}  {BLUE}          @         @  SSSSSSSSS         T         UUUUUUUUU         {YELLOW} {page}{END}                  
{RED}*{END}{PURPLE}------------------------------------------------------------------\________________________________________/          {RED}*
{RED}*{END} {YELLOW}         This is terminal studentent management system !                                                             {RED}*
{RED}************************************************************************************************************************{END}
'''
    print(art)


def stream_write(text):
    for char in text:
        print(char,end="")
        time.sleep(0.1)
    print("")

