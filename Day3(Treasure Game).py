print('''

     ,*-~"`^"*u_                                _u*"^`"~-*,
  p!^       /  jPw                            w9j \        ^!p
w^.._      /      "\_                      _/"     \        _.^w
     *_   /          \_      _    _      _/         \     _* 
       q /           / \q   ( `--` )   p/ \          \   p
       jj5****._    /    ^\_) o  o (_/^    \    _.****6jj
                *_ /      "==) ;; (=="      \ _*
                 `/.w***,   /(    )\   ,***w.\"
                  ^ ilmk ^c/ )    ( \c^      ^
                          'V')_)(_('V'
                              `` ``

''')
print("Welcome to Daddy Island.")
print("Your mission is to find your Daddy.") 
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left"or"right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve came to the lake.There is a island in the middle of the lake. Type"wait"for the boat. type "swim"swim across.\n').lower()
    if choice2== "wait":
        choice3 = input('You arrived at the island unharmed.There is a house with three doors.\n One red , one yellow and one blue.\nWhich color do you choose?\n').lower()
        if choice3 =="red":
            print("Its a room full of fire.\n burn to hell you trash.\nGame Over")
        elif choice3 =="yellow":
            print("Congrats you found your Daddy.\n ----------Call me Daddy---------")
        elif choice3 =="blue":
            print("Its a room full of Bats.\nSuch a dissapointed asshole you are.\nGame Over")

        else:
            print("You didnt choose which leads the Slender Man to find you.\nEaster Egg\n buhahahaha asshole die.\nGame Over")

    else:
        print("Cant Even do anything you know uncle ben son is good at making decissions.\n Game Over")

elif choice1 == "right":
    print("Fuiyyyyaaaaa \n Such a trash you are.\nGame Over")

else:
    print("Dissapointment game hasnt even started and you lost.\n You born dissapontment.\nGame Over")


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

