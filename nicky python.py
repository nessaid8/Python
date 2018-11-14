import pyautogui as pg
import webbrowser as wb
import time as t 
points = 0
show = pg.prompt ("What is your favorite TV show? ")

if show == "hannah montana":
    pg.alert ("OMG LOL xD ")
    points += 1
    t.sleep (1)
    wb.open ("https://www.youtube.com/watch?v=uVjRe8QXFHY")
elif show == "the office":
    pg.alert ("snazzy")
    points += 2
    t.sleep (1)
    wb.open ("https://www.youtube.com/watch?v=WaaANll8h18")
elif show == "family guy":
    pg.alert ("Cool")
    points += 10
    t.sleep (1)
    wb.open ("https://www.youtube.com/watch?v=-gTJVEQjuB0")
elif show == "rick and morty":
    pg.alert ("silly")
    points += 90
    t.sleep (1)
    wb.open("https://www.google.com/search?q=rick+and+morty&client=firefox-b-ab&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjj07fc6LDeAhUom-AKHYPLD_sQ_AUIDigB&biw=1366&bih=659#imgrc=BMBV2mHqYNFRIM:")
elif show == "Gossip Girl":
    pg.alert ("oh")
    points += 1
elif show == "sports center":
    pg.alert ("wow")
    points += 3
    t.sleep (1)
    wb.open ("https://www.google.com/search?q=sportscenter&rlz=1C1GCEA_enUS752US765&tbm=isch&source=lnms&sa=X&ved=0ahUKEwjG9YrAwsLeAhUEmuAKHVn_Ak8Q_AUIDCgD&biw=756&bih=684&dpr=0.9")
else:
    pg.alert ("Your favorite show is " + show )
    points += 0

game = pg.prompt ("What is your favorite game? ")

if game == "fortnite":
    pg.alert ("cool")
    points += 1
    t.sleep (1)
    wb.open ("https://www.google.com/search?q=fortnite&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjGy6zW67DeAhWlhOAKHTXDCiMQ_AUIECgD&biw=1011&bih=685#imgrc=BFNXM9L-mRUZiM:")

elif game == "pubg":
    pg.alert ("Holy massive")
    points += 1

elif game == "fifa":
    pg.alert ("Love that")
    points += 6
    t.sleep (1)
    wb.open ("https://www.google.com/search?q=fifa&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj8lNnh67DeAhUHhuAKHZl2A5AQ_AUIDigB&biw=1011&bih=685")

elif game == "nhl":
    pg.alert == ("Good game")
    points += 11
    t.sleep (1)
    wb.open ("https://www.youtube.com/watch?v=MdKlpDPaVGc")

elif game == "madden":
    pg.alert == ("lit")
    points += 15
    t.sleep (1)
    wb.open ("https://www.youtube.com/watch?v=Js04hvdVUA8&vl=en")

elif game == "cod":
    pg.alert == ("fun game")
    points += 15
    t.sleep (1)
    wb.open ("https://www.callofduty.com/blackops4")

else:
    pg.alert ("Your favorite game is " + game )
    points += 0


drop = pg.prompt ("What is your favorite landing area? ")

if drop == "tilted":
    pg.alert ("wow")
    points += 7
    t.sleep (1)
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US765&biw=1011&bih=685&tbm=isch&sa=1&ei=bbXZW9y9JaW3ggeJgI7IDA&q=tilted+towers&oq=tilted+tow&gs_l=img.3.0.0l10.5138.6526..8322...2.0..0.58.314.6......0....1..gws-wiz-img.......0i67.SupoxGxiNbw")
elif drop == "salty":
    pg.alert ("ok hot shot")
    points += 9
    t.sleep (1)
    wb.open ("https://www.google.com/search?q=salty+springs&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiFk8bcw8LeAhWDmeAKHZljBEoQ_AUIEygB&biw=756&bih=684#imgrc=Fo_0HFvHpBwcSM:")
elif drop == "retail":
    pg.alert ("Sick bro ")
    points += 8
    t.sleep (1)
    wb.open ("https://www.google.com/search?q=retail+row&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjF6_6z67DeAhXoc98KHWUCAr4Q_AUIDigB&biw=1011&bih=685#imgrc=0snZd1jdGAlKaM:")

