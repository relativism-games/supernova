# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

label intro_backend:

    transform q1:
        alpha 0.0 xalign .1 yalign .10
        ease 10 alpha 1.0

    transform q2:
        alpha 0.0 xalign .1 yalign .20
        ease 10 alpha 1.0 

    transform q3:
        alpha 0.0 xalign .1 yalign .30
        ease 10 alpha 1.0
        

# Игра начинается здесь:
label start:

    scene black with fade
    $ pause_ = 10
    show text "{color=#f00}90 percents of information we recieve come through our eyes...{/color}" at q1
    $ renpy.pause(pause_, hard=True)
    show text "{color=#f00}In the distant future, humanity used this to trick itself into believing...{/color}" at q2
    $ renpy.pause(pause_, hard=True)
    show text "{color=#f00}That we have made it through the border of the speed of light...{/color}" at q3
    $ renpy.pause(pause_, hard=True)
    "{cps=5}{color=#f00}S U P E R N O V A{/color}{/cps}"

#label start:

    #scene black with fade
    #$ pause_ = 10
    #image text_1 = "{color=#f00}90 percents of information we recieve come through our eyes...{/color}"(xalign=.1 yalign=.10)
    #$ renpy.pause(pause_, hard=True)
    

return
