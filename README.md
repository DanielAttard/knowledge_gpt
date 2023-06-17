<h1 align="center">
💸PropertyTaxGPT
</h1>

Accurate answers and instant citations for your documents.

## 🔧 Features

- Upload documents 📁(PDF, DOCX, TXT) and answer questions about them.
- Cite sources📚 for the answers, with excerpts from the text.

## 💻 Running Locally

1. Clone the repository📂

```bash
git clone https://github.com/mmz-001/knowledge_gpt
cd knowledge_gpt
```

2. Install dependencies with [Poetry](https://python-poetry.org/) and activate virtual environment🔨

```bash
poetry install
poetry shell
```

3. Run the Streamlit server🚀

```bash
cd knowledge_gpt
streamlit run main.py
```

## 🚀 Upcoming Features

- Add support for more formats (e.g. webpages 🕸️, PPTX 📊, etc.)
- Highlight relevant phrases in citations 🔦
- Support scanned documents with OCR 📝
- More customization options (e.g. chain type 🔗, chunk size📏, etc.)


Sasmitha Manathunga, Yesterday 11:30 AM
Ok, here's what's going on. When you run it on a google could workstation it's running on a different server (machine) and when you open VS code in the browser you are essentially connecting to it via a secure connection (SSH). So everything is encrypted between the browser VS code and your cloud workstation. But when you try to open the link via the external url you're trying to connect with it normally (no encryption) so it's probably rejecting it. 

You can solve this in two ways:
1. SSH port forwarding: You can allow your browser to securely connect to the network url. Go to the ports tab in the browser VSCode and forward the port 8501. Then you'll get a link where you can access it
2. Using a reverse proxy. Ok, this might be a little complicated but you'll need to allow HTTP connections to the external url. This will make it accessible to everyone (if that's what you want). I'm not sure how the Google Cloud Workstation works so you'll have to look up how to do this.

