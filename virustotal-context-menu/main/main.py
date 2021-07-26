'''
Created on Jul 26, 2021

@author: Private
'''
import sys
import time
import vt
from dotenv import load_dotenv
import os
import hashlib
import requests
import random

load_dotenv()

api_key = os.environ.get("api")
client = vt.Client(api_key)

filename = sys.argv[1] #reads in filename from context menu

#get md5 hash of file
gen_hash = hashlib.md5(open(filename, 'rb').read()).hexdigest()

print('''
 __      __ _                 _______      _          _      _    _         _                    _             
 \ \    / /(_)               |__   __|    | |        | |    | |  | |       | |                  | |            
  \ \  / /  _  _ __  _   _  ___ | |  ___  | |_  __ _ | |    | |  | | _ __  | |  ___    __ _   __| |  ___  _ __ 
   \ \/ /  | || '__|| | | |/ __|| | / _ \ | __|/ _` || |    | |  | || '_ \ | | / _ \  / _` | / _` | / _ \| '__|
    \  /   | || |   | |_| |\__ \| || (_) || |_| (_| || |    | |__| || |_) || || (_) || (_| || (_| ||  __/| |   
     \/    |_||_|    \__,_||___/|_| \___/  \__|\__,_||_|     \____/ | .__/ |_| \___/  \__,_| \__,_| \___||_|   
                                                                    | |                                        
                                                                    |_|                                        

++ By aliabe: https://github.com/aliabe-creator ++

===============================================================================================================
''')

time.sleep(1)

print(f'''
> Current file under analysis: <{filename}>

> Searching VirusTotal to see if analysis already exists...
''')

time.sleep(2)

posted = False

