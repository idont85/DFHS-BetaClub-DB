import json

data = "Sean Jamison <17319@stu.lexrich5.org>, Maria Figueredo Gutierrez <34339@stu.lexrich5.org>, Elsie Johnson <23372@stu.lexrich5.org>, Destiny Rossignol <40158@stu.lexrich5.org>, Mia Burgess <18067@stu.lexrich5.org>, Kayla Guess <18610@stu.lexrich5.org>, Tyler Lahn <51434@stu.lexrich5.org>, Nathan Boyd <20494@stu.lexrich5.org>, Reagan Byrd <22428@stu.lexrich5.org>, Tyler Dukes <18420@stu.lexrich5.org>, Blake Splittgerber <20801@stu.lexrich5.org>, Myla Boston <41662@stu.lexrich5.org>, Evan DeMasi <20981@stu.lexrich5.org>, Justin Etheredge <37425@stu.lexrich5.org>, Jaylon Nowell <37064@stu.lexrich5.org>, James Raye <41706@stu.lexrich5.org>, Hersh Patel <20432@stu.lexrich5.org>, Koen Schirnhofer <53615@stu.lexrich5.org>, John Spehl <21003@stu.lexrich5.org>, Destiny Jasmin <24434@stu.lexrich5.org>, Juan Andre Vejerano <30561@stu.lexrich5.org>, Jonathan White <42572@stu.lexrich5.org>, Ruth Munywoki <36137@stu.lexrich5.org>, Faith Ross <22435@stu.lexrich5.org>, Joshua Jacobs <25535@stu.lexrich5.org>, Miller Anderson <20985@stu.lexrich5.org>, Fatima Sangarie <49519@stu.lexrich5.org>, Jayden Won <31554@stu.lexrich5.org>, Mumtaheena Ali <53382@stu.lexrich5.org>, Luka Kublashvili <16038@stu.lexrich5.org>, Alexandra Armstrong <24678@stu.lexrich5.org>, Cierra Starks <19210@stu.lexrich5.org>, Adam Thur <23550@stu.lexrich5.org>, Kenneth Benson <39369@stu.lexrich5.org>, Lian Cing <21687@stu.lexrich5.org>, Lizabeth Shough <43638@stu.lexrich5.org>, Thorge Diekmann <54068@stu.lexrich5.org>, Kyrah Roussel <35427@stu.lexrich5.org>, Stacey Keener <20723@stu.lexrich5.org>, Cally Stillinger <31084@stu.lexrich5.org>, Makel Coleman <18439@stu.lexrich5.org>, Rachel Horrigan <23583@stu.lexrich5.org>, Moriah Ross <30627@stu.lexrich5.org>, Keira Harris <42308@stu.lexrich5.org>, Addison Biehl <26578@stu.lexrich5.org>, Dayon Barnett <33751@stu.lexrich5.org>, Dylan Russell <25236@stu.lexrich5.org>, Travis Johnson <32717@stu.lexrich5.org>, Ginevra Benvenuto <52653@stu.lexrich5.org>, Sarah Bennett <39257@stu.lexrich5.org>, Ashlyn Waites <26496@stu.lexrich5.org>, Paris Young <17665@stu.lexrich5.org>, Josephine Favati <25230@stu.lexrich5.org>, Luke Tully <23555@stu.lexrich5.org>, Micah Austin <28765@stu.lexrich5.org>, Majd Anay <24088@stu.lexrich5.org>, Ella Pridgen <24346@stu.lexrich5.org>, Jillian Giordano <27162@stu.lexrich5.org>, Jacob Parker <17974@stu.lexrich5.org>, Cyrus Farris <50709@stu.lexrich5.org>, Weiyi Tu <53785@stu.lexrich5.org>, T'Ariyah Henderson <39439@stu.lexrich5.org>, Skye Veil <26959@stu.lexrich5.org>, Zariel Hunt <23574@stu.lexrich5.org>, Leo Ha <40083@stu.lexrich5.org>, Payton Quillen <22319@stu.lexrich5.org>, Nicholas Anderson <22198@stu.lexrich5.org>, Preston Scott <19107@stu.lexrich5.org>, Caroline Wahrmund <20783@stu.lexrich5.org>, Caroline Caldwell <44784@stu.lexrich5.org>, Seungoh Son <40559@stu.lexrich5.org>, Cecilia Turner <39413@stu.lexrich5.org>, Mahika Mehta <26387@stu.lexrich5.org>, Lily Rowlett <26467@stu.lexrich5.org>, Ximena Villavicencio <16893@stu.lexrich5.org>, Levi Bundrick <26157@stu.lexrich5.org>, Michael Wang <25099@stu.lexrich5.org>, Shaniya Stokes <22347@stu.lexrich5.org>, Krish Patel <26420@stu.lexrich5.org>, Emma Morris <27413@stu.lexrich5.org>, Christiana Ross <30558@stu.lexrich5.org>, Bailey Whorton <23783@stu.lexrich5.org>, Katherine Pinkney <21369@stu.lexrich5.org>, Kerlss Khilqa <22410@stu.lexrich5.org>, Logan Pichey <39645@stu.lexrich5.org>, Xin Yao Zheng <47462@stu.lexrich5.org>, William Wang <29923@stu.lexrich5.org>, Ayden Robinson <44428@stu.lexrich5.org>, Hunter Taylor <26369@stu.lexrich5.org>, Edward Feng <30038@stu.lexrich5.org>, William Zamcho <20618@stu.lexrich5.org>, Alexander Kichukov <21001@stu.lexrich5.org>, Carson Witteborg <23987@stu.lexrich5.org>, Mikayla Linder <26630@stu.lexrich5.org>, Alexandra Sevilla <53337@stu.lexrich5.org>, Marianne Williams <23784@stu.lexrich5.org>, Valeria Rodriguez Galguera <46783@stu.lexrich5.org>, Mariyah Maston <22758@stu.lexrich5.org>, Alana Goggins <18259@stu.lexrich5.org>, Allison Burroughs <39359@stu.lexrich5.org>, Lily Chapman <26297@stu.lexrich5.org>, Michael Maston <18949@stu.lexrich5.org>, Sahasra Eippa <43012@stu.lexrich5.org>, Kaleb Kennedy <21056@stu.lexrich5.org>, Finlay Kramer <25404@stu.lexrich5.org>, Helena Tang <26494@stu.lexrich5.org>, Cedric Davis <20839@stu.lexrich5.org>, McRea Delbridge <20784@stu.lexrich5.org>, Anna Murphy <18010@stu.lexrich5.org>, Bradley O'Leary <21080@stu.lexrich5.org>, Micah Jones <20441@stu.lexrich5.org>, Madeline Muller <18940@stu.lexrich5.org>, Luisa Marmolejo Roman <28482@stu.lexrich5.org>, Tayla Toney <48152@stu.lexrich5.org>, Senai Ginther <32896@stu.lexrich5.org>, Caleb Neese <43048@stu.lexrich5.org>, Evan Thacker <23782@stu.lexrich5.org>, Camille Taylor <40948@stu.lexrich5.org>, Lucy Park <20918@stu.lexrich5.org>, Riley Garrick <26885@stu.lexrich5.org>, Bradley Ridenhour <25470@stu.lexrich5.org>, Keli Taylor <45328@stu.lexrich5.org>, Seth Cantave <28887@stu.lexrich5.org>, Suri Cantave <28888@stu.lexrich5.org>, George Bates <18059@stu.lexrich5.org>, Zhien Hu <49528@stu.lexrich5.org>, John Horrigan <23581@stu.lexrich5.org>, Olivia Fish <18082@stu.lexrich5.org>, Carmen Flores <39167@stu.lexrich5.org>, Maddox Nie <23767@stu.lexrich5.org>, Ki'Ree Pruitt <22500@stu.lexrich5.org>, Grace Ma <53160@stu.lexrich5.org>, Mustafa Azhar <28239@stu.lexrich5.org>, Lily DuBose <26490@stu.lexrich5.org>, Rachel Syracuse <20714@stu.lexrich5.org>, Lacey Graham <18181@stu.lexrich5.org>, Madison Etheredge <37423@stu.lexrich5.org>, Samiah Campbell <23294@stu.lexrich5.org>, Gental Htoo <28409@stu.lexrich5.org>, Mackenzie Elwood <44092@stu.lexrich5.org>, Ava Hair <27173@stu.lexrich5.org>, Khary Vinson <29941@stu.lexrich5.org>, Vanessa Weih <24351@stu.lexrich5.org>, Madison Inman <18007@stu.lexrich5.org>, Abigail Pouliot <20925@stu.lexrich5.org>, Norah Evans <40510@stu.lexrich5.org>, Emily McCauley <21836@stu.lexrich5.org>, Abigail Winn <49779@stu.lexrich5.org>, Skylar Laws <26416@stu.lexrich5.org>, Riya Hegde <20545@stu.lexrich5.org>, Emma Howard <30604@stu.lexrich5.org>, Tillman Bouknight <21076@stu.lexrich5.org>, Jordan Pollock <23536@stu.lexrich5.org>, Abby Morden <26636@stu.lexrich5.org>, Addison Godfrey <28232@stu.lexrich5.org>, Hayden Kirkland <20572@stu.lexrich5.org>, Mattie Cantrell <36294@stu.lexrich5.org>, Helene Hoang <35816@stu.lexrich5.org>, Bailey Johnson <18966@stu.lexrich5.org>, Kathryn Williams <18042@stu.lexrich5.org>, Heba Farhan <19187@stu.lexrich5.org>, Madeline Linder <23517@stu.lexrich5.org>, Karina Villavicencio <14076@stu.lexrich5.org>, Hewaud Khan <19113@stu.lexrich5.org>, Alina Brown <24191@stu.lexrich5.org>, Daniel Drayton <23446@stu.lexrich5.org>, Jocelyn Lemus <18095@stu.lexrich5.org>, Khloe Amburgey <47707@stu.lexrich5.org>, Max Nie <24089@stu.lexrich5.org>, Zaria Ward <34374@stu.lexrich5.org>, Amelia Barker <14054@stu.lexrich5.org>, Alyssa Parrott <18806@stu.lexrich5.org>, Joseph Eubanks <42277@stu.lexrich5.org>, Melissa Majewski <23520@stu.lexrich5.org>, Benjamin Godfrey <23677@stu.lexrich5.org>, Cole Theuerl <18142@stu.lexrich5.org>, David Dobbe <23474@stu.lexrich5.org>, Mariah Montgomery <20769@stu.lexrich5.org>, Connor Parks <24676@stu.lexrich5.org>, Elianna Miller-Martinez <44998@stu.lexrich5.org>, Hailey Richburg <18817@stu.lexrich5.org>, London Harper <35617@stu.lexrich5.org>, Hassaan Waheed <18336@stu.lexrich5.org>, Caroline Petruzzi <24862@stu.lexrich5.org>, Katherine Sipos <23378@stu.lexrich5.org>, Logan Rollins <17721@stu.lexrich5.org>, Tamya Morris <35094@stu.lexrich5.org>, Ramsey Green <18072@stu.lexrich5.org>, Anthony Fu <37469@stu.lexrich5.org>, Daniel Wang <28520@stu.lexrich5.org>, Tyler Jackson <23498@stu.lexrich5.org>, Jessica Mays <20444@stu.lexrich5.org>, Hampton Long <17748@stu.lexrich5.org>, Finley Strickland <20531@stu.lexrich5.org>, Khai Suan <18132@stu.lexrich5.org>, Jacob Klutz <18323@stu.lexrich5.org>, Kaitlyn Bingham <23467@stu.lexrich5.org>, Kyla Niles <27000@stu.lexrich5.org>, Meriella Holley <18006@stu.lexrich5.org>, Cleo Floyd-Johnstone <23534@stu.lexrich5.org>, Olivia Newman-Norlund <20777@stu.lexrich5.org>, Ariyan Oliver <23445@stu.lexrich5.org>, Brody Holm <16847@stu.lexrich5.org>, Kara Poore <18125@stu.lexrich5.org>, Olivia Li <50157@stu.lexrich5.org>, Taylor Washington <24196@stu.lexrich5.org>, Krupa Patel <23238@stu.lexrich5.org>, Adarsh Jagatheesan <33584@stu.lexrich5.org>, Kylie Pittman <18089@stu.lexrich5.org>, Lourde-saida Bazil <48769@stu.lexrich5.org>, Jessica Wang <18220@stu.lexrich5.org>, Zhixuan Xu <23676@stu.lexrich5.org>, Alanna Drinkwalter <30363@stu.lexrich5.org>, Riley Hunt <23507@stu.lexrich5.org>, Emmalee Posley <18111@stu.lexrich5.org>, Kathleen Tran <33536@stu.lexrich5.org>, Eva Bellamy <27048@stu.lexrich5.org>, Julie Drinkwalter <30362@stu.lexrich5.org>, Addison Jordan <14319@stu.lexrich5.org>, Ava Stanley <18198@stu.lexrich5.org>, Nathan Anderson <20991@stu.lexrich5.org>, Milan Townsend <41897@stu.lexrich5.org>, Jada White <42583@stu.lexrich5.org>, Meagan Evans <40511@stu.lexrich5.org>, Jade Cameron <17977@stu.lexrich5.org>, Alyssa Culver-Draper <18696@stu.lexrich5.org>, William Wang <18388@stu.lexrich5.org>, Taehoon Noh <28855@stu.lexrich5.org>, Prabhav Gudapati <21606@stu.lexrich5.org>, Conner Thatch <32853@stu.lexrich5.org>, Kaiyuan Xue <29774@stu.lexrich5.org>, Madison Washington <19962@stu.lexrich5.org>, Daniel Leuthner-Barrineau <38917@stu.lexrich5.org>, Tram Nguyen <44696@stu.lexrich5.org>, Thomas McKinney <20435@stu.lexrich5.org>"  # Keep the data here


output = {}

dataArray = data.split(",")

for entry in dataArray:
    name = entry.split(" <")[0].strip()
    id = entry.split(" <")[1].strip(">")
    
    id = id.replace("@stu.lexrich5.org", "")
    

    output[id] = name


jsonString = json.dumps(output, indent = 2)

print(jsonString)

database = open("databases/studentNames.json", "w")
database.write(jsonString)
database.close()
