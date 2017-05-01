from subprocess import call

#txt="Hello Elijah"
txt="Ik ben Natalja."

speed=400

call(["C:\Program Files (x86)\eSpeak\command_line\espeak.exe",
      "-s"+str(speed), "-z","-vnl",
      txt])