Daniel Attard, Yesterday 11:32 AM
I want to try and figure out the less complicated solution (#1). I just don't understand what you mean by this sentence: "Go to the ports tab in the browser VSCode and forward the port 8501"
do i set up port forwarding in chrome or vs code?

Sasmitha Manathunga, Yesterday 11:36 AM
You're running VS code in chrome right. Can you see a ports tab?

Daniel Attard, Yesterday 11:36 AM
VS code is a standalone app, right?

Sasmitha Manathunga, Yesterday 11:39 AM
Wait, when you said "VS code in the browser" what did you mean? How are you connecting to the google cloud workstation?

Daniel Attard, Yesterday 11:41 AM
Yes, I was originally connecting to the google cloud workstation using chrome.  Then I switched over to running VS Code locally and I was going to see if that was any different.  Which of these two methods do you think I should use?

Sasmitha Manathunga, Yesterday 11:42 AM
Running locally is the easiest, did you try it?

Daniel Attard, Yesterday 11:42 AM
i am trying that now but I am stuck on how to install poetry
i think it is installed, but when I do poetry install I get an error: poetry : The term 'poetry' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct 
and try again.
At line:1 char:1
+ poetry install
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (poetry:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

Sasmitha Manathunga, Yesterday 11:44 AM
Ah, you need to install poetry with
pip install poetry

Daniel Attard, Yesterday 11:45 AM
i did that and it says Requirement already satisfied...

Sasmitha Manathunga, Yesterday 11:46 AM
Try restarting VSCode.

Daniel Attard, Yesterday 11:47 AM
ok

Daniel Attard, Yesterday 11:51 AM
i closed and restarted VS Code and no difference.
should i be doing pip install poetry from CMD BASH or Powershell ?
I have always been confused about the difference in those

Sasmitha Manathunga, Yesterday 11:52 AM
CMD is fine for most purposes.

Daniel Attard, Yesterday 11:54 AM
i tried but still no luck.
this is so weird.  i'm sorry for taking up so much of your time.
i didn't expect it would be this complicated for me.

Sasmitha Manathunga, Yesterday 11:56 AM
Probably the issue is that your environment variables are messed up.  Manually editing them is a little complicated. Try installing it according to the official docs, it has a nice script:
https://python-poetry.org/docs/#installation
You'll have to use Powershell for this.

Daniel Attard, Yesterday 11:56 AM
Ok, I will give that a shot.  Thx.

Daniel Attard, Yesterday 12:08 PM
I managed to get Poetry installed manually as you suggested.  That's a start.
Then the problem was:  The currently activated Python version 3.8.5 is not supported by the project (^3.10).
Trying to find and use a compatible version.

Poetry was unable to find a compatible version. If you have one, you can explicitly use it via the "env use" command.
Then I tried to update python and received this:
i am going around in circles here.
I am the administrator and it's a Windows Server machine.

Sasmitha Manathunga, Yesterday 12:15 PM
You're getting there...Just a few more steps
You'll need to install Python 3.10 and I don't recommend installing it that way. 
You need to use a Python version management tool like py-env

Install it with the following command on Powershell:
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"

and check the installation  with pyenv --version on CMD
lmk if it's working, then we can move onto the next step

Daniel Attard, Yesterday 12:19 PM
I got this error in powershell: Invoke-WebRequest : The request was aborted: Could not create SSL/TLS secure channel.
At line:1 char:2

Daniel Attard, Yesterday 12:21 PM
ok, i fixed a few things and made progress...

Sasmitha Manathunga, Yesterday 12:22 PM
Oh, nice. Did you get py-env working?

Daniel Attard, Yesterday 12:22 PM
i think so...
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        15-Jun-23  12:18 PM                .pyenv
pyenv-win is successfully installed. You may need to close and reopen your terminal before using it.

Sasmitha Manathunga, Yesterday 12:22 PM
Try running this command pyenv --version

Daniel Attard, Yesterday 12:22 PM
ok
not recognized
maybe i need to close and reopen terminal.  will try that now
i restarted now now i get: pyenv 3.1.1

Sasmitha Manathunga, Yesterday 12:25 PM
NIce, let's now install Python 3.10.11 with:
pyenv install 3.10.11

Daniel Attard, Yesterday 12:25 PM
nice!  it is installing now!
completed

Sasmitha Manathunga, Yesterday 12:26 PM
Ok! now you need to activate it with:
pyenv global 3.10.11
Then check if it's working with:
python --version

Daniel Attard, Yesterday 12:28 PM

seems like it is still using 3.8.5

Sasmitha Manathunga, Yesterday 12:31 PM
Hmm, seems like you environment variables are kinda messed up. Editing it is a little bit messy. There's another way that might work. Try installing it with pip:
pip install pyenv-win --target %USERPROFILE%\\.pyenv
If this doesn't work:
pip install pyenv-win --target %USERPROFILE%\\.pyenv --no-user --upgrade

Daniel Attard, Yesterday 12:33 PM
the first command seemed to work.  how do i check?

Sasmitha Manathunga, Yesterday 12:34 PM
type where pyenv

Daniel Attard, Yesterday 12:34 PM
i did python --version and still 3.8.5


Sasmitha Manathunga, Yesterday 12:37 PM
Python 3.10.11 is already installed, I think it's the environment variables:
You can check the installation with:
where python

Sasmitha Manathunga, Yesterday 12:42 PM
If you're seeing python 3.8.5 as the first item then we'll have to change the environment variables... Let's keep this option as a last resort. I think poetry can automatically check if a suitable version is available. Try running poetry install on the project directory.

Daniel Attard, Yesterday 12:43 PM
ok i will try now
when you say to run that command on the project directory, i guess you mean from the knowledge_gpt folder

Sasmitha Manathunga, Yesterday 12:44 PM
correct

Sasmitha Manathunga, Yesterday 12:46 PM
btw you said you were running this on a Windows server machine. Is this your personal computer or a work computer?

Daniel Attard, Yesterday 12:48 PM
this is my own computer, and it is also a server, but not doing anything critical.
it is my personal playground

Sasmitha Manathunga, Yesterday 12:52 PM
Ah it's fine then. Because if you changed the environment variables on some work computer it might mess with other admin related stuff.

Ok, that's an weird error. You're there're two Python 3.8s

Can you run where python and check the output.

Daniel Attard, Yesterday 12:52 PM
i just noticed that when I enter py --version i get 3.10.11

Daniel Attard, Yesterday 12:55 PM
this is interesting:
seems like there is both py and python installed in separate locations
we want py which is 3.10.11

Sasmitha Manathunga, Yesterday 12:58 PM
Ok, if this is the case there might be another method. You can install poetry on Python 3.10 with
py -m pip install poetry

Daniel Attard, Yesterday 12:59 PM
ok, i think your suggestion will work.

Sasmitha Manathunga, Yesterday 1:00 PM
Did it install?

Daniel Attard, Yesterday 1:01 PM
yes!

Sasmitha Manathunga, Yesterday 1:01 PM
Ok, not install the dependencies with py -m poetry install on the project directory (You're currently on the wrong directory you have to go one folder up)
*now
type cd .. to go up

Sasmitha Manathunga, Yesterday 1:04 PM
Did it work?

Daniel Attard, Yesterday 1:06 PM
yes, it started to work, but then ran out of space on the C Drive 🙁
I will fix this issue and try again shortly

Sasmitha Manathunga, Yesterday 1:12 PM
I'll have to go now. I'll leave you with the next steps:
1.  Activate the virtual environment py -m poetry shell
2. Go to the knowledge_gpt folder with cd knowledge_gpt
3. Run Streamlit: streamlit run main.py

Also make sure to delete the .venv folder if you are running py -m poetry install again.
Hopefully this will work and if you have any issues we can talk tomorrow.
Bye

Daniel Attard, Yesterday 1:20 PM
Got it working, thanks to you.  You are amazing!
wow, incredible.

Sasmitha Manathunga, 10:47 AM
Cheers mate! 🎉

Daniel Attard, 10:57 AM
You should make it easy for people like me to send you money.  I looked around a bit and couldn't see an easy link to do that.
I see that your LinkedIn profile says you are open to work.  Maybe you might be interested in building something for me.

Sasmitha Manathunga, 12:11 PM
Well, buying me a coffee is always appreciated😊: https://www.buymeacoffee.com/mmz001