#check to see if file is already uploaded
def main_stuff():
    global posted
    
    try: #see if analysis already exists
        file = client.get_object("/files/" + gen_hash)
        
        stats = file.last_analysis_stats
        date = file.last_analysis_date
        size = file.size
        
        print(f'''
        ## Analysis Result ##
        ~~~~~~~~~~~~~~~~~~~~~
        Number of detections: {stats.get('malicious')}
        Number undetected: {stats.get('undetected')}
        ~~~~~~~~~~~~~~~~~~~~~
        File size (bytes): {size}
        Analyzed at {date}.
        
        ''')
        
        print('>>> Thanks for using VirusTotal Uploader! <<<\n\n')
        
    except Exception as e:
        if 'NotFound' in str(e): #means that the file hasn't been uploaded yet
            print('> File not in VirusTotal collection yet, uploading!\n')
            
            headers = {
                'x-apikey': api_key,
            }
            
            files = {'file': open(filename, 'rb')}
            
            requests.post('https://www.virustotal.com/api/v3/files', files=files, headers=headers) #upload file
            
            time.sleep(5)
            
            main_stuff() #returns to top
        
        if 'attribute' in str(e): #means that file.whatever fails, because the file is not analyzed yet
            if (posted == False): #post only once!
                print('> Looks like analysis has not completed yet. In the meantime, enjoy a selection of curated computer-speak.\n')
                posted = True
            
            time.sleep(4)
            
            funny_messages = ["Reticulating splines...",
                              "Generating witty dialog...",
                              "Swapping time and space...",
                              "Spinning violently around the y-axis...",
                              "Tokenizing real life...",
                              "Bending the spoon...",
                              "Filtering morale...",
                              "Don't think of purple hippos...",
                              "We need a new fuse...",
                              "Have a good day.",
                              "Upgrading Windows, your PC will restart several times. Sit back and relax.",
                              "640K ought to be enough for anybody",
                              "The architects are still drafting",
                              "The bits are breeding",
                              "We're building the buildings as fast as we can",
                              "Would you prefer chicken, steak, or tofu?",
                              "(Pay no attention to the man behind the curtain)",
                              "...and enjoy the elevator music...",
                              "Please wait while the little elves draw your map",
                              "Don't worry - a few bits tried to escape, but we caught them",
                              "Would you like fries with that?",
                              "Checking the gravitational constant in your locale...",
                              "Go ahead -- hold your breath!",
                              "...at least you're not on hold...",
                              "Hum something loud while others stare",
                              "You're not in Kansas any more",
                              "The server is powered by a lemon and two electrodes.",
                              "Please wait while a larger software vendor in Seattle takes over the world",
                              "We're testing your patience",
                              "As if you had any other choice",
                              "Follow the white rabbit",
                              "Why don't you order a sandwich?",
                              "While the satellite moves into position",
                              "keep calm and npm install",
                              "The bits are flowing slowly today",
                              "Dig on the 'X' for buried treasure... ARRR!",
                              "It's still faster than you could draw it",
                              "The last time I tried this the monkey didn't survive. Let's hope it works better this time.",
                              "I should have had a V8 this morning.",
                              "My other loading screen is much faster.",
                              "Testing on Timmy... We're going to need another Timmy.",
                              "Reconfoobling energymotron...",
                              "(Insert quarter)",
                              "Are we there yet?",
                              "Have you lost weight?",
                              "Just count to 10",
                              "Why so serious?",
                              "It's not you. It's me.",
                              "Counting backwards from Infinity",
                              "Don't panic...",
                              "Embiggening Prototypes",
                              "Do not run! We are your friends!",
                              "Do you come here often?",
                              "Warning: Don't set yourself on fire.",
                              "We're making you a cookie.",
                              "Creating time-loop inversion field",
                              "Spinning the wheel of fortune...",
                              "Loading the enchanted bunny...",
                              "Computing chance of success",
                              "I'm sorry Dave, I can't do that.",
                              "Looking for exact change",
                              "All your web browser are belong to us",
                              "All I really need is a kilobit.",
                              "I feel like im supposed to be loading something. . .",
                              "What do you call 8 Hobbits? A Hobbyte.",
                              "Should have used a compiled language...",
                              "Is this Windows?",
                              "Adjusting flux capacitor...",
                              "Please wait until the sloth starts moving.",
                              "Don't break your screen yet!",
                              "I swear it's almost done.",
                              "Let's take a mindfulness minute...",
                              "Unicorns are at the end of this road, I promise.",
                              "Listening for the sound of one hand clapping...",
                              "Keeping all the 1's and removing all the 0's...",
                              "Putting the icing on the cake. The cake is not a lie...",
                              "Cleaning off the cobwebs...",
                              "Making sure all the i's have dots...",
                              "We are not liable for any broken screens as a result of waiting.",
                              "We need more dilithium crystals",
                              "Where did all the internets go",
                              "Connecting Neurotoxin Storage Tank...",
                              "Granting wishes...",
                              "Time flies when you’re having fun.",
                              "Get some coffee and come back in ten minutes..",
                              "Spinning the hamster…",
                              "99 bottles of beer on the wall..",
                              "Stay awhile and listen..",
                              "Be careful not to step in the git-gui",
                              "You shall not pass! yet..",
                              "Load it and they will come",
                              "Convincing AI not to turn evil..",
                              "There is no spoon. Because we are not done loading it",
                              "Your left thumb points to the right and your right thumb points to the left.",
                              "How did you get here?",
                              "Wait, do you smell something burning?",
                              "Computing the secret to life, the universe, and everything.",
                              "When nothing is going right, go left!!...",
                              "I love my job only when I'm on vacation...",
                              "i'm not lazy, I'm just relaxed!!",
                              "Never steal. The government hates competition....",
                              "Why are they called apartments if they are all stuck together?",
                              "Life is Short – Talk Fast!!!!",
                              "Optimism – is a lack of information.....",
                              "Save water and shower together",
                              "Whenever I find the key to success, someone changes the lock.",
                              "Sometimes I think war is God’s way of teaching us geography.",
                              "I’ve got problem for your solution…..",
                              "Where there’s a will, there’s a relative.",
                              "User: the word computer professionals use when they mean !!idiot!!",
                              "Adults are just kids with money.",
                              "I think I am, therefore, I am. I think.",
                              "A kiss is like a fight, with mouths.",
                              "You don’t pay taxes—they take taxes.",
                              "Coffee, Chocolate, Men. The richer the better!",
                              "I am free of all prejudices. I hate everyone equally.",
                              "git happens",
                              "May the forks be with you",
                              "A commit a day keeps the mobs away",
                              "This is not a joke, it's a commit.",
                              "Constructing additional pylons...",
                              "Roping some seaturtles...",
                              "Locating Jebediah Kerman...",
                              "We are not liable for any broken screens as a result of waiting.",
                              "Hello IT, have you tried turning it off and on again?",
                              "If you type Google into Google you can break the internet",
                              "Well, this is embarrassing.",
                              "What is the airspeed velocity of an unladen swallow?",
                              "Hello, IT... Have you tried forcing an unexpected reboot?",
                              "They just toss us away like yesterday's jam.",
                              "They're fairly regular, the beatings, yes. I'd say we're on a bi-weekly beating.",
                              "The Elders of the Internet would never stand for it.",
                              "Space is invisible mind dust, and stars are but wishes.",
                              "Didn't know paint dried so quickly.",
                              "Everything sounds the same",
                              "I'm going to walk the dog",
                              "I didn't choose the engineering life. The engineering life chose me.",
                              "Dividing by zero...",
                              "Spawn more Overlord!",
                              "If I’m not back in five minutes, just wait longer.",
                              "Some days, you just can’t get rid of a bug!",
                              "We’re going to need a bigger boat.",
                              "Chuck Norris never git push. The repo pulls before.",
                              "Web developers do it with <style>",
                              "I need to git pull --my-life-together",
                              "Java developers never RIP. They just get Garbage Collected.",
                              "Cracking military-grade encryption...",
                              "Simulating traveling salesman...",
                              "Proving P=NP...",
                              "Entangling superstrings...",
                              "Twiddling thumbs...",
                              "Searching for plot device...",
                              "Trying to sort in O(n)...",
                              "Laughing at your pictures-i mean, loading...",
                              "Sending data to NS-i mean, our servers.",
                              "Looking for sense of humour, please hold on.",
                              "Please wait while the intern refills his coffee.",
                              "A different error message? Finally, some progress!",
                              "Hold on while we wrap up our git together...sorry",
                              "Please hold on as we reheat our coffee",
                              "Kindly hold on as we convert this bug to a feature...",
                              "Kindly hold on as our intern quits vim...",
                              "Winter is coming...",
                              "Installing dependencies",
                              "Switching to the latest JS framework...",
                              "Distracted by cat gifs",
                              "Finding someone to hold my beer",
                              "BRB, working on my side project",
                              "@todo Insert witty loading message",
                              "Let's hope it's worth the wait",
                              "Aw, snap! Not..",
                              "Ordering 1s and 0s...",
                              "Updating dependencies...",
                              "Whatever you do, don't look behind you...",
                              "Please wait... Consulting the manual...",
                              "It is dark. You're likely to be eaten by a grue.",
                              "Loading funny message...",
                              "It's 10:00pm. Do you know where your children are?",
                              "Waiting Daenerys say all her titles...",
                              "Feel free to spin in your chair",
                              "What the what?",
                              "format C: ...",
                              "Forget you saw that password I just typed into the IM ...",
                              "What's under there?",
                              "Your computer has a virus, its name is Windows!",
                              "Go ahead, hold your breath and do an ironman plank till loading complete",
                              "Bored of slow loading spinner, buy more RAM!",
                              "Help, I'm trapped in a loader!",
                              "What is the difference btwn a hippo and a zippo? One is really heavy, the other is a little lighter",
                              "Please wait, while we purge the Decepticons for you. Yes, You can thanks us later!",
                              "Chuck Norris once urinated in a semi truck's gas tank as a joke....that truck is now known as Optimus Prime.",
                              "Chuck Norris doesn’t wear a watch. HE decides what time it is.",
                              "Mining some bitcoins...",
                              "Downloading more RAM..",
                              "Updating to Windows Vista...",
                              "Deleting System32 folder",
                              "Hiding all ;'s in your code",
                              "Alt-F4 speeds things up.",
                              "Initializing the initializer...",
                              "When was the last time you dusted around here?",
                              "Optimizing the optimizer...",
                              "Last call for the data bus! All aboard!",
                              "Running swag sticker detection...",
                              "When nothing is going right, go left!",
                              "Never let a computer know you're in a hurry.",
                              "A computer will do what you tell it to do, but that may be much different from what you had in mind.",
                              "Some things man was never meant to know. For everything else, there's Google.",
                              "Unix is user-friendly. It's just very selective about who its friends are.",
                              "Shovelling coal into the server",
                              "Pushing pixels...",
                              "How about this weather, eh?",
                              "Building a wall...",
                              "Everything in this universe is either a potato or not a potato",
                              "The severity of your issue is always lower than you expected.",
                              "Updating Updater...",
                              "Downloading Downloader...",
                              "Debugging Debugger...",
                              "Reading Terms and Conditions for you.",
                              "Digested cookies being baked again.",
                              "Live long and prosper.",
                              "There is no cow level, but there's a goat one!",
                              "Running with scissors...",
                              "Definitely not a virus...",
                              "You may call me Steve.",
                              "All you had to do is to commit the damn funnies, CJ!",
                              "You seem like a nice person...",
                              "Coffee at my place, tommorow at 10A.M. - don't be late!",
                              "Work, work...",
                              "Patience! This is difficult, you know...",
                              "Discovering new ways of making you wait...",
                              "Your time is very important to us. Please wait while we ignore you...",
                              "Time flies like an arrow; fruit flies like a banana",
                              "Two men walked into a bar; the third ducked...",
                              "Sooooo... Have you seen my vacation photos yet?",
                              "Sorry we are busy catching em' all, we're done soon",
                              "TODO: Insert elevator music",
                              "Still faster than Windows update",
                              "Composer hack: Waiting for reqs to be fetched is less frustrating if you add -vvv to your command.",
                              "Obfuscating quantum entaglement",
                              "Knock, Knock! Who’s there? Ken Ken who? Ken I come in? It's cold out here.",
                              "If at first you don't succeed, call it version 1.0.",
                              "I love pressing F5. It's so refreshing.",
                              "CAPS LOCK – Preventing Login Since 1980.",
                              "Chuck Norris doesn't scroll with a mouse. He uses a lion.",
                              "Chuck Norris can delete the Recycling Bin.",
                              "With just two toothpicks, a lightbulb, and his RoundHouse Kick, Chuck Norris can override the Pentagon's computer system.",
                              "If you see the Blue Screen of Death on your laptop... it's because Chuck Norris found out you were reading Chuck Norris jokes.",
                              "Chuck Norris didn't survive the first night in Minecraft, the first night survived Chuck Norris.",
                              "Chuck Norris could play cd-based games on his Nintendo 64.",
                              "Why did the computer get cold? Because it forgot to close windows.",
                              "Chuck Norris's keyboard doesn't have a Ctrl key because nothing controls Chuck Norris.",
                              "Preventing robot uprising ...",
                              "Hacking into the Main Frame...",
                              "Installing virus...",
                              "Loading Error...",
                              "PC LOAD LETTER...",
                              "Waiting for something to load sucks...",
                              "Deleting system32...",
                              "- What are you working? - I'm a programmer. - More precisely? - At home, I change TV programs.",
                              "New LG Refrigerators with Windows 10 ... 'A cold brandy pleats!' - Server Error 404, no Brandy available.",
                              "Oh, are you waiting for me?",
                              "Do you smell carrots? -a snowman",
                              "That job was a piece of cake",
                              "Oh you are an eager beaver",
                              "He makes a monkey business",
                              "The Game - you just lost it."]
            
            print(random.choice(funny_messages))
            
            time.sleep(10)
            
            main_stuff() #check again to see if analyzed
            
main_stuff()