elif drop == "pleasant":
    pg.alert ("cool")
    points += 76
    t.sleep (1)
    wb.open ("https://www.google.com/search?q=pleasant+park&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwih3bfyw8LeAhVCpFkKHT43AawQ_AUIEygB&biw=756&bih=684#imgrc=D11hLiwDoHbjBM:")
elif drop == "risky reels":
    pg.alert ("Great area")
    points += 14
elif drop == "paradise palms":
    pg.alert ("wow")
    points += 31
else:
    pg.alert ("You drop at " + drop )
    points += 0

food = pg.prompt ("What is you favorite food?")
if food == "sushi":
    pg.alert ("Thats my favorite")
    points += 17
    t.sleep (1)
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US765&tbm=isch&q=sushi&chips=q:sushi,g_1:japanese:--ab589XR4c%3D&usg=AI4_-kQihCH4vMlRDSUxNjkDlASUr2s5cQ&sa=X&ved=0ahUKEwi80KX26bDeAhXjUN8KHVrqBiIQ4lYILSgD&biw=1011&bih=685&dpr=0.9")
elif food == "tacos":
    pg.alert ("another great food")
    points += 11
    t.sleep (1)
    wb.open ("https://www.google.com/search?q=tacos&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjL9sKdxMLeAhVPq1kKHYaLBX0Q_AUIFCgC&biw=756&bih=684#imgrc=7Ks07d4VnVKaAM:")
elif food == "pizza":
    pg.alert ("its so good")
    points += 11
elif food == "ice cream":
    pg.alert ("such a great food")
    points += 2
    t.sleep (1)
    wb.open ("https://www.google.com/search?q=ice+cream&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwics8OvxMLeAhUrq1kKHRItB4wQ_AUIFCgC&biw=756&bih=684#imgrc=TlPFnPHAqJPTnM:")
elif food == "hamburgers":
    pg.alert ("classic")
    points += 19
    t.sleep (1)
    wb.open ("https://www.google.com/search?q=hamburgers&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwib2Oe8xMLeAhWluVkKHeqcAVQQ_AUIFCgC&biw=756&bih=684#imgrc=O_6Ix0v62pojWM:")
elif food == "pancakes":
    pg.alert ("awesome")
    points += 4
    t.sleep (1)
    wb.open ("https://www.google.com/search?q=pancakes&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj_tMPU6bDeAhWjct8KHSvdA4IQ_AUIDigB&biw=1011&bih=685#imgrc=9eK6mnqp3LvoaM:")

else:
    pg.alert ("Your Favorite food is" + food)

tunes = pg.prompt ("Who is you favorite loony tunes character?")
if tunes == "bugs bunny":
    pg.alert ("he is the best ")
    points += 17
    t.sleep (1)
    wb.open("https://www.youtube.com/watch?v=qDLN3W4Y2l4")
elif tunes == "yosemite":
    pg.alert ("my favorite")
    points += 4
    t.sleep (1)
    wb.open("https://www.youtube.com/watch?v=QYiCP1kxL1E")

elif tunes == "elmer fudd":
    pg.alert ("he is a classic")
    points += 53
    t.sleep (1)
    wb.open ("https://www.youtube.com/watch?v=qRVKFq9qUiQ")
elif tunes == "roadrunner":
    pg.alert ("one of the best")
    points += 53
    t.sleep (1)
    wb.open("https://www.youtube.com/watch?v=GdKkI1vGsmE")
elif tunes == "taz":
    pg.alert ("Everyone love him")
    points += 11
    t.sleep (1)
    wb.open("https://www.youtube.com/watch?v=FOTlNOZB4Zo")
elif tunes == "tweety":
    pg.alert ("gotta love him")
    points +=47
    t.sleep (1)
    wb.open("https://www.youtube.com/watch?v=F3wP--Wc9tQ")
else:
    pg.alert ("Your favorite character from loony tunes is " + tunes)

        





pg.alert("You scored: " +(str(points)))




