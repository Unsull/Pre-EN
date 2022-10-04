
class Question:
    global score
    def quiz_game(user_name):

        questions = {
            "ล้างจานยังไงมือไม่เปียก?" : ["a.กินแล้วแช่", "b.ใช้สายยางฉีด", "c.ใส่ถุงมือ", "d.ใช้แปรงขัด", "a"],
            "ขนมอะไรกินแล้วตีหัวแตก?" : ["a.ขนมกล้วย", "b.ขนมชั้น", "c.ขนมเบื้อง", "d.ขนมครก", "b"],
            "ผักอะไร? น่าตกตะลึงที่สุด" : ["a.ผักกาด", "b.ผักปุ้ง", "c.ตำลึง", "d.โหระพา", "d"],
            "จังหวัดอะไรไม่มีกระเทียมกิน" : ["a.ตาก", "b.เชียงใหม่", "c.กระบี่", "d.พะเยา", "c"],
            "เกาะอะไร? เห็นฉันวิ่ง" : ["a.เกาะแม่กิน", "b.เกาะเต่า", "c.เกาะสิมิลัน", "d.เกาะรถ", "c"]
            } 

        score = 0 
        for question_number, question_main in enumerate(questions): 
            print ("Question",question_number+1) 
            print (question_main)

            for item in questions[question_main][:-1]: # เอาตั้งแต่ 0 ถึงก่อน -1(ตัวสุดท้าย)
                print (item)
            user_cull = input("Answer : ")
            user_cull = user_cull.lower()

            if user_cull == questions[question_main][-1]:
                print ("   ถูกต้องแล้วค้าบบบบ! ( ͡♥ 3 ͡♥)")
                if question_number+1 == 1:
                    print("เฉลย  --->>  กินแล้วแช่  ให้แม่ล้างให้")
                    score += 20

                elif question_number+1 == 2:
                    print("เฉลย  --->> ขนมชั้น  ไม่ใช้ขนมแก")
                    score += 20

                elif question_number+1 == 3:
                    print("เฉลย  --->> โหระพา  (โห้...ระพา)")
                    score += 20

                elif question_number+1 == 4:
                    print("เฉลย  --->> กระบี่  (กระบี่ไร้เทียมทาน)")
                    score += 20
                    
                elif question_number+1 == 5:
                    print("เฉลย  --->> เกาะสิมิลัน  (see me run)")
                    score += 20

            else: 
                print ("   ว้ายยยยผิด! ʕ - _ - ?")

                if question_number+1 == 1:
                    print("เฉลย  --->>  กินแล้วแช่  ให้แม่ล้างให้")

                elif question_number+1 == 2:
                    print("เฉลย  --->> ขนมชั้น  ไม่ใช้ขนมแก")
                            
                elif question_number+1 == 3:
                    print("เฉลย  --->> โหระพา  (โห้...ระพา)")
                                
                elif question_number+1 == 4:
                    print("เฉลย  --->> กระบี่  (กระบี่ไร้เทียมทาน)")
                    
                elif question_number+1 == 5:
                    print("เฉลย  --->> เกาะสิมิลัน  (see me run)")
                        

            print("•---------------♛---------------•")
            print()

        user = user_name
        score = str(score)
        with open('data_quiz.txt', 'a', encoding='utf8') as sc:
            sc.write("\n")
            sc.write(user + "  :  " + score + "   point")

        print(">>> Your score <<<")
        print(user, " : ", int(score), "  point")

        #with open('data_quiz.txt', 'r',) as sc:
        #    print(sc.read())


#quiz_game()
#print(score)
#user_name = "Irin"
#quizGame = Question
#quizGame.quiz_game(user_name)
